# Thesis Spec

## Tema

De fichas de tablas en Markdown a una arquitectura de conocimiento para equipos de datos.

## Audiencia

Equipo data mixto:

- Data Scientists que trabajan con tablas, notebooks, features, metricas y conocimiento operativo.
- Analistas que consumen y documentan fuentes de datos para responder preguntas de negocio.
- Data engineers o analytics engineers que entienden lineage, ownership, calidad y convenciones de datos.
- Lideres tecnicos que necesitan escalar conocimiento sin depender solo de expertos individuales.

## Problema

El equipo trabaja con muchas tablas y cada persona conoce una parte distinta del contexto: que contiene cada tabla, para que se usa, que columnas importan, que riesgos tiene, con que otras tablas se cruza y que dudas ya fueron resueltas antes.

La solucion inicial parece sencilla: crear un archivo `.md` por tabla con descripcion, diccionario y usos. Pero cuando el numero de fichas crece, aparecen nuevos problemas:

- las fichas quedan dispersas;
- no queda claro cual es la version vigente;
- no hay navegacion entre tablas, metricas, dominios y casos de uso;
- el conocimiento sigue dependiendo de personas;
- un agente tendria que leer demasiados archivos para reconstruir contexto;
- una wiki visual puede ayudar a humanos, pero no necesariamente define gobierno ni consulta operacional.

## Tesis central

Cuando un equipo documenta muchas tablas, no necesita solo mas documentacion. Necesita convertir ese conocimiento operativo en una memoria comun, navegable, versionada y preparada para consulta por agentes.

Formulacion breve:

> Documentar tablas se vuelve arquitectura de conocimiento cuando el equipo necesita conectar, mantener y consultar lo que sabe.

## Cambio esperado

La audiencia debe salir con un mapa mental claro:

- Antes: "hagamos un `.md` por tabla".
- Despues: "definamos que capa cumple cada rol: formato, navegacion, gobierno, acceso para agentes y evolucion futura".

Tambien debe poder distinguir:

- `Markdown` como formato portable y versionable.
- `Wiki` o segundo cerebro como navegacion humana.
- `Knowledge repo` como memoria operacional gobernada.
- `OKF` como referencia de convencion portable.
- `MCP/API` como interfaz de acceso para agentes.

## Fuera de alcance

- Profundizar en RAG, embeddings o grafos.
- Comparar vector stores, bases de grafos o frameworks de orquestacion.
- Explicar LangGraph.
- Hacer tutorial de Obsidian o comparar plugins.
- Definir un estandar corporativo final de documentacion de datos.
- Prometer ahorro cuantitativo de tokens, tiempo o costo sin evidencia propia.
- Crear el deck o construir una demo tecnica en esta fase.

RAG y grafos solo aparecen como teaser final hacia la segunda charla de la serie.

## Tradeoff central

Documentacion simple versus memoria operacional:

- Fichas Markdown sueltas: baratas, faciles de escribir y versionables, pero escalan mal si no tienen estructura, enlaces y reglas de mantenimiento.
- Wiki o segundo cerebro: mejora navegacion humana y descubrimiento, pero puede volverse decorativa si no tiene fuente de verdad, ownership y control de vigencia.
- Knowledge repo: exige convenciones, metadata, revision y mantenimiento, pero permite que el conocimiento sea gobernado, reutilizable y consultable por agentes.

La charla no plantea que Markdown o wiki sean insuficientes. Plantea que son capas necesarias, pero no equivalen por si solas a una arquitectura de conocimiento.

## Riesgos de framing

- Que suene a "Markdown no sirve". Mitigacion: presentarlo como el primer ladrillo correcto, no como el sistema completo.
- Que suene a "hay que comprar una herramienta". Mitigacion: insistir en capas y responsabilidades antes que productos.
- Que se mezcle con RAG/grafos. Mitigacion: dejar esos temas como segunda charla y tratarlos solo como puerta futura.
- Que parezca una charla abstracta de arquitectura. Mitigacion: usar una tabla de clientes como ejemplo conductor.
- Que parezca una charla de Obsidian. Mitigacion: tratar Obsidian/segundo cerebro como referencia de navegacion humana, no como destino obligatorio.

## Decision de continuidad

- seguir
