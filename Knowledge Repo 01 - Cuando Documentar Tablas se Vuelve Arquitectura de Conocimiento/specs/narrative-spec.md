# Narrative Spec

## Tesis aprobada

Documentar tablas se vuelve arquitectura de conocimiento cuando cada ficha deja de ser una pagina aislada y pasa a formar parte de una memoria operacional con contrato minimo: identidad estable, metadata, ownership, relaciones, vigencia, historial y una interfaz de consulta para humanos y agentes.

## Audiencia final

Equipo data mixto: Data Scientists, analistas, data engineers, analytics engineers y lideres tecnicos que trabajan con muchas tablas, conocimiento tacito y uso creciente de asistentes o agentes de IA.

## Cambio esperado

La audiencia debe dejar de ver el problema como "crear mas `.md`" y empezar a verlo como una decision de arquitectura de conocimiento por capas: formato portable, navegacion humana, gobierno/metadata, fuente de verdad operacional e interfaz de consulta para agentes.

## Tradeoff central

Archivos sueltos versus memoria comun gobernada:

- Markdown da formato portable y versionable;
- una wiki mejora discovery y navegacion humana;
- un knowledge repo disciplina versionado, ownership, metadata, relaciones y revision;
- MCP/API expone esa memoria a agentes, pero no la reemplaza.

## Lo que queda fuera

- RAG, embeddings y grafos como tema principal.
- LangGraph u orquestacion avanzada.
- Tutorial de Obsidian.
- Comparativa competitiva entre tools o catalogs.
- Implementacion tecnica detallada.
- Claims cuantitativos de ahorro sin evidencia propia.

## Arco narrativo

- cover: el volumen de tablas convierte documentacion en problema de memoria comun
- baseline: Markdown resuelve el primer paso, no el sistema
- tension: la pregunta real cruza tablas, metricas, owners, riesgos y decisiones pasadas
- lectura ejecutiva: formato, wiki, knowledge repo y MCP/API cumplen roles distintos
- cierre: la documentacion que escala conserva decisiones reutilizables

## Slides propuestas

### Slide 1

- kicker: Tesis
- titulo con tesis: Documentar tablas deja de ser documentacion cuando el equipo necesita memoria comun
- objeto de prueba visible: una ficha de tabla que se multiplica hasta convertirse en un mapa de conocimiento
- takeaway: el problema no es escribir mas; es conectar y mantener lo que el equipo ya sabe

### Slide 2

- kicker: Baseline
- titulo con tesis: Una ficha Markdown por tabla resuelve el primer 20%, no el sistema
- objeto de prueba visible: `clientes.md` simple con descripcion, columnas y usos
- takeaway: Markdown es buen formato base porque es portable y versionable

### Slide 3

- kicker: Friccion
- titulo con tesis: El dolor aparece cuando la pregunta cruza tablas, metricas y decisiones pasadas
- objeto de prueba visible: preguntas reales alrededor de la ficha `clientes`: owner, vigencia, joins, riesgos, dashboards y dudas resueltas
- takeaway: la unidad de valor ya no es la ficha; es la red de conocimiento

### Slide 4

- kicker: Distincion
- titulo con tesis: Wiki no es lo mismo que memoria operacional
- objeto de prueba visible: dos paneles, grafo humano versus checklist operacional
- takeaway: navegar conocimiento y gobernarlo son problemas distintos

### Slide 5

- kicker: Contrato
- titulo con tesis: Un knowledge repo empieza cuando cada ficha declara identidad, relaciones y responsabilidad
- objeto de prueba visible: YAML frontmatter + cuerpo Markdown + links a metricas, dominios y owners
- takeaway: la arquitectura vive en el contrato minimo, no en la herramienta

### Slide 6

- kicker: Ecosistema
- titulo con tesis: Los catalogs modernos confirman que la metadata util es relacional
- objeto de prueba visible: una tabla conectada a owner, glossary, lineage, quality, contract, dashboard y consumidores
- takeaway: no estamos inventando burocracia; estamos bajando capacidades de catalogo a una escala operable

### Slide 7

- kicker: Agentes
- titulo con tesis: Un agente no necesita leerlo todo: necesita una entrada confiable y contexto ensamblable
- objeto de prueba visible: agente -> MCP/API -> knowledge repo -> fichas, versionado y owners
- takeaway: preparar memoria reduce improvisacion y contexto irrelevante

### Slide 8

- kicker: Tradeoff
- titulo con tesis: La decision no es Markdown versus catalogo: es que capa cumple cada rol
- objeto de prueba visible: matriz formato / navegacion / gobierno / interfaz / operacion con `Markdown`, `Wiki`, `Knowledge repo`, `OKF`, `MCP/API`
- takeaway: separar capas evita comprar herramienta o sobrediseniar antes de tiempo

### Slide 9

- kicker: Cierre
- titulo con tesis: La documentacion que escala no guarda paginas: conserva decisiones reutilizables
- objeto de prueba visible: archivo editorial vivo con caminos iluminados entre tablas, metricas, owners y decisiones
- takeaway: una memoria comun vale cuando permite que otro continue el razonamiento

## Cierre

- mensaje final: `La documentacion escala cuando deja de describir tablas y empieza a conservar decisiones.`
- cita: `Una memoria comun no es donde guardamos lo que sabemos; es donde otro puede continuar el razonamiento.`
- autor: frase editorial propia
- tono emocional: calma estrategica, disciplina operativa y claridad editorial
- direccion visual sugerida: archivo editorial de tarjetas de datos sobre una mesa clara, con trazos luminosos sutiles conectando tablas, metricas, owners y decisiones. Evitar dashboards, grafos tecnicos, robots o wallpaper generico.

## Riesgos narrativos

- Riesgo de sonar anti-Markdown: mitigarlo mostrando Markdown como punto de partida correcto.
- Riesgo de parecer venta de herramienta: mitigarlo organizando la lectura por capas y responsabilidades.
- Riesgo de sobredimensionar OKF: mitigarlo tratandolo como referencia emergente de formato, no como estandar corporativo final.
- Riesgo de contaminarse con RAG/grafos: mitigarlo reservando esos temas para la segunda charla.
- Riesgo de abstraccion: mitigarlo usando `clientes` como ejemplo conductor y preguntas reales del equipo.

## Listo para build

- si
