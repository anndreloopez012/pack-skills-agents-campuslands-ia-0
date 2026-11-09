---
name: journal-entries
description: "Convierte compras, ventas, cobros, pagos, planillas y gastos en partidas de diario cuadradas, con cuentas, debe, haber y glosa. Úsala cuando digas «hazme la partida de esta factura», «cómo registro este pago» o «pasa estas operaciones al libro diario»."
---

# Partidas contables

Pasa cada operación de la empresa a una partida de diario de doble partida, cuadrada y explicada,
para quien lleva la contabilidad de una empresa o de clientes en Guatemala.

## Cuándo usarla

- «Hazme la partida de esta factura de compra.»
- «¿Cómo registro el pago de la planilla y las cuotas del IGSS?»
- «Pasa al diario estas 20 operaciones del mes.»
- Al corregir una partida mal hecha o preparar una partida de ajuste o de cierre.

## Qué necesito de ti

- La operación: factura, recibo, estado de cuenta o tu descripción (fecha, monto, proveedor o cliente,
  forma de pago).
- Tu nomenclatura contable (catálogo de cuentas). Si no la tienes, uso nombres de cuenta comunes y te
  lo marco como «Supuesto:».
- El régimen de la empresa: IVA general o pequeño contribuyente; ISR sobre utilidades u opcional
  simplificado; si es agente de retención de IVA o ISR.
- Si el documento trae nombres, NIT o cuentas bancarias, te propongo pasarlo antes por `data-shield`.
- Si falta algo importante, hago como máximo 3 preguntas cortas y sigo con supuestos marcados.

## Cómo trabajo

1. Identifico el tipo de operación (compra, venta, cobro, pago, gasto, planilla, depreciación,
   provisión, ajuste, cierre) y el documento que la respalda.
2. Separo el monto: base, IVA (12 % en el régimen general; el monto con IVA se divide entre 1.12 para
   sacar la base), retenciones y otros cargos. Si es pequeño contribuyente, no separo crédito fiscal.
3. Elijo las cuentas de tu nomenclatura y decido qué va al debe y qué al haber.
4. Verifico que el total del debe sea igual al total del haber. Si no cuadra, no entrego la partida:
   te muestro dónde está la diferencia.
5. Escribo la glosa: qué pasó, con qué documento (serie y número de la FEL, cheque o transferencia) y
   a quién.
6. Si la operación tiene efecto fiscal (crédito fiscal, retención, gasto no deducible), lo anoto en
   «Observaciones» para que lo revises con `tax-returns-gt`.

## Lo que te entrego

```text
PARTIDA No. ___            Fecha: dd/mm/aaaa         Tipo: Diario | Ajuste | Cierre
Documento de soporte: FEL serie ___ No. ___ | Cheque No. ___ | Transferencia ref. ___
```

| Código | Cuenta | Debe (Q) | Haber (Q) |
|---|---|---:|---:|
| 1.1.5.01 | Inventario de mercadería | 10,000.00 | |
| 1.1.6.01 | IVA por cobrar (crédito fiscal) | 1,200.00 | |
| 2.1.1.01 | Proveedores | | 11,200.00 |
| | **Sumas iguales** | **11,200.00** | **11,200.00** |

```text
Glosa: Compra de mercadería a [PROVEEDOR], FEL serie A No. 1234, al crédito 30 días.
Observaciones: crédito fiscal válido si la FEL está a nombre de la empresa y vinculada a la
actividad. Supuestos: ____.
```

Para varias operaciones, entrego además un resumen:

| No. | Fecha | Operación | Debe total (Q) | Haber total (Q) | ¿Cuadra? |
|---|---|---|---:|---:|---|

## Reglas

- Siempre doble partida y sumas iguales; montos en quetzales con dos decimales.
- Nunca invento una cuenta, un número de factura ni un monto que no venga en tus datos: si falta,
  lo marco como pendiente.
- El IVA solo se separa si el documento es una FEL válida a nombre de la empresa; si no, va al costo
  o al gasto, y lo aviso.
- Gastos sin documento, multas o gastos personales los marco como posible gasto no deducible para
  que el contador decida.
- Tasas de referencia: IVA 12 %; cuota laboral IGSS 4.83 %; cuota patronal IGSS 10.67 %, IRTRA 1 %,
  INTECAP 1 %. Verifica que sigan vigentes en portal.sat.gob.gt e igssgt.org (revisado: noviembre de
  2026).
- La IA prepara la partida; el contador la revisa, la aprueba y la registra en su sistema.
- Para hojas con muchas operaciones, me apoyo en `spreadsheet-helper` para dejar fórmulas de cuadre.

## Ejemplo

**Pedido:** «Pagué la factura de luz de Q560.00 con IVA por transferencia. Régimen general.»
**Entrega (resumen):** partida con Debe Energía eléctrica Q500.00 e IVA por cobrar Q60.00, Haber
Bancos Q560.00; sumas iguales Q560.00; glosa con número de FEL y referencia de la transferencia, y la
nota de que el crédito fiscal requiere la FEL a nombre de la empresa.
