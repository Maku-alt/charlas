# Recomendacion de upgrade y compatibilidad

Fecha de validacion: 2026-06-02

## Objetivo

Definir combinaciones de versiones que:

- respeten el stack actual del equipo
- mantengan compatibilidad interna entre librerias
- separen claramente lo que se puede hacer en `Python 3.10` y lo que se desbloquea con `Python 3.11`

La compatibilidad de los stacks recomendados fue revisada de dos maneras:

1. documentacion oficial y metadatos de paquetes
2. resolucion real con `pip install --dry-run --ignore-installed`

Importante:

- esto valida compatibilidad de dependencias, no regresion funcional de notebooks o modelos del equipo
- si usan features muy especificas, igual conviene una smoke test suite antes de cambiar el entorno base

## Resultado de validacion practica

Se levantaron entornos limpios y se validaron imports reales de las librerias objetivo.

Validado con instalacion completa mas import check:

- `Python 3.10.11` con `pandas 2.3.3`, `scikit-learn 1.7.2`, `scipy 1.15.3`, `feature-engine 1.9.4`, `optbinning 0.21.0`, `xgboost 3.2.0`, `lightgbm 4.6.0`
- `Python 3.11.9` con `pandas 3.0.3`, `scikit-learn 1.9.0`, `scipy 1.17.1`, `feature-engine 1.9.4`, `optbinning 0.21.0`, `xgboost 3.2.0`, `lightgbm 4.6.0`
- `Python 3.11.9` con `pandas 2.3.3`, `scikit-learn 1.9.0`, `scipy 1.17.1`, `feature-engine 1.9.4`, `optbinning 0.21.0`, `xgboost 3.2.0`, `lightgbm 4.6.0`, `scikit-llm 1.4.3`

Hallazgo importante:

- la variante con `scikit-llm` si instala e importa, pero altera parte del arbol transitive
- en `Python 3.11`, el entorno sin `scikit-llm` resolvio `ortools==9.11.4210`
- en `Python 3.11` con `scikit-llm`, el resolver bajo a `ortools==9.10.4067`

Esto no invalida el stack, pero si confirma que `scikit-llm` aumenta complejidad operacional y cambia el perfil real del entorno.

## Stack actual

- `Python==3.10`
- `pandas==2.2.0`
- `scikit-learn==1.4.2`
- `scipy==1.10.1`
- `optbinning==0.18.0`
- `feature-engine==1.8.3`
- `xgboost==2.0.3`
- `lightgbm==3.3.5`

## Recomendacion 1: stack maximo compatible en Python 3.10

Este stack resolvio correctamente en `Python 3.10.11` y paso import check:

- `pandas==2.3.3`
- `scikit-learn==1.7.2`
- `scipy==1.15.3`
- `feature-engine==1.9.4`
- `optbinning==0.21.0`
- `xgboost==3.2.0`
- `lightgbm==4.6.0`

### Lectura ejecutiva

Si el criterio principal es "subir lo maximo posible sin salir de Python 3.10 y sin romper dependencias", esta es la recomendacion base.

### Ganancia principal

- mantienes `Python 3.10`
- llevas el stack clasico a versiones muy recientes
- mejoras compatibilidad con `NumPy 2`, `scipy.sparse` moderno y ecosistema 2025-2026
- incorporas versiones nuevas de boosting, feature engineering y binning sin forzar migracion de runtime

### Tradeoff principal

- no puedes usar `pandas 3.x`
- no puedes usar `scikit-learn 1.8+`
- sigues cargando costo tecnico de permanecer en una rama de Python mas vieja

## Recomendacion 2: stack moderno en Python 3.11

### Variante A: modernizacion tabular completa

Este stack resolvio correctamente en `Python 3.11.9` y paso import check:

- `pandas==3.0.3`
- `scikit-learn==1.9.0`
- `scipy==1.17.1`
- `feature-engine==1.9.4`
- `optbinning==0.21.0`
- `xgboost==3.2.0`
- `lightgbm==4.6.0`

### Ganancia principal

- habilita `pandas 3.x`
- habilita `scikit-learn 1.9`
- habilita `scipy 1.17`
- reduce el gap frente al stack moderno del ecosistema

### Tradeoff principal

- requiere migracion de runtime a `Python 3.11`
- puede romper codigo que depende de `object` dtype o deprecations ya vencidas
- no convive con `scikit-llm 1.4.3`

### Variante B: Python 3.11 manteniendo Scikit-LLM

Este stack resolvio correctamente en `Python 3.11.9` y paso import check:

- `pandas==2.3.3`
- `scikit-learn==1.9.0`
- `scipy==1.17.1`
- `feature-engine==1.9.4`
- `optbinning==0.21.0`
- `xgboost==3.2.0`
- `lightgbm==4.6.0`
- `scikit-llm==1.4.3`

### Ganancia principal

- subes el runtime a `Python 3.11`
- modernizas `scikit-learn` y `scipy`
- mantienes `scikit-llm`

### Tradeoff principal

