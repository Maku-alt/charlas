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
- `notes/bibliografia.md` presente si hubo fuentes externas

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
- estado de bibliografia
- veredicto final


## QA visual PPTX
- PowerPoint nativo es el gate visual primario.
- Primero inspeccionar solo contact sheet PowerPoint nativo.
- Abrir slides individuales solo si el contact sheet muestra defecto.
- No hacer fixes visuales ni modificar el deck desde review.
- Si PowerPoint nativo falla, registrar bloqueo o continuar solo como review diagnostico si el usuario lo pidio.
- LibreOffice/Poppler son auxiliares, no gate de aprobacion.
