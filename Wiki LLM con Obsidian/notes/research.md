# Research

Research value: high

## Idea o pregunta investigada

`Puede un stack basado en Obsidian convertirse en una wiki LLM realmente util para trabajo de conocimiento y para un repo tecnico, y como se implementa sin quedarse en una idea abstracta?`

## Tesis propuesta

La tesis mas fuerte no es "Obsidian reemplaza RAG". La tesis mas fuerte es:

`Para conocimiento que se consulta y refina repetidamente, conviene compilar una capa intermedia de conocimiento en markdown antes que reconsultar fuentes crudas en cada pregunta. Obsidian funciona bien como frontend y filesystem de esa capa, siempre que exista esquema, proveniencia, enlaces, ingest incremental y lint de calidad.`

## Resumen ejecutivo

El disparador real de esta idea fue el gist `LLM Wiki` de Andrej Karpathy, publicado el `4 de abril de 2026`, donde plantea que la experiencia comun con LLMs y documentos se parece a RAG: se buscan trozos y se responde, pero no se acumula conocimiento. Esa pieza da la tesis, no el playbook completo.

La buena noticia es que ya aparecieron implementaciones mas operativas que si bajan la idea a flujo: `init -> ingest -> compile -> query -> lint`, con una wiki en markdown, `[[wikilinks]]`, frontmatter, git y Obsidian como visor natural.

La conclusion del research hasta ahora es clara: si quieres una charla fuerte, el angulo no debe ser "Obsidian con IA". Debe ser `conocimiento compilado versus conocimiento rederivado`. Obsidian importa menos como marca y mas como combinacion de tres propiedades: archivos markdown locales, enlaces nativos y ecosistema util para visualizar y auditar la memoria.

## Panorama actual

### Hecho verificado

- El gist de Karpathy existe y fue creado el `4 de abril de 2026`.
- Su planteamiento central es que el problema de muchos flujos tipo RAG es que vuelven a descubrir el conocimiento desde cero en cada consulta.
- Obsidian encaja bien como frontend porque trabaja sobre markdown local, `[[wikilinks]]`, propiedades y graph view.
- Ya existen implementaciones open source que convierten la idea en un flujo operativo.

### Interpretacion

El espacio se esta moviendo rapido desde `chat with docs` hacia `compile your docs into a durable artifact`. Esto no invalida RAG, pero si cambia el centro de gravedad cuando el trabajo exige continuidad y acumulacion.

### Recomendacion

La charla debe poner en el centro el cambio de paradigma:

- de `buscar y responder`
- a `compilar, enlazar y mantener`

## Hallazgos que si merecen slide

1. `El problema no es solo recuperar bien; es no empezar de cero cada vez`
   Karpathy formula con claridad el limite del patron clasico basado en retrieval por consulta.

2. `La wiki LLM agrega una capa intermedia entre la fuente cruda y la respuesta`
   Esa capa ya contiene resumentes, enlaces, entidades, conceptos y contradicciones detectadas.

3. `Obsidian es valioso porque ya resuelve visualizacion y estructura nativa`
   Graph view, propiedades y clipping local reducen mucha friccion de producto.

4. `La unidad minima no es el prompt, sino el workflow`
   Los proyectos mas operativos convergen en `init`, `ingest`, `compile`, `query`, `lint`.

5. `La clave no es solo responder preguntas; es escribir de vuelta en la memoria`
   Algunas implementaciones archivan las respuestas o promueven queries utiles a paginas durables.

6. `Sin esquema y proveniencia, la wiki se degrada`
   El sistema necesita frontmatter, reglas de nombrado, separacion entre `raw/` y `wiki/`, y trazabilidad.

7. `No todo debe entrar`
   La wiki util no es dump infinito; necesita criterio de seleccion, merge y mantenimiento.

## Opciones o enfoques encontrados

