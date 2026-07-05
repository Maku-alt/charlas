# Narrative Brief

Run id: `knowledge-repo-01-full-rebuild-20260704`

## Tesis propuesta

Documentar tablas se vuelve arquitectura de conocimiento cuando el equipo necesita conectar, mantener y consultar lo que sabe.

La formulacion operativa para build es:

> Una ficha de tabla deja de ser documentacion aislada cuando declara identidad, ownership, relaciones, vigencia, historial e interfaz de consulta.

## Lectura narrativa

La charla no debe vender una herramienta ni atacar Markdown. Debe mostrar una evolucion: Markdown es el ladrillo correcto; la wiki ayuda a navegar; el knowledge repo introduce contrato operativo; OKF sirve como referencia emergente de portabilidad; MCP/API expone la memoria a agentes, pero no la reemplaza.

El hilo conductor es `clientes`: empieza como una ficha simple y termina como una pieza de memoria operacional conectada a metricas, owners, riesgos, decisiones, consumidores y acceso para agentes.

## Audiencia y cambio esperado

Audiencia: Data Scientists, analistas, data engineers, analytics engineers y lideres tecnicos que trabajan con muchas tablas y conocimiento tacito.

Cambio esperado:

- Antes: "hagamos un `.md` por tabla".
- Despues: "definamos que capa cumple cada rol: formato, navegacion, gobierno, memoria operacional e interfaz para agentes".

La decision que debe quedar instalada es empezar por contrato minimo y ownership, no por herramienta ni por RAG.

## Comparacion o tension central

La tension central es `archivo suelto` versus `memoria operacional gobernada`.

| Capa | Sirve para | Riesgo si se confunde |
|---|---|---|
| Markdown | formato portable y versionable | creer que formato equivale a memoria |
| Wiki | discovery humano y navegacion | tener enlaces sin autoridad ni vigencia |
| Knowledge repo | contrato, ownership, relaciones, historial | sobregobernar antes de encontrar valor |
| OKF | referencia emergente de bundle Markdown + frontmatter | tratar un draft como estandar corporativo final |
| MCP/API | interfaz de consulta para agentes | exponer desorden mas rapido |

## Lo que queda fuera

- RAG, embeddings y grafos como tema principal.
- LangGraph u orquestacion avanzada.
- Tutorial de Obsidian.
- Comparativa competitiva entre herramientas.
- Implementacion tecnica detallada.
- Promesas cuantitativas de ahorro, costo, tokens o tiempo.
- Claims de adopcion amplia de OKF.

RAG/grafos aparecen solo como puente hacia la charla 2: primero memoria ordenada, despues busqueda y razonamiento.

## Narrativa propuesta de la charla

### Slide 1

- kicker: Tesis
- titulo con tesis: Documentar tablas deja de ser documentacion cuando el equipo necesita memoria comun
- concepto visual: cover editorial donde una ficha `clientes.md` se multiplica y empieza a formar un mapa curado, no un caos de archivos
- objeto de prueba visible: una ficha de tabla en primer plano y varias fichas conectadas por trazos discretos hacia metricas, owners y decisiones
- takeaway: el problema no es escribir mas; es conectar y mantener lo que el equipo ya sabe
- notas de soporte: abrir con el cambio de escala: pocas tablas toleran notas sueltas; muchas tablas exigen memoria compartida.

### Slide 2

- kicker: Baseline
- titulo con tesis: Markdown es el primer ladrillo correcto, pero no define el edificio
- concepto visual: una ficha Markdown limpia, util y limitada, como pieza inicial de arquitectura
- objeto de prueba visible: `clientes.md` con descripcion, columnas principales y usos conocidos
- takeaway: Markdown aporta portabilidad, lectura humana y versionado; todavia no aporta gobierno
- notas de soporte: cuidar el framing: Markdown no es el problema. El problema es pedirle que resuelva identidad, vigencia, ownership y relaciones sin contrato adicional.

### Slide 3

- kicker: Friccion
- titulo con tesis: El dolor real aparece cuando una pregunta cruza tablas, metricas y decisiones pasadas
- concepto visual: la ficha `clientes` como centro de una mesa de investigacion con preguntas pegadas alrededor
- objeto de prueba visible: owner, freshness, joins frecuentes, dashboards, metricas, riesgos, consumidores y dudas ya resueltas
- takeaway: la unidad de valor deja de ser la ficha; pasa a ser la red de contexto que permite decidir
- notas de soporte: usar preguntas concretas: "puedo joinear esto con ventas?", "quien valida churn?", "esta columna sigue vigente?", "que dashboard depende de esto?".

### Slide 4

- kicker: Distincion
- titulo con tesis: Una wiki ayuda a encontrar conocimiento; no garantiza que ese conocimiento sea vigente
- concepto visual: comparacion editorial entre un grafo de notas navegable y un control operacional de vigencia
- objeto de prueba visible: panel izquierdo con links/backlinks; panel derecho con owner, status, fecha de revision, fuente canonica y decision registrada
- takeaway: navegar y gobernar son problemas distintos
- notas de soporte: no desacreditar wikis. Funcionan para discovery humano; el salto a memoria operacional requiere autoridad, mantenimiento y criterios de inclusion.

