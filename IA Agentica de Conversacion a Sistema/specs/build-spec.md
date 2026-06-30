# Build Spec

## Narrativa fuente

- `specs/narrative-spec.md`
- `notes/narrative-brief.md`
- `notes/research-brief.md`

## Formato esperado

- pptx editable
- 9 slides
- render completo
- review posterior con `review-charlas`

## Sistema visual

- tono visual: ejecutivo, tecnico, didactico y sobrio; madurez operativa, no hype futurista
- densidad: media; una tesis por slide, poco texto, objeto de prueba visible claro
- paleta: usar `STYLE-CHARLAS.md` como base
  - fondo claro principal `#F4F0E8`
  - tinta principal `#0F172A`
  - azul profundo `#102A43`
  - acento naranja `#C75C2A`
  - acento verde `#2D6A4F`
  - rojo riesgo `#B42318`
- uso de tablas: solo cuando muestren tradeoff o matriz de decision
- uso de charts: no usar charts cuantitativos; no hay benchmark propio
- uso de imagenes: usar una imagen editorial fuerte en el cierre; el resto puede apoyarse en diagramas, matrices, iconos y objetos visuales editables
- tratamiento de cierre: fondo oscuro o imagen full-bleed con overlay sobrio; mensaje principal, cita atribuida y fuente discreta

## Restricciones

- no romper la tesis por slide
- no meter bullets innecesarios
- no perder legibilidad
- preservar tildes y texto correcto
- mantener fuente visible cuando aplique
- no presentar IA web como mala; presentarla como punto de partida valido
- no vender una estructura de carpetas como estandar obligatorio
- no mencionar proveedores como comparacion competitiva
- no usar claims cuantitativos de productividad
- no agregar precios, releases, politicas de datos o casos corporativos recientes sin validacion actual

## Referencias visuales

- `STYLE-CHARLAS.md`
- decks previas del repo como familia visual, sin copiar metafora de cierre:
  - `Harness Engineer/Harness-Engineering-Data-Science.pptx`
  - `SDD-IAgentica/SDD-IAgentica-v2.pptx`

## Slides a construir

### Slide 1
- kicker: Cambio de unidad
- titulo: IA agentica empieza cuando la conversacion se convierte en sistema
- objeto visible: comparacion chat aislado vs workspace con reglas, contexto, tools, estado y review
- takeaway: no se trata de abandonar IA web, sino de saber cuando ya no alcanza

### Slide 2
- kicker: El caso que todos reconocen
- titulo: Un analisis se rompe cuando el contexto vive solo en el chat
- objeto visible: flujo de analisis de negocio hacia features con inputs, hipotesis, decisiones, archivos y outputs dispersos
- takeaway: el problema no es solo la calidad de la respuesta, sino la continuidad del trabajo

### Slide 3
- kicker: Que cambia con un agente
- titulo: Un agente no solo responde: usa herramientas y modifica artefactos
- objeto visible: tres verbos, observar, decidir, actuar, conectados a limites operativos
- takeaway: actuar exige limites operativos

### Slide 4
- kicker: Rendimiento real
- titulo: Los agentes son tan buenos como el entorno que les damos
- objeto visible: cita de Anthropic y ejemplos de tools de Data Science
- takeaway: herramientas, contexto e instrucciones son parte del diseno, no accesorios
- fuente visible: Anthropic Engineering, `Writing tools for agents`, 2025

### Slide 5
- kicker: Sistema minimo
- titulo: No necesitamos una carpeta unica; necesitamos responsabilidades claras
- objeto visible: matriz de responsabilidades: reglas, contexto, datos permitidos, estado, outputs, decisiones y review
- takeaway: la estructura debe ser adaptable, pero las responsabilidades no son opcionales

### Slide 6
- kicker: Seguridad operativa
- titulo: La autonomia solo escala con permisos pequenos y revision humana
- objeto visible: mapa riesgo-control: datos sensibles, sandbox, scopes, approvals, logs, cambios revisables
- takeaway: los controles no frenan el uso de agentes; son lo que permite usarlos en trabajo real
- fuentes visibles discretas: OWASP LLM06, NIST AI 600-1

### Slide 7
- kicker: Traduccion a Data Science
- titulo: Para analisis y features, el estado visible es parte del metodo
- objeto visible: caso con `state.md` o equivalente, notebooks, scripts, fuentes, pendientes, outputs y revision
- takeaway: trazabilidad no es documentacion extra; permite revisar, retomar y transferir el trabajo

### Slide 8
- kicker: Criterio de adopcion
- titulo: El sistema minimo debe ayudar mas de lo que estorba
- objeto visible: matriz de decision por exploracion, trabajo recurrente, trabajo sensible y automatizacion
- takeaway: no todo amerita agente; el criterio es recurrencia, sensibilidad, trazabilidad y costo de error

### Slide 9
- kicker: Cierre editorial
- titulo: La IA no reemplaza el sistema de trabajo. Lo exige.
- objeto visible: imagen editorial de mesa/banco de trabajo con herramientas, bitacora, permisos/llaves, artefactos en revision y humano decidiendo
- cita: "Agents are only as effective as the tools we give them." - Anthropic
- fuente visible: Anthropic Engineering, `Writing tools for agents`, 2025
- takeaway: el valor no esta en soltar al agente, sino en darle un lugar seguro donde trabajar

## Imagen editorial final

Generar o usar una imagen bitmap local en `assets/` para la slide final.

Prompt base:

```text
Editorial corporate illustration for a technical executive presentation. A calm data analysis team working around a structured digital workbench, not a chatbot interface. The scene shows ordered work artifacts: a notebook or logbook, trusted tools, access keys or permission tokens, reviewed outputs, and a human making the final decision. The AI appears only as a subtle connective layer of light between the work artifacts, not as a robot or chat window. Warm neutral workspace, deep navy shadows, muted orange and green accents, premium business technology editorial style, clean composition, enough negative space for a closing quote overlay. No dashboards, no charts, no bullet lists, no vendor logos, no readable UI text, no futuristic cliches.
```

## Evidencia obligatoria de build

- ruta del pptx
- cantidad de slides
- renders individuales
- contact sheet
- chequeo textual con extraccion del pptx
- chequeos mecanicos
- estado de render nativo de PowerPoint si esta disponible
- riesgos residuales

## Decision de continuidad

- listo para build

