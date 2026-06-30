# Build Report

## Artefacto final

- PPTX versionable: `SDD-IAgentica/SDD-IAgentica-v2.pptx`
- PPTX fuente local: `SDD-IAgentica/slides/SDD-IAgentica-v2.pptx`
- Slides: 9
- SHA256: `DCA25F0C473F937402FC56D89C09AB1C682433D800F031BB5BB62AB111F4A00C`

## Workflow usado

- Build desde cero con `python-pptx`.
- Script editable local: `SDD-IAgentica/slides/build_deck.py`.
- Diseno alineado con `STYLE-CHARLAS.md`: fondo claro, tinta oscura, acento naranja, paneles marfil y cierre editorial.
- Benchmark propio documentado en `SDD-IAgentica/notes/token-benchmark.md`.
- Bibliografia documentada en `SDD-IAgentica/notes/bibliografia.md`.
- Imagen final generada previamente con `image_gen` y copiada a `SDD-IAgentica/assets/closing-background.png`.
- Imagen final estabilizada para render con LibreOffice como `SDD-IAgentica/assets/closing-background-style.jpg`.

## Comandos principales

```powershell
python SDD-IAgentica\slides\build_deck.py
python -m markitdown SDD-IAgentica\slides\SDD-IAgentica-v2.pptx > SDD-IAgentica\review\extracted-text-v2.txt
rg -n "xxxx|lorem|ipsum|TODO|TBD|BIBLIOGRAFIA|Bibliografia|Spectral" SDD-IAgentica\review\extracted-text-v2.txt
& 'C:\Program Files\LibreOffice\program\soffice.exe' --headless --convert-to pdf --outdir 'C:\Users\Victor\Proyectos\2026\charlas\SDD-IAgentica\review' 'C:\Users\Victor\Proyectos\2026\charlas\SDD-IAgentica\slides\SDD-IAgentica-v2.pptx'
& 'C:\Users\Victor\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe' -jpeg -r 150 'SDD-IAgentica\review\SDD-IAgentica-v2.pdf' 'SDD-IAgentica\review\render-v2'
```

## Renders

- PDF LibreOffice: `SDD-IAgentica/review/SDD-IAgentica-v2.pdf`
- JPG render Poppler: `SDD-IAgentica/review/render-v2-1.jpg` a `SDD-IAgentica/review/render-v2-9.jpg`
- Contact sheet: `SDD-IAgentica/review/contact-sheet-v2-style.jpg`

## Chequeo textual

- Extracto textual: `SDD-IAgentica/review/extracted-text-v2.txt`
- Resultado: 9 slides detectadas.
- Resultado: sin placeholders, bibliografia embebida ni marcadores de mojibake en el texto extraido por `markitdown` y revisado con `rg`.

## Chequeo visual

- La review v2 style detecto tres defectos materiales:
  - slide 9: la imagen final no se veia en el render LibreOffice;
  - slide 5: texto secundario del callout con bajo contraste;
  - slide 8: contraste bajo y numeros de pasos demasiado chicos.
- Correcciones aplicadas:
  - se uso `closing-background-style.jpg` para render estable de la imagen final;
  - se subio contraste y tamano de los textos afectados;
  - se agrandaron los cuadrados numerados en slide 8.
- Contact sheet final revisada: sin cortes, solapamientos bloqueantes ni texto fuera de caja.

## Nota sobre versiones

- `SDD-IAgentica-v2.pptx` es la version final valida.
- La version posterior sin dependencia de `STYLE-CHARLAS.md` fue una prueba y no reemplaza el artefacto final del repo.

## Riesgos residuales

- El benchmark usa aproximacion `caracteres / 4`; sirve para orden de magnitud, no como auditoria exacta por tokenizer.
