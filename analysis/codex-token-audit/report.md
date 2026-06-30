# Codex Token Audit Report

## 1. Executive summary

- Diagnostico principal: el consumo extremo no vino de generar texto visible ni de rehacer una PPT en si; vino de input/contexto acumulado y reenviado muchas veces.
- La hipotesis del orquestador leyendo o reteniendo demasiado contexto queda confirmada en una forma concreta: el hilo principal acumulo roles, prompts, specs, `agent-log`, evidencia y handoffs, y luego tuvo checkpoints de ~180k-195k tokens casi todos como cached input. No queda probado que haya recibido el historial completo de subagentes.
- La sesion mas anomala (`rollout-2026-06-28T14-19-34-019f0fac-2c1d-74a0-ad8d-7323e42c5980.jsonl`) registro 17.79M tokens, 17.74M input, 16.81M cached input, 938k uncached input y solo 42k output.
- La cadena multiagente multiplico el costo: el hilo padre hizo 14 `spawn_agent`, 31 `wait_agent`, 12 `close_agent` y 127 checkpoints; ademas hubo subhilos hijos con costos propios.
- `view_image` fue un amplificador real en sesiones de review visual, pero no explica la sesion principal mas cara: esa sesion tuvo mayormente `exec_command`, `spawn_agent`, `wait_agent` y `close_agent`, no `view_image`.

## 2. Evidence inventory

