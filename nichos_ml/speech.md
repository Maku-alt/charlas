# Speech — PySubgroup: encontrar los nichos que el promedio esconde

**Contrato:** charlas-specialist-result-v1 · speech para la narrativa aprobada  
**Duración:** 20:00, incluida la demostración  
**Uso:** acompaña las pruebas visuales; no repite como inventario todas las etiquetas de pantalla.

## 1. La pregunta que el promedio no responde — 2:00

“Un promedio nos dice cuánto hay en el conjunto, pero puede dejar abierta la pregunta que importa para actuar: ¿dónde se concentra el contraste?

Hoy no vamos a negar el valor de los promedios ni a prometer que siempre exista un nicho extraordinario. Vamos a mirar una herramienta que hace explícita la búsqueda de una región legible: una combinación de condiciones que podamos revisar, validar y discutir.”

**Acción:** pausar después de “¿dónde se concentra el contraste?”. No presentar aún el ejemplo de churn ni una cifra de demo.

**Puente:** “Antes de ver pysubgroup, comparemos esta pregunta con las lentes que ya tenemos.”

## 2. Tres lentes y una pregunta distinta — 2:30

“Un segmento manual puede ser operativo, pero sus cortes fueron escogidos antes de mirar esta búsqueda. Un cluster organiza por similitud de covariables; eso no garantiza que la región tenga un target distinto. Un modelo global puede ordenar clientes individualmente, aunque su ranking no nos entregue una regla colectiva que negocio pueda leer.

No estoy diciendo que estas herramientas fallen ni que haya que reemplazarlas. Estoy separando preguntas. Subgroup Discovery pregunta qué combinación explícita de condiciones cubre una región cuyo target contrasta con la población.

Es otra vista del mismo problema: complementa segmentos, clusters y modelos porque pone en primer plano una descripción interpretable del contraste.”

**Acción:** al señalar cada ruta decir “responde otra pregunta”. Evitar “mejor” o “peor”.

**Puente:** “Esa pregunta se vuelve útil cuando su salida es una regla que podemos leer y discutir.”

## 3. La propuesta de pysubgroup en cinco piezas — 4:00

“La arquitectura de pysubgroup cabe en cinco decisiones.

Los selectors describen qué filas cubre cada condición. El target define qué estamos contrastando; para un target binario, la API ofrece BinaryTarget. La quality function puntúa el contraste con la población y hace visible el intercambio con el tamaño. El algoritmo explora el espacio de descripciones, mientras la profundidad acota la complejidad. Finalmente, el soporte mínimo y la revisión humana protegen la interpretación.

En la configuración que veremos usaremos selectors creados a partir de las columnas, BinaryTarget, WRAccQF o StandardQF(alpha=1), una búsqueda acotada y MinSupportConstraint.

La fórmula de calidad no es un sello de verdad. Es una declaración de qué llamamos interesante para ordenar la revisión. Por eso una regla top-1 sin n no es una afirmación completa: no sabemos si la tasa la sostienen cientos de filas o unas pocas.”

**Acción:** revelar cada pieza de izquierda a derecha. En QF, explicar “contraste y tamaño” sin derivar la fórmula completa.

**Puente:** “Veamos todas esas piezas juntas, una sola vez, en un caso reproducible.”

## 4. El único ejemplo: churn, de configuración a hipótesis — 4:00

“Este es el único momento de la charla con datos de telecom, churn y tasas. El ejemplo es sintético: tiene semilla fija, ruido y una interacción controlada, pero no es evidencia de una telco ni un benchmark del sector.

En la misma vista vemos la procedencia, la configuración, el baseline cercano al cuatro por ciento y una regla descubierta. Primero leo cuántas filas la sostienen y cuál es su soporte. Después comparo la tasa del subgrupo con el baseline, miro el lift y la quality. Finalmente compruebo si la dirección continúa en holdout.

La configuración no está separada de la conclusión: esta es precisamente la relación que queremos enseñar. Si la regla conserva su dirección, se vuelve un candidato razonable para investigar. Si baja mucho o no se replica, ese resultado también informa.

La traducción operativa es limitada: priorizar una revisión de calidad y retención para clientes con este patrón. No demuestra que una condición cause churn, no autoriza una oferta a todos y no convierte la asociación en causalidad.”

