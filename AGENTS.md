# AGENTS

Este archivo captura como debe trabajar el agente dentro de este repositorio de charlas.

## Contexto del repo

- Este repositorio contiene multiples charlas.
- Cada carpeta de primer nivel representa una charla distinta.
- Las charlas estan orientadas a Data Science, datos, IA aplicada, stack tecnico, mejores practicas y decisiones de arquitectura.
- La audiencia objetivo es `Data Scientists` en general. No amarrar la narrativa a telco salvo que el usuario lo pida de forma explicita.

## Flujo de trabajo esperado

Cuando el usuario llegue con una idea de charla, el agente debe:

1. ayudar a madurar la tesis central
2. proponer una narrativa ejecutiva y tecnica
3. estructurar la charla normalmente en `8-10 slides`
4. crear o actualizar la carpeta de la charla
5. dejar notas de soporte, baseline tecnico y material validado cuando corresponda
6. construir un `pptx` editable y visualmente fuerte

Convencion minima recomendada dentro de cada carpeta de charla:

- `notes/`: narrativa, fuentes, claims, material validado y bibliografia
- `slides/` o `deck/`: fuente editable y exportables de la presentacion
- `assets/`: imagenes, prompts visuales y recursos de soporte cuando existan
- `review/`: observaciones, ajustes y chequeos finales cuando existan

Cuando convenga, separar explicitamente el flujo en agentes especializados:

- `orchestrator-charlas`: coordinar el flujo, dependencias y bifurcaciones entre agentes
- `researcher-charlas`: explorar el tema, investigar, proponer tesis y converger narrativa
- `deck-builder-charlas`: tomar una direccion ya discutida y convertirla en deck editable
- `image-closer-charlas`: resolver la metafora visual y la imagen editorial final del cierre
- `review-charlas`: revisar deck, cierre e imagen final contra los lineamientos del repo

No asumir que todo hallazgo del research entra automaticamente a la presentacion.

Si el framing principal ya esta claro y existen subpreguntas independientes, el research puede paralelizarse antes de converger de nuevo en una sola narrativa.

Orden recomendado:

1. `orchestrator-charlas`
2. `researcher-charlas`
3. research en paralelo si aplica
4. `deck-builder-charlas`
5. `image-closer-charlas`
6. `review-charlas`

`deck-builder-charlas` e `image-closer-charlas` pueden bifurcarse en paralelo cuando la tesis, el mensaje final, la cita y el tono ya estan suficientemente claros.

## Patron narrativo preferido

Por defecto, las charlas deben incluir:

- cover con tesis clara
- slides de contexto o baseline
- slides de comparacion o tradeoff
- una recomendacion o lectura ejecutiva
- una slide final de cierre con un solo mensaje fuerte

## Regla de cierre

Toda charla debe cerrar con:

- una frase o cita breve
- un mensaje de cierre que sintetice la tesis
- una imagen editorial alineada con el tema

La imagen final:

- no debe repetir tablas, bullets o diagramas de la deck
- no debe explicar literalmente la charla como si fuera otra slide tecnica
- debe amplificar el mensaje conceptual o emocional del cierre
- debe sentirse premium, editorial y deliberada
- debe diferenciarse visualmente de otras charlas aunque comparta el mismo universo de estilo

## Como decidir la imagen final

El agente debe buscar una metafora visual que converse con la tesis:

- `evolucion del stack`: modernizacion, transicion, madurez tecnica
- `nube vs on-premise`: costo, control, infraestructura, tension estrategica
- `harness engineering`: motor, contexto, sistema, ejecucion

El objetivo no es decorar. El objetivo es que la ultima slide deje memoria.

## Nivel de evidencia

Si una charla afirma:

- precios
- releases
- compatibilidad
- costos actuales
- casos corporativos recientes

entonces el agente debe verificar con fuentes actuales antes de consolidar la narrativa.

## Preferencias del usuario

- tono ejecutivo tecnico
- copy directo y claro
- visuales de alto impacto
- slides con tesis, no con titulos genericos
- cierre editorial fuerte