- renuncias a `pandas 3.x`
- arrastras una dependencia LLM con superficie transitive grande

## Conflicto real detectado

La combinacion siguiente fallo en el resolver:

- `Python 3.11`
- `pandas==3.0.3`
- `scikit-llm==1.4.3`

Motivo:

- `scikit-llm 1.4.3` depende de `pandas>=1.5.0,<3.0.0`

Conclusion:

- si quieres `pandas 3.x`, `scikit-llm` no debe vivir en el mismo entorno
- si `scikit-llm` es importante, conviene dejarlo como entorno o extra opcional

## Validacion adicional de librerias LLM cercanas al stack DS

Se hizo una validacion adicional en `Python 3.11` para revisar extensiones LLM plausibles alrededor del stack clasico.

### Caso 1: `scikit-llm` + `optuna`

La combinacion siguiente resolvio e importo correctamente:

- `pandas==2.3.3`
- `scikit-learn==1.9.0`
- `scipy==1.17.1`
- `scikit-llm==1.4.3`
- `optuna==4.8.0`

Lectura:

- `scikit-llm` si puede vivir como capa opcional si renuncias a `pandas 3.x`
- `optuna` no introduce conflicto en esa combinacion y sirve bien como herramienta de experimentacion para workflows LLM

### Caso 2: `pandasai`

La combinacion con `pandasai==3.0.0` no resolvio junto con `scikit-learn==1.9.0` y `scipy==1.17.1`.

Motivo detectado por el resolver:

- `pandasai 3.0.0` depende de `scipy==1.10.1`

Lectura:

- `pandasai` hoy no entra de forma limpia como capa adicional sobre el stack moderno recomendado
- si se quisiera evaluarlo, convendria hacerlo en un entorno separado y no en el ambiente base DS

## Recomendacion practica de entornos

En vez de un solo ambiente gigante, la opcion mas sana es separar:

### Entorno base DS

- pandas
- scikit-learn
- scipy
- feature-engine
- optbinning
- xgboost
- lightgbm

### Entorno opcional LLM

- stack base compatible
- `scikit-llm`
- credenciales y SDKs asociados

Esto reduce:

- tiempo de instalacion
- superficie de conflicto
- ruido por dependencias de `google-cloud-aiplatform` y `openai`

## Ganancias y tradeoffs por libreria

### pandas

Actual:

- `2.2.0`

Recomendado en `Python 3.10`:

- `2.3.3`

Recomendado en `Python 3.11`:

- `3.0.3` si no usas `scikit-llm`
- `2.3.3` si si usas `scikit-llm`

Ganancia:

- `2.3.x` mejora compatibilidad con `NumPy >= 2`
- corrige varios bugs en `StringDtype`, `to_hdf`, `to_excel` y operaciones de string
- `3.0.x` cambia el default de strings a `dtype=str`, lo que mejora tipado y puede mejorar memoria y seguridad de tipos

Tradeoff:

- `3.0.x` es el salto mas delicado del stack
- codigo que espera `dtype=object` en columnas string puede romperse
- para el propio proyecto pandas recomienda pasar primero por `2.3` antes de `3.0`

### scikit-learn

Actual:

- `1.4.2`

Recomendado en `Python 3.10`:

- `1.7.2`

Recomendado en `Python 3.11`:

- `1.9.0`

Ganancia:

- `1.7` agrega mejor soporte de Array API, mejora MLP con `sample_weight` y `loss="poisson"`, y avanza en la migracion a sparse arrays
- `1.9` agrega callbacks experimentales, utiles para observabilidad y control del entrenamiento

Tradeoff:

- `1.8+` ya pide `Python 3.11+`
- cambios asociados a sparse arrays y nuevas rutas internas pueden requerir retest de pipelines custom

### scipy

Actual:

- `1.10.1`

Recomendado en `Python 3.10`:

- `1.15.3`

Recomendado en `Python 3.11`:

- `1.17.1`

Ganancia:

- `1.15` ya trae sparse arrays mas funcionales, nuevo submodulo `scipy.differentiate` y `scipy.optimize.elementwise`
- `1.17` suma mas soporte para batching n-dimensional y Array API, mejoras en `sparse`, `spatial` y `stats`

Tradeoff:

- varias deprecations entre `1.15` y `1.17` ya se vuelven remociones reales
- si hay uso de APIs viejas, `1.17` exige mas limpieza

### feature-engine

Actual:

- `1.8.3`

Recomendado:

- `1.9.4`

Ganancia:

- `1.9.0` expande `ProbeFeatureSelection`, `RecursiveFeatureAddition` y `RecursiveFeatureElimination`
- `1.9.4` agrega transformadores nuevos para texto, geodatos, datetime ordinal e `ArcSinhTransformer`
- `1.9.4` agrega soporte para `pandas 3`

Tradeoff:

- si el equipo no usa esos transformadores, la ganancia inmediata puede ser baja
- el valor fuerte esta en compatibilidad futura y en nuevas opciones de feature engineering

### optbinning

Actual:

- `0.18.0`

