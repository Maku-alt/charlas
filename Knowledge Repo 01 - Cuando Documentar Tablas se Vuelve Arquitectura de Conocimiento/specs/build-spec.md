# Build Spec

## Narrativa fuente

- `specs/narrative-spec.md`
- `notes/narrative-brief.md`
- `notes/research-brief.md`
- `notes/image-close-brief.md`, si ya existe al momento de construir

## Formato esperado

- pptx editable
- 9 slides
- render completo
- review posterior con `review-charlas`

## Sistema visual

- tono visual: ejecutivo, tecnico, editorial y sobrio; calma estrategica, no hype
- densidad: media; una tesis por slide, poco texto, objeto de prueba visible claro
- slide 1 debe funcionar como cover editorial introductoria con fondo azul profundo, alineada con la familia visual de decks del repo
- evitar que el interior de la deck se vuelva una sucesion de cajas, conectores y matrices; cada slide debe tener una idea visual dominante que refuerce la tesis
- paleta: usar `STYLE-CHARLAS.md` como base
  - fondo claro principal `#F4F0E8`
  - tinta principal `#0F172A`
  - azul profundo `#102A43`
  - azul secundario `#16324F`
  - acento naranja `#C75C2A`
  - acento naranja claro `#E07A3F`
  - acento verde `#2D6A4F`
  - arena suave `#EADBC8`
- uso de tablas: solo para tradeoffs o matrices de capas
- uso de charts: no usar charts cuantitativos; no hay benchmark propio
- uso de imagenes: usar una imagen editorial fuerte solo en el cierre; el resto debe apoyarse en diagramas, matrices, fichas y objetos visuales editables
- tratamiento de cierre: imagen full-bleed o semi-bleed con overlay sobrio, mensaje final y aire suficiente

## Restricciones

- no romper la tesis por slide
- no meter bullets innecesarios
- no perder legibilidad
- preservar tildes y texto correcto
- mantener fuente visible cuando aplique
- no sonar anti-Markdown; presentarlo como punto de partida correcto
- no vender ninguna herramienta como solucion total
- no presentar OKF como estandar corporativo maduro; usarlo como referencia emergente de formato portable
- no presentar MCP/API como memoria; es interfaz de consulta
- no presentar el knowledge repo como reemplazo automatico de catalogo
- no agregar claims cuantitativos de ahorro, costo o tokens
- no agregar precios, releases, compatibilidad o casos corporativos recientes sin validacion actual

## Referencias visuales

- `STYLE-CHARLAS.md`
- decks previas del repo como familia visual, sin copiar metafora de cierre:
  - `SDD-IAgentica/SDD-IAgentica-v2.pptx`
  - `IA Agentica de Conversacion a Sistema/IA-Agentica-De-Conversacion-A-Sistema.pptx`

## Slides a construir

### Slide 1

- kicker: Tesis
- titulo: Documentar tablas deja de ser documentacion cuando el equipo necesita memoria comun
- objeto visible: una ficha de tabla en primer plano y varias fichas conectadas hacia metricas, owners y decisiones
- concepto visual: cover editorial donde una ficha `clientes.md` se multiplica y empieza a formar un mapa curado
- takeaway: el problema no es escribir mas; es conectar y mantener lo que el equipo ya sabe

### Slide 2

- kicker: Baseline
- titulo: Markdown es el primer ladrillo correcto, pero no define el edificio
- objeto visible: `clientes.md` con descripcion, columnas principales y usos conocidos
- concepto visual: ficha Markdown limpia, util y limitada, tratada como pieza inicial de arquitectura
- takeaway: Markdown aporta portabilidad, lectura humana y versionado; todavia no aporta gobierno

### Slide 3

- kicker: Friccion
- titulo: El dolor real aparece cuando una pregunta cruza tablas, metricas y decisiones pasadas
- objeto visible: owner, freshness, joins frecuentes, dashboards, metricas, riesgos, consumidores y dudas ya resueltas alrededor de `clientes`
- concepto visual: la ficha `clientes` como centro de una mesa de investigacion con preguntas pegadas alrededor
- takeaway: la unidad de valor deja de ser la ficha; pasa a ser la red de contexto que permite decidir

