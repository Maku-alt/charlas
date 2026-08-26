# Review and release

Review approves an exact frontend artifact, never effort or builder claims.

## Reviewer boundary

Use a fresh `review_charlas` agent with read-only sandbox and minimal context. It may inspect the candidate, sources and evidence but may not modify frontend, narrative, assets, renders or reports. It returns a structured result; the orchestrator persists it.

## Required checks

- Independently recomputed candidate SHA-256.
- Thesis, narrative, speech, bibliography and source support.
- One full-size inspection of every final render.
- Real-browser navigation, direct position, keyboard, fullscreen, focus and limits.
- Console, page errors, assets, overflow, legibility and reduced motion.
- Interactive initial state, transitions, reset, repeatability, fallback and conceptual fidelity.
- Opening, rhythm and closing image/message.
- Offline behavior when promised.

## Severity and verdict

- `P1`: broken, wrong, incomplete or impossible to present.
- `P2`: material narrative, evidence, visual, interaction, accessibility or runtime defect.
- `P3`: worthwhile polish that does not block presentation.

Approve only with no P1 or P2. A limitation that prevents checking a required gate blocks approval.

## Integrity

Build freezes candidate hash -> Review recomputes and approves that hash -> Orchestrator persists the report -> Release recomputes and promotes the same hash.

Any mutation returns to Build and requires fresh renders and Review. The hash recorded in `review/report.md` is the release authority; no workflow manifest or sentinel is needed.

