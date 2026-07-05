# Research Brief

Research value: high

## Idea o pregunta investigada

Como definir con precision un `knowledge repo` para equipos de datos y por que importa como paso evolutivo entre fichas Markdown sueltas y una memoria operacional util para humanos y agentes.

## Modo de trabajo

- Modo: orientado a decision + estado del arte.
- Nivel de esfuerzo: standard.
- Decision de continuidad: seguir.

## Tesis propuesta

Cuando un equipo documenta muchas tablas, la unidad de trabajo deja de ser "un archivo por tabla" y pasa a ser una memoria operacional: un repo con convenciones, relaciones, ownership, vigencia, historial e interfaces de consulta. Markdown puede ser el ladrillo correcto; la arquitectura aparece cuando el equipo define como se conectan, se mantienen y se consumen esas piezas por humanos y agentes.

Formulacion breve:

> Documentar tablas se vuelve arquitectura de conocimiento cuando el equipo necesita conectar, mantener y consultar lo que sabe.

## Resumen ejecutivo

La hipotesis se sostiene. Las fuentes actuales separan con claridad cuatro capas: Markdown como formato legible y portable; wiki o segundo cerebro como navegacion humana; catalogos/metadatos como evidencia de que ownership, lineage, glossaries, calidad y versionado son parte del conocimiento operativo; y MCP/API como interfaz para exponer contexto y herramientas a agentes. OKF, publicado como draft v0.1 en junio de 2026, aporta una referencia emergente para bundles de Markdown con frontmatter, pero su valor debe presentarse como convencion portable, no como arquitectura completa ni como estandar maduro.

El angulo recomendado no es "necesitamos una herramienta", sino "necesitamos separar responsabilidades". La charla debe ayudar a la audiencia a dejar de discutir si el destino es Markdown, wiki, catalogo o agente, y empezar a ver esas piezas como capas: formato, navegacion, gobierno, memoria y acceso.

## Panorama actual

### 1. Markdown resuelve forma, no sistema

Markdown tiene fuerza porque es texto plano: se lee en cualquier editor, difiere bien en Git y permite contenido estructurado sin plataforma pesada. CommonMark lo define como formato de texto plano para documentos estructurados. GitHub lo usa como lenguaje legible para prose y codigo. Eso justifica "un `.md` por tabla" como inicio.

El limite es que Markdown no define por si mismo identidad canonica de cada activo, estructura minima obligatoria, ownership, vigencia, relaciones, procesos de revision, politicas de acceso ni semantica de consulta para agentes.

Lectura: Markdown es formato de captura y versionado, no memoria operacional.

### 2. Wiki y segundo cerebro mejoran navegacion humana

Herramientas como Obsidian muestran bien el valor de enlazar notas: links internos, backlinks y redes de conocimiento ayudan a explorar contexto. Eso es valioso para humanos, especialmente cuando el conocimiento esta distribuido y la busqueda textual no alcanza.

Pero una wiki no garantiza gobierno. Puede tener buenos enlaces y aun asi fallar en ownership, vigencia, autoridad, duplicados, control de cambios y criterios de inclusion. La wiki responde "como navego"; el knowledge repo debe responder tambien "que fuente vale", "quien mantiene", "cuando se actualizo" y "como se consume de forma confiable".

Lectura: la wiki es una capa de navegacion, no necesariamente la fuente operacional gobernada.

### 3. Los catalogos de datos prueban que la metadata relacional importa

DataHub y OpenMetadata son evidencia conceptual fuerte. No hacen "documentacion de tabla" como texto aislado: modelan entidades, propietarios, tags, glossary terms, dominios, lineage, perfiles, calidad, tareas, uso, version history y custom properties. dbt exposures muestra el mismo principio desde otro angulo: documentar downstream uses como dashboards, aplicaciones o pipelines, y conectar esos usos con el DAG.

El punto para la charla no es recomendar un catalogo especifico. Es usar esa madurez como prueba de que, cuando el volumen crece, el conocimiento sobre datos se vuelve relacional y operativo. Una ficha de tabla util no describe solo columnas: tambien registra relaciones, consumidores, riesgos, uso, owner, vigencia, joins frecuentes, terminos de negocio, calidad y decisiones previas.

Lectura: si los catalogos modelan relaciones y gobierno, un repo de conocimiento serio no puede quedarse en texto suelto.

### 4. OKF es referencia emergente, no destino final

Google Cloud introdujo Open Knowledge Format (OKF) el 12 de junio de 2026. La especificacion v0.1 lo presenta como formato abierto, humano y agent-friendly para representar conocimiento como directorios de Markdown con YAML frontmatter. Sus campos recomendados cubren `type`, `title`, `description`, `resource`, `tags` y `timestamp`; permite links Markdown, `index.md` para disclosure progresivo y `log.md` para historial.

