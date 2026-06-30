# Narrative Spec

## Tesis propuesta

La transicion relevante no es de chat a otro producto de IA, sino de conversacion aislada a sistema de trabajo: reglas, contexto, herramientas, permisos, estado visible, outputs verificables y revision humana.

Formulacion para la charla:

> La IA agentica no empieza cuando el modelo responde mejor; empieza cuando trabaja dentro de un entorno que le dice que puede hacer, con que contexto, sobre que artefactos y bajo que limites.

Version de cierre:

> La IA no reemplaza el sistema de trabajo. Lo exige.

## Lectura narrativa

La charla debe mover a la audiencia desde una lectura de IA como interfaz hacia una lectura de IA como capacidad operable.

El punto de partida no es criticar la IA web. La IA web es util, rapida y de baja friccion para explorar, redactar, desbloquear ideas y hacer trabajo puntual. El problema aparece cuando el trabajo se vuelve recurrente, sensible, colaborativo o auditable: el contexto queda pegado manualmente, el estado vive en la conversacion, los criterios de cierre no son visibles y las decisiones quedan en memoria informal.

La IA agentica cambia la unidad de trabajo. Ya no se trata solo de una conversacion, sino de un caso o workspace donde existen instrucciones, fuentes permitidas, scripts, notebooks, estado, outputs, permisos, revision y criterios de cierre.

La lectura ejecutiva es: el valor no esta en soltar al agente, sino en darle un lugar gobernado donde trabajar.

## Audiencia y cambio esperado

Audiencia:

- Analistas y Data Scientists dentro de una gerencia donde muchas personas ya hacen analisis y usan IA web.
- Personas con distintos niveles de familiaridad con repositorios, agentes de codigo y estructuras reproducibles.
- Equipos que necesitan mejorar continuidad, trazabilidad y calidad sin imponer una unica forma de organizar cada proyecto.

Cambio esperado:

- Pasar de "que tan bueno es el modelo" a "que entorno necesita para producir trabajo revisable".
- Reconocer que chat web, convenciones personales, workspace minimo y plataforma corporativa completa son opciones distintas, no una escalera obligatoria para todo caso.
- Salir con una pregunta de equipo: que responsabilidades minimas queremos compartir para que el uso de IA sea trazable, seguro y revisable sin matar la flexibilidad.

## Comparacion o tension central

La tension central es velocidad sin sistema versus capacidad operable con limites.

| Modo | Ventaja | Limite | Lectura |
|---|---|---|---|
| Conversacion aislada | Rapida, flexible, facil de empezar | Estado fragil, contexto manual, poca trazabilidad | Excelente para exploracion y tareas puntuales |
| Convenciones personales | Mejora prompts y repetibilidad individual | Depende de disciplina manual y memoria del usuario | Buen puente, insuficiente para trabajo sensible o recurrente |
| Sistema minimo de trabajo | Contexto, artefactos, estado, reglas, permisos y outputs revisables | Requiere orden minimo y friccion inicial | La opcion defendida para trabajo analitico serio |
| Plataforma corporativa completa | Gobierno centralizado e integraciones | Puede vender herramienta antes que metodo | Evolucion posible, no requisito de la charla |

La charla debe evitar el framing "chat malo, agente bueno". El criterio es riesgo, recurrencia, sensibilidad, necesidad de trazabilidad y costo de error.

## Lo que queda fuera

- Demo tecnica en vivo.
- Comparacion de proveedores.
- Arquitectura avanzada de MCP, RAG, orquestadores o multiagentes.
- Promesa de automatizacion end-to-end.
- Estandar cerrado de carpetas.
- Benchmarks cuantitativos de productividad sin evidencia propia.
- Claims actuales sobre precios, planes, compatibilidad, retencion de datos o casos corporativos recientes.

## Narrativa propuesta de la charla

### Slide 1

- kicker: Cambio de unidad
- titulo con tesis: IA agentica empieza cuando la conversacion se convierte en sistema
- objeto de prueba visible: comparacion simple entre chat aislado y workspace con reglas, contexto, tools, estado y review
- takeaway: no se trata de abandonar IA web, sino de saber cuando ya no alcanza
- notas de soporte: abrir reconociendo el valor del chat web; situar la charla como madurez operativa, no como hype de una herramienta nueva.

### Slide 2

- kicker: El caso que todos reconocen
- titulo con tesis: Un analisis se rompe cuando el contexto vive solo en el chat
- objeto de prueba visible: flujo de analisis de negocio hacia features con inputs, hipotesis, decisiones, archivos y outputs dispersos
- takeaway: el problema no es solo la calidad de la respuesta, sino la continuidad del trabajo
- notas de soporte: usar un caso conductor cercano a Data Science: pedido de negocio, exploracion, fuentes, hipotesis, features candidatas, validacion y cierre.

### Slide 3

- kicker: Que cambia con un agente
- titulo con tesis: Un agente no solo responde: usa herramientas y modifica artefactos
- objeto de prueba visible: tres verbos resumidos desde fuentes de agentes: observar, decidir, actuar
- takeaway: actuar exige limites operativos
- notas de soporte: apoyarse en definiciones convergentes de Anthropic, OpenAI y Google: agentes combinan modelo, instrucciones, herramientas, estado/contexto y acciones en un entorno.

### Slide 4

