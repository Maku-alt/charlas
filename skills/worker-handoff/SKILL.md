---
name: worker-handoff
description: Use this skill when a task should run in an isolated worker, separate Codex thread, subagent, or external chat with bounded context and file-based handoff. Use it for long-running research, audits, builds, reviews, experiments, or any workflow where the parent/orchestrator must not monitor worker chat or logs and should rely only on sentinels, compact summary files, and referenced evidence.
---

# Worker Handoff

Use this skill to run work through an isolated worker without contaminating the parent context or depending on chat history. The parent acts as orchestrator. The worker owns execution. The contract between them is a small set of files: inputs, summary, sentinel, and referenced evidence.

## Core Idea

Do not use the worker chat as the interface.

Use files as the interface:

- The parent prepares a minimal execution package.
- The worker reads only the package and required artifacts.
- The worker writes a compact summary and a completion sentinel.
- The parent validates sentinel identity and the summary before accepting completion.
- Evidence, logs, renders, outputs, and reports stay in files referenced by the summary.

This keeps the parent context small and prevents partial worker reasoning, logs, and exploratory noise from becoming orchestration state.

## When To Use

Use this skill when any of these are true:

- The task is long-running or token-heavy.
- The worker needs a fresh context.
- The parent should not inherit research, build, review, or audit details.
- The task may produce lots of logs or evidence.
- The task should be independently auditable.
- The workflow has phases with explicit pass/block decisions.
- The user says to use a worker, separate thread, isolated chat, subagent, sentinel, handoff, or compact summary.

Do not use it for small direct edits, quick questions, or tasks where the parent can safely complete the work in one context.

## Roles

### Parent / Orchestrator

The parent decides scope, prepares inputs, launches or instructs the worker, and decides the next transition after completion.

The parent should avoid inspecting worker chat, logs, or partial reasoning. It checks the sentinel identity and validates the agreed summary file before accepting completion.

### Worker

The worker executes the task from the package. It does not rely on hidden parent context. It writes artifacts, evidence, summary, and sentinel. Its final chat response should be minimal:

```text
DONE: summary written
```

or:

```text
BLOCKED: summary written
```

## Execution Package

Before launching a worker, prepare a minimal package with:

- Objective: concrete task and phase.
- Scope: what is in and out.
- Inputs: exact files, links, specs, prompts, or artifacts to read.
- Output contract: required summary path, sentinel path, and artifact paths.
- Acceptance criteria: what means pass, requires changes, or blocked.
- Constraints: what not to do, tools to use, limits, and repo-specific rules.
- Context policy: whether the worker may use external research, web, APIs, or only local files.
- Runtime preference: model, effort, fork-context behavior, or execution mode when applicable.
- Handoff rule: worker must write summary before sentinel.

The package should be enough for a fresh worker to execute without reading the parent conversation.

## Sentinel Contract

A sentinel is a small, run-aware completion record written after the worker has finished writing and validating the summary.

Rules:

- The worker writes the summary first.
- The worker writes the sentinel last.
- Completion requires a sentinel whose identity matches the expected contract version, run ID, phase, attempt, status, and summary path, plus a valid summary. Sentinel existence alone is not completion.
- If relaunching the same phase, the parent deletes, renames, or explicitly ignores the old sentinel.
- If the sentinel does not exist, the parent does not inspect worker chat to infer status.

Suggested generic sentinel names:

```text
.status/done
.status/blocked
```

or phase-specific:

```text
notes/.phase-research.done
notes/.phase-build.done
notes/.phase-review.done
```

Repo rules may override exact paths.

## Summary Contract

The summary must be compact and current. It is not a log.

Use this minimum structure:

```markdown
# Phase Summary

## Last phase
[phase name]

## Status
completed | requires changes | blocked

## Pass / No Pass
pass | no pass

## Summary
[1-3 sentences]

## Artifacts
- [path]
- [path]

## Blocking findings
- [finding or "None"]

## Next action
[one concrete next step]
```

For audits or reviews, include a referenced report path when findings are too detailed for the summary.

Do not paste full logs, transcripts, renders, command output, or raw evidence into the summary. Reference file paths instead.

## Parent Workflow

1. Identify whether isolation is useful.
2. Prepare the execution package.
3. Ensure output directories exist if needed.
4. Remove or explicitly ignore stale sentinels.
5. Launch or instruct the worker.
6. Wait for the sentinel using a filesystem check.
7. Validate its identity and validate the summary file.
8. Read only the validated summary file.
9. Decide the next transition from the summary.
10. Read referenced reports only when the summary says they are needed for the transition.
11. Do not inspect worker chat, logs, or reasoning to make orchestration decisions.

## Worker Workflow

1. Read the execution package.
2. Read only required input artifacts.
3. Execute the task.
4. Write outputs and evidence to agreed paths.
5. Write the summary with current status.
6. Validate the summary, then write the sentinel last.
7. Respond only with `DONE: summary written` or `BLOCKED: summary written`.

## Blocked State

A worker should mark blocked when it cannot complete the task under the given contract.

The summary should say:

- What blocked execution.
- Which checks succeeded.
- Which checks failed.
- Which artifacts exist.
- What decision or input is needed next.

The parent should not fill missing worker context by reading logs. If the summary is insufficient, treat that as a handoff failure and relaunch or ask for human input.

## Audits And Reviews

For audit-style tasks, the worker should produce:

- A compact summary.
- A detailed report file with findings.
- Evidence paths for each finding.
- Severity or priority.
- Minimal suggested fix or next action.
- Pass / no pass decision.

The parent should read the detailed report only after the summary references it and only if it is needed to decide the next transition.

## Parallel Workers

Parallel workers may run only if their outputs do not overwrite each other.

Use separate temporary summaries:

```text
notes/.phase-build.summary.md
notes/.phase-image.summary.md
```

Then the parent waits for both sentinels, reads both summaries, and writes or requests a consolidated summary.

## Repository Adaptation

This skill defines the protocol. The repo defines the concrete paths.

Before using the skill in a repo, check:

- `AGENTS.md`
- local agent files
- local templates or specs
- existing sentinel names
- required summary format
- prohibited monitoring behavior
- phase-specific preconditions

Follow repo rules when they are stricter than this skill.

## Common Failure Modes

Avoid these:

- Parent reads worker chat to check progress.
- Worker writes a long log instead of a summary.
- Sentinel is written before the summary.
- Old sentinel is reused accidentally.
- Worker depends on context that was not in the package.
- Parent advances phase from a missing or stale summary.
- Review fixes the artifact instead of reporting findings.
- Audit findings are not tied to evidence paths.
