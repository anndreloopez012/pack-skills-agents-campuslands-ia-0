---
name: financial-statements
description: "Arma el balance general, el estado de resultados y el flujo de efectivo con sus notas a partir de tu balanza de saldos. Úsala cuando digas «hazme los estados financieros de diciembre», «arma el balance con esta balanza» o «necesito el flujo de efectivo»."
---

# Estados financieros

Convierte una balanza de comprobación en estados financieros ordenados, cuadrados y con notas, para
el contador que cierra el mes o el año.

## Cuándo usarla

- «Con esta balanza arma el balance general y el estado de resultados.»
- «Necesito el flujo de efectivo del año por el método indirecto.»
- «Prepara las notas para el banco que nos pide estados financieros.»

## Qué necesito de ti

- Balanza de comprobación del periodo (cuenta, saldo deudor, saldo acreedor) y, si existe, la del
  periodo anterior para comparar y armar el flujo.
- Nombre de la empresa, fecha de cierre, régimen de ISR y marco contable que usan (NIIF para las
  PYMES, NIIF completas u otro que defina la empresa).
- Ajustes pendientes ya conocidos (depreciaciones, provisiones, ISR del periodo).
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Reviso que la balanza cuadre (total deudor igual a total acreedor). Si no cuadra, me detengo y te
   muestro la diferencia.
2. Clasifico cada cuenta: activo corriente y no corriente, pasivo corriente y no corriente,
   patrimonio, ingresos, costos y gastos.
3. Armo el estado de resultados hasta la utilidad neta; si me das la tasa de ISR del régimen, calculo
   el impuesto estimado y lo marco para revisión con `tax-returns-gt`.
4. Armo el balance general y verifico: Activo = Pasivo + Patrimonio, con la utilidad del periodo
   incluida en patrimonio.
5. Armo el flujo de efectivo por el método indirecto (operación, inversión, financiamiento) con las
   variaciones contra el periodo anterior, y verifico que cierre con el saldo de caja y bancos.
6. Redacto notas básicas: entidad, bases de preparación, políticas principales, y detalle de las
   cuentas importantes (efectivo, cuentas por cobrar, inventarios, propiedad planta y equipo,
   préstamos, patrimonio).

## Lo que te entrego

```text
[EMPRESA, S.A.]
ESTADO DE RESULTADOS del 01/01/aaaa al 31/12/aaaa (cifras en quetzales)
```

| Concepto | Año actual (Q) | Año anterior (Q) |
|---|---:|---:|
| Ventas netas | | |
| (−) Costo de ventas | | |
| **Utilidad bruta** | | |
| (−) Gastos de venta | | |
| (−) Gastos de administración | | |
| **Utilidad en operación** | | |
| (±) Otros ingresos y gastos, gastos financieros | | |
| **Utilidad antes de ISR** | | |
| (−) ISR del periodo | | |
| **Utilidad neta** | | |

```text
BALANCE GENERAL al 31/12/aaaa
```

| Activo | Q | Pasivo y patrimonio | Q |
|---|---:|---|---:|
| Efectivo y equivalentes | | Proveedores | |
| Cuentas por cobrar, neto | | Impuestos por pagar (IVA, ISR, IGSS) | |
| Inventarios | | Préstamos a corto plazo | |
| **Total activo corriente** | | **Total pasivo corriente** | |
| Propiedad, planta y equipo, neto | | Préstamos a largo plazo | |
| | | Provisión de indemnizaciones | |
| | | Capital pagado, reserva legal, utilidades | |
| **Total activo** | | **Total pasivo y patrimonio** | |

```text
FLUJO DE EFECTIVO (método indirecto): utilidad neta + depreciaciones ± variación de capital de
trabajo = efectivo de operación; ± inversión; ± financiamiento; = variación de efectivo;
+ saldo inicial = saldo final (debe igualar caja y bancos del balance).

NOTAS: 1. Entidad  2. Bases de preparación  3. Políticas contables  4 en adelante: detalle de
cuentas.
Control de cuadre: Balanza OK | Activo = Pasivo + Patrimonio OK | Flujo = Caja y bancos OK
```

## Reglas

- No presento estados que no cuadren; te muestro qué falla.
- No invento saldos del año anterior ni notas con datos que no tengo: dejo «[dato pendiente]».
- La reserva legal y otras obligaciones mercantiles las menciono como punto a confirmar con el Código
  de Comercio vigente; no calculo porcentajes que no me confirmes.
- Tasas de ISR de referencia: 25 % sobre utilidades; régimen opcional simplificado 5 % hasta
  Q30,000 mensuales y 7 % sobre el excedente. Verifica vigencia en portal.sat.gob.gt (revisado:
  noviembre de 2026).
- Los estados los firma el contador registrado y el representante legal; la IA solo prepara.
- Para analizar los resultados, sigue con `financial-ratios`; para un resumen a gerencia, `one-pager`.

## Ejemplo

**Pedido:** «Aquí está la balanza al 31/12 y la del año pasado. Empresa en régimen sobre utilidades.»
**Entrega (resumen):** estado de resultados comparativo con ISR estimado al 25 % marcado para
revisión, balance cuadrado, flujo de efectivo indirecto que cierra con caja y bancos, seis notas
básicas y dos saldos marcados como pendientes de soporte.
