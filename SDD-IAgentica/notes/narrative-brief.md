# Narrative Brief: SDD e IA agentica con contexto acotado

## Tesis propuesta

SDD no hace mas inteligente al agente; hace mas legible y gobernable el trabajo. Su valor esta en disenar el contexto por fase: cada subagente recibe un contrato pequeno con objetivo, entradas, restricciones, artefactos esperados y criterio de salida.

La charla debe defender que la unidad de trabajo en IA agentica no es una conversacion mas larga, sino un handoff verificable.

## Lectura narrativa

La narrativa parte de un dolor operativo conocido por Data Scientists y equipos tecnicos: una conversacion larga funciona al inicio, pero se vuelve fragil cuando mezcla exploracion, decisiones, descartes, fuentes, instrucciones, outputs y revisiones en el mismo historial.

El giro no es "usar mas agentes". El giro es tratar el contexto como superficie de trabajo. SDD convierte el historial en contratos de fase: research, narrativa, build y review pueden ejecutarse con contexto acotado, dejando evidencia revisable y preservando en el chat principal solo las decisiones que importan.

La charla debe sonar practica, no metodologica. No vende documentacion por documentacion. Vende menos arrastre, mas foco, mejores gates y mayor capacidad de repetir o corregir una fase sin contaminar todo el flujo.

## Audiencia y cambio esperado

Audiencia principal: Data Scientists, analistas tecnicos, ingenieros de datos y perfiles que ya usan IA para trabajo real, pero sienten que los flujos largos se vuelven dificiles de auditar, reproducir o continuar.

Cambio esperado: pasar de optimizar prompts aislados a disenar sistemas de trabajo con fases, specs, handoffs, artefactos y reviews.

Lectura ejecutiva esperada: si el trabajo es corto, una conversacion puede bastar; si el trabajo es largo, costoso o revisable, el contexto debe disenarse como un pipeline.

## Comparacion o tension central

Conversacion monolitica vs. orquestacion por fases con contexto acotado.

- Conversacion monolitica: rapida, flexible y natural; pero arrastra ruido, mezcla objetivos y vuelve dificil saber que decision produjo que resultado.
- SDD agentico: mas explicito y auditable; pero exige buenos contratos, handoffs proporcionados y gates humanos.

La tension debe presentarse sin caricatura. Long context y chats largos no son malos; son capacidad. SDD agrega gobernanza cuando la capacidad sola ya no basta.

## Lo que queda fuera

- Benchmarks numericos universales o comparativas entre vendors.
- Comparativas entre vendors o plataformas.
- Promesas de autonomia total sin supervision.
- Detalles internos de Codex, OpenAI, Claude o frameworks especificos.
- Profundizacion academica sobre cada paper de contexto largo.
- Slides de "metodologia SDD" como checklist burocratico.

## Narrativa propuesta de la charla

### Slide 1

- kicker: Tesis
- titulo con tesis: SDD convierte agentes en workflow, no en una conversacion larga
- objeto de prueba visible: contraste visual entre un chat monolitico lleno de historial y un flujo de fases con specs pequenos
- takeaway: El valor no esta en hablar mas con la IA; esta en darle mejores unidades de trabajo.
- notas de soporte: Abrir con la tesis refinada. SDD no aumenta magicamente la capacidad del modelo. Hace que el trabajo sea mas legible, transferible y verificable.

### Slide 2

- kicker: Dolor operativo
- titulo con tesis: El historial completo se vuelve deuda de contexto
- objeto de prueba visible: pila de contexto con capas mezcladas: dudas, descartes, fuentes, decisiones, instrucciones y outputs
- takeaway: En trabajos largos, el chat deja de ser solo memoria y empieza a ser ruido operativo.
- notas de soporte: Conectar con la experiencia de equipos tecnicos: el modelo recibe todo, pero no todo sigue siendo relevante. El humano tambien pierde trazabilidad.

### Slide 3

- kicker: Baseline
- titulo con tesis: Una ventana grande no decide que informacion importa
- objeto de prueba visible: comparacion entre "capacidad de contexto" y "calidad de contexto"
- takeaway: Long context es una posibilidad tecnica; no es una estrategia de trabajo.
- notas de soporte: Usar la evidencia de long context con cuidado: no afirmar que ventanas largas fallan siempre. La lectura es que mas tokens no eliminan la necesidad de curadoria, posicionamiento y reduccion de distractores.

### Slide 4

- kicker: Cambio de lente
- titulo con tesis: Context engineering trata el contexto como un recurso disenado
- objeto de prueba visible: matriz simple con cuatro acciones: seleccionar, comprimir, aislar y persistir
- takeaway: La pregunta deja de ser "que prompt escribo" y pasa a ser "que contexto necesita esta fase".
- notas de soporte: Traducirlo para Data Scientists: se parece mas a seleccionar features para una tarea que a guardar todo el dataset en cada paso.

### Slide 5

