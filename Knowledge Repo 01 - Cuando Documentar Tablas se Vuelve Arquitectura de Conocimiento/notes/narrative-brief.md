# Narrative Brief

## Tesis propuesta

Documentar tablas se vuelve arquitectura de conocimiento cuando el equipo deja de producir paginas descriptivas y empieza a operar una memoria comun: una base mantenible de decisiones, relaciones, vigencia y ownership que humanos y agentes pueden consultar sin improvisar contexto.

La lectura editorial cambia el centro de la charla: no es una escalera de herramientas (`Markdown -> wiki -> repo -> MCP`), sino el paso de un inventario de fichas a un sistema operativo de conocimiento. Las capas importan, pero entran como responsabilidades dentro de un loop: capturar, conectar, validar, mantener y consultar.

## Lectura narrativa

La charla debe sentirse como una decision de arquitectura liviana para equipos de datos que ya tienen demasiadas tablas, demasiadas respuestas tacitas y demasiadas preguntas repetidas. El problema no empieza con la herramienta; empieza cuando una pregunta real ya no cabe en una ficha.

El arco nuevo parte de la presion operacional: una persona o agente pregunta algo concreto sobre una tabla y descubre que la respuesta vive repartida entre columnas, dashboards, owners, freshness, decisiones pasadas y riesgos conocidos. Desde ahi, la charla construye el contrato minimo de una memoria mantenible y solo despues ubica Markdown, wiki, catalogos, OKF y MCP como piezas de acceso o soporte.

## Audiencia y cambio esperado

Audiencia: Data Scientists, analistas, data engineers, analytics engineers y lideres tecnicos que trabajan con muchas tablas, conocimiento tacito y uso creciente de asistentes o agentes.

Cambio esperado: dejar de preguntar "donde escribimos la documentacion?" y empezar a preguntar "que memoria operacional necesita el equipo para que otra persona, o un agente, continue el razonamiento con contexto confiable?".

## Comparacion o tension central

Tension central: inventario de paginas versus memoria operable.

- Inventario de paginas: describe objetos, depende de heroes locales, envejece en silencio y obliga a reconstruir contexto en cada pregunta.
- Memoria operable: declara identidad, ownership, vigencia, relaciones, evidencia, historial y rutas de consulta.

La pregunta de decision no es "Markdown o catalogo?" sino "que parte del razonamiento queremos poder reutilizar sin volver a entrevistar al equipo?".

## Lo que queda fuera

- RAG, embeddings y grafos como tema principal.
- Tutorial de Obsidian, GitHub Wiki, dbt, catalogos, OKF o MCP.
- Comparativa competitiva entre herramientas.
- Implementacion tecnica detallada de un servidor MCP.
- Claims cuantitativos de ahorro de tokens, tiempo o costo sin evidencia propia.
- Presentar OKF como estandar ampliamente adoptado; solo puede aparecer como patron emergente o referencia portable.

## Narrativa propuesta de la charla

### Slide 1

- kicker: Punto de quiebre
- titulo con tesis: Una tabla deja de estar documentada cuando nadie puede reconstruir su contexto
- concepto visual: una ficha de tabla en primer plano, rodeada por sombras de preguntas no resueltas; la imagen debe comunicar que el problema no es ausencia de texto sino perdida de contexto.
- objeto de prueba visible: pregunta conductora: `puedo usar clientes para entrenar este modelo y explicar el KPI del dashboard?`
- takeaway: el volumen de tablas convierte la documentacion en un problema de memoria comun.
- notas de soporte: abrir con una situacion reconocible, no con definiciones. La pregunta debe cruzar uso, metrica, owner, freshness, riesgo y decision pasada.

### Slide 2

- kicker: Falso avance
- titulo con tesis: Escribir mas fichas no arregla una memoria que no tiene contrato
- concepto visual: una mesa editorial con fichas Markdown prolijas pero desalineadas; algunas tienen huecos visibles en owner, vigencia o relaciones.
- objeto de prueba visible: tres fichas `.md` con campos inconsistentes: una tiene owner, otra freshness, otra decision historica.
- takeaway: Markdown hace el conocimiento revisable; el contrato lo vuelve mantenible.
- notas de soporte: cuidar que no suene anti-Markdown. Markdown sigue siendo el formato base correcto por legibilidad, portabilidad y Git.

### Slide 3

- kicker: Pregunta real
- titulo con tesis: La unidad de valor no es la ficha, es el camino que permite responder
- concepto visual: una ruta iluminada que parte de `clientes` y toca metrica, dashboard, owner, lineage, freshness, riesgo y decision.
- objeto de prueba visible: mapa de una consulta: `tabla -> columnas criticas -> joins validos -> KPI -> dashboard -> owner -> dudas resueltas`.
- takeaway: documentar datos es conservar rutas de razonamiento, no solo describir objetos.
- notas de soporte: esta slide reemplaza la vieja "friccion" por una escena de investigacion operativa. El foco es el camino reutilizable.

### Slide 4

- kicker: Contrato minimo
- titulo con tesis: Un knowledge repo empieza cuando cada tabla declara que promete mantener
- concepto visual: una ficha como contrato firmado, no como pagina; frontmatter arriba, cuerpo narrativo al centro, relaciones y revision al pie.
- objeto de prueba visible: plantilla minima con `id`, `owner`, `dominio`, `estado`, `freshness`, `relaciones`, `decisiones`, `riesgos`, `revision`.
- takeaway: la arquitectura vive en convenciones observables, no en el nombre de la herramienta.
- notas de soporte: conectar con research: ownership, vigencia, relaciones, historial y criterios de revision son los criterios que separan memoria de notas.

