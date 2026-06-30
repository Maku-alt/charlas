# Prompt: Run Compact Build Review

Estas ejecutando una fase compacta de build y review para charla pequena.

Usa solo:

- `Build Review Package`
- research package aprobado
- assets o referencias explicitamente incluidos

Usa `pptx` como capa de ejecucion para construir el deck. Despues revisa el artefacto exacto producido.

Devuelve:

- ruta del `pptx`
- evidencia de build
- hallazgos de review
- riesgos residuales
- estado de `notes/bibliografia.md` y `notes/agent-log.md`
- entrada para `notes/agent-log.md` con fase, agente, modelo, esfuerzo, estado, artefactos, errores o bloqueos, y siguiente accion
- veredicto final: `aprobado` o `requiere cambios`