**Acción:** avanzar dentro de la única composición en el orden configuración → baseline → regla y métricas → holdout → hipótesis. Señalar n antes de la tasa. No abrir un segundo momento para la preparación o la validación.

**Fallback de ejecución:** “La interacción no está respondiendo; paso al resultado precalculado de la misma semilla. La lectura no cambia: en esta única composición siguen visibles configuración, baseline, regla, tamaño, contraste y holdout.”

**Fallback si holdout no confirma:** “La regla contrastó en discovery, pero no conserva dirección fuera de muestra. La salida responsable es replicar o revisar, no activar.”

**Puente:** “La demo muestra la mecánica; la decisión de adopción depende del entorno real y de las alternativas.”

## 5. Por qué esta elección contextual en Python 3.10 — 3:30

“Mi veredicto no es un ranking universal. Es una decisión para este equipo, este stack y este alcance.

Con pysubgroup 0.9.0, NumPy 1.26.4, scikit-learn 1.7.2, pandas 2.x y dependencias compatibles fijadas, la API compacta es una opción pragmática bajo Python 3.10. El proyecto declara estado Beta y la actividad visible después de la release es limitada; por eso el entorno debe fijarse y el import y las APIs deben pasar un smoke test.

subgroups es una alternativa relevante, más reciente y con un catálogo más amplio, pero su metadata actual exige Python 3.11 o superior. SYFLOW y Constrained Subgroup Discovery muestran líneas de investigación más expresivas o con restricciones, pero no son un reemplazo drop-in validado para esta demo. Puede ser preferible otra opción si migramos de versión o necesitamos esas familias de algoritmos. No hemos hecho un benchmark común de calidad o velocidad, así que no decimos que una librería sea superior en general.

La frase correcta es ‘encaja mejor en nuestras restricciones actuales’. Si cambian Python, la política de NumPy o el alcance de algoritmos que necesitamos, el veredicto debe revisarse.”

**Acción:** poner énfasis en “para este contexto”; no mostrar score agregado ni medallas.

**Puente:** “Elegir la herramienta no elimina las preguntas estadísticas que quedan después de encontrar una regla.”

## 6. Extensión y límites que protegen la lectura — 2:30

“El buscador prueba muchas descripciones. Un p-value posterior no convierte automáticamente esa exploración en confirmación. El soporte mínimo protege estabilidad, aunque un soporte más alto también puede ocultar nichos. Varias reglas pueden cubrir casi a las mismas personas. Y asociación no es causalidad: para atribuir un efecto necesitamos temporalidad, control de confusión o experimento.

SoftClassifierTarget y SubROC responden una pregunta posterior: dado un clasificador y sus scores, ¿en qué regiones rinde diferente? Es una extensión de auditoría del modelo, no la forma natural de buscar directamente el churn observado del único ejemplo. Por eso queda separada y breve.

La herramienta encuentra candidatos interpretables. La confirmación requiere otro diseño.”

**Acción:** recorrer los cuatro límites en una frase cada uno. Mantener la extensión por debajo de 30 segundos y no abrir una segunda demo. No mostrar signo de ROC-AUC/PR-AUC sin verificar implementación/tests de 0.9.0.

**Puente:** “Con esa frontera clara, queda una sola idea sobre la elección.”

## 7. Una pregunta explícita para saber dónde mirar — 1:30

“No nos llevamos un ranking universal ni la promesa de que una regla observacional sea causal.

Nos llevamos una decisión y una práctica: bajo Python 3.10, fijar el entorno y usar pysubgroup para buscar descripciones legibles; después exigir tamaño, holdout y revisión.

El promedio dice cuánto; pysubgroup hace explícito dónde mirar.”

**Acción:** dejar la imagen y la frase final en silencio unos segundos. Repetir la frase una sola vez. No añadir un resumen técnico.

## Recuperación general

- Si falla la ejecución en vivo, usar el estado precalculado de la misma semilla, etiquetarlo como fallback y mantener la única composición de churn.
- Si falla la búsqueda, no inventar un top-1: mostrar el contrato de búsqueda y el resultado precalculado ya validado, o declarar que no se puede certificar en ese momento.
- Si holdout no conserva dirección, sustituir “candidato a acción” por “candidato a replicación/revisión”.
- Si un control no responde, avanzar linealmente por los estados de la única composición; el público debe seguir la historia sin interacción.
