# Aprendizaje del flujo de agentes modulares

Esta nota resume la ruta de aprendizaje que tuvimos al convertir la creacion de charlas en un flujo modular, auditable y con menor consumo de contexto. No es un log tecnico completo; es una lectura narrativa de que problema encontramos, que probamos, como nos fue y que aprendimos.

## 1. Punto de partida: un chat padre que hacia todo

Al inicio, el chat principal concentraba casi todo: research, narrativa, build, review, correcciones, renders y decisiones de cierre. Eso permitia avanzar rapido, pero el contexto crecia sin control.

Problema observado:
- El consumo de tokens subia en cada interaccion.
- Era dificil saber que fase estaba consumiendo mas.
- El padre absorbia detalles de ejecucion que no necesitaba para decidir.
- El flujo podia producir algo, pero no era facil de gobernar.

Aprendizaje:
El problema no era solo construir una PPT. El problema era convertir una conversacion larga en un sistema de trabajo con fases, contratos y evidencia.

Baseline cuantitativo confirmado:
- Una auditoria temporal local documento una sesion anomala de `17.79M` tokens.
- De esos, `17.74M` fueron input tokens y `16.81M` cached input.
- El output fue solo `42k` tokens.

Lectura:
El costo extremo no vino de escribir mucho texto visible. Vino de reenviar contexto acumulado: roles, prompts, specs, logs, evidencia, handoffs y decisiones dentro del padre.

## 2. Faseado SDD y agentes especializados

El primer cambio fue ordenar la charla como una secuencia de fases:

- tesis
- research
- convergencia con el usuario
- narrativa
- build
- cierre visual
- review

Luego definimos roles especializados:

- `orchestrator-charlas`
- `researcher-charlas`
- `narrative-charlas`
- `deck-builder-charlas`
- `image-closer-charlas`
- `review-charlas`

Tambien aparecieron specs por fase: `thesis-spec`, `research-spec`, `narrative-spec`, `build-spec` y `review-spec`.

Resultado:
La modularidad conceptual mejoro. Ya no era "un asistente haciendo todo", sino un flujo con responsabilidades mas claras.

Aprendizaje:
Separar responsabilidades ayuda a disenar mejor, pero no garantiza por si solo menor consumo de tokens.

## 3. Primera prueba de aislamiento: subagentes

Probamos subagentes como mecanismo para aislar fases pesadas.

Resultado medido:
- Subagentes: `9,661,763` tokens.

Como nos fue:
Mejoro frente al baseline anomalo de `17.79M`, pero no fue suficiente. La modularidad existia, pero el costo seguia siendo muy alto.

Aprendizaje:
Un subagente no reduce consumo por existir. Solo ayuda si la frontera esta bien disenada: entrada acotada, salida compacta, evidencia en archivos y cero razonamiento/logs largos devueltos al padre.

Matiz importante:
En teoria, el patron tambien podria funcionar con subagentes. El problema de nuestra prueba no fue "subagente" como concepto, sino que no logramos demostrar un aislamiento operativo confiable. No estaba claro si el padre dejaba de absorber contexto del subagente o si el handoff seguia trayendo demasiado ruido.

## 4. Segunda prueba: hilos worker con monitoreo por chat

Despues probamos hilos separados. La idea era que cada fase corriera fuera del padre.

Problema:
El padre monitoreaba los workers usando `read_thread`.

Resultado medido:
- Hilos con polling: `11,382,147` tokens.

Como nos fue:
Fue peor que los subagentes.

Aprendizaje:
Separar hilos no sirve si el padre lee las conversaciones de los workers. En ese caso, el contexto vuelve al padre y se pierde el beneficio del aislamiento.

## 5. Tercera prueba: hilos worker con sentinel y handoff por disco

Cambiamos el contrato de coordinacion:

- no `read_thread`
- no leer chat worker
- el worker escribe `notes/phase-summary.md`
- el worker escribe un sentinel `.phase-*.done`
- el padre solo espera el sentinel y luego lee el summary

Resultado medido:
- Hilos sentinel: `7,028,838` tokens.

Como nos fue:
Mejoro frente a hilos con polling y subagentes, aunque seguia siendo caro.

Aprendizaje:
La interfaz entre agentes no debe ser una conversacion. Debe ser un contrato pequeno por archivos: summary, sentinel y artefactos referenciados.

## 6. Cuarta prueba: Presentations y PowerPoint nativo

El siguiente cambio no fue solo de arquitectura de agentes, sino de herramienta de build.

Cambiamos:
- de `pptxgenjs` para decks nuevos
- a Presentations / `@oai/artifact-tool`

Tambien fijamos PowerPoint nativo como gate final:
- PowerPoint debe abrir/exportar el PPTX.
- LibreOffice/Poppler quedan como auxiliares.

Resultado medido:
- Presentations sentinel: `4,134,978` tokens.

Resultado tecnico:
- PowerPoint nativo abrio/exporto el PPTX.
- Desaparecio el error PowerPoint `0x80070570`.

