# Prompt: Run Compact Build

Estas ejecutando solo la fase compacta de build para una charla pequena.

Usa solo:

- `Build Package`
- research package o narrativa aprobada
- assets o referencias explicitamente incluidos

Construye el PPTX editable con el renderer local desde `deck-spec.json` y `scripts/deck_renderer/theme-charlas.json`. Ejecuta los chequeos mecanicos y la validacion nativa de PowerPoint. Registra `Workflow mode: compact`, el SHA256 del candidato exacto y publica el summary y sentinel de `build` exclusivamente con `scripts/agent_workflow/complete-phase.py`.

No revises, no apruebes el deck y no ejecutes review. Entrega el handoff completo para una fase `review` independiente: summary de build terminado, ruta del candidato exacto, SHA256 y evidencia.
