# Caso Practico

## Caso elegido

Use el propio repo `charlas` como caso practico de `LLM Wiki`.

Fue la mejor eleccion por tres razones:

1. ya tiene `AGENTS.md`, `MEMORY.md`, `STYLE-CHARLAS.md` y backlog
2. tiene preguntas recurrentes que exigen continuidad entre sesiones
3. ya mezcla conocimiento estable, conocimiento cambiante y decisiones editoriales

## Lo que demuestra el caso

Este repo ya tiene memoria distribuida, pero todavia no tiene memoria compilada.

La diferencia es importante:

- memoria distribuida: reglas y decisiones viven en varios markdowns separados
- memoria compilada: una capa intermedia ya captura lo esencial, enlaza paginas y archiva respuestas reutilizables

## Estructura del demo

La demo vive en [demo-charlas](C:/Users/Victor/Proyectos/2026/charlas/Wiki%20LLM%20con%20Obsidian/demo-charlas).

Incluye:

- `WIKI-SCHEMA.md`
- `raw/source-manifest.md`
- `compiled/index.md`
- paginas de sistema y portfolio
- una query archivada de priorizacion

## Lo que cambia frente al modo "leer todo otra vez"

Sin wiki compilada, para contestar `que charla sigue?`, el agente debe releer:

- `IDEAS.md`
- `MEMORY.md`
- al menos un `README.md` de charla
- reglas de tono y narrativa

Con wiki compilada, puede entrar por:

- `index.md`
- `ideas-pendientes.md`
- `queries/que-charla-priorizar-despues.md`

Eso reduce dos costos:

1. costo de contexto
2. costo de reconstruccion mental

## El punto clave

La gran mejora no es solo `faster retrieval`.

La gran mejora es que la wiki:

- conserva decisiones
- conecta paginas
- deja respuestas de alta reutilizacion
- marca donde hay drift o falta de evidencia

## Limites observados

- si nadie mantiene `source_refs`, la wiki se vuelve decorativa
- si todo entra, la wiki se vuelve otro dump
- si no se distingue `hecho verificado` de `interpretacion`, la memoria se contamina
- si no hay staleness control, la wiki envejece sin avisar

## Conclusiones del caso

1. el patron si aterriza bien a un repo pequeno y real
2. `Obsidian` no es la tesis; la tesis es `conocimiento compilado`
3. la capa mas convincente para la charla no es la query, sino la separacion `raw -> compiled -> query filed`
4. el caso conecta muy bien con tu intuicion sobre decisiones, intentos fallidos, memoria de analisis y continuidad del trabajo
