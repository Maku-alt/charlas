# Charlas SDD

Templates para trabajar charlas como specs encadenados y bajar consumo de contexto. El chat principal orquesta; las fases pesadas corren con paquetes acotados. El contrato repo-wide vive en `AGENTS.md`; la mecanica operativa vive en `agents/orchestrator-charlas.md`.

## Modos
Usa `full/` cuando la charla tenga tesis incierta, research externo, claims sensibles, audiencia importante o riesgo de framing:

1. `thesis-spec.md`
2. `research-spec.md`
3. `narrative-spec.md`
4. `image-spec.md`, si necesita imagen editorial final
5. `build-spec.md`
6. `review-spec.md`

Usa `compact/` cuando la charla sea pequena, tenga tesis clara o no tenga claims sensibles:

1. `research-package.md`
2. `build-package.md`
3. `review-package.md`

## Paquete de ejecucion
Cada fase pesada debe recibir:

- rol especializado, por ejemplo `agents/researcher-charlas.md`
- spec o package de fase
- prompt desde `templates/charlas-sdd/prompts/`
- artefactos necesarios
- `notes/phase-summary.md` como unico handoff operativo para el padre, salvo summaries temporales de `build` + `image-close` paralelos
- `model`, `reasoning_effort` y `fork_context: false` explicitos cuando se use subagente

El spec define el encargo concreto. El rol define metodologia y criterio de calidad. El prompt consume el spec y el paquete de ejecucion de esa fase, sin duplicar un handoff generico, y evita que avance automaticamente a otra etapa.

La imagen final puede correr como fase separada con `image-closer-charlas`; su salida alimenta build y review.

El feedback humano tambien es entrada SDD: `orchestrator-charlas` lo clasifica, relanza la fase afectada con paquete minimo y exige review nueva si cambia el deck o el cierre.

`modo chat separado` sigue el protocolo `skills/worker-handoff` y las reglas de `agents/orchestrator-charlas.md`: paquete acotado, summary en disco y sentinel escrito al final.

## Precondiciones
| Fase | Spec minimo | Artefactos minimos |
|---|---|---|
| thesis-review | `thesis-spec.md` | brief o tesis abierta, `run_id` y decision hacia `research` o `stop` |
| research | `research-spec.md` o package compacto | framing o tesis base |
| narrativa | `narrative-spec.md` | research aprobado |
| build | `build-spec.md` | `narrative-spec.md` aprobado, `notes/bibliografia.md` si hubo research |
| imagen final | `image-spec.md` | tesis, mensaje final, cita/fallback, tono y restricciones visuales |
| review | `review-spec.md` | deck exacto, sentinels previos requeridos, build report o evidencia de build, cierre visual cuando aplique, bibliografia y `notes/phase-summary.md` |

Si falta un spec obligatorio, no lances la fase. Corrige primero el contrato.

Para pasar de narrativa a build, el handoff debe incluir `concepto visual` por slide, ademas de titulo, objeto visible y takeaway.

Si hubo research externo, el handoff tambien debe incluir `notes/bibliografia.md`. Si corrio una fase pesada, debe quedar `notes/phase-summary.md` actualizado con el contrato v2 completo, incluyendo identidad de corrida, fase, estado de ejecucion, decision, veredicto de review, evidencia y siguiente accion.

## Phase summary
`notes/phase-summary.md` reemplaza cualquier bitacora operativa. Debe representar el estado actual y ser lo unico que el hilo padre lee para avanzar.

Formato minimo: usar exactamente `templates/charlas-sdd/phase-summary.md`. La combinacion de `Execution status`, `Decision` y `Review verdict` reemplaza campos ambiguos: una fase que termino pero requiere otra iteracion registra `completed`, `iterate` y el veredicto que corresponda.

No pegues outputs de comandos, renders, transcripts ni reportes completos en el padre. Escribe evidencia larga a archivos y referencia rutas.

## Worker separado
Usa `skills/worker-handoff` y `agents/orchestrator-charlas.md` para sentinels, summaries temporales, esperas y reglas de monitoreo. Estos templates solo definen insumos y salidas esperadas por fase.

## Build PPTX
Para decks `pptx` nuevos desde cero, usar por defecto el renderer local del repo en `scripts/deck_renderer/` desde `deck-spec.json`. El theme default es `scripts/deck_renderer/theme-charlas.json`.

La skill `pptx` queda solo para emergencia o diagnostico avanzado. Los detalles de build y QA viven en `scripts/deck_renderer/README.md`, `agents/deck-builder-charlas.md` y `agents/review-charlas.md`.

## Defaults
| Fase | Model | Reasoning effort | Salida esperada |
|---|---|---|---|
| research | `gpt-5.5` | `medium` | research discutible |
| narrativa | `gpt-5.5` | `medium` | narrativa aprobable |
| build | `gpt-5.4` | `medium` | `pptx` editable y evidencia |
| imagen final | `gpt-5.4` | `medium` | direccion visual o asset final |
| review | `gpt-5.4` | `medium` | veredicto sobre artefacto exacto |

## Bloqueo y continuidad
Una fase bloqueada debe devolver `Execution status: blocked`, la fase, hallazgos bloqueantes concretos, artefactos generados, evidencia de chequeos, riesgos residuales y una accion propuesta.

El padre decide `esperar`, `relanzar`, `volver a la fase anterior` o `escalar`. No completa la fase especializada desde fuera.

Ninguna fase avanza automaticamente a la siguiente. Cada output debe cerrar con una decision: seguir, reformular, profundizar o descartar.

## Compatibilidad v1
Workflow v2 applies to new or explicitly reopened talks. Existing v1 summaries remain readable but are not valid inputs for a new v2 transition until upgraded. Closed legacy talks are not migrated in bulk.
