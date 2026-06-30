# Agentes de Charlas

Esta carpeta contiene roles especializados. El chat principal usa `orchestrator-charlas` para preparar el paquete de fase y no debe absorber el trabajo pesado de cada rol.

## Roles
- `orchestrator-charlas`: coordina fase, dependencias, launch, paralelizacion y bloqueos.
- `researcher-charlas`: investiga, tensiona tesis y devuelve research discutible.
- `narrative-charlas`: convierte research convergido en narrativa de `8-10 slides`.
- `deck-builder-charlas`: construye `pptx` editable con la skill `pptx` y evidencia de QA.
- `image-closer-charlas`: define metafora e imagen editorial de cierre.
- `review-charlas`: valida el artefacto exacto antes de cerrar.

## Paquete de fase
Cada fase pesada debe ejecutarse con contexto acotado:

- rol especializado desde `agents/*.md`
- spec desde `specs/` o `templates/charlas-sdd/`
- prompt desde `templates/charlas-sdd/prompts/`
- artefactos previos estrictamente necesarios
- `model`, `reasoning_effort` y `fork_context: false` explicitos

El rol no es opcional. Por ejemplo, narrativa requiere `agents/narrative-charlas.md` ademas de `narrative-spec.md` y `run-narrative.md`.

## Mapeo rapido
| Fase | Rol | Spec | Prompt |
|---|---|---|---|
| research | `researcher-charlas` | `research-spec.md` | `run-research.md` |
| narrativa | `narrative-charlas` | `narrative-spec.md` | `run-narrative.md` |
| build | `deck-builder-charlas` | `build-spec.md` | `run-build.md` |
| imagen final | `image-closer-charlas` | cierre en `narrative-spec.md` o `build-spec.md` | `run-image-close.md` |
| review | `review-charlas` | `review-spec.md` | `run-review.md` |

## Dependencias
- `narrative-charlas` depende de research o tesis convergida.
- `deck-builder-charlas` depende de narrativa aprobada.
- `image-closer-charlas` depende de tesis, mensaje final, cita real de referente o fallback justificado, y tono claros.
- `review-charlas` depende de deck parcial o final, cierre y evidencia de build.
- Si hay duda sobre fase o dependencias, empezar por `orchestrator-charlas`.

`deck-builder-charlas` e `image-closer-charlas` pueden correr en paralelo solo si mensaje final, cita/fallback y direccion de cierre ya existen o se fijan antes.

## Artefactos obligatorios
- Si hubo research externo, debe existir `notes/bibliografia.md`.
- Si corrio cualquier fase pesada, debe existir `notes/agent-log.md`.
- Cada entrada del log debe registrar fase, agente, `model`, `reasoning_effort`, estado, artefactos, errores o bloqueos, y siguiente accion.

## Gates de calidad
Una deck no esta terminada solo porque existe un `pptx`. El flujo exige:

- texto espanol correcto y `UTF-8` sin mojibake
- chequeos mecanicos de archivo y layout
- render completo e inspeccion individual a tamano completo
- render nativo de PowerPoint en Windows cuando este disponible
- rechazo de solapamiento, clipping o corrupcion visible aunque los checkers no reporten errores
- rechazo de decks mecanicamente correctas pero pobres: slides sin concepto visual, exceso de grillas o cierre sin imagen editorial real
- bibliografia y `notes/agent-log.md` completos para las fases ejecutadas

`deck-builder-charlas` produce evidencia. `review-charlas` valida de forma independiente. `orchestrator-charlas` impide cerrar si hay hallazgos bloqueantes.

## Uso
- Si llega feedback humano sobre una fase o deck existente, empieza por `orchestrator-charlas`; el orquestador clasifica y relanza el rol que corresponda.
- Usa `researcher-charlas` si falta tesis, evidencia o angulo.
- Usa `narrative-charlas` si toca decidir historia, slide order, titulos-conclusion y cierre antes de construir.
- Usa `deck-builder-charlas` si la narrativa ya fue discutida y toca construir el `pptx`.
- Usa `image-closer-charlas` si el cierre necesita una imagen editorial fuerte.
- Usa `review-charlas` si ya existe artefacto concreto y toca decidir si se aprueba o itera.

## Operacion local
- En Windows, si `@oai/artifact-tool` resuelve mal, relanzar con `HOME=C:\\Users\\Victor`.
- Si `soffice` no aparece en `PATH`, usar `scripts/resolve-soffice.ps1` o `C:\\Program Files\\LibreOffice\\program\\soffice.exe`.
- Los specs y prompts reutilizables viven en `templates/charlas-sdd/`.
