# Prompt: Run Image Close

Estas ejecutando solo la fase `image-closer-charlas`.

Usa solo:

- tesis aprobada
- mensaje final
- cita real de referente con autor/fuente, o fallback justificado
- tono emocional
- restricciones visuales del `Narrative Spec` o `Build Spec`
- referencias visuales explicitamente incluidas

No construyas el `pptx`. No hagas review final. No uses la imagen para explicar otra vez la parte tecnica.

Modelo sugerido para esta fase:

- `model`: `gpt-5.4`
- `reasoning_effort`: `medium`

Regla para `modo chat separado` o hilo worker separado:

- el resultado operativo se comunica solo por archivos en disco
- sobrescribe `notes/phase-summary.md` con el estado actual de image-close
- escribe `notes/.phase-image.done` al terminar
- responde en chat solo `DONE: summary written` o `BLOCKED: summary written`
- no pegues el contenido del summary en chat
- no uses `agent-log.md`

Si este cierre corre en paralelo con build, escribe temporalmente `notes/.phase-image.summary.md` en vez de sobrescribir `notes/phase-summary.md`. Escribe igual `notes/.phase-image.done`; el padre consolidara cuando tambien exista `notes/.phase-build.done`.

Devuelve:

- tesis que debe amplificar
- mensaje final
- cita real de referente con autor/fuente o fallback propio justificado
- tono emocional
- metaforas visuales candidatas
- direccion recomendada
- composicion de slide sugerida: imagen protagonista, zona de texto, recorte y relacion con la cita
- prompt final de imagen
- riesgos o cosas a evitar
- `notes/phase-summary.md` actualizado con fase, estado, pasa/no pasa, resumen, rutas, hallazgos bloqueantes y siguiente accion
- `notes/.phase-image.done` escrito al finalizar en modo chat separado o worker separado
- decision: `listo para build`, `requiere ajuste editorial` o `descartar direccion`; no uses `listo para build` si la imagen funcionaria como accesorio, wallpaper generico o contenedor pequeno
