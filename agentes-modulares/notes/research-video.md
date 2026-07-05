# Fuente inicial: agentes modulares

## Video

- Fuente: https://www.youtube.com/watch?v=mWvtOHlZM-I
- Titulo original: "Tool, skill, or subagent? Decomposing an agent that outgrew its prompt"
- Canal: Claude
- Duracion: 45:06
- Publicacion: 2026-05-23
- Transcripcion: extraida con MCP `youtube_transcript`, idioma `en-orig`.
- Transcripcion normal para lectura: `notes/transcripcion.md`.
- Respaldo tecnico con timestamps: `notes/transcript-original.en-orig.vtt`.

## Nombre de carpeta

`agentes-modulares`

## Titulo tentativo

**Del prompt gigante al agente modular**

Subtitulo sugerido:

**Tools, skills y subagentes con criterio**

## Tesis de trabajo, no validada

Un agente no falla solo porque el modelo sea insuficiente; muchas veces falla porque su arquitectura acumula contexto, tools y subagentes sin criterio. La mejora viene de separar lo que debe estar siempre en el prompt, lo que debe entrar por skills, lo que debe ejecutarse como tool y lo que merece un subagente con contexto separado.

Esta tesis queda abierta hasta hacer research profundo y contrastarla con nuestras pruebas locales.

## Ideas fuertes de la transcripcion, pendientes de contraste

- El problema inicial es un agente que funcionaba bien, pero crecio por acumulacion de requisitos: prompt de cientos de lineas, muchas tools y varios subagentes.
- La complejidad empezo a generar regresiones: rutas ineficientes, contradicciones en politicas y fallas de comunicacion entre orquestador y subagentes.
- El caso practico usa un agente de inventario llamado `Stock Pilot`: stock bajo, forecast, proveedores, ordenes de compra y reportes semanales.
- La arquitectura inicial tenia un orquestador, un system prompt de unas 400 lineas, 12 tools y 3 subagentes envueltos como tools.
- La charla insiste en que el problema de forecast no era "modelo malo", sino mala informacion alrededor del modelo: contexto largo, contradictorio y dificil de usar.
- El metodo de mejora es correr evals, diagnosticar fallas, cambiar arquitectura y volver a medir. Lo llaman hill climbing sobre evals.
- Skills se presentan como informacion empaquetada y componible que el agente trae al contexto solo cuando la necesita.
- El system prompt debe reservarse para instrucciones siempre necesarias; politicas o procedimientos de uso ocasional deben moverse a skills.
- Tools no deberian proliferar sin criterio. La recomendacion es partir de primitivas humanas: leer/escribir archivos, ejecutar codigo, buscar, mantener tareas.
- Para datos tabulares o documentos, dar ejecucion de codigo puede ser mejor que cargar todo el CSV al contexto.
- MCP no deberia ser el primer reflejo: tiene sentido cuando hay una coleccion comun, estandarizada y gobernada de tools para varios clientes o agentes.
- Subagentes son especialmente utiles para paralelizar trabajo grande o para tener una "mente fresca" separada, por ejemplo revision o forecasting independiente.
- La arquitectura final del ejemplo redujo tools, redujo el prompt a unas 15 lineas, movio logica de negocio a skills y mantuvo solo el subagente que realmente justificaba separacion.
- El resultado reportado fue mejora de evals, menor uso de tokens, menor costo y mejor eficiencia operativa.

## Angulo posible para nuestra charla

La charla puede conectar muy bien con nuestras pruebas actuales si no se presenta como "tutorial de Claude", sino como marco de decision para arquitectura de agentes:

- Cuando el prompt crece, no lo ordenes: descomponlo.
- Cuando una regla no aplica siempre, no va al prompt: va a una skill.
- Cuando el modelo necesita actuar sobre datos, no siempre necesita mas contexto: muchas veces necesita una tool o codigo.
- Cuando la tarea necesita independencia, revision o paralelismo, ahi aparece el subagente.
- Cuando cambias arquitectura sin evals, solo estas opinando; con evals puedes escalar el agente con control.

## Posible promesa ejecutiva, pendiente

Aprender a decidir donde vive cada parte de la inteligencia de un agente para evitar prompts gigantes, tools duplicadas, subagentes innecesarios y regresiones invisibles.

## Puntos abiertos para research posterior

- Validar si el marco `tool / skill / subagent` sigue siendo el vocabulario mas actual y transferible fuera del ecosistema Claude.
- Revisar si alguna recomendacion del video esta desactualizada o demasiado atada a Claude Managed Agents.
- Contrastar la idea "MCP no primero" con practicas actuales: cuando conviene MCP, cuando conviene tool local, cuando conviene CLI o codigo.
- Separar afirmaciones universales de afirmaciones especificas de Anthropic, Claude Code o Claude Managed Agents.
- Verificar claims de performance: reduccion de tokens, costo, latencia y mejora de evals.
- Revisar si `skills` como progressive disclosure tiene analogos claros en otros stacks o si debe explicarse como patron, no como feature de proveedor.
- Decidir si nuestras pruebas locales confirman, matizan o contradicen la tesis del video.
- Identificar un caso propio de nuestras pruebas que sirva como hilo conductor.
- Definir que significa "agente modular" para la charla: arquitectura tecnica, metodologia de trabajo o criterio operativo.
- Explorar si el titulo final debe mantener `Tools, skills y subagentes con criterio` o si conviene una formula menos dependiente de nomenclatura de proveedor.

## No hacer todavia

- No convertir esto en narrativa todavia.
- No construir PPTX todavia.
- No cerrar tesis todavia.
- No asumir que el video es fuente suficiente.
- No investigar nuevas fuentes hasta que terminen las pruebas locales y se habilite la fase de research.
