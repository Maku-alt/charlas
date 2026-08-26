# Rediseño pendiente — `nichos_ml`

## Estado real

El release actual pasó controles técnicos, pero **fue rechazado por el usuario como producto**. No representa la charla deseada y no debe presentarse mañana sin rediseño.

La falla principal fue de prioridad: la metáfora visual, la validación técnica y el proceso ocuparon el lugar de la necesidad original. La charla debía presentar `pysubgroup`, compararlo con alternativas, justificar por qué es la mejor elección para Python 3.10 y mostrar un único ejemplo teórico de churn.

No repetir research, generación de datos, smoke tests, exploración de conceptos ni imágenes. Las fuentes existentes en `notes/` siguen siendo válidas para el alcance. El ejemplo no necesita ejecutar la librería ni demostrar rendimiento.

## Feedback vinculante del usuario

- `index.html` no comunica el nombre del producto. El archivo final debe llamarse `pysubgroup.html`.
- La librería tarda demasiado en aparecer y no es la protagonista.
- El comparativo existe, pero está tarde, pequeño y sin una decisión visible.
- El ejemplo de churn global 4% está comprimido y parece una prueba técnica.
- El ejemplo debe ser **teórico**, fácil de leer y contener reclamos e indisponibilidad del servicio.
- Hay demasiado espacio vacío y el contenido queda pequeño en el centro.
- La paleta azul petróleo/celeste fue rechazada.
- La dirección “mesa de registro / papel vegetal” no debe conservarse.

## Nombre y promesa

Nombre recomendado del archivo:

`pysubgroup.html`

Título de la charla:

> **pysubgroup: nichos que el promedio esconde**

Promesa en una línea:

> Una forma interpretable de encontrar combinaciones de condiciones donde el target se comporta de manera excepcional.

## Arco de contenido recomendado

La unidad sigue siendo el momento frontend, pero debe sentirse como una presentación directa, no como una experiencia conceptual que haya que descifrar.

### 1. Qué es y por qué importa

- `pysubgroup` visible desde el primer segundo.
- Título, promesa y una regla legible como prueba visual.
- Sin introducción abstracta de varios minutos.

### 2. Qué pregunta responde Subgroup Discovery

- Promedio: resume la población.
- Modelo: predice individuos.
- Clustering: agrupa por similitud.
- Subgroup Discovery: encuentra descripciones interpretables con contraste en el target.
- Una sola comparación conceptual, breve.

### 3. Cómo funciona `pysubgroup`

Mostrar grande y en orden:

`selectors → target → quality function → search algorithm → resultados`

Incluir `BinaryTarget`, `StandardQF` y dos algoritmos de búsqueda como ejemplos reales. Evitar una captura extensa de código.

### 4. Comparativo y ganador contextual

Este debe ser uno de los momentos principales y ocupar casi todo el viewport.

Comparar, como mínimo:

| Criterio | pysubgroup | subgroups | Research especializado |
|---|---|---|---|
| Python 3.10 | Sí | No, versión actual requiere 3.11+ | Variable |
| Filosofía | Framework configurable | Catálogo amplio de algoritmos | Soluciones específicas |
| Uso práctico | Alto | Alto en 3.11+ | Mayor fricción |
| Auditoría de modelos | SoftClassifierTarget / SubROC | No es su foco principal | Depende del proyecto |

El veredicto debe verse sin leer letra pequeña:

> **Nuestro contexto: gana `pysubgroup` porque funciona con Python 3.10 y cubre el caso práctico sin migrar el stack.**

No usar puntuaciones 9.1/9.3 ni afirmar superioridad algorítmica sin benchmark.

### 5. Único ejemplo teórico: churn 4%

Una sola pantalla, sin ejecución en vivo, seeds, holdout, logs ni apariencia de benchmark.

Usar cifras claramente marcadas como ilustrativas:

- Churn global: **4%**.
- Regla teórica: `reclamos_90d ≥ 2 AND indisponibilidad_90d ≥ 3 AND contrato = mensual`.
- Nicho ilustrativo: **12% de churn**.
- Tamaño: mostrar un soporte plausible y fácil de interpretar, por ejemplo **6% de clientes**.
- Lectura: el nicho tiene **3×** la tasa global.
- Acción: investigar calidad de servicio y diseñar una intervención controlada.
- Nota visible: asociación no implica causalidad.

El trabajo visual es la transformación `4% global → combinación de condiciones → 12% en el nicho`. La audiencia debe entenderla en menos de diez segundos.

### 6. Por qué elegimos `pysubgroup`

