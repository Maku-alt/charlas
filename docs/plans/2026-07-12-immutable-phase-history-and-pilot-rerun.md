# Immutable Phase History and Pilot Rerun Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminate `P2-AUD-01` by making every published phase summary independently revalidatable, then repeat the light workflow-v2 pilot and audit before integrating into `develop`.

**Architecture:** Keep `notes/phase-summary.md` as the mutable current-state handoff. During atomic completion, snapshot the exact validated bytes to `notes/phase-summary.<run_id>.md`, store that path and its SHA256 in the sentinel, and validate historical phases against the immutable snapshot. Preserve the first pilot and audit as evidence; run the corrected pilot in a new directory.

**Tech Stack:** Python 3 standard library, Markdown, JSON sentinels, PowerShell, local deck renderer, PowerPoint-native QA, `unittest`.

## Global Constraints

- Work only on `codex/agent-workflow-hardening`; do not modify or merge `develop` during this plan.
- Preserve the first pilot under `smoke-workflow-v2/` and its audit under `analysis/workflow-v2-light-pilot-2026-07-12/`.
- Do not modify audited artifacts while correcting the workflow.
- Keep `notes/phase-summary.md` as the only current operational handoff read by the parent.
- Historical snapshots are immutable evidence, not additional current-state handoffs.
- Do not read worker chats or use `read_thread` during the pilot or audit.
- Do not estimate tokens when runtime usage checkpoints are absent.
- PowerPoint native remains the final PPTX opening/export gate.
- The unrelated main-worktree change in `scripts/deck_renderer/render-deck.js` remains untouched.

---

### Task 1: Specify immutable publication in tests

**Files:**
- Modify: `tests/agent_workflow/test_workflow_contract.py`

**Interfaces:**
- Consumes: current `complete_phase()` test helper and sentinel validation helpers.
- Produces: regression tests for immutable summary creation, hashing, overwrite rejection and historical revalidation.

- [ ] **Step 1: Add a helper for the expected immutable path**

Add this helper to `WorkflowContractTests`:

```python
def immutable_summary_path(self, summary: Path, run_id: str) -> Path:
    return summary.with_name(f"phase-summary.{run_id}.md")
```

- [ ] **Step 2: Add the failing publication test**

Add `test_complete_phase_snapshots_exact_summary_and_hashes_it`. Publish a valid phase, then assert:

```python
snapshot = self.immutable_summary_path(summary, "talk-review-final-20260710-1200")
sentinel = summary.parent / ".phase-review-final.done"
payload = json.loads(sentinel.read_text(encoding="utf-8"))

self.assertEqual(summary.read_bytes(), snapshot.read_bytes())
self.assertEqual(f"notes/{snapshot.name}", payload["summary"])
self.assertEqual(
    hashlib.sha256(snapshot.read_bytes()).hexdigest(),
    payload["summary_sha256"],
)
```

- [ ] **Step 3: Add the failing historical-validation test**

Add `test_historical_summary_remains_valid_after_current_summary_changes`. Publish `build`, overwrite only `notes/phase-summary.md` with a valid later `review` summary, and validate the build snapshot with the build sentinel:

```python
errors = self.workflow_contract._validate_summary(
    build_snapshot,
    self.contract,
    build_sentinel,
)
self.assertEqual([], errors)
```

- [ ] **Step 4: Add immutability and tamper tests**

Add:

```python
def test_complete_phase_rejects_existing_historical_snapshot(): ...
def test_historical_validation_rejects_summary_hash_mismatch(): ...
def test_current_summary_cannot_validate_against_historical_sentinel(): ...
```

The first test pre-creates `phase-summary.<run_id>.md` and expects completion to exit `1` without replacing either snapshot or sentinel. The second modifies the snapshot after publication and expects an error containing `Sentinel summary SHA256 does not match summary`. The third validates the mutable current summary after advancing phases and expects a sentinel summary-path mismatch.

- [ ] **Step 5: Run the focused tests and confirm red state**

Run:

```powershell
python -m unittest `
  tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_complete_phase_snapshots_exact_summary_and_hashes_it `
  tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_historical_summary_remains_valid_after_current_summary_changes `
  tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_complete_phase_rejects_existing_historical_snapshot `
  tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_historical_validation_rejects_summary_hash_mismatch `
  tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_current_summary_cannot_validate_against_historical_sentinel -v
