# Charlas de Data Science

Este repositorio agrupa materiales para distintas charlas relacionadas con Data Science, analitica aplicada y el uso practico de datos.

## Documentos raiz
- `README.md`: explicacion humana del repositorio
- `maestro_charlas.md`: indice vivo de charlas trabajadas, estado, tesis y entregables principales
- `AGENTS.md`: instrucciones persistentes para el agente al trabajar en estas charlas
- `STYLE-CHARLAS.md`: sistema visual y narrativo compartido entre presentaciones
- `agents/`: agentes especializados para investigar temas y construir decks de este repo

## Proposito
Las charlas de este repo estan pensadas para data scientists y equipos tecnicos que trabajan con datos, modelos, experimentacion, automatizacion y mejores practicas de trabajo.

Los temas pueden incluir, por ejemplo:

- actualizaciones relevantes del stack clasico de Python para Data Science
- nuevas tecnicas de modelado, evaluacion y optimizacion
- buenas practicas para experimentacion, reproducibilidad y explicabilidad
- uso de agentes, LLMs y tooling aplicado a flujos de trabajo de datos
- seguridad, gobernanza y control en sistemas basados en datos o IA

## Estructura del repositorio
Cada carpeta de primer nivel representa una charla distinta, salvo carpetas de infraestructura como `agents/`, `templates/`, `scripts/` y `skills/`.

Dentro de cada charla se pueden incluir materiales como:

- slides o archivos fuente de presentacion
- notas de investigacion
- claim spine o narrativa
- referencias y fuentes
- assets o recursos visuales

Convencion minima recomendada por charla:

- `notes/`: narrativa, fuentes, claims validados y bibliografia
- `slides/` o `deck/`: estructura, archivos editables y exportables
- `assets/`: imagenes, prompts y recursos visuales cuando existan
- `specs/`: specs SDD locales cuando se trabaje con la metodologia nueva
- `review/`: comentarios, observaciones y ajustes finales locales cuando existan

Esta convencion no es retroactiva. Las charlas anteriores pueden no tener `specs/` o `review/`; se migran solo si se reabren o si aporta valor concreto.

`slides/`, `assets/`, `specs/` y `review/` pueden existir localmente, pero por defecto no se suben al repo remoto.

Charlas actuales:

- `Harness Engineer/`
- `Evolucion Stack Clasico DS/`
- `El Eterno Retorno/`
- `Wiki LLM con Obsidian/`
- `SDD-IAgentica/`

## Convencion recomendada
Cuando se cree una nueva charla, agregar una carpeta dedicada con un nombre claro del tema.

Ejemplos:

- `Actualizacion Stack ML/`
- `Scikit Learn y el nuevo stack/`
- `LLMs para Data Science/`
- `Explicabilidad y SHAP/`

## Enfoque editorial
Estas charlas deben priorizar:

- utilidad practica sobre hype
- precision tecnica
- ejemplos aplicables a trabajo real de Data Science
- comparaciones claras entre enfoques clasicos y nuevos

## Linea editorial
Las charlas de este repo suelen combinar:

- una tesis tecnica clara
- comparaciones o tradeoffs concretos
- una recomendacion ejecutiva
- una slide final con mensaje de cierre e imagen editorial alineada con la tesis

## Flujo recomendado
Cuando una charla arranca solo desde un tema o una pregunta abierta, conviene separar tres momentos:

- primero investigar, tensionar y converger la tesis
- despues fijar la narrativa slide by slide
- despues construir la deck editable y visualmente fuerte

La carpeta `agents/` captura esa separacion con agentes distintos para research, narrativa, deck building, imagen editorial final y review.

## Orquestacion recomendada
El flujo recomendado es:

1. `orchestrator-charlas` para identificar fase, dependencia y siguiente agente
2. `researcher-charlas` para explorar el tema, tensionar la tesis y devolver insumos discutibles
3. research en paralelo solo cuando el framing ya esta claro y existan subpreguntas independientes
4. `narrative-charlas` para convertir el research convergido en una historia de `8-10 slides`
5. `deck-builder-charlas` para construir decks nuevos con el renderer local desde `deck-spec.json`; la skill `pptx` queda solo para emergencia o diagnostico avanzado
6. `image-closer-charlas` para resolver la imagen editorial final
7. `review-charlas` para revisar narrativa, visuales y cierre antes de cerrar la charla

`deck-builder-charlas` e `image-closer-charlas` pueden correr en paralelo si la narrativa ya esta fija y ya existen, o se fijan antes, el mensaje final y la cita real de referente o fallback justificado.

Si hay duda sobre en que fase esta una charla o que agente deberia correr primero, el entrypoint recomendado es `orchestrator-charlas`.

Este repo no esta orientado a generar imagenes sueltas. La imagen final existe para cerrar una charla ya estructurada.

## Inicio rapido del workflow v2

Para una charla nueva o reabierta, opera en cinco pasos:

1. Elige `templates/charlas-sdd/full/` para una charla normal o compleja, o `templates/charlas-sdd/compact/` cuando el framing ya sea claro.
2. Copia los specs elegidos a `<talk>/specs/` y completa solo los requisitos concretos de esa charla.
3. Copia `templates/charlas-sdd/execution-package.md` y registra `run_id`, intento, fase, rol, entradas permitidas, salidas, criterios de aceptacion y runtime real.
4. Lanza el rol aislado con `fork_context: false`, los insumos mínimos, su rol, spec y prompt especializados. El worker sobrescribe `notes/phase-summary.md` y publica el sentinel al final mediante `scripts/agent_workflow/complete-phase.py`.
5. Valida el handoff y, si pasa, aplica la transicion del contrato:

   ```powershell
   python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --summary "<talk>/notes/phase-summary.md" --sentinel "<talk>/notes/.phase-<phase>.done"
   ```

Consulta `agents/workflow-contract.json` para fases, transiciones y sentinels; `agents/runtime-defaults.json` contiene únicamente preferencias de runtime.

El padre conversa con el usuario, prepara paquetes acotados y decide la transición indicada por el contrato canónico. No lee chats, logs ni razonamiento del worker. Antes de leer `notes/phase-summary.md`, valida `run_id`, fase, intento y estado de ejecución; la mera existencia del sentinel no implica finalización.
