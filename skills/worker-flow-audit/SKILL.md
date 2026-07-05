---
name: worker-flow-audit
description: Audit Codex workflows by phase, including parent-run phases, worker threads, sentinels, file handoffs, and token/function-call accounting. Use this whenever the user asks to validate token consumption, map a run to the right events/sessions, check whether workers actually ran, whether read_thread/subagents were avoided, whether a parent did heavy work, or whether an audit may have counted the wrong events. Includes guidance for the charlas repo workflow.
---

# Worker Flow Audit

Use this skill to audit Codex workflows phase by phase. A phase may run in the parent conversation, in a separate worker thread, or in a mixed/iterative path. The audit maps each phase to the right local events/sessions and then determines whether product validity, execution mode, and token/function-call consumption are measurable.

The audit must separate three questions:

1. Did the final product pass?
2. Which phases ran, where did they run, and are they tied to the right events/sessions?
3. Is token/function-call usage measurable from reliable local evidence?

Do not collapse these into one verdict. A run can pass as product and fail as auditable token design.

## Core Rules

Never use `read_thread` to inspect worker chats.

Do not read worker chat transcripts.

Do not use subagents for the audit unless the user explicitly asks for a separate meta-audit.

Do not rerun build, review, fix, or final review phases during audit.

Do not modify audited artifacts. Only write the audit report.

Do not count text mentions as tool calls. Strings such as `create_thread`, `send_message_to_thread`, `read_thread`, worker ids, or run ids inside prompts, markdown, CSVs, command output, or assistant messages are not function calls.

A JSONL can only be classified as a real parent/orchestrator session if it has structured evidence of launching workers, such as real function calls to `create_thread` or `send_message_to_thread`, or local metadata that proves it created child threads.

If phase or worker JSONL files are missing, say so. Do not infer token totals.

Do not treat `phase-summary.md`, hand-written JSON, or worker-authored summaries as proof of token usage. They can identify phases, artifacts, sentinels, and declared status, but token consumption must come from runtime events, JSONL usage checkpoints, or another verifiable system source.

## Evidence Sources

Prefer local evidence in this order:

