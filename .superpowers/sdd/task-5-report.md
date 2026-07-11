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
