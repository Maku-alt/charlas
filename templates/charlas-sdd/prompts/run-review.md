# Prompt: Run Review

Estas ejecutando solo la fase `review-charlas`.

Precondicion del launch:

- este prompt debe ejecutarse junto con `agents/review-charlas.md`
- el archivo de rol especializado define el comportamiento; este prompt solo acota la fase

Usa solo:

- `Review Spec`
- build report o evidencia de build
- ruta del deck y renders indicados
- `notes/phase-summary.md` y rutas de evidencia referenciadas
- si es `review-final`: `review-report` inicial, evidencia de `build-fix` y PPTX/source candidato corregido

Precheck obligatorio:

- si falta `review-spec.md` o no es legible, aborta la fase con bloqueo de transicion
- si faltan sentinels previos requeridos o summaries suficientes, aborta con bloqueo de transicion salvo review diagnostico pedido explicitamente
- no improvises ni crees el `review-spec.md` dentro de esta fase

No reescribas la charla. No reconstruyas ni modifiques el deck.
No leas chats worker para completar contexto; usa `notes/phase-summary.md` y evidencia en disco.

Modelo sugerido para esta fase:

- `model`: `gpt-5.4`
- `reasoning_effort`: `medium`

Regla para `modo chat separado` o hilo worker separado:

- el resultado operativo se comunica solo por archivos en disco
- sobrescribe `notes/phase-summary.md` con el estado actual de review
- escribe `notes/.phase-review.done` al terminar
- responde en chat solo `DONE: summary written` o `BLOCKED: summary written`
- no pegues el contenido del summary en chat
- no uses `agent-log.md`
- no escribas `phase-summary-review.md`
- deja evidencia pesada en `review/`, `assets/` o `slides/` y referenciala desde `notes/phase-summary.md`

Formato de `notes/phase-summary.md`: `Ultima fase`, `Estado` (`completado`, `requiere cambios` o `bloqueado`), `Pasa / no pasa`, `Resumen` de 1-3 frases, `Artefactos` con rutas, `Hallazgos bloqueantes` y `Siguiente accion`.

En review debe indicar si el flujo esta en `review` o `review-final`, artefacto candidato actual, artefacto final si existe, hallazgos bloqueantes restantes y siguiente accion.

Devuelve:

- hallazgos priorizados con severidad P1/P2/P3
- si el veredicto es `requiere cambios`, un `review-report` en `review/` con hallazgos accionables por slide: `slide`, `severidad`, `problema observado`, `criterio incumplido`, `cambio minimo sugerido` y `rutas de evidencia`
- resumen de review
- slides mas debiles
- riesgos residuales
- estado de `notes/bibliografia.md` y `notes/phase-summary.md`
- `notes/phase-summary.md` actualizado con fase, estado, pasa/no pasa, resumen, rutas, hallazgos bloqueantes y siguiente accion
- `notes/.phase-review.done` escrito al finalizar en modo chat separado o worker separado
- veredicto final: `aprobado` o `requiere cambios`

Si la review inicial devuelve `requiere cambios`, no cierres el flujo: deja `Siguiente accion: orquestador decide build-fix o bloqueo`. Si `review-final` devuelve `requiere cambios`, registra `Estado: bloqueado` o `Pasa / no pasa: no pasa` con bloqueo explicito; no propongas otro ciclo salvo autorizacion explicita del usuario.

El review debe evaluar tambien fuerza conceptual y editorial. Una deck puede ser mecanicamente valida y aun asi requerir cambios si varias slides son demasiado cuadriculadas, repetitivas o no tienen concepto visual claro.

QA visual PPTX:

- PowerPoint nativo es el gate visual primario.
- Primero inspecciona solo contact sheet PowerPoint nativo.
- Abre slides individuales solo si el contact sheet muestra defecto.
- No hagas fixes visuales ni modifiques el deck desde review.
- Si PowerPoint nativo falla, registra bloqueo o continua solo como review diagnostico si el usuario lo pidio.
- LibreOffice/Poppler son auxiliares, no gate de aprobacion.

Si no puedes cerrar la review por falta de insumos o por bloqueo operativo, devuelve:

- `Estado`: `bloqueado`
- `Fase`: `review`
- `Bloqueo concreto`
- `Artefactos o evidencia disponible`
- `Chequeos o comandos que fallaron`
- `Chequeos o comandos que si funcionaron`
- `Riesgos residuales`
- `Accion siguiente propuesta`
