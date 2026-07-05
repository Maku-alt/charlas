# Worker Package: Image Close

## Objetivo

Ejecutar la fase `image-close` para la corrida `knowledge-repo-01-full-rebuild-20260704`.

Debes definir y producir la imagen editorial de cierre para la slide final de la charla. No construyas PPTX.

## Contexto minimo

Repositorio: `C:\Users\Victor\Proyectos\2026\charlas`

Carpeta de charla: `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`

Run id: `knowledge-repo-01-full-rebuild-20260704`

## Archivos a leer

- `AGENTS.md`
- `agents/image-closer-charlas.md`
- `templates/charlas-sdd/prompts/run-image-close.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/narrative-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/build-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/narrative-brief.md`

No leas decks ni reviews anteriores.

## Direccion visual

La imagen final no debe repetir tablas, bullets ni diagramas. Debe amplificar el cierre y sentirse editorial, deliberada y distinta.

Mensaje final:

`La documentacion que escala no guarda paginas: conserva decisiones reutilizables.`

Direccion sugerida:

Archivo editorial vivo o mesa de trabajo sobria con tarjetas de datos, notas curadas y caminos de luz sutiles entre tablas, metricas, owners y decisiones. Debe dejar aire para texto sobrepuesto y evitar robots, dashboards, grafos tecnicos y wallpaper generico.

## Salidas obligatorias

Escribe:

- `notes/image-close-brief.md`
- imagen bitmap final en `assets/closing-knowledge-repo.png`
- `notes/phase-summary.md`
- `review/knowledge-repo-01-full-rebuild-20260704/telemetry/image-usage-summary.json`
- sentinel: `notes/.phase-image.done`

Si no puedes generar imagen, escribe un brief completo y marca bloqueado o requiere cambios. No uses una imagen floja como si estuviera aprobada.

## Summary minimo

`notes/phase-summary.md` debe decir:

- Ultima fase: `image-close`
- Estado: `completado`, `requiere cambios` o `bloqueado`
- Pasa / no pasa
- Resumen de 1-3 frases
- Artefactos
- Hallazgos bloqueantes
- Siguiente accion: lanzar build si pasa

Telemetry JSON minimo:

```json
{
  "run_id": "knowledge-repo-01-full-rebuild-20260704",
  "phase": "image-close",
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
  "sentinel": "notes/.phase-image.done",
  "status": "done|blocked"
}
```

Si no puedes obtener tokens o JSONL real, deja esos campos en `null` o `""`; no inventes medicion.

## Reglas

- Escribe `notes/phase-summary.md` antes del sentinel.
- Escribe el sentinel al final.
- No pegues logs completos en ningun summary.
- No construyas PPTX.
- Respuesta final del worker en chat: solo `DONE: summary written` o `BLOCKED: summary written`.
