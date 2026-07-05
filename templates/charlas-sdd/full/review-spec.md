# Review Spec

## Artefacto a revisar
<ruta exacta del pptx o deck>

## Modo de review
- `review`: revision inicial del artefacto candidato
- `review-final`: revision posterior a un unico `build-fix`

Review no modifica el deck. Si devuelve `requiere cambios`, produce reporte accionable; el orquestador decide si relanza `build-fix` o bloquea.

## Gates narrativos
- tesis clara
- titulos con conclusion
- secuencia coherente
- cierre fuerte

## Gates visuales
- concepto visual claro por slide
- variacion compositiva suficiente
- no exceso de cajas o grillas repetidas
- jerarquia clara
- sin clipping
- sin solapamientos
- tablas legibles
- contraste correcto
- cierre con imagen protagonista bien recortada y cita real atribuida si usa formato de cita

## Gates tecnicos
- texto correcto
- sin mojibake
- numero de slides correcto
- contact sheet PowerPoint nativo
- identidad del archivo revisado
- sentinels previos requeridos presentes
- `notes/bibliografia.md` presente si hubo fuentes externas
- `notes/phase-summary.md` presente y actualizado
- en modo chat separado o worker separado, `notes/.phase-review.done` escrito al terminar

## Severidad
- P1: bloquea presentacion
- P2: debilita de forma material
- P3: mejora fina

## Salida esperada
- hallazgos priorizados
- si hay `requiere cambios`, `review-report` en `review/` con hallazgos accionables por slide: `slide`, `severidad`, `problema observado`, `criterio incumplido`, `cambio minimo sugerido` y `rutas de evidencia`
- resumen de review
- slides mas debiles
- slides sin concepto visual suficiente
- riesgos residuales
- estado de bibliografia y `notes/phase-summary.md`
- veredicto final

## Handoff worker separado
- unico handoff operativo: `notes/phase-summary.md`
- sobrescribir `notes/phase-summary.md` con el estado actual de review
- escribir `notes/.phase-review.done` al terminar
- responder en chat solo `DONE: summary written` o `BLOCKED: summary written`
- no usar `agent-log.md`
- no escribir `phase-summary-review.md`
- formato de `notes/phase-summary.md`: `Ultima fase`, `Estado` (`completado`, `requiere cambios` o `bloqueado`), `Pasa / no pasa`, `Resumen` de 1-3 frases, `Artefactos` con rutas, `Hallazgos bloqueantes` y `Siguiente accion`
- en build/review, `notes/phase-summary.md` debe indicar flujo (`build`, `build-fix`, `review` o `review-final`), artefacto candidato actual, artefacto final si existe, hallazgos bloqueantes restantes y siguiente accion
- si la review inicial devuelve `requiere cambios`, `Siguiente accion` debe ser `orquestador decide build-fix o bloqueo`
- si `review-final` no pasa, registrar bloqueo explicito; no abrir otro ciclo salvo autorizacion explicita del usuario

## QA visual PPTX
- PowerPoint nativo es el gate visual primario.
- Primero inspeccionar solo contact sheet PowerPoint nativo.
- Abrir slides individuales solo si el contact sheet muestra defecto.
- No hacer fixes visuales ni modificar el deck desde review.
- Si PowerPoint nativo falla, registrar bloqueo o continuar solo como review diagnostico si el usuario lo pidio.
- LibreOffice/Poppler son auxiliares, no gate de aprobacion.
