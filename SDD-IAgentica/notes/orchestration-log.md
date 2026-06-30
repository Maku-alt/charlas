# Orchestration Log

## Objetivo del experimento
Probar el flujo del repo para una charla nueva sobre SDD e IA agentica, usando subagentes Codex con contexto acotado y registrando si el comportamiento coincide con el diseno del repositorio.

## Decisiones iniciales
- Carpeta de charla: `SDD-IAgentica`
- Modo SDD: `full`, porque la charla combina tesis metodologica, claims sobre contexto y build completo.
- Audiencia: Data Scientists y tecnicos que ya usan IA en trabajo real.
- Angulo elegido: SDD como empaquetado de contexto y contrato operacional para subagentes.
- Restriccion clave: no prometer cifras exactas de ahorro de tokens sin medicion; se permite una estimacion propia si queda rotulada como orden de magnitud.

## Plan de fases
1. Crear specs.
2. Ejecutar research en subagente sin historial completo.
3. Ejecutar narrativa en subagente sin historial completo, usando research y spec.
4. Construir PPT editable localmente con evidencia de render.
5. Generar o integrar imagen editorial final.
6. Ejecutar review con contexto acotado y registrar veredicto.

## Criterio de exito
- Existe un `pptx` editable de 8-10 slides.
- Existe imagen final alineada al cierre.
- Existen renders verificables.
- La review no reporta P1 ni P2 al cierre.
- Queda una lectura explicita sobre si los subagentes siguieron el diseno del repo.

## Ejecucion observada
- `researcher-charlas`: corrio como subagente con `fork_context=false`, recibio solo spec, tesis, agente local, estilo y prompt de fase. Produjo `notes/research-brief.md` y decision `seguir`.
- `narrative-charlas`: corrio como subagente con contexto acotado. Produjo `notes/narrative-brief.md` y decision `listo para build`.
- `deck-builder-charlas`: el build se ejecuto localmente desde `slides/build_deck.py`, usando `python-pptx`, imagen final generada y renders completos.
- `review-charlas`: primera pasada con contexto acotado detecto correctamente un P2 visual en slide 2 y marco `requiere cambios`.
- Correccion: se ajusto slide 2, se regenero el PPTX y se reexportaron renders nativos.
- `review-charlas` v2 style: pasada final acotada aprobo el artefacto alineado con `STYLE-CHARLAS.md`, versionado como `SDD-IAgentica/SDD-IAgentica-v2.pptx`, con SHA256 `DCA25F0C473F937402FC56D89C09AB1C682433D800F031BB5BB62AB111F4A00C`.

## Decision de version final

- La version valida para publicar y versionar es `SDD-IAgentica/SDD-IAgentica-v2.pptx`.
- La prueba posterior sin dependencia de `STYLE-CHARLAS.md` queda descartada como version final.
- Las fuentes editables permanecen en `slides/` y los assets en `assets/`, ambos locales/no remotos por defecto.

## Conclusion del experimento
Los subagentes se comportaron como fue disenado el repo:

- no heredaron el historial completo del chat principal;
- trabajaron con specs y artefactos de entrada delimitados;
- produjeron salidas compactas en archivos esperados;
- respetaron las fronteras de fase: research no construyo PPT, narrativa no hizo build, review no reconstruyo;
- el reviewer agrego valor real al detectar un defecto que el builder habia pasado por alto;
- el chat principal funciono como orquestador: registro decisiones, integro outputs, corrigio el P2 y relanzo review.

El patron si mostro la ventaja esperada: la conversacion principal no tuvo que cargar todo el razonamiento interno de cada fase, solo los artefactos y decisiones de continuidad.
