# Build Report

## Estado

- fase: build fix puntual slide 9
- agente: deck-builder-charlas
- estado: completado con artefacto
- fecha local: 2026-06-28
- deck canonico: `Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`
- SHA256 deck canonico: `8DE296CFD8D33583EAC370917D2439137B97D4CD265F1A6DBD64CDFA53964585`
- slides: 9

## Fixes aplicados

- Slide 6: se movio el rotulo `lineage` fuera del subtitulo y se rerutearon conectores hacia los bordes del bloque central para evitar cruces sobre el texto.
- Slide 5: se reforzo la jerarquia de labels perifericos (`review`, `freshness`, `owner`, `riesgo`) con borde/color mas claro sin agregar conectores que compitan con el loop.
- Slide 8: se agrego una fila de responsabilidades (`fuente`, `uso`, `control`, `paquete`, `consulta`) para hacer mas explicita la asignacion por capa sin volver a una matriz plana.
- Slide 9: se elimino el claim superior, el bloque editorial intermedio y el takeaway/footer; quedo solo la cita breve de John Gruber con atribucion.

## Workflow

- workflow `pptx`: edicion del build PptxGenJS existente.
- cierre bitmap preservado/regenerado localmente con Pillow en `assets/closing-knowledge-repo.png`.
- renderer PDF: LibreOffice `C:\Program Files\LibreOffice\program\soffice.exe`.
- renderer nativo: PowerPoint COM export a PNG.

## Comandos relevantes

```powershell
python "Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento\slides\generate-closing-image.py"
node "Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento\slides\build-knowledge-repo-01.js"
& "C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf --outdir "Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento\review" "Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento\Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx"
& "C:\Users\Victor\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe" -png -r 150 -f 9 -l 9 "Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento\review\Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pdf" "Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento\review\renders\slide"
```

## Evidencia generada

- texto extraido directo del XML del PPTX: `review/extracted-text.md`
- PDF: `review/Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pdf`
- render PDF refrescado para slide 9: `review/renders/slide-9.png`
- evidencia nativa previa preservada, no refrescada en este fix puntual: `review/native-renders/`, `review/native-contact-sheet.png`
- contact sheet PDF previo preservado, no refrescado en este fix puntual: `review/contact-sheet.png`
- evidencia puntual del fix: `review/slide-9-feedback-fix.md`

## Chequeos

- PPTX empaquetado: 9 slides.
- Texto: `replacement_chars=0`; los dos signos de apertura de pregunta se preservan como U+00BF.
- PDF LibreOffice generado correctamente. LibreOffice emitio el warning `Could not find platform independent libraries <prefix>`, pero produjo PDF valido.
- Render PDF puntual generado con Poppler desde binario real del runtime: slide 9.
- No se refresco render nativo PowerPoint en este fix puntual.
- La evidencia previa de slides 5, 6 y 8 no fue modificada en esta ola.
- Inspeccion visual puntual PDF en slide 9: solo quedan cita y atribucion; no queda claim superior, bloque editorial intermedio ni takeaway/footer.

## Riesgos residuales

- No se hizo review final completa por instruccion explicita; solo QA puntual de slide 9.
- El cierre bitmap sigue siendo ilustracion procedural local, no imagen generativa fotorrealista; cumple direccion editorial y no fue modificado conceptualmente en esta ola.
