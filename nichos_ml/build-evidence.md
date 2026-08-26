# Build evidence · 2026-08-25

## Candidate

- Canonical frontend: `candidate/index.html`
- Reproducible source: `src/index.template.html`, `src/styles.css`, `src/app.js`, `src/build.ps1`
- Build command: `powershell -ExecutionPolicy Bypass -File nichos_ml/src/build.ps1`
- SHA-256: `8EBA95E45CFD95B18BD82965CDCF54FE1DD12631F0A2B57E79B5EE47DA072F4A`
- Presentation: 16:9, 1600×900 evidence renders; seven addressable moments.

## Reproducible demo

`tools/generate_demo.py` generated two independent 11,000-row windows with seeds `20260826` (discovery) and `20260827` (holdout), no `risk_niche` column, correlated but non-identical complaints/outages, noise, and a bounded selector space over complaints, outages, tenure, contract and plan. The actual run used `BinaryTarget("churn", True)`, `StandardQF(1)`, `BeamSearch(beam_width=50)`, depth `3`, and `MinSupportConstraint(0.02)`.

Observed discovery rule:

`contract_type=='month-to-month' AND outages_90d>=3 AND plan_type=='basic'`

- Discovery: global `4.0636%`; `n=467`, support `4.2455%`, subgroup `6.8522%`, lift `1.6862×`, difference `+2.7886 pp`, quality `0.0009194`.
- Independent holdout: global `4.0818%`; `n=519`, support `4.7182%`, subgroup `5.0096%`, lift `1.2273×`, difference `+0.9278 pp`; direction retained.
- Full output: `data/demo-result.json`; source rows: `data/discovery.csv`, `data/holdout.csv`.

`tools/run-smoke.ps1` completed in a clean isolated Python `3.10.11` venv at `%TEMP%\\nichos_ml_pysubgroup_smoke_20260826`. It installed and exercised `pysubgroup 0.9.0`, `numpy 1.26.4`, `scikit-learn 1.7.2`, `pandas 2.2.3`, `scipy 1.14.1`, `matplotlib 3.9.4`, and `statsmodels 0.14.5`. No global environment was mutated; the deterministic rule and metrics matched the prior run exactly.

## QA

- `tools/qa_browser.py` with Playwright Chromium from `file://`, 1600×900: 7/7 renders captured and individually inspected in `renders/01.png`–`renders/07.png`.
- Navigation: visible previous/next; direct position buttons 01–07; Arrow/Page keys, Home/End; boundary clamped.
- Interaction: Space/Enter inner states for M1/M2/M3/M4; M1 cancels its ambient animation on reveal; M2 cycles A–D coherently; M4 reveals four semantic evidence stages with focus; `R` deterministic reset; presentation navigation is not trapped.
- Fullscreen: `document.fullscreenEnabled === true` in Chromium; control is visible and synchronizes visible text and accessible name on enter/exit.
- Assets: local `assets/registration-sheet.svg` loaded; no network assets or hotlinks.
- Console: no console errors or page errors.
- Layout: no horizontal/vertical overflow at 1600×900; 10 semantic buttons; six inactive moments hidden.
- Accessibility: visible focus ring, button labels/aria-current, headings focus on position changes, reduced-motion CSS verified (`1e-05s` transition in Chromium emulation).
- Detector: ran once at finish on source and candidate. Result `[]`; detector reported degraded regex fallback because `htmlparser2`, `css-select`, `css-tree`, and `domutils` were unavailable, so this is an undercount rather than a clean parser-backed bill.

## Residual risks

- Python 3.10.11 was smoke-tested directly with the pinned dependency window.
- The demo values are synthetic and observational; the visual explicitly labels them synthetic and association ≠ causality.
- Candidate is ready for fresh independent review. Do not mutate `candidate/index.html` after review begins; recalculate the hash if any fix is authorized.
