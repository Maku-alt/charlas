# deck-builder-charlas

## Objetivo
Tomar una narrativa aprobada y convertirla en un `pptx` editable, visualmente fuerte y alineado con `AGENTS.md` y `STYLE-CHARLAS.md`.

Para decks `pptx` nuevos desde cero, usa por defecto el renderer local del repo: `deck-spec.json` + `scripts/deck_renderer/render-deck.js`.

La skill `pptx` queda permitida solo como emergencia o diagnostico avanzado: inspeccion de PPTX, extraccion de texto, unpack/pack, reparacion puntual y diagnostico de XML/estructura cuando los scripts del repo no expliquen el fallo.

## Uso
Usalo cuando ya existe narrativa aprobada y toca convertir direccion en slides, visuales y `pptx`.

Tambien usalo para `build-fix` despues de una review con `requiere cambios`, pero solo con paquete minimo del orquestador y solo sobre las slides indicadas.

No lo uses para descubrir tema, reemplazar `narrative-charlas` ni resolver la metafora final que corresponde a `image-closer-charlas`.

## Contrato SDD
Cuando corra como fase aislada, debe recibir `build-spec.md`, narrativa aprobada y artefactos o restricciones marcados por el orquestador.

Si corre en `modo chat separado` o hilo worker separado, el handoff operativo es `notes/phase-summary.md`: sobrescribelo con el estado actual, escribe `notes/.phase-build.done` al terminar y responde en chat solo `DONE: summary written` o `BLOCKED: summary written`. No uses `agent-log.md` ni `phase-summary-build.md`.

Si corre en paralelo con `image-closer-charlas`, puede escribir temporalmente `notes/.phase-build.summary.md` en vez de sobrescribir `notes/phase-summary.md`. Debe escribir igual `notes/.phase-build.done`; el padre consolidara despues con `notes/.phase-image.summary.md`.

Formato de `notes/phase-summary.md`: `Ultima fase`, `Estado`, `Pasa / no pasa`, `Resumen`, `Artefactos`, `Hallazgos bloqueantes` y `Siguiente accion`.

En build/review debe indicar si el flujo esta en `build` o `build-fix`, el artefacto candidato actual, el artefacto final si existe, hallazgos bloqueantes restantes y siguiente accion.

## Capa de ejecucion
Antes de construir o modificar:

1. Para decks nuevos normales, genera o actualiza `deck-spec.json` y renderiza con `scripts/deck_renderer/render-deck.js`.
2. Ejecuta `scripts/deck_renderer/qa-deck.py` y `scripts/deck_renderer/validate-powerpoint.ps1`.
3. Si el problema es de contenido o layout soportado, corrige `deck-spec.json` o el layout del renderer y regenera.
4. Usa `scripts/deck_renderer/patch-pptx-text.py` solo para fixes textuales quirurgicos que no ameriten regenerar.
5. Usa la skill `pptx` solo si el trabajo exige inspeccion, extraccion, unpack/pack, reparacion puntual o diagnostico de estructura no cubierto por scripts.

## Responsabilidad
- Respetar narrativa aprobada y no rehacerla salvo gap critico.
- En `build-fix`, corregir solo las slides indicadas por el orquestador y no rehacer research, narrativa, image-close ni build completo para hallazgos puntuales.
- Decidir layouts, recursos visuales y jerarquia por slide.
- Convertir concepto visual en composicion, no solo cajas y conectores.
- Construir un `pptx` editable y fuerte.
- Preservar tildes, signos de apertura y caracteres del espanol.
- Preparar cierre con imagen protagonista, mensaje breve, cita real atribuida o fallback justificado.
- Entregar evidencia verificable de build, texto, archivo y render.
- Actualizar `notes/phase-summary.md` con estado, pasa/no pasa, rutas, bloqueos, riesgos y siguiente accion.

## Reglas de deck
1. No conviertas la deck en dump de research.
2. Cada slide debe tener kicker, titulo-conclusion, concepto visual, objeto visible y takeaway.
3. Usa tablas, diagramas o comparaciones solo si agregan lectura ejecutiva.
4. Respeta el sistema visual compartido: fondo claro principal, tinta oscura, jerarquia fuerte, aire y paneles limpios; usa fondo oscuro solo si ayuda en cover o cierre.
5. Conserva fecha o fuente visible si una afirmacion depende de evidencia actual.
6. La slide final debe tratar la imagen como protagonista full-bleed o casi full-bleed.
7. La primera slide debe funcionar como cover editorial; por defecto usa fondo azul profundo salvo que el spec indique otra direccion.
8. Si tres o mas slides seguidas usan la misma gramatica de cajas, redisenia al menos una con metafora, escena, flujo, mapa, foco editorial o composicion dominante.
9. No aceptes una slide solo porque es legible; si no tiene concepto visual claro, devuelve a narrativa o redisenia antes del handoff.

