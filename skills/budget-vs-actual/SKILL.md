---
name: budget-vs-actual
description: "Compara el presupuesto con lo ejecutado por renglón o partida, calcula diferencias en Q y en porcentaje, y explica por qué se movió cada una. Pídela así: «compara presupuesto contra gastado», «explícame la variación del mes»."
---

# Presupuesto vs ejecutado

Pone lado a lado lo planificado y lo gastado, separa las diferencias que importan y las explica en
palabras que entiende la junta directiva o la gerencia. Para administradores y gerentes de obra.

## Cuándo usarla

- «Aquí está mi presupuesto anual del edificio y lo gastado a octubre, compáralos».
- «Por qué energía eléctrica se pasó 18 % este trimestre».
- «Prepara el informe de ejecución para la asamblea de propietarios».

## Qué necesito de ti

- Presupuesto por partida o renglón (mantenimiento, energía, agua, seguridad, limpieza, seguros,
  administración, reserva) y por mes si lo tienes.
- Gasto real del mismo periodo, con el mismo nombre de partida.
- Notas de lo que pasó (reparación imprevista, alza de tarifa, contrato nuevo).
- Si hay planillas con nombres o salarios, propone primero `data-shield`.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Empato partidas del presupuesto con las del gasto; lo que no empata lo listo aparte.
2. Calculo por partida: diferencia = ejecutado - presupuesto; % de ejecución = ejecutado /
   presupuesto x 100; y la ejecución esperada al corte (presupuesto acumulado a la fecha).
3. Clasifico: dentro de rango (diferencia de 5 % o menos), atención (más de 5 % y hasta 10 %),
   alerta (más de 10 %). Los umbrales los ajustas tú.
4. Explico cada alerta con una causa: precio (subió la tarifa), cantidad (se usó más), evento
   (reparación no prevista), calendario (se pagó antes o después de lo planeado) o error de registro.
5. Proyecto el cierre del año si sigue el ritmo actual y propongo ajustes.

## Lo que te entrego

```
PRESUPUESTO VS EJECUTADO - <Edificio / proyecto> - Corte: <mes año>
| Partida | Presupuesto anual Q | Presupuesto al corte Q | Ejecutado al corte Q | Diferencia Q | % ejecución al corte | Semáforo | Causa | Acción |

RESUMEN
- Total presupuesto al corte: Q ___  Ejecutado: Q ___  Diferencia: Q ___ (___ %)
- Partidas en alerta: ___   Partidas sin gasto (posible atraso o subregistro): ___

PROYECCIÓN AL CIERRE
| Partida | Ritmo mensual actual Q | Proyección al 31 dic Q | Presupuesto anual Q | Faltante o sobrante Q |

EXPLICACIÓN PARA LA GERENCIA (máximo 5 líneas)
```

## Reglas

- No escondo diferencias: si el dato no cuadra, lo digo y pido el respaldo.
- Una partida sin gasto no es ahorro hasta confirmar que no hay facturas pendientes.
- Separo gasto recurrente (energía, limpieza) de extraordinario (reparación de bomba) para no
  distorsionar la proyección.
- En instituciones públicas, las partidas son renglones del Manual de Clasificaciones
  Presupuestarias del MINFIN; para ubicarlos usa `budget-classifier`.
- Para fórmulas y gráficos en Excel, apóyate en `spreadsheet-helper`; para el resumen a la junta,
  en `one-pager`.
- Montos en quetzales (Q). Sin emojis.

## Ejemplo

**Pedido:** «Presupuesto 2026 del edificio y gasto a septiembre».
**Entrega (resumen):** 11 partidas; energía en alerta (+16 %, causa precio: ajuste de tarifa y aire
encendido fuera de horario), mantenimiento en atención (+8 %, cambio de motor de bomba no previsto),
seguros sin gasto (pago anual en diciembre); proyección de cierre con faltante de Q 38,500 y dos
ajustes propuestos.
