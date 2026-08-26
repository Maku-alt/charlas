# Charlas

Repositorio de Web Talks tecnicas sobre datos, Data Science, IA aplicada, tooling y arquitectura.

## Producto

El entregable canonico es una experiencia frontend autocontenida y lista para presentar. Puede combinar escenas editoriales, datos, simulaciones, comparadores, demos e imagenes; no se limita a reproducir slides dentro de HTML.

PPTX es un artefacto historico o una exportacion opcional cuando el usuario la pide.

Documentos principales:

- `PRODUCT.md`: proposito, usuarios y contrato del producto.
- `DESIGN.md`: firma editorial y principios de experiencia sin imponer un tema visual.
- `AGENTS.md`: reglas persistentes del repositorio.
- `skills/charlas-workflow/SKILL.md`: workflow operativo para nuevas charlas.
- `maestro_charlas.md`: indice de charlas y entregables.

## Workflow 5.6

```text
Brief -> Research -> Narrative -> Build <-> Review -> Release
```

Research y `notes/bibliografia.md` son obligatorios. Narrative define la tesis, el arco, los momentos y el speech sin una cuota fija: usa la extension minima que sirva al argumento y propone una serie cuando un tema contiene varios arcos.

Build usa `impeccable`, diseña y construye directamente el frontend, integra imagenes e interaccion, genera renders y ejecuta QA. Review es independiente y read-only. Release promueve el mismo SHA-256 aprobado.

El workflow 5.6 usa artefactos reales como estado y handoffs nativos compactos. No crea execution packages, phase summaries, sentinels, snapshots ni manifests de corrida.

## Estructura recomendada por charla

```text
<charla>/
|-- notes/
|   |-- research.md
|   |-- bibliografia.md
|   |-- narrativa.md
|   `-- speech.md
|-- web/ o talk/
|-- assets/
|-- review/
|   |-- renders/
|   `-- report.md
`-- release/
```

La forma exacta puede adaptarse al proyecto; importa preservar research verificable, narrativa aprobada, fuente frontend, evidencia final y el candidato liberado.

Las charlas historicas no se migran hasta que se reabran. Los scripts PPTX y la infraestructura SDD anterior no gobiernan nuevas ejecuciones.
