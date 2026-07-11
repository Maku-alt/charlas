"""Validation helpers for the run-aware charla workflow contract."""

from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import re
from typing import Any


REQUIRED_FIELDS = (
    "contract version", "run id", "attempt", "phase", "execution status",
    "decision", "review verdict", "summary", "artifacts", "evidence",
    "candidate artifact", "final artifact", "blocking findings", "next phase",
    "next action",
)
ARTIFACT_PHASES = {"build", "review", "review-final", "build-fix"}


def validate_compact_review_independence(
    build_identity: dict[str, str],
    review_identity: dict[str, str],
    *,
    independence_required: bool,
) -> list[str]:
    """Reject compact review identity reuse when an independent review is required."""
    if not independence_required:
        return []

    errors: list[str] = []
    for field in ("worker_id", "session_id"):
        build_value = build_identity.get(field, "").strip()
        review_value = review_identity.get(field, "").strip()
        if build_value and build_value == review_value:
            errors.append(
                f"Compact review {field} must differ from compact build when independence is required"
            )
    return errors


def parse_summary(path: str | Path) -> dict[str, str]:
    """Return normalized H2 Markdown blocks from a phase summary."""
    text = Path(path).read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^## +(.+?)\s*$", text)
    return {
        blocks[index].strip().lower(): blocks[index + 1].strip()
        for index in range(1, len(blocks), 2)
    }


def _value(summary: dict[str, str], name: str) -> str:
    return summary.get(name, "").strip()


def _scalar(summary: dict[str, str], name: str) -> str:
    return _value(summary, name).splitlines()[0].strip() if _value(summary, name) else ""


def validate_transition(summary: dict[str, str], contract: dict[str, Any]) -> list[str]:
    """Validate phase, enum, transition, review, and artifact coherence."""
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if not _value(summary, field):
            errors.append(f"Missing required field: {field}")

    phase = _scalar(summary, "phase")
    phases = contract.get("phases", {})
    if phase not in phases:
        errors.append(f"Unknown phase: {phase or '<missing>'}")
        return errors

    if _scalar(summary, "contract version") != str(contract.get("contract_version")):
        errors.append("Contract version does not match workflow contract")
    if _scalar(summary, "execution status") not in contract.get("execution_statuses", []):
        errors.append("Invalid execution status")
    if _scalar(summary, "decision") not in contract.get("decisions", []):
        errors.append("Invalid decision")

    verdict = _scalar(summary, "review verdict")
    if verdict not in contract.get("review_verdicts", []):
        errors.append("Invalid review verdict")
    if not phase.startswith("review") and verdict != "not_applicable":
        errors.append("Non-review phases require review verdict not_applicable")

    attempt = _scalar(summary, "attempt")
    if not attempt.isdigit() or int(attempt) <= 0:
        errors.append("Attempt must be a positive integer")

    next_phase = _scalar(summary, "next phase")
    allowed = phases[phase].get("next", [])
    if next_phase not in {"none", ""} and next_phase not in allowed:
        errors.append(f"Next phase {next_phase!r} is not allowed from {phase!r}")
    if phase.startswith("review") and verdict == "approved" and next_phase not in {"release", "none"}:
        errors.append("An approved review must advance to release or finish")
    if phase.startswith("review") and verdict == "requires_changes" and next_phase in {"release", "none"}:
        errors.append("A review requiring changes must route to corrective work")

    if phase in ARTIFACT_PHASES and _scalar(summary, "candidate artifact") == "none":
        errors.append(f"Phase {phase!r} requires a candidate artifact")
    if phase == "release" and _scalar(summary, "final artifact") == "none":
        errors.append("Release requires a final artifact")
    if _value(summary, "artifacts") in {"none", "- none"}:
        errors.append("Artifacts must list at least one artifact")
    if _value(summary, "evidence") in {"none", "- none"}:
        errors.append("Evidence must list at least one evidence artifact")
    return errors


def _run_launch_timestamp(run_id: str) -> float | None:
    match = re.search(r"-(\d{8})-(\d{4})$", run_id)
    if not match:
        return None
    return datetime.strptime("".join(match.groups()), "%Y%m%d%H%M").timestamp()


def _validate_sentinel(
    summary: dict[str, str], sentinel: Path, contract: dict[str, Any], summary_path: Path,
) -> list[str]:
    errors: list[str] = []
    if not sentinel.is_file():
        return [f"Missing sentinel: {sentinel}"]
    try:
        values = json.loads(sentinel.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ["Sentinel must contain valid JSON"]
    if not isinstance(values, dict):
        return ["Sentinel must contain a JSON object"]

    expected = {
        "contract_version": contract.get("contract_version"),
        "run_id": _scalar(summary, "run id"),
        "phase": _scalar(summary, "phase"),
        "attempt": int(_scalar(summary, "attempt")) if _scalar(summary, "attempt").isdigit() else None,
        "execution_status": _scalar(summary, "execution status"),
        "summary": f"{summary_path.parent.name}/{summary_path.name}",
    }
    for field, expected_value in expected.items():
        if values.get(field) != expected_value:
            errors.append(f"Sentinel {field.replace('_', ' ')} does not match summary")

    run_id = expected["run_id"]
    launch = _run_launch_timestamp(run_id)
    if launch is None:
        errors.append("Run ID must end in -YYYYMMDD-HHMM")
    elif sentinel.stat().st_mtime < launch:
        errors.append("Sentinel mtime is before run launch")
    return errors


def _validate_summary(path: str | Path, contract: dict[str, Any], sentinel: Path | None = None) -> list[str]:
    summary_path = Path(path)
    summary = parse_summary(summary_path)
    errors = validate_transition(summary, contract)
    phase = _scalar(summary, "phase")
    phase_contract = contract.get("phases", {}).get(phase)
    if phase_contract:
        expected = summary_path.parent / phase_contract["sentinel"]
        errors.extend(_validate_sentinel(summary, sentinel or expected, contract, summary_path))
    return errors


def validate_summary(path: str | Path, contract: dict[str, Any]) -> list[str]:
    """Validate a phase summary and the phase sentinel beside it."""
    return _validate_summary(path, contract)