## Flujo
1. Tomar insumos: audiencia, objetivo, claims obligatorios, restricciones y referencias.
2. Validar convergencia: si la narrativa no esta lista para `8-10 slides`, devolver a `narrative-charlas`.
3. Definir estrategia de build: `deck-spec.json`, layouts del renderer, tablas, charts, imagenes y variacion compositiva.
4. Construir el `pptx` con el renderer local priorizando editabilidad, jerarquia, composicion limpia y consistencia.
5. Integrar el cierre sin absorber el trabajo conceptual de `image-closer-charlas`.
6. Completar gates antes del handoff.

## Build-fix desde review
Si el encargo es `build-fix`, el paquete debe traer: PPTX/source candidato actual, slides concretas a corregir, hallazgos accionables por slide, criterio de aceptacion y rutas minimas. Si falta alguno, registra bloqueo de transicion.

Reglas del fix:

- editar solo slides indicadas, salvo que una dependencia tecnica obligue a tocar un recurso compartido
- aplicar el cambio minimo sugerido o uno equivalente que cumpla el criterio de aceptacion
- para hallazgos de contenido/layout, corregir primero `deck-spec.json` o layout y regenerar; para texto puntual, preferir `patch-pptx-text.py`
- no relanzar build completo pesado si los hallazgos son puntuales
- no rehacer research, narrativa ni image-close
- dejar claro que el artefacto resultante es candidato corregido, no final aprobado
- actualizar `notes/phase-summary.md` con `Ultima fase: build-fix`, `Pasa / no pasa`, artefacto candidato actual, artefacto final si existe, hallazgos restantes y `Siguiente accion: review-final`
- escribir `notes/.phase-build.done` al terminar en modo aislado, limpiando o ignorando cualquier sentinel anterior segun indique el orquestador

## Gates bloqueantes
Un gate fallido devuelve el deck a edicion.

### Texto y mecanica
- Trabajar en `UTF-8`; revisar tildes, signos, mojibake y texto empaquetado en el `pptx`.
- No usar la visualizacion de consola como unica prueba de Unicode.
- Confirmar que el `pptx` abre, que el numero de slides es el esperado y que el archivo final corresponde exactamente a la version renderizada.
- Ejecutar chequeos disponibles de layout. Cero warnings es necesario, no suficiente.

### Render visual
- PowerPoint nativo es el gate final de apertura/export para entregables `pptx`.
- Primero inspeccionar solo contact sheet generado con PowerPoint nativo.
- Abrir slides individuales solo si el contact sheet muestra defecto; en `build-fix`, abrir solo las slides afectadas y dependencias visuales directas.
- Revisar titulos, metricas, listas, tablas, diagramas, imagenes, contenedores, pies y numeracion.
- Revisar textos largos, saltos de linea y componentes cercanos.
- En el cierre, revisar recorte, encuadre, proporciones, zona de texto, atribucion y protagonismo de imagen.
- Marcar como defecto cualquier deck excesivamente cuadriculada, repetitiva o mecanica.
- Hacer maximo 1 ciclo de fix visual y 1 revalidacion PowerPoint nativo, salvo permiso explicito.

Si PowerPoint nativo falla, hacer maximo 1 intento acotado de fix. Si persiste, registrar bloqueo en `notes/phase-summary.md`; no aprobar por LibreOffice/Poppler. LibreOffice/Poppler son auxiliares, no gate de aprobacion. Para LibreOffice, probar `soffice`; si no existe, usar `C:\Program Files\LibreOffice\program\soffice.exe` o `scripts/resolve-soffice.ps1`.

## Fallos que bloquean handoff
- mojibake o caracteres danados
- texto cortado, desbordado o fuera de contenedor
- listas, metricas, labels o rails solapados
- tablas o diagramas ilegibles
- composicion repetitiva que debilita varias slides
- slide sin concepto visual claro
- cierre sin imagen editorial real cuando el spec la pide
- cierre con imagen accesoria, descuadrada, generica o sin cita real/fallback justificado
- colision visible aunque el checker reporte cero errores
- diferencia entre archivo final y archivo revisado

## Evidencia de entrega
Incluye ruta del `pptx`, cantidad de slides, `deck-spec.json` usado cuando aplique, contact sheet PowerPoint nativo, renders auxiliares si existen, `notes/phase-summary.md`, sentinel en modo aislado, resultados de texto/mecanica/render, workflow usado, comando de build si aplica, warnings y riesgos residuales.

En `build-fix`, incluye ademas slides corregidas, hallazgo de review que atiende cada cambio, criterio de aceptacion aplicado y rutas de evidencia del fix. No declares aprobado el deck; la siguiente accion es `review-final`.

## Formato de salida
En `modo chat separado` o hilo worker separado, responde solo `DONE: summary written` o `BLOCKED: summary written`.

Fuera de ese modo, usa: `Narrativa recibida`, `Lectura ejecutiva`, `Decisiones visuales clave`, `Concepto visual por slide`, `Claims que llevan fuente visible`, `Estructura del cierre editorial`, `Evidencia de QA`, `Phase summary` y `Riesgos o ajustes pendientes`.

## Reglas adicionales
- No uses titulos genericos como `Contexto`, `Arquitectura` o `Conclusiones`.
- No sobrecargues con bullets si una comparacion visual explica mejor.
- No metas cita sin autor ni claim propio si no esta justificado como ultimo recurso.
