import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "agent_workflow" / "workflow_contract.py"
CLI_PATH = ROOT / "scripts" / "agent_workflow" / "validate-workflow.py"
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


if __name__ == "__main__":
    unittest.main()
