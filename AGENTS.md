# AGENTS

Contrato operativo corto para este repo de charlas.

## Contexto repo-wide
- Cada carpeta de primer nivel suele ser una charla, salvo infraestructura como `agents/`, `templates/`, `scripts/`, `skills/` y carpetas ocultas.
- Audiencia por defecto: gente que trabaja con datos, usualmente `Data Scientists`.
- Tono por defecto: ejecutivo, tecnico, directo y claro.
- No amarrar la narrativa a telco salvo pedido explicito.
- Verifica con fuentes actuales cualquier claim sobre precios, releases, compatibilidad, costos actuales o casos corporativos recientes.

## Flujo base
Toda charla pasa por tesis, research cuando haga falta, convergencia con el usuario, narrativa de `8-10 slides`, build `pptx`, cierre visual y review.

El research no pasa automaticamente a PPT: primero se discute, se recorta y se fija el angulo.

Cada slide debe tener tesis, lectura ejecutiva, objeto visible y concepto visual. Si varias slides quedan como cajas, tablas o conectores sin idea visual clara, vuelve a narrativa o build antes de aprobar.

## Donde vive cada regla
- Roles especializados: `agents/*.md`.
- Mapa de roles, paquetes y dependencias: `agents/README.md`.
- Orquestacion de fases, prechecks, workers, sentinels y ciclo de correccion: `agents/orchestrator-charlas.md`.
- Specs y prompts SDD reutilizables: `templates/charlas-sdd/`.
- Renderer local, theme default y comandos de build/QA: `scripts/deck_renderer/README.md`.
- Ejemplo de `deck-spec.json`: `templates/deck-renderer/deck-spec.example.json`.
- Protocolo repo-local de workers separados: `skills/worker-handoff`.

## Agentes
- `orchestrator-charlas`: decide fase, dependencias, launch, workers y bloqueo.
- `researcher-charlas`: investiga, tensiona tesis y entrega research discutible.
- `narrative-charlas`: convierte research convergido en narrativa aprobable.
- `deck-builder-charlas`: construye decks `pptx` y fixes puntuales.
- `image-closer-charlas`: define imagen editorial de cierre.
- `review-charlas`: valida deck, texto, visuales, cierre y evidencia.

No omitas el rol especializado: el prompt de fase no reemplaza `agents/*.md`.

## Estructura por charla
Convencion recomendada hacia adelante:

- `specs/`: specs SDD copiados o adaptados desde `templates/charlas-sdd/`
- `notes/`: narrativa, claims, material validado, `bibliografia.md` y `phase-summary.md`
- `slides/` o `deck/`: fuente editable y exportables locales
- `assets/`: imagenes, prompts visuales y recursos de soporte
- `review/`: observaciones, ajustes y chequeos finales

No migres charlas antiguas salvo que se reabran. `slides/` y `assets/` deben existir localmente cuando la charla los necesite, pero por defecto no se suben al remoto.

Si hubo research externo, `notes/bibliografia.md` es obligatorio. Si corrio una fase pesada, `notes/phase-summary.md` debe existir y representar el estado actual.

## Specs SDD
La metodologia vive en `templates/charlas-sdd/`.

- Usa `full/` para charlas normales o complejas: `thesis-spec.md`, `research-spec.md`, `narrative-spec.md`, `build-spec.md` y `review-spec.md`.
- Usa `compact/` para charlas pequenas o con framing claro: `research-package.md` y `build-review-package.md`.
- Usa los prompts de `templates/charlas-sdd/prompts/` para acotar cada fase.

## Build PPTX
Para decks `pptx` nuevos desde cero, el build normal usa el renderer local del repo:

`deck-spec.json` -> `scripts/deck_renderer/render-deck.js` -> `scripts/deck_renderer/qa-deck.py` -> `scripts/deck_renderer/validate-powerpoint.ps1`

El theme default es `scripts/deck_renderer/theme-charlas.json`. Los detalles de instalacion, dependencias y comandos viven en `scripts/deck_renderer/README.md`.

La skill `pptx` queda solo para emergencia o diagnostico avanzado: inspeccion, extraccion, unpack/pack, reparacion puntual y diagnostico XML/estructura cuando los scripts del repo no expliquen el fallo.

## Workers y handoff
No cambies la politica de workers desde este archivo. Para `modo chat separado` o hilos worker separados, sigue `skills/worker-handoff` y `agents/orchestrator-charlas.md`.

Reglas repo-wide minimas:

- el padre observa archivos, no chats worker ni `read_thread`
- `notes/phase-summary.md` es el handoff operativo oficial, salvo summaries temporales permitidos para `build` + `image-close` paralelos
- la finalizacion se verifica con `Test-Path` sobre el sentinel esperado
- el worker escribe el sentinel al terminar y responde solo `DONE: summary written` o `BLOCKED: summary written`
- `fork_context: false` es el default para subagentes

Los tiempos de espera, sentinels, limpieza de sentinels viejos, consolidacion de summaries temporales y bloqueo de workers viven en `agents/orchestrator-charlas.md` y el protocolo `skills/worker-handoff`.

## Gates de cierre
El entregable primario es un `pptx` editable compatible con PowerPoint nativo.

Una charla no se cierra sin tesis clara, comparacion o tradeoff, lectura ejecutiva, cierre editorial fuerte, bibliografia si hubo fuentes externas, `notes/phase-summary.md` actualizado y review aprobada del artefacto exacto.

PowerPoint nativo es el gate final de apertura/export. Los detalles de QA visual corresponden a `deck-builder-charlas`, `review-charlas` y `scripts/deck_renderer/README.md`; LibreOffice/Poppler son auxiliares y no aprueban build.
