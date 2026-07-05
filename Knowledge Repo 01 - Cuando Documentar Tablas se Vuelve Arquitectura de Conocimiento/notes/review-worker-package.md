# Worker Package: Review

## Objetivo

Ejecutar la fase `review` para la corrida `knowledge-repo-01-full-rebuild-20260704`.

Debes revisar el PPTX candidato construido desde cero y decidir si pasa o requiere cambios. No corrijas el deck.

## Contexto minimo

Repositorio: `C:\Users\Victor\Proyectos\2026\charlas`

Carpeta de charla: `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`

Run id: `knowledge-repo-01-full-rebuild-20260704`

PPTX candidato:

`Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`

## Archivos a leer

- `AGENTS.md`
- `agents/review-charlas.md`
- `templates/charlas-sdd/prompts/run-review.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/review-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/narrative-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/build-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/narrative-brief.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/bibliografia.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/build-report.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/extracted-text.txt`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/native-contact-sheet.png`

Solo abre slides individuales si el contact sheet muestra defecto o si `review-spec.md` pide inspeccion puntual. No leas chats ni artefactos antiguos.

## Gates obligatorios

- Confirmar 9 slides.
- Confirmar que el PPTX valida y abre.
- Confirmar render completo de todas las slides.
- Confirmar PowerPoint nativo como gate final.
- Revisar contact sheet para ritmo global.
- Inspeccionar slides 5, 7 y 9 con especial cuidado por densidad conceptual y cierre editorial.
- Verificar texto extraido para tildes, signos de apertura y caracteres especiales.

## Salida si requiere cambios

Si hay P1/P2, escribe un review report accionable con esta estructura por hallazgo:

- slide
- severidad
- problema observado
- criterio incumplido
- cambio minimo sugerido
- rutas de evidencia

Review no corrige el deck.

## Salidas obligatorias

Escribe:

- `review/review-report.md`
- `notes/phase-summary.md`
- `review/knowledge-repo-01-full-rebuild-20260704/telemetry/review-usage-summary.json`
- sentinel: `notes/.phase-review.done`

## Summary minimo

`notes/phase-summary.md` debe decir:

- Ultima fase: `review`
- Estado: `completado`, `requiere cambios` o `bloqueado`
- Pasa / no pasa
- Resumen de 1-3 frases
- Artefactos, incluyendo `review/review-report.md`
- Hallazgos bloqueantes, con referencia al report si aplica
- Siguiente accion: cierre si pasa; build-fix si requiere cambios puntuales

Telemetry JSON minimo:

```json
{
  "run_id": "knowledge-repo-01-full-rebuild-20260704",
  "phase": "review",
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
  "sentinel": "notes/.phase-review.done",
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
