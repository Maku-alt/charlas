# Research Brief: SDD e IA agentica con contexto acotado

Research value: high

## Idea o pregunta investigada

Que evidencia y marcos conceptuales respaldan la idea de que SDD ayuda a trabajar mejor con IA agentica al reducir contexto innecesario, separar fases y producir handoffs verificables?

La pregunta no busca probar un ahorro cuantitativo universal de tokens. Busca validar si la tesis operativa es defendible: en flujos largos con agentes, el cuello de botella no es solo el modelo, sino el diseno del contexto, las fases, los artefactos y los criterios de salida. Si se incluyen numeros, deben venir de una medicion propia o una estimacion reproducible.

## Modo de trabajo

modo orientado a decision

## Nivel de esfuerzo

standard

## Tesis propuesta

SDD vuelve mas practica la IA agentica porque convierte una conversacion larga en una cadena de contratos pequenos: cada fase recibe objetivo, contexto minimo, artefactos de entrada, restricciones y salida verificable. La mejora no viene de "usar subagentes" por si mismo, sino de aislar el contexto relevante y hacer auditable cada handoff.

Version mas fuerte para la charla:

> En IA agentica, el contexto no es memoria: es superficie de trabajo. SDD funciona porque decide que entra, que queda fuera y como se verifica el resultado antes de pasar a la siguiente fase.

## Resumen ejecutivo

La evidencia externa sostiene la tesis en cuatro puntos:

1. Las ventanas de contexto largas no eliminan el problema de gestion de contexto. Papers como "Lost in the Middle" muestran que los modelos pueden degradar su uso de informacion cuando el contexto crece o cuando la informacion relevante queda en posiciones menos favorables.
2. La industria ya trata el context engineering como una disciplina: seleccionar, comprimir, aislar y persistir contexto segun la tarea, no simplemente meter mas historial.
3. Los frameworks de agentes formalizan conceptos compatibles con SDD: instrucciones, herramientas, handoffs, guardrails, tracing y outputs estructurados.
4. Los sistemas multiagente efectivos parecen depender menos de "muchos agentes" y mas de arquitectura: roles claros, separacion de responsabilidades, artefactos intermedios, evaluacion y trazabilidad.

La tesis debe matizarse: SDD agrega overhead y puede fallar si los specs son pobres, si el handoff corta informacion critica o si nadie integra los resultados. Por eso el angulo correcto no es "subagentes siempre mejores", sino "subagentes funcionan cuando el contrato de entrada y el gate de salida estan bien disenados".

Decision de continuidad: seguir

## Panorama actual

El consenso practico emergente es que agentes utiles necesitan mas que una buena instruccion inicial. Necesitan un harness: un sistema que decide que informacion ve el modelo, que herramientas puede usar, como se delega, como se valida y como se observa la ejecucion.

Anthropic separa workflows y agentes, y recomienda empezar por patrones simples antes de aumentar autonomia. Su material reciente sobre context engineering define el problema como curar y mantener el conjunto optimo de tokens durante la inferencia. OpenAI Agents SDK modela agentes como LLMs configurados con instrucciones, herramientas, handoffs, guardrails y salidas estructuradas. LangChain describe context engineering como dar al agente la informacion y herramientas correctas en el formato correcto, y organiza estrategias como write, select, compress e isolate.

Para Data Scientists, la lectura es directa: un flujo agentico se parece mas a un pipeline reproducible que a una conversacion libre. Si el pipeline no explicita entradas, transformaciones, salida esperada y checks, el sistema puede producir resultados impresionantes pero dificiles de auditar.

## Hallazgos que si merecen slide

1. "Mas contexto" no equivale a "mejor contexto".
   - Evidencia: estudios de long context muestran degradacion por posicion, longitud o distractores.
   - Lectura: las ventanas grandes son capacidad, no gobernanza.

