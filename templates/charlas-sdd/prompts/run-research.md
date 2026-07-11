# Prompt: Run Research

Estas ejecutando solo la fase `researcher-charlas`.

Usa solo:

- `Research Spec`
- `Thesis Spec`, si fue incluido
- fuentes o contexto explicitamente pegados en el encargo

No construyas slides. No hagas build. No avances a narrativa final.

Para una corrida aislada, usa el paquete de ejecución y `agents/workflow-contract.json`. Publica el summary y el sentinel de `research` exclusivamente con `scripts/agent_workflow/complete-phase.py`; nunca escribas, reutilices ni comuniques sentinels manualmente.

Devuelve:

- tesis refinada
- hallazgos que si merecen slide
- contradicciones
- claims pendientes
- direccion de cierre
- fuentes consultadas
- contenido para `notes/bibliografia.md`, si hubo fuentes externas
- publicación validada de `research` conforme al paquete de ejecución
- decision de continuidad: `seguir`, `reformular`, `profundizar` o `descartar`
