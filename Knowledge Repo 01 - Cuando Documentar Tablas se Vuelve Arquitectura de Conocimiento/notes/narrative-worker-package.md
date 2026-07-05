# Worker Package: Narrative

## Objetivo

Ejecutar la fase `narrative` para la corrida `knowledge-repo-01-full-rebuild-20260704`.

Debes convertir el research aprobado en una narrativa aprobable de 8-10 slides para PPTX. No construyas el PPTX.

## Contexto minimo

Repositorio: `C:\Users\Victor\Proyectos\2026\charlas`

Carpeta de charla: `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`

Run id: `knowledge-repo-01-full-rebuild-20260704`

Producto final de la corrida: PPTX editable nuevo.

El usuario aprobo que la narrativa la controle Codex. Usa los specs existentes como insumo, pero puedes reordenar, recortar o mejorar la narrativa si eso fortalece la charla.

## Archivos a leer

- `AGENTS.md`
- `agents/narrative-charlas.md`
- `templates/charlas-sdd/prompts/run-narrative.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/README.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/thesis-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/narrative-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/research-brief.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/notes/bibliografia.md`

No leas decks ni reviews anteriores.

## Direccion narrativa

La charla debe responder:

Como pasamos de fichas sueltas de tablas a una memoria operacional que sirva para el equipo y pueda ser consultada por agentes sin convertir el repo en un basural de Markdown.

Tesis base:

Documentar tablas se vuelve arquitectura de conocimiento cuando el equipo necesita conectar, mantener y consultar lo que sabe.

Debe quedar claro:

- Markdown es un punto de partida correcto.
- Wiki ayuda a discovery humano, pero no basta como gobierno operacional.
- Knowledge repo aporta contrato, ownership, relaciones, vigencia e historial.
- OKF es referencia emergente de portabilidad, no estandar corporativo final.
- MCP/API es interfaz para agentes, no memoria.
- RAG/grafos quedan como teaser para la charla 2, no como tema principal.

## Salidas obligatorias

Escribe:

- `notes/narrative-brief.md`
- actualiza `specs/narrative-spec.md` solo si hace falta para que represente la narrativa nueva aprobable
- actualiza o crea `specs/build-spec.md` si la narrativa cambia slides u objetos visuales
- `notes/phase-summary.md`
- `review/knowledge-repo-01-full-rebuild-20260704/telemetry/narrative-usage-summary.json`
- sentinel: `notes/.phase-narrative.done`

La narrativa debe tener 9 slides salvo que exista una razon fuerte para usar 8 o 10.

Cada slide debe incluir:

- tesis o titulo con punto de vista;
- lectura ejecutiva;
- objeto visible;
- concepto visual.

## Summary minimo

`notes/phase-summary.md` debe decir:

- Ultima fase: `narrative`
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
  "phase": "narrative",
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
  "sentinel": "notes/.phase-narrative.done",
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
