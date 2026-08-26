# Narrativa — PySubgroup: encontrar los nichos que el promedio esconde

**Contrato:** charlas-specialist-result-v1 · fase Narrative  
**Charla:** PySubgroup: encontrar los nichos que el promedio esconde  
**Audiencia:** mixta de Data Science y negocio  
**Duración:** 20:00, incluida la demostración  
**Idioma:** español; nombres de API en inglés cuando ayudan a usar la librería  
**Fecha de charla:** 2026-08-26

## Decisión narrativa

### Tesis aprobada

Subgroup Discovery complementa los promedios y los modelos globales: explora un espacio explícito de descripciones para encontrar subpoblaciones relativamente pequeñas, interpretables y con un contraste inusual en el target. En el entorno existente de Python 3.10, pysubgroup 0.9.0 es una opción pragmática si se fijan dependencias y se acepta que su estado declarado es Beta y que su actividad reciente es limitada. No es una recomendación universal.

La charla es principalmente una introducción práctica y contextual a pysubgroup: qué pregunta responde, cómo se arma su búsqueda, qué ofrece frente a alternativas actuales y por qué encaja en el stack del equipo. El churn sintético demuestra la librería en **un único momento visual**, no constituye un arco separado. El resultado del ejemplo es asociación y una hipótesis de acción, no causalidad.

### Arco único

1. **Tensión:** un promedio o un modelo global puede dejar sin respuesta “¿dónde se concentra el contraste?”.
2. **Reencuadre:** segmentación manual, clustering y predicción global responden preguntas distintas; Subgroup Discovery busca reglas legibles para regiones contrastadas.
3. **Producto:** pysubgroup convierte esa pregunta en una API compacta: selectors, target, quality function, búsqueda y restricciones.
4. **Prueba única:** un solo momento de churn sintético muestra configuración, baseline cercano a 4%, regla, métricas y holdout.
5. **Decisión contextual:** Python 3.10 y dependencias fijadas hacen pragmática esta elección; alternativas tienen otras condiciones y no hay ranking universal.
6. **Recuerdo:** el valor no es encontrar “el mejor algoritmo”, sino hacer explícita y comprobable la pregunta de dónde mirar.

No aparecen varios arcos principales ni profundidad incompatible con una sesión. **No se propone dividir en serie.** SoftClassifierTarget/SubROC queda como extensión breve de auditoría, fuera de la demo principal.

### Qué queda fuera

- Un benchmark de calidad, velocidad o cobertura entre pysubgroup y subgroups.
- Un ranking universal de librerías o una afirmación de superioridad algorítmica.
- Un catálogo enciclopédico del campo.
- Datos reales o internos de telecom, ni tasas que pretendan ser benchmark del sector.
- Causalidad, ROI, descuentos o una intervención ya decidida.
- SoftClassifierTarget, ROC-AUC o PR-AUC como demo principal.
- Más de un momento/slide con datos de churn.

## Contrato del único momento de churn

M4 es el **único** momento visual que contiene el ejemplo de telecom/churn, sus tasas y su regla. Los otros momentos solo presentan conceptos, API, alternativas, límites y cierre. Dentro de M4 puede haber revelación secuencial o estados reiniciables, pero no se crea otro slide/momento de demo.

La superficie debe mostrar valores observados en una ejecución determinista; la narrativa fija el contrato, no números que el research no midió.

