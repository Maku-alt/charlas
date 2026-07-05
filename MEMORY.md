# Memory

## Que es este repo

Este repo agrupa charlas orientadas a Data Science, datos, IA aplicada, stack tecnico, decisiones de arquitectura y practicas de trabajo.

La audiencia por defecto es `Data Scientists` en general. No se amarra la narrativa a telco salvo pedido explicito.

## Linea editorial consolidada

- tono ejecutivo tecnico
- copy directo y claro
- slides con tesis, no con titulos genericos
- comparaciones y tradeoffs con lectura ejecutiva
- cierre editorial fuerte con cita breve, mensaje final e imagen deliberada

## Sistema documental del repo

Los documentos raiz que gobiernan el trabajo son:

- `README.md`: explicacion humana del repo
- `maestro_charlas.md`: indice vivo de charlas trabajadas, estado, tesis y entregables principales
- `AGENTS.md`: reglas persistentes de trabajo dentro de charlas
- `STYLE-CHARLAS.md`: sistema visual y narrativo compartido
- `agents/`: agentes especializados del flujo de charlas
- `templates/charlas-sdd/`: metodologia SDD reutilizable para research, narrativa, build y review
- `scripts/deck_renderer/`: renderer local para construir PPTX editables desde `deck-spec.json`

## Convencion por charla

La practica vigente del repo es:

- `specs/`: specs SDD propios de la charla, copiados o adaptados desde `templates/charlas-sdd/`
- `notes/`: narrativa, claims, fuentes, material validado y bibliografia
- `slides/` o `deck/`: fuente editable y exportables
- `assets/`: recursos visuales e imagen final cuando existan
- `review/`: observaciones y ajustes finales cuando existan

La bibliografia vive dentro de `notes/`.

Esta convencion aplica hacia adelante. Las charlas creadas antes de la adopcion de `specs/` y `templates/charlas-sdd/` no tienen que migrarse retroactivamente salvo que se reabran.

`slides/` y `assets/` pueden existir localmente para construir la charla, pero por defecto quedan fuera del repo remoto.

## Charlas existentes

### `Harness Engineer`

Charla sobre harness engineering para equipos de Data Science. La tesis consolidada es que el valor del agente no vive solo en el modelo, sino en el entorno operativo que organiza contexto, memoria, tools, checks y criterio.

### `Evolucion Stack Clasico DS`

Charla sobre la evolucion del stack clasico de Data Science en Python, con foco en adopcion practica, compatibilidad real y costo de migracion.

### `El Eterno Retorno`

Charla sobre la tension nube versus on-premise para workloads LLM y la idea de que no estamos viendo un simple regreso al pasado sino una nueva disciplina de arquitectura hibrida.

### `Wiki LLM con Obsidian`

Charla sobre wikis LLM con Obsidian como memoria operativa compilada para research, repos y decisiones tecnicas.

### `SDD-IAgentica`

Charla revisada bajo la metodologia nueva. El entregable versionable final es `SDD-IAgentica/SDD-IAgentica-v2.pptx`; las fuentes editables quedan en `slides/` y los assets en `assets/`.

### `IA Agentica de Conversacion a Sistema`

Charla revisada sobre el paso de IA web como conversacion aislada a IA agentica como sistema de trabajo con reglas, contexto, estado, permisos, outputs verificables y revision humana. El entregable versionable final es `IA Agentica de Conversacion a Sistema/IA-Agentica-De-Conversacion-A-Sistema.pptx`; la version aprobada tiene 10 slides y la review vigente es `review/review-formal-feedback-pass.md`.

## Sistema de agentes construido

El flujo especializado de este repo ya existe y fue disenado asi:

- `orchestrator-charlas`
- `researcher-charlas`
- `narrative-charlas`
- `deck-builder-charlas`
- `image-closer-charlas`
- `review-charlas`

Principio operativo:

1. primero converger tesis y narrativa
2. fijar una narrativa de `8-10 slides`
3. despues construir la deck con el renderer local
4. luego resolver el cierre visual
5. finalmente revisar el artefacto

El research paralelo solo conviene cuando el framing ya esta claro y hay subpreguntas independientes.

Por defecto, las fases pesadas deben recibir contexto acotado: rol, spec, artefactos necesarios, prompt de fase, `notes/phase-summary.md` como handoff y `fork_context: false` cuando se use subagente. En workers separados, el padre espera el sentinel por archivos y no lee chats worker.

## Aprendizajes ya validados

- no todo hallazgo del research pasa automaticamente a la PPT
- el cierre visual debe existir como agente separado del deck builder
- el review debe ocurrir sobre una deck o artefacto ya construido, no sobre ideas abiertas
- el build normal de PPTX usa `scripts/deck_renderer/render-deck.js` desde `deck-spec.json`
- PowerPoint nativo es el gate final de apertura/export
- el padre debe esperar 180 segundos antes del primer `Test-Path` sobre un sentinel worker
- `researcher.md` se conserva como pieza portable, pero no forma parte de la documentacion publica del flujo de `charlas`

## Test ya ejecutado

Se ejecuto un test end-to-end con una version temporal de `Harness Engineer 2`. El contenido del test fue eliminado despues de validarlo, pero dejo dos conclusiones utiles:

- el flujo `research -> deck -> image -> review` funciono de punta a punta en un caso previo del repo
- el build normal debe ser reproducible por script; si una herramienta auxiliar falla, no debe convertirse en default del flujo

Ese aprendizaje operativo ya fue absorbido en la documentacion de `agents/`. El flujo vigente agrega la fase explicita `narrative-charlas` entre research y build; lo que esta en curso es la validacion de ese cambio.

## Higiene del repo

- `researcher.md` debe quedar fuera de versionado
- `outputs/`, `analysis/`, `.codex/`, `.agents/`, `.ai/`, `preview/`, `layout/`, `qa/`, `node_modules/` y entornos virtuales deben tratarse como temporales

## Como usar esta memoria

Este archivo no reemplaza `AGENTS.md`. Sirve para recordar decisiones ya tomadas, el estado del sistema y la historia corta del repo para futuras sesiones.