### Slide 5

- kicker: Contrato
- titulo con tesis: Un knowledge repo empieza cuando cada ficha declara identidad, relaciones y responsabilidad
- concepto visual: una ficha partida en tres capas editables: frontmatter, cuerpo narrativo y bitacora de cambios
- objeto de prueba visible: YAML con `id`, `owner`, `domain`, `status`, `freshness`, `related_metrics`, `consumers`, `last_reviewed`; cuerpo Markdown con decisiones y links
- takeaway: la arquitectura vive en el contrato minimo, no en la herramienta
- notas de soporte: enfatizar progresividad: pocos campos obligatorios, crecimiento por valor y revision via Git/PR cuando aplique.

### Slide 6

- kicker: Evidencia
- titulo con tesis: Los catalogos modernos muestran que el conocimiento de datos ya es relacional
- concepto visual: activo de datos como nodo sobrio conectado a aspectos operativos, no como diagrama tecnico saturado
- objeto de prueba visible: tabla conectada a owner, glossary, lineage, quality, contract, dashboard, consumidores y version history
- takeaway: no se trata de inventar burocracia; se trata de capturar a escala pequena lo que los catalogos modelan a escala grande
- notas de soporte: presentar DataHub, OpenMetadata y dbt exposures como evidencia conceptual, no como recomendacion de compra ni reemplazo del repo.

### Slide 7

- kicker: Portabilidad
- titulo con tesis: OKF apunta a una idea util: Markdown con estructura explicita para humanos y agentes
- concepto visual: bundle de conocimiento como carpeta ordenada, con `index.md`, ficha Markdown, frontmatter y `log.md`
- objeto de prueba visible: ejemplo conceptual de bundle OKF-style con campos `type`, `title`, `description`, `resource`, `tags`, `timestamp` y links
- takeaway: OKF sirve como referencia emergente de convencion portable; no es un estandar corporativo final ni una plataforma completa
- notas de soporte: usar fecha si se menciona en build: Google Cloud lo introdujo el 12 de junio de 2026; spec v0.1 draft. Incluir non-goals: no prescribe storage, serving ni query.

### Slide 8

- kicker: Agentes
- titulo con tesis: MCP/API abre la puerta al agente, pero no convierte desorden en memoria
- concepto visual: un agente consulta una puerta estrecha y confiable, no una carpeta infinita de Markdown
- objeto de prueba visible: agente -> MCP/API -> indice curado -> ficha versionada -> owner/relaciones/decisiones
- takeaway: un agente no necesita leerlo todo; necesita entradas confiables y contexto ensamblable
- notas de soporte: MCP se explica como interfaz para resources, prompts y tools. No decir que almacena memoria ni que resuelve calidad del contenido.

### Slide 9

- kicker: Cierre
- titulo con tesis: La documentacion que escala no guarda paginas: conserva decisiones reutilizables
- concepto visual: imagen editorial protagonista de una memoria organizada, humana y consultable; debe sentirse como archivo curado, no dashboard
- objeto de prueba visible: sala o mesa de archivo moderna con una tarjeta de tabla abierta, caminos sutiles hacia decisiones y una interfaz discreta al fondo
- takeaway: antes de pedirle a un agente que entienda tus datos, dale una memoria que tu equipo pueda mantener
- notas de soporte: cerrar con mensaje editorial propio, no como cita atribuida: "Una memoria comun sirve cuando alguien que no estuvo en la decision puede continuar el razonamiento."

## Estructura de cierre

Mensaje final:

> Antes de pedirle a un agente que entienda tus datos, dale una memoria que tu propio equipo pueda mantener.

Mensaje secundario:

> Una memoria comun sirve cuando alguien que no estuvo en la decision puede continuar el razonamiento.

Tratamiento visual: imagen editorial fuerte, preferentemente full-bleed o semi-bleed, con aire para el mensaje. Evitar robots, grafos tecnicos, dashboards, tablas o wallpaper abstracto. La imagen debe amplificar disciplina operativa y continuidad de razonamiento.

No usar frase propia como cita. Si en build se encuentra una cita real y verificable de un referente pertinente, puede reemplazar el mensaje secundario; si no, mantenerlo como mensaje editorial.

## Riesgos narrativos

- Anti-Markdown: mitigado al presentarlo como primer ladrillo correcto.
- Venta de herramienta: mitigado al hablar de capas y responsabilidades.
- Sobregobierno: mitigado con contrato minimo progresivo.
- OKF sobredimensionado: mitigado al llamarlo referencia emergente v0.1, no estandar corporativo final.
- MCP sobredimensionado: mitigado al tratarlo como interfaz, no memoria.
- Solapamiento con charla 2: mitigado dejando RAG, embeddings y grafos solo como teaser.

## Phase summary

La fase narrative deja una narrativa de 9 slides lista para build, con tesis clara, tension por capas, objetos visibles por slide y cierre editorial alineado a la serie. La siguiente fase recomendada es build del PPTX editable.

## Listo para build

Si.
