# Compact Review Package

Usa este paquete exclusivamente para revisar, de manera independiente, una charla pequena ya construida. No modifica el deck.

## Completed build handoff
- build summary: <path to completed build `notes/phase-summary.md`>
- exact candidate PPTX: <path>
- candidate SHA256: <SHA256 recorded by build>
- build evidence: <paths>

## Review worker identity
- workflow mode: compact
- worker_id: <stable worker identifier distinct from build worker_id>
- session_id: <isolated session identifier distinct from build session_id>

## Independence gate
- `worker_id` and `session_id` must differ from the completed build handoff when independence is required.
- Validate with `validate_compact_review_independence`; reject a matching identifier.

## Review expected
- inspect the exact candidate whose SHA256 matches the build handoff
- independent review verdict and actionable report when changes are required
- completed review `notes/phase-summary.md` and canonical review sentinel

## Constraints
- Do not mutate the deck, source, candidate artifact, or build evidence.
- Do not approve a different artifact or a candidate whose hash does not match the completed build handoff.
