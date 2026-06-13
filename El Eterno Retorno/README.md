# El Eterno Retorno

## Título tentativo

`De la nube a on-premise para workloads LLM`

## Hipótesis

El costo creciente de usar modelos LLM por token a través de proveedores externos puede empujar a algunas empresas a reconsiderar infraestructura propia para ciertos workloads intensivos, especialmente cuando hay volumen alto, necesidad de control, restricciones de datos o presión fuerte sobre presupuesto.

La versión madura de esta hipótesis no es "todo vuelve a on-premise". La versión madura es:

- la nube seguirá siendo dominante para elasticidad, velocidad y acceso a frontier models
- pero ciertos workloads podrían migrar a infraestructura más controlada, privada o híbrida cuando el costo recurrente por inferencia deja de cerrar

## Pregunta central

Si el gasto en LLMs de terceros sigue subiendo, ¿volverá el paradigma de operar parte de la inferencia en infraestructura on-premise con modelos open source?

## Lo que la charla debe investigar

- cuánto cuesta hoy consumir LLMs por API en distintos escenarios
- qué workloads tienen patrón de uso suficiente para justificar hardware propio
- qué costo real tiene operar inferencia on-premise
- dónde la nube sigue ganando por flexibilidad, velocidad y simplicidad
- si esto es un retorno de paradigma o una especialización para casos concretos

## Tensión principal

La nube resuelve velocidad de adopción, elasticidad y acceso a modelos frontier.

On-premise promete:

- menor costo marginal en alto volumen
- más control de datos
- mayor previsibilidad de costos
- capacidad de usar modelos open source ajustados al dominio

Pero trae:

- costo de hardware
- mantenimiento operativo
- capacidad limitada
- complejidad de serving, observabilidad y actualización

## Tesis provisional recomendada

No estamos viendo un simple regreso al pasado. Estamos viendo el nacimiento de una nueva disciplina de arquitectura para IA:

- nube para experimentación, frontier models y demanda elástica
- infraestructura propia o privada para workloads repetitivos, sensibles o económicamente intensivos

## Audiencia

Líderes técnicos, equipos de Data Science, ML Platform, IA aplicada y arquitectura.

## Estado

Revisada.
