# Advisor Request

Solicitud acotada para una consulta transversal. No crea una fase, no autoriza cambios y no reemplaza `notes/phase-summary.md`.

## run_id
`<lowercase-slug-YYYYMMDD-HHMM>`

## decision question
`<pregunta concreta que requiere recomendaciÃ³n>`

## current phase
`<canonical phase name>`

## affected phases
- `<canonical phase or role>`

## constraints
- `<time, cost, quality, auditability or policy constraint>`

## alternatives already considered
- `<alternative and known consequence>`

## minimal artifact paths
- `<talk-relative path to phase summaries or evidence>`

## urgency
`<low | normal | high and decision deadline>`

## expected recommendation format
- Recommendation
- Why
- Alternatives considered
- Tradeoffs
- Assumptions
- Risks
- Evidence paths
- Confidence
- Decision owner: orchestrator

## output contract

- Recommendation: `<talk>/notes/advice/<run-id>-advisor.md`
- Sentinel written after the recommendation: `<talk>/notes/advice/.advisor-<run-id>.done`
- The sentinel contains the request `run_id`, actual model, completion timestamp and recommendation path.