1. Current repo artifacts.
2. Sentinels and handoff files.
3. Local Codex JSONL session files under `C:\Users\Victor\.codex\sessions\`.
4. `C:\Users\Victor\.codex\process_manager\chat_processes.json`.
5. `C:\Users\Victor\.codex\logs_2.sqlite` in read-only mode.
6. Generated asset folders, temp folders, and filesystem timestamps.
7. Prior audit reports, only as secondary evidence.

Use previous audit reports to compare or detect mistakes, not as primary truth.

## Session Identification

Start every audit by identifying the run/event boundary. Determine which local sessions or event records are related to the requested test, which are actual execution, and which are later audit or coordination discussion.

For every candidate JSONL, classify it as one of:

- `accepted_parent`
- `accepted_worker`
- `accepted_phase_session`
- `related_conversation`
- `audit_session`
- `rejected_candidate`

For each candidate record:

- file path
- session/conversation id
- timestamp range
- why it was considered
- run id hits
- worker id hits
- structured function calls
- textual mentions only
- associated phase, if any
- final decision

Reject a JSONL as parent if it only contains prompts, summaries, or audit discussion about the run.

If a JSONL spans multiple user tasks, only count the window relevant to the audited run. If the window cannot be bounded reliably, mark token measurement as partial or invalid.

## Function Call Accounting

Count only structured function-call events.

Report at least:

- `create_thread`
- `send_message_to_thread`
- `read_thread`
- `spawn_agent`
- `wait_agent`
- `close_agent`
- `exec_command`
- `apply_patch`
- `view_image`
- `load_workspace_dependencies`
- `image_generation_call`

If a tool name appears only in text, do not count it.

## Token Accounting

Use token checkpoints only from accepted sessions.

Report separately:

- `parent_tokens_confirmed`
- `worker_tokens_confirmed`
- `phase_tokens_confirmed`
- `observed_tokens_lower_bound`
- `end_to_end_tokens`

Set `end_to_end_tokens` to `unknown` if any required phase token usage is missing or cannot be bounded.

Never compare a partial token total against baselines as if it were end-to-end consumption.

For iterative phases such as research or narrative, measure only if the conversation window is clearly bounded. If the phase is mixed with unrelated discussion, report it as partially measurable or unknown rather than guessing.

If a mini or functional test passes operationally but lacks accepted token events, report it as `flow passes / token usage unknown`. Do not turn successful sentinels or artifacts into token evidence.

## Phase Execution Validation

Create a table per expected or observed phase:

- phase
- execution mode: `parent`, `worker`, `subagent`, `manual/external`, `unknown`
- accepted session/event id
- expected worker/thread id, if any
- sentinel path
- sentinel timestamp
- expected artifact
- artifact exists
- process_manager evidence
- SQLite evidence
- JSONL found
- tokens measurable
- verdict: `confirmed`, `partially confirmed`, or `not confirmed`

Use `confirmed` only when there is strong execution evidence, preferably JSONL or equivalent local metadata.

Use `partially confirmed` when sentinels/artifacts/timestamps support the workflow but tool-call or token evidence is missing. For parent-run phases, use `partially confirmed` when the artifact exists but the token window cannot be cleanly bounded.

## Report Structure

Create an audit output directory named for the experiment, for example:

```text
analysis/token-finalflow-workers-presentations-experiment-YYYY-MM-DD
analysis/token-finalflow-workers-presentations-experiment-YYYY-MM-DD-corrected
```

Generate these files when applicable:

```text
verdict.md
correction-notes.md
session-identification.md
worker-execution-validation.md
phase-execution-validation.md
final-product-validation.md
token-measurement-validation.md
function-calls-summary.csv
usage-sessions-summary.csv
sentinel-validation.md
visual-qa-validation.md
build-engine-validation.md
comparison-vs-previous-experiments.md
run-metadata.md
```

Keep reports concise. Use tables, timestamps, paths, hashes, and counts. Do not paste long logs or transcripts.

## Verdict Format

In `verdict.md`, declare separately:

- passes/fails as final product
- passes/fails as phase/event identification
- passes/fails as probable worker execution
- passes/fails as fully auditable worker contract
- passes/fails as end-to-end token measurement
- main cause of failure, if any
- concrete recommendation for the next run

Use language like:

```text
Producto final: pasa.
Ejecucion probable con workers: pasa parcialmente.
Contrato workers auditable completo: no pasa.
Medicion consumo end-to-end: no medible.
```

## Charlas Repo Adapter

Use this adapter when auditing:

```text
C:\Users\Victor\Proyectos\2026\charlas
```

Expected repo conventions:

```text
notes/phase-summary.md
notes/.phase-<phase>.done
review/<run-id>/
slides/<run-id>/
```

Expected phases are inferred from the user request, orchestration package, `phase-summary.md`, sentinel files, run folders, and artifacts. Common charla phases include `thesis`, `research`, `narrative`, `build`, `image-close`, `review`, `build-fix`, and `review-final`.

When auditing a relaunch, require timestamp or explicit stale-sentinel handling evidence. Some flows reuse base sentinels such as `.phase-build.done` and `.phase-review.done`; others may use phase-specific sentinels such as `.phase-build-fix.done` or `.phase-review-final.done`. Do not assume one convention without checking the run contract.

For PPTX flows, validate:

- final PPTX exists
- final PPTX SHA256
- filename has no experimental suffix when promoted
- `phase-summary.md` declares current phase and pass/fail
- PowerPoint native opened/exported final PPTX
- exported slide count
- contact sheet evidence
- review report and review-final report
- maximum one `review -> build-fix -> review-final` cycle unless explicitly authorized
- Presentations / `@oai/artifact-tool` used for new deck creation
- `pptxgenjs` not used for new deck creation
- LibreOffice/Poppler only auxiliary, not final gate

Known baselines for this repo:

```text
subagentes: 9,661,763
hilos polling: 11,382,147
hilos sentinel: 7,028,838
Presentations sentinel: 4,134,978
finalflow single-session invalido: 6,548,836
```

Do not compare against these using partial token totals. If only parent tokens are known, compare only as `parent_orchestration_tokens`.

## Common Failure Modes

Watch for these audit errors:

- Treating a prompt that says "use create_thread" as evidence that `create_thread` ran.
- Treating a JSONL with run-id mentions as the parent session.
- Counting the audit session itself as part of the run.
- Counting post-run conversation in the same JSONL.
- Declaring worker token savings when worker token logs are missing.
- Declaring no worker evidence while ignoring `process_manager` or filesystem artifacts.
- Approving a PPTX by LibreOffice/Poppler when the repo requires PowerPoint native as gate.

## Recommendation for Future Runs

If worker token measurement is required, ask each worker to write a small local telemetry file at completion, for example:

```text
review/<run-id>/telemetry/<phase>-usage-summary.json
```

Suggested fields:

```json
{
  "run_id": "",
  "phase": "",
  "thread_id": "",
  "session_jsonl": "",
  "started_at": "",
  "completed_at": "",
  "total_tokens": null,
  "input_tokens": null,
  "cached_input_tokens": null,
  "output_tokens": null,
  "function_calls": {},
  "artifacts": [],
  "sentinel": "",
  "status": "done|blocked"
}
```

If this file is missing, mark worker token measurement as unavailable.
