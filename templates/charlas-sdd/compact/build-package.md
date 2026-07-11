# Compact Build Package

Usa este paquete exclusivamente para construir una charla pequena con narrativa clara. La review es una fase separada e independiente.

## Narrative source
<approved research package or approved narrative path>

## Slides expected
- count:
- thesis by slide:
- closing direction:

## Visual system
- visual tone:
- density:
- palette:
- image use:
- closing treatment:

## Build worker identity
- worker_id: <stable worker identifier>
- session_id: <isolated session identifier>

## Build expected
- editable PPTX candidate
- source deck specification
- build from `deck-spec.json` with `scripts/deck_renderer/render-deck.js`
- textual and mechanical checks
- native PowerPoint contact-sheet evidence
- SHA256 of the exact candidate artifact
- completed build `notes/phase-summary.md` and canonical build sentinel

## Constraints
- Do not perform review or approve the deck.
- Do not advance automatically; hand off the completed build summary, candidate path, and candidate SHA256 to the independent compact review.

