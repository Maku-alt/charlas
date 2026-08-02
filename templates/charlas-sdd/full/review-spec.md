# Review Spec - Web Talk

## Target

- ruta exacta del HTML candidato;
- SHA256;
- fuente y commit o identidad de build;
- narrativa, speech y bibliografia aprobados.

## Evidencia requerida

- un render por momento;
- lint, test y build;
- self-audit;
- pruebas de navegacion, teclado, fullscreen, consola, assets, overflow, accesibilidad y offline.

## Gates

- identidad exacta entre candidato, hash, renders y evidencia;
- tesis, revelacion, ritmo, apertura y cierre;
- legibilidad y concepto visual por momento;
- controles, teclado, foco, reduced motion y viewport;
- ausencia de errores runtime, scroll primario, assets rotos y claims sin soporte;
- reviewer distinto del builder.

## Salida

Veredicto, hallazgos P1/P2/P3, `review-report.md`, `fix-list.json` si aplica y `notes/phase-summary.md`. Review no modifica el candidato.
