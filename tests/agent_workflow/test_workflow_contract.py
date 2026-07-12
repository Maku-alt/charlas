import importlib.util
import hashlib
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
        self.write_valid_review_final(summary)
        sentinel = notes / ".phase-review-final.done"
        self.write_sentinel(
            summary,
            sentinel,
            "review-final",
            worker_id="reviewer-8",
            session_id="review-session-13",
        )
        self.addCleanup(temp_dir.cleanup)
        return summary, sentinel

    def write_valid_review_final(self, summary):
        shutil.copy(FIXTURES / "valid-phase-summary.md", summary)
        self.write_sentinel(
            summary,
            summary.parent / ".phase-build-fix.done",
            "build-fix",
            worker_id="builder-7",
            session_id="build-session-12",
        )

    def write_sentinel(self, summary_path, sentinel, phase_name, **overrides):
        payload = {
            "contract_version": 2,
            "run_id": "review-contract-20260710-1200",
            "phase": phase_name,
            "attempt": 1,
            "execution_status": "completed",
            "summary": "notes/phase-summary.md",
            "completed_at": "2026-07-10T12:05:00-05:00",
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

    def write_compact_phase_summary(
        self, summary, *, phase, worker_id, session_id, candidate_sha256,
    ):
        review_verdict = "not_applicable" if phase == "build" else "requires_changes"
        next_phase = "review" if phase == "build" else "build-fix"
        text = (FIXTURES / "valid-phase-summary.md").read_text(encoding="utf-8")
        text = text.replace("## Phase\nreview-final", f"## Phase\n{phase}")
        text = text.replace("## Review verdict\napproved", f"## Review verdict\n{review_verdict}")
        text = text.replace("## Next phase\nrelease", f"## Next phase\n{next_phase}")
        text = text.replace(
            "## Candidate artifact\nslides/candidate.pptx",
            "## Candidate artifact\nslides/candidate.pptx"
            f"\n\n## Candidate SHA256\n{candidate_sha256}"
            f"\n\n## Worker ID\n{worker_id}"
            f"\n\n## Session ID\n{session_id}"
            "\n\n## Workflow mode\ncompact",
        )
        summary.write_text(text, encoding="utf-8")

    def publish_compact_build(self, summary, candidate, *, worker_id="builder-7", session_id="build-session-12"):
        candidate.parent.mkdir(exist_ok=True)
        candidate.write_bytes(b"compact candidate")
        candidate_sha256 = hashlib.sha256(candidate.read_bytes()).hexdigest()
        self.write_compact_phase_summary(
            summary,
            phase="build",
            worker_id=worker_id,
            session_id=session_id,
            candidate_sha256=candidate_sha256,
        )
        result = self.complete_phase(summary, phase="build")
        self.assertEqual(0, result.returncode, result.stdout)
        return candidate_sha256

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

    def test_blocked_phase_cannot_advance_or_report_approved_review(self):
        summary, _ = self.copy_valid_summary()
        summary.write_text(
            summary.read_text(encoding="utf-8").replace(
                "## Execution status\ncompleted", "## Execution status\nblocked"
            ),
            encoding="utf-8",
        )

        errors = self.workflow_contract.validate_transition(
            self.workflow_contract.parse_summary(summary), self.contract
        )

        self.assertTrue(any("Blocked phase" in error for error in errors), errors)

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

    def test_published_sentinel_requires_every_contract_field_and_valid_completion_timestamp(self):
        for mutation, expected_error in (
            (
                lambda payload: payload.pop("completed_at"),
                "Missing required sentinel field: completed_at",
            ),
            (
                lambda payload: payload.update(completed_at="not-a-timestamp"),
                "Sentinel completed at must be a timezone-aware ISO 8601 timestamp",
            ),
        ):
            with self.subTest(expected_error=expected_error):
                with tempfile.TemporaryDirectory() as temp_dir:
                    notes = Path(temp_dir) / "notes"
                    notes.mkdir()
                    summary = notes / "phase-summary.md"
                    self.write_valid_review_final(summary)

                    result = self.complete_phase(summary)

                    self.assertEqual(0, result.returncode, result.stdout)
                    sentinel = notes / ".phase-review-final.done"
                    payload = json.loads(sentinel.read_text(encoding="utf-8"))
                    mutation(payload)
                    sentinel.write_text(json.dumps(payload), encoding="utf-8")
                    errors = self.workflow_contract.validate_summary(summary, self.contract)

                    self.assertIn(expected_error, errors)

    def test_complete_phase_rejects_nonconforming_or_unsafe_run_ids_before_publication(self):
        for run_id in ("review-contract", "review/contract-20260710-1200"):
            with self.subTest(run_id=run_id):
                with tempfile.TemporaryDirectory() as temp_dir:
                    notes = Path(temp_dir) / "notes"
                    notes.mkdir()
                    summary = notes / "phase-summary.md"
                    self.write_valid_review_final(summary)
                    summary.write_text(
                        summary.read_text(encoding="utf-8").replace(
                            "review-contract-20260710-1200", run_id,
                        ),
                        encoding="utf-8",
                    )

                    result = self.complete_phase(summary, run_id=run_id)

                    self.assertEqual(1, result.returncode, result.stdout)
                    self.assertIn("Run ID", result.stdout)
                    self.assertFalse((notes / ".phase-review-final.done").exists())
                    self.assertFalse(list(notes.glob("phase-summary.*.md")))

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

    def test_cli_rejects_duplicate_template_fields_case_insensitively(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            template = Path(temp_dir) / "phase-summary.md"
            template.write_text(
                "# Phase Summary\n\n## Worker ID\na\n\n## worker id\nb\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(CLI_PATH), "--template", str(template)],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(1, result.returncode)
        self.assertIn("Duplicate template field: worker id", result.stdout)

    def test_complete_phase_writes_sentinel_after_valid_summary(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        self.write_valid_review_final(summary)
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
        self.assertNotIn("summary_sha256", payload)
        self.assertIn("completed_at", payload)
        self.assertEqual([], self.workflow_contract.validate_summary(summary, self.contract))

    def test_research_completion_publishes_only_current_summary_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            notes = Path(temp_dir) / "notes"
            notes.mkdir()
            summary = notes / "phase-summary.md"
            text = (FIXTURES / "valid-phase-summary.md").read_text(encoding="utf-8")
            text = (
                text.replace("## Run ID\nreview-contract-20260710-1200", "## Run ID\nresearch-contract-20260710-1200")
                .replace("## Phase\nreview-final", "## Phase\nresearch")
                .replace("## Review verdict\napproved", "## Review verdict\nnot_applicable")
                .replace("## Next phase\nrelease", "## Next phase\nnarrative")
            )
            summary.write_text(text, encoding="utf-8")

            result = self.complete_phase(
                summary,
                run_id="research-contract-20260710-1200",
                phase="research",
                launched_at="2026-07-10T12:00:00-05:00",
            )

            self.assertEqual(0, result.returncode, result.stdout)
            payload = json.loads((notes / ".phase-research.done").read_text(encoding="utf-8"))
            self.assertEqual("notes/phase-summary.md", payload["summary"])
            self.assertNotIn("summary_sha256", payload)
            self.assertFalse(list(notes.glob("phase-summary.*.md")))
            self.assertEqual(
                {
                    "contract_version", "run_id", "phase", "attempt",
                    "execution_status", "summary", "completed_at",
                },
                set(payload),
            )

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
        self.write_valid_review_final(summary)
        sentinel = notes / ".phase-review-final.done"
        self.write_sentinel(summary, sentinel, "review-final", run_id="old-run-20260709-1200")
        self.addCleanup(temp_dir.cleanup)

        result = self.complete_phase(summary)

        self.assertEqual(1, result.returncode)
        self.assertIn("stale", result.stdout.lower())
        self.assertEqual("old-run-20260709-1200", json.loads(sentinel.read_text(encoding="utf-8"))["run_id"])

    def test_complete_phase_rejects_stale_sentinel_from_same_run_with_other_attempt(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        text = (FIXTURES / "valid-phase-summary.md").read_text(encoding="utf-8")
        summary.write_text(
            text.replace("## Phase\nreview-final", "## Phase\nresearch")
            .replace("## Review verdict\napproved", "## Review verdict\nnot_applicable")
            .replace("## Candidate artifact\nslides/candidate.pptx", "## Candidate artifact\nnone")
            .replace("## Next phase\nrelease", "## Next phase\nnarrative"),
            encoding="utf-8",
        )
        sentinel = notes / ".phase-research.done"
        self.write_sentinel(summary, sentinel, "research", attempt=2)
        self.addCleanup(temp_dir.cleanup)

        result = self.complete_phase(summary, phase="research")

        self.assertEqual(1, result.returncode)
        self.assertIn("stale", result.stdout.lower())
        self.assertEqual(2, json.loads(sentinel.read_text(encoding="utf-8"))["attempt"])

    def test_complete_phase_rejects_sentinel_claimed_by_other_run_during_publish(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        self.write_valid_review_final(summary)
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

    def test_advisor_request_carries_sentinel_contract_while_prompt_stays_scoped(self):
        request = (ROOT / "templates" / "charlas-sdd" / "advisor-request.md").read_text(encoding="utf-8")
        prompt = (ROOT / "templates" / "charlas-sdd" / "prompts" / "run-advisor.md").read_text(encoding="utf-8")
        self.assertIn("<talk>/notes/advice/<run-id>-advisor.md", request)
        self.assertIn("<talk>/notes/advice/.advisor-<run-id>.done", request)
        self.assertIn("request `run_id`", request)
        self.assertIn("actual model", request)
        self.assertIn("completion timestamp", request)
        self.assertIn("agents/advisor-charlas.md", prompt)
        self.assertIn("Advisor Request", prompt)
        self.assertIn("agents/runtime-defaults.json", prompt)
        self.assertIn("requested and actual runtime", prompt)
        self.assertIn("--advisor-request", prompt)

    def test_cli_validates_advisor_sentinel_identity(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            request = Path(temp_dir) / "advisor-request.md"
            request.write_text(
                (ROOT / "templates" / "charlas-sdd" / "advisor-request.md")
                .read_text(encoding="utf-8")
                .replace("`<lowercase-slug-YYYYMMDD-HHMM>`", "advice-20260711-0900"),
                encoding="utf-8",
            )
            sentinel = Path(temp_dir) / ".advisor-advice-20260711-0900.done"
            sentinel.write_text(
                json.dumps({
                    "run_id": "advice-20260711-0900",
                    "actual_model": "gpt-5.6-sol",
                    "completed_at": "2026-07-11T09:05:00-05:00",
                    "recommendation_path": "notes/advice/advice-20260711-0900-advisor.md",
                }),
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable, str(CLI_PATH),
                    "--advisor-request", str(request),
                    "--advisor-sentinel", str(sentinel),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )

        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VALID ADVISOR SENTINEL", result.stdout)

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

    def test_compact_review_publication_rejects_shared_build_identity(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        self.addCleanup(temp_dir.cleanup)
        candidate_sha256 = self.publish_compact_build(summary, Path(temp_dir.name) / "slides" / "candidate.pptx")
        self.write_compact_phase_summary(
            summary,
            phase="review",
            worker_id="builder-7",
            session_id="review-session-13",
            candidate_sha256=candidate_sha256,
        )

        result = self.complete_phase(summary, phase="review")

        self.assertEqual(1, result.returncode)
        self.assertIn("worker_id", result.stdout)
        self.assertFalse((notes / ".phase-review.done").exists())

    def test_full_build_and_review_publication_do_not_require_compact_boundary_fields(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        self.addCleanup(temp_dir.cleanup)
        text = (FIXTURES / "valid-phase-summary.md").read_text(encoding="utf-8")
        summary.write_text(
            text.replace("## Run ID\nreview-contract-20260710-1200", "## Run ID\nbuild-contract-20260710-1200")
            .replace("## Phase\nreview-final", "## Phase\nbuild")
            .replace("## Review verdict\napproved", "## Review verdict\nnot_applicable")
            .replace("## Next phase\nrelease", "## Next phase\nreview")
            .replace(
                "## Final artifact\nnone",
                "## Final artifact\nnone\n\n## Worker ID\nbuilder-7\n\n## Session ID\nbuild-session-12",
            ),
            encoding="utf-8",
        )
        build = self.complete_phase(summary, phase="build", run_id="build-contract-20260710-1200")
        self.assertEqual(0, build.returncode, build.stdout)
        summary.write_text(
            text.replace("## Phase\nreview-final", "## Phase\nreview")
            .replace("## Review verdict\napproved", "## Review verdict\nrequires_changes")
            .replace("## Next phase\nrelease", "## Next phase\nbuild-fix")
            .replace(
                "## Final artifact\nnone",
                "## Final artifact\nnone\n\n## Worker ID\nreviewer-8\n\n## Session ID\nreview-session-13",
            ),
            encoding="utf-8",
        )

        review = self.complete_phase(summary, phase="review")

        self.assertEqual(0, review.returncode, review.stdout)
        self.assertTrue((notes / ".phase-review.done").exists())

    def test_full_review_publication_rejects_shared_build_identity(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        self.addCleanup(temp_dir.cleanup)
        text = (FIXTURES / "valid-phase-summary.md").read_text(encoding="utf-8")
        build_summary = (
            text.replace("## Phase\nreview-final", "## Phase\nbuild")
            .replace("## Review verdict\napproved", "## Review verdict\nnot_applicable")
            .replace("## Next phase\nrelease", "## Next phase\nreview")
            .replace(
                "## Final artifact\nnone",
                "## Final artifact\nnone\n\n## Worker ID\nbuilder-7\n\n## Session ID\nbuild-session-12",
            )
        )
        summary.write_text(build_summary, encoding="utf-8")
        build = self.complete_phase(summary, phase="build")
        self.assertEqual(0, build.returncode, build.stdout)

        review_summary = (
            text.replace("## Phase\nreview-final", "## Phase\nreview")
            .replace("## Review verdict\napproved", "## Review verdict\nrequires_changes")
            .replace("## Next phase\nrelease", "## Next phase\nbuild-fix")
            .replace(
                "## Final artifact\nnone",
                "## Final artifact\nnone\n\n## Worker ID\nbuilder-7\n\n## Session ID\nbuild-session-12",
            )
        )
        summary.write_text(review_summary, encoding="utf-8")

        review = self.complete_phase(summary, phase="review")

        self.assertEqual(1, review.returncode)
        self.assertIn("worker_id", review.stdout)
        self.assertFalse((notes / ".phase-review.done").exists())

    def test_full_sentinel_identity_must_match_summary(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        self.addCleanup(temp_dir.cleanup)
        text = (FIXTURES / "valid-phase-summary.md").read_text(encoding="utf-8")
        summary.write_text(
            text.replace("## Phase\nreview-final", "## Phase\nbuild")
            .replace("## Review verdict\napproved", "## Review verdict\nnot_applicable")
            .replace("## Next phase\nrelease", "## Next phase\nreview")
            .replace(
                "## Final artifact\nnone",
                "## Final artifact\nnone\n\n## Worker ID\nbuilder-7\n\n## Session ID\nbuild-session-12",
            ),
            encoding="utf-8",
        )
        result = self.complete_phase(summary, phase="build")
        self.assertEqual(0, result.returncode, result.stdout)
        summary.write_text(
            summary.read_text(encoding="utf-8").replace("## Worker ID\nbuilder-7", "## Worker ID\nother-worker"),
            encoding="utf-8",
        )

        errors = self.workflow_contract.validate_summary(summary, self.contract)

        self.assertTrue(any("sentinel worker id" in error.lower() for error in errors), errors)

    def test_compact_build_rejects_review_that_omits_or_changes_compact_mode(self):
        for review_mode in ("", "full"):
            with self.subTest(review_mode=review_mode):
                temp_dir = tempfile.TemporaryDirectory()
                notes = Path(temp_dir.name) / "notes"
                notes.mkdir()
                summary = notes / "phase-summary.md"
                self.addCleanup(temp_dir.cleanup)
                self.publish_compact_build(summary, Path(temp_dir.name) / "slides" / "candidate.pptx")
                self.write_compact_phase_summary(
                    summary,
                    phase="review",
                    worker_id="builder-7",
                    session_id="build-session-12",
                    candidate_sha256="0" * 64,
                )
                summary.write_text(
                    summary.read_text(encoding="utf-8").replace(
                        "## Workflow mode\ncompact", f"## Workflow mode\n{review_mode}"
                    ),
                    encoding="utf-8",
                )

                errors = self.workflow_contract.validate_publication(
                    self.workflow_contract.parse_summary(summary),
                    self.contract,
                    summary,
                )

                result = self.complete_phase(summary, phase="review")

                self.assertTrue(any("workflow mode" in error.lower() for error in errors), errors)
                self.assertEqual(1, result.returncode)
                self.assertIn("workflow mode", result.stdout.lower())
                self.assertFalse((notes / ".phase-review.done").exists())

    def test_compact_review_publication_rejects_mismatched_candidate_hash(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        self.addCleanup(temp_dir.cleanup)
        self.publish_compact_build(summary, Path(temp_dir.name) / "slides" / "candidate.pptx")
        self.write_compact_phase_summary(
            summary,
            phase="review",
            worker_id="reviewer-8",
            session_id="review-session-13",
            candidate_sha256="0" * 64,
        )

        result = self.complete_phase(summary, phase="review")

        self.assertEqual(1, result.returncode)
        self.assertIn("SHA256", result.stdout)
        self.assertFalse((notes / ".phase-review.done").exists())

    def test_compact_review_validation_rejects_shared_identity_and_mismatched_hash(self):
        temp_dir = tempfile.TemporaryDirectory()
        notes = Path(temp_dir.name) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        self.addCleanup(temp_dir.cleanup)
        self.publish_compact_build(summary, Path(temp_dir.name) / "slides" / "candidate.pptx")
        self.write_compact_phase_summary(
            summary,
            phase="review",
            worker_id="builder-7",
            session_id="build-session-12",
            candidate_sha256="0" * 64,
        )
        review_sentinel = notes / ".phase-review.done"
        self.write_sentinel(
            summary,
            review_sentinel,
            "review",
            workflow_mode="compact",
            worker_id="builder-7",
            session_id="build-session-12",
            candidate_artifact="slides/candidate.pptx",
            candidate_sha256="0" * 64,
        )

        errors = self.workflow_contract.validate_summary(summary, self.contract)

        self.assertTrue(any("worker_id" in error for error in errors), errors)
        self.assertTrue(any("SHA256" in error for error in errors), errors)

    def test_check_docs_rejects_model_literal_outside_runtime_defaults(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            document = Path(temp_dir) / "workflow.md"
            document.write_text("- `model`: `gpt-5.4`\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(CLI_PATH), "--check-docs", str(document)],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )

        self.assertEqual(1, result.returncode)
        self.assertIn("model literal", result.stdout.lower())

    def test_check_docs_rejects_generic_model_names_outside_runtime_defaults(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            document = Path(temp_dir) / "workflow.md"
            document.write_text("- model: o1\n- model: Claude 3.5 Sonnet\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(CLI_PATH), "--check-docs", str(document)],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )

        self.assertEqual(1, result.returncode)
        self.assertIn("model literal", result.stdout.lower())

    def test_check_docs_allows_runtime_defaults_and_legacy_talk_contexts(self):
        runtime_defaults = ROOT / "agents" / "runtime-defaults.json"
        legacy_document = (
            ROOT
            / "Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento"
            / "notes"
            / "research-launch-package.md"
        )

        result = subprocess.run(
            [sys.executable, str(CLI_PATH), "--check-docs", str(runtime_defaults), str(legacy_document)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VALID DOC REFERENCES", result.stdout)

    def test_check_docs_rejects_legacy_pass_fail_field_outside_legacy_talks(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            document = Path(temp_dir) / "workflow.md"
            document.write_text("## Pasa / no pasa\nno pasa\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(CLI_PATH), "--check-docs", str(document)],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )

        self.assertEqual(1, result.returncode)
        self.assertIn("pasa / no pasa", result.stdout.lower())

    def test_check_docs_rejects_mojibake(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            document = Path(temp_dir) / "workflow.md"
            document.write_text("La recomendaciÃ³n debe ser clara.\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(CLI_PATH), "--check-docs", str(document)],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )

        self.assertEqual(1, result.returncode)
        self.assertIn("mojibake", result.stdout.lower())

    def test_worker_flow_audit_charlas_adapter_matches_renderer_and_run_aware_sentinels(self):
        skill = (ROOT / "skills" / "worker-flow-audit" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("`deck-spec.json` -> `scripts/deck_renderer/render-deck.js`", skill)
        self.assertIn("`qa-deck.py` and `validate-powerpoint.ps1`", skill)
        self.assertIn("PowerPoint native remains the final gate", skill)
        self.assertIn("run ID, phase, attempt and summary path", skill)
        self.assertNotIn("mutable current summary as historical evidence", skill)
        self.assertNotIn("@oai/artifact-tool", skill)
        self.assertNotIn("`pptxgenjs` not used", skill)

    def test_contract_uses_current_handoff_and_minimal_sentinel_fields(self):
        self.assertEqual("notes/phase-summary.md", self.contract["current_summary"])
        self.assertNotIn("historical_summary_pattern", self.contract)
        self.assertEqual(
            [
                "contract_version",
                "run_id",
                "phase",
                "attempt",
                "execution_status",
                "summary",
                "completed_at",
            ],
            self.contract["required_sentinel_fields"],
        )

    def test_cli_validates_migrated_summary_without_a_completion_sentinel(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            notes = Path(temp_dir) / "notes"
            notes.mkdir()
            summary = notes / "phase-summary.md"
            text = (FIXTURES / "valid-phase-summary.md").read_text(encoding="utf-8")
            summary.write_text(
                text.replace("## Phase\nreview-final", "## Phase\nresearch")
                .replace("## Decision\nadvance", "## Decision\niterate")
                .replace("## Review verdict\napproved", "## Review verdict\nnot_applicable")
                .replace("## Candidate artifact\nslides/candidate.pptx", "## Candidate artifact\nnone")
                .replace("## Next phase\nrelease", "## Next phase\nresearch"),
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable, str(CLI_PATH),
                    "--summary", str(summary),
                    "--allow-migrated-summary-without-sentinel",
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )

        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VALID MIGRATED SUMMARY", result.stdout)


if __name__ == "__main__":
    unittest.main()
