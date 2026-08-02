# Build Spec - Web Talk

## Objetivo

Construir una Web Talk autocontenida desde la narrativa aprobada.

## Inputs

- tesis y audiencia;
- narrativa y secuencia de momentos;
- speech y bibliografia;
- restricciones de tiempo, marca, assets y runtime;
- referencia visual preferida, si existe.

## Direccion

- Skill principal: `impeccable`.
- Construccion directa como frontend; no convertir desde PPTX.
- Apertura, cierre, imagenes y sistema visual pertenecen al mismo builder.
- No cambiar claims ni arco sin devolver el trabajo a narrativa.

## Salidas

- HTML candidato autocontenido y SHA256;
- fuente reproducible;
- assets locales con procedencia;
- renders individuales;
- resultados de lint, test y build;
- evidencia de navegacion, teclado, fullscreen, foco, reduced motion, consola, overflow, assets y offline;
- self-audit y riesgos residuales;
- `notes/phase-summary.md`.

## Build fix

Aplicar solo los items autorizados de `fix-list.json`. Conservar identidad visual y contenido no afectado. Producir hash, renders y evidencia de regresion nuevos. Todo fix exige `review-final`.