| Opcion | Madurez | Ventajas | Limitaciones | Lectura para la charla |
|---|---|---|---|---|
| Gist/patron de Karpathy | Alta como idea | Tesis muy limpia, critica fuerte al loop de RAG | No trae implementacion paso a paso | Excelente apertura conceptual |
| Plugin orientado a Obsidian + flujo de comandos | Moderada | Baja la idea a operaciones concretas y estructura de carpetas | Acoplado a un agente o stack especifico | Muy util para slides de "asi se opera" |
| Framework de skills multi-agente con Obsidian | Moderada | Conecta wiki con agentes, skills, `AGENTS.md` y repo real | Puede sentirse demasiado meta si no se recorta | Ideal para unirlo con tu experiencia |
| Local-first con Ollama/Qwen/QMD | Moderada | Muestra variante privada y sin cloud | Anade complejidad de runtime y search | Sirve para tradeoff y limites |

## Narrativa sugerida de la charla

### Slide 1

- kicker: `Memoria`
- titulo con tesis: `El problema no es conversar con documentos; es que el sistema olvida todo lo que ya aprendio`
- objeto de prueba visible: comparacion simple entre `chat with docs` y `wiki compilada`
- takeaway: el costo oculto de RAG por consulta es rehacer sintesis una y otra vez

### Slide 2

- kicker: `Baseline`
- titulo con tesis: `La mayoria de flujos con documentos siguen funcionando como retrieval de ultima milla`
- objeto de prueba visible: diagrama de flujo `fuentes -> retrieval -> prompt -> respuesta`
- takeaway: responde, pero no acumula

### Slide 3

- kicker: `Cambio`
- titulo con tesis: `Karpathy propone compilar conocimiento antes de consultarlo`
- objeto de prueba visible: fecha `4 de abril de 2026`, gist y esquema conceptual
- takeaway: la unidad de valor pasa de chunk relevante a pagina durable

### Slide 4

- kicker: `Arquitectura`
- titulo con tesis: `La wiki LLM introduce una capa intermedia entre la fuente cruda y la respuesta`
- objeto de prueba visible: pipeline `raw -> compile -> wiki -> query`
- takeaway: la respuesta ya no parte de cero

### Slide 5

- kicker: `Producto`
- titulo con tesis: `Obsidian funciona bien porque ya trae markdown local, enlaces y visualizacion del grafo`
- objeto de prueba visible: tabla con `wikilinks`, `properties`, `graph view`, `web clipper`
- takeaway: gran parte del producto ya existe antes del LLM

### Slide 6

- kicker: `Operacion`
- titulo con tesis: `El workflow minimo se parece mas a mantener una base editorial que a chatear`
- objeto de prueba visible: secuencia `init -> ingest -> compile -> query -> lint`
- takeaway: el valor vive en la rutina operativa

### Slide 7

- kicker: `Repo`
- titulo con tesis: `Para un repositorio real, la wiki debe separar fuente, conocimiento compilado y reglas`
- objeto de prueba visible: estructura recomendada de carpetas
- takeaway: sin layout ni esquema, la memoria deriva rapido

### Slide 8

- kicker: `Tradeoff`
- titulo con tesis: `Una wiki LLM gana continuidad, pero exige curaduria, proveniencia y control de drift`
- objeto de prueba visible: comparacion `RAG ad hoc` vs `wiki compilada`
- takeaway: no es gratis; cambia compute por mantenimiento

### Slide 9

- kicker: `Decision`
- titulo con tesis: `Conviene cuando preguntas parecidas vuelven, las fuentes se acumulan y el contexto importa`
- objeto de prueba visible: criterios de adopcion
- takeaway: ideal para research, repos, decisiones tecnicas y memoria de equipo pequeno

### Slide 10

- kicker: `Cierre`
- titulo con tesis: `El verdadero upgrade no es buscar mejor, sino recordar mejor`
- objeto de prueba visible: frase final + imagen editorial
- takeaway: una memoria compuesta vale mas que mil consultas aisladas

## Caso paso a paso para un repo

Este es el hallazgo mas importante para ti: si existe una forma razonable de aterrizarlo a un repo, pero hay que mezclar el patron de Karpathy con implementaciones recientes.

