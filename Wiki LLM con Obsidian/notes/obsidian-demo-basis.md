# Obsidian Demo Basis

## En que me base para construir el demo

El demo no salio de un solo prompt copiado y pegado.

Salio de combinar tres capas:

1. `La tesis original de Andrej Karpathy`
   - el gist `LLM Wiki`
   - idea central: no volver a descubrir conocimiento desde cero en cada consulta

2. `Implementaciones operativas recientes`
   - `ekadetov/llm-wiki`
   - `Ar9av/obsidian-wiki`
   - `NiharShrotri/llm-wiki`
   - patron recurrente: `init -> ingest -> compile -> query -> lint`

3. `Este repo concreto`
   - `AGENTS.md`
   - `MEMORY.md`
   - `IDEAS.md`
   - `STYLE-CHARLAS.md`
   - un `README` de charla madura

## Patron que use

El patron practico que segui fue este:

1. elegir pocas fuentes estables del repo
2. separarlas como `raw/`
3. compilar paginas mas durables en `compiled/`
4. enlazar esas paginas con `[[wikilinks]]`
5. archivar una pregunta reusable en `compiled/queries/`
6. dejar `source_refs` y `last_compiled` para proveniencia y drift

## Prompt mental de trabajo

No fue un prompt literal unico, pero la instruccion operativa equivalente fue:

`Toma un conjunto pequeno de documentos del repo. No respondas preguntando sobre ellos como si fuera la primera vez. Primero compila una capa intermedia de markdown con paginas de sistema, portfolio, backlog y queries reutilizables. Cada pagina debe enlazar a otras, distinguir hechos de interpretacion y guardar proveniencia.`

## Por que el demo quedo asi

Lo hice asi porque queria que la demo mental mostrara tres niveles visibles:

- `raw`: de donde sale el conocimiento
- `compiled`: que conocimiento ya quedo destilado
- `query filed`: que respuesta ya no necesita reconstruirse desde cero

Eso conversa mejor con la tesis de la charla que una demo demasiado grande o demasiado automatizada.

## Fuentes

- Andrej Karpathy, `LLM Wiki`
- `ekadetov/llm-wiki`
- `Ar9av/obsidian-wiki`
- `NiharShrotri/llm-wiki`
- Obsidian Help: `Web Clipper`, `Properties`, `Graph View`
