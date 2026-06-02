# Speech base

## Titulo sugerido

`El eterno retorno: de la nube a on-premise para workloads LLM`

## Idea fuerza

Hace diez anos, gran parte de la conversacion de infraestructura era como salir del datacenter propio y llevar todo a la nube.

Hoy la nube gano esa batalla para muchisimos casos:

- elasticidad
- menor friccion operativa
- mejor disponibilidad
- acceso mas rapido a nuevos servicios

Pero los LLMs reabren una pregunta incomoda:

si el costo recurrente de inferencia crece demasiado, ¿vale la pena traer parte de ese workload de vuelta a infraestructura controlada?

## Apertura sugerida

Durante anos, el movimiento era claro: salir del on-premise y abrazar la nube.

Tener tus propios servidores significaba comprar hardware, mantenerlo, renovar capacidad, tener equipos especializados y absorber riesgos operativos. La nube parecia resolverlo todo: mejor disponibilidad, mejor escalabilidad, menos friccion y costos mas previsibles.

Y para muchisimos sistemas, eso sigue siendo cierto.

Pero los LLMs estan introduciendo un tipo de gasto que no siempre se comporta como el resto del software cloud. No es solo storage. No es solo compute tradicional. Es consumo probabilistico, intensivo y muchas veces dificil de controlar, porque cada prompt, cada agente y cada iteracion quema tokens.

Entonces aparece una pregunta que hace pocos anos parecia vieja: si usar modelos de terceros se vuelve demasiado caro, ¿vamos a volver a correr parte de la inteligencia dentro de casa?

## Problema que la charla plantea

La tension no es ideologica.

No se trata de "cloud bueno" versus "on-prem malo", ni al reves.

Se trata de economia operativa:

- cuanto cuesta consumir inteligencia por API
- cuanto cuesta correrla uno mismo
- en que punto la nube deja de ser la opcion obvia
- y para que tipo de workload empieza a tener sentido una arquitectura hibrida

## Argumento central

La nube no va a desaparecer.

Pero el supuesto de que siempre sera la opcion economicamente mas racional para inferencia intensiva con LLMs ya no se puede dar por sentado.

Cuando una empresa:

- tiene uso recurrente
- opera con muchos usuarios
- corre agentes largos o automatizaciones
- necesita soberania o control del dato
- y puede tolerar modelos open source suficientemente buenos

entonces empieza a ser racional comparar el gasto por tokens con el costo total de una infraestructura propia o semipropia.

## Parte de validacion con mercado

La idea no nace solo de intuicion.

Ya hay señales de fatiga de costos:

- Axios reporto el 28 de mayo de 2026 que lideres corporativos estan cuestionando si el gasto creciente en IA realmente esta generando retorno.
- Ese mismo articulo menciona que un cliente de un consultor gasto medio billon de dolares en un solo mes por no haber puesto limites de uso en Claude.
- Fortune reporto el 26 de mayo de 2026 que el COO de Uber dijo que el gasto en IA se estaba volviendo mas dificil de justificar.
- Anthropic documenta que Claude Code en despliegues enterprise puede promediar aproximadamente 150 a 250 dolares por desarrollador al mes, con amplia varianza.
- Axios tambien reporto el 28 de mayo de 2026 que Microsoft habia cancelado la mayoria de sus licencias internas de Claude Code, en parte por costos, citando a The Verge.
- The Information reporto el 8 de abril de 2026 que Meta retiro un leaderboard interno de uso de tokens.
- Fortune reporto el 12 de mayo de 2026 que Amazon tambien enfrentaba patrones de uso gamificado o `tokenmaxxing`.

La señal no es "la IA no sirve".

La senal es "el costo sin disciplina se dispara".

## Punto de madurez de la charla

La conclusion madura no es que todas las empresas van a volver al datacenter.

La conclusion madura es que vamos hacia una nueva segmentacion:

### Casos que seguiran en la nube

- frontier models
- demanda altamente variable
- prototipado rapido
- equipos pequenos
- casos donde la calidad del modelo pesa mas que el costo

### Casos que podrian migrar a infraestructura controlada

- asistentes internos de alto volumen
- inferencia repetitiva y predecible
- pipelines donde un open source bueno es suficiente
- entornos con requisitos de soberania, seguridad o compliance

## Cierre sugerido

Tal vez el retorno no sea al pasado.

Tal vez sea a una pregunta que habiamos dejado de hacer:

no solo "que modelo es mejor", sino "donde conviene correr la inteligencia".

Y esa pregunta, que parecia resuelta por la nube, vuelve hoy por una razon muy concreta: el costo.
