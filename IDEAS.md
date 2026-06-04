# Ideas de Charlas

## Objetivo

Backlog vivo de temas, hipotesis y lineas de investigacion que podrian convertirse en futuras charlas del repo.

## Ideas activas

### Wiki LLM con Obsidian

Pregunta:
`Puede un stack personal o de equipo basado en Obsidian convertirse en una wiki LLM realmente util para trabajo de conocimiento?`

Angulos posibles:

- Obsidian como memoria externa para agentes o equipos
- limites entre notas humanas, retrieval y contexto operativo
- cuando una wiki mejora el trabajo y cuando solo agrega friccion
- diferencias entre knowledge base pasiva y harness activo

Valor potencial:

- conecta trabajo de conocimiento, memoria operativa y tooling cotidiano
- puede interesar tanto a Data Science como a equipos tecnicos mas amplios

### Harness versus LLM suelto

Pregunta:
`Por que un harness bien disenado puede rendir mejor que un LLM usado de forma aislada?`

Angulos posibles:

- leverage del entorno versus leverage del modelo
- evidencia de rendimiento, confiabilidad y reproducibilidad
- contexto, tools, memoria, checks y evaluacion como sistema
- cuando un modelo mejor ayuda y cuando el cuello de botella esta en el harness

Valor potencial:

- profundiza una tesis ya visible en `Harness Engineer`
- puede convertirse en charla propia o en extensiones mas tecnicas

### Prompt Injection, skills y MCP

Pregunta:
`Como cambia la seguridad cuando un agente ya no solo responde texto, sino que usa skills, tools, memoria y servidores MCP?`

Tesis provisional:
`Prompt injection no es solo un bug del prompt. Es un problema de arquitectura del harness y de control sobre lo que el agente puede ver, recordar y ejecutar.`

Angulos posibles:

- por que el prompt deja de ser una frontera suficiente
- superficies de ataque nuevas: contexto, repo, memoria externa, tools, browser, skills y MCP
- diferencia entre un LLM pasivo y un agente con capacidad de actuar
- principios de contencion: least privilege, aislamiento, scopes, handoffs, aprobaciones y review
- que controles son de producto, cuales son de plataforma y cuales son de operacion del equipo

Valor potencial:

- conecta seguridad con el sistema de agentes que ya estamos construyendo
- conversa directamente con `Harness Engineer`
- abre una charla muy actual para Data Science, plataforma e IA aplicada

### Coste real de operar contexto

Pregunta:
`Que cuesta de verdad mantener contexto util en un sistema de agentes?`

Angulos posibles:

- costo de documentacion, hygiene y drift
- memoria externa, handoffs y verificacion
- tradeoff entre mas contexto y mas complejidad

### El reviewer como palanca

Pregunta:
`El mayor cambio no es generar mas rapido, sino revisar mejor?`

Angulos posibles:

- reviewer humano versus reviewer-agente
- evidencia frente a confianza implicita
- como cambia la calidad cuando el loop de review se vuelve estructural

### Protocolos minimos para equipos de Data Science con agentes

Pregunta:
`Cual es el protocolo minimo para que un equipo de datos trabaje bien con agentes sin caer en complejidad excesiva?`

Angulos posibles:

- repo, notes, AGENTS, checks y reviewer
- subagentes con scope pequeno
- que no hace falta construir al inicio

## Criterios para priorizar

Una idea sube de prioridad cuando:

- tiene tension clara
- puede formularse como tesis, no solo como tema
- promete comparacion o tradeoff visible
- tiene evidencia reciente o investigable
- conecta con trabajo real de equipos de Data Science

## Estado esperado de cada idea

Antes de volverse charla, una idea deberia madurar al menos hasta:

- pregunta central
- hipotesis o tesis provisional
- audiencia
- angulo diferencial
- lista de fuentes o frentes de research
