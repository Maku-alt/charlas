# Agentes de Charlas

Esta carpeta documenta los agentes especializados de este repo.

## Agentes disponibles

- `orchestrator-charlas`: coordina el flujo entre agentes, decide dependencias, detecta bloqueos y define cuando conviene paralelizar research.
- `researcher-charlas`: investiga un tema, propone tesis o hipotesis candidatas, ordena narrativa, separa claims fuertes de claims que requieren validacion y deja una direccion clara antes de construir la deck.
- `deck-builder-charlas`: toma una tesis y narrativa ya convergidas y las convierte en una presentacion editable, visualmente fuerte y alineada con `STYLE-CHARLAS.md`.
- `image-closer-charlas`: define la metafora visual y la imagen editorial de cierre para la ultima slide.
- `review-charlas`: revisa narrativa, calidad visual, cierre e integracion de la imagen final antes de cerrar la charla.

## Flujo recomendado

1. Arrancar con `orchestrator-charlas` para identificar fase, dependencia y siguiente agente.
2. Usar `researcher-charlas` para explorar el tema, elegir angulo y converger tesis.
3. Si el framing ya esta claro, abrir research en paralelo solo para subpreguntas independientes.
4. Pasar a `deck-builder-charlas` cuando la direccion ya este lo bastante clara.
5. Usar `image-closer-charlas` para resolver la imagen editorial final cuando el cierre ya tenga mensaje, cita y tono.
6. Cerrar con `review-charlas`.

La salida de `researcher-charlas` no pasa automaticamente a la PPT. Primero sirve para discutir y converger.

## Dependencias rapidas

- `deck-builder-charlas` depende de una tesis y narrativa ya convergidas
- `image-closer-charlas` depende de tesis, mensaje final, cita y tono razonablemente claros
- `deck-builder-charlas` e `image-closer-charlas` solo deberian correr en paralelo si la cita y el mensaje final ya existen o se fijan antes
- `review-charlas` depende de una deck parcial o final ya construida
- si hay duda sobre la fase, empezar por `orchestrator-charlas`

## Nota operativa

- en Windows, si el builder de presentaciones resuelve mal `@oai/artifact-tool`, relanzar con `HOME=C:\\Users\\Victor` para que tome el runtime correcto

## Cuando usar cada uno

Usa `orchestrator-charlas` cuando:

- quieres decidir en que fase esta la charla
- quieres saber que agente corresponde ahora
- necesitas coordinar dependencias o bifurcaciones
- quieres evaluar si conviene paralelizar research

Usa `researcher-charlas` cuando:

- el tema todavia esta abierto
- falta definir la tesis
- hay que investigar el panorama, tradeoffs o evidencia reciente
- quieres decidir que si merece entrar a la charla

Usa `deck-builder-charlas` cuando:

- la tesis principal ya esta razonablemente cerrada
- la narrativa ya fue discutida
- toca convertir direccion en slides, visuales y `pptx`

Usa `image-closer-charlas` cuando:

- la ultima slide ya necesita una imagen editorial fuerte
- el cierre ya tiene mensaje, cita o tono definidos
- quieres evitar una imagen generica o demasiado literal

Usa `review-charlas` cuando:

- ya existe deck parcial o final
- quieres validar narrativa, consistencia visual y cierre
- quieres detectar que esta flojo antes de cerrar

## Cuando no usar estos agentes

- no uses `orchestrator-charlas` para reemplazar el trabajo especializado de los otros agentes
- no uses `researcher-charlas` para research general que no vaya a terminar en charla
- no uses `deck-builder-charlas` para descubrir el tema desde cero
- no uses `image-closer-charlas` para reemplazar la definicion de tesis o narrativa
- no uses `review-charlas` sobre puro research o ideas abiertas
- no uses ninguno para respuestas rapidas que no necesiten evidencia externa ni construccion de deck

## Ejemplos de prompts

- `Tengo una idea de charla, no se en que fase esta ni que agente deberia correr ahora.`
- `Investiga el estado actual de los agentes LLM para Data Science y propon una tesis de charla.`
- `Compara notebooks asistidos por IA versus harness engineering y ayudame a elegir el angulo.`
- `Ya cerramos la tesis. Ahora convierte esto en una deck de 9 slides con cierre editorial fuerte.`
- `Toma esta narrativa y armame un pptx editable con titulos-conclusion, comparacion central y cita final con autor.`
- `Con esta tesis y este mensaje final, propon la imagen editorial de cierre y dame un prompt final de imagen.`
- `Revisa esta deck y dime que esta descuadrado, flojo o fuera de lineamiento antes de cerrarla.`
