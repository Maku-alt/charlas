# Charlas Deck Renderer

Renderer local para construir PPTX editables desde `deck-spec.json`.

Este es el build normal para decks nuevos del repo. La skill `pptx` queda para emergencia o diagnostico avanzado.

Theme default: `scripts/deck_renderer/theme-charlas.json`.

## Install

```powershell
cd scripts\deck_renderer
npm install
```

`node_modules/` no se versiona. `package-lock.json` si debe versionarse para fijar `pptxgenjs@4.0.1`.

## Render

```powershell
node scripts\deck_renderer\render-deck.js `
  templates\deck-renderer\deck-spec.example.json `
  outputs\example.pptx
```

Flujo normal:

1. narrativa aprobada
2. `deck-spec.json`
3. `render-deck.js`
4. `qa-deck.py`
5. `validate-powerpoint.ps1`
6. review del artefacto exacto

## QA

```powershell
python scripts\deck_renderer\qa-deck.py `
  outputs\example.pptx `
  --spec templates\deck-renderer\deck-spec.example.json `
  --render-dir outputs\example-native `
  --contact-sheet outputs\example-contact-sheet.png `
  --report outputs\example-qa.json
```

`qa-deck.py` es un gate mecanico. Cero warnings es necesario, no suficiente: el build debe revisarse visualmente.

## PowerPoint Gate

```powershell
powershell -ExecutionPolicy Bypass `
  -File scripts\deck_renderer\validate-powerpoint.ps1 `
  -PptxPath outputs\example.pptx
```

PowerPoint nativo es el gate final de apertura/export. LibreOffice/Poppler pueden ayudar como diagnostico auxiliar, pero no aprueban un build.

## Text Patch

```powershell
python scripts\deck_renderer\patch-pptx-text.py `
  --pptx outputs\example.pptx `
  --out outputs\example-patched.pptx `
  --slide 3 `
  --replace "texto viejo" `
  --with "texto nuevo"
```

Usa `patch-pptx-text.py` solo para fixes textuales quirurgicos. Para cambios de contenido o layout, corrige `deck-spec.json` o el renderer y regenera.
