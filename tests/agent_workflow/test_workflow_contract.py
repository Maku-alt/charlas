import importlib.util
import json
import msvcrt
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "agent_workflow" / "workflow_contract.py"
CLI_PATH = ROOT / "scripts" / "agent_workflow" / "validate-workflow.py"
COMPLETE_PHASE_PATH = ROOT / "scripts" / "agent_workflow" / "complete-phase.py"
FIXTURES = Path(__file__).parent / "fixtures"


def load_module():
    spec = importlib.util.spec_from_file_location("workflow_contract", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WorkflowContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads((ROOT / "agents" / "workflow-contract.json").read_text(encoding="utf-8"))
        cls.workflow_contract = load_module()

    def copy_valid_summary(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        shutil.copy(FIXTURES / "valid-phase-summary.md", summary)
        sentinel = notes / ".phase-review-final.done"
        self.write_sentinel(summary, sentinel, "review-final")
        self.addCleanup(temp_dir.cleanup)
        return summary, sentinel

    def write_sentinel(self, summary_path, sentinel, phase_name, **overrides):
        payload = {
            "contract_version": 2,
            "run_id": "review-contract-20260710-1200",
            "phase": phase_name,
            "attempt": 1,
            "execution_status": "completed",
            "summary": "notes/phase-summary.md",
        }
        payload.update(overrides)
        sentinel.write_text(json.dumps(payload), encoding="utf-8")
        now = datetime.now().timestamp()
        os.utime(sentinel, (now, now))

    def complete_phase_command(self, summary, **overrides):
        arguments = {
            "run_id": "review-contract-20260710-1200",
            "phase": "review-final",
            "attempt": "1",
            "launched_at": "2026-07-10T12:00:00-05:00",
        }
        arguments.update(overrides)
        return [
            sys.executable, str(COMPLETE_PHASE_PATH),
            "--contract", str(ROOT / "agents" / "workflow-contract.json"),
            "--summary", str(summary),
            "--run-id", arguments["run_id"],
            "--phase", arguments["phase"],
            "--attempt", arguments["attempt"],
            "--launched-at", arguments["launched_at"],
        ]

    def complete_phase(self, summary, **overrides):
        return subprocess.run(
            self.complete_phase_command(summary, **overrides),
            capture_output=True, text=True, check=False,
        )

    def hold_publish_lock(self, sentinel):
        lock_path = sentinel.parent / f"{sentinel.name}.lock"
        lock = lock_path.open("a+b")
        lock.seek(0)
        lock.write(b"0")
        lock.flush()
        lock.seek(0)
        msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
        self.addCleanup(lambda: lock_path.unlink(missing_ok=True))
        self.addCleanup(lock.close)
        return lock

    def test_valid_summary_has_no_errors(self):
        summary, _ = self.copy_valid_summary()
        self.assertEqual([], self.workflow_contract.validate_summary(summary, self.contract))

    def test_unknown_phase_is_rejected(self):
        summary, _ = self.copy_valid_summary()
        summary.write_text(summary.read_text(encoding="utf-8").replace("## Phase\nreview-final", "## Phase\nunknown"), encoding="utf-8")
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("unknown phase" in error.lower() for error in errors))

    def test_approved_review_must_advance_to_release_or_finish(self):
        summary, _ = self.copy_valid_summary()
        text = summary.read_text(encoding="utf-8").replace("## Next phase\nrelease", "## Next phase\nbuild-fix")
        summary.write_text(text, encoding="utf-8")
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("approved review" in error for error in errors))

    def test_non_review_phase_requires_not_applicable_verdict(self):
        summary, _ = self.copy_valid_summary()
        text = summary.read_text(encoding="utf-8").replace("## Phase\nreview-final", "## Phase\nbuild").replace("## Review verdict\napproved", "## Review verdict\nrequires_changes").replace("## Next phase\nrelease", "## Next phase\nreview")
        summary.write_text(text, encoding="utf-8")
        (summary.parent / ".phase-build.done").touch()
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("not_applicable" in error for error in errors))

    def test_next_phase_must_be_allowed_transition(self):
        summary, _ = self.copy_valid_summary()
        summary.write_text(
            summary.read_text(encoding="utf-8")
            .replace("## Phase\nreview-final", "## Phase\nnarrative")
            .replace("## Review verdict\napproved", "## Review verdict\nnot_applicable")
            .replace("## Next phase\nrelease", "## Next phase\nbuild"),
            encoding="utf-8",
        )
        sentinel = summary.parent / ".phase-narrative.done"
        self.write_sentinel(summary, sentinel, "narrative")
        self.assertEqual([], self.workflow_contract.validate_summary(summary, self.contract))

    def test_attempt_must_be_positive(self):
        summary, _ = self.copy_valid_summary()
        summary.write_text(summary.read_text(encoding="utf-8").replace("## Attempt\n1", "## Attempt\n0"), encoding="utf-8")
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("Attempt" in error and "positive" in error for error in errors))

    def test_sentinel_run_id_and_attempt_must_match_summary(self):
        summary, sentinel = self.copy_valid_summary()
        self.write_sentinel(summary, sentinel, "review-final", run_id="wrong-run-20260710-1200", attempt=2)
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("sentinel run id" in error.lower() for error in errors))
        self.assertTrue(any("sentinel attempt" in error.lower() for error in errors))

    def test_sentinel_mtime_cannot_precede_run_launch(self):
        summary, sentinel = self.copy_valid_summary()
        before_launch = datetime(2026, 7, 10, 11, 59).timestamp()
        os.utime(sentinel, (before_launch, before_launch))
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("before run launch" in error for error in errors))

    def test_sentinel_json_identity_fields_must_match_summary(self):
        summary, sentinel = self.copy_valid_summary()
        mismatches = {
            "contract_version": 99,
            "run_id": "wrong-run-20260710-1200",
            "phase": "review",
            "attempt": 2,
            "execution_status": "blocked",
            "summary": "notes/other-summary.md",
        }
        for field, value in mismatches.items():
            with self.subTest(field=field):
                self.write_sentinel(summary, sentinel, "review-final", **{field: value})
                errors = self.workflow_contract.validate_summary(summary, self.contract)
                self.assertTrue(any(field.replace("_", " ") in error.lower() for error in errors))

    def test_cli_prints_valid_and_exits_zero_for_valid_summary(self):
        summary, sentinel = self.copy_valid_summary()
        result = subprocess.run(
            [sys.executable, str(CLI_PATH), "--contract", str(ROOT / "agents" / "workflow-contract.json"),
             "--summary", str(summary), "--sentinel", str(sentinel)],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(0, result.returncode)
        self.assertEqual("VALID", result.stdout.strip())

    def test_cli_prints_errors_and_exits_one_for_invalid_summary(self):
        summary, sentinel = self.copy_valid_summary()
        summary.write_text(summary.read_text(encoding="utf-8").replace("## Attempt\n1", "## Attempt\n0"), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(CLI_PATH), "--contract", str(ROOT / "agents" / "workflow-contract.json"),
             "--summary", str(summary), "--sentinel", str(sentinel)],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("ERROR:", result.stdout)

    def test_complete_phase_writes_sentinel_after_valid_summary(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        shutil.copy(FIXTURES / "valid-phase-summary.md", summary)
        self.addCleanup(temp_dir.cleanup)

        result = self.complete_phase(summary)

        sentinel = notes / ".phase-review-final.done"
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(sentinel.is_file())
        payload = json.loads(sentinel.read_text(encoding="utf-8"))
        self.assertEqual(2, payload["contract_version"])
        self.assertEqual("review-contract-20260710-1200", payload["run_id"])
        self.assertEqual("review-final", payload["phase"])
        self.assertEqual(1, payload["attempt"])
        self.assertEqual("completed", payload["execution_status"])
        self.assertEqual("notes/phase-summary.md", payload["summary"])
        self.assertIn("completed_at", payload)
        self.assertEqual([], self.workflow_contract.validate_summary(summary, self.contract))

    def test_complete_phase_does_not_write_sentinel_for_invalid_summary(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        invalid = (FIXTURES / "valid-phase-summary.md").read_text(encoding="utf-8").replace(
            "## Attempt\n1", "## Attempt\n0"
        )
        summary.write_text(invalid, encoding="utf-8")
        self.addCleanup(temp_dir.cleanup)

        result = self.complete_phase(summary)

        self.assertEqual(1, result.returncode)
        self.assertIn("ERROR:", result.stdout)
        self.assertFalse((notes / ".phase-review-final.done").exists())

    def test_complete_phase_rejects_stale_sentinel_from_other_run(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        shutil.copy(FIXTURES / "valid-phase-summary.md", summary)
        sentinel = notes / ".phase-review-final.done"
        self.write_sentinel(summary, sentinel, "review-final", run_id="old-run-20260709-1200")
        self.addCleanup(temp_dir.cleanup)

        result = self.complete_phase(summary)

        self.assertEqual(1, result.returncode)
        self.assertIn("stale", result.stdout.lower())
        self.assertEqual("old-run-20260709-1200", json.loads(sentinel.read_text(encoding="utf-8"))["run_id"])

    def test_complete_phase_rejects_sentinel_claimed_by_other_run_during_publish(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        shutil.copy(FIXTURES / "valid-phase-summary.md", summary)
        sentinel = notes / ".phase-review-final.done"
        self.addCleanup(temp_dir.cleanup)
        lock = self.hold_publish_lock(sentinel)

        process = subprocess.Popen(self.complete_phase_command(summary), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        time.sleep(0.2)
        waiting = process.poll() is None
        try:
            self.write_sentinel(summary, sentinel, "review-final", run_id="old-run-20260709-1200")
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
        stdout, stderr = process.communicate(timeout=5)

        self.assertTrue(waiting, "publisher should wait for the sentinel claim")
        self.assertEqual(1, process.returncode, stderr)
        self.assertIn("stale", stdout.lower())
        self.assertEqual("old-run-20260709-1200", json.loads(sentinel.read_text(encoding="utf-8"))["run_id"])

    def test_complete_phase_rejects_noncanonical_summary_path(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "review-summary.md"
        shutil.copy(FIXTURES / "valid-phase-summary.md", summary)
        self.addCleanup(temp_dir.cleanup)

        result = self.complete_phase(summary)

        self.assertEqual(1, result.returncode)
        self.assertIn("notes/phase-summary.md", result.stdout)
        self.assertFalse((notes / ".phase-review-final.done").exists())

    def test_advisor_is_auxiliary_and_not_a_phase(self):
        advisor = self.contract["auxiliary_roles"]["advisor-charlas"]
        self.assertNotIn("advisor-charlas", self.contract["phases"])
        self.assertEqual("agents/advisor-charlas.md", advisor["role"])
        self.assertEqual(
            "templates/charlas-sdd/advisor-request.md",
            advisor["request_template"],
        )
        self.assertEqual("templates/charlas-sdd/prompts/run-advisor.md", advisor["prompt"])

    def test_advisor_has_no_transition_or_gate_authority(self):
        advisor = self.contract["auxiliary_roles"]["advisor-charlas"]
        self.assertFalse(advisor["owns_phase"])
        self.assertFalse(advisor["may_approve"])
        self.assertFalse(advisor["may_block"])
        self.assertNotIn("next", advisor)
        self.assertNotIn("advisor-charlas", {
            next_phase
            for phase in self.contract["phases"].values()
            for next_phase in phase["next"]
        })

    def test_advisor_cannot_write_phase_summary_or_mutate_artifacts(self):
        advisor = self.contract["auxiliary_roles"]["advisor-charlas"]
        role = (ROOT / advisor["role"]).read_text(encoding="utf-8")
        self.assertFalse(advisor["may_modify_artifacts"])
        self.assertFalse(advisor["may_write_phase_summary"])
        self.assertIn("No modifica", role)
        self.assertIn("no escribe `notes/phase-summary.md`", role)

    def test_advisor_request_requires_a_concrete_decision(self):
        request = (ROOT / "templates" / "charlas-sdd" / "advisor-request.md").read_text(encoding="utf-8")
        self.assertIn("## decision question", request)
        self.assertIn("concreta", request)
        self.assertIn("## current phase", request)
        self.assertIn("## affected phases", request)
        self.assertIn("## alternatives already considered", request)

    def test_advisor_output_records_assumptions_options_tradeoffs_and_recommendation(self):
        role = (ROOT / "agents" / "advisor-charlas.md").read_text(encoding="utf-8")
        for field in (
            "Recommendation",
            "Why",
            "Alternatives considered",
            "Tradeoffs",
            "Assumptions",
            "Risks",
            "Evidence paths",
            "Confidence",
            "Decision owner: orchestrator",
        ):
            with self.subTest(field=field):
                self.assertIn(field, role)

    def test_advisor_sentinel_matches_request_run_id(self):
        request = (ROOT / "templates" / "charlas-sdd" / "advisor-request.md").read_text(encoding="utf-8")
        prompt = (ROOT / "templates" / "charlas-sdd" / "prompts" / "run-advisor.md").read_text(encoding="utf-8")
        self.assertIn("<talk>/notes/advice/<run-id>-advisor.md", request)
        self.assertIn("<talk>/notes/advice/.advisor-<run-id>.done", request)
        self.assertIn("request `run_id`", request)
        self.assertIn("actual model", request)
        self.assertIn("completion timestamp", request)
        self.assertIn("run-aware advisory sentinel", prompt)

    def test_phase_asset_check_requires_worker_role_spec_and_prompt_but_allows_embedded_release(self):
        contract_path = ROOT / "agents" / ".task-7-workflow-contract.json"
        contract = json.loads((ROOT / "agents" / "workflow-contract.json").read_text(encoding="utf-8"))
        contract["phases"]["image-close"]["spec"] = "missing-image-spec.md"
        contract_path.write_text(json.dumps(contract), encoding="utf-8")
        self.addCleanup(contract_path.unlink, missing_ok=True)

        result = subprocess.run(
            [sys.executable, str(CLI_PATH), "--contract", str(contract_path), "--check-phase-assets"],
            capture_output=True, text=True, check=False,
        )

        self.assertEqual(1, result.returncode)
        self.assertIn("Phase image-close references missing spec", result.stdout)

        result = subprocess.run(
            [sys.executable, str(CLI_PATH), "--check-phase-assets"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VALID ORCHESTRATOR RELEASE release", result.stdout)

    def test_phase_asset_check_rejects_nonexistent_canonical_role(self):
        contract_path = ROOT / "agents" / ".task-7-role-contract.json"
        contract = json.loads((ROOT / "agents" / "workflow-contract.json").read_text(encoding="utf-8"))
        contract["phases"]["research"]["role"] = "missing-charlas"
        contract_path.write_text(json.dumps(contract), encoding="utf-8")
        self.addCleanup(contract_path.unlink, missing_ok=True)

        result = subprocess.run(
            [sys.executable, str(CLI_PATH), "--contract", str(contract_path), "--check-phase-assets"],
            capture_output=True, text=True, check=False,
        )

        self.assertEqual(1, result.returncode)
        self.assertIn("Phase research references missing role", result.stdout)

    def test_phase_asset_check_rejects_missing_or_not_applicable_worker_prompt(self):
        for prompt, expected in (
            ("missing-prompt.md", "references missing prompt"),
            ("not_applicable", "may use prompt not_applicable only for release"),
        ):
            with self.subTest(prompt=prompt):
                contract_path = ROOT / "agents" / f".task-7-prompt-{prompt.replace('.', '-')}.json"
                contract = json.loads((ROOT / "agents" / "workflow-contract.json").read_text(encoding="utf-8"))
                contract["phases"]["research"]["prompt"] = prompt
                contract_path.write_text(json.dumps(contract), encoding="utf-8")
                self.addCleanup(contract_path.unlink, missing_ok=True)

                result = subprocess.run(
                    [sys.executable, str(CLI_PATH), "--contract", str(contract_path), "--check-phase-assets"],
                    capture_output=True, text=True, check=False,
                )

                self.assertEqual(1, result.returncode)
                self.assertIn(f"Phase research {expected}", result.stdout)

    def test_compact_review_must_use_a_distinct_worker_and_session_from_build(self):
        build = {"worker_id": "builder-7", "session_id": "build-session-12"}

        for review, expected in (
            ({"worker_id": "builder-7", "session_id": "review-session-13"}, "worker_id"),
            ({"worker_id": "reviewer-8", "session_id": "build-session-12"}, "session_id"),
        ):
            with self.subTest(review=review):
                errors = self.workflow_contract.validate_compact_review_independence(
                    build,
                    review,
                    independence_required=True,
                )
                self.assertTrue(any(expected in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
