# Prompt: Run Build

Estas ejecutando solo la fase `deck-builder-charlas`.

Precondicion del launch:

- este prompt debe ejecutarse junto con `agents/deck-builder-charlas.md`
- el archivo de rol especializado define el comportamiento; este prompt solo acota la fase

Usa solo:

- `Build Spec`
- `Narrative Spec` aprobado
- assets o referencias explicitamente incluidos
- si es `build-fix`: PPTX/source candidato actual, slides concretas a corregir, hallazgos accionables, criterio de aceptacion y rutas minimas indicadas por el orquestador

Para construir un deck `pptx` nuevo desde cero, usa por defecto el renderer local del repo en `scripts/deck_renderer/` desde `deck-spec.json` y `scripts/deck_renderer/theme-charlas.json`.

La skill `pptx` queda permitida solo como emergencia o diagnostico avanzado: inspeccion de PPTX, extraccion de texto, unpack/pack, reparacion puntual y diagnostico de XML/estructura cuando los scripts del repo no expliquen el fallo.

Modelo sugerido para esta fase:

- `model`: `gpt-5.4`
- `reasoning_effort`: `medium`

Regla para `modo chat separado` o hilo worker separado:

- el resultado operativo se comunica solo por archivos en disco
- sobrescribe `notes/phase-summary.md` con el estado actual de build
- escribe `notes/.phase-build.done` al terminar
- responde en chat solo `DONE: summary written` o `BLOCKED: summary written`
- no pegues el contenido del summary en chat
- no uses `agent-log.md`
- no escribas `phase-summary-build.md`
- deja evidencia pesada en `review/`, `assets/` o `slides/` y referenciala desde `notes/phase-summary.md`

Si este build corre en paralelo con `image-close`, escribe temporalmente `notes/.phase-build.summary.md` en vez de sobrescribir `notes/phase-summary.md`. Escribe igual `notes/.phase-build.done`; el padre consolidara cuando tambien exista `notes/.phase-image.done`.

Formato de `notes/phase-summary.md`: `Ultima fase`, `Estado` (`completado`, `requiere cambios` o `bloqueado`), `Pasa / no pasa`, `Resumen` de 1-3 frases, `Artefactos` con rutas, `Hallazgos bloqueantes` y `Siguiente accion`.

En build/review, `notes/phase-summary.md` debe indicar si el flujo esta en `build` o `build-fix`, artefacto candidato actual, artefacto final si existe, hallazgos bloqueantes restantes y siguiente accion.

Devuelve:

- ruta del `pptx`
- cantidad de slides
- concepto visual por slide
- contact sheet PowerPoint nativo; renders auxiliares si existen
- chequeo textual
- chequeos mecanicos
- estado de render nativo
- riesgos residuales
- `notes/phase-summary.md` actualizado con fase, estado, pasa/no pasa, resumen, rutas, hallazgos bloqueantes y siguiente accion
- `notes/.phase-build.done` escrito al finalizar en modo chat separado o worker separado

Si este encargo es `build-fix`:

- corrige solo las slides indicadas
- no relances build completo para hallazgos puntuales
- no rehagas research, narrativa ni image-close
- deja el PPTX/source corregido como artefacto candidato, no como final aprobado
- registra slides corregidas, hallazgos atendidos, criterio de aceptacion aplicado y rutas de evidencia
- deja `Siguiente accion: review-final`

No entregues build si varias slides quedan como grillas de cajas sin concepto visual. La ausencia de clipping no basta.

QA visual PPTX:

- PowerPoint nativo es el gate final de apertura/export.
- Primero inspecciona solo contact sheet PowerPoint nativo.
- Abre slides individuales solo si el contact sheet muestra defecto; en `build-fix`, abre solo slides afectadas y dependencias visuales directas.
- Haz maximo 1 ciclo de fix visual y 1 revalidacion PowerPoint nativo, salvo permiso explicito.
- Si PowerPoint nativo falla, haz maximo 1 intento acotado de fix; si persiste, registra bloqueo en `notes/phase-summary.md`.
- LibreOffice/Poppler son auxiliares, no gate de aprobacion; no apruebes por LibreOffice/Poppler.

Si no puedes cerrar el build, no quedes en loop silencioso. Devuelve un reporte de bloqueo estructurado con:

- `Estado`: `bloqueado`
- `Fase`: `build`
- `Bloqueo concreto`
- `Artefactos generados`
- `Chequeos o comandos que fallaron`
- `Chequeos o comandos que si funcionaron`
- `Riesgos residuales`
- `Accion siguiente propuesta`

No hagas la review final salvo que el encargo indique modo compacto. En `build-fix`, la review final siempre corresponde a `review-charlas`.

No delegues implicitamente el cierre del build al padre. O entregas `completado con artefacto`, o entregas `bloqueado con evidencia`, o indicas `requiere volver a fase anterior`.
