# Review Report

Run id: `knowledge-repo-01-full-rebuild-20260704`

Artefacto revisado: `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`

SHA256: `A2D0CE76858A8FAF9B24E16F1ADA2B43566D72716345791F6F7A9EBFE870F76D`

Veredicto: `requiere cambios`

## Gates

- Cantidad de slides: 9, confirmada desde estructura interna del PPTX.
- Validacion mecanica: el PPTX contiene `ppt/presentation.xml`, `[Content_Types].xml` y 9 archivos `ppt/slides/slide*.xml`.
- Render completo: 9 renders auxiliares y 9 renders PowerPoint nativo disponibles.
- Gate PowerPoint nativo: `review/native-contact-sheet.png` y `review/native-renders/` usados como evidencia primaria.
- Contact sheet nativo: ritmo global aceptable, sin slide faltante ni defecto visual bloqueante de apertura.
- Slides 5, 7 y 9: inspeccionadas puntualmente; concepto, jerarquia y cierre editorial son aceptables.
- Texto extraido: falla por caracteres especiales y tildes ausentes.

## Hallazgos P1/P2

### Hallazgo 1

- slide: `1-9`
- severidad: `P2`
- problema observado: El texto del deck esta degradado a ASCII en palabras espanolas que deberian llevar tildes o ene con virgulilla. Ejemplos visibles en el texto extraido y renders: `documentacion`, `comun`, `metricas`, `util`, `explicita`, `estandar`, `indice`, `bitacora`, `canonica`, `decision`, `pequeno`, `paginas`.
- criterio incumplido: `review-spec.md` exige verificar tildes, signos de apertura y caracteres especiales, y define que no debe haber mojibake, caracteres sustituidos, texto cortado ni solapamientos.
- cambio minimo sugerido: Ejecutar un `build-fix` textual sobre todas las slides para restaurar ortografia espanola en titulos, labels, takeaways, pies y fuentes, sin cambiar narrativa, layout ni concepto visual.
- rutas de evidencia: `review/extracted-text.txt`; `review/native-contact-sheet.png`; `review/native-renders/slide-01.png`; `review/native-renders/slide-03.png`; `review/native-renders/slide-07.png`; `review/native-renders/slide-09.png`.

### Hallazgo 2

- slide: `3`
- severidad: `P2`
- problema observado: Las tarjetas de preguntas de la slide 3 contienen mojibake en el signo de apertura de pregunta: aparece un caracter `U+00C2` antes del signo invertido. El defecto es visible en el render nativo y esta presente en `review/extracted-text.txt`.
- criterio incumplido: `review-spec.md` indica que no debe haber mojibake ni caracteres sustituidos; `review-charlas` clasifica mojibake como P2.
- cambio minimo sugerido: Corregir solo el texto de las cuatro tarjetas de pregunta de slide 3, preservando las posiciones, conectores y estilo visual. Confirmar que los signos de apertura se renderizan como signos invertidos limpios y que no se introduce overflow.
- rutas de evidencia: `review/native-renders/slide-03.png`; `review/native-contact-sheet.png`; `review/extracted-text.txt`.

## Hallazgos P3

Ninguno que bloquee el flujo. La composicion de slides 5, 7 y 9 es suficientemente clara para el objetivo editorial. Slide 9 usa imagen protagonista, mantiene aire para el mensaje y no presenta la frase editorial como cita atribuida.

## Decision

No se aprueba el deck por P2 textual. Los hallazgos son puntuales y corregibles por `build-fix`; no requieren rehacer narrativa, research ni cierre de imagen.
