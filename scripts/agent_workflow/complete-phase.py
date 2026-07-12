"""Atomically complete a charla workflow phase after summary validation."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime
import hashlib
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


def _stale_sentinel_error(sentinel: Path, run_id: str, phase: str, attempt: int) -> str | None:
    if not sentinel.exists():
        return None
    try:
        payload = json.loads(sentinel.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return f"Stale sentinel cannot be safely replaced: {sentinel}"
    if not isinstance(payload, dict):
        return f"Stale sentinel cannot be safely replaced: {sentinel}"
    if (
        payload.get("run_id") != run_id
        or payload.get("phase") != phase
        or payload.get("attempt") != attempt
    ):
        return f"Stale sentinel belongs to a different run: {sentinel}"
    return f"Sentinel already exists for this run identity: {sentinel}"


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


def _write_snapshot_atomically_exclusive(path: Path, content: bytes) -> None:
    """Publish a durable summary snapshot without replacing historical evidence."""
    with tempfile.NamedTemporaryFile(
        mode="w+b", dir=path.parent, prefix=f".{path.name}.", suffix=".tmp", delete=False,
    ) as temporary:
        temporary.write(content)
        temporary.flush()
        os.fsync(temporary.fileno())
        temporary_path = Path(temporary.name)
    try:
        try:
            os.link(temporary_path, path)
        except FileExistsError as error:
            raise RuntimeError(f"Historical summary already exists: {path}") from error
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

    if not workflow_contract.is_valid_run_id(args.run_id):
        print("ERROR: Run ID must be a lowercase slug ending in -YYYYMMDD-HHMM")
        return 1

    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    summary_path = Path(args.summary).resolve()
    if summary_path.parent.name != "notes" or summary_path.name != "phase-summary.md":
        print("ERROR: --summary must resolve to <talk>/notes/phase-summary.md")
        return 1
    phase_contract = contract.get("phases", {}).get(args.phase)
    if phase_contract is None:
        print(f"ERROR: Unknown phase: {args.phase}")
        return 1
    if args.attempt <= 0:
        print("ERROR: Attempt must be a positive integer")
        return 1

    sentinel = summary_path.parent / phase_contract["sentinel"]
    with _sentinel_claim(sentinel):
        stale_error = _stale_sentinel_error(sentinel, args.run_id, args.phase, args.attempt)
        if stale_error:
            print(f"ERROR: {stale_error}")
            return 1

        summary_bytes = summary_path.read_bytes()
        summary = workflow_contract.parse_summary_text(summary_bytes.decode("utf-8"))
        errors = workflow_contract.validate_transition(summary, contract)
        errors.extend(workflow_contract.validate_publication(summary, contract, summary_path))
        errors.extend(_identity_errors(summary, args))
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1

        snapshot = summary_path.with_name(f"phase-summary.{args.run_id}.md")
        try:
            _write_snapshot_atomically_exclusive(snapshot, summary_bytes)
        except RuntimeError as error:
            print(f"ERROR: {error}")
            return 1

        payload = {
            "contract_version": contract["contract_version"],
            "run_id": args.run_id,
            "phase": args.phase,
            "attempt": args.attempt,
            "execution_status": _scalar(summary, "execution status"),
            "summary": f"{summary_path.parent.name}/{snapshot.name}",
            "summary_sha256": hashlib.sha256(summary_bytes).hexdigest(),
            "completed_at": datetime.now(launched_at.tzinfo).isoformat(),
        }
        if workflow_contract.is_identity_boundary(summary):
            payload.update({
                "worker_id": _scalar(summary, "worker id"),
                "session_id": _scalar(summary, "session id"),
            })
        if workflow_contract.is_compact_boundary(summary):
            payload.update({
                "workflow_mode": workflow_contract.COMPACT_WORKFLOW_MODE,
                "candidate_artifact": _scalar(summary, "candidate artifact"),
                "candidate_sha256": _scalar(summary, "candidate sha256"),
            })
        try:
            _write_atomically(sentinel, payload)
        except Exception:
            snapshot.unlink()
            raise
    print(f"COMPLETED: {sentinel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
