---
name: process-redesign
description: "Simplifica trámites y procesos de una institución: mide cómo están, quita pasos que no agregan valor y arma la ficha del proceso nuevo con sus indicadores. Úsala cuando digas «simplifica este trámite», «el proceso tarda demasiado» o «arma la ficha de proceso con indicadores»."
---

# Rediseño de procesos

Toma un trámite o proceso que hoy es lento, confuso o lleno de firmas y propone una versión más
simple, medible y fácil de explicar al ciudadano y al personal.

## Cuándo usarla

- «La solicitud de licencia de construcción tarda 45 días hábiles; ¿cómo la bajamos?».
- «Simplifica este trámite: piden los mismos papeles tres veces».
- «Arma la ficha del proceso de compras con sus indicadores».

## Qué necesito de ti

- Cómo se hace hoy, paso a paso (o la ficha que hizo `process-mapper`).
- Quién interviene en cada paso, cuánto tarda y qué documentos pide.
- Las quejas más frecuentes y el volumen (trámites al mes).
- La norma que regula el trámite, si la conoces.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Levanto el proceso actual (AS-IS): pasos, responsables, tiempo de trabajo y tiempo de espera,
   documentos pedidos.
2. Calculo el tiempo total de ciclo en días hábiles y cuánto de ese tiempo es espera.
3. Clasifico cada paso: agrega valor al usuario, necesario por norma, o desperdicio (esperas,
   copias, firmas repetidas, revisar dos veces lo mismo, traslados físicos).
4. Separo lo que manda la ley de lo que es costumbre. Lo que viene de una norma solo se cambia
   con una reforma; lo marco y no lo elimino.
5. Propongo el proceso nuevo (TO-BE) con técnicas concretas: eliminar, unir pasos, hacer en
   paralelo, ventanilla única, pedir el documento una sola vez, formularios en línea, firma
   delegada.
6. Armo la ficha de proceso y 3 a 5 indicadores (detalle con `indicators`).
7. Dibujo el antes y el después por carriles con `diagram-design`, si sirve.
8. Propongo un plan de implementación por fases y cómo comunicarlo a la población.

## Lo que te entrego

```
1. Proceso actual
| # | Paso | Responsable | Tiempo de trabajo | Tiempo de espera | Documento | Tipo (valor / norma / desperdicio) |
Tiempo de ciclo actual: __ días hábiles (espera: __ %)

2. Proceso propuesto
| # | Paso | Responsable | Tiempo estimado | Cambio aplicado |
Tiempo de ciclo propuesto: __ días hábiles

3. Ficha de proceso
Nombre · Objetivo · Dueño del proceso · Alcance (inicia / termina) · Usuarios · Entradas ·
Salidas · Base legal (por verificar) · Requisitos para el usuario · Riesgos · Registros

4. Indicadores
| Indicador | Fórmula | Meta | Frecuencia | Fuente |

5. Plan de implementación
| Fase | Acción | Responsable | Fecha | Requiere cambio de norma (sí/no) |
```

## Reglas

- Mido en días hábiles y lo digo; no mezclo días calendario.
- Nunca recomiendo saltarse un requisito legal ni un control de la Contraloría; si un paso parece
  inútil pero lo pide la norma, propongo cómo hacerlo más rápido, no quitarlo.
- La base legal que cite va con «verificar la norma vigente; revisado: noviembre de 2026». No
  invento artículos.
- Las estimaciones de tiempo del proceso nuevo son supuestos hasta medirlas en una prueba piloto.
- Si los ejemplos traen expedientes con datos de personas, propone primero `data-shield`.
- La IA propone; la autoridad decide y aprueba el cambio.

## Ejemplo

**Pedido:** «Trámite de constancia de residencia: 6 pasos, 8 días hábiles».
**Entrega (resumen):** 3 pasos son espera entre escritorios; se propone recepción y verificación
en la misma ventanilla, firma delegada al jefe de sección y entrega por correo; tiempo de ciclo
estimado de 2 días hábiles; indicadores: tiempo promedio de atención, porcentaje de constancias
entregadas en plazo y quejas por cada 100 trámites.
