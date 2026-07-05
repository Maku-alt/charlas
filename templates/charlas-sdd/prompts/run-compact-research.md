# Prompt: Run Compact Research

Estas ejecutando una fase compacta de research para charla pequena.

Usa solo el `Research Package` recibido.

Regla para `modo chat separado` o hilo worker separado:

- el resultado operativo se comunica solo por archivos en disco
- sobrescribe `notes/phase-summary.md` con el estado actual de research
- escribe `notes/.phase-research.done` al terminar
- responde en chat solo `DONE: summary written` o `BLOCKED: summary written`
- no pegues el contenido del summary en chat
- no uses `agent-log.md`

Devuelve:

- tesis refinada
- 3-5 hallazgos que si merecen slide
- riesgos o contradicciones
- mini narrativa sugerida
- cierre tentativo
- contenido para `notes/bibliografia.md`, si hubo fuentes externas
- `notes/phase-summary.md` actualizado con fase, estado, pasa/no pasa, resumen, rutas, hallazgos bloqueantes y siguiente accion
- `notes/.phase-research.done` escrito al finalizar en modo chat separado o worker separado
- decision: `seguir a build-review package`, `reformular`, `profundizar con full research spec` o `descartar`
