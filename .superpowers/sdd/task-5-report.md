# Task 5 report: normalize orchestrator and role boundaries

## Scope delivered

- Reduced `AGENTS.md` to stable repo principles and pointers to the canonical workflow contract.
- Rebuilt `agents/orchestrator-charlas.md` around all nine canonical phases, execution packages, validated run-aware polling at intervals of at most 60 seconds, and the exact-candidate SHA256 release gate.
- Replaced duplicated worker transport instructions in researcher, narrative, deck-builder, image-closer, and review roles with the execution-package/contract and `complete-phase.py` requirement. Workers must never handwrite or reuse a sentinel.

## Validation

- Obsolete transport scan: clean (no legacy fixed 180-second wait, old phase sentinel names, or worker chat completion strings in the target documentation).
- `git diff --check`: passed.
- Requested command `python scripts/agent_workflow/validate-workflow.py --check-docs AGENTS.md agents templates/charlas-sdd`: could not run because the current validator exposes only `--contract`, `--summary`, `--sentinel`, and `--template`; it exits 2 before recognizing `--check-docs`. Adding that validator mode is outside Task 5's documentation-only file scope.

## Commit

`refactor: align charla roles with canonical workflow`

## Review fix

- Normalized the affected full and compact phase specs plus execution prompts that still directed manual sentinels or chat completion strings.
- Each isolated phase now uses the execution package, `agents/workflow-contract.json`, and `scripts/agent_workflow/complete-phase.py`; compact build-review explicitly uses a separate package per canonical phase.
- `run-image-close.md` now refers to the canonical contract-selected sentinel for `image-close`, not `.phase-image.done`.
- Targeted obsolete-transport scan and `git diff --check` passed.
