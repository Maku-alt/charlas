# Prompt: Run Compact Review

Estas ejecutando solo la fase compacta de review para una charla pequena.

Usa solo:

- `Review Package`
- completed build summary
- exact candidate PPTX and its recorded SHA256
- build evidence and explicitly included assets

Antes de revisar, confirma que `worker_id` y `session_id` son distintos de los de build cuando se requiere independencia. Confirma que el SHA256 del candidato exacto coincide con el handoff. Revisa con `review-charlas`, genera un veredicto independiente y un reporte accionable si requiere cambios.

No modifiques el deck, el source, el candidato ni la evidencia de build. Publica el summary y sentinel de `review` exclusivamente con `scripts/agent_workflow/complete-phase.py`.

