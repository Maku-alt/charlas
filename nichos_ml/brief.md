# Brief — PySubgroup: encontrar los nichos que el promedio esconde

## Objetivo

Preparar una Web Talk para la charla interna de Data Science del 26 de agosto de 2026. La audiencia debe comprender qué problema resuelve Subgroup Discovery, conocer la propuesta y arquitectura de `pysubgroup`, compararla con alternativas actuales y entender por qué es la mejor elección contextual para el equipo bajo Python 3.10.

## Audiencia y contexto

- Audiencia mixta de Data Scientists y perfiles de negocio.
- Conocen conceptos generales de datos, segmentación y churn; no se asume conocimiento previo de Subgroup Discovery.
- Duración efectiva: 20 minutos, incluida la demostración.
- Presentación desde navegador y proyector.
- Idioma: español; nombres de API y conceptos técnicos se conservan en inglés cuando ayuden a usar la librería.

## Tesis inicial a investigar

Los promedios y segmentos definidos de antemano pueden ocultar combinaciones pequeñas pero relevantes de condiciones donde el churn se dispara. `pysubgroup` permite buscarlas de manera explícita, configurable e interpretable y, bajo Python 3.10, puede ser una elección más pragmática que alternativas con requisitos incompatibles.

La investigación debe verificar y, si corresponde, corregir esta tesis y las conclusiones previas compartidas por el usuario.

## Alcance de contenido

- Intuición de Subgroup Discovery y diferencia frente a segmentación manual, clustering y un modelo predictivo global.
- Anatomía de `pysubgroup`: selectors, target, quality function y search algorithm.
- Estado actual del proyecto, compatibilidad real con Python 3.10, mantenimiento y limitaciones.
- Comparación proporcionada con `subgroups` y líneas modernas relevantes; evitar un catálogo enciclopédico.
- Veredicto contextual, no un ranking universal.
- Un único momento/slide de ejemplo reproducible de churn con datos sintéticos realistas. El ejemplo demuestra la librería, pero no es el arco principal de la charla.

## Caso demostrativo

Dataset sintético de clientes de telecomunicaciones con, como mínimo:

- churn como target binario;
- cantidad de reclamos;
- indisponibilidad o caídas del servicio;
- antigüedad;
- tipo de plan o contrato;
- variables adicionales solo si ayudan a evitar una regla artificialmente obvia.

La generación debe incluir nichos controlados pero plausibles, semilla fija y suficiente ruido. La demo debe resolverse visualmente en un solo momento/slide: comparar la tasa global con un subgrupo descubierto, mostrar los elementos mínimos de la configuración, explicar la quality function y traducir el hallazgo a una hipótesis de acción. No debe presentar asociación como causalidad ni usar datos reales/internos.

La tasa global de churn debe quedar aproximadamente en 4%, como baseline indicado por el usuario. Los nichos pueden mostrar un uplift material sobre ese promedio, manteniendo tamaños y tasas plausibles.

## Entregable

- Web Talk frontend autocontenida, navegable por teclado, con controles visibles y fullscreen.
- Demo determinista, reiniciable y entendible en proyector, sin dependencia de red para el release.
- Research, bibliografía, narrativa y speech persistidos como evidencia útil.
- Review independiente del candidato exacto antes del release.

## Restricciones y tono

- Priorizar una idea memorable y evidencia visible sobre amplitud.
- Mantener rigor suficiente para DS y traducción clara para negocio.
- Verificar claims volátiles con fuentes actuales y primarias.
- El cierre debe dejar una sola idea vinculada a la tesis.
