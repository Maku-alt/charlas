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
- tratamiento de cierre: imagen full-bleed o semi-bleed con overlay sobrio, mensaje final y cita editorial con aire suficiente

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
- objeto visible: una ficha de tabla que se multiplica hasta convertirse en un mapa de conocimiento
- takeaway: el problema no es escribir mas; es conectar y mantener lo que el equipo ya sabe

### Slide 2
- kicker: Baseline
- titulo: Una ficha Markdown por tabla resuelve el primer 20 por ciento, no el sistema
- objeto visible: `clientes.md` simple con descripcion, columnas y usos
- takeaway: Markdown es buen formato base porque es portable y versionable

### Slide 3
- kicker: Friccion
- titulo: El dolor aparece cuando la pregunta cruza tablas, metricas y decisiones pasadas
- objeto visible: preguntas alrededor de `clientes`: owner, vigencia, joins, riesgos, dashboards, dudas resueltas y metricas relacionadas
- takeaway: la unidad de valor ya no es la ficha; es la red de conocimiento

### Slide 4
- kicker: Distincion
- titulo: Wiki no es lo mismo que memoria operacional
- objeto visible: dos paneles, grafo humano versus checklist operacional
- takeaway: navegar conocimiento y gobernarlo son problemas distintos

### Slide 5
- kicker: Contrato
- titulo: Un knowledge repo empieza cuando cada ficha declara identidad, relaciones y responsabilidad
- objeto visible: YAML frontmatter + cuerpo Markdown + links a metricas, dominios y owners
- takeaway: la arquitectura vive en el contrato minimo, no en la herramienta

### Slide 6
- kicker: Ecosistema
- titulo: Los catalogs modernos confirman que la metadata util es relacional
- objeto visible: una tabla conectada a owner, glossary, lineage, quality, contract, dashboard y consumidores
- takeaway: no estamos inventando burocracia; estamos bajando capacidades de catalogo a una escala operable

### Slide 7
- kicker: Agentes
- titulo: Un agente no necesita leerlo todo: necesita una entrada confiable y contexto ensamblable
- objeto visible: agente -> MCP/API -> knowledge repo -> fichas, versionado y owners
- takeaway: preparar memoria reduce improvisacion y contexto irrelevante

### Slide 8
- kicker: Tradeoff
- titulo: La decision no es Markdown versus catalogo: es que capa cumple cada rol
- objeto visible: matriz de capas con `Markdown`, `Wiki`, `Knowledge repo`, `OKF-style bundle`, `MCP/API`
- takeaway: separar capas evita comprar herramienta o sobrediseniar antes de tiempo

### Slide 9
- kicker: Cierre
- titulo: La documentacion que escala no guarda paginas: conserva decisiones reutilizables
- objeto visible: imagen editorial final alineada con `notes/image-close-brief.md` o, si falta, con la direccion visual del `narrative-spec`
- mensaje editorial: Una memoria comun sirve cuando alguien que no estuvo en la decision puede continuar el razonamiento.
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

- listo para build
