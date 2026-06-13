# Marco de hipótesis

## Punto de partida

Cada vez más empresas consumen LLMs desde proveedores externos. El patrón inicial suele ser racional:

- cero infraestructura propia
- acceso inmediato a modelos grandes
- menor tiempo de salida
- costo variable aparentemente manejable

## La duda que aparece después

Cuando la adopción crece, el costo agregado de inferencia puede empezar a tensionar el presupuesto anual.

La hipótesis de la charla es que, a cierto volumen, algunas empresas empezarán a evaluar una migración parcial hacia:

- modelos open source
- serving propio
- infraestructura privada u on-premise

## Preguntas de investigación

### Económicas

- cuánto cuesta hoy un millón de tokens por proveedor y por familia de modelo
- cuál es el costo mensual a distintos niveles de uso
- a partir de qué volumen un clúster propio se vuelve defendible

### Operativas

- cuantos usuarios concurrentes soporta un despliegue propio razonable
- qué hardware mínimo se necesita
- cuál es el costo de mantener disponibilidad, monitoreo y upgrades

### Estratégicas

- qué tipos de workload justifican este movimiento
- dónde los modelos frontier siguen siendo imposibles de reemplazar
- si la mejor respuesta no es on-premise total sino arquitectura híbrida

## Tesis provisional

No veremos un regreso masivo y simple al on-premise. Lo más probable es un esquema híbrido:

- modelos frontier y casos elásticos en la nube
- modelos de pesos abiertos y workloads repetitivos o sensibles en infraestructura controlada
- capacidad local personal para absorber volumen frecuente, privado o intensivo en iteraciones

## Nueva señal: RTX Spark

NVIDIA anunció el 31 de mayo de 2026 una nueva clase de PCs RTX Spark para otoño de 2026. La capacidad anunciada incluye hasta 128 GB de memoria unificada, hasta 1 petaflop FP4 de AI compute y ejecución local de LLMs de hasta 120B parámetros.

Esta señal no prueba un ROI ni elimina la nube. Amplía la hipótesis: la infraestructura controlada ya no significa solamente datacenter o cluster privado. Parte de la inferencia puede desplazarse al computador personal y funcionar como capacidad base.

La arquitectura resultante puede usar un orquestador para enrutar:

- tareas frecuentes, privadas o intensivas en volumen hacia modelos locales suficientemente buenos
- planificación compleja, modelos frontier, casos ambiguos y picos de demanda hacia cloud

El límite contractual de tokens deja de aplicar a la ruta local, pero permanecen límites de memoria, velocidad, energía y concurrencia.

## Posible claim de la charla

El costo de los LLMs y la nueva capacidad local pueden devolver parte de la inteligencia a infraestructura controlada, no como nostalgia del pasado sino como optimización selectiva de workloads.
