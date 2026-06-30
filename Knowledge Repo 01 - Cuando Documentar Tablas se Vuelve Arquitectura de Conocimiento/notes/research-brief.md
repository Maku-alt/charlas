# Research Brief

Research value: high

## Idea o pregunta investigada

Como definir con precision un `knowledge repo` para equipos de datos y por que importa como paso evolutivo entre fichas Markdown sueltas, una wiki de navegacion humana y una memoria operacional util para humanos y agentes.

## Modo de trabajo

- `modo orientado a decision`
- `modo estado del arte`

## Nivel de esfuerzo

`standard`

Esta es una nueva corrida desde cero. No se usaron briefs anteriores ni outputs previos.

## Tesis propuesta

Documentar tablas se vuelve arquitectura de conocimiento cuando el equipo deja de necesitar solo descripciones y empieza a necesitar memoria comun: fichas conectadas, versionadas, con ownership, vigencia, relaciones, evidencia y una interfaz de consulta acotada para humanos y agentes.

Formula breve:

> Un `knowledge repo` no es mas documentacion. Es el contrato operativo que convierte lo que el equipo sabe sobre sus datos en algo mantenible, navegable y consultable.

## Resumen ejecutivo

La hipotesis inicial se sostiene, con una correccion editorial: `Markdown`, `wiki`, `OKF` y `MCP/API` no compiten entre si. Son capas distintas.

- `Markdown` resuelve legibilidad, portabilidad y revision por Git, pero no define por si mismo ownership, vigencia, relaciones ni procesos.
- Una `wiki` o segundo cerebro mejora navegacion humana, enlaces y descubrimiento, pero no garantiza memoria operacional gobernada.
- Un `knowledge repo` aparece cuando hay convenciones explicitas: ficha minima, metadata, owners, estado de vigencia, relaciones, historial, criterios de revision y rutas de acceso.
- `OKF` sirve como referencia portable para bundles de conocimiento en Markdown con frontmatter, enlaces y validacion; hoy debe tratarse como patron emergente, no como estandar corporativo universal.
- `MCP/API` es la capa de acceso para agentes: permite buscar, leer y atravesar conocimiento preparado. No sustituye el repo ni su gobierno.

## Panorama actual

La evidencia converge en una separacion de responsabilidades:

| Capa | Rol | Lo que resuelve | Lo que no resuelve sola |
|---|---|---|---|
| Markdown | Formato base | Texto legible, versionable, revisable | Metadata obligatoria, ownership, freshness, relaciones |
| Wiki / segundo cerebro | Navegacion humana | Links, backlinks, grafo, lectura exploratoria | Gobierno, fuente de verdad, proceso de mantenimiento |
| Knowledge repo | Memoria operacional | Convenciones, ownership, vigencia, relaciones, revision | No es una UI por si mismo ni un agente |
| OKF o formatos cercanos | Paquete portable | Markdown tipado, frontmatter, links, validacion | No define estrategia de gobierno ni modelo organizacional |
| MCP/API | Interfaz de acceso | Herramientas para que agentes consulten conocimiento | No crea conocimiento confiable si el repo esta mal mantenido |

## Hallazgos que si merecen slide

- La distincion central no es herramienta contra herramienta; es capa contra capa. Markdown puede ser correcto y aun asi insuficiente.
- `Una ficha por tabla` es buen primer ladrillo, pero escala mal si no hay indice, relaciones, owners, estado de vigencia y regla de revision.
- La wiki organiza lectura humana; el knowledge repo organiza responsabilidad operacional.
- Los catalogos y herramientas de datos modernas modelan ownership, lineage, descripciones, tests o freshness porque documentar datos no es solo escribir texto.
- Para agentes, el problema no es "leer mas archivos"; es saber que buscar, que fuente es vigente, que relaciones seguir y que evidencia citar.
- MCP debe entrar como interfaz, no como arquitectura: el agente invoca herramientas sobre una memoria preparada.
- OKF puede ser una referencia util para explicar portabilidad y fichas tipadas, pero el argumento no debe depender de que OKF gane como estandar.

## Mapa de contradicciones

