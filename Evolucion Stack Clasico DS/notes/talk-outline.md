# Charla: Evolucion del stack clasico de Data Science

## Tesis

El stack clasico de Data Science no esta estancado. Incluso sin cambiar de paradigma, hay mejoras reales en compatibilidad, rendimiento, explicabilidad, APIs y mantenibilidad. La pregunta correcta no es "que libreria nueva aparecio", sino "que upgrades del stack actual generan valor real sin meter riesgo innecesario".

## Audiencia

Data scientists que trabajan con Python, features, modelado, optimizacion y explainability en entornos productivos o semi-productivos.

## Mensaje central

Hay tres decisiones distintas:

1. quedarse como estamos
2. modernizar el stack manteniendo `Python 3.10`
3. migrar a `Python 3.11` para desbloquear ramas nuevas del ecosistema

La charla muestra que la opcion 2 ya entrega bastante valor y que la opcion 3 tiene sentido cuando se busca modernizacion mas agresiva.

## Estructura sugerida de slides

### Slide 1. Portada

Titulo:

`Evolucion del stack clasico de Data Science`

Subtitulo:

`Que cambia realmente en las librerias que ya usamos`

### Slide 2. El mito

Idea:

El stack clasico no esta muerto. No todo avance relevante en Data Science viene de una libreria nueva o del mundo LLM.

Claim:

Mucho del valor practico hoy sigue viniendo de `pandas`, `scikit-learn`, `scipy`, `xgboost`, `lightgbm`, `feature-engine` y librerias alrededor.

### Slide 3. Nuestro stack actual

Tabla corta:

- `Python 3.10`
- `pandas 2.2.0`
- `scikit-learn 1.4.2`
- `scipy 1.10.1`
- `optbinning 0.18.0`
- `feature-engine 1.8.3`
- `xgboost 2.0.3`
- `lightgbm 3.3.5`

Claim:

No es un stack viejo; es un stack razonable. Pero ya existe espacio claro para upgrades estables.

### Slide 4. Que validamos

Idea:

No solo revisamos release notes. Probamos compatibilidad real.

Claim:

Se validaron entornos limpios con instalacion e imports para:

- stack maximo estable en `Python 3.10`
- stack moderno en `Python 3.11`
- variante `Python 3.11` con `scikit-llm`

### Slide 5. Stack recomendado sin cambiar runtime

Titulo:

`Modernizacion segura en Python 3.10`

Tabla:

- `pandas 2.3.3`
- `scikit-learn 1.7.2`
- `scipy 1.15.3`
- `feature-engine 1.9.4`
- `optbinning 0.21.0`
- `xgboost 3.2.0`
- `lightgbm 4.6.0`

Claim:

Este stack instala, resuelve e importa completo en un entorno limpio.

### Slide 6. Ganancia real de Python 3.10 recomendado

Mensajes:

- mejor compatibilidad con `NumPy 2`
- mas soporte de sparse arrays y Array API
- mejor soporte para pipelines modernos y librerias recientes
- mejoras incrementales sin costo de migrar runtime

### Slide 7. Que desbloquea Python 3.11

Titulo:

`Cuando si vale la pena subir el runtime`

Tabla:

- `pandas 3.0.3`
- `scikit-learn 1.9.0`
- `scipy 1.17.1`
- `feature-engine 1.9.4`
- `optbinning 0.21.0`
- `xgboost 3.2.0`
- `lightgbm 4.6.0`

Claim:

Si buscas modernizacion mas fuerte del stack tabular, `Python 3.11` es el punto de entrada natural.

### Slide 8. Donde aparece el conflicto real

Titulo:

`El caso Scikit-LLM`

Claim:

`scikit-llm 1.4.3` sigue siendo compatible, pero bloquea `pandas 3.x`.

Mensajes:

- `pandas 3.0.3` + `scikit-llm 1.4.3` no resuelve
- en `Python 3.11`, `scikit-llm` obliga a quedarse en `pandas 2.3.3`
- ademas mete un arbol transitive mucho mas grande

### Slide 9. Ganancia por libreria

Idea:

No todos los upgrades entregan el mismo valor.

Claim:

`pandas`, `scikit-learn` y `scipy` son los que mas cambian el entorno. `feature-engine`, `optbinning`, `xgboost` y `lightgbm` agregan valor, pero con impacto mas heterogeneo segun casos de uso.

### Slide 10. Recomendacion final

Tres caminos:

1. conservador: quedarse como estamos
2. recomendado: modernizar `Python 3.10`
3. estrategico: migrar a `Python 3.11` y separar un entorno LLM

## Cierre recomendado

No hace falta cambiar de stack para modernizarse. Muchas veces la mejor evolucion consiste en actualizar con criterio las librerias que ya usamos.
