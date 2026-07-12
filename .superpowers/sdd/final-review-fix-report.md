# Final Review Fix Report

## Status

Complete. All Critical and Important whole-branch review findings in the fix brief were addressed with the existing contract validator and atomic completion publisher.

## Findings addressed

- Full and compact `build`, `build-fix`, `review`, and `review-final` now require an in-talk candidate file whose SHA256 matches the summary.
- `review` consumes the exact candidate path/hash from `.phase-build.done`; `review-final` does the same from `.phase-build-fix.done`.
- Every artifact sentinel publishes candidate path/hash. Compact mode additionally retains `workflow_mode`.
- Review sentinels publish their verdict so release can validate approved predecessor semantics.
- An approved initial `review` can transition directly to `release`.
- Release accepts an exact candidate approved by initial or final review, validates the promoted final file is inside the talk directory and byte-identical by SHA256, and publishes candidate/final identities and hashes.
- Active parallel/temporary-summary instructions were removed; sequential publication and inactive `allows_parallel_with` metadata are now documented consistently.
- Duplicate orchestrator handoff prose was removed and release documentation now describes enforced validation.

## TDD evidence

RED was captured before production changes by running eight focused tests. Result: six assertion failures and two missing-payload-key errors, each caused by the absent full-mode candidate/release behavior.

GREEN was then captured for the same focused family: 8 tests passed. Additional focused coverage was added for approved initial review release and rejection of an approved predecessor for a different candidate. The final agent-workflow suite passes 61 tests.

## Files changed

- `agents/workflow-contract.json`
- `scripts/agent_workflow/workflow_contract.py`
- `scripts/agent_workflow/complete-phase.py`
- `tests/agent_workflow/test_workflow_contract.py`
- `agents/orchestrator-charlas.md`
- `agents/README.md`
- `templates/charlas-sdd/README.md`

No final SHA field was added to the summary template because completion recomputes it directly from the promoted file.

## Self-review

- Kept the existing atomic temp-file plus `os.replace` publication and stale-sentinel lock behavior unchanged.
- Kept the implementation local to the existing validator/publisher; no new storage, service, history, or telemetry subsystem was introduced.
- Release chooses an approved sentinel only when its candidate path and hash exactly match the release summary, preferring matching `review-final` evidence before matching initial `review` evidence.
- Candidate and final paths are resolved and containment-checked against the talk root.
- The protected modified historical plan and all untracked smoke evidence were left untouched.

## Concerns

None known. Operationally, promotion remains an orchestrator action performed before completion; completion is deliberately a rejecting publication gate, not a file-copy mechanism.