2. Context engineering es el nuevo nombre operativo para una practica vieja de datos: seleccionar features relevantes.
   - Evidencia: Anthropic y LangChain tratan el contexto como un recurso que se cura, comprime, aisla y persiste.
   - Lectura: SDD puede presentarse como feature engineering para agentes.

3. Los handoffs hacen visible el trabajo invisible.
   - Evidencia: frameworks como OpenAI Agents SDK formalizan handoffs, guardrails, tracing y outputs estructurados.
   - Lectura: un handoff bien escrito convierte una conversacion en un artefacto revisable.

4. La division por fases reduce mezcla de objetivos.
   - Evidencia: guias de prompt engineering recomiendan dividir tareas complejas en subtareas; sistemas multiagente exitosos usan roles especializados y coordinacion.
   - Lectura: research, narrativa, build y review no deberian compartir todo el mismo ruido conversacional.

5. La autonomia no reemplaza el gate humano.
   - Evidencia: Anthropic insiste en evaluaciones, harnesses y observabilidad; Microsoft recuerda que respuestas de LLMs deben validarse incluso con buen prompting.
   - Lectura: SDD no es waterfall, es iteracion con checkpoints.

## Mapa de contradicciones

| Tension | Evidencia a favor de SDD | Riesgo o contraargumento | Lectura para la charla |
|---|---|---|---|
| Contexto minimo vs continuidad | Aislar contexto reduce ruido y arrastre conversacional | Puede perder decisiones tacitas o supuestos importantes | El handoff debe preservar decisiones, no todo el historial |
| Subagentes vs overhead | Roles especializados permiten paralelismo y foco | Crear specs pobres puede duplicar trabajo o fragmentar la decision | Subagentes no son magia; el contrato manda |
| Artefactos verificables vs velocidad | Outputs escritos permiten review, tracing y continuidad | En tareas pequenas puede ser burocracia | Usar SDD completo solo cuando el costo del error o la longitud lo justifican |
| Ventanas largas vs gestion activa | Long context ayuda a incluir mas informacion | Papers muestran que mas tokens pueden traer degradacion o distraccion | Ventana grande no elimina curadoria |
| Estandarizacion vs creatividad | Fases y formatos reducen ambiguedad | Puede rigidizar una charla si se aplica como checklist | SDD debe organizar decisiones, no escribir la charla en piloto automatico |

## Opciones o enfoques encontrados

| Opcion | Madurez | Ventajas | Limitaciones | Lectura para la charla |
|---|---|---|---|---|
| Conversacion monolitica | Alta adopcion informal | Flexible, rapida, baja friccion inicial | Arrastra ruido, mezcla fases, dificulta auditoria | Buen punto de partida, mal sistema para trabajos largos |
| Prompt unico con mucho contexto | Comun | Aprovecha ventanas largas y reduce handoffs | Puede introducir informacion irrelevante, conflicto y costo | Capacidad sin disciplina no es workflow |
| SDD por fases con handoffs | Madurez emergente como practica | Foco, trazabilidad, artefactos, gates | Requiere escribir specs utiles y revisar integracion | Tesis principal recomendada |
| Multiagente autonomo | En crecimiento | Paralelismo, especializacion, exploracion amplia | Riesgo de overhead, supervision y coordinacion | Usarlo como consecuencia, no como punto de partida |
| Filesystem/artefactos como memoria externa | Muy relevante en agentes de codigo/research | Persistencia verificable, busqueda, continuidad entre sesiones | Puede volverse desordenado sin convenciones | Puente fuerte entre SDD y practica real |

## Direccion narrativa sugerida

Esta es una direccion de research, no una narrativa final cerrada.

1. Kicker: Problema
   - Titulo con tesis: La conversacion larga se vuelve un lugar caro para tomar decisiones
   - Objeto de prueba visible: diagrama de chat monolitico con historial, dudas, descartes y decisiones mezcladas
   - Takeaway: el problema no es hablar con IA, es no separar superficie de trabajo y memoria de decision

