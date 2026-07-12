# Workflow v2 Light Pilot and Audit Design

## Objective

Validate `codex/agent-workflow-hardening` with one low-cost, real worker flow before integration into `develop`. The pilot must exercise phase isolation, run-aware sentinels, independent review, the correction loop and hash-preserving release. A separate audit must determine whether the run is contractually valid and operationally auditable.

## Scope

The pilot uses a disposable three-slide talk under `smoke-workflow-v2/` in the feature worktree. It uses no external research, web access or generated imagery. The content is intentionally simple so the test measures workflow behavior rather than editorial complexity.

The executed phases are:

```text
narrative -> build -> review -> build-fix -> review-final -> release
```

Research, thesis-review and image-close are outside this pilot. Their static contract coverage remains in the existing unit and consistency tests.

## Pilot artifact

The synthetic talk contains:

1. A concrete operational problem.
2. A comparison with one explicit tradeoff.
3. An executive recommendation and editorial closing message.

The initial build must contain one controlled, documented defect on slide 2. Use a deterministic defect that can be verified from the source and rendered evidence, such as visible text clipping or insufficient foreground/background contrast. The defect must not corrupt the PPTX or prevent PowerPoint-native opening/export.

The expected correction is restricted to slide 2. The build-fix worker may not rewrite the narrative, rebuild unrelated slides or change the closing message.

## Execution architecture

Each heavy phase runs in an isolated worker with its own execution package, `worker_id`, `session_id`, `run_id` and attempt. Workers receive only their role, prompt, phase-specific spec and explicitly allowed artifacts. They write `notes/phase-summary.md` first and publish the phase sentinel through `scripts/agent_workflow/complete-phase.py`.

The parent coordinates only. It validates sentinel identity before reading the summary and does not inspect worker chat, use `read_thread` or perform narrative, build, fix or review work itself.

Build and build-fix may use the same specialized role but must have distinct execution identities. Review and review-final must each be independent from build and build-fix. Release is an orchestrator-owned promotion step and must not modify PPTX contents.

## Phase expectations

### Narrative

Produces the three-slide sequence, conclusion-style titles, visible object and visual concept per slide, plus the fixed closing direction. It advances to build.

### Build

Produces the editable candidate PPTX, `deck-spec.json`, renderer output, mechanical QA and PowerPoint-native evidence. It also introduces the single declared defect on slide 2. All other acceptance criteria must pass.

### Review

Consumes the exact candidate and evidence without modifying them. It must return `requires_changes`, identify slide 2, describe the observed defect and provide a minimal acceptance criterion for build-fix. Failure to detect the seeded defect fails the pilot.

### Build-fix

Changes only slide 2 and the minimum source required to remove the defect. It produces a new candidate, updated evidence and a new run-aware build-fix sentinel.

### Review-final

Runs with an identity independent from both build executions. It verifies the corrected slide, checks for regressions on slides 1 and 3 and either approves the exact candidate hash or stops the flow.

### Release

Promotes the exact approved PPTX to the final path, recomputes SHA256 and blocks if the promoted hash differs from the reviewed candidate hash.

## Audit design

The audit starts only after the pilot reaches release or a terminal failure. It follows `skills/worker-flow-audit/SKILL.md` with these constraints:

- do not inspect worker chats or use `read_thread`;
- do not rerun or modify any audited phase artifact;
- use repository artifacts, execution packages, summaries, sentinels, runtime JSONL, process-manager records and SQLite metadata in that order;
- count only structured function-call events;
- report missing token evidence as unknown instead of estimating it.

Audit output lives in `analysis/workflow-v2-light-pilot-2026-07-12/` and includes:

- `verdict.md`
- `run-metadata.md`
- `phase-execution-validation.md`
- `sentinel-validation.md`
- `final-product-validation.md`
- `build-engine-validation.md`
- `function-calls-summary.csv`
- `token-measurement-validation.md`
- `audit-contract-drift.md`

`audit-contract-drift.md` must explicitly compare the audit adapter with the canonical renderer contract. The currently observed stale references to Presentations, `@oai/artifact-tool` and prohibition of `pptxgenjs` are findings to report, not rules to apply to the pilot and not changes authorized during the audit.

## Evidence and observability

Each phase must record:

- execution package path;
- requested and actual runtime;
- worker and session identities;
- launch and completion timestamps;
- summary and sentinel paths;
- input and output artifact paths;
- candidate SHA256 when a PPTX exists.

Token and function-call measurement is a separate audit dimension. The product and workflow may pass while end-to-end token usage remains unknown. A token claim passes only when the relevant execution window can be tied to accepted runtime events.

## Failure handling

The pilot stops immediately on:

- an invalid or stale sentinel;
- a transition rejected by the canonical validator;
- review sharing an execution identity with build or build-fix;
- review failing to identify the seeded defect;
- build-fix modifying slides 1 or 3 without documented necessity;
- review-final approving a different candidate from the one released;
- PowerPoint-native opening/export failure;
- any P1 or P2 audit finding.

No second build-fix/review-final cycle is authorized. A failure produces evidence and a correction recommendation for the feature branch; it does not trigger a merge to `develop`.

## Acceptance decision

The branch is eligible for integration only when all of the following are true:

- all existing 43 workflow unit tests and consistency validators still pass;
- the six-phase pilot reaches release;
- the initial review detects the controlled defect;
- build-fix changes only the authorized scope;
- review-final is independent and approves the corrected candidate;
- release hash matches the approved candidate hash;
- PowerPoint-native evidence confirms opening/export and three slides;
- audit reports product, phase identification, probable worker execution and worker contract as passing;
- audit contains no P1 or P2 findings.

End-to-end token measurement is informative rather than a merge gate. If the evidence is incomplete, the verdict must say `unknown` without blocking an otherwise valid functional pilot.

## Non-goals

- No migration or modification of existing talks.
- No external research or bibliography.
- No generated closing image.
- No performance benchmark against historical token baselines.
- No correction of workflow or audit code during the run itself.
- No merge, cherry-pick, push or pull request as part of the pilot.
