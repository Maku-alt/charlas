import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "agent_workflow" / "workflow_contract.py"
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
        sentinel.write_text("run_id: review-contract-20260710-1200\nattempt: 1\n", encoding="utf-8")
        now = datetime.now().timestamp()
        os.utime(sentinel, (now, now))
        self.addCleanup(temp_dir.cleanup)
        return summary, sentinel

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

    def test_allowed_next_phase_is_accepted(self):
        summary, _ = self.copy_valid_summary()
        self.assertEqual([], self.workflow_contract.validate_summary(summary, self.contract))

    def test_attempt_must_be_positive(self):
        summary, _ = self.copy_valid_summary()
        summary.write_text(summary.read_text(encoding="utf-8").replace("## Attempt\n1", "## Attempt\n0"), encoding="utf-8")
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("Attempt" in error and "positive" in error for error in errors))

    def test_sentinel_run_id_and_attempt_must_match_summary(self):
        summary, sentinel = self.copy_valid_summary()
        sentinel.write_text("run_id: wrong-run-20260710-1200\nattempt: 2\n", encoding="utf-8")
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("Sentinel run ID" in error for error in errors))
        self.assertTrue(any("Sentinel attempt" in error for error in errors))

    def test_sentinel_mtime_cannot_precede_run_launch(self):
        summary, sentinel = self.copy_valid_summary()
        sentinel.write_text("run_id: review-contract-20260710-1200\nattempt: 1\n", encoding="utf-8")
        before_launch = datetime(2026, 7, 10, 11, 59).timestamp()
        os.utime(sentinel, (before_launch, before_launch))
        errors = self.workflow_contract.validate_summary(summary, self.contract)
        self.assertTrue(any("before run launch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
