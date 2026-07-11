# Prompt: Run Compact Build Review

Estas ejecutando una fase compacta de build y review para charla pequena.

Usa solo:

- `Build Review Package`
- research package aprobado
- assets o referencias explicitamente incluidos

Para construir un deck `pptx` nuevo desde cero, usa por defecto el renderer local del repo en `scripts/deck_renderer/` desde `deck-spec.json` y `scripts/deck_renderer/theme-charlas.json`. Despues revisa el artefacto exacto producido.

La skill `pptx` queda permitida solo como emergencia o diagnostico avanzado: inspeccion de PPTX, extraccion de texto, unpack/pack, reparacion puntual y diagnostico de XML/estructura cuando los scripts del repo no expliquen el fallo.

Modelo sugerido para esta fase compacta:

- `model`: `gpt-5.4`
- `reasoning_effort`: `medium`

Para una corrida aislada, usa paquetes de ejecución separados para cada fase canónica y `agents/workflow-contract.json`. Publica cada summary y su sentinel exclusivamente con `scripts/agent_workflow/complete-phase.py`; nunca combines ni escribas, reutilices o comuniques sentinels manualmente.

QA visual PPTX:

- PowerPoint nativo es el gate final de apertura/export.
- Primero inspecciona solo contact sheet PowerPoint nativo.
- Abre slides individuales solo si el contact sheet muestra defecto.
- Haz maximo 1 ciclo de fix visual y 1 revalidacion PowerPoint nativo, salvo permiso explicito.
- Si PowerPoint nativo falla despues de un fix acotado, registra bloqueo en `notes/phase-summary.md`.
- LibreOffice/Poppler son auxiliares, no gate de aprobacion; no apruebes por LibreOffice/Poppler.

Devuelve:

- ruta del `pptx`
- evidencia de build
- hallazgos de review
- riesgos residuales
- estado de `notes/bibliografia.md` y evidencia de cada fase declarada
- publicaciones validadas de las fases declaradas conforme a sus paquetes de ejecución
- veredicto final: `aprobado` o `requiere cambios`
