# Execution Package

Paquete acotado para una sola corrida aislada. Completar todos los campos antes de lanzar al worker; no autoriza transiciones ni trabajo fuera de los inputs y outputs declarados.

## run_id
<lowercase-slug-YYYYMMDD-HHMM>

## attempt
<positive integer>

## phase
<canonical phase name from agents/workflow-contract.json>

## workflow mode
<full | compact; compact activates independent build/review boundary validation>

## role
<agents/<role>.md>

## worker identity
- worker_id: `<stable worker identifier>`
- session_id: `<isolated session identifier>`

## spec
<talk-relative path to the applicable spec or package>

## prompt
<template-relative path to the isolated execution prompt>

## allowed inputs
- `<talk-relative path or explicitly supplied input>`

## allowed outputs
- `<talk-relative path>`

## sentinel
`<talk>/notes/<phase sentinel from agents/workflow-contract.json>`

## acceptance criteria
- <concrete, verifiable criterion>

## immutable completion record
At completion, `scripts/agent_workflow/complete-phase.py` snapshots the exact validated summary to `<talk>/notes/phase-summary.<run_id>.md`. The sentinel must store that immutable path and its SHA256 as `summary_sha256`, together with `contract_version`, `run_id`, `phase`, `attempt`, `execution_status`, and `completed_at`.

The parent reads only `<talk>/notes/phase-summary.md`, the mutable current summary, for transitions. Historical validation and audits read only the immutable sentinel-named snapshot; the mutable current summary is not historical evidence.

## actual runtime
- Requested model: `<model | thread_default>`
- Actual model: `<model>`
- Requested reasoning effort: `<level | none>`
- Actual reasoning effort: `<level | none>`
- Runtime notes: `<fallback or none>`

## external-access policy
<allowed | prohibited | allowed only for the declared research scope>

## independence constraints
<none | concrete constraint, including required separation from build/build-fix for review phases>
