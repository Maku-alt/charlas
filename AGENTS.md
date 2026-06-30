# AGENTS

Reglas de trabajo para este repo de charlas.

## Contexto
- Cada carpeta de primer nivel es una charla, salvo infraestructura como `agents/`, `templates/`, `outputs/` y carpetas ocultas.
- Audiencia por defecto: gente que trabaja con datos, usualmente `Data Scientists`.
- Tono por defecto: ejecutivo, tecnico, directo y claro.
- No amarrar la narrativa a telco salvo pedido explicito.

## Flujo
Toda charla debe pasar por tesis, research cuando haga falta, convergencia con el usuario, narrativa de `8-10 slides`, build `pptx`, cierre visual y review.

El research no pasa automaticamente a PPT. Primero se discute, se recorta y se fija el angulo.

Cada slide debe tener tesis, lectura ejecutiva, objeto visible y concepto visual. Si varias slides quedan como cajas, tablas o conectores sin idea visual clara, vuelve a narrativa o build antes de aprobar.

## Agentes
- `orchestrator-charlas`: decide fase, dependencias, launch y bloqueo.
- `researcher-charlas`: investiga, tensiona tesis y entrega research discutible.
- `narrative-charlas`: convierte research convergido en narrativa aprobable.
- `deck-builder-charlas`: construye `pptx` editable usando la skill `pptx`.
- `image-closer-charlas`: define imagen editorial de cierre.
- `review-charlas`: valida deck, texto, visuales, cierre y evidencia.

## Estructura por charla
Convencion recomendada:

- `specs/`: specs SDD propios de la charla, copiados o adaptados desde `templates/charlas-sdd/`
- `notes/`: narrativa, claims, material validado, `bibliografia.md` y `agent-log.md`
- `slides/` o `deck/`: fuente editable y exportables
- `assets/`: imagenes, prompts visuales y recursos de soporte
- `review/`: observaciones, ajustes y chequeos finales

La convencion aplica hacia adelante. No migres charlas antiguas salvo que se reabran.

`slides/` y `assets/` deben existir localmente cuando la charla los necesite, pero por defecto no se suben al remoto. El entregable publicable es el `pptx`, junto con notas, specs y review cuando corresponda.

Si hubo research externo, `notes/bibliografia.md` es obligatorio. Si corrio una fase pesada, debe quedar una entrada en `notes/agent-log.md` con agente, modelo, esfuerzo, estado, artefactos, errores o bloqueos, y siguiente accion.

## Specs SDD
La metodologia vive en `templates/charlas-sdd/`.

Usa `full/` para charlas normales o complejas:

- `thesis-spec.md`
- `research-spec.md`
- `narrative-spec.md`
- `build-spec.md`
- `review-spec.md`

Usa `compact/` para charlas pequenas o con framing claro:

- `research-package.md`
- `build-review-package.md`

Los prompts de fase viven en `templates/charlas-sdd/prompts/`.

## Ejecucion
El chat principal orquesta. Las fases pesadas corren por defecto como subagente Codex con contexto acotado:

- rol especializado desde `agents/*.md`
- spec concreto desde `specs/` o `templates/charlas-sdd/`
- prompt de fase desde `templates/charlas-sdd/prompts/`
- artefactos estrictamente necesarios
- `model: gpt-5.5`
- `reasoning_effort: medium`
- `fork_context: false`

El prompt de fase no reemplaza el rol especializado. El padre no debe completar `build` ni `review` si el subagente se bloquea.

El feedback humano posterior a una fase entra por `orchestrator-charlas`, que decide si relanza narrativa, build, imagen final o review.

`modo chat separado` queda como alternativa si el usuario quiere ejecutar una fase manualmente y traer de vuelta solo el output compacto.

Research usa esfuerzo `standard` por defecto. Usa `quick` si el usuario pide algo rapido o de bajo riesgo; usa `deep` si el usuario lo pide o la complejidad lo amerita.

## Precondiciones
- `build` requiere `specs/build-spec.md` y `specs/narrative-spec.md`.
- `review` requiere `specs/review-spec.md`, deck objetivo, `notes/bibliografia.md` cuando aplique, `notes/agent-log.md` y evidencia de build.
- Si falta un spec obligatorio, se corrige el contrato antes de lanzar la fase.

## Bloqueos
Una fase bloqueada debe devolver: estado, fase, bloqueo concreto, artefactos, chequeos fallidos, chequeos exitosos, riesgos residuales y accion propuesta.

El padre registra evidencia y decide si espera, relanza, devuelve a la fase anterior o escala al usuario. No absorbe una fase especializada.

## Cierre y evidencia
Toda charla debe tener tesis clara, comparacion o tradeoff, lectura ejecutiva y cierre editorial fuerte con mensaje breve e imagen alineada.

Verifica con fuentes actuales cualquier claim sobre precios, releases, compatibilidad, costos actuales o casos corporativos recientes.

La imagen final no debe repetir tablas, bullets ni diagramas; debe amplificar el cierre y sentirse editorial, deliberada y distinta.

Cuando el build necesite LibreOffice en Windows, resolver `C:\Program Files\LibreOffice\program\soffice.exe` o usar `scripts/resolve-soffice.ps1` desde la raiz del repo.
