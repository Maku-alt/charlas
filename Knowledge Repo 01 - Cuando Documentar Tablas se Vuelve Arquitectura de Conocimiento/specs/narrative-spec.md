# Narrative Spec

## Tesis aprobada

Documentar tablas se vuelve arquitectura de conocimiento cuando cada ficha deja de ser una pagina aislada y pasa a formar parte de una memoria operacional con contrato minimo: identidad estable, metadata, ownership, relaciones, vigencia, historial e interfaz de consulta para humanos y agentes.

Formulacion breve:

> Documentar tablas se vuelve arquitectura de conocimiento cuando el equipo necesita conectar, mantener y consultar lo que sabe.

## Audiencia final

Equipo data mixto: Data Scientists, analistas, data engineers, analytics engineers y lideres tecnicos que trabajan con muchas tablas, conocimiento tacito y uso creciente de asistentes o agentes de IA.

## Cambio esperado

La audiencia debe dejar de ver el problema como "crear mas `.md`" y empezar a verlo como una decision de arquitectura de conocimiento por capas: formato portable, navegacion humana, gobierno/metadata, fuente de verdad operacional e interfaz de consulta para agentes.

## Tradeoff central

Archivos sueltos versus memoria comun gobernada:

- Markdown da formato portable y versionable.
- Una wiki mejora discovery y navegacion humana.
- Un knowledge repo disciplina versionado, ownership, metadata, relaciones y revision.
- OKF orienta una convencion portable emergente para bundles Markdown con frontmatter.
- MCP/API expone esa memoria a agentes, pero no la reemplaza.

## Lo que queda fuera

- RAG, embeddings y grafos como tema principal.
- LangGraph u orquestacion avanzada.
- Tutorial de Obsidian.
- Comparativa competitiva entre tools o catalogs.
- Implementacion tecnica detallada.
- Claims cuantitativos de ahorro sin evidencia propia.

RAG y grafos solo aparecen como puente hacia la charla 2.

## Arco narrativo

- cover: el volumen de tablas convierte documentacion en problema de memoria comun
- baseline: Markdown es el ladrillo correcto, no el edificio completo
- tension: la pregunta real cruza tablas, metricas, owners, riesgos y decisiones pasadas
- distincion: wiki, knowledge repo, OKF y MCP/API cumplen roles distintos
- cierre: la documentacion que escala conserva decisiones reutilizables

## Slides propuestas

### Slide 1

- kicker: Tesis
- titulo con tesis: Documentar tablas deja de ser documentacion cuando el equipo necesita memoria comun
- concepto visual: cover editorial donde una ficha `clientes.md` se multiplica y empieza a formar un mapa curado
- objeto visible: una ficha de tabla en primer plano y varias fichas conectadas hacia metricas, owners y decisiones
- takeaway: el problema no es escribir mas; es conectar y mantener lo que el equipo ya sabe

### Slide 2

- kicker: Baseline
- titulo con tesis: Markdown es el primer ladrillo correcto, pero no define el edificio
- concepto visual: ficha Markdown limpia, util y limitada, tratada como pieza inicial de arquitectura
- objeto visible: `clientes.md` con descripcion, columnas principales y usos conocidos
- takeaway: Markdown aporta portabilidad, lectura humana y versionado; todavia no aporta gobierno

### Slide 3

- kicker: Friccion
- titulo con tesis: El dolor real aparece cuando una pregunta cruza tablas, metricas y decisiones pasadas
- concepto visual: la ficha `clientes` como centro de una mesa de investigacion con preguntas pegadas alrededor
- objeto visible: owner, freshness, joins frecuentes, dashboards, metricas, riesgos, consumidores y dudas ya resueltas
- takeaway: la unidad de valor deja de ser la ficha; pasa a ser la red de contexto que permite decidir

### Slide 4

