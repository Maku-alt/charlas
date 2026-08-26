# Bibliografía y fuentes verificadas

**Fecha de consulta de todas las fuentes web:** 2026-08-25.  
Se listan únicamente las fuentes utilizadas en `notes/research.md`. Las páginas de paquete y repositorio son fuentes primarias para versión, metadata y API; los papers son fuentes primarias o revisiones académicas para los conceptos y líneas de investigación.

## Conceptos de Subgroup Discovery

**[S1]** Michael Atzmueller, “Subgroup Discovery,” *WIREs Data Mining and Knowledge Discovery* (publicado originalmente 28-01-2015). Revisión de fundamentos, algoritmos, problemas avanzados, herramientas y aplicaciones.  
URL: https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.1144

**[S2]** Francisco Herrera, Cristóbal J. Carmona, Pedro González, María José del Jesus, “An overview on subgroup discovery: foundations and applications,” *Knowledge and Information Systems* 29 (2011), DOI 10.1007/s10115-010-0356-2. Presenta SD como extracción de reglas interesantes respecto de un target, en la intersección descriptiva/predictiva.  
URL: https://doi.org/10.1007/s10115-010-0356-2

## PySubgroup: versión, arquitectura y API

**[S4]** PyPI, proyecto `pysubgroup`, versión 0.9.0 (release 27-10-2025). Metadata de licencia, estado Beta, requisito Python, descripción y release history.  
URL: https://pypi.org/project/pysubgroup/

**[S5]** Florian Lemmerich et al., repositorio oficial `flemmerich/pysubgroup`, release 0.9.0 y commit history. Release notes de SubROC y commits de agosto de 2025 sobre SoftClassifierTarget, permutation testing y tests/documentación.  
URL: https://github.com/flemmerich/pysubgroup/

**[S6]** `pysubgroup/setup.cfg`, metadata y dependencias de la release: `python_requires >=3.8`, `numpy<2.0.0`, `scikit-learn>=1.7.1`, `statsmodels>=0.14.5`, pandas/SciPy/matplotlib. Fuente directa del límite NumPy y del análisis de compatibilidad efectiva.  
URL: https://github.com/flemmerich/pysubgroup/blob/master/setup.cfg

**[S7]** Documentación estable oficial de `pysubgroup` 0.9.0. Selectors, targets/QF, fórmulas de `StandardQF`, `SubgroupDiscoveryTask`, algoritmos de búsqueda, `create_selectors` y `MinSupportConstraint`.  
URL: https://pysubgroup.readthedocs.io/en/stable/

**[S8]** Documentación/API estable oficial, módulos de classifier targets y testing. Definiciones de `SoftClassifierTarget`, `ROCAUCQF`, `PRAUCQF`, `ARLQF`, `permutation_test`, preservación de tamaño/conteo de clase, semilla y corrección múltiple `fdr_by`.  
URL: https://pysubgroup.readthedocs.io/en/stable/api/pysubgroup.html

## Alternativas y compatibilidad del entorno

**[S9]** PyPI, proyecto `subgroups`, versión 0.1.12 (release 15-02-2026). Catálogo de algoritmos, licencia, release history y requisito Python >=3.11.  
URL: https://pypi.org/project/subgroups/

**[S10]** PyPI, `scikit-learn` 1.7.2 (release 09-09-2025). Metadata de Python >=3.10, dependencias NumPy/SciPy y wheels CPython 3.10.  
URL: https://pypi.org/project/scikit-learn/1.7.2/

**[S11]** NumPy, “NumPy 1.26.4 Release Notes.” Soporte de Python 3.9–3.12, útil para elegir una versión 1.26 bajo la restricción `numpy<2`.  
URL: https://numpy.org/devdocs/release/1.26.4-notes.html

**[S13]** pandas, “What’s new in pandas 3.0.0.” Metadata/documentación de la serie 3.0, que requiere Python 3.11+; justifica usar una versión 2.x fijada en Python 3.10.  
URL: https://pandas.pydata.org/pandas-docs/version/3.0/whatsnew/v3.0.0.html

## Líneas de investigación comparadas

**[S12]** Tom Siegl, Kutalmış Coşkun, Bjarne C. Hiller, Amin Mirzaei, Florian Lemmerich, Martin Becker, “SubROC: Subgroup Discovery for the Analysis of the Performance of Binary Classifiers,” arXiv:2505.11283 (submitted 16-05-2025; v2 27-08-2025). Framework de Exceptional Model Mining con ROC/PR-AUC, desequilibrio, poda, redundancia y testing.  
URL: https://arxiv.org/abs/2505.11283

**[S14]** Yao Xu, Benjamin Walter, Venkatesh Kalofolias, Jilles Vreeken, “Learning Exceptional Subgroups by End-to-End Maximizing KL-Divergence,” *Proceedings of ICML 2024*, PMLR 235. SYFLOW y su motivación frente a variables pre-discretizadas/targets complejos.  
URL: https://proceedings.mlr.press/v235/xu24w.html

**[S15]** Jakob Bach, “Constrained Subgroup Discovery,” arXiv:2406.01411 (2024), y repositorio oficial de experimentos. Formulación con SMT para restricciones de esparsidad/diversidad; el repositorio documenta comparaciones con `pysubgroup`, `subgroups` y otros paquetes, además de costes/dependencias experimentales.  
Paper: https://arxiv.org/abs/2406.01411  
Código: https://github.com/Jakob-Bach/Constrained-Subgroup-Discovery

## Validez estadística y causalidad

**[S16]** “Robust Subgroup Discovery,” *Data Mining and Knowledge Discovery* (2022), DOI 10.1007/s10618-022-00856-x. Discute que las medidas de calidad habituales no resuelven por sí solas la multiplicidad y propone penalizaciones/criterios robustos frente a múltiples hipótesis.  
URL: https://link.springer.com/article/10.1007/s10618-022-00856-x

**[S17]** Judea Pearl, “An Introduction to Causal Inference,” *The International Journal of Biostatistics* 6(2), Article 7 (2010), DOI 10.2202/1557-4679.1003. Distingue preguntas asociacionales de preguntas causales y los supuestos/datos adicionales necesarios para atribuir efectos.  
URL: https://jmlr.csail.mit.edu/proceedings/papers/v6/pearl10a/pearl10a.pdf

## Notas de trazabilidad

- La fecha de consulta de PyPI/repository/docs es la indicada arriba; los números de release y requisitos son volátiles y deben volver a verificarse si la charla se ejecuta después del 26-08-2026.
- La afirmación “Python 3.10 es el mínimo efectivo” es una inferencia de la intersección entre metadata de `pysubgroup` y su dependencia `scikit-learn>=1.7.1`; no debe presentarse como el valor literal de `python_requires`.
- No se usó una fuente sectorial para fijar 4% de churn: el 4% es una decisión del brief para un generador sintético. Las cifras de soporte/uplift propuestas en research son plausibilidad pedagógica, no evidencia de telecom.
