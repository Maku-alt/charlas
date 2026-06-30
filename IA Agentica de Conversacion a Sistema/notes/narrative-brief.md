# Narrative brief: IA Agentica de Conversacion a Sistema

Decision: listo para build

## Tesis propuesta

La transicion relevante no es de chat a otro producto de IA, sino de conversacion aislada a sistema de trabajo: reglas, contexto, herramientas, permisos, estado visible, outputs verificables y revision humana.

Formula corta:

> La IA agentica no empieza cuando el modelo responde mejor; empieza cuando trabaja dentro de un entorno que le dice que puede hacer, con que contexto, sobre que artefactos y bajo que limites.

## Lectura narrativa

La charla debe mostrar que el salto a IA agentica no es usar mas IA, sino cambiar la unidad de trabajo.

En IA web aislada, la unidad de trabajo es la conversacion: rapida y flexible, pero con estado fragil y trazabilidad limitada.

En IA agentica operable, la unidad de trabajo es un caso o workspace: instrucciones, fuentes permitidas, herramientas, artefactos, estado, permisos, outputs y revision.

## Audiencia y cambio esperado

Audiencia: analistas y Data Scientists que ya usan IA web, pero no necesariamente trabajan con agentes de codigo ni repositorios como sistema de trabajo.

Cambio esperado: salir de "que tan bueno es el modelo" y pasar a "que entorno necesita para producir trabajo revisable".

Pregunta final de equipo: que responsabilidades minimas queremos compartir para que el uso de IA sea trazable, seguro y revisable sin imponer una unica forma de trabajar.

## Comparacion o tension central

Velocidad sin sistema versus capacidad operable con limites.

- Conversacion aislada: rapida, flexible, facil de empezar; fragil para continuidad, trazabilidad y auditoria.
- Sistema minimo: mas friccion inicial; mayor continuidad, seguridad, trazabilidad y capacidad de revision.

La charla no debe decir "chat malo, agentes buenos". El criterio es riesgo, recurrencia, sensibilidad, necesidad de trazabilidad y costo de error.

## Lo que queda fuera

- Demo tecnica en vivo.
- Comparacion de proveedores.
- Arquitectura avanzada de MCP, RAG, orquestadores o multiagentes.
- Automatizacion end-to-end como promesa.
- Estandar cerrado de carpetas.
- Benchmarks cuantitativos de productividad sin evidencia propia.

## Narrativa propuesta de 9 slides

### 1. Cambio de unidad

- kicker: Cambio de unidad
- titulo con tesis: IA agentica empieza cuando la conversacion se convierte en sistema
- objeto de prueba visible: chat aislado vs workspace con reglas, contexto, tools, estado y review
- takeaway: no se trata de abandonar IA web, sino de saber cuando ya no alcanza

### 2. El caso que todos reconocen

- kicker: El caso que todos reconocen
- titulo con tesis: Un analisis se rompe cuando el contexto vive solo en el chat
- objeto de prueba visible: flujo de analisis de negocio hacia features con inputs, hipotesis, decisiones y outputs dispersos
- takeaway: el problema no es solo la calidad de la respuesta, sino la continuidad del trabajo

### 3. Que cambia con un agente

- kicker: Que cambia con un agente
- titulo con tesis: Un agente no solo responde: usa herramientas y modifica artefactos
- objeto de prueba visible: observar, decidir, actuar
- takeaway: actuar exige limites operativos

### 4. Rendimiento real

- kicker: Rendimiento real
- titulo con tesis: Los agentes son tan buenos como el entorno que les damos
- objeto de prueba visible: cita de Anthropic + tools de Data Science
- takeaway: herramientas, contexto e instrucciones son parte del diseno, no accesorios

### 5. Sistema minimo

- kicker: Sistema minimo
- titulo con tesis: No necesitamos una carpeta unica; necesitamos responsabilidades claras
- objeto de prueba visible: matriz de reglas, contexto, datos permitidos, estado, outputs, decisiones y review
- takeaway: la estructura debe ser adaptable, pero las responsabilidades no son opcionales

### 6. Seguridad operativa

- kicker: Seguridad operativa
- titulo con tesis: La autonomia solo escala con permisos pequenos y revision humana
- objeto de prueba visible: riesgo-control: datos sensibles, sandbox, scopes, approvals, logs, cambios revisables
- takeaway: los controles no frenan el uso de agentes; son lo que permite usarlos en trabajo real

### 7. Traduccion a Data Science

- kicker: Traduccion a Data Science
- titulo con tesis: Para analisis y features, el estado visible es parte del metodo
- objeto de prueba visible: caso con `state.md` o equivalente, notebooks, scripts, fuentes, pendientes, outputs y revision
- takeaway: trazabilidad no es documentacion extra; permite revisar, retomar y transferir el trabajo

### 8. Criterio de adopcion

- kicker: Criterio de adopcion
- titulo con tesis: El sistema minimo debe ayudar mas de lo que estorba
- objeto de prueba visible: matriz por exploracion, trabajo recurrente, trabajo sensible y automatizacion
- takeaway: no todo amerita agente; el criterio es recurrencia, sensibilidad, trazabilidad y costo de error

### 9. Cierre editorial

- kicker: Cierre editorial
- titulo con tesis: La IA no reemplaza el sistema de trabajo. Lo exige.
- objeto de prueba visible: mesa de trabajo con herramientas, bitacora, permisos/llaves, artefactos en revision y una persona tomando la decision final
- takeaway: el valor no esta en soltar al agente, sino en darle un lugar seguro donde trabajar

## Estructura de cierre

Mensaje final aprobado:

> La IA no reemplaza el sistema de trabajo. Lo exige.

Cita validada:

> "Agents are only as effective as the tools we give them." - Anthropic Engineering, "Writing tools for agents", 2025.

Fuente: https://www.anthropic.com/engineering/writing-tools-for-agents

Direccion visual: imagen editorial sobria de una mesa o banco de trabajo analitico; herramientas ordenadas, bitacora abierta, permisos/llaves, artefactos en revision y humano tomando la decision final. La IA aparece como capa de conexion, no como protagonista robotico.

## Riesgos narrativos

- Puede sonar anti-chat si no se reconoce que IA web sirve para exploracion y tareas puntuales.
- Puede sonar burocratica si el sistema minimo se presenta como arbol obligatorio de carpetas.
- Puede volverse compliance si seguridad no se aterriza en controles operativos concretos.
- Puede sonar a hype si se promete autonomia sin scopes, revision y criterio de cierre.
- Puede perder a analistas no programadores si se abre demasiado con jerga de repositorios.

## Listo para build

Decision: listo para build.

Notas para build:

- Construir 9 slides.
- Mantener titulos como conclusiones.
- Usar el caso conductor de analisis de negocio hacia features.
- Tratar cualquier estructura de carpetas como ejemplo adaptable.
- No agregar claims actuales de proveedores, precios, releases, politicas de datos o casos corporativos sin verificarlos en build.
