# Minimal Agent Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Simplificar el workflow v2 para crear charlas end to end con un padre liviano, workers acotados y controles minimos de identidad, transicion e integridad del PPTX.

**Architecture:** `agents/workflow-contract.json` sigue siendo la fuente canonica. `notes/phase-summary.md` vuelve a ser el unico handoff operativo; `complete-phase.py` valida y publica atomicamente un sentinel pequeño sin snapshots historicos. Build y review conservan identidad separada, y el PPTX aprobado conserva SHA256 en su frontera.

**Tech Stack:** Python 3 standard library, JSON, Markdown, `unittest`, PowerShell/Git.

## Global Constraints

- El padre no ejecuta fases pesadas ni lee chats, logs o razonamiento de workers.
- Cada worker usa `fork_context: false` y recibe solo rol, spec, prompt, inputs, outputs, sentinel y criterios de aceptacion.
- `agents/workflow-contract.json` es la unica fuente de verdad de fases y transiciones.
- No agregar dependencias, telemetria, base de datos ni historial inmutable.
- Conservar publicacion atomica, rechazo de sentinels viejos, review independiente y hash del PPTX aprobado.
- No modificar los cambios locales existentes en el worktree salvo los archivos enumerados en este plan.

---

## File Map

- `agents/workflow-contract.json`: contrato minimo de fases y campos del sentinel.
- `scripts/agent_workflow/complete-phase.py`: publicacion atomica del sentinel actual.
- `scripts/agent_workflow/workflow_contract.py`: validacion de summary, identidad, transiciones y sentinel.
- `scripts/agent_workflow/validate-workflow.py`: CLI y validacion de templates/documentos.
- `tests/agent_workflow/test_workflow_contract.py`: regresiones del contrato minimo.
- `templates/charlas-sdd/phase-summary.md`: handoff operativo canonico sin campos duplicados.
- `templates/charlas-sdd/execution-package.md`: paquete acotado de una corrida.
- `agents/orchestrator-charlas.md`, `README.md`, `templates/charlas-sdd/README.md`: explicacion operativa breve.
- `skills/worker-handoff/SKILL.md`, `skills/worker-flow-audit/SKILL.md`: protocolo alineado al sentinel minimo.
- `agentes-modulares/notes/phase-summary.md`: ejemplo migrado al contrato minimo.
- `agentes-modulares/notes/aprendizaje-workflow-agentes.md`: aprendizaje practico breve.

---

### Task 1: Reducir la publicacion a summary actual y sentinel minimo

**Files:**
- Modify: `tests/agent_workflow/test_workflow_contract.py`
- Modify: `agents/workflow-contract.json`
- Modify: `scripts/agent_workflow/complete-phase.py`
- Modify: `scripts/agent_workflow/workflow_contract.py`

**Interfaces:**
- Consumes: `notes/phase-summary.md`, `run_id`, `phase`, `attempt`, `launched_at`.
- Produces: sentinel JSON atomico con identidad minima; en fronteras de build/review agrega `worker_id`, `session_id`, `candidate_artifact` y `candidate_sha256` cuando aplican.

- [ ] **Step 1: Reemplazar las expectativas historicas por una prueba roja del sentinel minimo**

En `test_complete_phase_writes_sentinel_after_valid_summary`, exigir que la publicacion no cree snapshots y que el sentinel use el summary actual:

```python
self.assertEqual("notes/phase-summary.md", payload["summary"])
self.assertNotIn("summary_sha256", payload)
self.assertFalse(list(notes.glob("phase-summary.*.md")))
```

Agregar una prueba enfocada:

```python
def test_minimal_sentinel_contains_only_required_completion_metadata(self):
    with tempfile.TemporaryDirectory() as temp_dir:
        notes = Path(temp_dir) / "notes"
        notes.mkdir()
        summary = notes / "phase-summary.md"
        shutil.copy(self.fixture, summary)

        result = self.complete_phase(
            summary,
            run_id="research-contract-20260710-1200",
            phase="research",
        )

        self.assertEqual(0, result.returncode, result.stdout)
        payload = json.loads((notes / ".phase-research.done").read_text(encoding="utf-8"))
        self.assertEqual(
            {
                "contract_version", "run_id", "phase", "attempt",
                "execution_status", "summary", "completed_at",
            },
            set(payload),
        )
```

Mantener tests de candidato/hash en `build`, `review` y release; eliminar los tests cuya unica conducta sea crear, preservar o validar `phase-summary.<run_id>.md`.

- [ ] **Step 2: Ejecutar las pruebas y confirmar RED**

Run:

