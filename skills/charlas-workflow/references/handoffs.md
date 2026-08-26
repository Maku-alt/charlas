# Lightweight handoffs

Use native subagent messages with minimal context. Do not create package files.

## Dispatch

Provide:

- stable task ID and phase;
- one concrete objective;
- target talk directory;
- user decisions that affect scope;
- exact inputs to inspect;
- exact outputs the worker owns;
- constraints and external-source policy;
- observable acceptance criteria;
- required result schema: `charlas-specialist-result-v1`.

For Research require current sources and `notes/bibliografia.md`. For Build require `impeccable` and the frontend contract. For Review provide the expected candidate path and hash, require read-only operation and prohibit file writes.

## Result

```yaml
schema: charlas-specialist-result-v1
task_id: stable-short-id
phase: research|narrative|build|review
status: completed|partial|blocked
scope: concise description of work performed
outputs:
  - path: repository-relative path
    purpose: why it exists
checks:
  - gate: observable condition
    status: pass|fail|not_run
    evidence: path, URL, hash or concise observation
findings:
  - severity: P1|P2|P3|info
    issue: concise finding
    owner: orchestrator|researcher|narrative|builder|reviewer
next_action: one bounded recommendation
```

Research also returns verified URLs and consultation dates. Build includes the exact candidate SHA-256 and render paths. Review includes the independently recomputed hash and verdict.

## Acceptance

Accept a result only when task and phase match, outputs stay within ownership, gates have evidence and no hidden assumption changes scope. Ask one focused follow-up for an incomplete result; otherwise surface the blocker.

Do not request search diaries, logs, chain-of-thought, execution packages, phase summaries, sentinels or inherited full chat history.

