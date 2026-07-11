"""Atomically complete a charla workflow phase after summary validation."""

from __future__ import annotations

import argparse
from datetime import datetime
import importlib.util
import json
import os
from pathlib import Path
import tempfile


MODULE = Path(__file__).with_name("workflow_contract.py")
SPEC = importlib.util.spec_from_file_location("workflow_contract", MODULE)
workflow_contract = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(workflow_contract)


def _scalar(summary: dict[str, str], name: str) -> str:
    value = summary.get(name, "").strip()
    return value.splitlines()[0].strip() if value else ""


def _identity_errors(summary: dict[str, str], args: argparse.Namespace) -> list[str]:
    expected = {
        "run id": args.run_id,
        "phase": args.phase,
        "attempt": str(args.attempt),
    }
    return [
        f"Summary {field} does not match command argument"
        for field, value in expected.items()
        if _scalar(summary, field) != value
    ]


def _stale_sentinel_error(sentinel: Path, run_id: str) -> str | None:
    if not sentinel.exists():
        return None
    try:
        payload = json.loads(sentinel.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return f"Stale sentinel cannot be safely replaced: {sentinel}"
    if not isinstance(payload, dict) or payload.get("run_id") != run_id:
        return f"Stale sentinel belongs to a different run: {sentinel}"
    return None


def _write_atomically(sentinel: Path, payload: dict[str, object]) -> None:
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=sentinel.parent, prefix=f".{sentinel.name}.", suffix=".tmp", delete=False,
    ) as temporary:
        json.dump(payload, temporary)
        temporary.write("\n")
        temporary_path = Path(temporary.name)
    try:
        os.replace(temporary_path, sentinel)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--phase", required=True)
    parser.add_argument("--attempt", required=True, type=int)
    parser.add_argument("--launched-at", required=True)
    args = parser.parse_args()

    try:
        launched_at = datetime.fromisoformat(args.launched_at)
        if launched_at.tzinfo is None:
            raise ValueError
    except ValueError:
        print("ERROR: --launched-at must be an ISO 8601 timestamp with timezone")
        return 1

    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    summary_path = Path(args.summary)
    summary = workflow_contract.parse_summary(summary_path)
    errors = workflow_contract.validate_transition(summary, contract)
    errors.extend(_identity_errors(summary, args))
    phase_contract = contract.get("phases", {}).get(args.phase)
    if phase_contract is None:
        errors.append(f"Unknown phase: {args.phase}")
    if args.attempt <= 0:
        errors.append("Attempt must be a positive integer")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    sentinel = summary_path.parent / phase_contract["sentinel"]
    stale_error = _stale_sentinel_error(sentinel, args.run_id)
    if stale_error:
        print(f"ERROR: {stale_error}")
        return 1

    payload = {
        "contract_version": contract["contract_version"],
        "run_id": args.run_id,
        "phase": args.phase,
        "attempt": args.attempt,
        "execution_status": _scalar(summary, "execution status"),
        "summary": f"{summary_path.parent.name}/{summary_path.name}",
        "completed_at": datetime.now(launched_at.tzinfo).isoformat(),
    }
    _write_atomically(sentinel, payload)
    print(f"COMPLETED: {sentinel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
