# PPTX Renderer Smoke Results

Date: 2026-07-05

## Environment

- Node: `v24.12.0`
- npm: `11.12.1`
- Python: `3.11.9`
- `pptxgenjs`: `4.0.1`
- PowerPoint native COM: available

## Files

- `pptxgenjs-smoke.pptx`
- `python-pptx-smoke.pptx`
- `pptxgenjs-real-deck.pptx`
- `native-export-pptxgenjs-smoke/Diapositiva1.PNG` to `Diapositiva3.PNG`
- `native-export-python-pptx-smoke/Diapositiva1.PNG` to `Diapositiva3.PNG`
- `native-export-pptxgenjs-real-deck/Diapositiva1.PNG` to `Diapositiva9.PNG`
- `pptxgenjs-real-deck-contact-sheet.png`

## Validation

| renderer | generation | PowerPoint open/export | slides | PNG export | nonblank PNG |
|---|---|---:|---:|---:|---:|
| `pptxgenjs` | ok | ok | 3 | 3 | 3 |
| `python-pptx` | ok | ok | 3 | 3 | 3 |
| `pptxgenjs-real-deck` | ok | ok | 9 | 9 | 9 |

## Conclusion

The previous `pptxgenjs` failure (`PowerPoint COM 0x80070570`) did not reproduce. A simple `pptxgenjs` deck with Spanish text, shapes, and a local PNG opens and exports correctly through native PowerPoint. A more realistic 9-slide deck driven by `real-deck-spec.json` also opens and exports correctly.

This does not prove every future `pptxgenjs` deck is safe. It proves the library/runtime combination can produce PowerPoint-compatible files in this environment, including a 9-slide deck close to the repo style. The next useful step is to promote the test renderer into shared scripts with fixed dependencies and QA gates.
