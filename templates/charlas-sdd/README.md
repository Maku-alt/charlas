# Charlas SDD

Templates para Web Talks con fases acotadas: `thesis-review -> research? -> narrative -> build -> review -> build-fix? -> review-final? -> release`.

## Modos

Usa `full/` para tesis incierta, research externo, audiencia importante o riesgo alto. Usa `compact/` cuando la tesis y la narrativa ya estan claras. Ambos modos exigen worker y reviewer distintos, identidad de candidato, SHA256 y evidencia reproducible.

## Paquete de fase

Cada worker recibe rol Markdown, custom agent TOML, spec, prompt, inputs exactos, outputs permitidos, criterios, runtime y `fork_context: false`. El spec define el encargo; el rol define metodo y calidad; el TOML hace seleccionable al agente y fija runtime.

## Build web

`experience-designer-builder-charlas` usa `impeccable`, construye directamente frontend y absorbe diseño, apertura, cierre, imagenes y QA. No existe fase `image-close`. La PPTX no es intermediario.

Build entrega HTML, fuente, renders individuales, tests, self-audit, hash y `phase-summary.md`. Review repite gates criticos sobre el hash exacto sin modificarlo.

## Publicacion

El contrato vive en `agents/workflow-contract.json`. El worker publica `notes/phase-summary.md` y el sentinel al final mediante los scripts de `scripts/agent_workflow/`. Release promueve exclusivamente el candidato aprobado por review o review-final.

## Legado

Charlas cerradas en PPTX permanecen historicas. Cuando se reabren para una nueva version, usan el workflow Web Talk vigente. `scripts/deck_renderer/` queda para mantenimiento de artefactos antiguos.
