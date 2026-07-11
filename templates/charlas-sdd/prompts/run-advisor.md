# Prompt: Run Advisor

Ejecuta únicamente la consulta auxiliar `advisor` con el rol `agents/advisor-charlas.md`.

El paquete de solicitud debe identificar este prompt y el `Advisor Request` aplicable. Carga la preferencia de modelo y esfuerzo desde `agents/runtime-defaults.json`; registra el requested and actual runtime en la recomendación y el sentinel.

Analiza solo la solicitud y la evidencia referenciada. No modifiques artefactos de fase, no apruebes, no bloquees y no ejecutes transiciones.

Escribe una recomendación y después su sentinel JSON. Valídalo con:

```powershell
python scripts/agent_workflow/validate-workflow.py --advisor-request "<talk>/notes/advice/<run-id>-request.md" --advisor-sentinel "<talk>/notes/advice/.advisor-<run-id>.done"
```
