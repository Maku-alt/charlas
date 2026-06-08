# Demo Charlas Wiki

Este directorio contiene un caso practico de `wiki LLM` aplicado al repo `charlas`.

No es una implementacion automatizada. Es una demo deliberada para mostrar:

- que fuentes entran al sistema
- como se separa `raw/` de `compiled/`
- que tipo de paginas produce la compilacion
- como se responderia una pregunta reusable
- donde aparecen drift, proveniencia y mantenimiento

## Objetivo del demo

Probar la tesis en un repo pequeno y real:

`El valor no viene de volver a leer todos los markdowns en cada turno, sino de mantener una capa compilada de conocimiento que capture estructura, decisiones, relaciones y consultas utiles.`

## Alcance

Fuentes usadas:

- `AGENTS.md`
- `MEMORY.md`
- `IDEAS.md`
- `README.md`
- `STYLE-CHARLAS.md`
- `Harness Engineer/README.md`

## Estructura

- `raw/`: catalogo de fuentes y notas de ingest
- `compiled/`: paginas que la wiki ya consolidaria
- `WIKI-SCHEMA.md`: contrato operativo de la wiki

## Como leer este demo

1. empezar por `WIKI-SCHEMA.md`
2. revisar `raw/source-manifest.md`
3. abrir `compiled/index.md`
4. seguir con las paginas de sistema y de portfolio
5. terminar en `compiled/queries/que-charla-priorizar-despues.md`
