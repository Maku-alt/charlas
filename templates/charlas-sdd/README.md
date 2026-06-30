# Charlas SDD

Templates para trabajar charlas como specs encadenados y bajar consumo de contexto. El chat principal orquesta; las fases pesadas corren con paquetes acotados.

## Modos
Usa `full/` cuando la charla tenga tesis incierta, research externo, claims sensibles, audiencia importante o riesgo de framing:

1. `thesis-spec.md`
2. `research-spec.md`
3. `narrative-spec.md`
4. `build-spec.md`
5. `run-image-close.md`, si necesita imagen editorial final
6. `review-spec.md`

Usa `compact/` cuando la charla sea pequena, tenga tesis clara o no tenga claims sensibles:

1. `research-package.md`
2. `build-review-package.md`

## Paquete de ejecucion
Cada fase pesada debe recibir:

- rol especializado, por ejemplo `agents/researcher-charlas.md`
- spec o package de fase
- prompt desde `templates/charlas-sdd/prompts/`
- artefactos necesarios
- `model`, `reasoning_effort` y `fork_context: false` explicitos

El spec define el encargo concreto. El rol define metodologia y criterio de calidad. El prompt empaqueta la corrida y evita que avance automaticamente a otra etapa.

La imagen final puede correr como fase separada con `image-closer-charlas`; su salida alimenta build y review.

El feedback humano tambien es entrada SDD: `orchestrator-charlas` lo clasifica, relanza la fase afectada con paquete minimo y exige review nueva si cambia el deck o el cierre.

`modo chat separado` es fallback: el orquestador prepara el paquete, el usuario lo ejecuta en otro chat y devuelve solo el output compacto.

## Precondiciones
| Fase | Spec minimo | Artefactos minimos |
|---|---|---|
| research | `research-spec.md` o package compacto | framing o tesis base |
| narrativa | `narrative-spec.md` | research aprobado |
| build | `build-spec.md` | `narrative-spec.md` aprobado, `notes/bibliografia.md` si hubo research |
| imagen final | cierre en `narrative-spec.md` o `build-spec.md` | mensaje final, cita/fallback, tono |
| review | `review-spec.md` | deck exacto, build report o evidencia de build, renders, bibliografia y `notes/agent-log.md` |

Si falta un spec obligatorio, no lances la fase. Corrige primero el contrato.

Para pasar de narrativa a build, el handoff debe incluir `concepto visual` por slide, ademas de titulo, objeto visible y takeaway.

Si hubo research externo, el handoff tambien debe incluir `notes/bibliografia.md`. Si corrio una fase pesada, debe quedar una entrada en `notes/agent-log.md` con fase, agente, modelo, esfuerzo, estado, artefactos, errores o bloqueos, y siguiente accion.

## Defaults
| Fase | Model | Reasoning effort | Salida esperada |
|---|---|---|---|
| research | `gpt-5.5` | `medium` | research discutible |
| narrativa | `gpt-5.5` | `medium` | narrativa aprobable |
| build | `gpt-5.5` | `medium` | `pptx` editable y evidencia |
| imagen final | `gpt-5.5` | `medium` | direccion visual o asset final |
| review | `gpt-5.5` | `medium` | veredicto sobre artefacto exacto |

## Bloqueo y continuidad
Una fase bloqueada debe devolver `Estado`, `Fase`, `Bloqueo concreto`, `Artefactos generados`, chequeos fallidos y exitosos, riesgos residuales y accion propuesta.

El padre decide `esperar`, `relanzar`, `volver a la fase anterior` o `escalar`. No completa la fase especializada desde fuera.

Ninguna fase avanza automaticamente a la siguiente. Cada output debe cerrar con una decision: seguir, reformular, profundizar o descartar.