### Slide 5

- kicker: Loop operativo
- titulo con tesis: La memoria comun escala cuando tiene ciclo de vida, no cuando tiene mas enlaces
- concepto visual: ciclo sobrio de cinco estaciones: capturar, conectar, validar, revisar, retirar; cada estacion deja una marca sobre la ficha.
- objeto de prueba visible: loop de mantenimiento con estados: `draft`, `vigente`, `requiere revision`, `deprecated`.
- takeaway: wiki y backlinks ayudan a navegar; el knowledge repo tambien debe decidir que sigue vigente.
- notas de soporte: esta es la distincion wiki/repo sin repetir una comparacion frontal de paneles. La clave es que navegacion no equivale a gobierno.

### Slide 6

- kicker: Senal externa
- titulo con tesis: Los stacks de datos ya muestran que la metadata importante es operacional
- concepto visual: una misma tabla conectada a senales de sistema: lineage, tests, freshness, owner, consumidores, contrato y dashboards.
- objeto de prueba visible: inventario de capacidades observables en catalogos/dbt/data platforms: owners, lineage, freshness, tests, glossary, consumidores.
- takeaway: el knowledge repo no inventa burocracia; traduce una necesidad real a una escala portable.
- notas de soporte: no vender reemplazo de catalogo. Presentarlo como contrato complementario o capa liviana cuando el catalogo no captura conocimiento narrativo.

### Slide 7

- kicker: Agentes
- titulo con tesis: Un agente no necesita mas documentos; necesita una memoria que se pueda consultar con precision
- concepto visual: un agente frente a una ventanilla de consulta, no navegando una pila infinita; la ventanilla ofrece `search`, `read` y `neighbors`.
- objeto de prueba visible: flujo `pregunta -> search -> read -> neighbors -> evidencia citada -> owner si hay duda`.
- takeaway: MCP/API es una puerta de acceso; la confiabilidad viene del contrato del repo.
- notas de soporte: evitar prometer trazabilidad automatica. La interfaz expone recursos y herramientas, pero no arregla conocimiento mal mantenido.

### Slide 8

- kicker: Decision de arquitectura
- titulo con tesis: Separar responsabilidades evita convertir una herramienta en estrategia
- concepto visual: tablero de decision con cinco responsabilidades, no matriz de productos: formato, navegacion, gobierno, portabilidad, acceso.
- objeto de prueba visible: decision map: `Markdown = formato`, `wiki = exploracion`, `knowledge repo = gobierno`, `OKF = paquete portable`, `MCP/API = acceso`.
- takeaway: la decision correcta es asignar roles; no declarar un ganador universal.
- notas de soporte: OKF entra con cautela como patron emergente para bundles Markdown tipados, no como estandar corporativo probado.

### Slide 9

- kicker: Cierre editorial
- titulo con tesis: Antes de pedirle memoria a un agente, hay que construir una memoria que el equipo pueda mantener
- concepto visual: biblioteca tecnica en construccion: estantes etiquetados, fichas con marcas de revision, pasillos conectados y una puerta de consulta; una sola escena editorial, sin dashboards ni robots protagonistas.
- objeto de prueba visible: frase final sobre banda oscura + cita breve de John Gruber como contraste sobre legibilidad de Markdown.
- takeaway: delegar razonamiento exige primero conservar decisiones reutilizables.
- notas de soporte: usar la cita real de Markdown como contraste, no como autoridad sobre knowledge repos. Cierre emocional: disciplina operativa, calma estrategica y claridad.

## Estructura de cierre

- mensaje final: `Antes de pedirle memoria a un agente, hay que construir una memoria que el equipo pueda mantener.`
- cita real sugerida: John Gruber sobre Markdown: el objetivo de diseno es que la sintaxis sea "as readable as possible".
- uso editorial de la cita: Markdown nacio para legibilidad; esta charla dice que la legibilidad es necesaria pero no suficiente cuando el equipo necesita memoria operacional.
- metafora visual dominante: biblioteca tecnica en construccion, con estantes, etiquetas, fichas de mantenimiento y una puerta de consulta.
- rol protagonista de la imagen: la escena final debe amplificar la tesis; no debe ser diagrama, tabla, dashboard, robot ni collage de iconos.

## Riesgos narrativos

- Riesgo: parecer que se descarta Markdown. Mitigacion: decir explicitamente que Markdown es el formato base correcto, pero no el contrato completo.
- Riesgo: sonar como venta de knowledge repo como herramienta nueva. Mitigacion: definirlo por responsabilidades y criterios observables.
- Riesgo: duplicar funciones de catalogo de datos. Mitigacion: ubicar catalogos como evidencia de metadata operacional y al repo como contrato complementario o liviano.
- Riesgo: sobredimensionar OKF. Mitigacion: tratarlo como patron emergente y referencia portable, no como estandar adoptado.
- Riesgo: prometer agentes autonomos. Mitigacion: MCP/API aparece como interfaz de consulta, dependiente de la calidad del repo.
- Riesgo: abstraccion excesiva. Mitigacion: sostener la charla con la pregunta conductora sobre `clientes` y un camino de respuesta visible.

## Entrada para agent-log

Ver entrada agregada en `notes/agent-log.md`.

## Listo para build

Decision: `listo para build`.

Condicion para build: preservar el arco nuevo de "inventario de paginas -> memoria operable -> puerta de consulta". No reconstruir la secuencia como una simple lista de capas ni convertir la slide 8 en una tabla plana sin idea visual.
