# Worker Package: Build

## Objetivo

Ejecutar la fase `build` para la corrida `knowledge-repo-01-full-rebuild-20260704`.

Debes construir desde cero un PPTX editable de 9 slides para `Knowledge Repo 01`, usando la skill Presentations / `@oai/artifact-tool`.

## Contexto minimo

Repositorio: `C:\Users\Victor\Proyectos\2026\charlas`

Carpeta de charla: `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`

Run id: `knowledge-repo-01-full-rebuild-20260704`

PPTX final/candidato esperado:

`Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`

## Archivos a leer

- `AGENTS.md`
- `STYLE-CHARLAS.md`
- `agents/deck-builder-charlas.md`
- `templates/charlas-sdd/prompts/run-build.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/narrative-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/build-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/narrative-brief.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/research-brief.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/bibliografia.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/image-close-brief.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/assets/closing-knowledge-repo.png`

No leas decks ni review outputs anteriores.

## Requisitos de implementacion

- Debes usar la skill Presentations y su runtime `@oai/artifact-tool`.
- No uses `pptxgenjs`.
- No uses `python-pptx` para construir el deck.
- El PPTX debe ser editable en PowerPoint.
- Usa scratch fuera del repo para archivos temporales si la skill lo indica; solo deja entregables/evidencia en la carpeta de la charla.
- Mantener tildes y signos correctos.
- Una tesis por slide.
- Cada slide debe tener objeto visual dominante; evitar una sucesion plana de cajas.
- La slide final debe usar `assets/closing-knowledge-repo.png` sin sobrecargarla.

## Evidencia obligatoria

Escribe:

- PPTX candidato/final en la ruta esperada.
- `review/build-report.md`
- renders individuales en `review/renders/`
- contact sheet en `review/contact-sheet.png`
- render nativo PowerPoint y contact sheet nativo si PowerPoint esta disponible, por ejemplo en `review/native-renders/` y `review/native-contact-sheet.png`
- texto extraido en `review/extracted-text.txt`
- `notes/phase-summary.md`
- `review/knowledge-repo-01-full-rebuild-20260704/telemetry/build-usage-summary.json`
- sentinel: `notes/.phase-build.done`

Si PowerPoint nativo falla, haz maximo un intento acotado de fix. Si persiste, marca bloqueado en `notes/phase-summary.md`; no apruebes solo por LibreOffice/Poppler.

## Summary minimo

`notes/phase-summary.md` debe decir:

- Ultima fase: `build`
- Estado: `completado`, `requiere cambios` o `bloqueado`
- Pasa / no pasa
- Resumen de 1-3 frases
- Artefactos, incluyendo PPTX candidato actual
- Hallazgos bloqueantes
- Siguiente accion: lanzar review si pasa

Telemetry JSON minimo:

```json
{
  "run_id": "knowledge-repo-01-full-rebuild-20260704",
  "phase": "build",
  "thread_id": "",
  "session_jsonl": "",
  "started_at": "",
  "completed_at": "",
  "total_tokens": null,
  "input_tokens": null,
  "cached_input_tokens": null,
  "output_tokens": null,
  "function_calls": {},
  "artifacts": [],
  "sentinel": "notes/.phase-build.done",
  "status": "done|blocked"
}
```

Si no puedes obtener tokens o JSONL real, deja esos campos en `null` o `""`; no inventes medicion.

## Reglas

- Escribe `notes/phase-summary.md` antes del sentinel.
- Escribe el sentinel al final.
- No pegues logs completos en ningun summary.
- Respuesta final del worker en chat: solo `DONE: summary written` o `BLOCKED: summary written`.
