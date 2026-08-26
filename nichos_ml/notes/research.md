# Research — PySubgroup: encontrar los nichos que el promedio esconde

**Fase:** research (handoff para Narrative)  
**Consulta de fuentes:** 2026-08-25  
**Fecha de la charla:** 2026-08-26  
**Alcance:** validar la tesis, la elección contextual de librería y una demo sintética de churn telecom. No es una narrativa ni una especificación de frontend.

## Veredicto ejecutivo

La tesis es defendible, pero necesita dos ajustes de rigor:

> **Subgroup Discovery complementa los promedios y los modelos globales:** explora un espacio explícito de descripciones para encontrar subpoblaciones relativamente pequeñas, interpretables y con un contraste inusual en el target. En el entorno existente de Python 3.10, `pysubgroup` 0.9.0 es una opción pragmática si se fijan dependencias y se acepta que su estado declarado es Beta y que su actividad reciente es limitada. No es una recomendación universal: `subgroups` tiene un catálogo más amplio y una publicación más reciente, pero su metadata actual exige Python >=3.11.

El resultado de la demo debe presentarse como **asociación y generador de hipótesis de acción**, no como causalidad. La credibilidad depende de soporte mínimo, validación fuera de muestra/por tiempo y control de las muchas hipótesis que se prueban.

La decisión concreta para esta charla —Python 3.10 y churn global aproximadamente 4%— es razonable. Cambiaría si el proyecto migrara a Python 3.11, si `pysubgroup` actualizara su política de NumPy, o si `subgroups` añadiera compatibilidad 3.10 y se priorizara su catálogo de algoritmos.

## Clasificación de evidencia

| Afirmación | Estado | Base o alcance |
|---|---|---|
| Subgroup Discovery busca descripciones de subconjuntos que contrasten con un target, combinando inducción descriptiva y predictiva | **Hecho** | Revisiones de Atzmueller y Herrera et al. [S1–S2] |
| `pysubgroup` separa selectors, target, quality function, restricciones y algoritmo de búsqueda | **Hecho** | README y documentación/API oficiales [S4–S7] |
| La versión actual consultada es 0.9.0 (27-10-2025), con `SubROC` entre las novedades | **Hecho** | PyPI y release oficial de GitHub [S4–S5] |
| `pysubgroup` declara Python >=3.8, pero su dependencia actual `scikit-learn>=1.7.1` eleva el mínimo efectivo a Python 3.10; además declara `numpy<2.0.0` | **Hecho/inferencia de compatibilidad** | `setup.cfg`, PyPI de scikit-learn y NumPy [S6, S10–S11]. La elevación es una inferencia de resolver dependencias, no una modificación de metadata de `pysubgroup`. |
| Es la opción más pragmática en este entorno | **Interpretación contextual** | Depende de Python 3.10, reproducibilidad del entorno y alcance de la charla; no es ranking de calidad. |
| `subgroups` es más reciente y cubre más familias de algoritmos, pero exige Python >=3.11 | **Hecho contextual** | PyPI actual de `subgroups` [S9] |
| `SoftClassifierTarget`/SubROC auditan regiones donde un clasificador existente rinde diferente; no sustituyen al target binario de churn | **Hecho + aplicación** | API oficial y paper de SubROC [S8, S12] |
| Un nicho descubierto es causal o automáticamente accionable | **No respaldado** | Un contraste observacional requiere diseño causal/experimento adicional; ver advertencias más abajo [S17]. |

## 1. Qué problema resuelve Subgroup Discovery

La unidad de análisis no es “¿qué variable es importante?” ni “¿qué cluster aparece?”, sino una descripción legible como:

`contrato = mes a mes AND antigüedad ∈ [3, 12] AND caídas_90d >= 2`

Se compara la distribución del target dentro de esa descripción con la población de referencia. La revisión de Atzmueller define el campo como minería descriptiva para identificar subgrupos interesantes según una propiedad; la de Herrera et al. lo sitúa entre inducción descriptiva y predictiva [S1–S2]. Esto justifica la intuición editorial “el promedio esconde combinaciones”, sin afirmar que siempre existan nichos ni que el método supere a un modelo predictivo global.

