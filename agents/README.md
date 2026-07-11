# Agentes de Charlas

Esta carpeta contiene roles especializados. El chat principal usa `orchestrator-charlas` para preparar el paquete de fase y no debe absorber el trabajo pesado de cada rol.

## Roles
- `orchestrator-charlas`: coordina fase, dependencias, launch, paralelizacion y bloqueos.
- `researcher-charlas`: investiga, tensiona tesis y devuelve research discutible.
- `narrative-charlas`: convierte research convergido en narrativa de `8-10 slides`.
- `deck-builder-charlas`: construye decks `pptx` nuevos con el renderer local del repo desde `deck-spec.json` y evidencia de QA; `pptx` queda solo para emergencia o diagnostico avanzado.
- `image-closer-charlas`: define metafora e imagen editorial de cierre.
- `review-charlas`: valida el artefacto exacto antes de cerrar.
- `advisor-charlas`: recomienda sobre tradeoffs transversales complejos; no es fase ni tiene autoridad de gate, aprobación, bloqueo o mutación.

## Fuentes de verdad

| Concern | Canonical source |
|---|---|
| Repo principles | `AGENTS.md` |
| Phases, transitions, sentinels | `agents/workflow-contract.json` |
| Runtime preferences | `agents/runtime-defaults.json` |
| Role method and quality bar | `agents/<role>.md` |
| Advisory request and recommendation | `templates/charlas-sdd/advisor-request.md` and `<talk>/notes/advice/` |
| Talk-specific requirements | `<talk>/specs/*.md` |
| Worker launch boundary | `templates/charlas-sdd/prompts/*.md` |
| Current operational state | `<talk>/notes/phase-summary.md` |

`advisor-charlas` solo se activa por un trigger complejo documentado. Su evidencia queda en `<talk>/notes/advice/`; no escribe ni reemplaza el handoff operacional `notes/phase-summary.md`.

`agents/runtime-defaults.json` contiene preferencias de runtime, no reglas de validez del workflow. Si un modelo solicitado no esta disponible, solo puede usarse un fallback cuando el paquete de ejecucion registre el modelo solicitado y el modelo realmente usado. El orquestador hereda el modelo activo del thread; este archivo no cambia por si solo el thread padre. Consulta ese archivo para los defaults vigentes.

## Paquete de fase
Cada fase pesada debe ejecutarse con contexto acotado:

- rol especializado desde `agents/*.md`
- spec desde `specs/` o `templates/charlas-sdd/`
- prompt desde `templates/charlas-sdd/prompts/`
- artefactos previos estrictamente necesarios
- `notes/phase-summary.md` como handoff operativo, salvo summaries temporales de `build` + `image-close` paralelos
- `model`, `reasoning_effort` y `fork_context: false` explicitos cuando se use subagente

El rol no es opcional. Por ejemplo, narrativa requiere `agents/narrative-charlas.md` ademas de `narrative-spec.md` y `run-narrative.md`.

## Mapeo rapido
`agents/workflow-contract.json` define el mapeo completo y vigente de fases, roles, specs, prompts, transiciones y sentinels. No copies esa tabla a documentos operativos.

## Dependencias
- `narrative-charlas` depende de research o tesis convergida.
- `deck-builder-charlas` depende de narrativa aprobada.
- `image-closer-charlas` depende de tesis, mensaje final, cita real de referente o fallback justificado, y tono claros.
- `review-charlas` depende de deck parcial o final, cierre y evidencia de build.
- Si hay duda sobre fase o dependencias, empezar por `orchestrator-charlas`.

`deck-builder-charlas` e `image-closer-charlas` pueden correr en paralelo solo si mensaje final, cita/fallback y direccion de cierre ya existen o se fijan antes.

En hilos worker separados, el padre sigue `skills/worker-handoff` y las reglas concretas de `orchestrator-charlas`: verifica sentinels con `Test-Path`, no usa `read_thread` ni chat worker, y consolida summaries temporales solo en la bifurcacion `build` + `image-close`.

## Artefactos obligatorios
- Si hubo research externo, debe existir `notes/bibliografia.md`.
- Si corrio cualquier fase pesada, debe existir `notes/phase-summary.md`.
- `phase-summary.md` debe ser escueto y contener la version del contrato, identidad de corrida, fase, estado de ejecucion, decision, veredicto de review, artefactos, evidencia, bloqueos y siguiente accion.
- El padre lee solo `phase-summary.md` para decidir transiciones. La evidencia pesada queda referenciada por rutas. No usar `agent-log.md` como handoff operativo.

## Gates de calidad
Una deck no esta terminada solo porque existe un `pptx`. El flujo exige:

- texto espanol correcto y `UTF-8` sin mojibake
- chequeos mecanicos de archivo y layout
- PowerPoint nativo como gate final de apertura/export para `pptx`, segun `deck-builder-charlas`, `review-charlas` y `scripts/deck_renderer/README.md`
- LibreOffice/Poppler solo como auxiliares
- rechazo de solapamiento, clipping o corrupcion visible aunque los checkers no reporten errores
- rechazo de decks mecanicamente correctas pero pobres: slides sin concepto visual, exceso de grillas o cierre sin imagen editorial real
- bibliografia y `notes/phase-summary.md` completos para las fases ejecutadas

`deck-builder-charlas` produce evidencia. `review-charlas` valida de forma independiente. `orchestrator-charlas` impide cerrar si hay hallazgos bloqueantes.

## Uso
- Si llega feedback humano sobre una fase o deck existente, empieza por `orchestrator-charlas`; el orquestador clasifica y relanza el rol que corresponda.
- Usa `researcher-charlas` si falta tesis, evidencia o angulo.
- Usa `narrative-charlas` si toca decidir historia, slide order, titulos-conclusion y cierre antes de construir.
- Usa `deck-builder-charlas` si la narrativa ya fue discutida y toca construir el `pptx`.
- Usa `image-closer-charlas` si el cierre necesita una imagen editorial fuerte.
- Usa `review-charlas` si ya existe artefacto concreto y toca decidir si se aprueba o itera.

## Operacion local
- Build normal de decks nuevos: renderer local desde `deck-spec.json`.
- Si `soffice` no aparece en `PATH`, usar `scripts/resolve-soffice.ps1` o `C:\\Program Files\\LibreOffice\\program\\soffice.exe`.
- Los specs y prompts reutilizables viven en `templates/charlas-sdd/`.
