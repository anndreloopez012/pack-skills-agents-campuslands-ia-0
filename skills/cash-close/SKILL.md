---
name: cash-close
description: "Cuadra las ventas, cobros, pagos y movimientos del banco de un día, semana o mes, y te dice si la caja cuadra, cuánto ganaste y qué falta cobrar o pagar. Úsala con «cuadra mi caja», «no me cuadra el banco», «cuánto vendí esta semana»."
---

# Ventas, pagos y caja

Pone en orden lo que vendiste, lo que cobraste, lo que pagaste y lo que dice el banco, y encuentra
las diferencias. Para negocios pequeños que manejan efectivo, transferencias y tarjeta.

## Cuándo usarla

- «Cierro la caja del día y me faltan Q 150.»
- «Quiero saber cuánto vendí y cuánto gané esta semana.»
- «El estado de cuenta no coincide con mis ventas.»

## Qué necesito de ti

- Ventas del periodo: cuaderno, facturas FEL emitidas, reporte del POS o lista de pedidos.
- Cobros recibidos por forma de pago: efectivo, transferencia, tarjeta, depósito.
- Pagos hechos: proveedores, sueldos, servicios, retiros personales.
- Saldo inicial de caja y del banco, y el estado de cuenta del periodo.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Si los documentos traen nombres de clientes, NIT o números de cuenta completos, propongo
   `data-shield` y trabajo con los últimos 4 dígitos.
2. Separo caja (efectivo) y banco: cada uno cuadra por su lado.
3. Caja: saldo inicial + cobros en efectivo − pagos en efectivo − depósitos al banco = saldo
   esperado. Lo comparo con el efectivo contado.
4. Banco: saldo inicial + depósitos y transferencias recibidas + abonos de tarjeta − pagos y
   comisiones = saldo esperado. Lo comparo con el estado de cuenta.
5. Cruzo ventas contra cobros: lo vendido y no cobrado queda como cuentas por cobrar.
6. Cruzo compras contra pagos: lo comprado y no pagado queda como cuentas por pagar.
7. Listo cada diferencia con su posible causa: comisión de tarjeta, depósito en tránsito, venta
   no registrada, retiro personal sin anotar.
8. Calculo un resultado simple del periodo: ventas − costos y gastos pagados.

## Lo que te entrego

```
CIERRE DE CAJA Y BANCO — [periodo]

Caja (efectivo)
| Concepto | Q |
|---|---|
| Saldo inicial | |
| + Cobros en efectivo | |
| − Pagos en efectivo | |
| − Depositado al banco | |
| = Saldo esperado | |
| Efectivo contado | |
| Diferencia | |

Banco
| Concepto | Q |
|---|---|
| Saldo inicial / + Entradas / − Salidas / − Comisiones | |
| Saldo esperado vs. estado de cuenta | |

Ventas por forma de pago: efectivo Q __ | transferencia Q __ | tarjeta Q __ | crédito Q __
Por cobrar: | Cliente (etiqueta) | Monto | Desde | 
Por pagar: | Proveedor | Monto | Vence |
Diferencias y posible causa: ...
Resultado simple del periodo: Q __
```

## Reglas

- Las diferencias no se «ajustan» para que cuadre: se explican o se dejan pendientes.
- Retiros personales se anotan aparte; no son gasto del negocio.
- Esto es un control de gestión, no contabilidad formal ni declaración de impuestos. Para IVA o
  ISR consulta a tu contador y verifica en portal.sat.gob.gt.
- Nunca pido contraseñas de banca en línea ni datos completos de tarjetas.
- No hago pagos ni transferencias: solo te digo qué falta.
- Para el resumen mensual completo, usa el agente `monthly-close`.

## Ejemplo

**Pedido:** «Tienda de ropa en Xela. Vendí Q 18,400 en la semana: Q 9,000 efectivo, Q 6,200
tarjeta, Q 3,200 transferencia. El banco solo muestra Q 8,950 de tarjeta y transferencias.»
**Entrega (resumen):** Faltan Q 450 en banco. Posibles causas: comisión de tarjeta (con 5 %
serían Q 310, a confirmar con tu contrato del POS) y un abono de tarjeta del sábado aún en
tránsito. Caja cuadra con Q 20 de diferencia. Por cobrar: dos clientas con crédito por Q 600.
