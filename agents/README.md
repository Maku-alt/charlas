# Agentes de Charlas

El hilo principal orquesta y los custom agents bajo `.codex/agents/` ejecutan cuatro responsabilidades especializadas. La autoridad operativa compartida es `skills/charlas-workflow/SKILL.md`; estos Markdown describen solo el criterio propio de cada rol.

## Roles

- `researcher_charlas`: research obligatorio, tesis, evidencia y bibliografia.
- `narrative_charlas`: arco, momentos y speech sin cuota fija.
- `experience_designer_builder_charlas`: experiencia, imagenes, frontend, renders y QA con Impeccable.
- `review_charlas`: gate independiente y read-only del candidato exacto.

Todos usan `gpt-5.6-luna` con razonamiento `xhigh`. El modelo se configura exclusivamente en los TOML.

## Handoffs

Cada worker recibe objetivo, charla, inputs exactos, outputs que posee, restricciones y criterios observables. Devuelve solamente `charlas-specialist-result-v1` con rutas y evidencia compacta.

No se crean execution packages, phase summaries, sentinels ni logs de routing. El estado se deduce de los artefactos reales y la skill enruta desde el primer gate incumplido.

Build entrega candidato, hash, renders y QA. Review recalcula el hash, prueba la experiencia y devuelve el veredicto al orquestador, que persiste el reporte. Release promueve solo el SHA-256 aprobado.