```powershell
python -m unittest tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_minimal_sentinel_contains_only_required_completion_metadata -v
```

Expected: FAIL porque el sentinel aun contiene `summary_sha256` y se crea un snapshot historico.

- [ ] **Step 3: Simplificar el contrato y la publicacion**

En `agents/workflow-contract.json`:

```json
"current_summary": "notes/phase-summary.md",
"required_sentinel_fields": [
  "contract_version",
  "run_id",
  "phase",
  "attempt",
  "execution_status",
  "summary",
  "completed_at"
]
```

Eliminar `historical_summary_pattern` y `summary_sha256`.

En `complete-phase.py`, eliminar `_write_snapshot_atomically_exclusive`, `hashlib` para el summary y toda creacion/borrado de snapshots. Publicar:

```python
payload = {
    "contract_version": contract["contract_version"],
    "run_id": args.run_id,
    "phase": args.phase,
    "attempt": args.attempt,
    "execution_status": _scalar(summary, "execution status"),
    "summary": f"{summary_path.parent.name}/{summary_path.name}",
    "completed_at": datetime.now(launched_at.tzinfo).isoformat(),
}
```

Conservar `_sentinel_claim`, `_write_atomically`, la validacion previa y los campos condicionales de identidad/candidato.

En `workflow_contract.py`, validar que `summary` sea exactamente `notes/phase-summary.md`; eliminar la comparacion SHA256 del summary y toda bifurcacion entre summary actual e historico.

- [ ] **Step 4: Ejecutar pruebas enfocadas y suite completa**

Run:

```powershell
python -m unittest tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_minimal_sentinel_contains_only_required_completion_metadata -v
python -m unittest discover -s tests/agent_workflow -p "test_*.py" -v
```

Expected: PASS; ningun test depende de snapshots historicos.

- [ ] **Step 5: Commit**

```powershell
git add agents/workflow-contract.json scripts/agent_workflow/complete-phase.py scripts/agent_workflow/workflow_contract.py tests/agent_workflow/test_workflow_contract.py
git commit -m "refactor: simplify phase completion contract"
```

---

### Task 2: Reducir el handoff y rechazar templates ambiguos

**Files:**
- Modify: `tests/agent_workflow/test_workflow_contract.py`
- Modify: `scripts/agent_workflow/validate-workflow.py`
- Modify: `templates/charlas-sdd/phase-summary.md`
- Modify: `templates/charlas-sdd/execution-package.md`

**Interfaces:**
- Consumes: Markdown con secciones H2.
- Produces: template sin encabezados duplicados y validador que falla ante duplicaciones futuras.

- [ ] **Step 1: Escribir la prueba roja de encabezados duplicados**

Agregar:

```python
def test_template_validation_rejects_duplicate_h2_fields(self):
    with tempfile.TemporaryDirectory() as temp_dir:
        template = Path(temp_dir) / "phase-summary.md"
        template.write_text(
            "# Phase Summary\n\n## Worker ID\na\n\n## Worker ID\nb\n",
            encoding="utf-8",
        )
        result = subprocess.run(
            [sys.executable, str(self.validator), "--contract", str(self.contract_path), "--template", str(template)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("Duplicate template field: worker id", result.stdout)
```

- [ ] **Step 2: Ejecutar y confirmar RED**

Run:

```powershell
python -m unittest tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_template_validation_rejects_duplicate_h2_fields -v
```

Expected: FAIL porque el CLI actual colapsa duplicados silenciosamente.

- [ ] **Step 3: Implementar la validacion minima**

En `validate-workflow.py`, antes de `parse_summary`, extraer H2 y rechazar duplicados:

```python
headings = [value.strip().lower() for value in re.findall(r"(?m)^## +(.+?)\s*$", Path(args.template).read_text(encoding="utf-8"))]
duplicates = sorted({heading for heading in headings if headings.count(heading) > 1})
if duplicates:
    for field in duplicates:
        print(f"ERROR: Duplicate template field: {field}")
    return 1
```

En `phase-summary.md`, conservar una sola pareja `Worker ID`/`Session ID` y marcarla como condicional para build, build-fix, review y review-final. Conservar `Candidate SHA256` porque protege el PPTX, no el summary.

En `execution-package.md`, reemplazar la seccion historica por:

```markdown
## completion
The worker overwrites `<talk>/notes/phase-summary.md` and publishes the phase sentinel last with `scripts/agent_workflow/complete-phase.py`. The parent validates run ID, phase, attempt and execution status before reading the summary.
```

- [ ] **Step 4: Verificar template y suite**

Run:

