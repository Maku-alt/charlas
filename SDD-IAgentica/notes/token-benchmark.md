# Token Benchmark: SDD-IAgentica

## Proposito
Mostrar que la reduccion de contexto no es solo limpieza narrativa: tambien tiene impacto economico porque los tokens de entrada se pagan.

Este benchmark es una estimacion propia sobre los artefactos de esta charla. No prueba que SDD reduzca tokens en todos los casos.

## Metodo
Se conto el tamano de los artefactos de texto en caracteres y se uso la regla aproximada `tokens = caracteres / 4`.

Escenario monolitico:
- cada una de 4 fases recibe el paquete completo de `specs/` + `notes/`
- paquete completo: 43,359 caracteres, aprox. 10,840 tokens
- 4 fases: aprox. 43,359 tokens de entrada

Escenario SDD acotado:
- research: `thesis-spec.md` + `research-spec.md` + prompt de fase
- narrativa: `narrative-spec.md` + `research-brief.md` + prompt de fase
- build: `build-spec.md` + `narrative-brief.md` + `STYLE-CHARLAS.md` + prompt de fase
- review: `review-spec.md` + `build-report.md` + `extracted-text.txt` + prompt de fase
- total: 52,063 caracteres, aprox. 13,016 tokens de entrada

Resultado:
- ahorro aproximado por corrida de 4 fases: 30,343 tokens de entrada
- reduccion aproximada: 70%

## Conversion a dolares
Para no amarrar la narrativa a un vendor, la slide usa un rango redondeado de costo de input: USD 0.50 a USD 5.00 por 1M tokens de entrada.

Con 1,000 corridas similares:
- tokens ahorrados: aprox. 30.3M
- costo evitado: aprox. USD 15 a USD 152 solo en input

La cifra es deliberadamente conservadora porque no incluye output, retrabajo, tiempo humano, errores detectados ni reintentos.

## Fuentes
- OpenAI API pricing: https://openai.com/api/pricing/
- Anthropic, Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI Agents SDK, Handoffs: https://openai.github.io/openai-agents-python/handoffs/
- OpenAI Agents SDK, Tracing: https://openai.github.io/openai-agents-python/tracing/
- LangChain, Context engineering for agents: https://www.langchain.com/blog/context-engineering-for-agents
- Liu et al., Lost in the Middle: https://arxiv.org/abs/2307.03172
- Shi et al., LLMs can be distracted by irrelevant context: https://www.semanticscholar.org/paper/Large-Language-Models-Can-Be-Easily-Distracted-by-Shi-Chen/3d68522abfadfc8ee6b7ec9edaaf91f1b2f38e5e
