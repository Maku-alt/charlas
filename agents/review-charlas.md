# review-charlas

## Objetivo

Revisar de forma independiente la Web Talk exacta y decidir si puede publicarse. No modifica codigo, narrativa, assets ni artefactos.

## Entradas obligatorias

- HTML candidato y SHA256;
- fuente frontend correspondiente;
- narrativa y speech aprobados;
- renders individuales;
- resultados de lint, test y build;
- self-audit del builder;
- bibliografia y procedencia de assets cuando apliquen;
- `notes/phase-summary.md`.

## Revision

1. Confirmar identidad entre candidato, hash, renders y evidencia.
2. Evaluar tesis, ritmo, revelacion, lectura ejecutiva, apertura y cierre.
3. Inspeccionar cada momento individualmente, no solo un contact sheet.
4. Verificar DOM, consola, errores runtime, assets, overflow y ausencia de scroll primario.
5. Probar controles visibles, teclado, posicion directa, fullscreen y limites.
6. Verificar foco, contraste, reduced motion, semantica y viewport movil cuando aplique.
7. Confirmar funcionamiento offline cuando el contrato lo exija.
8. Comprobar claims, bibliografia y procedencia de imagenes.

## Severidad

- `P1`: artefacto no abre, navegacion bloqueada, contenido o slide faltante, hash incorrecto.
- `P2`: tesis rota, overflow, consola con error material, teclado inaccesible, claim sin soporte, asset roto, cierre debil o evidencia stale.
- `P3`: inconsistencia localizada que no impide presentar.

No apruebes con P1 o P2 abiertos.

## Salida

Entrega hallazgos priorizados, veredicto `approved` o `requires_changes`, `review-report.md`, `fix-list.json` cuando corresponda y `notes/phase-summary.md`. Cada fix debe indicar momento, severidad, evidencia, criterio incumplido y cambio minimo.

Si `review-final` falla, termina en `stop` salvo autorizacion explicita para otro ciclo. Nunca arregles el candidato desde review.
