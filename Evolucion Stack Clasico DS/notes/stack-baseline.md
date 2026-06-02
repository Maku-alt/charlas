# Baseline del stack actual

## Version base

- Python `3.10`

## Librerias reportadas por el usuario

- `pandas==2.2.0`
- `scikit-learn==1.4.2`
- `scipy==1.10.1`
- `optbinning==0.18.0`
- `feature-engine==1.8.3`
- `xgboost==2.0.3`
- `lightgbm==3.3.5`

## Tesis preliminar de la charla

La evolucion del stack clasico de Data Science no pasa solamente por cambiar de libreria. Pasa por entender que mejoras reales ya existen dentro de las herramientas que el equipo usa hoy, cuales pueden adoptarse manteniendo `Python 3.10`, y en que puntos una migracion a `Python 3.11+` empieza a desbloquear capacidades relevantes.

## Hipotesis de trabajo

1. Una parte importante del upgrade posible puede hacerse sin salir de `Python 3.10`.
2. Los cortes mas importantes parecen estar en `pandas 3.x` y `scikit-learn 1.8+`.
3. La charla debe separar claramente:
   - upgrades continuistas dentro de `Python 3.10`
   - mejoras interesantes pero condicionadas a `Python 3.11+`
   - novedades que suenan bien pero no cambian demasiado el trabajo diario

## Primeras observaciones verificadas

### Compatible con Python 3.10

- `pandas 2.3.x` sigue soportando `Python 3.10`.
- `scikit-learn 1.7.x` soporta `Python 3.10`.
- `SciPy 1.15.x` requiere `Python 3.10-3.13`.
- `feature-engine 1.9.4` requiere `Python >=3.9.0`.
- `optbinning 0.21.0` requiere `Python >=3.7`.
- `xgboost 3.2.0` requiere `Python >=3.10`.
- `lightgbm 4.6.0` requiere `Python >=3.7`.
- `scikit-llm 1.4.3` requiere `Python >=3.9`.

### Ya empuja a Python 3.11+

- `pandas 3.0.0` soporta `Python 3.11` o superior.
- `scikit-learn 1.8.0` soporta `Python 3.11-3.14`.

## Posible framing para slides

### Bloque 1: donde estamos

- stack actual
- por que equipos de DS suelen quedarse en versiones estables por bastante tiempo
- costo oculto de no revisar el stack

### Bloque 2: cuanto puede avanzar Python 3.10

- upgrades de bajo riesgo
- mejoras utiles por libreria
- cambios que valen la pena evaluar ya

### Bloque 3: que desbloquea Python 3.11

- compatibilidad con nuevas ramas mayores
- simplificacion de mantenimiento a mediano plazo
- posible argumento de migracion

### Bloque 4: conclusion

- roadmap recomendado: quick wins, upgrades seguros, decisiones de migracion

## Fuentes iniciales a revisar

- pandas release notes e installation docs
- scikit-learn release notes y GitHub releases
- SciPy release notes y toolchain roadmap
- PyPI de feature-engine, optbinning, xgboost, lightgbm y scikit-llm
