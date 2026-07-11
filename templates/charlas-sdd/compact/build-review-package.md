# Build Review Package

Usa este paquete para construir y revisar una charla pequena con narrativa ya clara.

## Narrativa fuente
<ruta o resumen del research-package aprobado>

## Slides esperadas
- cantidad:
- tesis por slide:
- cierre:

## Sistema visual
- tono visual:
- densidad:
- paleta:
- uso de imagenes:
- tratamiento de cierre:

## Build esperado
- pptx editable
- build de decks nuevos con el renderer local del repo desde `deck-spec.json`
- theme default: `scripts/deck_renderer/theme-charlas.json`
- skill `pptx` permitida solo como emergencia o diagnostico avanzado: inspeccion, extraccion, unpack/pack, reparacion puntual o diagnostico XML/estructura
- contact sheet PowerPoint nativo; renders auxiliares si existen
- `notes/phase-summary.md` actualizado
- chequeo textual
- chequeos mecanicos
- PowerPoint nativo como gate final de apertura/export

## Review gates
- tesis clara
- titulos con conclusion
- sin clipping ni solapamientos
- texto correcto sin mojibake
- cierre fuerte
- identidad del archivo revisado
- bibliografia y `notes/phase-summary.md` requeridos presentes
- sentinels requeridos presentes

## Salida esperada
- ruta del pptx
- evidencia de build
- hallazgos de review
- estado de bibliografia y `notes/phase-summary.md`
- veredicto final

## Handoff worker separado
- usar un paquete de ejecución separado por cada fase canónica y `agents/workflow-contract.json`
- publicar cada summary y su sentinel exclusivamente con `scripts/agent_workflow/complete-phase.py`
- no combinar ni escribir, reutilizar o comunicar sentinels manualmente; cada paquete define identidad y transporte

## QA visual PPTX
- PowerPoint nativo es el gate final de apertura/export.
- Primero inspeccionar solo contact sheet PowerPoint nativo.
- Abrir slides individuales solo si el contact sheet muestra defecto.
- Maximo 1 ciclo de fix visual y 1 revalidacion PowerPoint nativo, salvo permiso explicito.
- Si PowerPoint nativo falla despues de un fix acotado, registrar bloqueo en `notes/phase-summary.md`.
- LibreOffice/Poppler son auxiliares, no gate de aprobacion; no aprueban build.
