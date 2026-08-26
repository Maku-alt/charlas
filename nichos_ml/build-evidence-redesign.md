# Build evidence — `pysubgroup`

Estado: candidato listo para review independiente. No se modifica `nichos_ml/release/**`.

## Dirección ejecutada

- Concepto: pizarra de búsqueda clara; el promedio queda como línea de referencia y una ventana azul/naranja vuelve visible una combinación.
- Evidencia dominante: comparación contextual, flujo de API y una única transformación teórica de churn.
- Paleta: fondo frío claro `#f5f7fb`, carbón `#101828`, azul intenso `#155eef`, naranja `#f97316`.
- Apertura: `pysubgroup` aparece en marca, título y promesa desde el primer momento.
- Gesto memorable: `4% global → regla interpretable → 12% en un nicho teórico`.
- Cierre: una sola idea y una visual protagonista de promedio frente a combinación visible.
- Se evita: mesa/papel vegetal, azul petróleo/celeste apagado, ranking numérico, benchmark, ejecución en vivo y dependencia de red.

## Artefactos

- Candidato: `nichos_ml/candidate/pysubgroup.html`
- Fuente reproducible: `nichos_ml/src/index.template.html`, `nichos_ml/src/styles.css`, `nichos_ml/src/app.js`, `nichos_ml/src/build.ps1`
- Build: `& .\\nichos_ml\\src\\build.ps1`
- Renders desktop 1600×900: `nichos_ml/renders/redesign/01-desktop.png` … `07-desktop.png`
- Renders móvil 390×844: `nichos_ml/renders/redesign/01-mobile.png` … `07-mobile.png`
- QA reproducible: `nichos_ml/src/qa_redesign.py`
- No se usan imágenes externas ni hotlinks. El cierre usa geometría SVG inline para respetar la restricción del handoff de no crear/reutilizar una imagen conceptual de papel; el candidato sigue autocontenido y offline.

## Momentos

1. `pysubgroup` y la pregunta de dónde mirar; regla genérica y ventana de contraste.
2. Cuatro lentes sobre la misma población: segmento manual, clustering, modelo global y Subgroup Discovery.
3. Flujo grande `selectors → target → quality function → search → resultado`, con `BinaryTarget`, `StandardQF`, `DFS / Beam Search` y `MinSupportConstraint`.
4. Comparativo grande; el veredicto contextual visible declara que gana `pysubgroup` para Python 3.10 + caso práctico.
5. Único ejemplo de churn: 4% global, regla exacta con reclamos/indisponibilidad/contrato mensual, nicho 12%, soporte 6%, contraste 3× y advertencia de no causalidad.
6. Límites y extensión: multiplicidad, soporte, solapamiento, asociación ≠ causalidad, Beta/NumPy y `SoftClassifierTarget + SubROC`.
7. Cierre con una sola frase: “No buscamos otro promedio. Buscamos la combinación que merece atención.”

## Checks ejecutados

- Build: PASS; genera `pysubgroup.html` y CSS/JS inline.
- Playwright headless sobre Chrome del sistema: PASS en 1600×900 y 390×844.
- Momentos: PASS; 7 momentos, uno visible por vez.
- Navegación: PASS; botones 01–07, anterior/siguiente, `Home`, `End`, `ArrowLeft`, `ArrowRight`, `PageUp`, `PageDown`.
- Posición directa: PASS; `#moment-5` abre el momento 5 y el hash se actualiza al navegar.
- Interacciones: PASS; espacio recorre lentes/arquitectura y enfatiza el ejemplo; `R` reinicia el estado determinista.
- Consola/page errors: PASS; `errors: []` en ambas viewports.
- Overflow: PASS; `1600×900` y `390×844` reportan `scrollWidth/scrollHeight` iguales al viewport.
- Offline/assets: PASS; no hay `<img>`, hojas externas ni scripts con `src`; SVG del cierre es inline.
- Fullscreen: PASS a nivel de control; botón visible, etiqueta ARIA dinámica y fallback de error implementado. La entrada real de fullscreen no se certifica en Chromium headless.
- Accesibilidad estática: PASS; idioma `es`, headings etiquetados, `aria-label`/`aria-current`, focus-visible y `prefers-reduced-motion`.
- Detector mecánico Impeccable: PASS; salida `[]` en la única ejecución sobre template, CSS, JS y candidato.
- Inspección visual: PASS; cada uno de los 7 momentos se inspeccionó individualmente en desktop y móvil después de capturar la ronda final.

## Hash

`SHA-256 nichos_ml/candidate/pysubgroup.html`  
`BFE8BA5477EBD8B1847A592B4BC7D75BB50194E5F3349CBDC8FA4A74B6319AAE`

## Self-audit y riesgos residuales

- Self-audit: cumple nombre de archivo, presencia inmediata de `pysubgroup`, comparativo y ganador contextual, ejemplo teórico único, paleta clara, controles, teclado, fullscreen, foco, reduced motion y operación sin red.
- Riesgo residual 1: el candidato no demuestra que una regla observacional sea causal; la advertencia está visible y la acción se limita a revisar/replicar.
- Riesgo residual 2: la compatibilidad Python 3.10 y las limitaciones de versiones pertenecen a la evidencia de research; este artefacto no ejecuta la librería.
- Riesgo residual 3: en móvil, momentos densos usan desplazamiento interno para mantener controles de presentación fijos; la navegación principal sigue siendo lineal/directa.
- Riesgo residual 4: falta la revisión independiente sobre este hash exacto. El Build no aprueba su propio artefacto.
