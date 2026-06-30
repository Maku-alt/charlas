# Prompt: Run Review

Estas ejecutando solo la fase `review-charlas`.

Precondicion del launch:

- este prompt debe ejecutarse junto con `agents/review-charlas.md`
- el archivo de rol especializado define el comportamiento; este prompt solo acota la fase

Usa solo:

- `Review Spec`
- build report o evidencia de build
- ruta del deck y renders indicados

Precheck obligatorio:

- si falta `review-spec.md` o no es legible, aborta la fase con bloqueo de transicion
- no improvises ni crees el `review-spec.md` dentro de esta fase

No reescribas la charla. No reconstruyas el deck.

Modelo sugerido para esta fase:

- `model`: `gpt-5.5`
- `reasoning_effort`: `medium`

Devuelve:

- hallazgos priorizados con severidad P1/P2/P3
- resumen de review
- slides mas debiles
- riesgos residuales
- estado de `notes/bibliografia.md` y `notes/agent-log.md`
- entrada de review para `notes/agent-log.md` con fase, agente, modelo, esfuerzo, estado, artefactos, errores o bloqueos, y siguiente accion
- veredicto final: `aprobado` o `requiere cambios`

El review debe evaluar tambien fuerza conceptual y editorial. Una deck puede ser mecanicamente valida y aun asi requerir cambios si varias slides son demasiado cuadriculadas, repetitivas o no tienen concepto visual claro.

Si no puedes cerrar la review por falta de insumos o por bloqueo operativo, devuelve:

- `Estado`: `bloqueado`
- `Fase`: `review`
- `Bloqueo concreto`
- `Artefactos o evidencia disponible`
- `Chequeos o comandos que fallaron`
- `Chequeos o comandos que si funcionaron`
- `Riesgos residuales`
- `Accion siguiente propuesta`
