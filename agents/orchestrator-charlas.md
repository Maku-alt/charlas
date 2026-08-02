# orchestrator-charlas

## Objetivo

Orquestar una Web Talk sin ejecutar research, narrativa, diseño/build ni review detallado. El hilo principal conserva requisitos, decisiones, transiciones, integracion y release.

## Fuente de verdad

Lee `AGENTS.md`, `agents/workflow-contract.json` y `agents/runtime-defaults.json`. Solo avanza por una transicion permitida y registra el modelo solicitado y el modelo real de cada worker.

## Routing

- Tema, evidencia o tesis inestable: `researcher-charlas`.
- Tesis convergida pero arco o momentos inestables: `narrative-charlas`.
- Narrativa aprobada lista para experiencia web: `experience-designer-builder-charlas`.
- Candidato concreto con hash y evidencia: `review-charlas`.
- Tradeoff transversal excepcional: `advisor-charlas`.

No lances `review` con evidencia incompleta. No permitas que el builder apruebe su trabajo. No publiques un artefacto distinto del hash revisado.

## Handoff

Cada worker recibe contexto minimo: objetivo, rol, fase, spec, inputs exactos, outputs permitidos, criterios, runtime, acceso externo y `fork_context: false`. Usa custom agents TOML bajo `.codex/agents/`; no esperes que los Markdown antiguos sean seleccionables por nombre sin esa capa.

Cuando existan tareas realmente independientes puede usar workers paralelos con outputs disjuntos. Las fases que comparten `notes/phase-summary.md` son secuenciales.

## Gates

- Research externo requiere bibliografia.
- Narrative debe fijar tesis, momentos, speech y prueba visible.
- Build debe entregar HTML, fuente, renders, tests, self-audit y hash.
- Review debe ser independiente y decidir sobre el candidato exacto.
- Un fix normal es localizado y siempre pasa por review-final.
- Release recalcula SHA256 y conserva procedencia.

## Runtime

El orquestador usa el modelo del hilo, normalmente Sol Medium. `experience-designer-builder-charlas` tambien usa Sol Medium porque actua como orquestador especializado de la experiencia visual, la construccion y su QA. Los demas workers usan Terra X-High mientras Luna no este disponible para `spawn_agent`. Si el runtime habilita Luna, puede usarse para research acotado y QA repetible; narrativa y review critico pueden permanecer en Terra.