| Tension | Evidencia / lectura | Resolucion editorial |
|---|---|---|
| Markdown es suficiente porque Git ya versiona | CommonMark muestra que Markdown es formato de texto estructurado; Git aporta historial, pero no define semantica operacional. | Presentar Markdown como ladrillo correcto, no como sistema completo. |
| Wiki ya es knowledge repo | GitHub y Obsidian enfatizan documentacion, links, grafo y navegacion. Eso ayuda al humano, pero no obliga ownership, freshness ni contratos de mantenimiento. | Wiki = capa de descubrimiento; repo = memoria gobernada. |
| Data catalogs ya resuelven esto | dbt/DataHub/OpenMetadata muestran metadata, lineage, ownership y freshness. Pero una charla sobre knowledge repo puede ser tool-agnostic: el repo puede complementar catalogos o servir como capa liviana. | No vender reemplazo de catalogo; hablar de contrato de conocimiento. |
| OKF parece promesa demasiado nueva | Repos actuales lo presentan como Markdown tipado, agent-friendly y Git-diffable, pero el ecosistema aun es emergente. | Usarlo como ejemplo de patron portable, no como estandar obligatorio. |
| MCP/API suena a solucion completa | La especificacion MCP define herramientas, recursos y mensajes; no define calidad del conocimiento subyacente. | MCP = puerta de acceso, no memoria. |

## Opciones o enfoques encontrados

| Opcion | Madurez | Ventajas | Limitaciones | Lectura para la charla |
|---|---|---|---|---|
| Fichas Markdown sueltas | Alta como practica simple | Baratas, legibles, versionables | Se dispersan, pierden vigencia, no fuerzan relaciones | Buen inicio, no destino |
| Wiki / Obsidian / GitHub Wiki | Alta como navegacion | Links, backlinks, grafo, edicion colaborativa | Puede volverse decorativa o inconsistente | Capa humana de descubrimiento |
| Catalogo de datos / dbt metadata | Alta en stack de datos | Lineage, tests, freshness, owners, docs tecnicas | Puede no capturar conocimiento operativo narrativo | Evidencia de que metadata importa |
| Knowledge repo | Media como patron organizacional | Une convenciones, revision, ownership y acceso | Requiere disciplina y mantenimiento | Tesis central de la charla |
| OKF / bundles agent-ready | Emergente | Portable, Git-diffable, frontmatter, links, MCP posible | No consolidado como estandar universal | Referencia futura y cautelosa |
| MCP/API sobre repo | Alta como protocolo emergente de acceso | Permite consultas acotadas por agentes | Depende de calidad y estructura del repo | Interfaz, no sustituto |

## Direccion narrativa sugerida

No es narrativa final ni build. Es direccion para `narrative-charlas`.

1. Kicker: `El problema no es escribir tablas`.
   Titulo con tesis: `Cuando las fichas crecen, documentar deja de ser redaccion y se vuelve arquitectura`.
   Objeto visible: carpeta con muchas fichas `.md` y una pregunta imposible de responder.
   Takeaway: el volumen cambia la naturaleza del problema.

2. Kicker: `Primer ladrillo`.
   Titulo con tesis: `Markdown hace el conocimiento revisable, pero no lo vuelve gobernado`.
   Objeto visible: ficha de tabla con campos faltantes.
   Takeaway: formato no equivale a memoria.

3. Kicker: `Navegacion humana`.
   Titulo con tesis: `Una wiki ayuda a encontrar, pero no decide que esta vigente`.
   Objeto visible: grafo de notas con nodos huerfanos y enlaces utiles.
   Takeaway: descubrimiento y gobierno son problemas distintos.

4. Kicker: `Contrato minimo`.
   Titulo con tesis: `El salto ocurre cuando cada ficha tiene owner, estado, relaciones y regla de revision`.
   Objeto visible: ficha de tabla con frontmatter y secciones obligatorias.
   Takeaway: el repo empieza cuando hay convencion mantenible.

5. Kicker: `Trabajo real de datos`.
   Titulo con tesis: `Los stacks de datos ya tratan ownership, lineage y freshness como metadata operacional`.
   Objeto visible: ejemplo dbt/source freshness o catalogo con owner/lineage.
   Takeaway: la documentacion tecnica madura como sistema de metadatos.

6. Kicker: `Agentes`.
   Titulo con tesis: `Un agente no necesita leer todo; necesita saber que fuente consultar y que relaciones seguir`.
   Objeto visible: consulta acotada: tabla -> metricas -> riesgos -> owner.
   Takeaway: memoria preparada reduce ambiguedad, no magia.

7. Kicker: `Interfaz`.
   Titulo con tesis: `MCP/API es la puerta, no la biblioteca`.
   Objeto visible: agente llamando `search`, `read`, `neighbors` contra repo.
   Takeaway: sin contrato de conocimiento, la interfaz solo expone desorden.

8. Kicker: `Referencia portable`.
   Titulo con tesis: `OKF muestra hacia donde va el patron: conocimiento legible por humanos y agentes`.
   Objeto visible: bundle Markdown con YAML frontmatter, links y validacion.
   Takeaway: usarlo como inspiracion, no como religion.

