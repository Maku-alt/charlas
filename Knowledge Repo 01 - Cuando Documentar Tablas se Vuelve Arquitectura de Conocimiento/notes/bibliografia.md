# Bibliografia

Esta bibliografia corresponde a una nueva corrida de research desde cero ejecutada el 2026-06-28. No reutiliza briefs anteriores.

## Fuentes primarias u oficiales

1. CommonMark. `CommonMark Spec`, version 0.31.2, 2024-01-28.
   URL: https://spec.commonmark.org/0.31.2/
   Uso: sustentar que Markdown es formato de texto estructurado y legible, no un sistema completo de gobierno de conocimiento.
   Lectura critica: fuente primaria del formato; no habla de ownership, freshness, lineage ni procesos de mantenimiento.

2. John Gruber. `Markdown`.
   URL: https://daringfireball.net/projects/markdown/
   Uso: cita candidata sobre legibilidad como objetivo de Markdown.
   Lectura critica: fuente historica del formato; util para framing, no para claims sobre arquitectura de conocimiento.

3. GitHub Docs. `About wikis`.
   URL: https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis
   Uso: sustentar que una wiki sirve para alojar documentacion de repositorios, editar contenido y permitir colaboracion, pero no implica por si misma gobierno operacional.
   Lectura critica: fuente oficial de GitHub; sesgo hacia capacidades de GitHub.

4. Obsidian Help. `Internal links`.
   URL: https://help.obsidian.md/links
   Uso: sustentar links internos, notas conectadas y red de conocimiento como capa de navegacion humana.
   Lectura critica: fuente oficial de producto; fuerte para navegacion, no para gobierno de datos.

5. Obsidian Help. `Graph view`.
   URL: https://help.obsidian.md/plugins/graph
   Uso: sustentar visualizacion de relaciones entre notas mediante nodos y links.
   Lectura critica: fuente oficial de producto; no equivale a metadata operacional.

6. dbt Labs Docs. `Add sources to your DAG`.
   URL: https://docs.getdbt.com/docs/build/sources
   Uso: evidencia concreta de que equipos de datos documentan fuentes, describen tablas/columnas, crean dependencias/lineage, testean supuestos y calculan freshness.
   Lectura critica: fuente oficial de dbt; sesgo hacia ecosistema dbt, pero muy pertinente para equipos de datos.

7. DataHub Project. `Ownership.pdl`.
   URL: https://github.com/datahub-project/datahub/blob/master/metadata-models/src/main/pegasus/com/linkedin/common/Ownership.pdl
   Uso: evidencia primaria de que plataformas de metadata modelan ownership como aspecto de entidades y registran `lastModified`.
   Lectura critica: fuente de codigo del proyecto; util para probar que ownership es metadata operacional, no solo texto.

8. Model Context Protocol. `Specification - Overview`.
   URL: https://modelcontextprotocol.io/specification/draft/basic
   Uso: sustentar que MCP separa protocolo, server features, tools, resources y mensajes; sirve como interfaz de acceso, no como memoria de conocimiento.
   Lectura critica: especificacion primaria; cambia con versiones, validar antes de claims definitivos.

9. Model Context Protocol. `Server Features - Tools`.
   URL: https://modelcontextprotocol.io/specification/draft/server/tools
   Uso: sustentar que MCP permite exponer herramientas invocables por modelos, con schemas, resultados y consideraciones de seguridad/human-in-the-loop.
   Lectura critica: fuente primaria; no define calidad ni gobierno del contenido consultado.

## Fuentes sobre OKF y ecosistema emergente

10. GoogleCloudPlatform. `knowledge-catalog / okf`.
    URL: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
    Uso: referencia principal para Open Knowledge Format cuando este disponible. Debe revisarse directamente antes de usar claims especificos en slides.
    Lectura critica: se trato como fuente primaria esperada; validar contenido puntual antes de deck final.

11. OWOX. `OWOX Model Canvas`.
    URL: https://github.com/OWOX/owox-model-canvas
    Uso: ejemplo actual de herramienta que lee/escribe OKF, describe data marts como nodos, relaciones como edges y exporta bundles Markdown con YAML frontmatter.
    Lectura critica: proyecto de proveedor; util como evidencia de implementacion, no como prueba de adopcion general.

12. OKFy. `Open Knowledge Format for AI agents`.
    URL: https://github.com/0dust/OKFy
    Uso: ejemplo actual de OKF aplicado a bundles agent-readable con frontmatter, links, backlinks, fuente, freshness local y MCP read-only.
    Lectura critica: proyecto comunitario reciente; fuerte para mostrar patron emergente, debil para claims de madurez.

## Fuentes complementarias a validar si entran en deck

13. OpenMetadata Docs. `Table entity / metadata schemas`.
    URL: https://docs.open-metadata.org/
    Uso potencial: ownership, columns, lineage, glossary y metadata operacional en catalogos de datos.
    Estado: consulta web parcial tuvo problemas de conexion; validar de nuevo antes de usar en slide.

14. DataHub Docs. `Metadata model / dataset concepts`.
    URL: https://datahubproject.io/docs/
    Uso potencial: completar ejemplos de ownership, lineage, glossary y dataset metadata desde docs narrativas.
    Estado: se uso una fuente primaria de codigo para ownership; validar docs narrativas si se quiere citar en slide.