Aprendizaje:
La arquitectura de agentes no compensa una herramienta fragil. Elegir bien el motor de ejecucion puede reducir problemas tecnicos y bajar costo operativo.

Lectura posterior:
Este paso fue util como prueba de ruta, pero no quedo como default permanente. La decision actual vino despues: para decks nuevos normales, el build debe ser un renderer local versionado desde `deck-spec.json`; las herramientas auxiliares no deben convertirse en default solo porque funcionaron en una prueba.

## 7. Quinta prueba: review controlado con build-fix y review-final

Aparecio un problema de proceso: que pasa cuando review no aprueba.

Antes, el riesgo era entrar en ciclos ambiguos:
- review detecta problemas
- build corrige algo
- review vuelve a fallar
- el padre improvisa
- se repite sin cierre claro

Cambiamos el contrato:
- `review` no corrige el deck.
- `review` deja hallazgos accionables por slide.
- el orquestador decide si corresponde un `build-fix` puntual.
- `build-fix` corrige solo las slides indicadas.
- luego corre una `review-final`.
- maximo un ciclo `build-fix` + `review-final`, salvo autorizacion explicita.

Resultado:
El orquestador dejo de ser solo un lanzador de fases. Paso a controlar transiciones, limites y criterios de cierre.

Aprendizaje:
Un sistema de agentes necesita reglas de salida. Si no hay limite de ciclos, el flujo puede producir trabajo infinito sin converger.

## 8. Sexta prueba: flujo final en una sola sesion

Probamos el flujo final con:

- build
- review
- build-fix
- review-final

Resultado medido:
- Finalflow single-session: `6,548,836` tokens.

Resultado de producto:
- PPTX final aprobado.

Problema:
La prueba no fue valida como diseno de consumo porque build, review, fix y review-final corrieron en una sola sesion padre.

Aprendizaje:
Un producto aprobado no prueba que el sistema sea eficiente. Hay que separar "calidad del entregable" de "calidad del flujo operativo".

Lectura metodologica:
Este resultado debe contarse como fallo de concepto, no como hito valido de consumo. Sirvio porque demostro el ciclo funcional `review -> build-fix -> review-final`, pero reforzo la necesidad de que el orquestador no ejecute fases pesadas cuando el contrato exige workers.

## 9. Septima prueba: workers reales para build/review/fix/review-final

Probamos el flujo con workers separados para:

- build
- review
- build-fix
- review-final

Resultado de producto:
- PPTX final aprobado.
- Review-final paso.
- PowerPoint nativo exporto 9 slides.
- Los sentinels y artefactos existieron.

Resultado de consumo:
- No medible de forma end-to-end.

Problema:
Faltaron JSONL o eventos suficientes para medir los workers. Tambien falto un parent claramente asociado a `create_thread` / `send_message_to_thread` estructurados.

Aprendizaje:
La siguiente frontera no era funcional, sino de observabilidad. Si el sistema no deja eventos medibles, la auditoria no puede inventar el consumo.

## 10. Auditoria corregida: producto, workers y tokens son dimensiones distintas

Una auditoria inicial tomo eventos incorrectos: uso un JSONL relacionado al run como si fuera el parent real, aunque solo contenia menciones textuales.

Corregimos el criterio:
- no contar strings como function calls
- no aceptar un parent solo porque menciona el run id
- separar producto, ejecucion y medicion de consumo
- declarar `unknown` cuando los tokens no son medibles

Resultado:
La auditoria corregida concluyo:
- producto final: pasa
- ejecucion probable con workers: pasa parcialmente
- contrato workers auditable completo: no pasa
- consumo end-to-end: no medible

Aprendizaje:
La auditoria tambien necesita contrato. Sin una definicion clara de que cuenta como evento real, se pueden tomar datos equivocados y llegar a conclusiones falsas.

## 11. Formalizacion como skills

Convertimos parte del aprendizaje en skills repo-locales:

- `skills/worker-handoff`: protocolo para ejecutar trabajo aislado con paquete acotado, summary y sentinel.
- `skills/worker-flow-audit`: auditoria por fase, evento, worker, consumo de tokens y evidencia.

Tambien ajustamos el orquestador:
- el orquestador usa `worker-handoff`
- el worker recibe solo paquete acotado
- el padre espera 180 segundos antes del primer `Test-Path` sobre el sentinel
- el padre usa `Test-Path`, no chat
- el padre no compensa ejecutando fases pesadas

Aprendizaje:
Cuando una practica se repite y corrige errores reales, debe convertirse en protocolo reutilizable.

## 12. Prueba mini: flujo validado, consumo no medible

Ejecutamos una prueba deliberadamente pequena para validar el comportamiento del flujo, no la calidad de una charla real.

La prueba cubrio:

- research minimo
- narrative minima
- build con error controlado
- review que falla
- build-fix que corrige solo el error
- review-final que pasa

Resultado:
- El flujo operativo paso.
- El padre lanzo workers por fase.
- La review inicial fallo por el error controlado.
- `build-fix` corrigio el marcador previsto.
- `review-final` paso.

