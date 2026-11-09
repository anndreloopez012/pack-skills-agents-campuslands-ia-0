---
name: bank-reconciliation
description: "Cruza el estado de cuenta del banco con el libro de bancos, encuentra las diferencias y arma la conciliación con partidas en tránsito y ajustes. Úsala cuando digas «concilia el banco de octubre», «no me cuadra el banco» o «qué cheques están en circulación»."
---

# Conciliación bancaria

Cruza movimiento por movimiento lo que dice el banco con lo que dicen tus libros, explica cada
diferencia y deja la conciliación lista para firmar.

## Cuándo usarla

- «Concilia la cuenta monetaria de octubre.»
- «El saldo del banco no me cuadra con el libro, ¿dónde está la diferencia?»
- «¿Qué cheques siguen en circulación?»
- Cierre de mes, antes de preparar `financial-statements`.

## Qué necesito de ti

- Estado de cuenta del banco del mes (movimientos con fecha, descripción, débito, crédito y saldo).
- Libro de bancos o auxiliar contable de la misma cuenta y el mismo periodo.
- La conciliación del mes anterior (para arrastrar partidas en tránsito pendientes).
- Te propongo pasar los documentos por `data-shield` antes: los números de cuenta completos no hacen
  falta, basta con los últimos 4 dígitos.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Confirmo saldo inicial y final de ambos lados y que sean del mismo periodo y la misma cuenta.
2. Cruzo por monto exacto, luego por número de cheque o referencia, luego por fecha cercana
   (hasta 5 días de diferencia) y descripción.
3. Clasifico lo que no cruzó:
   - En libros y no en banco: cheques en circulación, depósitos en tránsito.
   - En banco y no en libros: comisiones, intereses, notas de débito o crédito, transferencias no
     registradas, cheques rechazados.
   - Errores: montos invertidos (por ejemplo 1,520 y 1,250), registros duplicados, cuenta equivocada.
4. Armo la conciliación por el método de saldos ajustados: los dos saldos ajustados deben ser iguales.
5. Propongo las partidas de ajuste para lo que falta registrar en libros (las armo con
   `journal-entries` si me lo pides).
6. Señalo partidas antiguas: cheques en circulación de más de 90 días y depósitos en tránsito de más
   de 5 días hábiles, para que se investiguen.

## Lo que te entrego

```text
CONCILIACIÓN BANCARIA
Empresa: ________   Banco: ________   Cuenta: ****1234   Mes: ________
```

| Concepto | Detalle | Monto (Q) |
|---|---|---:|
| **Saldo según estado de cuenta al dd/mm/aaaa** | | 0.00 |
| (+) Depósitos en tránsito | fecha, referencia | 0.00 |
| (−) Cheques en circulación | No. cheque, fecha, beneficiario | 0.00 |
| (±) Errores del banco | descripción | 0.00 |
| **Saldo bancario ajustado** | | **0.00** |
| **Saldo según libros al dd/mm/aaaa** | | 0.00 |
| (+) Notas de crédito no registradas | intereses, transferencias recibidas | 0.00 |
| (−) Notas de débito no registradas | comisiones, cheques rechazados, cargos | 0.00 |
| (±) Errores en libros | descripción | 0.00 |
| **Saldo en libros ajustado** | | **0.00** |
| **Diferencia (debe ser 0.00)** | | **0.00** |

Detalle de partidas en tránsito:

| Tipo | Fecha | Referencia / No. cheque | Descripción | Monto (Q) | Días pendiente | Acción |
|---|---|---|---|---:|---:|---|

Ajustes propuestos en libros:

| Fecha | Cuenta debe | Cuenta haber | Monto (Q) | Glosa |
|---|---|---|---:|---|

```text
Preparó: ________  Revisó: ________  Fecha: ________
```

## Reglas

- Si la diferencia final no es cero, lo digo claro y muestro el monto sin explicar; nunca la tapo con
  un ajuste «varios».
- No invento movimientos: todo sale de los dos documentos que me diste.
- Los ajustes van en libros, nunca «se corrige el banco»; los errores del banco se reclaman al banco.
- Cheques en circulación muy antiguos: sugiero revisar si procede anularlos o reclasificarlos según la
  política de la empresa; el contador decide.
- La conciliación la firma quien la prepara y quien la revisa: es un control clave (ver
  `internal-control`).

## Ejemplo

**Pedido:** «Banco dice Q48,320.15 al 31/10; mi libro dice Q45,970.15. Te pego los dos.»
**Entrega (resumen):** dos cheques en circulación por Q3,500.00, un depósito en tránsito de Q1,250.00,
comisión bancaria no registrada de Q35.00 y un error de transposición de Q135.00; saldos ajustados
iguales y tres partidas de ajuste propuestas.
