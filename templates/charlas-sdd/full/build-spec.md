# Build Spec

## Narrativa fuente
<link o referencia a narrative spec>

## Formato esperado
- pptx editable
- 8-10 slides
- contact sheet PowerPoint nativo
- review posterior
- si es build-fix: PPTX/source candidato corregido sobre slides indicadas y review-final posterior

## Motor de build
- Para decks `pptx` nuevos desde cero, usar por defecto el renderer local del repo en `scripts/deck_renderer/` desde `deck-spec.json`.
- El theme default es `scripts/deck_renderer/theme-charlas.json`.
- La skill `pptx` queda permitida solo como emergencia o diagnostico avanzado: inspeccion de PPTX, extraccion de texto, unpack/pack, reparacion puntual y diagnostico de XML/estructura cuando los scripts del repo no expliquen el fallo.
- El entregable primario es un `pptx` editable compatible con PowerPoint nativo.

## Sistema visual
- tono visual:
- densidad:
- paleta:
- uso de tablas:
- uso de charts:
- uso de imagenes:
- tratamiento de cierre: imagen protagonista, texto minimo, zona de lectura, recorte y atribucion
- variacion compositiva:
- regla de cover:

## Restricciones
- no romper la tesis por slide
- no meter bullets innecesarios
- no perder legibilidad
- no construir una sucesion de cajas si el concepto visual pide otra composicion
- no entregar slides sin concepto visual reconocible
- no cerrar con imagen accesoria, generica o descuadrada
- preservar tildes y texto correcto
- mantener fuente visible cuando aplique

## Referencias visuales
- <deck previa, estilo, ejemplo, plantilla>

## Evidencia obligatoria de build
- ruta del pptx
- cantidad de slides
- concepto visual por slide
- contact sheet PowerPoint nativo; renders auxiliares si existen
- chequeo textual
- chequeos mecanicos
- estado de render nativo
- riesgos residuales

## Build-fix desde review
Aplica solo cuando el orquestador relanza despues de una review con `requiere cambios`. El paquete debe incluir:

- PPTX/source candidato actual
- slides concretas a corregir
- hallazgos accionables por slide
- criterio de aceptacion
- rutas minimas de entrada, evidencia y salida

Restricciones:

- corregir solo las slides indicadas, salvo dependencia tecnica directa
- no relanzar build completo si los hallazgos son puntuales
- no rehacer research, narrativa ni image-close
- mantener el renderer local como motor para decks nuevos; `pptx` solo para emergencia o diagnostico avanzado: inspeccion, extraccion, unpack/pack, reparacion puntual y diagnostico
- dejar el resultado como artefacto candidato corregido; la aprobacion corresponde a `review-final`
- maximo 1 ciclo build-fix salvo autorizacion explicita del usuario

## QA visual PPTX
- PowerPoint nativo es el gate final de apertura/export.
- Primero inspeccionar solo contact sheet PowerPoint nativo.
- Abrir slides individuales solo si el contact sheet muestra defecto; en build-fix, abrir solo slides afectadas y dependencias visuales directas.
- Maximo 1 ciclo de fix visual y 1 revalidacion PowerPoint nativo, salvo permiso explicito.
- Si PowerPoint nativo falla despues de un fix acotado, registrar un bloqueo explícito.
- LibreOffice/Poppler son auxiliares, no gate de aprobacion; no aprueban build.