```

Expected: failures because no immutable snapshot or `summary_sha256` is published yet.

- [ ] **Step 6: Commit the failing tests**

```powershell
git add tests/agent_workflow/test_workflow_contract.py
git commit -m "test: require immutable phase summary history"
```

### Task 2: Publish and validate immutable summaries atomically

**Files:**
- Modify: `scripts/agent_workflow/complete-phase.py`
- Modify: `scripts/agent_workflow/workflow_contract.py`
- Modify: `tests/agent_workflow/test_workflow_contract.py`

**Interfaces:**
- Consumes: canonical `notes/phase-summary.md`, phase contract and run identity.
- Produces: immutable `notes/phase-summary.<run_id>.md`; sentinel fields `summary` and `summary_sha256`; historical validation through `_validate_summary()`.

- [ ] **Step 1: Parse the exact bytes that will be archived**

Add to `workflow_contract.py`:

```python
def parse_summary_text(text: str) -> dict[str, str]:
    blocks = re.split(r"(?m)^## +(.+?)\s*$", text)
    return {
        blocks[index].strip().lower(): blocks[index + 1].strip()
        for index in range(1, len(blocks), 2)
    }


def parse_summary(path: str | Path) -> dict[str, str]:
    return parse_summary_text(Path(path).read_text(encoding="utf-8"))
```

This ensures the publisher can validate the same byte sequence it archives.

- [ ] **Step 2: Add an exclusive atomic snapshot writer**

Add to `complete-phase.py`:

```python
def _write_snapshot_atomically_exclusive(path: Path, content: bytes) -> None:
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as snapshot:
            snapshot.write(content)
            snapshot.flush()
            os.fsync(snapshot.fileno())
            temporary_path = Path(snapshot.name)
        os.link(temporary_path, path)
    except FileExistsError as error:
        raise RuntimeError(f"Historical summary already exists: {path}") from error
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()
```

The temporary file is fully flushed before the atomic hard-link publication. `os.link` fails rather than overwriting an existing historical snapshot.

The run ID already uses a lowercase slug plus timestamp; use it without path separators:

```python
snapshot = summary_path.with_name(f"phase-summary.{args.run_id}.md")
```

- [ ] **Step 3: Move exact validation and publication under the phase lock**

Inside `_sentinel_claim(sentinel)`, perform this order:

1. reject a stale/current sentinel;
2. read `summary_bytes = summary_path.read_bytes()` once;
3. decode UTF-8 and call `parse_summary_text()`;
4. run transition, publication and CLI identity validation;
5. reject an existing snapshot;
6. write the snapshot exclusively;
7. compute `summary_sha256 = hashlib.sha256(summary_bytes).hexdigest()`;
8. publish the sentinel atomically last.

If sentinel publication fails after snapshot creation, remove only the snapshot created by the current invocation before returning failure. Never replace a pre-existing snapshot.

- [ ] **Step 4: Point the sentinel at immutable evidence**

Replace the current `summary` field with:

```python
"summary": f"notes/{snapshot.name}",
"summary_sha256": hashlib.sha256(summary_bytes).hexdigest(),
```

Keep all existing identity, mode and candidate fields unchanged.

- [ ] **Step 5: Validate the archived hash**

In `_validate_sentinel()`, retain the path comparison based on the supplied summary path and add:

```python
actual_summary_sha256 = hashlib.sha256(summary_path.read_bytes()).hexdigest()
if values.get("summary_sha256") != actual_summary_sha256:
    errors.append("Sentinel summary SHA256 does not match summary")
