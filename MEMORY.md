# Memory

## Producto vigente

Charlas produce Web Talks para audiencias tecnicas, normalmente personas que trabajan con datos. Una Web Talk es una experiencia frontend presentable: puede combinar narrativa, imagen, datos e interaccion y no esta limitada a slides HTML.

La ruta operativa es `skills/charlas-workflow/SKILL.md`. `PRODUCT.md` define el producto y `DESIGN.md` su firma compartida.

## Decisiones consolidadas

- Research es obligatorio y siempre mantiene `notes/bibliografia.md`.
- El flujo es `brief -> research -> narrative -> build <-> review -> release`.
- Narrative trabaja con momentos y speech, sin numero fijo. Si el tema contiene varios arcos principales, propone una serie antes de Build.
- Build usa `impeccable` como proceso principal y construye frontend directo.
- Una interaccion debe enseñar o revelar algo; debe ser determinista, reiniciable, operable por teclado y tener fallback.
- Cada charla tiene direccion visual propia. El sello comun es tesis fuerte, evidencia visible, navegacion silenciosa y cierre editorial memorable.
- El cierre contiene una sola idea o mensaje y una imagen protagonista; una cita real es opcional.
- Review es independiente y read-only sobre el candidato, hash y renders exactos.
- Cualquier mutacion posterior invalida el review. Release recalcula y promueve el SHA-256 aprobado.
- Las nuevas corridas no usan specs SDD, execution packages, phase summaries, sentinels, snapshots ni manifests operativos.

## Agentes

Los cuatro especialistas son `researcher_charlas`, `narrative_charlas`, `experience_designer_builder_charlas` y `review_charlas`. Todos usan `gpt-5.6-luna` con razonamiento `xhigh`; el hilo principal orquesta e integra.

## Historia

Las PPTX y notas de workflows anteriores se conservan como artefactos historicos. No gobiernan nuevas Web Talks y solo se migran cuando una charla se reabre.

## Charlas existentes

- `Harness Engineer`: el valor del agente vive tambien en su entorno operativo.
- `Evolucion Stack Clasico DS`: modernizacion practica del stack de Data Science.
- `El Eterno Retorno`: tension nube, on-premise y arquitectura hibrida para LLMs.
- `Wiki LLM con Obsidian`: memoria operativa compilada para research y decisiones.
- `SDD-IAgentica`: charla historica con release PPTX.
- `IA Agentica de Conversacion a Sistema`: charla historica sobre agentes como sistemas de trabajo.

Este archivo conserva decisiones; `AGENTS.md` sigue siendo la autoridad de operacion.
