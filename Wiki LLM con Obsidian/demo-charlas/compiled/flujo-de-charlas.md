---
type: system
status: active
source_refs:
  - ../../AGENTS.md
  - ../../MEMORY.md
  - ../../STYLE-CHARLAS.md
last_compiled: 2026-06-05
---

# Flujo De Charlas

## Resumen ejecutivo

El repo ya define una cadena de trabajo bastante precisa:

`orquestar -> investigar -> construir deck -> resolver cierre visual -> revisar`

## Hechos verificados

- el flujo especializado incluye `orchestrator-charlas`, `researcher-charlas`, `deck-builder-charlas`, `image-closer-charlas` y `review-charlas`
- no todo hallazgo de research debe entrar a la PPT
- el cierre visual es una responsabilidad distinta del armado de slides
- el review debe ocurrir sobre una deck construida, no sobre ideas abiertas
- la charla debe cerrar con una frase breve, una sintesis y una imagen editorial

## Interpretacion

Si un agente volviera a leer estos documentos desde cero cada vez, gastaria contexto en redescubrir:

- en que fase esta la charla
- que agente sigue
- que material es soporte y que material ya es mensaje

Una pagina compilada reduce ese costo y evita mezclar flujo operativo con detalle textual disperso.

## Riesgo de drift

Si cambia el orden del flujo o los nombres de agentes, esta pagina debe recompilarse.

## Paginas relacionadas

- [[repo-charlas]]
- [[portafolio-de-charlas]]
- [[harness-engineer]]
