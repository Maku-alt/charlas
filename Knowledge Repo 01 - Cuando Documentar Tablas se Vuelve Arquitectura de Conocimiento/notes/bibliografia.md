# Bibliografia

## Fuentes principales

1. Google Cloud Blog. "Introducing the Open Knowledge Format." 2026-06-12. https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
   - Uso: fuente principal para OKF, fecha de anuncio, motivacion, bundles Markdown + YAML frontmatter y posicionamiento como formato, no plataforma.
   - Nota: fuente de proveedor; usar con cuidado para no sobredimensionar adopcion o madurez.

2. GoogleCloudPlatform / knowledge-catalog. "Open Knowledge Format (OKF) SPEC.md." Version 0.1, Draft. https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
   - Uso: fuente primaria para definicion de OKF, estructura de bundle, concept documents, fields, links, citations, goals y non-goals.
   - Hallazgo clave: OKF no prescribe storage, serving, query infrastructure ni reemplaza schemas de dominio.

3. Model Context Protocol. "Specification 2025-06-18." https://modelcontextprotocol.io/specification/2025-06-18
   - Uso: fuente primaria para definir MCP como protocolo de integracion entre hosts, clients y servers, con resources, prompts y tools.
   - Lectura para la charla: MCP expone contexto y capacidades; no sustituye la memoria gobernada.

4. Anthropic. "Introducing the Model Context Protocol." 2024-11-25. https://www.anthropic.com/news/model-context-protocol
   - Uso: origen publico de MCP y framing como estandar abierto para conectar asistentes con sistemas donde vive la data.
   - Nota: fuente de creador/proveedor; usar para origen y motivacion, no como prueba unica de adopcion.

5. DataHub Docs. "The Metadata Model." https://docs.datahub.com/docs/metadata-modeling/metadata-model
   - Uso: evidencia conceptual de modelado de metadata: entidades, aspectos, browse paths, ownership, descriptions, tags, glossary terms y versioned aspects.
   - Lectura para la charla: el conocimiento de datos escala como entidad + relaciones + aspectos, no como texto aislado.

6. OpenMetadata Docs. "Overview of Data Assets." Version v1.12.x. https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/data-asset-tabs
   - Uso: evidencia de que una vista de activo de datos incluye owner, tier, usage, description, schema, tasks, sample data, queries, profiler, lineage, custom properties y version history.
   - Lectura para la charla: una ficha de tabla util debe mirar mas alla de columnas.

7. OpenMetadata Docs. "Glossary | OpenMetadata Data Glossary Guide." Version v1.12.x. https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary
   - Uso: soporte para glosarios como vocabulario controlado, etiquetado de activos, descubrimiento, recuperacion, exploracion y gobierno.
   - Lectura para la charla: definiciones de negocio son metadata relacional, no solo texto de soporte.

8. dbt Developer Hub. "Add Exposures to your DAG." Version v2.0. https://docs.getdbt.com/docs/build/exposures
   - Uso: ejemplo de metadata como codigo para downstream uses: dashboards, aplicaciones y data science pipelines.
   - Lectura para la charla: los consumidores y usos tambien son parte del contexto operacional de una tabla/modelo.

9. Obsidian Help. "Internal links." https://obsidian.md/help/links
   - Uso: evidencia sobre links internos y redes de conocimiento en wikis/segundos cerebros basados en notas.
   - Lectura para la charla: navegacion humana es una capa real, pero distinta de gobierno y vigencia.

10. CommonMark. "What is Markdown?" https://commonmark.org/
    - Uso: definicion base de Markdown como formato de texto plano para documentos estructurados.
    - Lectura para la charla: Markdown es excelente como formato portable, pero no define por si mismo arquitectura de conocimiento.

11. GitHub Docs. "Basic writing and formatting syntax." https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
    - Uso: evidencia practica de Markdown como formato comun en repositorios y flujos GitHub.
    - Lectura para la charla: versionar docs junto a codigo es natural, pero requiere convenciones adicionales.

12. Diataxis. "Diataxis." https://diataxis.fr/
    - Uso: referencia secundaria para separar tipos de documentacion por necesidad del usuario.
    - Lectura para la charla: ayuda a evitar mezclar referencia, explicacion y guia dentro de una sola ficha larga.

## Claims verificados y nivel de evidencia

| Claim | Evidencia | Nivel |
|---|---|---|
| Markdown es portable y legible, pero no define ownership, vigencia ni relaciones | CommonMark, GitHub Docs; inferencia desde ausencia de esos conceptos en el formato | Alto para formato, medio para limite operacional |
| Wiki/segundo cerebro mejora navegacion humana | Obsidian Help sobre links internos y red de conocimiento | Alto |
| Wiki no equivale automaticamente a gobierno | Inferencia a partir de que links no cubren owner, vigencia, revision ni autoridad | Medio |
| Metadata de datos es relacional y gobernada | DataHub, OpenMetadata, dbt Exposures | Alto |
| OKF es emergente y debe presentarse como draft v0.1 | Google Cloud Blog y OKF SPEC.md | Alto |
| OKF no reemplaza schemas ni infraestructura de query/serving | OKF SPEC.md non-goals | Alto |
| MCP es interfaz para contexto, tools y resources, no memoria | MCP Specification y Anthropic announcement | Alto |

## Claims que no deben afirmarse sin evidencia propia

- Reduccion cuantitativa de costos, tokens o tiempo por usar knowledge repo.
- Adopcion amplia de OKF fuera del ecosistema inicial.
- Que MCP sea suficiente para resolver calidad del conocimiento.
- Que una wiki simple fracase siempre.
- Que un knowledge repo reemplace un catalogo de datos corporativo.