Contrastes útiles para la audiencia:

- **Segmentación manual:** evalúa cortes que alguien decidió antes. Puede ser útil operativamente, pero no explora combinaciones sistemáticamente.
- **Clustering:** optimiza similitud de covariables, no necesariamente una diferencia de churn; un cluster puede no ser un grupo de riesgo.
- **Modelo global:** optimiza predicción individual (por ejemplo, ranking de clientes), mientras que SD busca regiones descritas que tengan un contraste colectivo y explicable. Un modelo puede complementar la búsqueda, no vuelve innecesario el contraste de subgrupos.

Esto es una comparación conceptual; no se ha medido en un benchmark común para esta charla. Debe decirse “responde otra pregunta”, no “es mejor que clustering/modelos”.

## 2. Anatomía de `pysubgroup`

La documentación oficial describe los **selectors** como objetos con `covers` que indican qué filas cubren. Ofrece selectores de igualdad e intervalo, negación y combinaciones de conjunción/disyunción; también permite implementar selectores propios [S7]. La arquitectura conceptual para explicar la demo es:

1. **Datos + selectors:** atributos categóricos y numéricos discretizados o acotados.
2. **Target:** `BinaryTarget("churn", True)` cuando se busca una tasa de churn inusual.
3. **Quality function (QF):** puntúa el contraste con el conjunto total. `StandardQF(alpha=1)` equivale a WRAcc en la parametrización habitual; la documentación muestra la forma general `((N_SG/N)^alpha) * (p_SG/N_SG - p/N)`. Esto hace visible el intercambio entre tamaño y elevación de tasa [S7].
4. **Search space + algoritmo:** `create_selectors(...)` y, por ejemplo, DFS o Beam Search; `SubgroupDiscoveryTask` recibe target, espacio, QF, tamaño de resultado, profundidad, calidad mínima y restricciones [S7].
5. **Restricción y revisión:** `MinSupportConstraint` impide que la tabla se llene de reglas minúsculas. El ranking no debe confundirse con evidencia confirmatoria.

En una explicación de 20 minutos bastan esos cinco bloques. El resultado que conviene mostrar para cada regla es: descripción, `n`, soporte, churn del subgrupo, churn global, lift/diferencia y quality. Un “top 1” sin su tamaño es una afirmación incompleta.

## 3. Estado, mantenimiento y compatibilidad (consulta 2026-08-25)

### Versión y mantenimiento

PyPI publica `pysubgroup` 0.9.0, lanzado el 27 de octubre de 2025, licencia Apache-2.0 y estado de desarrollo Beta [S4]. El repositorio oficial muestra trabajo concentrado en agosto-octubre de 2025: tests/documentación para `SoftClassifierTarget`, permutation testing y SubROC, culminando en el release 0.9.0 [S5]. En la consulta no aparecen commits posteriores al 27-10-2025.

La lectura responsable es “proyecto utilizable con una release reciente pero mantenimiento visible limitado después de esa release”, no “abandonado”. La release está publicada como wheel `py3-none-any`, pero la compatibilidad real también depende de sus dependencias.

### Python 3.10 y NumPy

El `setup.cfg` actual declara `python_requires >=3.8`, pero también:

- `numpy<2.0.0`;
- `scikit-learn>=1.7.1`;
- `statsmodels>=0.14.5`;
- pandas, SciPy y matplotlib sin límites superiores explícitos [S6].

`scikit-learn` 1.7.2 declara Python >=3.10 y ofrece wheel para CPython 3.10 [S10]. Las versiones actuales 1.8/1.9 ya exigen Python >=3.11 según su metadata de PyPI; por tanto, un entorno 3.10 debe fijar una versión compatible, no dejar que el futuro resolver seleccione cualquier “latest”. NumPy 1.26.4 soporta Python 3.9–3.12 [S11] y es una base razonable bajo la restricción `numpy<2`; no hay evidencia aquí de soporte de NumPy 2 por `pysubgroup`. pandas 3.0 exige Python >=3.11 [S13], así que en 3.10 debe usarse y fijarse una versión 2.x validada durante el build.

