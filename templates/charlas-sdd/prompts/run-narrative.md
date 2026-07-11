# Prompt: Run Narrative

Estas ejecutando solo la fase `narrative-charlas`.

Precondicion del launch:

- este prompt debe ejecutarse junto con `agents/narrative-charlas.md`
- el archivo de rol especializado define el comportamiento; este prompt solo acota la fase

Usa solo:

- `Narrative Spec`
- research aprobado o research brief incluido

No construyas el `pptx`. No hagas review final.

Para una corrida aislada, usa el paquete de ejecución y `agents/workflow-contract.json`. Publica el summary y el sentinel de `narrative` exclusivamente con `scripts/agent_workflow/complete-phase.py`; nunca escribas, reutilices ni comuniques sentinels manualmente.

Devuelve:

- tesis propuesta
- lectura narrativa
- audiencia y cambio esperado
- comparacion o tension central
- narrativa propuesta de 8-10 slides
- estructura de cierre
- riesgos narrativos
- publicación validada de `narrative` conforme al paquete de ejecución
- decision: `listo para build` o `requiere ajuste`

Para cada slide, incluye tambien:

- concepto visual

No declares `listo para build` si alguna slide solo tiene objetos sueltos o cajas sin una idea visual clara.
