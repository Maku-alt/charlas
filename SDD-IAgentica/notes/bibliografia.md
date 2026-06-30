# Bibliografia: SDD-IAgentica

## Fuentes principales

| Fuente | Uso en la charla | Enlace |
|---|---|---|
| Anthropic, Building effective agents | Diferencia entre workflows y agentes; recomendacion de empezar simple antes de aumentar autonomia. | https://www.anthropic.com/engineering/building-effective-agents |
| Anthropic, Effective context engineering for AI agents | Soporte conceptual para tratar el contexto como superficie que se cura, no como memoria acumulada. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Anthropic, How we built our multi-agent research system | Caso practico de subagentes, coordinacion y trabajo por fases. | https://www.anthropic.com/engineering/multi-agent-research-system |
| OpenAI Agents SDK, Agents | Marco de agentes con instrucciones, herramientas y outputs estructurados. | https://openai.github.io/openai-agents-python/agents/ |
| OpenAI Agents SDK, Handoffs | Soporte para la idea de delegar entre agentes especializados. | https://openai.github.io/openai-agents-python/handoffs/ |
| OpenAI Agents SDK, Tracing | Soporte para auditabilidad de generaciones, tool calls, handoffs y guardrails. | https://openai.github.io/openai-agents-python/tracing/ |
| OpenAI Agents SDK, Context management | Distincion entre contexto local y contexto visible para el LLM. | https://openai.github.io/openai-agents-python/context/ |
| LangChain, Context engineering for agents | Estrategias write, select, compress e isolate para gestionar contexto en agentes. | https://www.langchain.com/blog/context-engineering-for-agents |
| LangChain Docs, Context engineering in agents | Explicacion practica de dar informacion, herramientas y formato correctos al agente. | https://docs.langchain.com/oss/python/langchain/context-engineering |
| Liu et al., Lost in the Middle | Evidencia de que modelos long-context no usan informacion de forma uniforme segun posicion. | https://arxiv.org/abs/2307.03172 |
| Shi et al., Large Language Models Can Be Easily Distracted by Irrelevant Context | Evidencia de sensibilidad a contexto irrelevante. | https://www.semanticscholar.org/paper/Large-Language-Models-Can-Be-Easily-Distracted-by-Shi-Chen/3d68522abfadfc8ee6b7ec9edaaf91f1b2f38e5e |
| OpenAI API pricing | Rango de precios usado para convertir el benchmark propio de tokens a dolares. | https://openai.com/api/pricing/ |

## Nota metodologica

El benchmark de tokens de la slide 5 es propio e ilustrativo. Usa `caracteres / 4` como aproximacion de tokens de entrada y compara:

- flujo monolitico: reinyectar todo el paquete de `specs/` + `notes/` en cada fase;
- flujo SDD acotado: enviar solo spec, prompt y artefactos necesarios por fase.

La cifra no prueba una mejora universal de SDD. Solo muestra que, en trabajos por fases, recortar contexto repetido puede tener impacto operativo y economico.