- Python 3.10.
- API configurable y legible.
- Varios algoritmos de búsqueda y quality functions.
- Extensión útil para auditoría de clasificadores.
- Limitaciones visibles: estado Beta, `numpy<2.0`, documentación mejorable.

### 7. Cierre

Una sola frase:

> **No buscamos otro promedio. Buscamos la combinación que merece atención.**

## Dirección visual

Reemplazar completamente el mundo actual.

- Fondo claro: blanco frío o gris muy claro.
- Texto carbón de alto contraste.
- Azul intenso para `pysubgroup` y estructura.
- Naranja para riesgo, churn y decisión.
- Sin azul petróleo, celeste apagado, papel vegetal, cintas ni textura arquitectónica.
- Usar entre 85% y 92% del viewport útil; evitar contenido pequeño flotando en un campo vacío.
- Títulos grandes y cortos. Cuerpo legible en proyector; como referencia, no bajar de 24–26 px a 1600×900.
- Comparativo y ejemplo deben ocupar el escenario completo, no una tarjeta dentro del escenario.
- Controles discretos, pero visibles.
- Interacción mínima: navegación y, si aporta, una única revelación en el ejemplo `4% → 12%`. Nada más.

## Qué conservar

- Research y bibliografía de `notes/`.
- La explicación de selectors, target, quality function y search.
- El veredicto contextual Python 3.10.
- Los límites estadísticos y de causalidad, expresados brevemente.
- Navegación, teclado, fullscreen y accesibilidad del frontend actual si no condicionan el nuevo diseño.

## Qué descartar

- Dirección “mesa de registro”.
- Comps actuales como autoridad visual; pueden usarse únicamente como anti-referencia.
- Dataset, CSV, ejecución y métricas observadas como contenido de la charla.
- La obligación de justificar la charla mediante smoke tests.
- Densidad de metadata, seeds, versiones secundarias y lenguaje de validación en el ejemplo.

## Criterios de aceptación

- En tres segundos se entiende que la charla es sobre `pysubgroup`.
- El comparativo se encuentra inmediatamente y el ganador contextual es inequívoco.
- El ejemplo muestra claramente 4%, reclamos, indisponibilidad y el nicho teórico.
- No parece una demo en vivo ni una prueba de rendimiento.
- No existe texto central diminuto rodeado de grandes zonas vacías.
- La paleta es clara, enérgica y de alto contraste.
- El archivo entregable se llama `pysubgroup.html`.
- Funciona offline, con teclado y fullscreen.
- Se realiza una sola implementación y una sola verificación visual; no abrir ciclos de research ni concepto.

## Prompt listo para ejecutar mañana

```text
Rediseña la Web Talk ubicada en `nichos_ml` siguiendo `nichos_ml/REDESIGN-HANDOFF.md` como autoridad principal y el feedback actual del usuario por encima del release existente.

Objetivo: producir una presentación directa y clara sobre la librería `pysubgroup`, compararla con alternativas y justificar por qué es nuestra mejor elección contextual bajo Python 3.10. El ejemplo de churn es estrictamente teórico; no ejecutes Python, no regeneres datos y no lo presentes como prueba de la herramienta.

Lee únicamente:
- `AGENTS.md`
- `PRODUCT.md`
- `DESIGN.md`
- `nichos_ml/REDESIGN-HANDOFF.md`
- `nichos_ml/brief.md`
- `nichos_ml/notes/research.md`
- `nichos_ml/notes/bibliografia.md`
- el frontend actual solo como anti-referencia y para rescatar navegación/accesibilidad.

No hagas nuevo research, no uses image generation, no generes conceptos alternativos, no ejecutes smoke tests y no delegues tareas que puedan resolverse en la edición directa. Realiza un único rediseño completo y una verificación visual acotada.

Requisitos centrales:
1. `pysubgroup` aparece desde el primer momento.
2. El comparativo es grande, central y muestra el ganador contextual.
3. Hay un único ejemplo teórico: churn global 4%; reclamos >=2; indisponibilidad >=3; contrato mensual; nicho ilustrativo 12%; soporte ilustrativo 6%; asociación no causalidad.
4. Fondo claro, texto carbón, azul intenso y naranja; eliminar azul petróleo y metáfora de papel vegetal.
5. El contenido ocupa 85–92% del viewport y es legible en proyector.
6. Entregable final `nichos_ml/release/pysubgroup.html`.

Antes de terminar, captura e inspecciona cada momento una sola vez. Si hay defectos, corrígelos en un único batch. Devuelve rutas, hash final y riesgos residuales sin abrir otra ronda salvo que exista un bloqueo material.
```