Recomendado:

- `0.21.0`

Ganancia:

- `0.21.0` agrega `transform` en scorecard
- agrega `to_dict` para serializacion de binning tables
- incluye fixes cuando se usa `sample_weight`

Tradeoff:

- la ganancia es mas localizada que en pandas o sklearn
- si el uso del equipo es estable y acotado, es un upgrade de bajo dramatismo pero razonable

### xgboost

Actual:

- `2.0.3`

Recomendado:

- `3.2.0`

Ganancia:

- la rama `3.x` mejora memoria externa y performance
- agrega `ExtMemQuantileDMatrix`
- amplía soporte para categoricas, quantile regression y escenarios distribuidos

Tradeoff:

- el salto `2.x -> 3.x` no es menor
- si el equipo no usa external memory, distribucion o categoricas nativas, parte del beneficio puede no sentirse de inmediato

### lightgbm

Actual:

- `3.3.5`

Recomendado:

- `4.6.0`

Ganancia:

- la rama `4.x` limpió bastante la capa Python
- `4.6.0` trae mejoras de compatibilidad con versiones nuevas de scikit-learn y Python
- resuelve bien con el stack propuesto tanto en `Python 3.10` como `3.11`

Tradeoff:

- `4.x` trae breaking changes en la API Python
- en particular se removieron rutas viejas de entrenamiento y wrappers antiguos; hay que revisar llamadas legacy

### scikit-llm

Actual:

- no esta en el stack base reportado, pero se esta evaluando como extension

Recomendado:

- `1.4.3`, solo como dependencia opcional

Ganancia:

- se integra con workflows estilo scikit-learn
- hoy sigue siendo compatible con `Python 3.10` y `3.11`

Tradeoff:

- bloquea `pandas 3.x`
- mete un arbol de dependencias mucho mas grande que el resto del stack
- suma dependencias de `openai` y `google-cloud-aiplatform`, aumentando superficie de conflicto y mantenimiento
- en la prueba real, tambien modifico dependencias transitive del stack base, por ejemplo `ortools`

## Recomendacion final

### Si quieres el camino mas seguro

Usa `Python 3.10` y sube a:

- `pandas==2.3.3`
- `scikit-learn==1.7.2`
- `scipy==1.15.3`
- `feature-engine==1.9.4`
- `optbinning==0.21.0`
- `xgboost==3.2.0`
- `lightgbm==4.6.0`

Y deja `scikit-llm` fuera del entorno base.

### Si quieres el mejor stack clasico moderno

Usa `Python 3.11` y sube a:

- `pandas==3.0.3`
- `scikit-learn==1.9.0`
- `scipy==1.17.1`
- `feature-engine==1.9.4`
- `optbinning==0.21.0`
- `xgboost==3.2.0`
- `lightgbm==4.6.0`

Y mueve `scikit-llm` a un entorno separado.

### Si quieres Python 3.11 pero todavia con Scikit-LLM

Usa:

- `pandas==2.3.3`
- `scikit-learn==1.9.0`
- `scipy==1.17.1`
- `feature-engine==1.9.4`
- `optbinning==0.21.0`
- `xgboost==3.2.0`
- `lightgbm==4.6.0`
- `scikit-llm==1.4.3`

## Siguiente paso recomendado

Para la charla, la historia mas limpia es esta:

1. stack actual
2. stack maximo en `Python 3.10`
3. que desbloquea `Python 3.11`
4. conflicto real `pandas 3` vs `scikit-llm`
5. recomendacion de separar entorno base y entorno LLM

## Fuentes principales

- pandas installation docs: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
- pandas 2.3.0 release notes: https://pandas.pydata.org/pandas-docs/version/2.3/whatsnew/v2.3.0.html
- pandas 3.0.0 release notes: https://pandas.pydata.org/pandas-docs/stable/whatsnew/v3.0.0.html
- scikit-learn 1.7 release highlights: https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html
- scikit-learn 1.9 release highlights: https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_1_9_0.html
- SciPy 1.15.0 release notes: https://docs.scipy.org/doc/scipy-1.15.1/release/1.15.0-notes.html
- SciPy 1.17.0 release notes: https://docs.scipy.org/doc/scipy/release/1.17.0-notes.html
- Feature-engine 1.8 notes: https://feature-engine.trainindata.com/en/latest/whats_new/v_180.html
- Feature-engine 1.9 notes: https://feature-engine.trainindata.com/en/latest/whats_new/v_190.html
- OptBinning releases: https://github.com/guillermo-navas-palencia/optbinning/releases
- XGBoost 3.0 changes: https://xgboost.readthedocs.io/en/stable/changes/v3.0.0.html
- LightGBM releases: https://github.com/lightgbm-org/LightGBM/releases
- scikit-llm PyPI: https://pypi.org/project/scikit-llm/

## Nota sobre validacion

Las combinaciones recomendadas en este documento fueron comprobadas con `pip install --dry-run --ignore-installed` sobre:

- `Python 3.10.11`
- `Python 3.11.9`
