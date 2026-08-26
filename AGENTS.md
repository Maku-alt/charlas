# Charlas

## Producto y autoridad

Este repositorio produce Web Talks: experiencias frontend autocontenidas para presentar una tesis investigada mediante momentos editoriales, visuales e interactivos. El entregable canonico se construye directamente como HTML/CSS/JavaScript o React/TypeScript. PPTX es solo una exportacion opcional cuando el usuario la solicita.

Para crear, continuar, construir, revisar o liberar una charla usa primero `skills/charlas-workflow/SKILL.md`. La skill gobierna routing, handoffs y gates con progressive disclosure.

Fuentes de verdad, en orden:

1. La instruccion actual del usuario.
2. El brief y las restricciones concretas de la charla.
3. El research aprobado y `notes/bibliografia.md`.
4. La narrativa y el speech aprobados.
5. `PRODUCT.md` y `DESIGN.md`.
6. `skills/charlas-workflow/`.
7. El candidato frontend, su review exacto y el release.

## Invariantes

- Research es obligatorio. Toda charla debe tensionar la tesis, verificar claims actuales y mantener `notes/bibliografia.md` con las fuentes realmente usadas.
- La narrativa aprobada es la unica fuente de contenido del Build. Si cambia la tesis o el arco, vuelve a Narrative.
- Build usa obligatoriamente `impeccable` como proceso principal de direccion y ejecucion. Construye frontend directo; nunca convierte PPTX al artefacto canonico.
- Una Web Talk se compone de momentos, no necesariamente slides. Puede combinar escenas editoriales, visualizaciones, simulaciones, comparadores, demos y cierres visuales cuando ayuden a comprender la tesis.
- No existe un numero fijo de momentos. Narrative elige la extension minima que sostenga la tesis y el tiempo disponible; si el tema contiene varios arcos o exige demasiada profundidad, propone dividirlo en una serie y consulta al usuario antes de Build.
- La interaccion debe ser presentable: determinista, reiniciable, operable por teclado, legible en proyector y con fallback claro. No uses interactividad decorativa.
- El cierre contiene una sola idea o mensaje y una imagen protagonista vinculada con la tesis. Una cita real es opcional, nunca un requisito artificial.
- La presentacion ofrece navegacion lineal, posicion directa, controles visibles y fullscreen; evita scroll como navegacion primaria.
- Respeta foco visible, contraste, semantica y `prefers-reduced-motion`. Cuando el release promete autonomia, funciona sin red y usa assets locales.
- Review lo ejecuta un agente distinto, read-only, sobre el HTML, hash y renders exactos. Cualquier mutacion invalida el veredicto.
- Release contiene exactamente el candidato aprobado. El orquestador recalcula SHA-256 antes de promoverlo.

## Flujo y roles

`brief -> research -> narrative -> build <-> review -> release`

- `researcher_charlas`: valida tesis, evidencia, contradicciones, actualidad y bibliografia.
- `narrative_charlas`: convierte research aprobado en tesis, arco, momentos y speech.
- `experience_designer_builder_charlas`: define la experiencia, imagenes, frontend, renders y QA con Impeccable.
- `review_charlas`: revisa de forma independiente el candidato exacto y devuelve veredicto y fixes accionables.

Los cuatro custom agents usan `gpt-5.6-luna` con razonamiento `xhigh`. El hilo principal es el orquestador: conserva decisiones, envia handoffs minimos, integra resultados y publica release.

El pipeline es serial por defecto. Usa subagentes en paralelo solo para dos o mas trabajos sustanciales, independientes y con outputs disjuntos. Nunca permitas escrituras concurrentes sobre el mismo archivo.

## Estado y evidencia

Infiere el estado desde los artefactos sustantivos de la charla. Para ejecuciones nuevas no crees execution packages, phase summaries, sentinels, snapshots, routing logs ni manifests de corrida.

Persiste solo producto y evidencia util: brief, research, bibliografia, narrativa, speech, fuente frontend, assets usados, candidato, renders finales, review/fix-list y release.

Los contratos SDD, sentinels, scripts y decks PPTX antiguos son historia del repositorio; no gobiernan nuevas Web Talks. No migres charlas historicas salvo que se reabran.

## Operacion segura

- Revisa `git status --short` antes de editar y conserva cambios ajenos.
- Delimita la carpeta de la charla y evita cargar `node_modules`, builds, renders o candidatos historicos si la fase no los necesita.
- Los workers reciben objetivo, inputs exactos, outputs permitidos, restricciones y criterios observables. Devuelven `charlas-specialist-result-v1`; no entregan logs ni razonamiento interno.
- Pide al usuario solo decisiones que bloqueen materialmente el siguiente paso.
