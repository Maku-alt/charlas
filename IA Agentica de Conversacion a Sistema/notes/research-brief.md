# Research brief: IA Agentica de Conversacion a Sistema

Research value: high

Decision de continuidad: seguir

## Idea o pregunta investigada

Que evidencia sostiene una charla practica sobre la transicion desde IA web aislada hacia IA agentica integrada en una estructura propia de trabajo para analisis y Data Science, con foco en contexto, herramientas, estado, seguridad operativa y revision humana.

La pregunta no es si los agentes son "mejores" que el chat web. La pregunta defendible para la charla es: que condiciones minimas hacen que la IA pase de ser ayuda conversacional a convertirse en capacidad operable dentro del trabajo analitico.

## Modo de trabajo

Modo orientado a decision.

La investigacion busca decidir el angulo de la charla, que comparacion conviene poner al centro, que claims son fuertes, cuales deben quedar como advertencia y que evidencia primaria puede sostener el mensaje.

## Nivel de esfuerzo

Standard.

Se revisaron fuentes primarias de laboratorios/proveedores, guias de seguridad y referencias de trabajo reproducible en data science. La evidencia es suficiente para pasar a narrativa, pero algunos claims de adopcion corporativa o capacidades de proveedores deberian revalidarse si se usan como ejemplos actuales en la deck final.

## Tesis propuesta

Tesis refinada:

> La transicion relevante no es de chat a otro producto de IA, sino de conversacion aislada a sistema de trabajo: reglas, contexto, herramientas, permisos, estado visible, outputs verificables y revision humana.

Formulacion breve para la charla:

> La IA agentica no empieza cuando el modelo responde mejor; empieza cuando trabaja dentro de un entorno que le dice que puede hacer, con que contexto, sobre que artefactos y bajo que limites.

La tesis es defendible porque las fuentes convergen en tres puntos:

- Los agentes se definen por usar herramientas y actuar en un entorno, no solo por generar texto.
- La efectividad depende de diseno de herramientas, contexto, instrucciones, evaluacion y feedback humano.
- La autonomia aumenta la superficie de riesgo, por lo que hacen falta limites: permisos, sandbox, scopes pequenos, proteccion de datos y revision.

## Resumen ejecutivo

Para una audiencia de analistas y Data Scientists, el framing mas fuerte es mostrar que el salto no es "usar mas IA", sino cambiar la unidad de trabajo.

En IA web aislada, la unidad de trabajo es la conversacion: util, rapida y flexible, pero con estado fragil, contexto pegado manualmente, outputs dificiles de auditar y decisiones que quedan en la memoria informal del usuario.

En IA agentica operable, la unidad de trabajo es un caso o workspace: instrucciones, fuentes, scripts, notebooks, estado, permisos, artefactos y criterios de cierre. El agente puede ayudar mas porque tiene donde mirar, que modificar, que producir y que no tocar.

La cita candidata de Anthropic queda validada. La forma correcta y enlazable es:

> "Agents are only as effective as the tools we give them." - Anthropic Engineering, "Writing tools for agents", 2025.

Enlace: https://www.anthropic.com/engineering/writing-tools-for-agents

## Panorama actual

Hechos verificados:

- Anthropic distingue entre workflows y agents; reserva "agent" para sistemas donde los LLMs dirigen procesos y uso de herramientas de forma dinamica, con cierto control sobre como cumplir la tarea.
- OpenAI documenta agentes como sistemas que combinan modelos, herramientas, instrucciones, guardrails, handoffs y estado/sessions.
- Google Cloud describe agentes de IA generativa como aplicaciones que persiguen objetivos observando informacion, razonando y actuando mediante herramientas, extensiones o funciones.
- OWASP identifica riesgos especificos de LLMs y agentes, incluyendo excessive agency, divulgacion de informacion sensible, tool misuse, supply chain y permisos excesivos.
- NIST AI 600-1 trata riesgos de GenAI como privacidad, seguridad, explicabilidad, control humano, dependencia excesiva y gestion de impactos.
- Practicas consolidadas de data science reproducible recomiendan estructura, documentacion, separacion de datos/codigo/resultados y artefactos rastreables.

Interpretacion:

- El agente no es solo un modelo con instrucciones largas. Es un actor de software que opera sobre recursos. Por eso necesita entorno.
- Para Data Science, el entorno natural no es una ventana de chat sino un repo/workspace con notebooks, scripts, datos permitidos, decisiones y outputs revisables.
- La estructura minima debe explicarse como responsabilidades, no como carpetas obligatorias. Si se vende como estandar rigido, la charla se vuelve burocratica.

