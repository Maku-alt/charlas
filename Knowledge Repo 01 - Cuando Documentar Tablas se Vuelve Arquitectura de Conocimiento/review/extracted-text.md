# Extracted Text


## Slide 1

PUNTO DE QUIEBRE
01
Una tabla deja de estar documentada cuando nadie puede reconstruir su contexto
Pregunta conductora
¿Puedo usar clientes para entrenar este modelo y explicar el KPI del dashboard?
El volumen de tablas convierte la documentación en un problema de memoria común.
clientes.md
descripcion
columnas
usos
owner
freshness
PII
KPI
decisión
La ficha sola ya no contiene el razonamiento.


## Slide 2

FALSO AVANCE
02
Escribir más fichas no arregla una memoria que no tiene contrato
Markdown hace el conocimiento revisable; el contrato lo vuelve mantenible.
clientes.md
owner: crecimiento
freshness: mensual
relaciones: --
ventas.md
owner: --
freshness: diaria
decisiones: pricing-2025
churn.md
owner: analytics
freshness: --
relaciones: clientes
owner faltante
vigencia parcial
relaciones débiles
Markdown es buen formato base; sin contrato, solo produce inventario más prolijo.


## Slide 3

PREGUNTA REAL
03
La unidad de valor no es la ficha, es el camino que permite responder
Documentar datos es conservar rutas de razonamiento, no solo describir objetos.
tabla
clientes
columnas
críticas
joins
válidos
KPI
retención
dashboard
CX
owner
growth
dudas
resueltas
La respuesta útil incluye evidencia, contexto, vigencia y alguien responsable si hay duda.
La red de conocimiento vale más que la suma de fichas aisladas.


## Slide 4

CONTRATO MÍNIMO
04
Un knowledge repo empieza cuando cada tabla declara qué promete mantener
clientes.md
---
id: data.crm.clientes
owner: growth-analytics
dominio: crm
estado: vigente
freshness: mensual
relaciones:
  metricas: [retencion, churn]
  dashboards: [cx-retention]
decisiones: [segmentacion-2026]
revision: 2026-09-30
---
Identidad estable
id canónico que no depende del título
Responsabilidad
owner, estado y fecha de revisión
Relaciones
métricas, dominios, consumidores
Historial
decisiones y riesgos recuperables
Convención observable > herramienta
La arquitectura vive en convenciones observables.


## Slide 5

LOOP OPERATIVO
05
La memoria común escala cuando tiene ciclo de vida, no cuando tiene más enlaces
Wiki y backlinks ayudan a navegar; el repo también debe decidir qué sigue vigente.
capturar
conectar
validar
revisar
retirar
estado
draft
vigente
requiere revisión
deprecated
review
owner
freshness
riesgo
Memoria operacional significa mantenimiento, no solo navegación.


## Slide 6

SEÑAL EXTERNA
06
Los stacks de datos ya muestran que la metadata importante es operacional
El knowledge repo traduce esa necesidad a una escala portable y complementaria.
tabla: clientes
asset central
no texto aislado
owner
lineage
freshness
tests
glossary
consumidores
contrato
No reemplaza un catálogo: captura conocimiento narrativo y decisiones que suelen quedar fuera.
La metadata útil describe responsabilidad, vigencia y relaciones.


## Slide 7

AGENTES
07
Un agente no necesita más documentos; necesita una memoria consultable con precisión
MCP/API es una puerta de acceso; la confiabilidad viene del contrato del repo.
pregunta
¿puedo usar clientes?
Ventanilla
MCP/API
search
read
neighbors
knowledge repo
fichas
versionado
owners
evidencia
contexto
citable
ensamblable
actualizable
El agente ensambla contexto; no inventa ownership, vigencia ni relaciones.
Preparar memoria reduce improvisación y contexto irrelevante.


## Slide 8

DECISIÓN DE ARQUITECTURA
08
Separar responsabilidades evita convertir una herramienta en estrategia
La decisión correcta es asignar roles; no declarar un ganador universal.
fuente
uso
control
paquete
consulta
formato
Markdown
exploración
Wiki
gobierno
Knowledge repo
portabilidad
OKF-style bundle
acceso
MCP/API
OKF se presenta como patrón emergente para bundles portables, no como estándar corporativo maduro.
Separar capas evita comprar herramienta o sobrediseñar antes de tiempo.


## Slide 9

"The overriding design goal for Markdown's formatting syntax is to make it as readable as possible."
John Gruber, Markdown


## Checks

- slides: 9
- replacement_chars: 0
