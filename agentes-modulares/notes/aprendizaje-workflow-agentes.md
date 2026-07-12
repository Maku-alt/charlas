# Aprendizaje: un padre liviano para crear charlas con agentes

## Antes

Las reglas y el conocimiento de cada fase se repetian entre instrucciones. El padre corria el riesgo de absorber contexto de ejecucion que luego competia con la conversacion necesaria para definir una buena charla.

## Cambio central

El padre conversa con el usuario, converge la idea y enruta el trabajo mediante el `workflow-contract.json` canonico. Ese contrato ordena fases y transiciones, pero no se convierte en el producto.

Cada worker especializado recibe solo su rol, spec, prompt e inputs minimos, trabaja con `fork_context: false` y publica un handoff compacto en `notes/phase-summary.md`. El padre lee unicamente ese resumen actual cuando ya fue validado.

## Flujo

1. Idea y convergencia con el usuario.
2. Research para tensionar la tesis y validar claims.
3. Narrativa para fijar el arco de la charla.
4. Build del PPTX editable.
5. Image-close para resolver el cierre editorial.
6. Review independiente del candidato exacto.
7. Si hace falta, build-fix y review-final.
8. Release del artefacto aprobado.

Research, narrativa, build, image-close y review pertenecen a workers acotados. El padre decide la transicion sin incorporar sus chats ni rehacer su ejecucion.

## Controles minimos

- Identidad de corrida para no mezclar ejecuciones.
- Sentinel escrito al final, despues del resumen validado.
- Un solo summary compacto que representa el estado actual.
- Review con identidad independiente de quien construyo el deck.
- SHA256 del PPTX candidato para revisar y promover el mismo archivo.
- Apertura y export en PowerPoint nativo como gate final.
- Bibliografia cuando hubo research externo.

## Advisor

El advisor es excepcional y consultivo. Se convoca solo ante una decision que cruza fases o un tradeoff dificil; no ejecuta una fase ni sustituye al worker responsable.

## Por que importa

El contexto del padre permanece util para colaborar y converger con el usuario. A la vez, cada especialista conserva un limite claro y el entregable sigue siendo el PPTX editable, no la infraestructura del workflow.

## Como usarlo en la siguiente charla

Converge primero la tesis con el usuario. Luego lanza una fase por vez con el paquete minimo, valida su publicacion y decide la siguiente transicion leyendo `notes/phase-summary.md`. Solo libera el PPTX que haya pasado review independiente y el gate nativo.
