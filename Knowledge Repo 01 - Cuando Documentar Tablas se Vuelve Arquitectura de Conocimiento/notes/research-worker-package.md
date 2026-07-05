# Worker Package: Research

## Objetivo

Ejecutar la fase `research` para la charla `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`.

Debes validar y tensionar la tesis desde fuentes actuales y producir insumos discutibles para narrativa. No construyas PPTX.

## Contexto minimo

Repositorio: `C:\Users\Victor\Proyectos\2026\charlas`

Carpeta de charla: `C:\Users\Victor\Proyectos\2026\charlas\Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento`

Run id: `knowledge-repo-01-full-rebuild-20260704`

Audiencia por defecto: gente que trabaja con datos, especialmente Data Scientists, analistas, data engineers, analytics engineers y lideres tecnicos.

Tono: ejecutivo, tecnico, directo y claro. No amarrar la narrativa a telco.

## Archivos a leer

- `AGENTS.md`
- `agents/researcher-charlas.md`
- `templates/charlas-sdd/prompts/run-research.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/README.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/thesis-spec.md`
- `Knowledge Repo 01 - Cuando Documentar Tablas se Vuelve Arquitectura de Conocimiento/specs/research-spec.md`

No leas artefactos viejos de `review/`, `slides/` o PPTX anteriores; fueron borrados para esta corrida.

## Research requerido

Usa research `standard`. Verifica con fuentes actuales cualquier claim sobre releases, compatibilidad, estandares emergentes, herramientas, MCP/API, OKF o casos corporativos recientes.

Cubrir:

- diferencia entre Markdown como formato y knowledge repo como sistema operativo de conocimiento;
- wiki o segundo cerebro como navegacion humana, y sus limites frente a gobierno/ownership/vigencia;
- metadata relacional en catalogos de datos como evidencia conceptual;
- OKF o formatos similares como referencia emergente, sin sobredimensionarlos;
- MCP/API como interfaz de consulta para agentes, no como sustituto de la memoria;
- contraargumentos razonables.

## Salidas obligatorias

Escribe:

- `notes/research-brief.md`
- `notes/bibliografia.md`
- `notes/phase-summary.md`
- `review/knowledge-repo-01-full-rebuild-20260704/telemetry/research-usage-summary.json`
- sentinel: `notes/.phase-research.done`

Formato minimo de `notes/phase-summary.md`:

```md
# Phase Summary

## Ultima fase
research

## Estado
completado | requiere cambios | bloqueado

## Pasa / no pasa
pasa | no pasa

## Resumen
1-3 frases.

## Artefactos
- `notes/research-brief.md`
- `notes/bibliografia.md`

## Hallazgos bloqueantes
- Ninguno

## Siguiente accion
Lanzar narrativa si pasa.
```

Telemetry JSON minimo:

```json
{
  "run_id": "knowledge-repo-01-full-rebuild-20260704",
  "phase": "research",
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
  "sentinel": "notes/.phase-research.done",
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
