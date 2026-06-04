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
- `AGENTS.md`: reglas persistentes de trabajo dentro de charlas
- `STYLE-CHARLAS.md`: sistema visual y narrativo compartido
- `agents/`: agentes especializados del flujo de charlas

## Convencion por charla

La practica vigente del repo es:

- `notes/`: narrativa, claims, fuentes, material validado y bibliografia
- `slides/` o `deck/`: fuente editable y exportables
- `assets/`: recursos visuales e imagen final cuando existan
- `review/`: observaciones y ajustes finales cuando existan

La bibliografia vive dentro de `notes/`.

## Charlas existentes

### `Harness Engineer`

Charla sobre harness engineering para equipos de Data Science. La tesis consolidada es que el valor del agente no vive solo en el modelo, sino en el entorno operativo que organiza contexto, memoria, tools, checks y criterio.

### `Evolucion Stack Clasico DS`

Charla sobre la evolucion del stack clasico de Data Science en Python, con foco en adopcion practica, compatibilidad real y costo de migracion.

### `El Eterno Retorno`

Charla sobre la tension nube versus on-premise para workloads LLM y la idea de que no estamos viendo un simple regreso al pasado sino una nueva disciplina de arquitectura hibrida.

## Sistema de agentes construido

El flujo especializado de este repo ya existe y fue diseñado asi:

- `orchestrator-charlas`
- `researcher-charlas`
- `deck-builder-charlas`
- `image-closer-charlas`
- `review-charlas`

Principio operativo:

1. primero converger tesis y narrativa
2. despues construir la deck
3. luego resolver el cierre visual
4. finalmente revisar el artefacto

El research paralelo solo conviene cuando el framing ya esta claro y hay subpreguntas independientes.

## Aprendizajes ya validados

- no todo hallazgo del research pasa automaticamente a la PPT
- el cierre visual debe existir como agente separado del deck builder
- el review debe ocurrir sobre una deck o artefacto ya construido, no sobre ideas abiertas
- `researcher.md` se conserva como pieza portable, pero no forma parte de la documentacion publica del flujo de `charlas`

## Test ya ejecutado

Se ejecuto un test end-to-end con una version temporal de `Harness Engineer 2`. El contenido del test fue eliminado despues de validarlo, pero dejo dos conclusiones utiles:

- el flujo `research -> deck -> image -> review` funciona de punta a punta en un caso real del repo
- en Windows, si el builder de presentaciones resuelve mal `@oai/artifact-tool`, conviene relanzar con `HOME=C:\\Users\\Victor`

Ese aprendizaje operativo ya fue absorbido en la documentacion de `agents/`.

## Higiene del repo

- `researcher.md` debe quedar fuera de versionado
- `outputs/`, `preview/`, `layout/`, `qa/`, `node_modules/` y entornos virtuales deben tratarse como temporales

## Como usar esta memoria

Este archivo no reemplaza `AGENTS.md`. Sirve para recordar decisiones ya tomadas, el estado del sistema y la historia corta del repo para futuras sesiones.
