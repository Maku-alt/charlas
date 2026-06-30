# Maestro Charlas

Indice vivo de las charlas trabajadas en este repo.

## Resumen
| Charla | Estado | Tesis corta | Entregable principal |
|---|---|---|---|
| `Harness Engineer` | Revisada | El valor de los coding agents no vive solo en el modelo, sino en el harness que organiza contexto, tools, memoria y validacion. | `Harness-Engineering-Data-Science.pptx` |
| `Evolucion Stack Clasico DS` | Revisada | El stack clasico de Data Science sigue evolucionando; la decision clave es que adoptar sin romper compatibilidad. | `Evolucion-Stack-Clasico-DS.pptx` |
| `El Eterno Retorno` | Revisada | No vuelve simplemente el on-premise; aparece una arquitectura hibrida para workloads LLM segun costo, control y elasticidad. | `El-Eterno-Retorno.pptx` |
| `Wiki LLM con Obsidian` | Pendiente de revision final | Una wiki LLM util no es RAG con otra interfaz, sino conocimiento compilado, enlazado y mantenible por agentes. | `Wiki-LLM-con-Obsidian.pptx` |
| `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento` | En diseno | Documentar muchas tablas deja de ser una tarea de escritura y se vuelve arquitectura de conocimiento para humanos y agentes. | Pendiente |
| `Knowledge Repo 02 - Buscar No Es Entender` | Pendiente | Buscar texto, recuperar contexto y entender relaciones son capacidades distintas sobre una memoria de datos. | Pendiente |
| `SDD-IAgentica` | Revisada | SDD vuelve practica la IA agentica porque convierte conversaciones largas en contratos de trabajo pequenos y verificables. | `SDD-IAgentica-v2.pptx` |
| `IA Agentica de Conversacion a Sistema` | Revisada | Pasar de IA web a IA agentica no es cambiar de interfaz, sino mover la IA dentro de una estructura propia, gobernada y segura. | `IA-Agentica-De-Conversacion-A-Sistema.pptx` |

## Harness Engineer
**Carpeta:** `Harness Engineer/`

**Audiencia:** Data scientists y analistas tecnicos que trabajan en repositorios con SQL, Python, modelado, revisiones y tareas asistidas por agentes.

**Tesis:** El valor de los coding agents para workflows de datos no depende solo de tener un modelo mejor. Depende de construir un sistema reproducible donde el contexto, la orquestacion y la verificacion funcionen como parte del entorno de trabajo.

**Pregunta central:** Como pasamos de usar un agente como chatbot a operar un sistema confiable de trabajo con contexto, herramientas, memoria y verificacion.

**Estado:** Revisada.

**Material versionado principal:**
- `Harness-Engineering-Data-Science.pptx`
- `README.md`
- `notes/`

## Evolucion Stack Clasico DS
**Carpeta:** `Evolucion Stack Clasico DS/`

**Audiencia:** Data scientists y equipos tecnicos que trabajan con datos, features, modelado, optimizacion y explicabilidad en Python.

**Tesis:** Las librerias clasicas de Data Science no se han quedado quietas. La charla separa mejoras adoptables en entornos actuales, cambios que exigen migracion y ruido que no merece prioridad.

**Pregunta central:** Que mejoras del stack clasico podemos adoptar hoy sin romper compatibilidad, y que queda bloqueado hasta migrar de version de Python.

**Estado:** Revisada.

**Material versionado principal:**
- `Evolucion-Stack-Clasico-DS.pptx`
- `README.md`
- `notes/`

## El Eterno Retorno
**Carpeta:** `El Eterno Retorno/`

**Audiencia:** Lideres tecnicos, equipos de Data Science, ML Platform, IA aplicada y arquitectura.

**Tesis:** No estamos viendo un simple regreso al pasado. Estamos viendo una nueva disciplina de arquitectura para IA: nube para experimentacion, frontier models y demanda elastica; infraestructura propia o privada para workloads repetitivos, sensibles o economicamente intensivos.

**Pregunta central:** Si el gasto en LLMs de terceros sube o se vuelve dificil de controlar, cuando tiene sentido operar parte de la inferencia en infraestructura propia, privada o hibrida.

**Estado:** Revisada.

**Material versionado principal:**
- `El-Eterno-Retorno.pptx`
- `README.md`
- `notes/`

## Wiki LLM con Obsidian
**Carpeta:** `Wiki LLM con Obsidian/`

**Audiencia:** Data Scientists y equipos tecnicos que trabajan con research, repositorios, decisiones de arquitectura, notas operativas y agentes.

**Tesis:** Para trabajo de conocimiento y repositorios tecnicos pequenos o medianos, el mayor salto no viene de recuperar chunks cada vez mejor. Viene de convertir fuentes crudas en una wiki viva de markdown, con esquema, enlaces, proveniencia y rutinas de mantenimiento que un agente pueda operar incrementalmente.

