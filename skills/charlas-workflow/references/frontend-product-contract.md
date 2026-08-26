# Frontend product contract

The canonical deliverable is a presentational frontend built directly with `impeccable`. It may use HTML/CSS/JavaScript or React/TypeScript; never convert PPTX into the canonical artifact.

## Presentation surface

- Sequence of addressable moments without scroll as the primary route.
- Visible previous/next controls, direct position, keyboard navigation and fullscreen.
- Stage 16:9 by default, with full-viewport moments when the experience benefits.
- Controls remain available without competing with content.
- Visible focus, semantic labels, sufficient contrast and reduced-motion support.
- Local asset integrity and offline operation when promised.

## Moments

Choose the form that best proves the idea: editorial composition, data visualization, comparison, transformation, simulation, exploration, guided demo, code or image-led scene.

For each interactive moment:

- make the presenter action and audience payoff obvious;
- use a deterministic initial state and reproducible transitions;
- provide reset and keyboard operation;
- prevent interaction from trapping presentation navigation;
- provide a static or reduced-motion fallback;
- disclose conceptual simplifications in simulations;
- keep the experience legible on a projector.

The closing moment contains one message or idea and a dominant image connected to the thesis. It is not a summary screen. A verified quote may support it but is not required.

## Build evidence

- Exact candidate path and SHA-256.
- One numbered full-viewport render per moment.
- Results for navigation, direct position, keyboard, fullscreen, reset, assets, console, overflow, accessibility and offline behavior when applicable.
- Individual inspection of every moment plus unresolved risks.