- kicker: Metodo
- titulo con tesis: El spec reemplaza al recuerdo como unidad de coordinacion
- objeto de prueba visible: contrato de fase con entradas, restricciones, output esperado y gate de aceptacion
- takeaway: Un subagente no necesita toda la historia si recibe un contrato claro.
- notas de soporte: Esta es la slide central. Debe dejar claro que SDD disena el paquete de trabajo: objetivo, artefactos, limites, formato de salida y decision esperada.

### Slide 6

- kicker: Workflow
- titulo con tesis: El chat principal guarda decisiones; los subagentes ejecutan fases
- objeto de prueba visible: flujo orchestrator -> research -> narrative -> build -> review, con handoffs entre estaciones
- takeaway: Separar fases reduce mezcla de roles y hace mas facil repetir, corregir o auditar una parte.
- notas de soporte: Mostrar que research no pasa automaticamente a PPT; primero se converge angulo, luego narrativa, luego build, luego review. El chat principal conserva continuidad editorial y decisiones, no todo el proceso bruto.

### Slide 7

- kicker: Control
- titulo con tesis: Handoffs y gates hacen visible lo que antes era intuicion
- objeto de prueba visible: ejemplo conceptual de handoff verificable: input, salida, criterio de aceptacion y evidencia
- takeaway: La calidad mejora cuando se puede revisar donde fallo el flujo.
- notas de soporte: Conectar con tracing, outputs estructurados y guardrails sin entrar en detalle de herramientas. El punto es auditabilidad: no solo "me gusto/no me gusto", sino evidencia por fase.

### Slide 8

- kicker: Tradeoff
- titulo con tesis: SDD falla cuando el contrato es peor que la conversacion
- objeto de prueba visible: tabla corta de uso proporcional: tarea pequena, tarea larga, riesgo alto, specs pobres, informacion tacita
- takeaway: SDD no elimina criterio humano; lo obliga a aparecer antes.
- notas de soporte: Esta slide evita hype. Debe decir que SDD tiene overhead, puede cortar contexto critico y puede fragmentar decisiones si los specs son malos. La recomendacion es usarlo cuando la longitud, el costo del error o la necesidad de review lo justifican.

### Slide 9

- kicker: Decision
- titulo con tesis: Para trabajos largos, el contexto debe operar como pipeline
- objeto de prueba visible: before/after del flujo: de "chat acumulado" a "fase, spec, artefacto, review y decision"
- takeaway: La practica reutilizable es disenar handoffs, no acumular historial.
- notas de soporte: Convertir el research en recomendacion concreta para la audiencia. Empezar con pocos templates, outputs claros y gates visibles. No vender multiagente como fin; vender gobernabilidad del trabajo.

### Slide 10

- kicker: Cierre
- titulo con tesis: La nueva habilidad es disenar el contexto que otros agentes pueden ejecutar
- objeto de prueba visible: imagen editorial de mesa de control o mesa editorial con pequenos paquetes de trabajo iluminados, rutas de ejecucion al fondo y espacio para frase final
- takeaway: Menos conversacion acumulada; mas contratos de trabajo.
- notas de soporte: Cerrar con una frase breve, no con resumen tecnico. Evitar robots, dashboards, tablas o diagramas. La imagen debe sentirse sobria, editorial y deliberada.

## Estructura de cierre

Mensaje final recomendado:

> El futuro no es hablar mas con la IA; es darle mejores unidades de trabajo.

Frase de cierre alternativa para superponer en la imagen:

> Contexto no es memoria. Contexto es diseno.

Direccion visual:

Una sala de control sobria o mesa editorial con paquetes pequenos de trabajo etiquetados, iluminados como planos operativos. Debe transmitir precision, foco y continuidad. No debe verse como un dashboard tecnico, una tabla, una linea de ensamblaje literal ni una imagen generica de robots.

Funcion narrativa del cierre:

La audiencia debe salir con una decision mental clara: en IA agentica, el problema no es recordar mas historial; es construir unidades de trabajo que puedan ejecutarse, revisarse y transferirse.

## Riesgos narrativos

- Sonar burocratico: si las slides hablan demasiado de "documentar", se pierde la tesis. El lenguaje debe ser trabajo, contratos, gates y foco.
- Sonar anti-long-context: la charla debe reconocer que ventanas largas ayudan, pero no reemplazan seleccion ni gobierno.
- Prometer ahorro cuantitativo universal: los claims de tokens deben quedar como medicion propia o estimacion reproducible, no como garantia general.
- Confundir subagentes con magia: enfatizar que el contrato y el gate importan mas que el numero de agentes.
- Volverse demasiado abstracta: cada slide necesita un objeto de prueba visible y una lectura operacional.
- Diluir el cierre: no terminar con una lista de beneficios; terminar con la idea de unidades de trabajo verificables.

## Listo para build

Decision: listo para build.

Condiciones para el builder:

- Mantener 10 slides solo si el ritmo visual permite aire suficiente; si hace falta recortar, fusionar Slide 3 y Slide 4.
- No usar claims numericos de ahorro de tokens sin medicion propia y nota metodologica.
- No nombrar vendors salvo como soporte en notas o fuentes, no como centro de la narrativa.
- Priorizar comparaciones visuales, contratos de fase y before/after por encima de diagramas densos.
