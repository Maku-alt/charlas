# Phases and gates

Advance from the earliest unmet gate. Do not manufacture phase markers.

## Brief

The main orchestrator converges the objective, audience, duration, presentation context, constraints and initial thesis with the user. Ask only for a decision that materially blocks Research.

## Research

Owner: `researcher_charlas`.

Research is mandatory. It tests the thesis, verifies volatile claims, finds contradictions and gathers factual and visual evidence. It writes or updates the research notes and `notes/bibliografia.md` with consultation dates and usable sources.

Ready when the thesis is defensible, uncertainty is explicit, strong claims have evidence and Narrative has enough material to choose a clear angle.

## Narrative

Owner: `narrative_charlas`.

Inputs: brief, approved research and bibliography. Outputs: approved thesis, sequence of moments and matching speech. For every moment define its narrative job, visible proof, experience type, presenter action when applicable, takeaway and transition.

There is no fixed moment count. Use the shortest sequence that carries the argument within the available time. If the material contains multiple main arcs, recommend a series with a concrete split and wait for the user's decision before Build.

Ready when the sequence can be built without inventing claims, content or the argument. Narrative describes visual intent but does not design the frontend.

## Build

Owner: `experience_designer_builder_charlas`.

Before work, load `impeccable` and the frontend product contract. Choose a distinct art direction, build the canonical frontend, integrate local assets, create one full-viewport render per moment and run browser QA.

Interactive moments must have a deterministic initial state, keyboard operation, reset and an understandable reduced-motion or static fallback.

Ready for Review when the exact candidate hash, complete renders, interaction checks and residual risks are available.

## Review

Owner: a fresh `review_charlas` agent, independent from Build and read-only.

Review recomputes the candidate hash, inspects every render at full size and tests the real frontend. It returns `approved` or `requires_changes` with evidence and minimal fixes. The orchestrator persists `review/report.md` and an optional `review/fix-list.md`.

If changes are required, route the smallest correction to Narrative or Build. A new candidate always requires new evidence and Review; there is no separate `review-final` phase.

## Release

Owner: main orchestrator.

Recompute SHA-256 and release only when it matches the hash approved in `review/report.md` and no blocking finding remains. Copy the exact approved frontend and the useful final evidence; do not mutate the candidate during promotion.

