# Marco económico para madurar la hipótesis

Fecha de referencia: 2026-06-02

## 1. Lo primero: corregir la conversación de modelos

Para que la charla sea precisa, conviene hablar de modelos reales y precios reales del momento.

### OpenAI API pricing oficial

Según la página oficial de precios de OpenAI al 2026-06-02:

- `GPT-5.5`: `input $5 / 1M tokens`, `output $30 / 1M tokens`
- `GPT-5.4`: `input $2.5 / 1M tokens`, `output $15 / 1M tokens`
- `GPT-5.4 mini`: `input $0.75 / 1M tokens`, `output $4.5 / 1M tokens`

### Anthropic API pricing oficial

Según la documentación oficial de Anthropic al 2026-06-02:

- `Claude Opus 4.8`: `input $5 / 1M tokens`, `output $25 / 1M tokens`
- `Claude Sonnet 4.6`: `input $3 / 1M tokens`, `output $15 / 1M tokens`
- `Claude Haiku 4.5`: `input $1 / 1M tokens`, `output $5 / 1M tokens`

Esto importa porque la charla debe evitar hablar de versiones imprecisas o desactualizadas.

## 2. Señales de tensión de costos

### Casos de mercado útiles para la narrativa

- Axios publicó el `2026-05-28` que empresas están empezando a cuestionar si el gasto creciente en IA entrega retornos claros.
- El mismo artículo dice que un cliente de un consultor gastó `500 millones de dólares en un solo mes` al no poner límites de uso sobre Claude.
- Fortune publicó el `2026-05-26` que Uber había consumido su presupuesto anual de IA en cuatro meses y que su COO dijo que el gasto se estaba volviendo más difícil de justificar.
- La documentación de Claude Code dice que en despliegues enterprise el costo promedio puede estar alrededor de `150 a 250 dólares por desarrollador por mes`, con alta varianza según uso y automatización.

### Casos adicionales que sí se pueden citar

- Axios reportó el `2026-05-28` que Microsoft había cancelado la mayoría de sus licencias internas de Claude Code, en parte por costos, citando a The Verge.
- The Information reportó el `2026-04-08` que Meta había desmontado un leaderboard interno de tokens llamado `Claudeonomics`.
- Fortune reportó el `2026-05-12` que Amazon había tenido un patrón similar de `tokenmaxxing`, con uso incentivado por rankings internos.

### Casos que no conviene afirmar todavía

No encontré evidencia suficientemente sólida y verificable para usar en la charla afirmaciones específicas sobre:

- Rappi
- Kereqi o nombres parecidos mencionados oralmente

Si aparecen luego fuentes primarias o reportes sólidos, se pueden agregar. Por ahora conviene no citarlos como hecho.

## 3. Mini escenarios para usar en la charla

Estos escenarios son ilustrativos. No representan una empresa concreta.

### Escenario A: 50 personas, uso moderado

Supuesto mensual por persona:

- `30M` tokens de input
- `6M` tokens de output

#### Costo mensual aproximado

- `GPT-5.5`: `(30 x 5) + (6 x 30) = 330 USD por persona`
- total para `50 personas`: `16,500 USD/mes`

- `Claude Opus 4.8`: `(30 x 5) + (6 x 25) = 300 USD por persona`
- total para `50 personas`: `15,000 USD/mes`

- `Claude Sonnet 4.6`: `(30 x 3) + (6 x 15) = 180 USD por persona`
- total para `50 personas`: `9,000 USD/mes`

Lectura:

- para 50 personas, el costo ya puede ser relevante
- pero todavía no necesariamente justifica infraestructura propia
- en muchos casos, la nube sigue ganando por simplicidad

### Escenario B: 200 personas, uso intensivo y agentes

Supuesto mensual por persona:

- `100M` tokens de input
- `20M` tokens de output

#### Costo mensual aproximado

- `GPT-5.5`: `(100 x 5) + (20 x 30) = 1,100 USD por persona`
- total para `200 personas`: `220,000 USD/mes`

