# Slide 9 Feedback Fix

## Estado

- fecha local: 2026-06-28
- fase: fix puntual deck-builder-charlas
- estado: completado
- deck canonico: `Knowledge-Repo-01-Cuando-Documentar-Tablas-se-Vuelve-Arquitectura-de-Conocimiento.pptx`
- SHA256 deck canonico: `8DE296CFD8D33583EAC370917D2439137B97D4CD265F1A6DBD64CDFA53964585`

## Cambio aplicado

Se simplifico la slide 9 para resolver feedback humano sobre exceso de texto editorial encima de la cita.

Texto que queda en slide 9:

```text
"The overriding design goal for Markdown's formatting syntax is to make it as readable as possible."
John Gruber, Markdown
```

Texto eliminado de slide 9:

- `Antes de pedirle memoria a un agente, hay que construir una memoria que el equipo pueda mantener`
- `Markdown nacio para legibilidad; esta charla agrega responsabilidad, vigencia y una puerta de consulta.`
- `Delegar razonamiento exige primero conservar decisiones reutilizables.`

## QA puntual

- Regenerado PPTX canonico con `node slides/build-knowledge-repo-01.js`.
- Extraido texto desde XML del PPTX a `review/extracted-text.md`: `slides=9`, `replacement_chars=0`.
- Regenerado PDF con LibreOffice.
- Regenerado render PDF solo de slide 9 en `review/renders/slide-9.png`.
- Inspeccion visual puntual de `review/renders/slide-9.png`: la imagen se preserva, hay aire suficiente y no queda doble mensaje ni bloque extra arriba de la cita.

## No ejecutado

No se hizo review final completa por instruccion explicita.