### Estructura minima recomendada

```text
repo/
|-- AGENTS.md
|-- docs/ o notes/
|-- wiki/
|   |-- raw/
|   |   |-- repo-docs/
|   |   |-- decisions/
|   |   |-- transcripts/
|   |   `-- external/
|   |-- compiled/
|   |   |-- concepts/
|   |   |-- entities/
|   |   |-- systems/
|   |   |-- queries/
|   |   `-- index.md
|   |-- outputs/
|   |   `-- reports/
|   |-- MEMORY.md
|   |-- PLAN.md
|   `-- WIKI-SCHEMA.md
`-- .obsidian/
```

### Flujo operativo recomendado

1. `Inicializar`
   Crear la estructura del vault o del subarbol `wiki/`, con reglas de nombres, tipos de pagina y frontmatter base.

2. `Separar raw de compiled`
   `raw/` no se edita manualmente salvo higiene minima. `compiled/` es propiedad del agente.

3. `Definir esquema`
   En `WIKI-SCHEMA.md` o equivalente:
   - tipos de pagina
   - secciones obligatorias
   - campos de proveniencia
   - convenciones de `[[wikilinks]]`
   - reglas de merge y actualizacion

4. `Ingestar fuentes del repo`
   - `README.md`
   - `AGENTS.md`
   - `MEMORY.md`
   - ADRs o decisiones
   - notas de research
   - transcripciones o conversaciones utiles

5. `Compilar paginas`
   El agente crea o actualiza:
   - paginas de concepto
   - paginas de entidades
   - paginas de sistema
   - indices tematicos
   - resumentes de fuente

6. `Consultar sobre la wiki compilada`
   Las preguntas deben leer primero `compiled/`, no volver a leer todo `raw/`, salvo cuando falte evidencia o haya staleness.

7. `Escribir de vuelta`
   Si una respuesta produjo una sintesis util y reusable, se archiva en `queries/` o se promueve a pagina canonica.

8. `Lint y drift control`
   Revisar:
   - paginas huerfanas
   - enlaces muertos
   - contradicciones
   - paginas sin fuente
   - fuentes cambiadas sin recompilar

### Que markdowns son vitales

- `AGENTS.md`: reglas de comportamiento del agente dentro del repo
- `MEMORY.md`: contexto estable y decisiones persistentes
- `PLAN.md`: trabajo temporal o fase actual, no memoria permanente
- `WIKI-SCHEMA.md`: contrato operativo de la wiki
- `index.md`: mapa de entrada para navegacion y query

### Donde se parece a tu idea de harness

Se parece bastante, pero con otro centro:

- `Harness Engineer` habla del sistema operativo del agente
- `Wiki LLM con Obsidian` habla de la memoria operativa compilada dentro de ese sistema

La charla 2 de `protocolos minimos` seria aun mas prescriptiva:

- como organizas repo
- que markdowns son obligatorios
- como separas stages
- que checks hacen falta
- como defines skills y scopes

Esa charla seria casi un manual minimo de operacion para equipos.

## Claims a validar antes de cerrar la deck

- Si queremos afirmar que este patron ya desplaza RAG en equipos reales, falta evidencia fuerte.
- Si queremos hablar de adopcion de Obsidian en empresas, falta fuente mas robusta.
- Si queremos cuantificar ahorro de tokens o tiempo, hoy no tengo benchmark serio y comparable.
- Si queremos afirmar que ciertas implementaciones son las mas maduras del mercado, falta un barrido mas amplio.

## Riesgos y consideraciones

- `Vendor drift`: varias implementaciones dependen de un agente especifico.
- `Hallucination persistence`: si una pagina compilada queda mal, el error puede propagarse.
- `Editorial overhead`: mantener buena estructura exige disciplina.
- `Falsa sensacion de memoria`: una wiki grande sin lint ni proveniencia se vuelve otro basurero semantico.
- `Escala`: para corpus muy grande, la capa compilada necesita buenos criterios de sharding, search y refresh.

## Recomendacion

Usaria como tesis principal:

`La ventaja no viene de preguntarle mejor al modelo, sino de darle una memoria compilada que no tenga que reconstruirse en cada turno.`

La comparacion central debe ser:

- `RAG por consulta`
- versus
- `wiki compilada e incremental`

Dejaria fuera, al menos en la primera version:

- guerra de plugins de Obsidian
- detalles finos de embeddings
- comparativas de modelos locales
- obsesion por herramientas especificas

El corazon de la charla debe ser arquitectonico y operativo, no de gadget.

## Cierre editorial propuesto

- mensaje final de una linea: `No todo conocimiento debe recuperarse; parte del conocimiento debe quedarse escrito.`
- cita o frase breve: `Recordar bien tambien es una forma de pensar bien.`
- metafora visual sugerida: una sala de archivo contemporanea convertida en red viva de hilos y fichas, mitad biblioteca editorial, mitad sistema nervioso
- tono emocional del cierre: lucido, deliberado, sobrio

## Donde profundizar despues

- que tan bien funciona esto para repositorios de codigo frente a research puro
- como modelar staleness y recompilacion incremental
- como combinar wiki compilada con retrieval clasico sin duplicar complejidad
- patrones de calidad para evitar que la memoria se pudra
- caso practico end-to-end sobre un repo real pequeno

## Fuentes consultadas

1. Andrej Karpathy, `LLM Wiki`, fuente primaria, gist, `4 de abril de 2026`, relevancia muy alta, patron original.  
   https://gist.github.com/karpathy

2. Obsidian Help, `Web Clipper`, fuente primaria, documentacion oficial, consultada en junio de 2026, relevancia alta para ingest local y clipping.  
   https://obsidian.md/help/web-clipper

3. Obsidian Help, `Properties view`, fuente primaria, documentacion oficial, consultada en junio de 2026, relevancia alta para metadata y esquema.  
   https://obsidian.md/help/plugins/properties

4. Obsidian Help, `Graph view`, fuente primaria, documentacion oficial, consultada en junio de 2026, relevancia alta para visualizacion y estructura de enlaces.  
   https://obsidian.md/help/plugins/graph

5. `ekadetov/llm-wiki`, fuente secundaria pero concreta, repositorio GitHub, consultado en junio de 2026, relevancia alta por su flujo `init/ingest/compile/query/lint`.  
   https://github.com/ekadetov/llm-wiki

6. `ekadetov/llm-wiki/WALKTHROUGH.md`, fuente secundaria, walkthrough operativo, consultado en junio de 2026, relevancia muy alta por el paso a paso.  
   https://github.com/ekadetov/llm-wiki/blob/main/WALKTHROUGH.md

7. `Ar9av/obsidian-wiki`, fuente secundaria, repositorio GitHub, consultado en junio de 2026, relevancia alta por conectar wiki con skills, agentes y `AGENTS.md`.  
   https://github.com/Ar9av/obsidian-wiki

8. `Ar9av/obsidian-wiki/SETUP.md`, fuente secundaria, guia de setup, consultada en junio de 2026, relevancia muy alta para aterrizarlo a repos y a Codex.  
   https://github.com/Ar9av/obsidian-wiki/blob/main/SETUP.md

9. `NiharShrotri/llm-wiki`, fuente secundaria, repositorio GitHub, consultado en junio de 2026, relevancia moderada-alta para la variante local-first con Ollama/Qwen/QMD.  
   https://github.com/NiharShrotri/llm-wiki

10. `blacksmithgu/obsidian-dataview`, fuente secundaria muy consolidada, repositorio GitHub, consultado en junio de 2026, relevancia alta para consultas sobre frontmatter e indices.  
   https://github.com/blacksmithgu/obsidian-dataview

## Nivel de confianza

Moderado a alto.

La tesis principal esta bien soportada por fuentes primarias y por implementaciones recientes. Lo que todavia no esta bien soportado es la parte cuantitativa: adopcion, ROI, ahorro de tokens o superioridad medible frente a RAG en escenarios comparables.
