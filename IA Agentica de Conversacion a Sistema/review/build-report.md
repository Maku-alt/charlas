# Build Report

## Resultado

Build generado y verificado.

## Artefactos

- PPTX final: `IA-Agentica-De-Conversacion-A-Sistema.pptx`
- Script fuente: `slides/build-deck-python.py`
- Asset de cierre usado: `assets/closing-workbench-right.jpg`
- Texto extraido: `review/extracted-text.txt`
- Contact sheet: `review/contact-sheet.png`
- Renders nativos iniciales: `review/native-renders/Diapositiva1.PNG` a `Diapositiva9.PNG`
- Renders nativos finales post-feedback: `review/feedback-renders/Diapositiva1.PNG` a `Diapositiva10.PNG`

## Workflow

- Workflow usado: build desde cero con `python-pptx`.
- Motivo: la ruta inicial con `PptxGenJS` produjo PPTX que PowerPoint COM rechazo con `0x80070570`; la ruta `python-pptx` valida y abre correctamente en PowerPoint.
- Imagen final: generada como bitmap editorial, convertida a JPG RGB y recortada para la mitad derecha del cierre.

## Verificaciones

### Validacion mecanica

Comando:

```powershell
python C:\Users\Victor\.codex\skills\pptx\scripts\office\validate.py "IA Agentica de Conversacion a Sistema\IA-Agentica-De-Conversacion-A-Sistema.pptx"
```

Resultado:

```text
All validations PASSED!
```

### Conteo y texto

Comando:

```powershell
python -c "<python-pptx text/layout check>"
```

Resultado:

```text
slides 9
out_of_bounds 0
replacement False
mojibake False
key_text_ok True
```

Nota: este conteo corresponde al primer build. Despues del cambio solicitado, la version final aprobada tiene 10 slides y fue revisada en `review/review-formal-feedback-pass.md`.

Tildes verificadas por texto extraido con `python-pptx`: `conversación`, `análisis`, `revisión`, `pequeños`, `documentación`.

### Render nativo PowerPoint

Comando:

```powershell
$pres.Export($out, 'PNG', 1920, 1080)
```

Resultado:

```text
slides=9
```

PowerPoint exporto 9 PNGs nativos en `review/native-renders/`.

La pasada final post-feedback exporto 10 PNGs nativos en `review/feedback-renders/`.

### QA visual

Primer pase detecto dos problemas:

- Slide 7: lineas diagonales cruzaban etiquetas y reducian legibilidad.
- Slide 9: la imagen de cierre no se veia; PowerPoint exportaba la mitad derecha negra.

Correcciones aplicadas:

- Slide 7 se cambio a flujo horizontal con hitos y tarjetas, sin lineas diagonales largas.
- Slide 9 usa `assets/closing-workbench-right.jpg`, un recorte RGB compatible, sin overlay negro.
- Se corrigio un out-of-bounds menor de la imagen en slide 9.

Segundo pase:

- Contact sheet final generada en `review/contact-sheet.png`.
- Slide 7 legible sin cruces sobre texto.
- Slide 9 renderiza la imagen editorial y mantiene el mensaje/cita legibles.

## Riesgos residuales

- Los renders alternativos por LibreOffice no se usaron porque el wrapper `soffice.py` fallo en Windows con `socket.AF_UNIX`.
- La revision final independiente post-feedback se ejecuto con `review-charlas` y aprobo el artefacto de 10 slides en `review/review-formal-feedback-pass.md`.
- `slides/` y `assets/` son artefactos locales no versionables por defecto segun `.gitignore`.

## Decision

Build inicial listo para review; version final post-feedback aprobada.
