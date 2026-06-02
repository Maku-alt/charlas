# Marco de hipotesis

## Punto de partida

Cada vez mas empresas consumen LLMs desde proveedores externos. El patron inicial suele ser racional:

- cero infraestructura propia
- acceso inmediato a modelos grandes
- menor tiempo de salida
- costo variable aparentemente manejable

## La duda que aparece despues

Cuando la adopcion crece, el costo agregado de inferencia puede empezar a tensionar el presupuesto anual.

La hipotesis de la charla es que, a cierto volumen, algunas empresas empezaran a evaluar una migracion parcial hacia:

- modelos open source
- serving propio
- infraestructura privada u on-premise

## Preguntas de investigacion

### Economicas

- cuanto cuesta hoy un millon de tokens por proveedor y por familia de modelo
- cual es el costo mensual a distintos niveles de uso
- a partir de que volumen un cluster propio se vuelve defendible

### Operativas

- cuantos usuarios concurrentes soporta un despliegue propio razonable
- que hardware minimo se necesita
- cual es el costo de mantener disponibilidad, monitoreo y upgrades

### Estrategicas

- que tipos de workload justifican este movimiento
- donde los modelos frontier siguen siendo imposibles de reemplazar
- si la mejor respuesta no es on-premise total sino arquitectura hibrida

## Tesis provisional

No veremos un regreso masivo y simple al on-premise. Lo mas probable es un esquema hibrido:

- modelos frontier y casos elasticos en la nube
- modelos open source y workloads repetitivos o sensibles en infraestructura controlada

## Posible claim de la charla

El costo de los LLMs puede hacer volver parte de la infraestructura propia, pero no como nostalgia del pasado sino como optimizacion selectiva de workloads.
