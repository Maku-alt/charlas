# Talk Spine

## Tesis final recomendada

`La mejor memoria para un agente no es un dump infinito de contexto ni una consulta RAG rehecha en cada turno. Es una capa compilada de conocimiento que conserva decisiones, relaciones y respuestas reutilizables.`

## Pregunta central

`Cuando el trabajo depende de continuidad, conviene seguir reconsultando fuentes crudas o compilar una wiki viva que el agente pueda mantener?`

## Angulo recomendado

No vender la charla como:

- tutorial de Obsidian
- comparativa de plugins
- demo de second brain personal

Venderla como:

- arquitectura de memoria operativa para trabajo de conocimiento
- alternativa al patron de rederivar todo en cada consulta
- puente entre repo, notas, research y decisiones

## Narrativa ejecutiva

1. hoy muchos flujos con documentos siguen funcionando como `rediscover every time`
2. eso responde preguntas, pero no acumula criterio
3. una wiki compilada crea una capa intermedia durable
4. Obsidian funciona bien como frontend porque ya resuelve markdown, links y visualizacion
5. el valor real aparece cuando la wiki archiva decisiones y queries utiles
6. el costo no desaparece: se traslada a esquema, proveniencia y mantenimiento
7. para repos pequenos o medianos, ese tradeoff puede cerrar muy bien

## Estructura sugerida de 8-10 slides

### Slide 1

- kicker: `Memoria`
- titulo: `El problema no es recuperar documentos; es volver a pensar lo mismo en cada turno`
- prueba visible: contraste entre consulta ad hoc y capa compilada
- takeaway: retrieval no equivale a acumulacion

### Slide 2

- kicker: `Patron actual`
- titulo: `La mayoria de stacks con documentos siguen operando como descubrimiento repetido`
- prueba visible: flujo `files -> retrieve -> prompt -> answer`
- takeaway: el sistema responde, pero no aprende estructuralmente

### Slide 3

- kicker: `Cambio de paradigma`
- titulo: `Karpathy reordena la pregunta: primero compilar, despues consultar`
- prueba visible: gist del `4 de abril de 2026` y cambio de arquitectura
- takeaway: la unidad de valor pasa del chunk a la pagina durable

### Slide 4

- kicker: `Caso real`
- titulo: `En este repo, una wiki compilada ya puede responder sin releerlo todo`
- prueba visible: demo `charlas` con `raw`, `compiled` y `query filed`
- takeaway: la idea no es abstracta; se aterriza

### Slide 5

- kicker: `Frontend`
- titulo: `Obsidian importa menos por la marca que por sus primitivas correctas`
- prueba visible: markdown local, `[[wikilinks]]`, properties, graph, clipper
- takeaway: gran parte del producto ya existe

### Slide 6

- kicker: `Workflow`
- titulo: `La unidad minima no es el prompt; es el ciclo ingest, compile, query y lint`
- prueba visible: secuencia operativa
- takeaway: esto se parece mas a editar una base viva que a chatear

### Slide 7

- kicker: `Valor`
- titulo: `La wiki gana cuando conserva decisiones, intentos, fallos y respuestas reutilizables`
- prueba visible: ejemplo de query archivada y paginas relacionadas
- takeaway: memoria operativa es mas que almacenamiento

### Slide 8

- kicker: `Tradeoff`
- titulo: `La memoria compilada reduce reconstruccion, pero exige curaduria y control de drift`
- prueba visible: tabla `RAG ad hoc` vs `wiki compilada`
- takeaway: cambia compute por mantenimiento deliberado

### Slide 9

- kicker: `Decision`
- titulo: `Conviene cuando el trabajo vuelve sobre las mismas preguntas con fuentes que crecen`
- prueba visible: criterios de adopcion
- takeaway: mejor para research, repos tecnicos y equipos pequenos que para corpus masivo sin gobierno

### Slide 10

- kicker: `Cierre`
- titulo: `El verdadero upgrade no es buscar mejor, sino recordar mejor`
- prueba visible: cita + imagen editorial
- takeaway: parte del conocimiento debe quedarse escrito

## Slides que merecen objeto de prueba fuerte

- slide 4: screenshot o esquema del demo del repo
- slide 6: pipeline claro de operaciones
- slide 8: tabla ejecutiva de tradeoffs

## Cosas que dejaria fuera

- guerra RAG vs no-RAG demasiado dogmatica
- detalles de vectores o embeddings
- plugin zoo de Obsidian
- claims de ROI cuantitativo sin benchmark serio

## Mensaje final recomendado

`Un agente mejora cuando su memoria deja de ser contexto pasajero y se vuelve conocimiento mantenido.`

## Cita breve candidata

`Recordar bien tambien es una forma de pensar bien.`

## Metafora visual de cierre

Archivo editorial contemporaneo convertido en red viva: fichas, hilos, papel, luz y estructura; menos dashboard, mas memoria materializada.
