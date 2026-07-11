# Prompt: Run Image Close

Estas ejecutando solo la fase `image-closer-charlas`.

Usa solo el `Image Close Spec`, el `Execution Package` y las referencias visuales explicitamente incluidas.

No construyas el `pptx`. No hagas review final. No uses la imagen para explicar otra vez la parte tecnica.

Modelo sugerido para esta fase:

- `model`: `gpt-5.4`
- `reasoning_effort`: `medium`

Para una corrida aislada, usa el paquete de ejecución y `agents/workflow-contract.json`. Publica el summary y el sentinel canónico seleccionado para `image-close` exclusivamente con `scripts/agent_workflow/complete-phase.py`; nunca escribas, reutilices ni comuniques sentinels manualmente. El paquete define las salidas temporales permitidas si corre en paralelo con build.

Devuelve:

- `Image Close Spec` completado: tesis, mensaje, cita/fallback, tono, restricciones, metaforas, direccion, asset, relacion de aspecto, espacio negativo y criterios de aceptacion
- composicion de slide sugerida y prompt final de imagen
- riesgos o cosas a evitar
- publicación validada de `image-close` conforme al paquete de ejecución
- decision: `listo para build`, `requiere ajuste editorial` o `descartar direccion`; no uses `listo para build` si la imagen funcionaria como accesorio, wallpaper generico o contenedor pequeno
