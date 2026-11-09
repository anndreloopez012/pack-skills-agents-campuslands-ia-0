---
name: project-control
description: "Controla una obra o proyecto: avance físico y financiero, valor ganado (PV, EV, AC, CPI, SPI) explicado en llano y alertas de atraso o sobrecosto. Pídela así: «calcula el valor ganado de la obra», «la remodelación va atrasada, cuánto»."
---

# Control de obra

Mide si una obra va a tiempo y dentro del presupuesto con el método de valor ganado, y lo explica
sin jerga. Para gerentes de infraestructura, supervisores y administradores.

## Cuándo usarla

- «Tengo el cronograma y lo pagado de la remodelación del lobby, cómo vamos».
- «Calcula CPI y SPI de la obra a la semana 10».
- «Arma el informe de avance para la gerencia».

## Qué necesito de ti

- Renglones de trabajo (actividades) con su costo presupuestado en Q y el cronograma (semana o mes
  en que debía hacerse cada parte).
- Avance físico real de cada renglón en % (lo que mide el supervisor en obra).
- Costo real pagado o devengado a la fecha de corte.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Armo la línea base: cuánto se tenía que haber gastado en cada corte según el cronograma.
2. Calculo los tres valores, explicados así:
   - **PV (valor planificado):** el valor del trabajo que debía estar hecho a la fecha. «Lo que
     debíamos llevar».
   - **EV (valor ganado):** el valor del trabajo realmente hecho = % de avance físico x presupuesto
     del renglón. «Lo que de verdad llevamos, medido en quetzales del presupuesto».
   - **AC (costo real):** lo que realmente costó ese trabajo. «Lo que llevamos gastado».
3. Calculo los índices:
   - **CPI = EV / AC.** Mayor que 1: rinde el dinero; menor que 1: cada quetzal da menos obra de lo
     planeado (sobrecosto).
   - **SPI = EV / PV.** Mayor que 1: vamos adelantados; menor que 1: vamos atrasados.
   - Variación de costo CV = EV - AC y variación de plazo SV = EV - PV, en Q.
   - Estimado al terminar EAC = presupuesto total / CPI (si el ritmo de costos sigue igual).
4. Doy semáforo: verde si el índice es 0.95 o más, amarillo de 0.90 a 0.94, rojo menor que 0.90.
5. Identifico los renglones que más empujan el atraso o el sobrecosto y propongo acciones.

## Lo que te entrego

```
CONTROL DE OBRA - <Proyecto> - Corte: semana __ / __/__/____
Presupuesto total (BAC): Q ___   Plazo: __ semanas

| Renglón | Presupuesto Q | % planificado | % físico real | PV Q | EV Q | AC Q | CV Q | SV Q | CPI | SPI | Semáforo |

TOTAL DEL PROYECTO
| PV Q | EV Q | AC Q | CPI | SPI | EAC Q | Diferencia con presupuesto Q |

EN LLANO
- Avance físico: __ % (debía ser __ %).
- Por cada Q 1.00 gastado se obtuvo Q __ de obra.
- Si sigue así, la obra costará Q ___ y terminará aproximadamente __ semanas tarde.

ALERTAS Y ACCIONES
| Renglón | Problema | Causa probable | Acción propuesta | Responsable | Fecha |
```

## Reglas

- El avance físico lo mide el supervisor en obra; no lo deduzco de lo pagado.
- Si el AC incluye anticipos sin trabajo hecho, lo separo: un anticipo no es obra ejecutada.
- El atraso en semanas es una aproximación (plazo / SPI); lo aclaro siempre.
- Sin cronograma no hay PV: si no existe, ayudo a armar uno sencillo antes de calcular.
- Para la comparación anual por partida usa `budget-vs-actual`; para el informe a gerencia,
  `one-pager`; para las fórmulas en Excel, `spreadsheet-helper`.
- La IA calcula y propone; la persona decide órdenes de cambio o pagos. Sin emojis.

## Ejemplo

**Pedido:** «Remodelación de Q 400,000 en 12 semanas. Semana 6: debía ir al 50 %, va al 40 %, se han
pagado Q 190,000».
**Entrega (resumen):** PV Q 200,000; EV Q 160,000; AC Q 190,000; CPI 0.84 (rojo: por cada quetzal
sale Q 0.84 de obra); SPI 0.80 (rojo: unas 3 semanas de atraso aproximado); EAC Q 476,190; acciones
en acabados e instalaciones eléctricas.