```powershell
python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --template templates/charlas-sdd/phase-summary.md
python -m unittest discover -s tests/agent_workflow -p "test_*.py" -v
```

Expected: `VALID TEMPLATE` y suite PASS.

- [ ] **Step 5: Commit**

```powershell
git add scripts/agent_workflow/validate-workflow.py tests/agent_workflow/test_workflow_contract.py templates/charlas-sdd/phase-summary.md templates/charlas-sdd/execution-package.md
git commit -m "fix: keep phase handoff minimal and unambiguous"
```

---

### Task 3: Alinear la documentacion operativa con el flujo minimo

**Files:**
- Modify: `tests/agent_workflow/test_workflow_contract.py`
- Modify: `README.md`
- Modify: `agents/orchestrator-charlas.md`
- Modify: `templates/charlas-sdd/README.md`
- Modify: `skills/worker-handoff/SKILL.md`
- Modify: `skills/worker-flow-audit/SKILL.md`

**Interfaces:**
- Consumes: contrato minimo implementado en Tasks 1-2.
- Produces: instrucciones que describen el summary actual y sentinel minimo sin reintroducir historia inmutable.

- [ ] **Step 1: Convertir los tests documentales a la regla minima y confirmar RED**

Reemplazar los tests de historia inmutable por:

```python
def test_operational_docs_use_current_summary_without_historical_snapshots(self):
    targets = (
        self.root / "README.md",
        self.root / "agents" / "orchestrator-charlas.md",
        self.root / "templates" / "charlas-sdd" / "README.md",
        self.root / "templates" / "charlas-sdd" / "execution-package.md",
        self.root / "skills" / "worker-handoff" / "SKILL.md",
        self.root / "skills" / "worker-flow-audit" / "SKILL.md",
    )
    for path in targets:
        text = path.read_text(encoding="utf-8")
        self.assertIn("notes/phase-summary.md", text)
        self.assertNotIn("phase-summary.<run_id>.md", text)
        self.assertNotIn("summary_sha256", text)
```

Run:

```powershell
python -m unittest tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_operational_docs_use_current_summary_without_historical_snapshots -v
```

Expected: FAIL por referencias historicas actuales.

- [ ] **Step 2: Reducir cada documento a la misma regla operativa**

Usar este contenido conceptual, sin copiar tablas de fases:

```markdown
El worker sobrescribe `notes/phase-summary.md` y publica el sentinel al final mediante `complete-phase.py`. El padre valida `run_id`, fase, intento y estado; solo entonces lee el summary. La existencia del archivo por si sola no completa una fase.
```

Mantener en `orchestrator-charlas.md` la regla de contexto: `fork_context: false`, inputs minimos, no leer chats/logs y transicionar solo segun `workflow-contract.json`.

En `worker-flow-audit`, auditar identidad, transicion, artefacto y evidencia real; eliminar la exigencia de snapshots historicos del summary.

- [ ] **Step 3: Ejecutar validadores documentales**

Run:

```powershell
python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --check-docs AGENTS.md README.md agents templates/charlas-sdd skills/worker-handoff skills/worker-flow-audit
python -m unittest discover -s tests/agent_workflow -p "test_*.py" -v
```

Expected: `VALID DOC REFERENCES` y suite PASS.

- [ ] **Step 4: Commit**

```powershell
git add README.md agents/orchestrator-charlas.md templates/charlas-sdd/README.md skills/worker-handoff/SKILL.md skills/worker-flow-audit/SKILL.md tests/agent_workflow/test_workflow_contract.py
git commit -m "docs: focus workflow guidance on charla delivery"
```

---

### Task 4: Migrar el ejemplo y registrar el aprendizaje practico

**Files:**
- Modify: `agentes-modulares/notes/phase-summary.md`
- Create: `agentes-modulares/notes/aprendizaje-workflow-agentes.md`
- Modify: `tests/agent_workflow/test_workflow_contract.py`

**Interfaces:**
- Consumes: experiencia de `agentes-modulares` y contrato minimo.
- Produces: example summary valido y una guia de aprendizaje breve, no una nueva especificacion.

- [ ] **Step 1: Agregar una prueba de alcance del aprendizaje**

Agregar:

```python
def test_agentes_modulares_learning_note_stays_practical_and_compact(self):
    note = self.root / "agentes-modulares" / "notes" / "aprendizaje-workflow-agentes.md"
    text = note.read_text(encoding="utf-8")
    for heading in (
        "## Antes", "## Cambio central", "## Flujo", "## Controles minimos", "## Por que importa",
    ):
        self.assertIn(heading, text)
    self.assertLessEqual(len(text.splitlines()), 120)
    self.assertNotIn("phase-summary.<run_id>.md", text)
    self.assertNotIn("summary_sha256", text)
```

