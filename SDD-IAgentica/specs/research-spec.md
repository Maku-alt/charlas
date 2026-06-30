# Research Spec

## Pregunta investigada
Que evidencia y marcos conceptuales respaldan la idea de que SDD ayuda a trabajar mejor con IA agentica al reducir contexto innecesario, separar fases y producir handoffs verificables?

## Modo
orientado a decision

## Nivel de esfuerzo
standard

## Hipotesis inicial
En flujos agenticos, el problema no es solo la inteligencia del modelo, sino el diseno del contexto. SDD funciona porque transforma una conversacion abierta en paquetes pequenos de trabajo: especificacion, prompt de fase, artefactos de entrada, salida esperada y review.

## Claims a verificar
- Las ventanas de contexto largas no eliminan el problema de gestion de contexto; tambien pueden introducir ruido y costo.
- Dividir tareas por fases con handoffs explicitos mejora auditabilidad y reduce arrastre conversacional.
- Los agentes funcionan mejor cuando tienen roles, objetivos, restricciones y criterios de salida claros.
- El ahorro de tokens debe presentarse como razonamiento operativo, no como cifra exacta sin medicion.

## Perspectivas a cubrir
- practitioner: como trabaja una persona que usa Codex para producir artefactos reales
- engineer: como se disena el flujo, el prompt y el contrato de handoff
- skeptic: cuando subagentes agregan overhead o fragmentan la decision
- operator: como se revisa calidad, evidencia y cierre
- economist: como pensar costo de tokens y tiempo sin inventar cifras

## Preguntas fuertes
- Que tendria que ser cierto para sostener que SDD reduce consumo util de contexto?
- Que evidencia debilitaria la tesis? Por ejemplo, specs pobres, handoffs incompletos o subagentes duplicando trabajo.
- Que actor tendria incentivos para exagerar? Vendors de agentes, tooling de AI dev, consultores de metodologia.
- Que parte depende de informacion actual? Precios, limites de contexto, features concretas de plataformas y casos corporativos recientes.

## Evidencia minima para avanzar
- Fuentes primarias u oficiales sobre prompt engineering, context management o agentes.
- Articulos tecnicos recientes o docs de alta autoridad sobre context engineering, task decomposition y agent workflows.
- Evidencia conceptual suficiente para defender el tradeoff sin prometer metricas exactas.
- Contradicciones: overhead de specs, perdida de continuidad, dificultad de integrar outputs.

## Salida esperada
- tesis refinada
- hallazgos que si merecen slide
- contradicciones
- claims pendientes
- direccion de cierre
