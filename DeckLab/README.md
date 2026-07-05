# DeckLab

Purpose: preserve the renderer learning/demo that proved `pptxgenjs` can create PowerPoint-compatible decks for this repo.

Acceptance criterion: PowerPoint native COM opens the generated `.pptx` and exports all slides to PNG without repair.

Run:

```powershell
cd DeckLab
npm install
python python-pptx-smoke.py
npm run build:pptxgenjs
npm run build:real
powershell -ExecutionPolicy Bypass -File .\validate-powerpoint.ps1 -PptxPath .\python-pptx-smoke.pptx
powershell -ExecutionPolicy Bypass -File .\validate-powerpoint.ps1 -PptxPath .\pptxgenjs-smoke.pptx
powershell -ExecutionPolicy Bypass -File .\validate-powerpoint.ps1 -PptxPath .\pptxgenjs-real-deck.pptx
```

The reusable renderer lives in `scripts/deck_renderer/`.
