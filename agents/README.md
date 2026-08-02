# Agentes de Charlas

El chat principal orquesta; los custom agents TOML bajo `.codex/agents/` ejecutan fases especializadas y cargan estos contratos Markdown como metodo de trabajo.

## Roles vigentes

- `orchestrator-charlas`: hilo principal; decide fase, dependencias, handoff, fix y release.
- `researcher-charlas`: evidencia, contradicciones, claims y bibliografia.
- `narrative-charlas`: tesis, arco, momentos, speech y contrato visual/contenido.
- `experience-designer-builder-charlas`: sistema visual, experiencia, imagenes, frontend, QA y fixes localizados.
- `review-charlas`: gate independiente del candidato exacto.
- `advisor-charlas`: recomendacion excepcional sin autoridad de fase.

`experience-designer-builder-charlas` reemplaza a los antiguos `deck-builder-charlas` e `image-closer-charlas`. Apertura, cierre e imagenes forman parte de una sola experiencia y no son fases separadas.

## Fuentes de verdad

| Concern | Canonical source |
|---|---|
| Principios del repo | `AGENTS.md` |
| Fases y transiciones | `agents/workflow-contract.json` |
| Runtime solicitado | `agents/runtime-defaults.json` |
| Metodo de rol | `agents/<role>.md` |
| Configuracion nativa | `.codex/agents/*.toml` |
| Requisitos de charla | `<talk>/specs/*.md` |
| Estado actual | `<talk>/notes/phase-summary.md` |

Los defaults de runtime expresan preferencia, no disponibilidad. Cada corrida registra modelo solicitado y modelo real. Mientras Luna no este habilitada para `spawn_agent`, los TOML usan Terra X-High como fallback operativo.

## Handoff

Cada worker recibe solo objetivo, rol, spec, inputs necesarios, outputs permitidos, criterios de aceptacion, runtime y politica de acceso externo. El worker devuelve un resumen compacto y evidencia por rutas; no vuelca logs ni depende del historial completo del padre.

El builder produce evidencia y self-audit. El reviewer repite los gates criticos de forma independiente. El orquestador publica exclusivamente el candidato aprobado por hash.