Limitacion:
- El consumo de tokens no fue medible end-to-end porque no hubo JSONL/usage local suficiente por worker.

Aprendizaje:
La prueba mini valida la mecanica de fases y transiciones, pero no valida ahorro de tokens. Para consumo, el dato debe venir de eventos reales o JSONL aceptados. Si esos eventos no existen o no se pueden acotar, el consumo queda `unknown`.

Principio operativo:
No hay que crear telemetria paralela que solo repita `phase-summary.md`. `phase-summary.md` sirve para decidir transiciones; los tokens se auditan desde eventos reales.

## 13. Ajuste actual: renderer local como default operativo

Despues de la prueba con Presentations, el flujo se simplifico otra vez: el build normal de decks nuevos paso al renderer local del repo.

Decision actual:
- `deck-builder-charlas` genera o actualiza `deck-spec.json`.
- `scripts/deck_renderer/render-deck.js` construye el PPTX editable.
- `scripts/deck_renderer/theme-charlas.json` es el theme default.
- `scripts/deck_renderer/qa-deck.py` hace QA mecanico.
- `scripts/deck_renderer/validate-powerpoint.ps1` mantiene PowerPoint nativo como gate final.
- La skill `pptx` queda solo para emergencia o diagnostico avanzado: inspeccion, extraccion, unpack/pack, reparacion puntual y diagnostico XML/estructura.

Aprendizaje:
El build deja de depender de una conversacion larga o una herramienta generativa por defecto. El agente decide narrativa, layout y spec; el script hace la fabricacion repetible.

Tambien se fijaron defaults de modelo por fase:
- research / tesis: `gpt-5.5 medium`
- narrativa: `gpt-5.5 medium`
- build / build-fix: `gpt-5.4 medium`
- image-close: `gpt-5.4 medium`
- review / review-final: `gpt-5.4 medium`

## Sintesis conceptual

La tesis que emerge es:

> Modularizar agentes no es suficiente. Para que un sistema de agentes sea productivo, cada modulo necesita contrato, handoff, limites de contexto, gates de calidad y auditoria por eventos reales.

Otra forma de decirlo:

> El salto no es de "un agente grande" a "muchos agentes". El salto real es de conversacion a sistema operativo auditable.

La frase clave para defender esta idea:

> El problema no era el tipo de ejecutor; era la frontera. Un subagente, un hilo worker o un chat externo solo ayudan si la frontera esta bien disenada.

En nuestro caso, los hilos separados no fueron magia. Funcionaron mejor porque obligaron a una frontera operacional mas clara:

- thread separado
- paquete acotado
- sentinel
- summary en disco
- no lectura de chat
- auditoria por archivos y eventos

La eficiencia viene del contrato de frontera, no del nombre del mecanismo.

## Lectura para la charla de agentes modulares

Esta ruta sirve como caso practico para una charla sobre agentes modulares:

- La modularidad empieza como separacion de roles.
- Luego exige contratos por fase.
- Despues exige handoff por archivos, no por conversacion.
- Mas tarde exige gates de calidad.
- Finalmente exige auditoria de consumo y eventos.

El aprendizaje central es que un agente modular no es solo un prompt especializado. Es una pieza dentro de un sistema con entradas, salidas, responsabilidades, evidencia y limites.

Respuesta preparada para una objecion esperable:

Si alguien pregunta "por que no hacerlo con subagentes?", la respuesta es: si el subagente opera bajo el mismo contrato de frontera, podria funcionar. Debe recibir contexto acotado, escribir evidencia a archivos, devolver solo un summary minimo y no exponer razonamiento/logs al padre. En nuestra prueba, los subagentes no dieron suficiente ahorro porque esa frontera no estaba todavia suficientemente disenada ni auditada. Los workers ayudaron porque hicieron mas visible y exigible esa separacion.

## Estado actual

Ya tenemos una base mas madura:

- flujo por fases
- specs SDD
- agentes especializados
- handoff por sentinel
- `phase-summary.md` como handoff operativo
- renderer local para decks nuevos desde `deck-spec.json`
- PowerPoint nativo como gate
- ciclo controlado `review -> build-fix -> review-final`
- skill `worker-handoff`
- skill `worker-flow-audit`
- defaults actuales de modelo: `gpt-5.5 medium` para research/narrativa, `gpt-5.4 medium` para build/image/review

Lo pendiente no es demostrar que se puede producir un PPTX. Eso ya se logro.

Lo pendiente es ejecutar una prueba completa, ligera y limpia desde un chat nuevo, con fases separadas y auditoria posterior, para medir mejor el consumo real por fase.

Nota de medicion:
Un chat con historial largo sirve para coordinar, pero no sirve como base limpia para medir el consumo de una prueba. Para medir consumo, la corrida debe tener una frontera temporal y de contexto clara, y la auditoria debe separar conversacion relacionada, ejecucion real y auditoria posterior.