2. Kicker: Baseline
   - Titulo con tesis: Una ventana grande no decide que informacion importa
   - Objeto de prueba visible: comparacion "capacidad de contexto" vs "calidad de contexto"
   - Takeaway: long context es una posibilidad tecnica, no una estrategia operativa

3. Kicker: Evidencia
   - Titulo con tesis: Los modelos no usan todo el contexto con la misma robustez
   - Objeto de prueba visible: lectura simplificada de "Lost in the Middle" y distractores
   - Takeaway: meter mas tokens puede aumentar ruido, no solo informacion

4. Kicker: Cambio de lente
   - Titulo con tesis: Context engineering trata el contexto como un recurso disenado
   - Objeto de prueba visible: matriz select / compress / isolate / persist
   - Takeaway: el trabajo pasa de escribir prompts a disenar entradas de fase

5. Kicker: Metodo
   - Titulo con tesis: SDD convierte la conversacion en contratos pequenos
   - Objeto de prueba visible: spec -> prompt de fase -> artefactos -> output -> review
   - Takeaway: cada subagente trabaja con lo necesario, no con toda la historia

6. Kicker: Workflow
   - Titulo con tesis: Separar fases reduce mezcla de objetivos
   - Objeto de prueba visible: research, narrativa, build y review como estaciones con handoffs
   - Takeaway: el agente no debe investigar, escribir, construir y juzgar con el mismo contexto sucio

7. Kicker: Control
   - Titulo con tesis: Handoffs y tracing hacen auditable lo que antes era intuicion
   - Objeto de prueba visible: ejemplo conceptual de handoff verificable con input, salida y criterio de aceptacion
   - Takeaway: la calidad mejora cuando se puede revisar donde fallo el flujo

8. Kicker: Tradeoff
   - Titulo con tesis: SDD falla cuando el contrato es peor que la conversacion
   - Objeto de prueba visible: tabla corta de overhead, perdida de continuidad, duplicacion, specs pobres
   - Takeaway: la metodologia debe ser proporcional al riesgo y la complejidad

9. Kicker: Decision
   - Titulo con tesis: Para trabajos largos, el chat principal debe guardar decisiones, no todo el proceso
   - Objeto de prueba visible: comparacion antes/despues del rol del chat principal
   - Takeaway: el humano opera como editor de continuidad y gates

10. Kicker: Cierre
   - Titulo con tesis: La unidad de trabajo ya no es el prompt: es el handoff verificable
   - Objeto de prueba visible: imagen editorial de una linea de montaje sobria o sala de control con paquetes pequenos de trabajo
   - Takeaway: agentic AI exige diseno de flujo, no solo conversacion mas larga

## Claims a validar antes de cerrar la deck

- Cualquier claim sobre ahorro de tokens debe quedar cualitativo salvo que se mida en este repo o en un experimento propio.
- Cualquier limite de ventana de contexto, feature de Codex, OpenAI, Claude, LangChain u otra plataforma debe validarse con documentacion vigente en la fecha de build.
- Si se menciona "context engineering" como termino de mercado, conviene citarlo como practica emergente, no como estandar formal universal.
- Si se usa un caso corporativo o benchmark reciente, debe validarse con fuente primaria o reporte tecnico.
- Si se afirma que subagentes mejoran calidad, formularlo condicionalmente: mejoran cuando hay roles claros, contexto acotado, criterios de salida y review.

## Riesgos y consideraciones

- Riesgo de sonar burocratico: evitar vender SDD como mas documentos; mostrarlo como menos contexto innecesario y mas verificabilidad.
- Riesgo de sonar anti-long-context: la tesis no debe negar el valor de ventanas largas; debe decir que capacidad no reemplaza seleccion.
- Riesgo de confundir SDD con waterfall: enfatizar iteracion, gates y decision de continuidad.
- Riesgo de extrapolar papers: "Lost in the Middle" y estudios de distractores no prueban directamente SDD, pero si respaldan la premisa de que el contexto debe gestionarse.
- Riesgo de sesgo vendor: muchas fuentes sobre agentes vienen de proveedores de tooling; compensar con papers academicos y con claims moderados.

