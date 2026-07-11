# Prompt: Run Thesis Review

Estas ejecutando solo la fase `thesis-review` para una charla.

Usa solo el `Thesis Spec` y el `Execution Package` recibidos. No avances a research, narrativa ni build: solo deja la transicion declarada para que el orquestador la ejecute.

El `run_id`, la decision y la transicion deben coincidir entre el spec, el paquete y el phase summary. Para `advance`, la unica transicion es `research`; para `stop`, la transicion es `stop`.

Publica el summary y `.phase-thesis-review.done` exclusivamente mediante `scripts/agent_workflow/complete-phase.py` despues de validar el summary. Nunca escribas ni reutilices un sentinel manualmente.

Devuelve:

- lectura de la tesis, riesgos de framing y preguntas abiertas
- cambios sugeridos al `Thesis Spec`
- `notes/phase-summary.md` con el `run_id`, fase, estado, decision, evidencia, hallazgos bloqueantes y siguiente fase
- publicacion atomica validada de `thesis-review`
- decision: `advance` hacia `research` o `stop`

No devuelvas explicaciones fuera de ese formato.