9. Kicker: `Decision`.
   Titulo con tesis: `La pregunta correcta no es que herramienta usar, sino que capa falta`.
   Objeto visible: stack de capas: formato, navegacion, gobierno, acceso.
   Takeaway: separar responsabilidades evita comprar o construir de mas.

10. Kicker: `Cierre`.
    Titulo con tesis: `El conocimiento que no se puede mantener tampoco se puede delegar a un agente`.
    Objeto visible: archivo vivo convertido en mapa operativo.
    Takeaway: preparar memoria es preparar autonomia.

## Claims a validar antes de cerrar la deck

- No afirmar que OKF es un estandar ampliamente adoptado. Mejor: `patron emergente` o `referencia portable`.
- No prometer reduccion cuantitativa de tokens, costo o tiempo sin evidencia propia.
- No afirmar que MCP garantiza trazabilidad; MCP permite exponer herramientas y recursos, pero la trazabilidad depende del diseno del servidor y del repo.
- No decir que wiki "no sirve"; decir que resuelve navegacion humana, no gobierno completo.
- Si se menciona un producto especifico, validar fecha, version y claim en la fuente primaria antes de ponerlo en slide.

## Riesgos y consideraciones

- Riesgo de hype: convertir `knowledge repo` en etiqueta nueva para documentacion vieja. Mitigacion: definir criterios observables.
- Riesgo de herramienta: que la charla parezca tutorial de Obsidian, GitHub Wiki, dbt, OKF o MCP. Mitigacion: cada uno ocupa una capa.
- Riesgo de abstraccion: la audiencia necesita un ejemplo conductor, idealmente una tabla de clientes o transacciones.
- Riesgo de sobreprometer agentes: un agente mejora si el conocimiento esta preparado; no compensa ausencia de ownership ni vigencia.
- Riesgo de duplicacion con catalogo: presentar el repo como contrato complementario, no como reemplazo universal.

## Recomendacion

Continuar a narrativa.

La tesis esta suficientemente validada si se formula como separacion de capas:

1. Markdown = formato.
2. Wiki = navegacion humana.
3. Knowledge repo = memoria operacional gobernada.
4. OKF = referencia portable para paquetes de conocimiento.
5. MCP/API = interfaz de acceso para agentes.

La charla debe evitar discutir RAG, embeddings, grafos y orquestacion salvo como teaser de una segunda parte.

## Cierre editorial propuesto

Mensaje final:

> Antes de pedirle memoria a un agente, hay que construir una memoria que el equipo pueda mantener.

Cita candidata real:

> "The overriding design goal for Markdown's formatting syntax is to make it as readable as possible."
> John Gruber, Markdown

Uso sugerido: no como cierre literal sobre Markdown, sino como contraste. Markdown nacio para legibilidad; el knowledge repo agrega responsabilidad, vigencia y acceso.

Metafora visual:

Una biblioteca tecnica en construccion: no una pila de documentos, sino estanterias con etiquetas, fichas de mantenimiento, pasillos conectados y una puerta de consulta para humanos/agentes. Debe sentirse editorial, sobria y deliberada, no dashboard ni diagrama.

## Donde profundizar despues

- Ejemplo concreto de ficha minima para una tabla: frontmatter, owner, dominio, fuente, SLA/freshness, columnas criticas, joins validos, riesgos, preguntas respondidas, relaciones.
- Relacion entre knowledge repo y catalogo de datos existente.
- Como exponer `search/read/neighbors` via MCP sin permitir que el agente modifique conocimiento sin revision humana.
- Charla 2: RAG, grafos, embeddings y recuperacion sobre knowledge repo.

## Self-review

- Confidence score: 0.78
- Weakest link: OKF como referencia actual; hay actividad reciente, pero adopcion y autoridad aun son heterogeneas.
- Bias check: hay sesgo hacia docs-as-code y Git; se mitiga al presentar catalogos y wikis como capas validas.
- Missing perspective: compliance/data governance formal en empresas reguladas; no profundizado porque esta fuera del alcance de la charla 1.
- What would change my mind: evidencia de que el equipo ya tiene un catalogo de datos con ownership, freshness, docs, busqueda y agentes integrados; en ese caso la charla deberia enfocarse en extension de catalogo, no en repo independiente.

## Fuentes consultadas

Ver `notes/bibliografia.md`.

## Artefactos para notes

- `notes/research-brief.md`
- `notes/bibliografia.md`
- `notes/agent-log.md`

## Nivel de confianza

Alto para la tesis central y la separacion de capas. Moderado para OKF como referencia, por madurez y adopcion todavia emergentes.

## Decision de continuidad

`seguir`
