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

Para una corrida aislada, usa el paquete de ejecución y `agents/workflow-contract.json`. Publica el summary y el sentinel canónico seleccionado para `image-close` exclusivamente con `scripts/agent_workflow/complete-phase.py`; nunca escribas, reutilices ni comuniques sentinels manualmente. El paquete define las salidas temporales permitidas si corre en paralelo con build.

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
- publicación validada de `image-close` conforme al paquete de ejecución
- decision: `listo para build`, `requiere ajuste editorial` o `descartar direccion`; no uses `listo para build` si la imagen funcionaria como accesorio, wallpaper generico o contenedor pequeno