Recomendacion:

- Presentar IA web como excelente punto de partida para exploracion, redaccion y desbloqueo puntual.
- Presentar IA agentica como siguiente nivel para trabajo recurrente, sensible o auditable.
- El centro debe ser el tradeoff: velocidad sin sistema vs capacidad operable con limites.

## Hallazgos que si merecen slide

1. El agente necesita entorno, no solo prompt

Objeto de prueba: definiciones de Anthropic/OpenAI/Google sobre agentes, herramientas y acciones.

Lectura: si el agente actua, necesita contexto, herramientas, permisos y criterios de cierre. Sin eso, solo se automatiza una conversacion fragil.

2. Las herramientas son parte del rendimiento

Objeto de prueba: cita validada de Anthropic y articulo "Writing tools for agents".

Lectura: un agente mal equipado falla aunque el modelo sea bueno. Para analisis, herramientas significa acceso controlado a archivos, notebooks, queries, scripts, metadata y outputs.

3. La estructura minima no es burocracia: es memoria operativa

Objeto de prueba: contraste entre chat aislado y workspace con `state.md`, inputs, outputs y decisiones.

Lectura: el estado visible reduce perdida de contexto, hace revisable el razonamiento y permite retomar trabajo sin depender de memoria informal.

4. Seguridad operativa es condicion para escalar

Objeto de prueba: OWASP LLM06 Excessive Agency, Anthropic Claude Code security guidance, OpenAI agent approvals/security, NIST AI 600-1.

Lectura: a mayor autonomia, mas importante es limitar acciones, datos y cambios. Los controles no son freno; son lo que permite usar agentes en trabajo real.

5. Data Science ya tiene una cultura compatible

Objeto de prueba: The Turing Way, Cookiecutter Data Science, Microsoft TDSP.

Lectura: reproducibilidad, separacion de datos/codigo/resultados, documentacion y revision ya son parte del oficio. La charla no inventa un metodo nuevo: traduce esas responsabilidades al trabajo con agentes.

6. El humano no desaparece; cambia de rol

Objeto de prueba: guardrails, approvals, human oversight y evaluacion humana en guias de proveedores y seguridad.

Lectura: el usuario deja de ser solo quien pregunta y pasa a ser quien disena limites, revisa artefactos y decide cierre.

## Mapa de contradicciones

Consensos fuertes:

- Agentes efectivos requieren herramientas y contexto.
- La autonomia debe operar con permisos y limites.
- Las acciones sobre datos, codigo o sistemas requieren revision y trazabilidad.
- Para trabajo analitico, la estructura mejora reproducibilidad y continuidad.

Conflictos o tensiones:

- Vendor framing: proveedores tienden a presentar agentes como salto de productividad; guias de seguridad enfatizan riesgos de exceso de agencia, datos sensibles y acciones no autorizadas.
- Flexibilidad vs estructura: demasiada estructura puede matar adopcion; demasiada libertad vuelve el trabajo irrevisable.
- Chat vs agente: el chat es mejor para exploracion abierta; el agente gana cuando hay tareas con artefactos, pasos, estado y criterios de exito.
- Automatizacion vs judgement: la narrativa de agentes puede sonar a reemplazo del humano, pero la evidencia de seguridad apunta a aprobaciones, scopes y supervision.

Claims debiles o que no conviene sobredimensionar:

- "Todo equipo necesita la misma estructura de carpetas." No esta sostenido y contradice la hipotesis adaptable.
- "Los agentes siempre son mejores que IA web." Falso como framing; depende de tarea, riesgo y costo de coordinacion.
- "Basta con un repo para estar seguros." Falso; el repo ayuda a trazabilidad, pero la seguridad depende de permisos, datos, revisiones, sandbox y cultura operativa.

Dato que cambiaria la conclusion:

- Evidencia fuerte de que agentes sin estado externo, sin tools bien disenadas y sin permisos granularizados logran resultados igualmente auditables en trabajo analitico recurrente. No aparecio evidencia convincente en esa direccion.

## Opciones o enfoques encontrados