La propia especificacion declara no objetivos importantes: no define taxonomia fija, no prescribe infraestructura de storage/serving/query y no reemplaza schemas de dominio como Avro, Protobuf u OpenAPI. Eso lo vuelve muy util para explicar "convencion portable", pero peligroso si se vende como solucion completa.

Lectura: OKF puede ser el ejemplo moderno de "Markdown con contrato minimo para agentes"; no reemplaza el diseno del knowledge repo.

### 5. MCP/API es interfaz de consulta, no memoria

MCP, anunciado por Anthropic el 25 de noviembre de 2024 y documentado en la especificacion vigente 2025-06-18, estandariza como aplicaciones LLM comparten contexto, exponen herramientas y construyen integraciones. Su modelo distingue hosts, clients y servers; los servers ofrecen resources, prompts y tools.

Eso encaja con la tesis: MCP sirve para exponer una memoria preparada a agentes, no para crear esa memoria. Si el repositorio esta desordenado, sin ownership ni vigencia, MCP solo hace mas facil consultar desorden. La interfaz no sustituye la arquitectura de conocimiento.

Lectura: primero memoria gobernada; despues interfaz de agente.

## Hallazgos que si merecen slide

1. "Un `.md` por tabla" es una buena primera decision, pero no una arquitectura.
2. Hay cuatro responsabilidades distintas: formato, navegacion, gobierno e interfaz.
3. La ficha de tabla minima deberia parecerse mas a metadata operacional que a descripcion larga.
4. Los catalogos de datos ya modelan el problema como grafo de metadata.
5. OKF muestra hacia donde se mueve el formato: Markdown + frontmatter + links + historial.
6. MCP no arregla memoria mala; la expone.
7. La decision ejecutiva es ownership antes que tooling.

## Mapa de contradicciones

| Tension | Lectura fuerte | Resolucion editorial |
|---|---|---|
| Markdown es simple vs. el sistema requiere gobierno | La simplicidad de Markdown es virtud, pero no alcanza para definir memoria. | "Markdown es el ladrillo; el repo es la arquitectura." |
| Wiki navegable vs. memoria confiable | Links y backlinks reducen friccion humana, pero no prueban vigencia ni autoridad. | Separar navegacion de gobierno. |
| Catalogo de datos vs. knowledge repo | El catalogo puede ser fuente de metadata; el repo puede capturar narrativa, decisiones y contexto operativo que no siempre vive en el catalogo. | Presentarlos como complementarios, no rivales. |
| OKF como estandar vs. OKF como draft reciente | OKF v0.1 es prometedor, pero todavia emergente. | Usarlo como referencia de direccion, no como mandato. |
| MCP conecta agentes vs. MCP resuelve conocimiento | MCP estandariza acceso a contexto/herramientas, pero no decide que contexto es valido. | "MCP es puerto de consulta, no memoria." |
| Mas documentacion vs. menos friccion | Pedir mas campos puede matar adopcion. | Definir contrato minimo y crecimiento progresivo por valor. |

## Opciones o enfoques encontrados

| Opcion | Madurez | Ventajas | Limitaciones | Lectura para la charla |
|---|---:|---|---|---|
| Fichas Markdown sueltas | Alta como formato, baja como sistema | Baratas, versionables, faciles de revisar | Escalan mal sin indice, relaciones y ownership | Buen inicio, insuficiente como destino |
| Wiki / segundo cerebro | Alta para navegacion humana | Links, backlinks, graph view, descubrimiento | Puede volverse decorativa o stale sin gobierno | Capa de navegacion |
| Knowledge repo gobernado | Media como practica, alta como patron software | Git, PRs, owners, historia, convenciones, CI posible | Requiere disciplina y contrato minimo | Tesis recomendada |
| Catalogo de datos | Alta en data governance | Metadata relacional, lineage, owners, glossary, calidad | Puede no capturar decisiones, narrativa o conocimiento tacito | Evidencia conceptual y posible fuente |
| OKF | Emergente, draft v0.1 | Markdown portable con frontmatter y convenciones para agentes | No define taxonomia, serving ni query | Referencia moderna, no solucion completa |
| MCP/API | Alta adopcion emergente para integracion agente-herramienta | Estandariza acceso a resources, prompts y tools | No corrige contenido pobre o desactualizado | Interfaz de consulta |

## Direccion narrativa sugerida