**Recomendación reproducible para la demo:** probar un entorno limpio de Python 3.10 con `pysubgroup==0.9.0`, `numpy==1.26.4`, `scikit-learn==1.7.2` y versiones compatibles fijadas de pandas/SciPy/matplotlib/statsmodels. El research no ejecuta el build ni afirma que cada combinación esté ya instalada; el siguiente paso debe ser un smoke test del import y de las APIs usadas.

La restricción de NumPy no invalida la charla, pero sí impide decir “compatible con el stack moderno” sin matiz. La formulación exacta es “pragmático en este stack fijado de Python 3.10/NumPy 1.26”.

## 4. Comparación contextual

### `subgroups`

`subgroups` publica una versión 0.1.12 del 15-02-2026, licencia BSD-4-Clause, y declara Python >=3.11 [S9]. Su catálogo documentado incluye SDMap/SDMap*, VLSD, BSD/CBSD/CPBSD, QFinder, IDSD, GMSL, DSLM y SDIGA. Por fecha y amplitud de algoritmos es una alternativa actual relevante; sin embargo, no es instalable directamente en el entorno Python 3.10 indicado en el brief.

El veredicto no debe ser “`pysubgroup` gana”: para esta charla, `pysubgroup` gana en fricción de adopción bajo 3.10 y tiene una API compacta para enseñar; `subgroups` puede ser preferible al migrar a 3.11 o si se necesita su catálogo específico. La comparación no incluye un benchmark de calidad/velocidad, por lo que no debe inferirse superioridad algorítmica.

### Líneas modernas de investigación, con alcance acotado

- **SubROC (2025):** framework de Exceptional Model Mining para encontrar subgrupos donde un modelo binario rinde de forma heterogénea; cubre ROC-AUC/PR-AUC, desequilibrio, redundancia, poda y significancia [S8, S12]. Es una extensión de auditoría de un modelo y ya aparece incorporado en `pysubgroup` 0.9.0, no un sustituto independiente para descubrir directamente el target churn.
- **SYFLOW (ICML/PMLR 2024):** aprende subgrupos maximizando divergencia KL con flujos normalizantes y descripciones interpretables; aborda limitaciones de métodos que parten de variables pre-discretizadas y targets más complejos [S14]. Es una línea de investigación más expresiva, con mayor complejidad de modelado/ingeniería; no es una alternativa drop-in validada para esta demo.
- **Constrained Subgroup Discovery (2024):** formula restricciones de diversidad/esparsidad con SMT y reporta heurísticas sobre datasets de clasificación; su repositorio compara varios paquetes, incluido `pysubgroup`, pero documenta costes de experimentación y dependencias heterogéneas [S15]. Es relevante para hablar de restricciones y redundancia, no para ampliar la demo.

Estas tres líneas bastan para contextualizar actualidad sin convertir la charla en catálogo. El mensaje es que el campo sigue activo y que `pysubgroup` ocupa una posición práctica/educativa, no necesariamente el frente investigador más nuevo.

## 5. SoftClassifierTarget, ROC-AUC, PR-AUC, permutación y SubROC

### Qué sí hace

La API oficial define `SoftClassifierTarget(label_column="label", prediction_column="prediction")` como target mínimo para medidas de rendimiento de un clasificador binario con scores suaves [S8]. `ROCAUCQF` y `PRAUCQF` comparan el ROC-AUC o PR-AUC de un subgrupo con el del dataset. `ARLQF` trabaja con average ranking loss. El target presupone que ya existe un clasificador y sus predicciones; no es la forma natural de buscar directamente “dónde hay más churn” en una tabla sin score.

Para el arco principal, usar `BinaryTarget` + `WRAccQF`/`StandardQF`. Como apéndice opcional, entrenar un modelo de churn con train y obtener `prediction` out-of-fold o en holdout; después usar `SoftClassifierTarget` para preguntar “¿en qué nichos el modelo se equivoca o discrimina peor?”. Eso separa riesgo observado de auditoría del modelo y evita enseñar dos problemas como si fueran uno.