| Opcion | Madurez | Ventajas | Limitaciones | Lectura para la charla |
|---|---|---|---|---|
| Chat web aislado | Alta adopcion | Rapido, flexible, baja friccion, ideal para exploracion | Estado fragil, contexto manual, trazabilidad limitada, dificil auditoria | Es el punto de partida, no el enemigo |
| Chat con convenciones personales | Media | Mejora prompts, plantillas y repetibilidad individual | Sigue dependiendo mucho de disciplina manual y memoria del usuario | Buen puente, insuficiente para trabajo sensible o recurrente |
| Repo/workspace minimo con agente | Emergente pero practico | Contexto, artefactos, estado, reglas, permisos y outputs revisables | Requiere orden minimo y curva operativa | Tesis principal: estructura minima como condicion de uso serio |
| Plataforma corporativa completa de agentes | En maduracion | Gobierno centralizado, integraciones, observabilidad | Puede ser pesada, lenta de adoptar o vender herramienta antes que metodo | Fuera del centro; mencionarla como evolucion posible, no como requisito |
| Automatizacion end-to-end | Variable por caso | Potencial de productividad alto en tareas repetibles | Mayor riesgo operativo; necesita evals, aprobaciones, rollback y monitoreo | No conviene ponerla como promesa de la charla |

## Direccion narrativa sugerida

Secuencia sugerida de 9 slides para que `narrative-charlas` cierre despues:

1. Kicker: el salto no es de herramienta, es de unidad de trabajo
   Titulo con tesis: "IA agentica empieza cuando la conversacion se convierte en sistema"
   Objeto de prueba visible: diagrama simple chat aislado vs workspace con reglas, contexto, tools, estado y review
   Takeaway: no se trata de abandonar IA web, sino de saber cuando ya no alcanza.

2. Kicker: el caso que todos reconocen
   Titulo con tesis: "Un analisis de negocio se rompe cuando el contexto vive solo en el chat"
   Objeto de prueba visible: flujo de analisis que evoluciona a features, con inputs, decisiones y outputs dispersos
   Takeaway: el problema no es la calidad de la respuesta, sino la continuidad del trabajo.

3. Kicker: que cambia con un agente
   Titulo con tesis: "Un agente no solo responde: usa herramientas y modifica artefactos"
   Objeto de prueba visible: definiciones de agentes desde Anthropic/OpenAI/Google resumidas en 3 verbos: observar, decidir, actuar
   Takeaway: actuar exige limites operativos.

4. Kicker: el rendimiento no vive solo en el modelo
   Titulo con tesis: "Los agentes son tan buenos como el entorno que les damos"
   Objeto de prueba visible: cita validada de Anthropic + ejemplos de tools para Data Science
   Takeaway: herramientas, contexto e instrucciones son parte del diseno, no accesorios.

5. Kicker: el sistema minimo
   Titulo con tesis: "No necesitamos una carpeta unica; necesitamos responsabilidades claras"
   Objeto de prueba visible: matriz de responsabilidades: contexto, datos permitidos, estado, outputs, decisiones, review
   Takeaway: la estructura debe ser adaptable, pero las responsabilidades no son opcionales.

6. Kicker: seguridad como capacidad, no como freno
   Titulo con tesis: "La autonomia solo escala con permisos pequenos y revision humana"
   Objeto de prueba visible: controles operativos mapeados a riesgos: sandbox, scopes, datos sensibles, approvals, logs
   Takeaway: los controles permiten usar agentes en trabajo real sin apostar todo a la confianza.

7. Kicker: traduccion a Data Science
   Titulo con tesis: "Para analisis y features, el estado visible es parte del metodo"
   Objeto de prueba visible: ejemplo adaptable de `state.md`, notebooks, scripts, fuentes, pendientes y outputs
   Takeaway: trazabilidad no es documentacion extra; es lo que permite revisar y retomar.

8. Kicker: donde no conviene sobrediseniar
   Titulo con tesis: "El sistema minimo debe ayudar mas de lo que estorba"
   Objeto de prueba visible: tradeoff simple: exploracion, trabajo recurrente, trabajo sensible, automatizacion
   Takeaway: no todo amerita agente; el criterio es riesgo, recurrencia y necesidad de trazabilidad.

9. Kicker: cierre editorial
   Titulo con tesis: "La IA no reemplaza el sistema de trabajo. Lo exige."
   Objeto de prueba visible: imagen editorial de una mesa de trabajo con herramientas, permisos/llaves, bitacora y humano revisando
   Takeaway: el valor no esta en soltar al agente, sino en darle un lugar seguro donde trabajar.

## Claims a validar antes de cerrar la deck

Claims listos para usar con fuente:

- "Agents are only as effective as the tools we give them." Fuente validada: Anthropic Engineering, "Writing tools for agents".
- Los agentes combinan modelo, herramientas, instrucciones/guardrails y estado. Fuentes: OpenAI Agents docs, Anthropic Building effective agents, Google Cloud agentic AI overview.
- La agencia excesiva es un riesgo reconocido en aplicaciones LLM. Fuente: OWASP LLM06 Excessive Agency.
- El control humano, privacidad y gestion de riesgos son preocupaciones centrales de GenAI. Fuente: NIST AI 600-1.

