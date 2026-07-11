"""Atomically complete a charla workflow phase after summary validation."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
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


@contextmanager
def _sentinel_claim(sentinel: Path):
    """Serialize stale-sentinel validation and publication for one phase."""
    lock_path = sentinel.parent / f"{sentinel.name}.lock"
    with lock_path.open("a+b") as lock:
        lock.seek(0)
        lock.write(b"0")
        lock.flush()
        lock.seek(0)
        try:
            import msvcrt

            msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
            unlock = lambda: msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
        except ImportError:
            import fcntl

            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
            unlock = lambda: fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
        try:
            yield
        finally:
            lock.seek(0)
            unlock()


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
    summary_path = Path(args.summary).resolve()
    if summary_path.parent.name != "notes" or summary_path.name != "phase-summary.md":
        print("ERROR: --summary must resolve to <talk>/notes/phase-summary.md")
        return 1
    summary = workflow_contract.parse_summary(summary_path)
    errors = workflow_contract.validate_transition(summary, contract)
    errors.extend(workflow_contract.validate_publication(summary, contract, summary_path))
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
    with _sentinel_claim(sentinel):
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
        if args.phase in workflow_contract.COMPACT_BOUNDARY_PHASES:
            payload.update({
                "worker_id": _scalar(summary, "worker id"),
                "session_id": _scalar(summary, "session id"),
                "candidate_artifact": _scalar(summary, "candidate artifact"),
                "candidate_sha256": _scalar(summary, "candidate sha256"),
            })
        _write_atomically(sentinel, payload)
    print(f"COMPLETED: {sentinel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
