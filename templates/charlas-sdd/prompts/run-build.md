# Prompt: Run Build

Estas ejecutando solo la fase `deck-builder-charlas`.

Precondicion del launch:

- este prompt debe ejecutarse junto con `agents/deck-builder-charlas.md`
- el archivo de rol especializado define el comportamiento; este prompt solo acota la fase

Usa solo:

- `Build Spec`
- `Narrative Spec` aprobado
- assets o referencias explicitamente incluidos

Usa la skill instalada `pptx` como capa de ejecucion. No reemplaces esa skill con rutas legacy.

Modelo sugerido para esta fase:

- `model`: `gpt-5.5`
- `reasoning_effort`: `medium`

Devuelve:

- ruta del `pptx`
- cantidad de slides
- concepto visual por slide
- renders individuales
- chequeo textual
- chequeos mecanicos
- estado de render nativo
- riesgos residuales
- entrada para `notes/agent-log.md` con fase, agente, modelo, esfuerzo, estado, artefactos, errores o bloqueos, y siguiente accion

No entregues build si varias slides quedan como grillas de cajas sin concepto visual. La ausencia de clipping no basta.

Si no puedes cerrar el build, no quedes en loop silencioso. Devuelve un reporte de bloqueo estructurado con:

- `Estado`: `bloqueado`
- `Fase`: `build`
- `Bloqueo concreto`
- `Artefactos generados`
- `Chequeos o comandos que fallaron`
- `Chequeos o comandos que si funcionaron`
- `Riesgos residuales`
- `Accion siguiente propuesta`

No hagas la review final salvo que el encargo indique modo compacto.

No delegues implicitamente el cierre del build al padre. O entregas `completado con artefacto`, o entregas `bloqueado con evidencia`, o indicas `requiere volver a fase anterior`.
