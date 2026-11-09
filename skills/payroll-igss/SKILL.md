---
name: payroll-igss
description: "Calcula la planilla de sueldos con cuotas del IGSS, IRTRA e INTECAP, bonificación incentivo, bono 14, aguinaldo, vacaciones e indemnización, mostrando cada cálculo. Úsala cuando digas «arma la planilla de noviembre», «calcula el bono 14» o «cuánto le toca de liquidación a quien renunció»."
---

# Planilla e IGSS

Arma la planilla del mes y calcula prestaciones laborales de Guatemala con el detalle paso a paso,
para quien paga sueldos en una empresa o lleva la planilla de clientes.

## Cuándo usarla

- «Arma la planilla de noviembre de estos 12 empleados.»
- «Calcula el bono 14 de julio» o «el aguinaldo de diciembre».
- «Cuánto le toca de liquidación a un empleado despedido sin causa justificada.»
- «Cuánto pago de cuotas patronales al IGSS este mes.»

## Qué necesito de ti

- Por empleado: código o iniciales, puesto, fecha de ingreso, salario ordinario mensual, horas
  extra, comisiones, días laborados y descuentos (anticipos, préstamos, embargos judiciales).
- Para liquidación: fecha de salida, motivo (renuncia, despido con o sin causa justificada) y
  salarios de los últimos 6 meses.
- Si hay ISR retenido en relación de dependencia, el monto que ya proyectó el contador.
- Recomiendo pasar la lista por `data-shield`: no necesito nombres completos, DPI ni cuentas
  bancarias, basta con un código por empleado.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Calculo el salario devengado: salario ordinario + horas extra + comisiones (todo esto es base
   para IGSS).
2. Sumo la bonificación incentivo de Q250, que no es base para cuotas del IGSS ni para prestaciones.
3. Calculo descuentos: cuota laboral IGSS 4.83 % sobre el devengado, ISR retenido si aplica, y otros
   descuentos autorizados.
4. Calculo el costo patronal: IGSS 10.67 %, IRTRA 1 % e INTECAP 1 % sobre el devengado (12.67 % en
   total).
5. Prestaciones: bono 14 (un salario, periodo del 1 de julio al 30 de junio) y aguinaldo (un salario,
   periodo del 1 de diciembre al 30 de noviembre), proporcionales al tiempo trabajado; vacaciones
   (15 días hábiles por año); indemnización (un salario por año de servicio, proporcional por
   fracción), con el salario promedio de los últimos 6 meses más la proporción de bono 14 y aguinaldo
   que indique la ley.
6. Verifico que la planilla cuadre: devengado − descuentos = líquido; y que el total de cuotas
   coincida con lo que se reportará al IGSS.

## Lo que te entrego

| Cód. | Puesto | Días | Salario ordinario | Horas extra | Comisiones | **Devengado** | Bonif. incentivo | IGSS laboral 4.83 % | ISR | Otros desc. | **Líquido a pagar** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| E01 | | 30 | | | | | 250.00 | | | | |
| | **Totales** | | | | | | | | | | |

| Costo patronal | Base (Q) | Tasa | Monto (Q) |
|---|---:|---:|---:|
| IGSS patronal | | 10.67 % | |
| IRTRA | | 1 % | |
| INTECAP | | 1 % | |
| **Total a reportar al IGSS (laboral + patronal)** | | | |

```text
LIQUIDACIÓN (si aplica)   Empleado: E__   Ingreso: dd/mm/aaaa   Salida: dd/mm/aaaa   Motivo: ____
Salario promedio últimos 6 meses: Q____
Indemnización: Q____ (Q____ × años y fracción ____)  | solo si el despido es sin causa justificada
Aguinaldo proporcional: Q____ (días ____ / 365)
Bono 14 proporcional:   Q____ (días ____ / 365)
Vacaciones no gozadas:  Q____ (días ____)
Salarios pendientes:    Q____
TOTAL A PAGAR:          Q____
Supuestos y puntos a confirmar con el Código de Trabajo: ____
```

## Reglas

- Cifras de referencia, revisado: noviembre de 2026; verifica vigencia en igssgt.org, en el Código de
  Trabajo, en el Decreto 76-78 (aguinaldo), en el Decreto 42-92 (bono 14) y en el Ministerio de
  Trabajo: IGSS laboral 4.83 %, IGSS patronal 10.67 %, IRTRA 1 %, INTECAP 1 %, bonificación
  incentivo Q250, bono 14 y aguinaldo de un salario, indemnización de un salario por año.
- Fechas de pago de referencia: bono 14 en la primera quincena de julio; aguinaldo en la primera
  quincena de diciembre (la ley permite pagar la mitad en diciembre y la mitad en enero). Confírmalo
  en la fuente oficial.
- Reviso que ningún salario quede por debajo del salario mínimo vigente para la actividad; no lo
  invento: pido la cifra del acuerdo gubernativo del año o lo marco para confirmar.
- La planilla al IGSS se presenta y paga en el plazo que fije el IGSS (confírmalo en igssgt.org).
- Casos dudosos (despido con causa, ausencias, suspensiones IGSS, pactos colectivos) los marco para
  revisión de un abogado laboralista o del contador.
- La IA calcula; la persona revisa, aprueba y paga.

## Ejemplo

**Pedido:** «Empleado E03, salario Q4,500, 4 horas extra por Q160, mes completo.»
**Entrega (resumen):** devengado Q4,660.00; bonificación Q250.00; IGSS laboral Q225.08; líquido
Q4,684.92; costo patronal IGSS Q497.22, IRTRA Q46.60, INTECAP Q46.60; total al IGSS Q815.50.
