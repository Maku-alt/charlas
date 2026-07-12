# Minimal Agent Workflow Design

## Objetivo

Optimizar el workflow de charlas para un nivel de automatizacion intermedio: crear una charla end to end con un padre liviano, workers especializados con contexto acotado y controles minimos en los limites importantes.

El sistema existe para producir charlas. La trazabilidad solo se conserva cuando evita errores operativos concretos.

## Flujo objetivo

```text
idea -> research -> narrative -> build + image-close -> review
                                         |
                                         +-> build-fix -> review-final
```

`advisor-charlas` es una consulta opcional para decisiones transversales o tradeoffs dificiles. No es una fase, no aprueba artefactos y no interviene en el flujo rutinario.

## Responsabilidad del padre

El padre conversa con el usuario, converge la idea, consulta `agents/workflow-contract.json`, prepara paquetes acotados y decide la siguiente transicion.

El padre no ejecuta fases pesadas, no hereda el contexto de los workers y no lee sus chats o razonamiento. Para conocer el resultado de una fase valida el sentinel esperado y lee `notes/phase-summary.md`.

## Responsabilidad de los workers

Cada worker recibe `fork_context: false` y solo estos insumos:

- rol especializado;
- spec o package de la fase;
- prompt de ejecucion;
- inputs estrictamente necesarios;
- outputs permitidos;
- sentinel esperado;
- criterios de aceptacion.

El worker produce los artefactos de su fase, sobrescribe el summary operativo y publica el sentinel mediante el helper del repo.

## Contrato canonico

Se conserva `agents/workflow-contract.json` como unica fuente de verdad para fases, transiciones, roles, specs, prompts, inputs, outputs, sentinels e independencia de review.

`agents/runtime-defaults.json` conserva solo preferencias de ejecucion. Cambiar un modelo no cambia la validez del workflow.

## Handoff minimo

`notes/phase-summary.md` es el estado operativo actual y contiene solamente:

- fase y estado;
- decision;
- resumen breve;
- artefactos;
- evidencia minima;
- hallazgos bloqueantes;
- siguiente fase y accion.

No es un log, una transcripcion ni evidencia historica inmutable.

El sentinel contiene solamente la identidad necesaria para no confundir corridas:

- version del contrato;
- `run_id`;
- fase;
- intento;
- estado de ejecucion;
- fecha de finalizacion.

La publicacion sigue siendo atomica. No se conservan snapshots `phase-summary.<run_id>.md` ni `summary_sha256`.

## Controles que permanecen

- transiciones validas segun el contrato;
- `run_id`, fase e intento coherentes entre comando, summary y sentinel;
- sentinel publicado solo despues de validar el summary;
- separacion de identidad entre build/build-fix y review/review-final;
- candidato real requerido en fases de artefacto;
- SHA256 del PPTX en la frontera review/release para promover el archivo exacto aprobado;
- PowerPoint nativo como gate final del deck;
- bibliografia cuando hubo research externo.

## Complejidad que se elimina

- snapshots historicos del summary;
- hash del summary;
- validaciones y tests dedicados solo a historia inmutable;
- campos duplicados de worker y sesion;
- narrativa extensa de auditoria y pilotos en documentos operativos;
- repeticion de reglas que ya viven en el contrato canonico;
- evidencia local de smoke tests que no sea necesaria para operar o verificar el flujo.

## Aprendizaje en la charla piloto

Se crea un unico documento breve en `agentes-modulares/notes/aprendizaje-workflow-agentes.md`. Debe explicar:

- como funcionaba el flujo anterior;
- que problema resolvio la separacion padre/workers;
- por que el contexto acotado importa;
- por que se conserva un contrato canonico;
- cuales son los controles minimos;
- por que se descarto una arquitectura de auditoria mas pesada;
- como aplicar el flujo al crear una charla real.

Este documento es material de aprendizaje, no una nueva especificacion operativa.

## Criterios de aceptacion

La optimizacion pasa si:

1. El padre puede rutear el flujo consultando el contrato y summaries compactos.
2. Cada worker puede ejecutar su fase sin heredar el contexto completo.
3. Un sentinel viejo o de otra corrida no puede aceptarse como finalizacion actual.
4. Build y review mantienen identidad independiente.
5. El PPTX publicado coincide con el candidato aprobado.
6. Los tests y validadores esenciales pasan sin depender de historia inmutable.
7. Los documentos operativos describen el mismo contrato sin duplicarlo.
8. `agentes-modulares` contiene un unico aprendizaje practico y breve.

## Fuera de alcance

- telemetria end to end de tokens;
- event sourcing o historial completo de ejecuciones;
- plataforma general de auditoria de agentes;
- dashboards, bases de datos o servicios externos;
- convertir el aprendizaje en PPTX dentro de esta optimizacion.
