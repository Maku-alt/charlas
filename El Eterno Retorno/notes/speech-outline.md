# Speech base

## Título sugerido

`El eterno retorno: de la nube a on-premise para workloads LLM`

## Idea fuerza

Hace diez años, gran parte de la conversación de infraestructura era cómo salir del datacenter propio y llevar todo a la nube.

Hoy la nube ganó esa batalla para muchísimos casos:

- elasticidad
- menor fricción operativa
- mejor disponibilidad
- acceso más rápido a nuevos servicios

Pero los LLMs reabren una pregunta incómoda:

si el costo recurrente de inferencia crece demasiado, ¿vale la pena traer parte de ese workload de vuelta a infraestructura controlada?

## Apertura sugerida

Durante años, el movimiento era claro: salir del on-premise y abrazar la nube.

Tener tus propios servidores significaba comprar hardware, mantenerlo, renovar capacidad, tener equipos especializados y absorber riesgos operativos. La nube parecía resolverlo todo: mejor disponibilidad, mejor escalabilidad, menos fricción y costos más previsibles.

Y para muchísimos sistemas, eso sigue siendo cierto.

Pero los LLMs están introduciendo un tipo de gasto que no siempre se comporta como el resto del software cloud. No es solo storage. No es solo compute tradicional. Es consumo probabilístico, intensivo y muchas veces difícil de controlar, porque cada prompt, cada agente y cada iteración quema tokens.

Entonces aparece una pregunta que hace pocos años parecía vieja: si usar modelos de terceros se vuelve demasiado caro, ¿vamos a volver a correr parte de la inteligencia dentro de casa?

## Problema que la charla plantea

La tensión no es ideológica.

No se trata de "cloud bueno" versus "on-prem malo", ni al revés.

Se trata de economía operativa:

- cuánto cuesta consumir inteligencia por API
- cuánto cuesta correrla uno mismo
- en qué punto la nube deja de ser la opción obvia
- y para qué tipo de workload empieza a tener sentido una arquitectura híbrida

## Argumento central

La nube no va a desaparecer.

Pero el supuesto de que siempre será la opción económicamente más racional para inferencia intensiva con LLMs ya no se puede dar por sentado.

Cuando una empresa:

- tiene uso recurrente
- opera con muchos usuarios
- corre agentes largos o automatizaciones
- necesita soberanía o control del dato
- y puede tolerar modelos open source suficientemente buenos

entonces empieza a ser racional comparar el gasto por tokens con el costo total de una infraestructura propia o semipropia.

## Parte de validación con mercado

La idea no nace solo de intuicion.

Ya hay señales de fatiga de costos:

- Axios reportó el 28 de mayo de 2026 que líderes corporativos están cuestionando si el gasto creciente en IA realmente está generando retorno.
- Ese mismo artículo menciona que un cliente de un consultor gastó medio billón de dólares en un solo mes por no haber puesto límites de uso en Claude.
- Fortune reportó el 26 de mayo de 2026 que el COO de Uber dijo que el gasto en IA se estaba volviendo más difícil de justificar.
- Anthropic documenta que Claude Code en despliegues enterprise puede promediar aproximadamente 150 a 250 dólares por desarrollador al mes, con amplia varianza.
- Axios también reportó el 28 de mayo de 2026 que Microsoft había cancelado la mayoría de sus licencias internas de Claude Code, en parte por costos, citando a The Verge.
- The Information reportó el 8 de abril de 2026 que Meta retiró un leaderboard interno de uso de tokens.
- Fortune reportó el 12 de mayo de 2026 que Amazon también enfrentaba patrones de uso gamificado o `tokenmaxxing`.

La señal no es "la IA no sirve".

La señal es "el costo sin disciplina se dispara".

## Punto de madurez de la charla

La conclusión madura no es que todas las empresas van a volver al datacenter.

La conclusión madura es que vamos hacia una nueva segmentación:

### Casos que seguirán en la nube

- frontier models
- demanda altamente variable
- prototipado rápido
- equipos pequeños
- casos donde la calidad del modelo pesa más que el costo

### Casos que podrían migrar a infraestructura controlada

- asistentes internos de alto volumen
- inferencia repetitiva y predecible
- pipelines donde un modelo de pesos abiertos suficientemente bueno es suficiente
- entornos con requisitos de soberanía, seguridad o compliance

## Nueva frontera: capacidad local personal

El 31 de mayo de 2026, NVIDIA anunció sistemas RTX Spark para otoño de 2026 con hasta 128 GB de memoria unificada, hasta 1 petaflop FP4 de AI compute y capacidad anunciada para ejecutar localmente LLMs de hasta 120B parámetros.

La importancia para esta charla no es el producto en sí ni una promesa de ahorro todavía no demostrada. La señal es que la segmentación de workloads puede llegar al computador personal:

- el modelo local absorbe tareas frecuentes, privadas y repetitivas
- un orquestador evalúa costo, riesgo y calidad requerida
- la nube queda reservada para planificación compleja, modelos frontier, casos ambiguos y picos de demanda

El mensaje oral recomendado es:

> El modelo local no necesita ser siempre mejor. Necesita ser suficientemente bueno para absorber el volumen y reservar la nube para donde su calidad adicional realmente importa.

Evitar decir que el uso local ofrece tokens ilimitados o que garantiza menor TCO. Desaparece la cuota contractual por iteración, pero siguen existiendo límites de capacidad, energía, concurrencia y costo de hardware.

## Cierre sugerido

Tal vez el retorno no sea al pasado.

Tal vez sea a una pregunta que habíamos dejado de hacer:

no solo "qué modelo es mejor", sino "dónde conviene correr la inteligencia".

Y esa pregunta, que parecía resuelta por la nube, vuelve hoy por una razón muy concreta: el costo.
