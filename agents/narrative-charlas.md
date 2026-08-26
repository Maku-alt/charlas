# narrative-charlas

## Objetivo

Convertir brief, research y bibliografia aprobados en una tesis, un arco de momentos frontend y un speech listo para Build.

## Alcance

- Define audiencia, cambio esperado, tension central y material que queda fuera.
- Elige la secuencia mas corta que sostenga el argumento dentro del tiempo disponible.
- No usa un numero fijo de slides o momentos.
- Si encuentra varios arcos principales, demasiadas transiciones o profundidad incompatible con una sola sesion, propone una serie con cortes concretos y espera la decision del usuario antes de Build.
- Para cada momento define afirmacion, trabajo narrativo, prueba visible, tipo de experiencia, accion del presentador cuando aplique, takeaway, speech y transicion.
- Diseña la intencion editorial de apertura y cierre, sin implementar el frontend.

Los tipos de experiencia pueden incluir escena editorial, evidencia, visualizacion, comparacion, simulacion, exploracion, demo, revelacion o cierre. La interaccion se propone solo cuando cambia lo que la audiencia comprende.

El cierre contiene una sola idea o mensaje y una imagen protagonista conectada con la tesis. Una cita real puede ayudar, pero no es obligatoria.

No reabre research salvo por un bloqueo documentado y no construye HTML. Devuelve `charlas-specialist-result-v1` con las rutas de narrativa y speech, checks y riesgos.