### Precaución con la documentación de signo

La documentación de `ROCAUCQF` y `PRAUCQF` dice que un rendimiento menor del subgrupo puede producir calidad positiva, pero la fórmula publicada aparece como diferencia `métrica(subgrupo) - métrica(dataset)`, que produciría signo negativo cuando el subgrupo rinde peor. `ARLQF` sí es coherente con “más ranking loss = peor” y diferencia positiva. Es una inconsistencia documental que debe verificarse contra la implementación/test de 0.9.0 antes de poner el signo en pantalla. En la charla conviene decir “contraste de rendimiento” y mostrar el signo solo después del smoke test.

### Permutation testing y multiplicidad

La API `permutation_test` se limita a `SoftClassifierTarget`. Mantiene tamaño del subgrupo y conteo de clase, permite semilla mediante `np_rng`, devuelve p-values crudos, flags de rechazo, p-values corregidos, calidades y muestras nulas; su corrección por defecto es `fdr_by`, delegando métodos a `statsmodels` [S8]. Más muestras producen una resolución más fina del p-value.

La interpretación correcta es “¿es raro este contraste bajo una redistribución nula que conserva estructura básica?”, no “la permutación demuestra causalidad”. Como el buscador examinó muchas descripciones, usar p-values crudos para certificar el top-1 produce riesgo de falsos positivos. La literatura de SD identifica precisamente esta tensión de múltiples hipótesis [S16]. Para la demo, el test puede calcularse offline y mostrarse como validación posterior; no debe consumir el tiempo central ni ocultar que la regla fue seleccionada por la misma búsqueda.

## 6. Demo sintética de telecom: diseño defendible

### Objetivo y baseline

El brief fija un churn global aproximado de **4%**. Esto cambia la escala del ejemplo: una regla de 20% no es creíble para una gran población si su soporte es diminuto o si se obtiene por selección; debe mostrarse junto a `n` y validarse en holdout. Un nicho de 8–12% con soporte de varios cientos puede ser un uplift material pero plausible para una demo sintética; la cifra final es una decisión del generador que debe comprobarse, no una tasa empírica de telecom.

### Generación recomendada (inferencia de diseño)

- Semilla fija, por ejemplo `20260826`, entre 10.000 y 12.000 clientes.
- Variables: `churn`, `complaints_90d`, `outages_90d` o `downtime_hours_90d`, `tenure_months`, `contract_type`, `plan_type`, `autopay`, `monthly_charge` y, como máximo, una región/canal útil para ruido. Hacer que caídas y reclamos estén correlacionados, pero no idénticos.
- Generar churn con una probabilidad logística calibrada a ~0.04 global: efectos moderados de antigüedad, contrato y servicio, más una interacción controlada (por ejemplo, mes-a-mes + antigüedad 3–12 meses + >=2 caídas + >=2 reclamos). Añadir ruido y no incluir una columna latente `risk_niche` ni una fórmula visible.
- Ajustar el intercepto después de simular para que el promedio global quede cercano a 4%; reportar la tasa real obtenida, no prometer “exactamente 4%”.
- Separar discovery y validación: otra semilla, un split temporal simulado o datos de validación independientes. La regla debe conservar dirección y una tasa elevada fuera de la muestra; la demo debe enseñar que el hallazgo puede bajar.

### Búsqueda y tabla visible

Una configuración pedagógica es `create_selectors(df, nbins=5, ignore=["churn"])`, `BinaryTarget("churn", True)`, `WRAccQF`/`StandardQF(alpha=1)`, profundidad 3, 5–8 resultados y `MinSupportConstraint`. Para 10.000–12.000 filas, empezar con 2–5% de soporte (200–600 clientes) y ajustarlo solo si impide encontrar el nicho diseñado. La función de calidad penaliza el tamaño pequeño implícitamente, pero no reemplaza la restricción mínima.

Mostrar una tabla con:

| campo | por qué está |
|---|---|
| descripción | hace interpretable la regla |
| `n` y soporte | impide que un porcentaje aislado engañe |
| churn del subgrupo | contraste directo |
| churn global ≈4% | baseline para interpretar lift |
| lift y diferencia | traducción de magnitud |
| quality | conecta resultado con QF |
| holdout | evidencia de estabilidad, no solo descubrimiento |

Una acción posible (“priorizar revisión de calidad y retención para clientes con ese patrón”) debe formularse como hipótesis operativa. No decir “las caídas causan churn” ni “hay que ofrecer descuento a todos”.

### Qué no usar como demo principal

No usar `SoftClassifierTarget` para una tabla que solo tiene `churn`: faltaría la predicción de un modelo y se mezclarían conceptos. No enseñar ROC-AUC/PR-AUC como si midieran la tasa de churn del subgrupo. Si se incluye la extensión, usar scores de un modelo entrenado en train y evaluar en holdout; exigir suficiente número de positivos y negativos, reportar intervalos/variabilidad y comprobar el signo de la QF.

## 7. Límites que deben quedar explícitos

1. **Múltiples pruebas:** el buscador puntúa muchas combinaciones. FDR/permutación ayuda, pero un p-value post-selección no convierte automáticamente una exploración en confirmación; replicar en holdout/otra ventana y reducir el espacio con conocimiento de negocio.
2. **Soporte mínimo:** subirlo mejora estabilidad y accionabilidad, pero puede ocultar nichos reales; bajarlo aumenta varianza y reglas espurias. Con baseline 4%, un subgrupo de 20 clientes con 5 churns no es evidencia de un 25% estable.
3. **Solapamiento y redundancia:** varias reglas pueden describir casi los mismos clientes. Enseñar una sola regla representativa y mencionar que la lista requiere deduplicación/revisión.
4. **Asociación ≠ causalidad:** SD describe un contraste condicional. Para atribuir efecto a una intervención se requieren temporalidad, tratamiento/exposición definida, control de confusión y/o experimento [S17]. La salida apropiada es una hipótesis para investigación/acción controlada.
5. **Sintético ≠ negocio real:** la semilla y la interacción se diseñan para hacer visible el mecanismo; las tasas no son benchmark de una telco. El generador debe quedar documentado y ser reproducible.
6. **Dependencias y signo de SubROC:** fijar entorno 3.10/NumPy<2 y verificar imports/API; no esconder la incertidumbre documental de ROC/PR-AUC.

## Comprobaciones realizadas

- Revisadas las páginas oficiales de PyPI, repositorio/release y `setup.cfg` de `pysubgroup`.
- Revisada documentación estable de selectors, targets/QF, task/algoritmos, `SoftClassifierTarget` y permutation testing.
- Contrastada metadata actual de `subgroups`, scikit-learn 1.7.2, NumPy 1.26.4 y pandas 3.0 para resolver la afirmación sobre Python 3.10.
- Contrastadas tres líneas modernas (SubROC, SYFLOW y constrained SD) con paper/repo primarios.
- Bibliografía y URLs consultadas quedan en `nichos_ml/notes/bibliografia.md`, todas con fecha de consulta 2026-08-25.

## Uncertainty ledger

- No se ejecutó aquí un `pip install` ni un notebook; la compatibilidad propuesta es análisis de metadata y debe confirmarse con smoke test limpio.
- No se hizo benchmark de tiempo, calidad, cobertura o redundancia entre `pysubgroup` y `subgroups`; cualquier claim de “mejor” sería inválido.
- La documentación oficial presenta una posible inconsistencia de signo en `ROCAUCQF`/`PRAUCQF`; revisar implementación/tests de 0.9.0 antes de usarla en una visualización.
- Las cifras de uplift y soporte son recomendaciones para generar un dataset pedagógico, no evidencia del sector telecom.

## Siguiente acción acotada

Ejecutar un smoke test reproducible en Python 3.10 con el pin de dependencias propuesto y un dataset sintético de baseline ~4%: importar `pysubgroup`, correr la búsqueda binaria con `MinSupportConstraint`, comprobar `n`/churn/lift en holdout y verificar el signo de una QF de SubROC antes de que Narrative cierre la historia.
