# Thesis Spec

## Tema
Como la metodologia SDD se implementa en flujos de trabajo con IA agentica usando subagentes Codex con contexto acotado.

## Audiencia
Data Scientists, analytics engineers, ML engineers y lideres tecnicos que ya usan asistentes de IA para investigacion, codigo, analisis o documentacion.

## Problema
Los flujos largos en una sola conversacion reinyectan demasiado historial en cada paso: decisiones viejas, exploraciones descartadas, dudas intermedias y contexto que ya no aporta. Eso aumenta consumo de tokens, ruido cognitivo y riesgo de que el agente mezcle fases. La charla debe explicar por que convertir el trabajo en specs y handoffs compactos permite delegar mejor a subagentes.

## Tesis central
SDD vuelve practica la IA agentica porque convierte conversaciones largas en contratos de trabajo pequenos: cada subagente recibe solo el spec, los artefactos necesarios y un output esperado; el chat principal conserva decisiones, no todo el historial.

## Cambio esperado
La audiencia debe dejar de pensar en "hablar mas con el agente" como estrategia principal y empezar a disenar flujos: tesis, spec, handoff, artefacto, review y decision de continuidad.

## Fuera de alcance
- Benchmark cuantitativo exacto entre modelos o proveedores.
- Comparativa comercial entre plataformas de agentes.
- Implementacion interna de Codex o detalles privados de runtime.
- Prometer autonomia total sin supervision humana.

## Benchmark permitido
Se permite incluir un benchmark propio e ilustrativo sobre esta charla, siempre que quede etiquetado como estimacion de orden de magnitud. Debe comparar reinyectar todo el paquete de trabajo en cada fase vs. pasar solo el contrato y artefactos necesarios por fase. La conversion a dolares debe presentarse como rango aproximado usando precios vigentes citados, no como promesa universal de ahorro.

## Tradeoff central
Conversacion monolitica rica en contexto vs. ejecucion por fases con contexto minimo y artefactos verificables.

## Riesgos de framing
- Puede sonar como "mas documentacion" si no se muestra como ahorro operativo.
- Puede parecer que subagentes siempre mejoran calidad; la tesis debe matizar que mejoran cuando el contrato de entrada es bueno.
- Puede confundirse SDD con waterfall; hay que mostrarlo como iteracion con gates, no como plan rigido.
- Hay que evitar claims actuales de precio/costo sin fuente vigente.

## Decision de continuidad
seguir