- kicker: Distincion
- titulo con tesis: Una wiki ayuda a encontrar conocimiento; no garantiza que ese conocimiento sea vigente
- concepto visual: comparacion editorial entre grafo de notas navegable y control operacional de vigencia
- objeto visible: panel izquierdo con links/backlinks; panel derecho con owner, status, fecha de revision, fuente canonica y decision registrada
- takeaway: navegar y gobernar son problemas distintos

### Slide 5

- kicker: Contrato
- titulo con tesis: Un knowledge repo empieza cuando cada ficha declara identidad, relaciones y responsabilidad
- concepto visual: ficha partida en frontmatter, cuerpo narrativo y bitacora de cambios
- objeto visible: YAML con `id`, `owner`, `domain`, `status`, `freshness`, `related_metrics`, `consumers`, `last_reviewed`; cuerpo Markdown con decisiones y links
- takeaway: la arquitectura vive en el contrato minimo, no en la herramienta

### Slide 6

- kicker: Evidencia
- titulo con tesis: Los catalogos modernos muestran que el conocimiento de datos ya es relacional
- concepto visual: activo de datos como nodo sobrio conectado a aspectos operativos
- objeto visible: tabla conectada a owner, glossary, lineage, quality, contract, dashboard, consumidores y version history
- takeaway: no se trata de inventar burocracia; se trata de capturar a escala pequena lo que los catalogos modelan a escala grande

### Slide 7

- kicker: Portabilidad
- titulo con tesis: OKF apunta a una idea util: Markdown con estructura explicita para humanos y agentes
- concepto visual: bundle de conocimiento como carpeta ordenada, con `index.md`, ficha Markdown, frontmatter y `log.md`
- objeto visible: ejemplo conceptual de bundle OKF-style con campos `type`, `title`, `description`, `resource`, `tags`, `timestamp` y links
- takeaway: OKF sirve como referencia emergente de convencion portable; no es un estandar corporativo final ni una plataforma completa

### Slide 8

- kicker: Agentes
- titulo con tesis: MCP/API abre la puerta al agente, pero no convierte desorden en memoria
- concepto visual: un agente consulta una puerta estrecha y confiable, no una carpeta infinita de Markdown
- objeto visible: agente -> MCP/API -> indice curado -> ficha versionada -> owner/relaciones/decisiones
- takeaway: un agente no necesita leerlo todo; necesita entradas confiables y contexto ensamblable

### Slide 9

- kicker: Cierre
- titulo con tesis: La documentacion que escala no guarda paginas: conserva decisiones reutilizables
- concepto visual: imagen editorial protagonista de una memoria organizada, humana y consultable
- objeto visible: sala o mesa de archivo moderna con una tarjeta de tabla abierta, caminos sutiles hacia decisiones y una interfaz discreta al fondo
- takeaway: antes de pedirle a un agente que entienda tus datos, dale una memoria que tu equipo pueda mantener

## Cierre

- mensaje final: `Antes de pedirle a un agente que entienda tus datos, dale una memoria que tu propio equipo pueda mantener.`
- mensaje secundario: `Una memoria comun sirve cuando alguien que no estuvo en la decision puede continuar el razonamiento.`
- cita: no usar frase propia como cita; si no hay cita real verificada, mantener mensaje editorial propio
- tono emocional: calma estrategica, disciplina operativa y claridad editorial
- direccion visual sugerida: archivo editorial moderno con fichas de datos curadas y conexiones sutiles hacia decisiones, metricas y owners. Evitar dashboards, grafos tecnicos, robots o wallpaper generico.

## Riesgos narrativos

- Riesgo de sonar anti-Markdown: mitigarlo mostrando Markdown como punto de partida correcto.
- Riesgo de parecer venta de herramienta: mitigarlo organizando la lectura por capas y responsabilidades.
- Riesgo de sobredimensionar OKF: mitigarlo tratandolo como referencia emergente de formato, no como estandar corporativo final.
- Riesgo de contaminarse con RAG/grafos: mitigarlo reservando esos temas para la segunda charla.
- Riesgo de abstraccion: mitigarlo usando `clientes` como ejemplo conductor y preguntas reales del equipo.

## Listo para build

Si.
