# Worker Package: Build Fix

## Objetivo

Ejecutar un unico `build-fix` puntual para la corrida `knowledge-repo-01-full-rebuild-20260704`.

Debes corregir el PPTX candidato solo por hallazgos P2 textuales: tildes/caracteres especiales degradados y mojibake en slide 3. No rehagas narrativa, research, imagen de cierre ni layout.

## Contexto minimo

Repositorio: `C:\Users\Victor\Proyectos\2026\charlas`

Carpeta de charla: `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`

Run id: `knowledge-repo-01-full-rebuild-20260704`

PPTX candidato a corregir:

`Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`

## Archivos a leer

- `AGENTS.md`
- `agents/deck-builder-charlas.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/review-report.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/review/extracted-text.txt`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/narrative-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/build-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/narrative-brief.md`

No leas chats ni artefactos antiguos.

## Cambios permitidos

- Restaurar ortografia espanola en titulos, labels, takeaways, pies y fuentes.
- Corregir slide 3 para que los signos de apertura de pregunta sean limpios, sin `Â` ni mojibake.
- Regenerar o editar el PPTX usando Presentations / `@oai/artifact-tool`.
- Regenerar evidencia de build necesaria para review-final.

## Cambios prohibidos

- No cambiar narrativa ni cantidad de slides.
- No redisenar layouts.
- No cambiar imagen final salvo que sea estrictamente necesario para mantener el render.
- No agregar nuevas fuentes, claims o slides.
- No iniciar otro ciclo de review ni corregir hallazgos no solicitados.

## Evidencia obligatoria

Escribe:

- PPTX corregido en la misma ruta canonica.
- `review/build-fix-report.md`
- renders corregidos necesarios, preferentemente todas las slides si regenerar completo es mas simple
- contact sheet PowerPoint nativo actualizado
- texto extraido actualizado en `review/extracted-text.txt`
- `notes/phase-summary.md`
- `review/knowledge-repo-01-full-rebuild-20260704/telemetry/build-fix-usage-summary.json`
- sentinel: `notes/.phase-build-fix.done`

PowerPoint nativo sigue siendo gate de apertura/export. Si falla tras un intento acotado, marca bloqueado.

## Summary minimo

`notes/phase-summary.md` debe decir:

- Ultima fase: `build-fix`
- Estado: `completado`, `requiere cambios` o `bloqueado`
- Pasa / no pasa
- Resumen de 1-3 frases
- Artefactos
- Hallazgos bloqueantes restantes
- Siguiente accion: lanzar `review-final` si pasa

Telemetry JSON minimo:

```json
{
  "run_id": "knowledge-repo-01-full-rebuild-20260704",
  "phase": "build-fix",
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
  "sentinel": "notes/.phase-build-fix.done",
  "status": "done|blocked"
}
```

Si no puedes obtener tokens o JSONL real, deja esos campos en `null` o `""`; no inventes medicion.

## Reglas

- Escribe `notes/phase-summary.md` antes del sentinel.
- Escribe el sentinel al final.
- No pegues logs completos en ningun summary.
- Respuesta final del worker en chat: solo `DONE: summary written` o `BLOCKED: summary written`.