### Slide 4

- kicker: Distincion
- titulo: Una wiki ayuda a encontrar conocimiento; no garantiza que ese conocimiento sea vigente
- objeto visible: panel izquierdo con links/backlinks; panel derecho con owner, status, fecha de revision, fuente canonica y decision registrada
- concepto visual: comparacion editorial entre grafo de notas navegable y control operacional de vigencia
- takeaway: navegar y gobernar son problemas distintos

### Slide 5

- kicker: Contrato
- titulo: Un knowledge repo empieza cuando cada ficha declara identidad, relaciones y responsabilidad
- objeto visible: YAML con `id`, `owner`, `domain`, `status`, `freshness`, `related_metrics`, `consumers`, `last_reviewed`; cuerpo Markdown con decisiones y links
- concepto visual: ficha partida en frontmatter, cuerpo narrativo y bitacora de cambios
- takeaway: la arquitectura vive en el contrato minimo, no en la herramienta

### Slide 6

- kicker: Evidencia
- titulo: Los catalogos modernos muestran que el conocimiento de datos ya es relacional
- objeto visible: tabla conectada a owner, glossary, lineage, quality, contract, dashboard, consumidores y version history
- concepto visual: activo de datos como nodo sobrio conectado a aspectos operativos, sin saturar la composicion
- takeaway: no se trata de inventar burocracia; se trata de capturar a escala pequena lo que los catalogos modelan a escala grande
- fuente visible: DataHub, OpenMetadata, dbt exposures

### Slide 7

- kicker: Portabilidad
- titulo: OKF apunta a una idea util: Markdown con estructura explicita para humanos y agentes
- objeto visible: ejemplo conceptual de bundle OKF-style con `index.md`, ficha Markdown, frontmatter, `log.md` y links
- concepto visual: bundle de conocimiento como carpeta ordenada y portable
- takeaway: OKF sirve como referencia emergente de convencion portable; no es un estandar corporativo final ni una plataforma completa
- fuente visible: Google Cloud OKF, 2026-06-12; OKF spec v0.1 draft

### Slide 8

- kicker: Agentes
- titulo: MCP/API abre la puerta al agente, pero no convierte desorden en memoria
- objeto visible: agente -> MCP/API -> indice curado -> ficha versionada -> owner/relaciones/decisiones
- concepto visual: un agente consulta una puerta estrecha y confiable, no una carpeta infinita de Markdown
- takeaway: un agente no necesita leerlo todo; necesita entradas confiables y contexto ensamblable
- fuente visible: Model Context Protocol specification 2025-06-18

### Slide 9

- kicker: Cierre
- titulo: La documentacion que escala no guarda paginas: conserva decisiones reutilizables
- objeto visible: imagen editorial final alineada con `notes/image-close-brief.md` o, si falta, con la direccion visual del `narrative-spec`
- concepto visual: archivo editorial moderno con una tarjeta de tabla abierta, caminos sutiles hacia decisiones y una interfaz discreta al fondo
- mensaje editorial: Antes de pedirle a un agente que entienda tus datos, dale una memoria que tu propio equipo pueda mantener.
- mensaje secundario: Una memoria comun sirve cuando alguien que no estuvo en la decision puede continuar el razonamiento.
- fuente visible: no presentar frase editorial propia como cita; usar `Mensaje editorial` o una cita real atribuible si se valida externamente
- takeaway: una memoria comun vale cuando permite que otro continue el razonamiento

## Imagen editorial final

Generar o usar una imagen bitmap local en `assets/` para la slide final.

Nombre sugerido del artefacto:

- `assets/closing-knowledge-repo.png`

La imagen:

- no debe repetir tablas, dashboards, bullets ni grafos tecnicos
- debe dejar aire para texto sobrepuesto
- debe sentirse mas archivo editorial curado que interfaz de software
- debe reforzar calma estrategica y disciplina operativa

## Evidencia obligatoria de build

- ruta del pptx
- cantidad de slides
- renders individuales
- contact sheet
- chequeo textual con extraccion del pptx
- chequeos mecanicos
- estado de render nativo de PowerPoint si esta disponible
- riesgos residuales

## Decision de continuidad

Listo para build.