- Dataset sintético de **10.000–12.000 clientes**, semilla fija 20260826.
- Target churn; baseline global calibrado a **aproximadamente 4%** y reportado con la tasa real.
- Variables mínimas: complaints_90d, outages_90d o downtime_hours_90d, tenure_months, contract_type y plan_type; autopay, monthly_charge y como máximo una variable de ruido solo si ayudan. Reclamos y caídas se correlacionan, pero no son idénticos.
- Interacción controlada pero no obvia: por ejemplo, contrato mes a mes + antigüedad de 3–12 meses + al menos 2 caídas + al menos 2 reclamos. Hay ruido y no existe risk_niche.
- Discovery y validación se separan por otra semilla, ventana temporal simulada o datos independientes. La regla debe conservar dirección fuera de muestra; puede bajar su tasa.
- En la misma composición visual: configuración mínima (create_selectors, BinaryTarget, WRAccQF/StandardQF, profundidad y MinSupportConstraint), baseline, regla, n, soporte, tasa del subgrupo, lift/diferencia, quality y tasa/contraste en holdout.
- El rango pedagógico sugerido por research es soporte 2–5% (aprox. 200–600 clientes) y tasa del nicho 8–12%; son objetivos de plausibilidad, no hechos del sector. Si la ejecución produce otros valores, se muestran los observados.
- La acción se etiqueta como hipótesis: “priorizar una revisión de calidad y retención para clientes con este patrón”.

## Secuencia de momentos

### Momento 1 — La pregunta que el promedio no responde

**Tiempo:** 2:00  
**Afirmación:** Un promedio resume escala, pero no localiza una combinación de condiciones donde el target contraste.  
**Trabajo narrativo:** Abrir con tensión, sin portada administrativa ni empezar por una librería. Hacer que la audiencia reconozca el hueco entre medir y decidir dónde mirar.  
**Prueba visible:** Escena conceptual de una población resumida en una sola línea de “promedio” que deja varias regiones sin descripción; aparece la pregunta “¿qué combinación legible merece investigación?”. No usar aún valores ni tabla de churn.  
**Tratamiento:** Editorial estático con revelación secuencial breve. El foco pasa de “cuánto” a “dónde”; reduced motion conserva ambos estados.  
**Acción del presentador:** Pausar después del promedio conceptual y formular la pregunta.  
**Takeaway:** “El promedio es una señal de escala, no una explicación de distribución.”  
**Speech:** “Un promedio nos dice cuánto hay en el conjunto, pero puede dejar abierta la pregunta que importa para actuar: ¿dónde se concentra el contraste? Hoy no vamos a negar el valor de los promedios. Vamos a mirar la herramienta que hace explícita la búsqueda de una región legible.”  
**Transición:** “Antes de ver pysubgroup, comparemos la pregunta con las lentes que ya tenemos.”

### Momento 2 — Tres lentes y una pregunta distinta

**Tiempo:** 2:30  
**Afirmación:** Segmentación manual, clustering y un modelo global son útiles, pero responden preguntas distintas de Subgroup Discovery.  
**Trabajo narrativo:** Reencuadrar la objeción “ya tenemos segmentos/modelos” sin presentar un ganador.  
**Prueba visible:** Comparación conceptual en cuatro rutas: cortes elegidos antes; similitud de covariables; ranking/predicción individual; y descripción de una región con contraste en el target. Solo la última muestra la forma de una regla interpretable.  
**Tratamiento:** Comparación estática o revelación controlada por teclado. Cada ruta muestra una frase de pregunta, no métricas ficticias ni benchmark.  
**Acción del presentador:** Decir “responde otra pregunta” en lugar de “es mejor”. Señalar que SD complementa, no reemplaza.  
**Takeaway:** “Subgroup Discovery busca un contraste colectivo expresado como descripción, no solo similitud, cortes heredados o scores.”  
**Speech:** “Un segmento manual puede ser operativo, pero sus cortes fueron escogidos antes. Un cluster organiza por similitud, no necesariamente por una diferencia de churn. Un modelo global ordena clientes individualmente. Subgroup Discovery formula otra pregunta: ¿qué combinación explícita de condiciones cubre una región cuyo target contrasta con la población? Es una pieza complementaria.”  
**Transición:** “Esa pregunta se vuelve útil cuando su salida es una regla que podemos leer y discutir.”

### Momento 3 — La propuesta de pysubgroup en cinco piezas

