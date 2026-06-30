# Prompt: Run Narrative

Estas ejecutando solo la fase `narrative-charlas`.

Precondicion del launch:

- este prompt debe ejecutarse junto con `agents/narrative-charlas.md`
- el archivo de rol especializado define el comportamiento; este prompt solo acota la fase

Usa solo:

- `Narrative Spec`
- research aprobado o research brief incluido

No construyas el `pptx`. No hagas review final.

Devuelve:

- tesis propuesta
- lectura narrativa
- audiencia y cambio esperado
- comparacion o tension central
- narrativa propuesta de 8-10 slides
- estructura de cierre
- riesgos narrativos
- entrada para `notes/agent-log.md` con fase, agente, modelo, esfuerzo, estado, artefactos, errores o bloqueos, y siguiente accion
- decision: `listo para build` o `requiere ajuste`

Para cada slide, incluye tambien:

- concepto visual

No declares `listo para build` si alguna slide solo tiene objetos sueltos o cajas sin una idea visual clara.
