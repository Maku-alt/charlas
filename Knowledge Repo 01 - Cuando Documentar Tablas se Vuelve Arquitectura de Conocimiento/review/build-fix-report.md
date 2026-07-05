# Build Fix Report

Run id: `knowledge-repo-01-full-rebuild-20260704`

## Alcance

- Fase: `build-fix`
- Artefacto corregido: `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`
- SHA256 corregido: `3E16EE34E83748EE71CC050A53598E3388486078FF589F50B96CBBE6ADE85A4C`
- Slides corregidas: `1-9` para ortografia espanola; slide `3` para signos de apertura limpios.

## Hallazgos atendidos

### P2 textual en slides 1-9

- Review original: tildes y caracteres especiales degradados en palabras espanolas.
- Cambio aplicado: restauracion de tildes y caracteres en titulos, labels, takeaways, pies y fuentes visibles, sin cambiar narrativa, cantidad de slides ni layout.
- Criterio de aceptacion: extraccion textual sin mojibake ni patrones degradados objetivo.

### P2 mojibake en slide 3

- Review original: las cuatro tarjetas de pregunta contenian `Â¿`.
- Cambio aplicado: sustitucion por signos de apertura limpios en las cuatro tarjetas, preservando posiciones, conectores y estilo visual.
- Criterio de aceptacion: render nativo de slide 3 sin `Â` visible y sin overflow.

## QA ejecutado

- PowerPoint nativo: abre el PPTX corregido y exporta 9 slides.
- Conteo de slides: 9.
- Texto extraido actualizado: `review/extracted-text.txt`.
- Chequeo textual: 0 coincidencias para mojibake y patrones degradados objetivo.
- `slides_test.py`: pasa con `HOME=C:\Users\Victor`; no detecta overflow.
- Contact sheet PowerPoint nativo actualizado: `review/native-contact-sheet.png`.
- Renders PowerPoint nativo actualizados: `review/native-renders/`.

## Evidencia

- PPTX corregido: `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`
- Backup del candidato anterior: `review/knowledge-repo-01-full-rebuild-20260704/build-fix-original-backup.pptx`
- Texto extraido: `review/extracted-text.txt`
- Contact sheet nativo: `review/native-contact-sheet.png`
- Renders nativos: `review/native-renders/Diapositiva1.PNG` a `Diapositiva9.PNG`
- Copias normalizadas: `review/native-renders/slide-01.png` a `slide-09.png`

## Riesgos residuales

- Este build-fix no aprueba el deck final; deja un candidato corregido para `review-final`.
