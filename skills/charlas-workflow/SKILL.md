---
name: charlas-workflow
description: Orchestrate, research, narrate, build, review, or release a Charlas Web Talk as a canonical frontend presentation. Use for work on talks in this repository; do not use for unrelated websites or historical PPTX maintenance.
---

# Charlas workflow

Move one Web Talk toward an approved frontend experience using the smallest substantive next step. Persist product and evidence, not orchestration ceremony.

## Start

1. Read repository `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`, and the target talk brief or user notes.
2. Inspect only relevant artifacts from the target talk. Do not load generated builds, renders, or historical candidates before they are needed.
3. Detect the earliest unmet gate in [references/phases.md](references/phases.md).
4. Dispatch the bounded specialist with [references/handoffs.md](references/handoffs.md). The main thread owns decisions, integration and release.

## Route

- Research: `researcher_charlas`.
- Narrative and speech: `narrative_charlas`.
- Experience, imagery, frontend, renders and Build QA: `experience_designer_builder_charlas`.
- Independent candidate review: `review_charlas`.

Research is never skipped. The main pipeline is serial; parallelize only substantial independent work with disjoint outputs.

## Load progressively

- Read [references/phases.md](references/phases.md) to detect or advance work.
- Read [references/handoffs.md](references/handoffs.md) only when delegating or accepting a specialist result.
- Before Build or product-level review, read [references/frontend-product-contract.md](references/frontend-product-contract.md).
- Before Review or Release, read [references/review-and-release.md](references/review-and-release.md).

## Non-negotiable invariants

- Research validates the thesis and writes `notes/bibliografia.md` with sources actually used.
- Narrative is the content authority for Build. Return material changes to Narrative instead of silently rewriting the argument.
- Narrative chooses the fewest moments that serve the thesis and time. If the topic contains multiple main arcs, propose a series and ask the user before Build.
- Build loads and uses `impeccable` as its primary design process. Build the canonical frontend directly; do not derive it from PPTX.
- Design moments around the best proof: editorial scene, data, simulation, exploration, demo or another appropriate frontend form. Interaction must teach, not decorate.
- The closing moment has one idea or message and a dominant image connected to the thesis. A quote is optional.
- Review uses a fresh read-only agent against the exact candidate hash and real renders. Any mutation invalidates the verdict.
- Release recomputes SHA-256 and promotes only the unchanged approved candidate.

## State and evidence

Infer state from substantive artifacts. Do not create execution packages, phase summaries, sentinels, snapshots, routing logs or run manifests.

Persist only the brief, research, bibliography, narrative, speech, frontend source and candidate, used assets, final review renders, review/fix-list and release.