Claims que requieren cuidado o validacion adicional:

- Cualquier afirmacion sobre capacidades actuales de una herramienta especifica, precios, planes empresariales, integraciones o politicas de datos debe verificarse en la fecha de build.
- Si se menciona una plataforma corporativa especifica, revisar documentacion actual de permisos, aislamiento, retencion y conectores.
- Si se afirma que una estructura concreta mejora productividad, presentarlo como hipotesis operacional o experiencia de trabajo, no como benchmark cuantitativo salvo que haya medicion propia.
- Si se usan casos corporativos recientes, validar con fuente primaria o reporte confiable de fecha cercana.

## Riesgos y consideraciones

- Riesgo de framing: sonar a "chat malo, agentes buenos". Mitigacion: abrir reconociendo que IA web es excelente para exploracion y tareas puntuales.
- Riesgo de burocracia: que el publico crea que la charla vende carpetas. Mitigacion: hablar de responsabilidades minimas, no de estructura unica.
- Riesgo de seguridad abstracta: convertir la charla en compliance. Mitigacion: seguridad operativa concreta: permisos, sandbox, scopes, datos sensibles, aprobaciones y review.
- Riesgo de hype: prometer autonomia sin evaluar riesgo. Mitigacion: decir que el humano no desaparece; cambia de rol.
- Riesgo de sobrediseno: aplicar agentes a tareas donde un chat o script basta. Mitigacion: proponer criterio de decision por recurrencia, sensibilidad, trazabilidad y costo de error.

## Recomendacion

Usaria como tesis principal:

> El salto a IA agentica no consiste en darle mas instrucciones al modelo, sino en darle un entorno de trabajo gobernado: contexto, herramientas, estado, permisos y revision.

Comparacion central:

- Conversacion aislada: velocidad y flexibilidad, con contexto fragil.
- Sistema de trabajo: mas friccion inicial, pero mayor continuidad, seguridad, trazabilidad y capacidad de revision.

Dejaria fuera para no diluir:

- Comparacion de proveedores.
- Arquitectura avanzada de MCP/RAG/orquestadores.
- Demo tecnica en vivo.
- Promesa de automatizacion end-to-end.
- Estandar rigido de carpetas.

Recomendacion para build-spec:

- Usar un caso conductor de analisis de negocio que escala a preparacion de features.
- Visualizar el cambio de unidad de trabajo: chat -> caso/workspace.
- Mostrar una estructura minima como ejemplo adaptable, no como mandato.
- Hacer de seguridad una slide practica, no legalista.
- Cerrar con frase fuerte y visual editorial, no con resumen tecnico.

## Cierre editorial propuesto

Mensaje final de una linea:

> La IA no reemplaza el sistema de trabajo. Lo exige.

Cita breve validada:

> "Agents are only as effective as the tools we give them." - Anthropic

Metafora visual sugerida:

- Un banco de trabajo editorial y sobrio: herramientas ordenadas, una bitacora abierta, permisos/llaves visibles, artefactos en revision y una persona tomando la decision final. Debe sentirse como sistema operativo de trabajo, no como robot futurista.

Tono emocional:

- Sobrio, pragmatico, ejecutivo. Sensacion de madurez: pasar de entusiasmo individual a capacidad confiable.

## Donde profundizar despues

- Ejemplos concretos de estructura minima para analisis y features: `context.md`, `state.md`, `data-policy.md`, `outputs/`, `review.md` o equivalentes.
- Checklist de seguridad operativa para agentes en equipos de datos: datos permitidos, permisos de escritura, sandbox, aprobaciones, logs y criterio de cierre.
- Ejemplos de prompts/instrucciones de equipo que convierten normas tacitas en reglas reutilizables.
- Casos internos o experiencias propias donde la falta de estado haya causado retrabajo o mala trazabilidad.
- Una decision de narrativa: cuanto del ejemplo debe ser repo tecnico y cuanto debe ser lenguaje de responsabilidades para no perder a analistas no programadores.

## Self-review

Confidence score: 0.82

Weakest link: no hay benchmark independiente y general que mida "estructura minima de workspace" vs "chat aislado" en productividad o calidad para Data Science. La tesis se sostiene mejor como argumento operacional basado en definiciones de agentes, seguridad y reproducibilidad, no como claim cuantitativo.

