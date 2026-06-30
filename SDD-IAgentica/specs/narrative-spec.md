# Narrative Spec

## Tesis aprobada
SDD vuelve practica la IA agentica porque convierte conversaciones largas en contratos de trabajo pequenos: cada subagente recibe solo el spec, los artefactos necesarios y un output esperado; el chat principal conserva decisiones, no todo el historial.

## Audiencia final
Data Scientists y tecnicos que ya usan IA para trabajo real y necesitan escalar de "una conversacion larga" a un workflow reproducible.

## Cambio esperado
Pasar de optimizar prompts aislados a disenar sistemas de trabajo: specs, fases, handoffs, artefactos y reviews.

## Tradeoff central
Conversacion monolitica con memoria completa vs. orquestacion por fases con contexto acotado.

## Lo que queda fuera
- Benchmark cuantitativo exacto entre modelos o proveedores.
- Comparativa entre vendors.
- Automatizacion sin supervision humana.
- Detalles internos de Codex.

## Arco narrativo
- cover
- baseline
- tension o tradeoff
- lectura ejecutiva o recomendacion
- cierre

## Slides propuestas

### Slide 1
- kicker: Tesis
- titulo con tesis: SDD convierte agentes en workflow, no en una conversacion larga
- objeto de prueba visible: contraste entre chat monolitico y flujo por specs
- takeaway: El valor no esta en escribir mas; esta en empaquetar mejor el trabajo.

### Slide 2
- kicker: Dolor operativo
- titulo con tesis: El historial completo se vuelve deuda de contexto
- objeto de prueba visible: pila de contexto con capas utiles y ruido
- takeaway: Cada paso arrastra exploraciones, dudas y decisiones que ya no deberian pesar.

### Slide 3
- kicker: Cambio de unidad
- titulo con tesis: El spec reemplaza al recuerdo como unidad de coordinacion
- objeto de prueba visible: contrato de entrada y salida por fase
- takeaway: Un subagente no necesita la historia completa si recibe un contrato claro.

### Slide 4
- kicker: Arquitectura
- titulo con tesis: El chat principal orquesta decisiones; los subagentes ejecutan fases
- objeto de prueba visible: diagrama orchestrator -> research -> narrative -> build -> review
- takeaway: El flujo reduce mezcla de roles y concentra el historial en decisiones.

### Slide 5
- kicker: Economia del contexto
- titulo con tesis: El ahorro aparece cuando deja de reinyectarse lo irrelevante
- objeto de prueba visible: benchmark propio de esta charla, comparando paquete completo por fase vs. contrato acotado por fase
- takeaway: La reduccion de contexto tambien es dinero, siempre que se mida como orden de magnitud y no como promesa universal.

### Slide 6
- kicker: Calidad
- titulo con tesis: La separacion por specs tambien mejora la revision
- objeto de prueba visible: gates de calidad: tesis, fuentes, narrativa, render, review
- takeaway: La calidad sube cuando cada fase deja evidencia revisable.

### Slide 7
- kicker: Tradeoff
- titulo con tesis: Subagentes sin buen contrato solo distribuyen la confusion
- objeto de prueba visible: tabla de cuando usar flujo SDD y cuando no
- takeaway: SDD no elimina criterio humano; lo obliga a aparecer antes.

### Slide 8
- kicker: Playbook
- titulo con tesis: El patron reutilizable es fase, spec, artefacto, review y decision
- objeto de prueba visible: loop operacional de cinco pasos
- takeaway: Cualquier equipo puede empezar con pocos templates y gates claros.

### Slide 9
- kicker: Cierre
- titulo con tesis: La nueva habilidad es disenar el contexto que otros agentes pueden ejecutar
- objeto de prueba visible: imagen editorial final con mensaje y cita
- takeaway: Menos conversacion acumulada; mas contratos de trabajo.

## Cierre
- mensaje final: No delegues memoria: delega contratos.
- cita: The palest ink is better than the best memory.
- autor: Proverbio chino
- tono emocional: sobrio, ejecutivo, ligeramente editorial
- direccion visual sugerida: un escritorio oscuro con tarjetas/specs iluminadas como planos de trabajo, y varias rutas de ejecucion saliendo hacia el fondo; no debe verse como dashboard ni diagrama tecnico.

## Riesgos narrativos
- Hacer que la charla parezca una defensa burocratica de documentar mas.
- Prometer ahorro cuantitativo sin medicion propia o sin fuente de precios vigente.
- Perder la diferencia entre subagente y chat separado si no se visualiza el handoff.

## Listo para build
si
