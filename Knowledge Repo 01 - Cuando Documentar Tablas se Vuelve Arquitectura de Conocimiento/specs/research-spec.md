# Research Spec

## Pregunta investigada
Como definir con precision un `knowledge repo` para equipos de datos y por que importa como paso evolutivo entre fichas Markdown sueltas y una memoria operacional util para humanos y agentes.

## Modo
- orientado a decision
- estado del arte

## Nivel de esfuerzo
- standard

Default del repo: `standard`.

## Hipotesis inicial
Markdown por tabla es un buen punto de partida, pero no escala como memoria comun sin capas adicionales de navegacion, gobierno, versionado e interfaz de consulta. Un `knowledge repo` importa porque convierte documentacion dispersa en una capacidad operacional mantenible, consultable y revisable por equipos y agentes.

## Claims a verificar
- `Markdown` resuelve portabilidad y versionado basico, pero no define por si solo estructura, ownership, vigencia ni relaciones entre activos de conocimiento.
- una `wiki` o segundo cerebro mejora navegacion y descubrimiento humano, pero no equivale automaticamente a una memoria operacional gobernada.
- un `knowledge repo` necesita convenciones explicitas, metadata, ownership, historial y procesos de mantenimiento para ser util a escala.
- `MCP/API` debe presentarse como interfaz de acceso para agentes sobre conocimiento preparado, no como sustituto de la capa de memoria.
- `OKF` o formatos similares sirven como referencia portable para fichas o artefactos de conocimiento, pero no reemplazan el diseno del sistema de memoria.

## Perspectivas a cubrir
- practitioner de datos que documenta y consume tablas
- data engineer o analytics engineer que piensa en ownership, lineage y gobierno
- lider tecnico que necesita escalar conocimiento sin dependencia excesiva de expertos
- esceptico que cuestiona si esto es solo documentacion con nuevo nombre
- operador de agentes que necesita consultas acotadas y trazables

## Preguntas fuertes
- que tendria que existir para distinguir con claridad una coleccion de `.md` de un `knowledge repo`
- que evidencia muestra que navegacion humana y gobierno operacional son problemas distintos
- que parte del argumento depende de herramientas especificas y cual debe quedar agnostica
- que referencias actuales sirven para explicar `OKF` sin sobredimensionarlo
- como explicar `MCP/API` como interfaz de acceso sin venderlo como arquitectura de conocimiento
- que contraargumentos razonables diria alguien que prefiere seguir solo con docs sueltas o una wiki simple

## Evidencia minima para avanzar
- fuentes primarias u oficiales sobre `OKF` y, si aplica, sus limites como formato
- referencias actuales y concretas sobre patrones de wiki o segundo cerebro como capa de navegacion humana
- ejemplos creibles de metadata o contrato minimo para fichas de tablas en equipos de datos
- una formulacion clara y defendible de `MCP/API` como interfaz de consulta para agentes
- contradicciones registradas entre formato, wiki, repo e interfaz, con resolucion editorial

## Salida esperada
- tesis refinada
- hallazgos que si merecen slide
- contradicciones
- claims pendientes
- direccion de cierre
