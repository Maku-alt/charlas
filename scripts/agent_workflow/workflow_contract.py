"""Validation helpers for the run-aware charla workflow contract."""

from __future__ import annotations

from datetime import datetime
import hashlib
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
COMPACT_BOUNDARY_PHASES = {"build", "review"}
IDENTITY_BOUNDARY_PHASES = {"build", "review", "build-fix", "review-final"}
WORKFLOW_MODES = {"full", "compact"}
COMPACT_WORKFLOW_MODE = "compact"


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


def is_compact_boundary(summary: dict[str, str]) -> bool:
    """Return whether this build/review summary opted into compact boundary gates."""
    return (
        _scalar(summary, "phase") in COMPACT_BOUNDARY_PHASES
        and _scalar(summary, "workflow mode").lower() == COMPACT_WORKFLOW_MODE
    )


def is_identity_boundary(summary: dict[str, str]) -> bool:
    """Return whether this phase must publish an execution identity."""
    return _scalar(summary, "phase") in IDENTITY_BOUNDARY_PHASES


def _candidate_path(summary: dict[str, str], summary_path: Path) -> Path | None:
    candidate = _scalar(summary, "candidate artifact")
    if not candidate or candidate == "none":
        return None
    path = (summary_path.parent.parent / candidate).resolve()
    talk_root = summary_path.parent.parent.resolve()
    try:
        path.relative_to(talk_root)
    except ValueError:
        return None
    return path


def _candidate_identity_errors(summary: dict[str, str], summary_path: Path) -> list[str]:
    errors: list[str] = []
    for field in ("worker id", "session id", "candidate sha256"):
        if not _scalar(summary, field):
            errors.append(f"Missing compact boundary field: {field}")
    candidate = _candidate_path(summary, summary_path)
    if candidate is None or not candidate.is_file():
        return [*errors, "Candidate artifact must be an existing file inside the talk directory"]
    actual_sha256 = hashlib.sha256(candidate.read_bytes()).hexdigest()
    if _scalar(summary, "candidate sha256") != actual_sha256:
        errors.append("Candidate SHA256 does not match the candidate artifact")
    return errors


