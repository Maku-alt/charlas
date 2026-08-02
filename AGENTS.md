# Charlas

## Producto vigente

Este repositorio crea Web Talks: presentaciones HTML autocontenidas, navegables y listas para exponer. Las PPTX existentes son artefactos historicos; no definen el formato de nuevas charlas. Una exportacion PPTX es opcional y solo se produce cuando el usuario la pide.

Audiencia por defecto: personas que trabajan con datos, normalmente Data Scientists. Tono: ejecutivo, tecnico, directo y claro. Verifica con fuentes actuales precios, releases, compatibilidad, costos y casos recientes.

## Flujo

`thesis-review -> research? -> narrative -> build -> review -> build-fix? -> review-final? -> release`

- El hilo principal actua como `orchestrator-charlas`: decide fase, prepara handoffs, conserva decisiones y publica el release.
- Cada fase pesada se ejecuta con el custom agent TOML correspondiente bajo `.codex/agents/`.
- El orquestador no sustituye research, narrativa, experiencia/build ni review detallado.
- La narrativa aprobada es la unica fuente de contenido del build.
- El builder hace self-audit, pero nunca aprueba su propio artefacto.
- El reviewer debe ser independiente y revisar el hash exacto del candidato.
- Existe como maximo un ciclo normal de fix localizado; todo fix exige `review-final`.

## Roles

- `researcher-charlas`: investiga, tensiona tesis y entrega evidencia discutible.
- `narrative-charlas`: fija tesis, arco, momentos, speech y contrato de contenido.
- `experience-designer-builder-charlas`: absorbe diseño, frontend, apertura, cierre, imagenes y build; usa `impeccable` como skill principal.
- `review-charlas`: valida narrativa, experiencia, accesibilidad, runtime y evidencia sin modificar el candidato.
- `advisor-charlas`: consulta excepcional para decisiones transversales complejas; no es fase ni gate.

Los metodos detallados viven en `agents/*.md`; las fases y transiciones en `agents/workflow-contract.json`; las preferencias de runtime en `agents/runtime-defaults.json`.

## Contrato Web Talk

La salida canonica debe:

- construirse directamente como HTML/CSS/JavaScript o React/TypeScript, nunca mediante conversion desde PPTX;
- usar `impeccable` como flujo principal de diseño y ejecucion frontend;
- funcionar sin dependencia de red en runtime cuando el paquete de release lo requiera;
- ofrecer navegacion por teclado, controles visibles, posicion directa y fullscreen;
- respetar foco visible, contraste y `prefers-reduced-motion`;
- evitar scroll como navegacion primaria;
- incluir bibliografia cuando existan fuentes externas;
- producir renders individuales, pruebas, self-audit y hash del candidato;
- mantener apertura, cierre e imagenes dentro de la responsabilidad del Experience Designer Builder.

Screenshots ayudan a revisar, pero no sustituyen DOM, consola, tests, overflow, assets, navegacion y funcionamiento offline.

## Estructura por charla

- `notes/`: tesis, research, bibliografia, narrativa, speech y `phase-summary.md`.
- `web/` o `talk/`: fuente editable de la Web Talk.
- `assets/`: imagenes y recursos locales con procedencia.
- `specs/`: especificaciones de la charla.
- `review/`: renders, reportes, fix-list y evidencia.
- `release/`: candidato exacto aprobado y su identidad.

No migres charlas historicas salvo que se reabran. Si una charla antigua se reabre para una nueva version, el nuevo entregable sigue este contrato web.

## Workers y publicacion

Los workers reciben paquetes acotados con inputs, outputs permitidos, criterios de aceptacion y `fork_context: false`. Se comunican mediante resultados estructurados y artefactos validados. El hilo principal integra, verifica y decide la siguiente transicion.

Si hubo research externo, `notes/bibliografia.md` es obligatorio. Si corrio una fase pesada, `notes/phase-summary.md` debe representar el estado actual. Release solo promueve el hash aprobado por review o review-final.

## Validacion

Antes de cerrar una charla exige:

- tesis y arco claros;
- una lectura ejecutiva y objeto visible por momento;
- HTML construido y probado;
- renders inspeccionados individualmente;
- navegacion, teclado, fullscreen, consola, assets, overflow, accesibilidad y offline verificados;
- bibliografia cuando corresponda;
- review independiente aprobada sobre el archivo exacto.

Los scripts de `scripts/deck_renderer/` y la skill `pptx` quedan como soporte legado para presentaciones historicas, no como ruta normal de nuevas Web Talks.
