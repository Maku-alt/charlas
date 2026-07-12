# Workflow v2 Mini Flow Audit Design

**Purpose:** Validate the workflow-v2 branch with one inexpensive, real execution before it is integrated into `develop`.

## Scope

The experiment runs only in `codex/agent-workflow-hardening` and creates a disposable talk at `smoke-workflow-v2/`. It uses a fixed Spanish brief and a three-slide deck. It has no external research, generated imagery, or changes to existing talks.

The flow is deliberately not a happy-path-only test:

```text
narrative -> build (controlled defect) -> review (requires changes)
          -> build-fix -> review-final (approved) -> release
```

Each worker receives a separate v2 execution package with a distinct worker and session identity. The parent uses only validated files and sentinels to decide transitions.

## Test Artifact

`smoke-workflow-v2/` contains only the material needed to exercise the contract:

- `specs/`: a brief narrative/build/review contract copied and completed from the full templates.
- `notes/`: phase summaries, execution packages, sentinels and the controlled-defect description.
- `slides/`: `deck-spec.json`, the initial candidate, the corrected candidate, PowerPoint-native evidence and the promoted deliverable.
- `review/`: the initial actionable review report and the final approval report.
- `analysis/workflow-v2-mini-flow-audit-2026-07-12/`: audit output only; it never changes the candidate or phase artifacts.

The test deck consists of: (1) decision context, (2) an explicit before/after comparison, and (3) an editorial recommendation. The initial build introduces a declared, easily observable defect on slide 2. Review must identify that exact defect and require a focused fix; build-fix must change only slide 2.

## Execution Contract

All workers use `fork_context: false`, create their summary before their sentinel, and call `scripts/agent_workflow/complete-phase.py` to publish the sentinel. The parent checks each sentinel with `validate-workflow.py` before reading the summary and never obtains status from worker chat.

The initial build and review must use distinct `worker_id` and `session_id`. The review-final and build-fix must also be distinct. Candidate hashes are recorded at build, review, build-fix, review-final and release. Release promotes only the candidate hash approved by review-final and recomputes the promoted-file hash.

## Audit

After release, `worker-flow-audit` runs as a read-only audit. It does not replay phases, inspect worker chats, infer structured calls from text, or treat summaries as token evidence. It produces concise evidence files under the audit directory:

- `verdict.md`: separate product, execution-identification, worker-contract and token-measurement verdicts.
- `phase-execution-validation.md`: phase, identity, sentinel, artifact, evidence and confirmation level.
- `sentinel-validation.md`: identity and timestamp checks.
- `final-product-validation.md`: PPTX path, SHA256, slide count, native evidence and review evidence.
- `function-calls-summary.csv` and `usage-sessions-summary.csv`: only if runtime records can be bounded reliably.
- `correction-notes.md`: any contract/document drift found, including the stale renderer assumptions currently present in `skills/worker-flow-audit/SKILL.md`.

Token reporting remains separate: missing or unbounded runtime records yield `token usage: unknown`, not a functional failure.

## Pass Criteria

The experiment is eligible for integration only if all of the following hold:

1. The three-slide PPTX opens and exports with PowerPoint-native evidence.
2. The initial review independently finds the declared slide-2 defect and returns `requires_changes`.
3. Build-fix changes only the authorized slide and publishes a new, valid identity.
4. Review-final is independent, approves the corrected candidate, and records its exact hash.
5. Release promotes a byte-identical approved candidate and records matching SHA256 values.
6. Every phase transition and sentinel identity validates under workflow v2.
7. The audit has no P1 or P2 finding against execution identity, sentinel handling, review independence or release integrity.

Documentation drift in the audit adapter is reported separately. It blocks integration only if it causes the test or its audit to use an engine or final-quality gate that contradicts the workflow-v2 contract.

## Failure Handling

On any pass-criterion failure, stop before integration, preserve the disposable experiment and audit evidence, and create a focused remediation plan. Do not alter legacy talks or `develop`. Generated files from a failed smoke test may be removed only after the audit report captures their paths and hashes.

## Out of Scope

- Research quality, external citations and image-close generation.
- Token-efficiency comparisons against historical baselines.
- Bulk migration of talks or changes to existing deck-renderer behavior.
- Modifying the audit skill as part of this test; findings become a separate follow-up.
