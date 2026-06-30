# Research Launch Package

## Fase
`research`

## Charla
`Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`

## Rol especializado
`researcher-charlas`

Archivo:
`C:\Users\Victor\Proyectos\2026\charlas\agents\researcher-charlas.md`

## Parametros de launch
- `model`: `gpt-5.5`
- `reasoning_effort`: `medium`
- `fork_context`: `false`

## Insumos minimos
- `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento\specs\thesis-spec.md`
- `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento\specs\research-spec.md`
- `C:\Users\Victor\Proyectos\2026\charlas\templates\charlas-sdd\prompts\run-research.md`
- `C:\Users\Victor\Proyectos\2026\charlas\AGENTS.md`
- `C:\Users\Victor\Proyectos\2026\charlas\STYLE-CHARLAS.md`

## Objetivo operativo
Validar y refinar el angulo aprobado:

> definir que es un `knowledge repo` y por que importa como paso evolutivo entre fichas Markdown sueltas y una memoria operacional util para humanos y agentes.

## Foco de investigacion
- distinguir con precision `Markdown`, `wiki`, `knowledge repo`, `OKF` y `MCP/API`
- sostener por que `knowledge repo` no es solo documentacion con otro nombre
- mantener la charla agnostica de herramienta y evitar convertirla en tutorial
- reservar `RAG`, grafos y orquestacion como teaser de la charla 2
- bajar el argumento al trabajo real de equipos de datos con tablas, ownership, relaciones, vigencia y consulta por agentes

## Claims que deben salir validados o debilitados
- `Markdown` sirve como formato portable y versionable, pero no resuelve por si solo gobierno, relaciones ni vigencia
- una `wiki` mejora navegacion humana, pero no equivale automaticamente a memoria operacional gobernada
- un `knowledge repo` requiere convenciones, metadata, ownership, historial y mantenimiento
- `MCP/API` es interfaz de acceso para agentes sobre conocimiento preparado, no sustituto de la memoria
- `OKF` o formatos cercanos pueden servir como referencia portable, pero no reemplazan la arquitectura de conocimiento

## Prompt de launch
Usa el rol `researcher-charlas` con estos insumos:

- `thesis-spec.md`
- `research-spec.md`
- `run-research.md`
- `AGENTS.md`
- `STYLE-CHARLAS.md`

Ejecuta solo la fase `research` para la charla `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`.

Parametros obligatorios:
- `model: gpt-5.5`
- `reasoning_effort: medium`
- `fork_context: false`

No construyas slides ni hagas build. No cierres narrativa final slide by slide.

Objetivo:
refinar y validar la tesis de que un `knowledge repo` importa porque transforma fichas Markdown dispersas en memoria operacional navegable, versionada y consultable por humanos y agentes.

Puntos obligatorios a resolver:
- diferencia entre `Markdown`, `wiki`, `knowledge repo`, `OKF` y `MCP/API`
- que evidencia sostiene que documentar tablas se vuelve problema de arquitectura de conocimiento
- que contraargumentos razonables debilitan la tesis
- que claims quedan listos para deck y cuales necesitan cautela
- como cerrar sin contaminar la charla con `RAG`, grafos u orquestacion avanzada

Devuelve exactamente:
- tesis refinada
- hallazgos que si merecen slide
- contradicciones
- claims pendientes
- direccion de cierre
- fuentes consultadas
- decision de continuidad: `seguir`, `reformular`, `profundizar` o `descartar`

## Salida esperada
Un brief de research compacto y discutible que deje la charla lista para pasar a `narrative-charlas`, o que explicite por que todavia no conviene avanzar.
