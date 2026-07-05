# Prompt: Run Narrative

Estas ejecutando solo la fase `narrative-charlas`.

Precondicion del launch:

- este prompt debe ejecutarse junto con `agents/narrative-charlas.md`
- el archivo de rol especializado define el comportamiento; este prompt solo acota la fase

Usa solo:

- `Narrative Spec`
- research aprobado o research brief incluido

No construyas el `pptx`. No hagas review final.

Regla para `modo chat separado` o hilo worker separado:

- el resultado operativo se comunica solo por archivos en disco
- sobrescribe `notes/phase-summary.md` con el estado actual de narrative
- escribe `notes/.phase-narrative.done` al terminar
- responde en chat solo `DONE: summary written` o `BLOCKED: summary written`
- no pegues el contenido del summary en chat
- no uses `agent-log.md`

Devuelve:

- tesis propuesta
- lectura narrativa
- audiencia y cambio esperado
- comparacion o tension central
- narrativa propuesta de 8-10 slides
- estructura de cierre
- riesgos narrativos
- `notes/phase-summary.md` actualizado con fase, estado, pasa/no pasa, resumen, rutas, hallazgos bloqueantes y siguiente accion
- `notes/.phase-narrative.done` escrito al finalizar en modo chat separado o worker separado
- decision: `listo para build` o `requiere ajuste`

Para cada slide, incluye tambien:

- concepto visual

No declares `listo para build` si alguna slide solo tiene objetos sueltos o cajas sin una idea visual clara.