**Tiempo:** 4:00  
**Afirmación:** pysubgroup separa la intención analítica en selectors, target, quality function, algoritmo de búsqueda y restricciones/revisión.  
**Trabajo narrativo:** Mostrar el producto y su arquitectura mínima antes de cualquier caso; DS obtiene un modelo mental utilizable y negocio entiende dónde entra cada decisión.  
**Prueba visible:** Flujo central y progresivo: datos → selectors → BinaryTarget("churn", True) → WRAccQF o StandardQF(alpha=1) → DFS/Beam Search, profundidad y tamaño de resultados → reglas revisadas. A un lado, una regla corta de ejemplo y el concepto de filas cubiertas. Junto a QF, la forma conceptual “contraste × tamaño”, o ((N_SG/N)^alpha) * (p_SG/N_SG - p/N), sin convertir la fórmula en el protagonista. MinSupportConstraint aparece como guardarraíl.  
**Tratamiento:** Visualización estática con estados de foco operables por teclado. Un toggle limitado puede alternar “tasa” y “tamaño” para hacer visible por qué una QF no debe premiar un porcentaje aislado. No sliders libres ni ranking universal.  
**Acción del presentador:** Introducir cada pieza con una sola frase: selectors cubren filas; target define qué se contrasta; QF hace explícito el intercambio; search explora; soporte y revisión controlan la salida.  
**Takeaway:** “La API no oculta la pregunta: permite declarar qué es interesante y por qué.”  
**Speech:** “La arquitectura cabe en cinco decisiones. Los selectors describen qué filas cubre cada condición. El target define el contraste; aquí será churn binario. La quality function combina diferencia y tamaño, así que una tasa llamativa en un grupo diminuto no basta. El algoritmo explora el espacio y la profundidad limita la complejidad. Finalmente, soporte mínimo y revisión humana impiden leer un top-1 como evidencia confirmatoria.”  
**Transición:** “Veamos todas esas piezas juntas, una sola vez, en un caso reproducible.”

### Momento 4 — El único ejemplo: churn, de configuración a hipótesis

**Tiempo:** 4:00  
**Afirmación:** Una búsqueda explícita puede hacer visible, en un caso sintético, cómo un baseline cercano a 4% convive con una regla interpretable, sus métricas y una comprobación en holdout.  
**Trabajo narrativo:** Demostrar pysubgroup sin abrir un arco de negocio separado. Este es el único momento/slide con datos de telecom, churn y tasas.  
**Prueba visible:** Una única composición con tres zonas: (a) configuración y procedencia —telecom sintético, seed 20260826, filas, selectors, BinaryTarget, QF, profundidad y soporte—; (b) baseline global observado ≈4%; (c) reveal de una regla y una tabla con descripción, n, soporte, churn del subgrupo, lift/diferencia, quality y discovery/holdout. La hipótesis de acción aparece al final y se etiqueta como asociación.  
**Tratamiento:** Demo determinista y reiniciable dentro del mismo momento: revelar configuración, baseline, resultado y holdout como estados de una sola escena. Si no hay runtime, fallback precalculado del mismo seed, etiquetado; no crear una escena de “setup” separada.  
**Acción del presentador:** Señalar n antes de la tasa; explicar QF en la misma composición; comparar discovery y holdout; traducir a “priorizar una revisión de calidad y retención”, nunca a causalidad.  
**Takeaway:** “La librería se entiende cuando configuración, contraste, tamaño y validación aparecen juntos.”  
**Speech:** “Este ejemplo es sintético, con semilla fija y ruido; no es evidencia de una telco. En la misma vista vemos la configuración que acabamos de explicar, la tasa global real cercana al cuatro por ciento y una regla descubierta. Primero leo cuántas filas la sostienen; después comparo su tasa con el baseline, miro lift y quality, y por último reviso si la dirección continúa en holdout. El resultado propone una hipótesis de revisión de calidad y retención. No demuestra que una condición cause churn ni ordena activar una oferta.”  
**Fallback:** “La ejecución interactiva no está respondiendo. Paso al estado precalculado de la misma semilla: la lectura es idéntica porque vemos configuración, baseline, regla, tamaño, contraste y holdout en esta única composición.” Si holdout no conserva dirección: “La salida correcta es replicar o revisar, no activar.”  
**Transición:** “La demo muestra la mecánica; la decisión de adopción depende del entorno real y de las alternativas.”