Bias check: muchas fuentes primarias son de proveedores que tienen incentivo a promover agentes. Se compenso con OWASP, NIST y referencias de reproducibilidad. Aun asi, conviene evitar lenguaje de inevitabilidad.

Missing perspective: seria valioso sumar evidencia interna o experiencia de usuarios reales sobre friccion de adopcion. El punto es importante para no sobrediseniar el sistema minimo.

What would change my mind: evidencia de que equipos de datos consiguen trazabilidad, seguridad y continuidad comparables solo con chat web y buenas practicas de prompting, sin estado externo ni permisos definidos.

## Fuentes consultadas

| Fuente | Clase | Tipo | Fecha | Relevancia | Enlace |
|---|---|---|---|---|---|
| Anthropic Engineering, "Writing tools for agents" | Primaria | Blog tecnico de laboratorio | 2025 | Valida la cita candidata y sostiene que el diseno de tools condiciona la efectividad del agente | https://www.anthropic.com/engineering/writing-tools-for-agents |
| Anthropic, "Building effective agents" | Primaria | Research/engineering guidance | 2024 | Diferencia workflows y agents; aporta marco para tools, control dinamico y patrones simples | https://www.anthropic.com/engineering/building-effective-agents |
| Anthropic Claude Code security | Primaria | Documentacion de producto | Vigente | Controles practicos: permisos, aprobaciones, proteccion de datos, trabajo en repos y ejecucion segura | https://docs.anthropic.com/en/docs/claude-code/security |
| OpenAI Platform, Agents guide | Primaria | Documentacion oficial | Vigente | Define componentes de agentes: models, tools, instructions, guardrails, handoffs/contexto | https://platform.openai.com/docs/guides/agents |
| OpenAI Agents SDK docs | Primaria | Documentacion tecnica | Vigente | Referencia concreta para tools, guardrails, handoffs, sessions y tracing | https://openai.github.io/openai-agents-python/ |
| OpenAI, Codex agent approvals and security | Primaria | Documentacion tecnica | Vigente | Evidencia controles de sandbox, aprobaciones y limites operativos para agentes de codigo | https://developers.openai.com/codex/agent-approvals-security/ |
| Google Cloud, Agentic AI overview | Primaria | Documentacion cloud | Vigente | Explica agentes como sistemas que razonan, actuan y usan herramientas en un entorno | https://docs.cloud.google.com/architecture/agentic-ai-overview |
| Google/Kaggle, "Agents" whitepaper | Primaria/secundaria | Whitepaper tecnico | 2024 | Marco didactico sobre razonamiento, herramientas, memory/state y actuacion de agentes | https://www.kaggle.com/whitepaper-agents |
| OWASP Top 10 for LLM Applications 2025 | Autoridad independiente | Guia de seguridad | 2025 | Riesgos como excessive agency, sensitive information disclosure y supply chain | https://genai.owasp.org/llm-top-10/ |
| OWASP LLM06: Excessive Agency | Autoridad independiente | Riesgo especifico | 2025 | Fuente directa para justificar permisos limitados, scopes pequenos y aprobaciones humanas | https://genai.owasp.org/llmrisk/llm06-excessive-agency/ |
| NIST AI 600-1, Artificial Intelligence Risk Management Framework: Generative AI Profile | Autoridad publica | Marco de riesgo | 2024 | Sustenta privacidad, control humano, riesgos de seguridad, dependencia y gobernanza de GenAI | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf |
| The Turing Way, reproducible research compendia | Comunidad/academica | Guia de reproducibilidad | Vigente | Apoya la idea de estructura, documentacion, codigo, datos y resultados rastreables | https://book.the-turing-way.org/reproducible-research/compendia/ |
| Cookiecutter Data Science | Comunidad/industria | Guia de estructura de proyecto | Vigente | Ejemplo conocido de organizacion reproducible para proyectos de data science | https://cookiecutter-data-science.drivendata.org/ |
| Microsoft Team Data Science Process | Primaria/industria | Metodologia tecnica | Vigente | Refuerza ciclo de vida, artefactos y colaboracion en proyectos de data science | https://learn.microsoft.com/en-us/azure/architecture/data-science-process/overview |

## Nivel de confianza

Alto para la tesis cualitativa: agentes efectivos requieren entorno, herramientas, contexto, permisos y revision.

Moderado para recomendaciones de estructura concreta: hay buen soporte por analogia con reproducibilidad y metodos de data science, pero no debe presentarse como unico estandar.

Bajo para claims cuantitativos de productividad: no usar numeros sin evidencia propia o fuente primaria confiable.