- `Claude Opus 4.8`: `(100 x 5) + (20 x 25) = 1,000 USD por persona`
- total para `200 personas`: `200,000 USD/mes`

- `Claude Sonnet 4.6`: `(100 x 3) + (20 x 15) = 600 USD por persona`
- total para `200 personas`: `120,000 USD/mes`

Lectura:

- a este nivel, la pregunta on-premise o privada deja de sonar exótica
- no porque la nube sea mala
- sino porque el gasto recurrente ya amerita una comparación seria contra alternativas de infraestructura

## 4. Qué tendría que pasar para que on-premise tenga sentido

On-premise o infraestructura controlada solo empieza a ser defendible si se cumplen varias condiciones al mismo tiempo:

1. demanda relativamente estable
2. volumen alto y recurrente
3. modelo open source suficientemente bueno para el caso de uso
4. capacidad de operar hardware, serving, monitoreo y seguridad
5. tolerancia a menor elasticidad y a ciclos de renovación de infraestructura

Si faltan esas condiciones, la nube suele seguir siendo mejor.

## 5. El tradeoff real

### Lo que gana la nube

- acceso inmediato a frontier models
- elasticidad
- cero operación de hardware
- velocidad para experimentar
- mejor opción para equipos pequeños o demanda variable

### Lo que podría ganar infraestructura controlada

- costo marginal menor a alto volumen
- más control sobre datos y cumplimiento
- mejor previsibilidad de costos
- posibilidad de ajustar o comprimir modelos open source

### Lo que cuesta volver

- comprar o alquilar hardware especializado
- tener equipo de plataforma o MLOps más fuerte
- operar disponibilidad y capacidad
- lidiar con refresh de infraestructura
- aceptar que no siempre se tendrá la calidad del mejor modelo frontier

## 6. Tesis recomendada para la charla

La mejor tesis no es:

- "la nube se acaba"

La mejor tesis es:

- "el costo de la inferencia LLM está empujando a las empresas no a abandonar la nube, sino a rediseñar sus arquitecturas hacia esquemas más híbridos, más disciplinados y más sensibles al costo por workload"

## 7. Conclusiones usables para la charla

1. El problema no es el uso de IA, sino el uso sin FinOps ni gobierno.
2. El primer movimiento racional no es volver a on-premise: es medir mejor.
3. El segundo movimiento racional es segmentar workloads.
4. Solo después de eso tiene sentido evaluar infraestructura propia o privada.
5. El retorno no es al datacenter clásico; es a una arquitectura híbrida con control económico.

## Fuentes principales

- OpenAI API pricing: https://openai.com/api/pricing/
- Anthropic model pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Claude Code costs: https://code.claude.com/docs/fr/costs
- Axios, `AI sticker shock hits corporate America`, 2026-05-28: https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs
- Axios, `CEOs go bargain hunting for AI`, 2026-05-29: https://www.axios.com/2026/05/29/ceos-ai-cheaper-tokens
- Fortune, `Uber burned through its entire 2026 AI budget in four months`, 2026-05-26: https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/
- Fortune, `That doesn't sound very healthy: Amazon's reported tokenmaxxing might gamify AI usage`, 2026-05-12: https://fortune.com/2026/05/12/amazon-tokenmaxxing-claude-ai-capex-meta-gil-luria//
- The Information, `Meta Shutters Internal AI Token Leaderboard`, 2026-04-08: https://www.theinformation.com/briefings/meta-shutters-internal-ai-token-leaderboard
- IBM, `Why infrastructure is key to AI readiness`, 2026-05-11: https://www.ibm.com/think/news/think-2026-infrastructure-recap
- IBM, `More Companies Turning to Open-Source AI Tools to Unlock ROI`, 2024-12-19: https://newsroom.ibm.com/2024-12-19-IBM-Study-More-Companies-Turning-to-Open-Source-AI-Tools-to-Unlock-ROI?asPDF=1
