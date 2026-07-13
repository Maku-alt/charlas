# Aprendizaje: un padre liviano para crear charlas con agentes

## Antes

`develop` ya tenia bien disenados el aislamiento, los roles especializados y el handoff por archivos: `fork_context: false`, workers acotados, roles, specs, prompts, sentinels y un unico `notes/phase-summary.md`. El problema no era conceptual, sino operativo: las mismas reglas aparecian en varios Markdown, dependian de una interpretacion consistente y no siempre se podian validar automaticamente.

## Cambio central

El padre conversa con el usuario, converge la idea y enruta el trabajo mediante el `workflow-contract.json` canonico. Ese contrato ordena fases y transiciones, pero no se convierte en el producto.

Cada worker especializado recibe solo su rol, spec, prompt e inputs minimos, trabaja con `fork_context: false` y publica un handoff compacto en `notes/phase-summary.md`. El padre lee unicamente ese resumen actual cuando ya fue validado.

## Comparacion con develop

| En `develop` | Ahora | Mejora concreta |
|---|---|---|
| Buenas practicas descritas en varios Markdown. | Reglas estructurales centralizadas en `workflow-contract.json`. | Una fuente canonica reduce repeticion y contradicciones. |
| El padre ya evitaba chats, logs y razonamiento de los workers. | Conserva ese aislamiento y consulta un contrato mas compacto. | No se reinventa el aislamiento; se formaliza y reduce la politica repetida en el padre. |
| Roles, specs, prompts y `fork_context: false` ya acotaban cada worker. | Un paquete de ejecucion explicita identidad, inputs, outputs y restricciones. | Es mas facil comprobar que cada worker fue lanzado con el contexto correcto. |
| El sentinel indicaba que una fase habia terminado. | Identifica contrato, corrida, fase, intento y estado. | Evita aceptar un sentinel viejo o perteneciente a otra ejecucion. |
| `phase-summary.md` ya representaba el estado operativo actual. | Mantiene esa funcion con un formato canonico y validado. | El padre puede decidir la transicion sin convertir el summary en un log historico. |
| La independencia de review se expresaba como instruccion. | Se verifica con identidades distintas de worker y sesion. | El builder no puede certificar su propio trabajo por omision o reutilizacion de identidad. |
| Las transiciones vivian principalmente en el orquestador. | El contrato JSON define y el codigo valida las transiciones permitidas. | Una fase no puede avanzar por una ruta contradictoria. |
| La review evaluaba el PPTX, pero no toda la cadena protegia la identidad exacta del archivo. | SHA256 enlaza build, review y release. | El PPTX liberado es exactamente el artefacto revisado y aprobado. |
| La documentacion repetia algunas reglas y excepciones. | Los documentos explican responsabilidades y el contrato gobierna la estructura. | Menor carga de mantenimiento y menos drift entre instrucciones. |

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