## Recomendacion

Usaria como tesis principal:

> SDD no hace mas inteligente al agente; hace mas legible el trabajo. Al reducir cada fase a un contrato de contexto, salida y review, convierte IA agentica en un workflow gobernable.

Comparacion central:

- Conversacion monolitica: rica, flexible, pero con arrastre de ruido y decisiones mezcladas.
- SDD agentico: mas estructurado, con handoffs verificables, pero exige buenos specs y gates.

Dejaria fuera:

- Benchmarks numericos universales de ahorro de tokens.
- Comparativa comercial entre plataformas.
- Promesas de autonomia total.
- Discusion profunda de arquitectura interna de modelos.

Decision de continuidad: seguir

## Cierre editorial propuesto

Mensaje final de una linea:

> El futuro no es hablar mas con la IA; es darle mejores unidades de trabajo.

Frase breve posible:

> "Contexto no es memoria. Contexto es diseno."

Metafora visual sugerida:

Una sala de control o mesa editorial con paquetes pequenos de trabajo etiquetados, no una imagen de robot ni un diagrama tecnico. La emocion debe ser control sobrio: precision, foco, continuidad.

## Donde profundizar despues

- Medir en un caso propio del repo: tokens aproximados, tiempo de build, cantidad de rework y errores detectados comparando chat monolitico vs fases SDD.
- Preparar un ejemplo visual de handoff bueno vs handoff malo.
- Buscar un caso tecnico adicional sobre agentes de codigo con filesystem o artefactos persistentes.
- Validar features actuales de Codex/OpenAI solo si la narrativa final nombra una plataforma concreta.
- Decidir si SDD se presenta como analogia a data pipelines, feature engineering o software delivery. Para Data Scientists, la analogia de pipeline + feature selection parece la mas fuerte.

## Self-review

Confidence score: 0.78

Weakest link: la evidencia disponible respalda principios de context management, task decomposition y agent workflows, pero no prueba directamente que "SDD" como metodologia reduzca tokens o mejore calidad en todos los casos.

Bias check: varias fuentes son de vendors o frameworks de agentes. Eso introduce sesgo a favor de tooling y arquitectura agentica. Se mitigo usando papers academicos sobre long context y distractores, y formulando claims como inferencias operativas.

Missing perspective: seria util sumar una perspectiva empirica interna con un experimento pequeno en el repo: mismo artefacto producido con chat monolitico vs specs/handoffs.

What would change my mind: evidencia de que modelos long-context recientes mantienen calidad estable con historiales largos, distractores y objetivos mezclados; o evidencia practica de que el overhead de SDD supera consistentemente sus beneficios en trabajos de charla.

## Fuentes consultadas