| Archivo/ruta | Tipo de evidencia | Que muestra | Relevancia para consumo de tokens |
|---|---|---|---|
| `C:\Users\Victor\Documents\Codex\2026-06-29\importante-esta-tarea-es-para-diagnosticar\outputs\codex-usage-audit\diagnosis_report.md` | Reporte previo | Totales, rankings, hipotesis y limites | Base cuantitativa: 45.8M tokens en 19 sesiones |
| `...\usage_sessions_summary.csv` | CSV de sesiones | Totales por sesion, parent/child threads, tools, ratios | Reconstruye hilo principal vs subagentes |
| `...\usage_checkpoints_all.csv` | CSV de checkpoints | Saltos incrementales por checkpoint | Confirma saltos de ~180k-195k tokens casi todos cached |
| `...\function_calls_summary.csv` | CSV de tools | Conteos y tamano de outputs por herramienta | Distingue `view_image` vs `exec_command` vs multi-agent |
| `C:\Users\Victor\.codex\sessions\2026\06\28\rollout-2026-06-28T14-19-34-019f0fac-2c1d-74a0-ad8d-7323e42c5980.jsonl` | JSONL de sesion principal | Hilo padre con multi-agent, checkpoints y handoffs | Sesion raiz del mayor consumo |
| `C:\Users\Victor\.codex\sessions\2026\06\28\rollout-2026-06-28T14-24-17...` a `23-48-09...` | JSONL de subhilos | Threads hijos con `parent_thread_id` del hilo principal | Evidencia de fan-out multiagente |
| `C:\Users\Victor\.codex\config.toml` | Config Codex | `multi_agent=true`, modelo/effort globales, sin `agents.max_threads` ni `max_depth` visibles | No hay limites explicitos detectados |
| `AGENTS.md` | Regla repo | Fases pesadas por defecto como subagente, `fork_context:false`, `agent-log` obligatorio en el diseno auditado | Diseno observado favorece subagentes y trazabilidad, pero el log amplio aumenta superficie de contexto |
| `agents/orchestrator-charlas.md` | Rol orquestador | Pide paquete acotado, no heredar historial, handoffs y bloqueo | Contrato correcto en intencion, debil en limites duros |
| `templates/charlas-sdd/README.md` | Metodologia SDD | Full/compact, paquete por fase, fallback chat separado | Confirma objetivo de bajar contexto |
| `Knowledge Repo 01...\notes\agent-log.md` | Log historico del flujo auditado | Registra research, narrativa, image-close, build, review, fix | Evidencia de que el mecanismo anterior se volvio dependencia frecuente; el diseno futuro lo reemplaza por `phase-summary.md` escueto |
| `Knowledge Repo 01...\review\contact-sheet.png`, `native-contact-sheet.png`, `renders\`, `native-renders\` | Evidencia visual | Renders y contact sheets usados en build/review | Amplifican costo cuando entran por `view_image` |
| `analysis/codex-token-audit/session_event_summary.csv` | Resumen generado | Conteos de eventos/tools/keywords por JSONL | Corrobora uso de multi-agent y acumulacion de outputs |
| `analysis/codex-token-audit/keyword_snippets.csv` | Resumen generado | Muestras truncadas de eventos relevantes | Evidencia local sin pegar JSONL completo |

## 3. Session usage reconstruction

| Sesion/hilo | Fase inferida | Input tokens | Cached input | Uncached input | Output | Observacion | Posible causa del salto |
|---|---:|---:|---:|---:|---:|---|---|
| `14-19-34...` padre | Orquestacion multiagente | 17,744,669 | 16,806,656 | 938,013 | 42,104 | 127 checkpoints, 182 calls, 14 spawn, 31 wait, 12 close | Prefijo enorme repetido + handoffs/agent-log en padre |
| `04-20-31...` | Build/review visual anterior | 5,576,155 | 5,307,904 | 268,251 | 34,960 | 5 `view_image`, 2.1M chars de tool output | Visual review + outputs grandes |
| `03-56-18...` | Setup/metodologia SDD | 3,875,434 | 3,577,984 | 297,450 | 33,814 | Muchas referencias a agents/templates/memory | Lectura de contratos, skills y specs |
| `22-19-12...` hijo | Review visual/fix | 3,642,156 | 3,356,416 | 285,740 | 18,899 | 16 `view_image`, 2.25M chars de outputs | Renders inspeccionados repetidamente |
| `22-02-07...` hijo | Build/review/fix | 3,019,059 | 2,693,632 | 325,427 | 27,835 | 4 `view_image`, 71 calls | Build + evidencia visual |
| `04-57-31...` | SDD/contratos | 2,105,249 | 1,918,976 | 186,273 | 19,063 | 57 calls, full specs hits | Lectura/relectura de specs y agentes |
| `14-37-06...` hijo | Review/render | 2,050,470 | 1,851,648 | 198,822 | 14,200 | 2 `view_image`, 1.03M chars output | Contact sheet/renders |
| `22-50-56...` hijo referencia | Review visual | 935,959 | 807,168 | 128,791 | 6,500 | 11 `view_image`, 2.17M chars output | Caso de referencia: caro por visuales, menor que padre |

Limites: la reconstruccion usa `usage_sessions_summary.csv` y `usage_checkpoints_all.csv` como fuente primaria. Los JSONL locales permiten correlacionar eventos, pero no explican la facturacion interna ni prueban si `wait_agent` devuelve historial completo o resumen enriquecido.

En la sesion padre, los mayores saltos fueron checkpoints 122-127: ~193k-195k tokens por checkpoint, con ~192k-194k cached input y solo cientos o pocos miles uncached. Eso es el patron de un prefijo grande ya cacheado que se reenvia en cada turno.

## 4. Orchestrator/subagent context flow

Flujo esperado:

1. El orquestador lee solo rol, spec, prompt y artefactos estrictamente necesarios.
2. Lanza subagente con `fork_context:false` y contexto acotado.
3. El subagente trabaja aislado.
4. El padre recibe solo resumen compacto, estado y rutas de artefactos.
5. El padre decide `pasa/no pasa`, relanza fase o escala.

Flujo observado:

1. El hilo principal arranca con un prefijo grande: instrucciones base, developer/app context, skills, plugins, memoria resumida y AGENTS del repo.
2. Antes de la orquestacion se leyeron skills completas como `brainstorming`, `subagent-driven-development` y `verification-before-completion`, y luego roles completos de `agents/*.md`, specs y prompts.
3. La sesion padre lanzo multiples subagentes y conservo en su transcript los `spawn_agent`, `wait_agent`, `close_agent`, outputs de comandos, rutas, `agent-log` y estados.
4. `notes/agent-log.md` se volvio una dependencia frecuente; aparece como keyword 150 veces en la sesion padre anomala.
5. Renders/contact sheets no dominaron la sesion padre, pero si dominaron sesiones hijas de review visual mediante `view_image`.
6. Cada turno posterior del padre reenvio un contexto que ya rondaba ~180k-195k tokens. La mayor parte fue cached input, pero siguio acumulando consumo de cuota.

La brecha es clara: el contrato auditado dice "contexto acotado", pero no hay enforcement cuantitativo de tamano de handoff, numero de subagentes, numero de waits, ni politica para no incorporar outputs pesados al hilo padre. El cambio acordado es que el flujo nuevo ya no use log historico como contrato: cada fase actualiza `phase-summary.md`, un archivo unico, sobrescribible y escueto que contiene solo resumen, pasa/no pasa, rutas y siguiente accion.

## 5. Root cause analysis

| Causa | Clasificacion | Evidencia |
|---|---|---|
| historical phase log in main thread | likely | En el flujo auditado, `agent-log` aparece repetidamente en el padre y se usa como evidencia de fase |
| verbose subagent handoffs | likely | 31 `wait_agent`, 12 `close_agent`; el padre conserva outputs y decisiones |
| repeated context packs | confirmed | Saltos de ~180k-195k cached input por checkpoint |
| full session history replay | likely | Patron de cached input gigante; no se prueba historial completo de subagentes |
| binary/PPT extraction repeated | possible | Build/review leen extracted text, build reports y PPT evidence; no se ve PPT binario serializado completo |
| image/render outputs repeated | confirmed para subhilos, unlikely como causa principal del padre | `view_image` domina sesiones de review; padre caro no depende de `view_image` |
| too many concurrent subagents | possible | Hay fan-out de hijos; no se ve max concurrency exacta |
| too much agent depth | possible | Parent/child existe; no se detecto profundidad mayor a un nivel en los datos revisados |
| reviewer reading everything | likely | En el flujo auditado, review exige renders completos, log historico, bibliography, build report, PPT exacto |
| prompt cache hiding actual repeated input cost | confirmed | 16.81M cached input de 17.74M input en padre |
| view_image as visual review cost amplifier | confirmed | Sesiones con 9-16 `view_image` generan 1.8M-2.25M chars de tool output |
| SDD contract not enforcing actual token isolation | confirmed | El contrato pide acotar, pero no limita bytes/tokens ni evita acumulacion en padre |

## 6. Recommendations

### Immediate changes

- Para una PPT de 8-10 slides con narrativa ya cerrada, usar single-agent + skill `pptx`; no lanzar build como subagente salvo que el padre este vacio o sea chat separado.
- Usar `notes/phase-summary.md` como contrato unico entre fases. El padre solo lee ese archivo.
- Cambiar handoff de subagentes a un summary operativo: estado, pasa/no pasa, resumen de 1-3 frases, rutas de artefactos, hallazgos bloqueantes y siguiente accion. Sin outputs de comandos ni snippets largos.
- Pasar rutas a renders y contact sheets, no imagenes ni outputs visuales al padre. El reviewer puede inspeccionar, pero devuelve solo defectos concretos.
- Evitar `wait_agent` repetido. Una espera por subagente y un cierre; si no termina, bloqueo estructurado y stop.

### Structural changes

- Convertir SDD en un sistema de artefactos, no de transcript: cada fase actualiza `phase-summary.md` compacto y el padre solo lee ese resumen.
- Usar `phase-summary.md` como archivo sobrescribible o de estado actual, no como append infinito. La historia completa no debe ser requisito del flujo.
- Usar `compact/` por defecto para charlas pequenas o con framing claro; reservar `full/` para research incierto o claims sensibles.
- Separar "evidencia pesada" de "decision de transicion": builds/reviews pueden producir mucho, pero el orquestador solo necesita `pass/fail`, defectos P1/P2 y rutas.
- Review visual en dos pasos: contact sheet una vez para screening, inspeccion puntual de slides riesgosas, y solo entonces render individual.
- No usar subagentes para correcciones pequenas de deck; hacer fix single-agent y review humana/manual posterior cuando el problema es puntual.

### Codex config changes

- Revisar si Codex permite `agents.max_threads` y `agents.max_depth`; no estan en `C:\Users\Victor\.codex\config.toml`.
- Considerar deshabilitar `multi_agent` por defecto para este repo o usarlo solo en sesiones creadas especificamente para research/review.
- Probar `fork_context:true` si la semantica disponible realmente aisla el subagente del padre; hoy `fork_context:false` no fue una proteccion efectiva de cuota.
- Limitar subagentes a research cuando haya preguntas independientes o review cuando se necesite independencia real. Build de PPT no deberia fan-out.

### Prompt contract changes

- Orquestador: "Usa solo `notes/phase-summary.md` para decidir transiciones. Maximo 500-800 tokens de contexto por transicion."
- Subagentes: "Actualiza `notes/phase-summary.md`; escribe evidencia larga a archivos separados; no pegues comandos completos en la respuesta final."
- Reviewer: "No reportes inspeccion slide-by-slide completa salvo defectos; devuelve tabla de hallazgos y veredicto. Renders quedan como rutas."
- Trazabilidad: "La trazabilidad del flujo nuevo vive en `phase-summary.md` y en rutas a evidencia pesada. Si se requiere auditoria historica, se reconstruye desde artefactos y reportes, no desde un log leido por el padre."
- Handoff: "Formato fijo en `phase-summary.md`: `ultima fase`, `estado`, `pasa/no pasa`, `resumen`, `artefactos`, `hallazgos bloqueantes`, `siguiente accion`; maximo 300-500 palabras."
- Revision visual PPT: "Usar contact sheet una vez; `view_image` individual solo para slides con riesgo. Nunca pasar imagenes al orquestador."

Formato recomendado para `notes/phase-summary.md`:

```md
# Phase Summary

## Ultima fase
build

## Estado
completado | requiere cambios | bloqueado

## Pasa / no pasa
pasa

## Resumen
1-3 frases maximo.

## Artefactos
- `ruta/al/pptx`
- `review/build-report.md`
- `review/contact-sheet.png`

## Hallazgos bloqueantes
- Ninguno

## Siguiente accion
Lanzar review sobre el PPTX canonico.
```

## 7. Proposed safe patch plan

- Fase 1: hardening de prompts/contratos. Editar `AGENTS.md`, `agents/orchestrator-charlas.md`, `agents/README.md` y `templates/charlas-sdd/README.md` para declarar `phase-summary.md` como unico archivo operativo del padre.
- Fase 2: limites de handoffs. Ajustar `run-build.md`, `run-review.md`, `deck-builder-charlas.md` y `review-charlas.md` para que evidencia pesada vaya a archivos y cada fase actualice `notes/phase-summary.md` con formato escueto.
- Fase 3: configuracion de subagentes. Definir politica repo: subagentes opt-in, no default para build; evaluar `multi_agent=false` o max depth/threads si Codex lo soporta.
- Fase 4: prueba controlada. Ejecutar una tarea pequena de deck con 3 variantes: single-agent, subagente con handoff compacto, modo chat separado.
- Fase 5: comparacion antes/despues. Medir input, cached input, uncached input, output, checkpoints, tool outputs y numero de waits; aprobar solo si el padre queda muy por debajo de 1M total tokens.

## 8. Final verdict

El problema no esta en SDD como metodologia conceptual. Esta en la orquestacion/context management: SDD definio fases sanas, pero la implementacion dejo que el hilo principal acumulara demasiada evidencia, handoffs, `agent-log`, herramientas y resultados.

No conviene eliminar subagentes de forma total; conviene restringirlos. Usalos cuando aporten independencia real: research paralelo, review independiente o tareas con contexto claramente separable. Para build de PPT, especialmente cuando la narrativa ya esta encaminada, el patron recomendado es single-agent con `pptx`, evidencia en archivos y revision humana/manual o review muy compacta despues.

Para tareas tipo PPT: tesis y narrativa pueden estar en specs; build deberia correr en un hilo fresco o single-agent con paquete minimo; review debe producir solo defectos accionables y rutas a evidencia. El padre solo debe leer `phase-summary.md`; no debe ser un repositorio de todo lo que paso.

Para una PPT ya encaminada, si ya hay narrativa y build-spec, conviene saltar directo a la skill `pptx` en modo controlado y hacer una revision posterior acotada. Relanzar todo el pipeline de subagentes para una correccion visual o un rebuild de 8-10 slides es desproporcionado en tokens.
