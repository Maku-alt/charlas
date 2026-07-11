# Prompt: Run Compact Research

Estas ejecutando una fase compacta de research para charla pequena.

Usa solo el `Research Package` recibido.

Para una corrida aislada, usa el paquete de ejecución y `agents/workflow-contract.json`. Publica el summary y el sentinel de `research` exclusivamente con `scripts/agent_workflow/complete-phase.py`; nunca escribas, reutilices ni comuniques sentinels manualmente.

Devuelve:

- tesis refinada
- 3-5 hallazgos que si merecen slide
- riesgos o contradicciones
- mini narrativa sugerida
- cierre tentativo
- contenido para `notes/bibliografia.md`, si hubo fuentes externas
- publicación validada de `research` conforme al paquete de ejecución
- decision: `seguir a build-review package`, `reformular`, `profundizar con full research spec` o `descartar`