| Fuente | Clase | Tipo | Fecha | Relevancia | Enlace |
|---|---|---|---|---|---|
| Anthropic, "Building effective agents" | primaria | blog tecnico de proveedor/model lab | 2024-12-19 | Define workflows vs agents y recomienda patrones simples antes de autonomia mayor | https://www.anthropic.com/engineering/building-effective-agents |
| Anthropic, "Effective context engineering for AI agents" | primaria | blog tecnico de proveedor/model lab | 2025-09-29 | Define context engineering como curadoria del conjunto optimo de tokens durante inferencia | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Anthropic, "How we built our multi-agent research system" | primaria | blog tecnico de proveedor/model lab | 2025-06-13 | Caso practico de sistema multiagente con planificacion, subagentes y arquitectura | https://www.anthropic.com/engineering/multi-agent-research-system |
| Anthropic, "Effective harnesses for long-running agents" | primaria | blog tecnico de proveedor/model lab | 2025-11-26 | Refuerza la idea de harness, sesiones incrementales y artefactos claros para continuidad | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |
| OpenAI Agents SDK, "Agents" | primaria | documentacion oficial | consultado 2026-06-26 | Modela agentes con instrucciones, herramientas, handoffs, guardrails y outputs estructurados | https://openai.github.io/openai-agents-python/agents/ |
| OpenAI Agents SDK, "Handoffs" | primaria | documentacion oficial | consultado 2026-06-26 | Formaliza delegacion entre agentes especializados | https://openai.github.io/openai-agents-python/handoffs/ |
| OpenAI Agents SDK, "Tracing" | primaria | documentacion oficial | consultado 2026-06-26 | Sustenta auditabilidad: trazas de generaciones, tool calls, handoffs y guardrails | https://openai.github.io/openai-agents-python/tracing/ |
| OpenAI Agents SDK, "Context management" | primaria | documentacion oficial | consultado 2026-06-26 | Distingue contexto local del codigo y contexto visible para el LLM | https://openai.github.io/openai-agents-python/context/ |
| OpenAI, "Prompt engineering" | primaria | documentacion oficial | consultado 2026-06-26 | Define prompt engineering y mejores practicas para instrucciones efectivas | https://developers.openai.com/api/docs/guides/prompt-engineering |
| OpenAI Help, "Best practices for prompt engineering with the OpenAI API" | primaria | guia oficial/help center | consultado 2026-06-26 | Refuerza claridad, formato y estructura como condiciones de calidad | https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api |
| Anthropic Claude Docs, "Prompt engineering overview" | primaria | documentacion oficial | consultado 2026-06-26 | Enfatiza criterios de exito controlables por prompt y limites de prompt engineering | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview |
| LangChain, "Context Engineering" | secundaria/vendor tecnica | blog tecnico de framework | 2025 | Resume estrategias write, select, compress e isolate para agentes | https://www.langchain.com/blog/context-engineering-for-agents |
| LangChain Docs, "Context engineering in agents" | secundaria/vendor tecnica | documentacion de framework | consultado 2026-06-26 | Presenta context engineering como dar informacion, herramientas y formato correctos | https://docs.langchain.com/oss/python/langchain/context-engineering |
| LangChain, "How and when to build multi-agent systems" | secundaria/vendor tecnica | blog tecnico de framework | 2025 | Discute control sobre que se pasa al LLM y cuando conviene multiagente | https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems |
| Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" | primaria academica | paper TACL/arXiv | 2023/2024 | Evidencia que modelos long-context no usan informacion de forma robusta segun posicion | https://arxiv.org/abs/2307.03172 |
| Shi et al., "Large Language Models Can Be Easily Distracted by Irrelevant Context" | primaria academica | paper | 2023 | Evidencia sensibilidad a informacion irrelevante en razonamiento | https://www.semanticscholar.org/paper/Large-Language-Models-Can-Be-Easily-Distracted-by-Shi-Chen/3d68522abfadfc8ee6b7ec9edaaf91f1b2f38e5e |
| "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval" | primaria academica | paper | 2025 | Sugiere que longitud de input puede degradar performance incluso con recuperacion correcta | https://arxiv.org/html/2510.05381v1 |
| Microsoft Foundry, "Prompt engineering techniques" | primaria/vendor documentacion | documentacion oficial | 2026 | Recuerda que incluso con buen prompt hay que validar respuestas y limites | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering |

## Nivel de confianza

Moderado-alto.

La direccion es fuerte como tesis operativa y conceptual. La evidencia directa sobre SDD como metodologia especifica es indirecta, pero los pilares son consistentes: long context tiene fallas conocidas, agentes requieren context engineering, los handoffs son una abstraccion formal en frameworks actuales y la trazabilidad importa para produccion. No hay base suficiente para prometer cifras universales de ahorro de tokens; si se muestran numeros, deben quedar como medicion propia o estimacion reproducible.

## Decision de continuidad

seguir
