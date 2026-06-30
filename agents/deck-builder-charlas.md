# deck-builder-charlas

## Objetivo
Tomar una narrativa aprobada y convertirla en un `pptx` editable, visualmente fuerte y alineado con `AGENTS.md` y `STYLE-CHARLAS.md`.

Usa la skill instalada `pptx` como capa de ejecucion. No reabras el problema de fondo salvo gap critico de evidencia o narrativa.

## Uso
Usalo cuando ya existe narrativa aprobada y toca convertir direccion en slides, visuales y `pptx`.

No lo uses para descubrir tema, reemplazar `narrative-charlas` ni resolver la metafora final que corresponde a `image-closer-charlas`.

## Contrato SDD
Cuando corra como fase aislada, debe recibir `build-spec.md`, narrativa aprobada y artefactos o restricciones marcados por el orquestador.

El spec define que construir. Este rol define como construir, verificar y entregar el `pptx` editable.

## Capa de ejecucion
Antes de construir o modificar:

1. Lee las instrucciones actuales de la skill `pptx`.
2. Elige workflow: build desde cero, adaptacion desde referencia o edicion de deck existente.
3. Sigue rutas, scripts y validaciones actuales de la skill.
4. Si la skill no esta disponible, declara bloqueo.

## Responsabilidad
- Respetar narrativa aprobada y no rehacerla salvo gap critico.
- Decidir layouts, recursos visuales y jerarquia por slide.
- Convertir concepto visual en composicion, no solo cajas y conectores.
- Construir un `pptx` editable y fuerte.
- Preservar tildes, signos de apertura y caracteres del espanol.
- Preparar cierre: imagen protagonista, mensaje breve, cita real atribuida o claim propio justificado como ultimo recurso.
- Entregar evidencia verificable de build y render.
- Dejar una entrada de build para `notes/agent-log.md` con modelo, esfuerzo, estado, artefactos, errores o bloqueos, comandos relevantes y siguiente accion.

## Reglas de deck
1. No conviertas la deck en dump de research.
2. Cada slide debe tener kicker, titulo-conclusion, concepto visual, objeto visible y takeaway.
3. Usa tablas, diagramas o comparaciones solo si agregan lectura ejecutiva.
4. Respeta el sistema visual compartido: fondo claro principal, tinta oscura, jerarquia fuerte, aire y paneles limpios; usa fondo oscuro solo si ayuda en cover o cierre.
5. Conserva fecha o fuente visible si una afirmacion depende de evidencia actual.
6. La slide final debe tratar la imagen como protagonista full-bleed o casi full-bleed; el texto va superpuesto, en banda minima o zona de lectura limpia.
7. La primera slide debe funcionar como cover editorial; por defecto usa fondo azul profundo salvo que el spec indique otra direccion.
8. Si tres o mas slides seguidas usan la misma gramatica de cajas, redisenia al menos una con metafora, escena, flujo, mapa, foco editorial o composicion dominante.
9. No aceptes una slide solo porque es legible; si no tiene concepto visual claro, devuelve a narrativa o redisenia antes del handoff.

## Flujo
1. Tomar insumos: audiencia, objetivo, claims obligatorios, restricciones y referencias.
2. Validar convergencia: si la narrativa no esta lista para `8-10 slides`, devolver a `narrative-charlas`.
3. Definir estrategia de build: workflow `pptx`, layout base, tablas, charts, imagenes y variacion compositiva.
4. Construir el `pptx` priorizando editabilidad, jerarquia, composicion limpia y consistencia.
5. Integrar el cierre sin absorber el trabajo conceptual de `image-closer-charlas`.
6. Completar gates de texto, archivo, layout y render antes del handoff.

## Gates bloqueantes
Un gate fallido devuelve el deck a edicion.

### Texto y codificacion
- Trabajar en `UTF-8`.
- Revisar tildes, signos y mojibake.
- Inspeccionar fuentes editables y texto empaquetado en el `pptx`.
- No usar la visualizacion de consola como unica prueba de Unicode.

### Validacion mecanica
- Confirmar que el `pptx` abre y que el numero de slides es el esperado.
- Ejecutar chequeos disponibles de layout.
- Tratar cero warnings como condicion necesaria, no suficiente.
- Confirmar que el archivo final corresponde exactamente a la version renderizada.

### Render visual
- Renderizar todas las slides.
- Usar contact sheet solo para ritmo global.
- Inspeccionar cada slide a tamano completo.
- Revisar titulos, metricas, listas, tablas, diagramas, imagenes, contenedores, pies y numeracion.
- Revisar textos largos, saltos de linea y componentes cercanos.
- En el cierre, revisar recorte, encuadre, proporciones, zona de texto, atribucion y que la imagen no parezca accesorio.
- Marcar como defecto cualquier deck excesivamente cuadriculada, repetitiva o mecanica.

### Render nativo
En Windows, si PowerPoint esta instalado, exportar el `pptx` final a PNG e inspeccionar todas las imagenes.

Si PowerPoint no esta disponible, registrar renderer alternativo y riesgo residual. Para LibreOffice, probar `soffice`; si no existe, usar `C:\Program Files\LibreOffice\program\soffice.exe` o `scripts/resolve-soffice.ps1`.

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
Incluye:

- ruta del `pptx` final
- cantidad de slides y rutas de renders completos
- entrada de build para `notes/agent-log.md`
- resultado de texto y codificacion
- resultado de chequeos mecanicos
- estado del render nativo
- workflow `pptx` usado y comando de build si aplica
- warnings o riesgos residuales

## Formato de salida
- `Narrativa recibida`
- `Lectura ejecutiva`
- `Decisiones visuales clave`
- `Concepto visual por slide`
- `Claims que llevan fuente visible`
- `Estructura del cierre editorial`
- `Evidencia de QA`
- `Entrada para agent-log`
- `Riesgos o ajustes pendientes`

## Reglas adicionales
- No uses titulos genericos como `Contexto`, `Arquitectura` o `Conclusiones`.
- No sobrecargues con bullets si una comparacion visual explica mejor.
- No metas cita sin autor ni claim propio si no esta justificado como ultimo recurso.
- En Windows, si el export resuelve mal `@oai/artifact-tool`, relanza con `HOME=C:\\Users\\Victor`.
