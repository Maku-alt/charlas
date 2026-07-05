# Worker Package: Review Final

## Objetivo

Ejecutar `review-final` para la corrida `knowledge-repo-01-full-rebuild-20260704`.

Debes validar el PPTX corregido despues de `build-fix`. No corrijas el deck.

## Contexto minimo

Repositorio: `C:\Users\Victor\Proyectos\2026\charlas`

Carpeta de charla: `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`

Run id: `knowledge-repo-01-full-rebuild-20260704`

PPTX candidato corregido:

`Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`

## Archivos a leer

- `AGENTS.md`
- `agents/review-charlas.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/review-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/review-report.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/build-fix-report.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/extracted-text.txt`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/native-contact-sheet.png`

Solo abre slides individuales si hace falta verificar los hallazgos corregidos o si el contact sheet muestra defecto. No leas chats ni artefactos antiguos.

## Alcance

Validar:

- 9 slides.
- PowerPoint nativo abre/exporta el PPTX corregido.
- Los P2 de tildes/caracteres especiales fueron corregidos.
- Slide 3 ya no tiene mojibake en signos de apertura de pregunta.
- No se introdujo overflow, solapamiento visible o defecto nuevo por la correccion.
- Slides 5, 7 y 9 siguen aceptables.

No abras un nuevo ciclo de fix. Si `review-final` no pasa, registra bloqueo explicito.

## Salidas obligatorias

Escribe:

- `review/final-review-report.md`
- `notes/phase-summary.md`
- `review/knowledge-repo-01-full-rebuild-20260704/telemetry/review-final-usage-summary.json`
- sentinel: `notes/.phase-review-final.done`

## Summary minimo

`notes/phase-summary.md` debe decir:

- Ultima fase: `review-final`
- Estado: `completado`, `requiere cambios` o `bloqueado`
- Pasa / no pasa
- Resumen de 1-3 frases
- Artefactos, incluyendo PPTX final si pasa
- Hallazgos bloqueantes
- Siguiente accion: cierre si pasa; bloqueo si no pasa

Telemetry JSON minimo:

```json
{
  "run_id": "knowledge-repo-01-full-rebuild-20260704",
  "phase": "review-final",
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
  "sentinel": "notes/.phase-review-final.done",
  "status": "done|blocked"
}
```

Si no puedes obtener tokens o JSONL real, deja esos campos en `null` o `""`; no inventes medicion.

## Reglas

- Escribe `notes/phase-summary.md` antes del sentinel.
- Escribe el sentinel al final.
- No pegues logs completos en ningun summary.
- No corrijas el PPTX.
- Respuesta final del worker en chat: solo `DONE: summary written` o `BLOCKED: summary written`.
