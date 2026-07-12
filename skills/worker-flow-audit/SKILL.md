---
name: worker-flow-audit
description: Audit a charla worker run against its canonical identity, transition, artifacts and referenced evidence without reading worker chats or modifying the run.
---

# Worker Flow Audit

Audit a bounded charla run from repository artifacts. The audit answers whether the declared phase ran under the expected identity, produced the expected artifact and supports the requested transition.

## Boundaries

- Treat `agents/workflow-contract.json` as canonical for phases, transitions, roles, inputs, outputs, sentinels and independence constraints. Do not reproduce its phase table.
- Never use `read_thread` or inspect worker chats, logs or reasoning.
- Do not rerun or modify the audited phase or its artifacts.
- Do not infer completion from sentinel existence alone.
- Keep Advisor exceptional and consultative; it is not a workflow phase or a source of transition authority.

## Evidence

Use the execution package, sentinel, `notes/phase-summary.md`, expected artifacts and evidence paths referenced by the summary. For each claim, cite a concrete path, field, hash or check result. Missing evidence remains missing; do not reconstruct it from conversation history.

## Audit Procedure

1. Read the execution package and canonical contract.
2. Validate that the sentinel matches `run_id`, phase, attempt and execution status.
3. Only after that validation, read `notes/phase-summary.md`.
4. Check that the summary and artifact match the declared phase and output contract.
5. Check that the proposed transition is allowed by the canonical contract.
6. Inspect only the referenced evidence needed for the verdict.
7. Write a concise report with findings and a pass, changes-required or blocked verdict.

The worker overwrites `notes/phase-summary.md` and publishes the sentinel last through `complete-phase.py`. The parent validates run identity, phase, attempt and execution status before reading the summary. Sentinel existence alone is not completion.

Validation ties the run ID, phase, attempt and summary path to the execution package.

## Independent Review And PPTX Gates

For review phases, confirm the reviewer is independent from build or build-fix as required by the contract. Review reports findings; it does not silently repair the candidate.

For a PPTX candidate, preserve these gates:

- Validate the exact candidate artifact and its integrity hash.
- Confirm review and review-final refer to that same candidate.
- Confirm new decks use `deck-spec.json` -> `scripts/deck_renderer/render-deck.js`.
- Confirm `qa-deck.py` and `validate-powerpoint.ps1` evidence exists.
- Require the editable PPTX to open and export in native PowerPoint.
- PowerPoint native remains the final gate.
- Treat LibreOffice and Poppler as auxiliary checks only.
- Allow release to promote only the candidate approved by review-final.

## Report

Keep the report compact:

- Run identity and phase.
- Sentinel validation result.
- Canonical transition result.
- Expected artifact and integrity result.
- Referenced evidence checked.
- Independence and native PowerPoint gate when applicable.
- Findings, verdict and one next action.

Do not paste transcripts or command logs. Reference their paths when they are legitimate evidence.