- kicker: Rendimiento real
- titulo con tesis: Los agentes son tan buenos como el entorno que les damos
- objeto de prueba visible: cita de Anthropic junto a ejemplos de tools para Data Science: archivos, notebooks, queries, scripts, metadata, outputs
- takeaway: herramientas, contexto e instrucciones son parte del diseno, no accesorios
- notas de soporte: mantener la cita validada: "Agents are only as effective as the tools we give them." - Anthropic Engineering, "Writing tools for agents", 2025.

### Slide 5

- kicker: Sistema minimo
- titulo con tesis: No necesitamos una carpeta unica; necesitamos responsabilidades claras
- objeto de prueba visible: matriz de responsabilidades: reglas, contexto, datos permitidos, estado, outputs, decisiones, review
- takeaway: la estructura debe ser adaptable, pero las responsabilidades no son opcionales
- notas de soporte: evitar vender un arbol de directorios como solucion universal; presentar equivalencias posibles para equipos tecnicos y no tecnicos.

### Slide 6

- kicker: Seguridad operativa
- titulo con tesis: La autonomia solo escala con permisos pequenos y revision humana
- objeto de prueba visible: mapa riesgo-control: datos sensibles, sandbox, scopes pequenos, approvals, logs, cambios revisables
- takeaway: los controles no frenan el uso de agentes; son lo que permite usarlos en trabajo real
- notas de soporte: apoyarse en OWASP Excessive Agency, guias de seguridad de agentes/codigo y NIST AI 600-1; no convertir la slide en compliance abstracto.

### Slide 7

- kicker: Traduccion a Data Science
- titulo con tesis: Para analisis y features, el estado visible es parte del metodo
- objeto de prueba visible: ejemplo adaptable de caso con `state.md` o equivalente, notebooks, scripts, fuentes, pendientes, outputs y revision
- takeaway: trazabilidad no es documentacion extra; es lo que permite revisar, retomar y transferir el trabajo
- notas de soporte: conectar con practicas ya familiares de reproducibilidad: separar datos, codigo, resultados, decisiones y artefactos.

### Slide 8

- kicker: Criterio de adopcion
- titulo con tesis: El sistema minimo debe ayudar mas de lo que estorba
- objeto de prueba visible: matriz de decision por exploracion, trabajo recurrente, trabajo sensible y automatizacion
- takeaway: no todo amerita agente; el criterio es recurrencia, sensibilidad, trazabilidad y costo de error
- notas de soporte: esta slide protege contra sobrediseno. Mantener IA web como opcion correcta para exploracion abierta o tareas de baja consecuencia.

### Slide 9

- kicker: Cierre editorial
- titulo con tesis: La IA no reemplaza el sistema de trabajo. Lo exige.
- objeto de prueba visible: imagen editorial de una mesa de trabajo con herramientas, bitacora, permisos/llaves, artefactos en revision y una persona tomando la decision final
- takeaway: el valor no esta en soltar al agente, sino en darle un lugar seguro donde trabajar
- notas de soporte: cerrar con una sola idea fuerte. No resumir tecnicamente las slides anteriores.

## Estructura de cierre

Mensaje final:

> La IA no reemplaza el sistema de trabajo. Lo exige.

Cita validada:

> "Agents are only as effective as the tools we give them." - Anthropic Engineering, "Writing tools for agents", 2025.

Fuente:

- https://www.anthropic.com/engineering/writing-tools-for-agents

Direccion visual:

- Una imagen editorial, sobria y deliberada.
- Metafora: banco o mesa de trabajo de un equipo analitico, con herramientas ordenadas, bitacora abierta, permisos/llaves visibles, artefactos en revision y una persona tomando la decision final.
- La IA debe sentirse como capa que conecta el flujo, no como robot o chatbot protagonista.
- No repetir tablas, bullets ni diagramas de la charla.

Emocion buscada:

- Madurez operativa.
- Paso de entusiasmo individual a capacidad confiable.
- Convocatoria practica: definir un minimo comun de equipo.

## Riesgos narrativos

- Riesgo de sonar anti-chat: mitigarlo declarando que IA web es excelente para exploracion y tareas puntuales.
- Riesgo de burocracia: mitigarlo hablando de responsabilidades minimas, no de carpetas obligatorias.
- Riesgo de seguridad abstracta: mitigarlo con controles concretos: permisos, sandbox, scopes, datos sensibles, aprobaciones, logs y review.
- Riesgo de hype agentico: mitigarlo evitando promesas de autonomia completa y manteniendo al humano como responsable de limites, revision y cierre.
- Riesgo de perder a analistas no programadores: mitigarlo con lenguaje de casos, decisiones y responsabilidades antes que jerga de repositorios.
- Riesgo de claim cuantitativo debil: no usar numeros de productividad ni superioridad sin evidencia propia.

## Listo para build

Decision: listo para build.

Condiciones para build:

- Construir 9 slides, no 10, salvo que el deck-builder encuentre una razon visual fuerte para separar seguridad y decision de adopcion.
- Mantener titulos como conclusiones, no encabezados genericos.
- Usar el caso conductor de analisis de negocio que evoluciona hacia features.
- Presentar cualquier estructura de carpetas como ejemplo adaptable, no como estandar obligatorio.
- Verificar de nuevo claims actuales si se agregan proveedores, precios, releases, politicas de datos o casos corporativos recientes.
