# Charlas de Data Science

Este repositorio agrupa materiales para distintas charlas relacionadas con Data Science, analitica aplicada y el uso practico de datos.

## Documentos raiz

- `README.md`: explicacion humana del repositorio
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

Cada carpeta de primer nivel representa una charla distinta.

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
- `review/`: comentarios, observaciones y ajustes finales cuando existan

Ejemplo actual:

- `Harness Engineer/`: materiales de una charla sobre harness engineering aplicado a workflows tecnicos

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

Cuando una charla arranca solo desde un tema o una pregunta abierta, conviene separar dos momentos:

- primero investigar, tensionar y converger la tesis y la narrativa
- despues construir la deck editable y visualmente fuerte

La carpeta `agents/` captura esa separacion con agentes distintos para research, deck building, imagen editorial final y review.

## Orquestacion recomendada

El flujo recomendado es:

1. `orchestrator-charlas` para identificar fase, dependencia y siguiente agente
2. `researcher-charlas` para explorar el tema y converger tesis y narrativa
3. research en paralelo solo cuando el framing ya esta claro y existan subpreguntas independientes
4. `deck-builder-charlas` para construir la deck
5. `image-closer-charlas` para resolver la imagen editorial final
6. `review-charlas` para revisar narrativa, visuales y cierre antes de cerrar la charla

`deck-builder-charlas` e `image-closer-charlas` pueden correr en paralelo si la direccion ya esta suficientemente definida y ya existe, o se fija antes, la cita y el mensaje final.

Si hay duda sobre en que fase esta una charla o que agente deberia correr primero, el entrypoint recomendado es `orchestrator-charlas`.

Este repo no esta orientado a generar imagenes sueltas. La imagen final existe para cerrar una charla ya estructurada.
