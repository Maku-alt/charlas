# Thesis Spec

## Run ID
<lowercase-slug-YYYYMMDD-HHMM; debe coincidir con el Execution Package y el phase summary>

## Tema
<tema bruto de la charla>

## Audiencia
<publico por defecto o publico especifico>

## Problema
<que problema, confusion o decision justifica esta charla>

## Tesis central
<afirmacion principal que la charla quiere defender>

## Cambio esperado
<que debe pensar, entender o decidir distinto la audiencia al final>

## Fuera de alcance
<temas que no entran para no diluir la charla>

## Tradeoff central
<comparacion o tension principal de la charla>

## Riesgos de framing
<donde la tesis puede sonar exagerada, ambigua o debil>

## Decision de continuidad
- `advance`: la tesis esta lista para pasar a `research`
- `stop`: no continuar esta charla

## Transicion esperada
`research` si la decision es `advance`; `stop` si la decision es `stop`.

## Publicacion atomica
- Actualizar `notes/phase-summary.md` con el mismo `run_id`, la decision y la transicion esperada.
- Publicar `.phase-thesis-review.done` solo mediante `scripts/agent_workflow/complete-phase.py` despues de validar el summary.
- No escribir, reutilizar ni comunicar el sentinel manualmente.