- [ ] **Step 2: Ejecutar y confirmar RED**

Run:

```powershell
python -m unittest tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_agentes_modulares_learning_note_stays_practical_and_compact -v
```

Expected: ERROR/FAIL porque el documento aun no existe.

- [ ] **Step 3: Crear el aprendizaje y migrar el summary**

Crear un documento de no mas de 120 lineas con estas secciones exactas:

```markdown
# Aprendizaje: un padre liviano para crear charlas con agentes

## Antes
## Cambio central
## Flujo
## Controles minimos
## Advisor
## Por que importa
## Como usarlo en la siguiente charla
```

Explicar con lenguaje practico: el padre conversa y enruta; research, narrativa, build, imagen y review viven en workers acotados; el contrato ordena sin convertirse en el producto; Advisor es excepcional; el PPTX sigue siendo el entregable.

Actualizar `agentes-modulares/notes/phase-summary.md` al template actual, corrigiendo mojibake visible y sin inventar una fase completada nueva.

- [ ] **Step 4: Validar documento y summary migrado**

Run:

```powershell
python -m unittest tests.agent_workflow.test_workflow_contract.WorkflowContractTests.test_agentes_modulares_learning_note_stays_practical_and_compact -v
python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --summary agentes-modulares/notes/phase-summary.md --allow-migrated-summary-without-sentinel
```

Expected: PASS y `VALID MIGRATED SUMMARY`.

- [ ] **Step 5: Commit**

```powershell
git add agentes-modulares/notes/phase-summary.md agentes-modulares/notes/aprendizaje-workflow-agentes.md tests/agent_workflow/test_workflow_contract.py
git commit -m "docs: capture practical agent workflow learning"
```

---

### Task 5: Verificacion final y limpieza controlada

**Files:**
- Verify: all files changed in Tasks 1-4
- Preserve: `docs/plans/2026-07-12-immutable-phase-history-and-pilot-rerun.md` unless separately committed or explicitly reverted
- Local cleanup only: Python `__pycache__` directories
- Local evidence decision: `smoke-workflow-v2*`

**Interfaces:**
- Consumes: rama implementada.
- Produces: evidencia de que el flujo minimo es coherente y una lista explicita de residuos que requieren decision.

- [ ] **Step 1: Ejecutar toda la verificacion fresca**

Run:

```powershell
python -m unittest discover -s tests/agent_workflow -p "test_*.py" -v
python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --template templates/charlas-sdd/phase-summary.md
python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --check-phase-assets
python scripts/agent_workflow/validate-workflow.py --contract agents/workflow-contract.json --check-docs AGENTS.md README.md agents templates/charlas-sdd skills/worker-handoff skills/worker-flow-audit
python -m py_compile scripts/agent_workflow/workflow_contract.py scripts/agent_workflow/complete-phase.py scripts/agent_workflow/validate-workflow.py
git diff --check develop...HEAD
```

Expected: todos los comandos con exit code 0.

- [ ] **Step 2: Confirmar que la complejidad eliminada no sigue activa**

Run:

```powershell
rg -n "phase-summary\.<run_id>|summary_sha256|historical_summary_pattern" agents scripts/agent_workflow templates/charlas-sdd README.md skills/worker-handoff skills/worker-flow-audit
```

Expected: sin coincidencias operativas; se permiten menciones solo en specs/planes historicos fuera de esos targets.

- [ ] **Step 3: Limpiar solo caches generadas y registrar residuos sin destruir evidencia**

Resolver y verificar que cada `__pycache__` este dentro del worktree antes de eliminarlo con PowerShell `Remove-Item -LiteralPath ... -Recurse`.

No borrar automáticamente `smoke-workflow-v2*` ni la modificacion existente del plan historico. Presentar al usuario dos decisiones separadas: conservar/ignorar la evidencia local o eliminarla; comprometer o descartar la actualizacion del plan.

- [ ] **Step 4: Revisar el diff final contra el objetivo**

Run:

```powershell
git diff --stat develop...HEAD
git diff --name-status develop...HEAD
git status --short --branch
```

Expected: los cambios implementados estan comprometidos; cualquier residuo preexistente queda identificado y no se presenta como parte terminada.

- [ ] **Step 5: Solicitar code review**

Invocar la skill `requesting-code-review`. Si CodeRabbit esta disponible y autenticado, ejecutar su review sobre `develop...HEAD`; si no, informar la limitacion exacta sin atribuirle una revision manual.
