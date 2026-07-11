# Prompt: Run Advisor

Ejecutas solo una consulta `advisor-charlas`, no una fase del workflow.

- Carga modelo y esfuerzo de razonamiento de Advisor desde `agents/runtime-defaults.json`; registra valores solicitados y reales.
- Analiza solo la solicitud advisory suministrada y la evidencia referenciada.
- No modifiques deck, specs, research, bibliografÃ­a ni `notes/phase-summary.md`.
- No apruebes, bloquees ni ejecutes una transiciÃ³n.
- Escribe una recomendaciÃ³n en `<talk>/notes/advice/<run-id>-advisor.md` con el formato del rol.
- Solo despuÃ©s escribe el run-aware advisory sentinel `<talk>/notes/advice/.advisor-<run-id>.done`, con el `run_id` de la solicitud, modelo real, timestamp de finalizaciÃ³n y ruta de recomendaciÃ³n.