1. "Cuando las tablas se multiplican, documentar deja de ser escribir." Objeto: carpeta con decenas de fichas. Takeaway: el volumen cambia la naturaleza del problema.
2. "La tabla que ves en SQL es solo la superficie." Objeto: tabla rodeada de owner, metricas, joins, riesgos y consumidores. Takeaway: el conocimiento relevante es relacional.
3. "Markdown resuelve el formato, no la memoria." Objeto: archivo `.md` sin owner, status ni links. Takeaway: falta contrato operacional.
4. "La navegacion humana no equivale a gobierno." Objeto: red de notas con una nota desactualizada. Takeaway: enlaces ayudan, pero no certifican verdad.
5. "El conocimiento de datos se comporta como metadata relacional." Objeto: dataset conectado a owner, glossary, lineage, quality y consumers. Takeaway: una ficha seria debe modelar relaciones.
6. "Un repo de conocimiento es memoria operada como software." Objeto: PR con cambios a ficha, owner, checklist, `log.md` e indice. Takeaway: versionado, revision y mantenimiento son parte del producto.
7. "El formato portable ayuda cuando humanos y agentes consumen lo mismo." Objeto: YAML frontmatter + body + links + timestamp. Takeaway: estandarizar minima estructura reduce friccion.
8. "MCP/API expone la memoria, no la reemplaza." Objeto: agente solicitando recursos acotados desde un repo curado. Takeaway: la interfaz amplifica la calidad o el desorden.
9. "Arquitectura de conocimiento es decidir que vive donde." Objeto: matriz de capas: formato, navegacion, gobierno, acceso. Takeaway: el equipo sale con mapa de responsabilidades.
10. "Despues de ordenar la memoria, recien vale razonar sobre ella." Objeto: biblioteca ordenada que habilita busqueda/RAG/grafo. Takeaway: cierre hacia charla 2.

## Claims a validar antes de cerrar la deck

- Si se menciona OKF, usar fecha exacta: Google Cloud lo introdujo el 12 de junio de 2026; spec v0.1 draft. No llamarlo "estandar consolidado".
- Si se menciona MCP, usarlo como protocolo de integracion para contexto, tools y resources. No decir que "almacena memoria".
- No prometer ahorro de tokens, tiempo o costo sin evidencia propia.
- No decir que una wiki "no sirve"; decir que no garantiza gobierno por si sola.
- No decir que un knowledge repo reemplaza catalogo de datos; decir que puede complementarlo o consumir metadata del catalogo.
- Si se usa una cita de Karpathy sobre LLM wiki, verificar fuente primaria del gist al momento de build o usar parafrasis sin comillas.

## Riesgos y consideraciones

- Riesgo de hype: OKF y MCP son temas calientes. Mantenerlos como capas concretas, no como centro de la charla.
- Riesgo de abstraccion: usar una tabla conductora y mostrar objetos visibles.
- Riesgo de sobregobierno: proponer contrato minimo y evolucion progresiva, no burocracia.
- Riesgo de herramienta: evitar que parezca charla de Obsidian, Confluence, DataHub u OpenMetadata.
- Riesgo de solapamiento con charla 2: RAG, embeddings y grafos solo como teaser final.

## Recomendacion

Seguir a narrativa. La tesis esta validada y el angulo mas fuerte es una arquitectura por capas: Markdown captura, wiki navega, knowledge repo gobierna, OKF orienta portabilidad y MCP/API expone consulta para agentes. La narrativa debe mantener una tabla o dominio de ejemplo como hilo conductor para no caer en abstraccion.

## Cierre editorial propuesto

Mensaje final:

> Antes de pedirle a un agente que entienda tus datos, dale una memoria que tu propio equipo pueda mantener.

Imagen editorial:

Una sala de archivo moderna: estanterias sobrias con fichas conectadas por hilos finos de luz, una mesa central con una unica tarjeta de tabla abierta y una interfaz de consulta discreta al fondo. No debe verse como dashboard, diagrama ni tabla; debe sentirse como memoria organizada, humana y consultable.

## Donde profundizar despues

- Patrones de contrato minimo para fichas de tabla: campos obligatorios, owner, lifecycle, freshness, consumers, riesgos, joins y decisiones.
- Integracion con catalogos: export/import de metadata desde DataHub/OpenMetadata/dbt hacia repo Markdown.
- Validaciones automaticas: lint de frontmatter, links rotos, freshness, owners y status.
- Charla 2: busqueda, RAG, grafos y agentes sobre una memoria ya ordenada.

## Self-review

- Confidence score: 0.82.
- Weakest link: "knowledge repo" como termino no tiene una definicion industrial unica; debe presentarse como patron operativo definido por el equipo, no como categoria cerrada.
- Bias check: las fuentes de OKF vienen de Google Cloud y empujan una vision favorable. Se compensa usando los non-goals de la propia spec y evidencia de catalogos independientes.
- Missing perspective: experiencia empirica interna del equipo sobre volumen real de tablas, frecuencia de cambios y dolores de mantenimiento.
- What would change my mind: evidencia de que el equipo tiene pocas tablas, baja rotacion y un catalogo ya gobernado que cubre todos los casos; en ese escenario un knowledge repo separado podria ser exceso.

## Fuentes consultadas

Ver `notes/bibliografia.md`.

## Artefactos para notes

- `notes/research-brief.md`
- `notes/bibliografia.md`
- `notes/phase-summary.md`

## Nivel de confianza

Alto para la tesis y la direccion narrativa. Medio para predicciones de adopcion de OKF, por ser una referencia publicada recientemente y en version draft.