```

Do not fall back to the mutable current summary when the sentinel names an immutable snapshot.

- [ ] **Step 6: Update pre-existing test expectations**

Change tests that expect `notes/phase-summary.md` in a newly published sentinel to expect `notes/phase-summary.<run_id>.md` and a valid `summary_sha256`. Hand-written legacy fixture sentinels may remain without the new field only when the test explicitly exercises invalid or v1 behavior; every valid v2 publication fixture must include it.

- [ ] **Step 7: Run the complete test suite**

```powershell
python -m unittest discover -s tests/agent_workflow -v
```

Expected: all existing 43 tests plus the five new tests pass.

- [ ] **Step 8: Commit the implementation**

```powershell
git add scripts/agent_workflow/complete-phase.py scripts/agent_workflow/workflow_contract.py tests/agent_workflow/test_workflow_contract.py
git commit -m "fix: preserve immutable phase publication evidence"
```

### Task 3: Align the operational contract and audit guidance

**Files:**
- Modify: `agents/workflow-contract.json`
- Modify: `agents/orchestrator-charlas.md`
- Modify: `templates/charlas-sdd/execution-package.md`
- Modify: `templates/charlas-sdd/README.md`
- Modify: `skills/worker-handoff/SKILL.md`
- Modify: `skills/worker-flow-audit/SKILL.md`
- Modify: `README.md`
- Modify: `tests/agent_workflow/test_workflow_contract.py`

**Interfaces:**
- Consumes: immutable publication behavior from Task 2.
- Produces: one documented convention for current summaries, historical summaries and sentinel validation.

- [ ] **Step 1: Version the publication requirement in the contract**

Add these top-level fields to `agents/workflow-contract.json` without changing phase transitions:

```json
"current_summary": "notes/phase-summary.md",
"historical_summary_pattern": "notes/phase-summary.<run_id>.md",
"sentinel_required_fields": [
  "contract_version",
  "run_id",
  "phase",
  "attempt",
  "execution_status",
  "summary",
  "summary_sha256",
  "completed_at"
]
```

- [ ] **Step 2: Document the parent/archival boundary**

State consistently:

```markdown
The parent reads `notes/phase-summary.md` only for the current transition. `complete-phase.py` snapshots that exact validated content to `notes/phase-summary.<run_id>.md` and writes its path and SHA256 into the sentinel. Historical validation and audit use the immutable path named by the sentinel.
```

Apply this rule to the orchestrator, execution package, template README, worker handoff, audit adapter and operator README. Remove any statement implying that a sentinel can be revalidated later against the mutable current summary.

- [ ] **Step 3: Add documentation regression assertions**

Extend `test_worker_flow_audit_charlas_adapter_matches_renderer_and_run_aware_sentinels` and the documentation checks to require `phase-summary.<run_id>.md` plus `summary_sha256` in operational docs and reject wording that calls the mutable summary historical evidence.

- [ ] **Step 4: Run syntax, documentation and asset gates**

```powershell
python -m json.tool agents/workflow-contract.json > $null
python scripts/agent_workflow/validate-workflow.py --check-docs AGENTS.md agents templates/charlas-sdd skills README.md
python scripts/agent_workflow/validate-workflow.py --check-phase-assets
python -m unittest discover -s tests/agent_workflow -v
git diff --check
```

Expected: JSON exits `0`; validators print `VALID DOC REFERENCES` and `VALID PHASE ASSETS`; all tests pass; no whitespace errors.

- [ ] **Step 5: Commit the contract alignment**

```powershell
git add agents/workflow-contract.json agents/orchestrator-charlas.md templates/charlas-sdd/execution-package.md templates/charlas-sdd/README.md skills/worker-handoff/SKILL.md skills/worker-flow-audit/SKILL.md README.md tests/agent_workflow/test_workflow_contract.py
git commit -m "docs: define immutable workflow phase history"
```

### Task 4: Run a focused historical-publication smoke test

**Files:**
- Create locally: `smoke-workflow-v2-history-rerun/notes/`
- Create locally: `smoke-workflow-v2-history-rerun/specs/execution/`
- Create locally: `analysis/workflow-v2-history-publication-smoke-2026-07-12/`

**Interfaces:**
- Consumes: corrected publisher and validator.
- Produces: two sequential phase publications proving that phase 1 remains valid after phase 2 overwrites the current summary.

- [ ] **Step 1: Create two minimal valid execution packages**

Use run IDs:

```text
workflow-v2-history-narrative-20260712-1200
workflow-v2-history-build-20260712-1201
```

Use distinct worker/session identities where the contract requires them. The packages must prohibit external access and write only inside `smoke-workflow-v2-history-rerun/`.

- [ ] **Step 2: Publish narrative and build sequentially**

For each phase, write the canonical current summary and invoke `complete-phase.py`. After build publication, confirm both immutable files exist and `notes/phase-summary.md` contains build state.

- [ ] **Step 3: Revalidate both historical publications**

Run:

```powershell
python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --summary "smoke-workflow-v2-history-rerun/notes/phase-summary.workflow-v2-history-narrative-20260712-1200.md" --sentinel "smoke-workflow-v2-history-rerun/notes/.phase-narrative.done"
python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --summary "smoke-workflow-v2-history-rerun/notes/phase-summary.workflow-v2-history-build-20260712-1201.md" --sentinel "smoke-workflow-v2-history-rerun/notes/.phase-build.done"
```

Expected: both print `VALID` after the current summary has advanced to build.

- [ ] **Step 4: Verify tamper detection without altering retained evidence**

Copy the narrative snapshot and sentinel into a temporary directory, change one byte in the copied summary, and run validation there. Expected: exit `1` with `Sentinel summary SHA256 does not match summary`. Delete only the temporary copies.

- [ ] **Step 5: Write the focused smoke verdict**

Create `analysis/workflow-v2-history-publication-smoke-2026-07-12/verdict.md` with commands, exit codes, snapshot paths, hashes and the explicit result for `P2-AUD-01`. Do not claim worker execution or tokens in this focused test.

### Task 5: Repeat the real light pilot and independent audit

**Files:**
- Preserve: `smoke-workflow-v2/`
- Preserve: `analysis/workflow-v2-light-pilot-2026-07-12/`
- Create locally: `smoke-workflow-v2-rerun/`
- Create locally: `analysis/workflow-v2-light-pilot-rerun-2026-07-12/`

**Interfaces:**
- Consumes: corrected and regression-tested workflow, plus the approved pilot design.
- Produces: a new six-phase run and corrected independent audit; does not reuse first-run sentinels or summaries.

- [ ] **Step 1: Prepare a fresh run boundary**

Copy only the synthetic three-slide brief/spec inputs from the first pilot. Do not copy outputs, summaries, sentinels, run IDs, worker IDs, session IDs, candidates or audit conclusions. Use new run IDs ending in the actual `YYYYMMDD-HHMM` launch minute.

- [ ] **Step 2: Execute the six canonical phases**

Run:

```text
narrative -> build -> review -> build-fix -> review-final -> release
```

Retain the same controlled slide-2 defect and one-cycle correction policy. Use an isolated identity for each worker phase. The parent validates the immutable summary named by each sentinel before applying a transition.

- [ ] **Step 3: Revalidate every phase after release**

For all six sentinels, read the `summary` path from sentinel JSON and invoke `validate-workflow.py` with that immutable summary and sentinel. Expected: six `VALID` results after `notes/phase-summary.md` contains release state.

- [ ] **Step 4: Run the independent audit**

Follow `skills/worker-flow-audit/SKILL.md`. Do not read chats, rerun phases or modify pilot artifacts. Write the full audit under `analysis/workflow-v2-light-pilot-rerun-2026-07-12/`, including `sentinel-validation.md`, product validation, phase/session identification, function-call accounting and token measurability.

- [ ] **Step 5: Apply the integration gate**

The rerun is eligible for integration only if:

- product and PowerPoint-native gates pass;
- six historical summaries validate after release;
- review detects the seeded defect;
- build-fix stays within slide 2;
- review-final is independent and approves the corrected candidate;
- release SHA256 matches the approved candidate;
- audit has no P1 or P2 findings;
- existing unit, documentation and phase-asset gates remain green.

Unknown end-to-end tokens remain non-blocking when the audit states why they are not measurable.

### Task 6: Prepare the integration decision

**Files:**
- Modify: `docs/plans/2026-07-09-agent-workflow-hardening.md`
- Reference: `analysis/workflow-v2-light-pilot-rerun-2026-07-12/verdict.md`

**Interfaces:**
- Consumes: corrected audit verdict and final regression output.
- Produces: an evidence-backed go/no-go status; performs no merge.

- [ ] **Step 1: Run final branch verification**

```powershell
python -m unittest discover -s tests/agent_workflow -v
python scripts/agent_workflow/validate-workflow.py --check-docs AGENTS.md agents templates/charlas-sdd skills README.md
python scripts/agent_workflow/validate-workflow.py --check-phase-assets
git diff --check
git status --short
```

- [ ] **Step 2: Update the hardening plan status**

Record the fix commits, test count, corrected audit verdict, remaining untracked pilot evidence and whether Task 13 is now eligible to proceed. Do not mark integration complete.

- [ ] **Step 3: Stop for user authorization**

Report the exact branch head and audit verdict. Merge, cherry-pick, push or PR creation requires a separate explicit user instruction.

---

## Self-review result

- Coverage: every element of `P2-AUD-01` maps to a failing test, publication change, documentation update, focused smoke test and real pilot rerun.
- Atomicity: the snapshot is created from the exact bytes validated under the phase lock; the sentinel is written last.
- Compatibility: the mutable current handoff remains at `notes/phase-summary.md`; historical snapshots stay directly under `notes/`, preserving existing talk-root resolution.
- Audit independence: the correction does not rewrite the first audit or use its summaries as runtime evidence.
- Scope: no phase graph, renderer, deck content methodology or token policy is redesigned.
