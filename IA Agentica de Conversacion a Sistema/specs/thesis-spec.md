# Thesis Spec

## Tema

IA agentica como transicion desde conversaciones aisladas en IA web hacia una estructura propia de trabajo para analisis y Data Science.

## Audiencia

Audiencia mixta:

- Analistas que ya usan IA web para acelerar analisis, redaccion, exploracion o consultas puntuales.
- Data Scientists que trabajan con repositorios, notebooks, scripts, datos, preparacion de features y modelamiento.

## Problema

Muchas personas ya usan IA, pero la usan como conversacion aislada. Eso ayuda en tareas puntuales, pero deja fuera del sistema de trabajo elementos criticos:

- contexto operativo;
- reglas del equipo;
- estado visible;
- trazabilidad de decisiones;
- limites de seguridad;
- outputs revisables;
- criterios de cierre.

Cuando el trabajo involucra analisis, datos o preparacion de features, esa falta de estructura aumenta el riesgo de perdida de contexto, lectura indebida de informacion sensible, outputs dificiles de auditar y dependencia excesiva de la memoria informal del usuario.

## Tesis central

Pasar de IA en la web a IA agentica no es solo cambiar de interfaz. Es mover la IA dentro de una estructura de trabajo donde existen reglas, contexto, estado, permisos, outputs verificables y revision humana.

Formulacion breve:

> El salto no es usar mas IA, sino pasar de usar IA como conversacion aislada a integrarla en una estructura propia de trabajo, gobernada y segura.

## Cambio esperado

La audiencia debe salir con un cambio mental:

- Antes: "uso IA cuando necesito ayuda".
- Despues: "diseno un sistema minimo para que la IA pueda trabajar conmigo de forma segura, trazable y revisable".

Tambien debe entender que el objetivo no es imponer una unica estructura de carpetas, sino acordar responsabilidades minimas que cada persona pueda adaptar a su forma de trabajo.

## Fuera de alcance

- Comparar proveedores o herramientas especificas como tema central.
- Vender una plataforma corporativa de agentes.
- Definir un estandar final obligatorio para todo el equipo.
- Hacer una demo tecnica en vivo.
- Profundizar en arquitectura avanzada de MCP, RAG, orquestadores o evaluaciones automatizadas.
- Tratar seguridad como compliance abstracto; el foco es seguridad operativa en el flujo de trabajo.

## Tradeoff central

Conversacion aislada versus sistema de trabajo:

- IA web: rapida, flexible y util para exploracion, pero con contexto fragil y trazabilidad limitada.
- IA agentica en una estructura propia: requiere minimo orden operativo, pero permite reglas, estado, permisos, outputs verificables y revision.

La charla no plantea que la IA web sea mala. Plantea que, para trabajo analitico recurrente o sensible, el siguiente nivel requiere sistema.

## Riesgos de framing

- Que suene a "herramientas web malas, agentes buenos". Mitigacion: presentar IA web como punto de partida valido para exploracion.
- Que parezca una charla de estructura de carpetas. Mitigacion: insistir en responsabilidades obligatorias antes que carpetas obligatorias.
- Que parezca una charla de seguridad restrictiva. Mitigacion: mostrar seguridad como condicion para escalar uso, no como freno.
- Que el ejemplo de `cases/<caso>/state.md` parezca estandar obligatorio. Mitigacion: presentarlo como una implementacion posible y adaptable.

## Decision de continuidad

- seguir

