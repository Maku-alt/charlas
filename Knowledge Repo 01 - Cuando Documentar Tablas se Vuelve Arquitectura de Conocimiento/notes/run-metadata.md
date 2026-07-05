# Run Metadata

Run id: `knowledge-repo-01-full-rebuild-20260704`

Objetivo: reconstruir desde cero la charla `Knowledge Repo 01` y entregar un PPTX final editable, usando workers, handoff por disco, PowerPoint nativo como gate final y auditoria posterior de flujo/tokens.

Artefacto final esperado: `Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`

Reglas de la corrida:

- El padre no lee chats ni logs de workers.
- Cada worker escribe `notes/phase-summary.md` antes de su sentinel.
- El sentinel se escribe al final.
- Evidencia pesada queda en `review/`, `slides/` o `assets/`.
- Build de PPTX nuevo usa Presentations / `@oai/artifact-tool`; no usa `pptxgenjs`.
- Review no corrige el deck; solo reporta hallazgos accionables.
- Se permite maximo un ciclo `review -> build-fix -> review-final`.