**Pregunta central:** Puede Obsidian convertirse en frontend de una memoria operativa util para agentes o equipos sin caer en una pila compleja de RAG, vectores y middleware.

**Estado:** Pendiente de revision final. La tesis, el caso practico, la demo en Obsidian y el PPTX ya estan construidos.

**Material versionado principal:**
- `Wiki-LLM-con-Obsidian.pptx`
- `README.md`
- `notes/`
- `review/`
- `demo-charlas/`

## Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento
**Carpeta:** `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/`

**Linea tematica:** `Knowledge Repo`.

**Audiencia:** Equipo data mixto: Data Scientists, analistas, data engineers, analytics engineers y lideres tecnicos que trabajan con muchas tablas, conocimiento tacito y uso creciente de asistentes o agentes de IA.

**Tesis:** Cuando un equipo documenta muchas tablas, no necesita solo mas documentacion. Necesita convertir ese conocimiento operativo en una memoria comun, navegable, versionada y preparada para consulta por agentes.

**Pregunta central:** Como pasamos de fichas sueltas de tablas a una memoria operacional que sirva para el equipo y pueda ser consultada por agentes sin convertir el repo en un basural de Markdown.

**Estado:** En diseno. Tiene tesis y narrativa inicial; falta research antes de build.

**Material versionable esperado:**
- `README.md`
- `specs/`
- `notes/`

**Material pendiente:**
- research validado
- build-spec
- deck editable
- review final

## Knowledge Repo 02 - Buscar No Es Entender
**Carpeta:** `Knowledge Repo 02 - Buscar No Es Entender/`

**Linea tematica:** `Knowledge Repo`.

**Audiencia tentativa:** Equipo data mixto que ya entiende la necesidad de una memoria operacional y quiere discutir como consultarla con busqueda, RAG, grafos y agentes.

**Tesis tentativa:** RAG ayuda a encontrar contexto; los grafos ayudan a representar relaciones; los agentes necesitan saber cuando buscar, cuando recuperar evidencia y cuando seguir dependencias explicitas.

**Pregunta central tentativa:** Como distinguir busqueda, RAG, grafos y orquestacion de agentes sin vender ninguna capa como solucion total.

**Estado:** Pendiente. Queda registrada como segunda charla de la serie; no tiene narrativa completa todavia.

**Material versionable esperado:**
- `README.md`

## SDD-IAgentica
**Carpeta:** `SDD-IAgentica/`

**Audiencia:** Data Scientists, analytics engineers, ML engineers y lideres tecnicos que ya usan asistentes de IA para investigacion, codigo, analisis o documentacion.

**Tesis:** SDD vuelve practica la IA agentica porque convierte conversaciones largas en contratos de trabajo pequenos: cada subagente recibe solo el spec, los artefactos necesarios y un output esperado; el chat principal conserva decisiones, no todo el historial.

**Pregunta central:** Como pasar de conversaciones largas y fragiles a flujos con specs, handoffs, artefactos, review y decision de continuidad.

**Estado:** Revisada. La version final aprobada es `SDD-IAgentica-v2.pptx`, alineada con `STYLE-CHARLAS.md`.

**Material versionable esperado:**
- `SDD-IAgentica-v2.pptx`
- `README.md`
- `specs/`
- `notes/`
- `review/`

**Material local no remoto por defecto:**
- `slides/`
- `assets/`

## IA Agentica de Conversacion a Sistema
**Carpeta:** `IA Agentica de Conversacion a Sistema/`

**Audiencia:** Analistas y Data Scientists que ya usan IA web o trabajan con repos, pero todavia necesitan una lectura comun sobre IA agentica como sistema de trabajo.

**Tesis:** Pasar de IA en la web a IA agentica no es solo cambiar de interfaz. Es mover la IA dentro de una estructura de trabajo donde existen reglas, contexto, estado, permisos, outputs verificables y revision humana.

**Pregunta central:** Como pasamos de conversaciones utiles pero aisladas a una forma de trabajo con IA agentica que sea trazable, adaptable y segura para el equipo.

**Estado:** Revisada. La version final aprobada tiene 10 slides tras el cambio solicitado y queda registrada en `review/review-formal-feedback-pass.md`.

**Material versionable esperado:**
- `IA-Agentica-De-Conversacion-A-Sistema.pptx`
- `README.md`
- `specs/`
- `notes/`
- `review/`

**Material local no remoto por defecto:**
- `slides/`
- `assets/`

## Reglas de lectura
- Este archivo es inventario editorial, no reemplaza `AGENTS.md`.
- Para flujo operativo, agentes y SDD, usar `AGENTS.md`, `agents/README.md` y `templates/charlas-sdd/`.
- Los estados se actualizan cuando cambia el artefacto real, no solo cuando aparece una idea nueva.
