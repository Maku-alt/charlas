# Prompt: Run Research

Estas ejecutando solo la fase `researcher-charlas`.

Usa solo:

- `Research Spec`
- `Thesis Spec`, si fue incluido
- fuentes o contexto explicitamente pegados en el encargo

No construyas slides. No hagas build. No avances a narrativa final.

Regla para `modo chat separado` o hilo worker separado:

- el resultado operativo se comunica solo por archivos en disco
- sobrescribe `notes/phase-summary.md` con el estado actual de research
- escribe `notes/.phase-research.done` al terminar
- responde en chat solo `DONE: summary written` o `BLOCKED: summary written`
- no pegues el contenido del summary en chat
- no uses `agent-log.md`

Devuelve:

- tesis refinada
- hallazgos que si merecen slide
- contradicciones
- claims pendientes
- direccion de cierre
- fuentes consultadas
- contenido para `notes/bibliografia.md`, si hubo fuentes externas
- `notes/phase-summary.md` actualizado con fase, estado, pasa/no pasa, resumen, rutas, hallazgos bloqueantes y siguiente accion
- `notes/.phase-research.done` escrito al finalizar en modo chat separado o worker separado
- decision de continuidad: `seguir`, `reformular`, `profundizar` o `descartar`
