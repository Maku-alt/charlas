---
name: worker-flow-audit
description: Audit a charla worker run against its canonical identity, transition, Web Talk artifact and referenced evidence without reading worker chats or modifying the run.
---

# Worker Flow Audit

Audit a bounded Web Talk run from repository artifacts. Treat `agents/workflow-contract.json` as canonical and never infer completion from chat, logs or sentinel existence alone.

## Evidence

Use the execution package, sentinel, `notes/phase-summary.md`, exact candidate and referenced evidence. Validate run ID, phase, attempt and summary path before reading the summary.

## Procedure

1. Validate execution identity and transition.
2. Confirm required outputs for the phase.
3. For build, confirm the exact HTML candidate, SHA256, source, tests, self-audit and individual renders.
4. For review, confirm independence from build and that candidate, hash, renders and evidence are identical.
5. Confirm keyboard, fullscreen, console, assets, overflow, accessibility and offline gates when required.
6. Confirm release promotes only the candidate approved by the authoritative review.

## Output

Return identity, phase, evidence checked, findings, verdict and one next action. Do not paste logs or modify the audited run.
