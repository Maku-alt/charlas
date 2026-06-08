# Wiki Schema

## Proposito

Esta wiki compila conocimiento operativo de un repo de charlas. No reemplaza los archivos fuente. Los resume, conecta y vuelve consultables.

## Reglas base

1. `raw/` es inmutable salvo metadatos de ingest.
2. `compiled/` es propiedad de la wiki.
3. Toda pagina compilada debe declarar `source_refs`.
4. Toda pagina compilada debe incluir:
   - resumen ejecutivo
   - hechos verificados
   - interpretacion
   - links salientes a otras paginas
5. Las respuestas reutilizables viven en `compiled/queries/`.
6. Las afirmaciones no soportadas deben marcarse como `hipotesis`.

## Tipos de pagina

### `system`

Describe estructura, reglas, workflow o arquitectura del repo.

Campos:

```yaml
type: system
status: active
source_refs: []
last_compiled: YYYY-MM-DD
```

### `talk`

Describe una charla ya existente o una charla candidata madura.

Campos:

```yaml
type: talk
status: active
source_refs: []
last_compiled: YYYY-MM-DD
```

### `backlog`

Agrupa ideas, tensiones y prioridades.

Campos:

```yaml
type: backlog
status: active
source_refs: []
last_compiled: YYYY-MM-DD
```

### `query`

Respuesta archivada a una pregunta que puede reutilizarse.

Campos:

```yaml
type: query
status: filed
source_refs: []
last_compiled: YYYY-MM-DD
```

## Regla de compilacion

La wiki no debe copiar todo el documento fuente. Debe:

- extraer decisiones estables
- separar hecho de interpretacion
- enlazar entidades y sistemas relacionados
- evitar repetir ruido transitorio

## Regla de staleness

Una pagina se considera potencialmente stale si:

- cambia un archivo en `source_refs`
- aparece una nueva charla o una idea nueva que la contradice
- cambia el flujo oficial del repo