### Momento 5 — Por qué esta elección contextual en Python 3.10

**Tiempo:** 3:30  
**Afirmación:** pysubgroup es la opción más pragmática para este equipo bajo Python 3.10 y este alcance, no el ganador universal de Subgroup Discovery.  
**Trabajo narrativo:** Convertir la demo en una decisión de adopción verificable, sin usar un ranking numérico.  
**Prueba visible:** Matriz contextual de pocas filas: pysubgroup 0.9.0, API compacta y Python 3.10 con entorno fijado; frente a subgroups 0.1.12 (publicado 2026-02-15), más reciente y de catálogo más amplio, pero metadata Python >=3.11. Un pie de contexto mantiene Beta, mantenimiento visible limitado después de 2025-10-27 y dependencia numpy<2.0.0. SYFLOW y Constrained Subgroup Discovery aparecen solo como líneas de investigación más expresivas/restrictivas, no como drop-in de esta demo. La matriz distingue “encaja en nuestro entorno” de “es mejor”.  
**Tratamiento:** Comparación estática con foco de teclado sobre “compatibilidad efectiva”, “alcance de API” y “mantenimiento”; no score agregado ni ranking.  
**Acción del presentador:** Pronunciar “para este contexto”. Nombrar el pin reproducible sugerido: pysubgroup==0.9.0, numpy==1.26.4, scikit-learn==1.7.2 y pandas 2.x compatible. Decir qué haría cambiar el veredicto: migración a 3.11, cambio de política NumPy o necesidad del catálogo de subgroups.  
**Takeaway:** “La mejor elección aquí significa menor fricción reproducible bajo las restricciones actuales.”  
**Speech:** “La decisión es contextual. En Python 3.10, con pysubgroup 0.9.0, NumPy 1.26.4, scikit-learn 1.7.2 y versiones compatibles fijadas, la API compacta permite reproducir esta búsqueda con poca fricción. Su estado declarado es Beta y la actividad visible después de la release es limitada; por eso fijamos el entorno y hacemos smoke test. subgroups es relevante, más reciente y más amplio, pero su metadata actual pide Python 3.11 o superior. Si migramos o necesitamos esas familias, la decisión puede cambiar. No hemos medido calidad o velocidad en un benchmark común; no corresponde decir que una gana universalmente.”  
**Transición:** “Elegir la herramienta no elimina las preguntas estadísticas que quedan después de encontrar una regla.”

### Momento 6 — Extensión y límites que protegen la lectura

**Tiempo:** 2:30  
**Afirmación:** El resultado necesita controles contra multiplicidad, soporte insuficiente, redundancia y causalidad; SoftClassifierTarget/SubROC responde una pregunta posterior, no la del ejemplo.  
**Trabajo narrativo:** Poner los límites en el mismo marco que la adopción, sin abrir otro arco.  
**Prueba visible:** Cuatro guardarraíles conectados a la tabla del único ejemplo: muchas combinaciones; soporte mínimo; reglas solapadas; asociación ≠ causalidad. Un recuadro “extensión” muestra SoftClassifierTarget + SubROC → auditar regiones donde un clasificador existente rinde distinto, separado de BinaryTarget → churn observado. No mostrar signo ROC/PR-AUC sin verificar la implementación/tests 0.9.0.  
**Tratamiento:** Panel editorial estático con apertura opcional del recuadro; no otra demo ni métricas de modelo.  
**Acción del presentador:** Recorrer los límites en una frase cada uno y cerrar la extensión en menos de 30 segundos.  
**Takeaway:** “La librería encuentra candidatos interpretables; la confirmación exige diseño y validación adicionales.”  
**Speech:** “El buscador probó muchas descripciones: un p-value post-selección no convierte automáticamente la exploración en confirmación. El soporte protege estabilidad, pero subirlo también puede ocultar nichos. Varias reglas pueden describir casi a las mismas personas. Y asociación no es causalidad: para atribuir un efecto necesitamos temporalidad, control de confusión o experimento. SoftClassifierTarget y SubROC son una extensión útil cuando ya existe un clasificador y queremos auditar dónde rinde diferente; no sustituyen al target binario de la demostración.”  
**Transición:** “Con esa frontera clara, queda una sola idea sobre la elección.”