def validate_compact_review_boundary(summary: dict[str, str], summary_path: Path) -> list[str]:
    """Validate the completed build handoff consumed by a compact review."""
    build_sentinel = summary_path.parent / ".phase-build.done"
    if not build_sentinel.is_file():
        return ["Compact review requires a completed build sentinel"]
    try:
        build = json.loads(build_sentinel.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ["Compact review build sentinel must contain valid JSON"]
    if not isinstance(build, dict) or build.get("phase") != "build":
        return ["Compact review requires a build sentinel"]
    if build.get("workflow_mode") != COMPACT_WORKFLOW_MODE:
        return ["Compact review requires a compact build sentinel"]

    review_identity = {
        "worker_id": _scalar(summary, "worker id"),
        "session_id": _scalar(summary, "session id"),
    }
    errors = validate_compact_review_independence(
        {"worker_id": str(build.get("worker_id", "")), "session_id": str(build.get("session_id", ""))},
        review_identity,
        independence_required=True,
    )
    if build.get("candidate_artifact") != _scalar(summary, "candidate artifact"):
        errors.append("Compact review candidate artifact does not match completed build")
    if build.get("candidate_sha256") != _scalar(summary, "candidate sha256"):
        errors.append("Compact review Candidate SHA256 does not match completed build")
    return errors


def _review_mode_errors(summary: dict[str, str], summary_path: Path) -> list[str]:
    """Reject a review whose mode differs from its completed build handoff."""
    if _scalar(summary, "phase") != "review":
        return []
    build_sentinel = summary_path.parent / ".phase-build.done"
    if not build_sentinel.is_file():
        return []
    try:
        build = json.loads(build_sentinel.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    if not isinstance(build, dict) or build.get("phase") != "build":
        return []
    build_mode = str(build.get("workflow_mode", "full")).lower()
    review_mode = _scalar(summary, "workflow mode").lower() or "full"
    if build_mode != review_mode:
        return ["Review workflow mode must match the completed build workflow mode"]
    return []


def _identity_boundary_errors(summary: dict[str, str], summary_path: Path) -> list[str]:
    """Require distinct build and review execution identities in every workflow mode."""
    phase = _scalar(summary, "phase")
    if phase not in IDENTITY_BOUNDARY_PHASES:
        return []

    errors = [
        f"Missing execution identity field: {field}"
        for field in ("worker id", "session id")
        if not _scalar(summary, field)
    ]
    predecessor = {"review": "build", "review-final": "build-fix"}.get(phase)
    if predecessor is None:
        return errors

    sentinel = summary_path.parent / f".phase-{predecessor}.done"
    if not sentinel.is_file():
        return [*errors, f"{phase} requires a completed {predecessor} sentinel"]
    try:
        previous = json.loads(sentinel.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return [*errors, f"{predecessor} sentinel must contain valid JSON"]
    if not isinstance(previous, dict) or previous.get("phase") != predecessor:
        return [*errors, f"{phase} requires a {predecessor} sentinel"]

    review_identity = {
        "worker_id": _scalar(summary, "worker id"),
        "session_id": _scalar(summary, "session id"),
    }
    errors.extend(validate_compact_review_independence(
        {
            "worker_id": str(previous.get("worker_id", "")),
            "session_id": str(previous.get("session_id", "")),
        },
        review_identity,
        independence_required=True,
    ))
    return errors


def validate_publication(summary: dict[str, str], contract: dict[str, Any], summary_path: Path) -> list[str]:
    """Validate runtime-bound build/review fields before a phase sentinel is published."""
    phase = _scalar(summary, "phase")
    errors = _identity_boundary_errors(summary, summary_path)
    errors.extend(_review_mode_errors(summary, summary_path))
    if not is_compact_boundary(summary):
        return errors
    errors.extend(_candidate_identity_errors(summary, summary_path))
    if phase == "review":
        errors.extend(validate_compact_review_boundary(summary, summary_path))
    return errors


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
    execution_status = _scalar(summary, "execution status")
    decision = _scalar(summary, "decision")
    if execution_status not in contract.get("execution_statuses", []):
        errors.append("Invalid execution status")
    if decision not in contract.get("decisions", []):
        errors.append("Invalid decision")
    workflow_mode = _scalar(summary, "workflow mode").lower()
    if workflow_mode and workflow_mode not in WORKFLOW_MODES:
        errors.append("Invalid workflow mode")

    verdict = _scalar(summary, "review verdict")
    if verdict not in contract.get("review_verdicts", []):
        errors.append("Invalid review verdict")
    if not phase.startswith("review") and verdict != "not_applicable":
        errors.append("Non-review phases require review verdict not_applicable")
    if execution_status == "blocked":
        if decision not in {"return", "stop"}:
            errors.append("Blocked phase must return or stop")
        if verdict != "not_applicable":
            errors.append("Blocked phase requires review verdict not_applicable")

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

    if is_identity_boundary(summary):
        for sentinel_field, summary_field in (
            ("worker_id", "worker id"),
            ("session_id", "session id"),
        ):
            if values.get(sentinel_field) != _scalar(summary, summary_field):
                errors.append(f"Sentinel {sentinel_field.replace('_', ' ')} does not match summary")

    if is_compact_boundary(summary):
        for sentinel_field, summary_field in (
            ("workflow_mode", "workflow mode"),
            ("candidate_artifact", "candidate artifact"),
            ("candidate_sha256", "candidate sha256"),
        ):
            if values.get(sentinel_field) != _scalar(summary, summary_field):
                errors.append(f"Sentinel {sentinel_field.replace('_', ' ')} does not match summary")

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
    errors.extend(validate_publication(summary, contract, summary_path))
    phase = _scalar(summary, "phase")
    phase_contract = contract.get("phases", {}).get(phase)
    if phase_contract:
        expected = summary_path.parent / phase_contract["sentinel"]
        errors.extend(_validate_sentinel(summary, sentinel or expected, contract, summary_path))
    return errors


def validate_summary(path: str | Path, contract: dict[str, Any]) -> list[str]:
    """Validate a phase summary and the phase sentinel beside it."""
    return _validate_summary(path, contract)


def validate_migrated_summary(path: str | Path, contract: dict[str, Any]) -> list[str]:
    """Validate v2 metadata migrated from a prior run without a new sentinel."""
    summary_path = Path(path)
    summary = parse_summary(summary_path)
    errors = validate_transition(summary, contract)
    phase = _scalar(summary, "phase")
    if _scalar(summary, "decision") == "iterate" and _scalar(summary, "next phase") == phase:
        errors = [error for error in errors if not error.startswith("Next phase ")]
    errors.extend(validate_publication(summary, contract, summary_path))
    return errors