### Momento 7 — Una pregunta explícita para saber dónde mirar

**Tiempo:** 1:30  
**Afirmación:** El valor de pysubgroup es convertir “¿dónde se concentra el contraste?” en una búsqueda explícita, interpretable y revisable.  
**Trabajo narrativo:** Cerrar sobre la tesis de producto y contexto, no sobre el dataset ni una lista de APIs.  
**Prueba visible:** Una única imagen protagonista: un espacio amplio resumido como promedio y una regla corta que ilumina una región concreta. Única frase: **“El promedio dice cuánto; pysubgroup hace explícito dónde mirar.”** No añadir nuevas cifras ni segundo mensaje.  
**Tratamiento:** Cierre estático o transición lenta; sin controles ni resumen técnico.  
**Acción del presentador:** Dejar la frase en silencio unos segundos y repetirla una sola vez.  
**Takeaway:** “La herramienta vale porque hace visible la pregunta y deja discutir la evidencia.”  
**Speech:** “No nos llevamos un ranking universal ni la promesa de que una regla observacional sea causal. Nos llevamos una decisión y una práctica: bajo Python 3.10, fijar el entorno y usar pysubgroup para buscar descripciones legibles; después exigir tamaño, holdout y revisión. El promedio dice cuánto; pysubgroup hace explícito dónde mirar.”  
**Transición:** Fin. Las preguntas técnicas pueden abrirse después de la imagen final.

## Checks para Build

- [x] Un solo arco y siete momentos; 20:00 exactos.
- [x] Churn aparece en exactamente un momento visual: M4. No hay setup, reveal ni holdout en otros momentos.
- [x] M4 contiene baseline ≈4%, configuración, QF, regla, n/soporte, tasa, lift/diferencia, quality, holdout e hipótesis de acción.
- [x] M3 muestra la propuesta y arquitectura de pysubgroup antes del caso.
- [x] M5 explica la elección contextual Python 3.10 y compara subgroups sin ranking universal.
- [x] Apertura con tensión y cierre con una sola idea e imagen protagonista.
- [x] Cada momento define afirmación, trabajo narrativo, prueba visible, tratamiento, acción, takeaway, speech y transición.
- [x] SoftClassifierTarget/SubROC es una extensión breve y separada del ejemplo principal.
- [x] Límites explícitos: multiplicidad, soporte, redundancia/solapamiento, asociación ≠ causalidad y sintético ≠ negocio real.
- [x] La interacción propuesta es determinista, reiniciable, operable por teclado y con fallback estático.

## Riesgos que Build debe conservar visibles

1. El smoke test de Python 3.10 y las cifras finales de la única ejecución de churn aún deben realizarse; no presentar objetivos como valores observados.
2. Si la regla no conserva dirección en holdout, la acción pasa a “replicar/revisar”, no “activar”.
3. No usar el posible signo inconsistente de ROCAUCQF/PRAUCQF sin verificar implementación/tests de 0.9.0.
4. Mantener “sintético” visible en toda M4; sus tasas no son benchmark de telecom.
