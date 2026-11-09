---
name: product-costing
description: "Calcula cuánto te cuesta producir un producto (materia prima, mano de obra y gastos indirectos), su precio de venta en quetzales con y sin IVA, el margen real y el punto de equilibrio. Úsala con «cuánto me cuesta hacer esto», «a cuánto lo vendo», «cuántas tengo que vender para no perder»."
---

# Costeo y precio

Te dice cuánto cuesta de verdad cada unidad que produces y a qué precio venderla para ganar, en
quetzales. Para emprendedoras y negocios pequeños que fijan precios «a ojo».

## Cuándo usarla

- «Hago pasteles y no sé si estoy ganando.»
- «¿A cuánto vendo mis velas aromáticas para ganar 35 %?»
- «¿Cuántas unidades al mes tengo que vender para cubrir gastos?»

## Qué necesito de ti

- La receta o lista de materiales por lote: cantidad, unidad y precio de compra.
- Cuántas unidades salen por lote y cuántas horas de trabajo lleva.
- Cuánto se paga la hora de trabajo (incluida la tuya, aunque hoy no te pagues).
- Gastos fijos del mes: alquiler, luz, gas, internet, empaque, transporte, plataformas.
- Cuántas unidades vendes o esperas vender al mes, y si cobras con factura (régimen de IVA).
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Materia prima por unidad: costo de cada insumo según lo que realmente usas, más merma
   (lo que se pierde; si no la sabes, uso 5 % como supuesto).
2. Mano de obra por unidad: horas por lote × costo por hora ÷ unidades del lote.
3. Gastos indirectos por unidad: gastos fijos del mes ÷ unidades del mes.
4. Costo total por unidad = materia prima + mano de obra + indirectos.
5. Precio sin IVA según el margen deseado: precio = costo ÷ (1 − margen). Explico la diferencia
   con markup: precio = costo × (1 + markup). Un markup de 50 % da solo 33 % de margen.
6. Precio con IVA: precio sin IVA × 1.12 (IVA general de 12 %; verificar vigencia en
   portal.sat.gob.gt, revisado el 9 de noviembre de 2026). Si eres pequeño contribuyente, el
   cálculo es distinto: lo señalo y pido confirmar tu régimen en la SAT.
7. Punto de equilibrio: gastos fijos del mes ÷ (precio sin IVA − costo variable por unidad).
8. Comparo con 2 o 3 precios de la competencia si me los das, y doy una conclusión.

## Lo que te entrego

```
COSTEO: [producto] — lote de __ unidades — [fecha]

Materia prima
| Insumo | Cantidad usada | Unidad | Precio de compra (Q) | Costo en el lote (Q) |
|---|---|---|---|---|
Merma __ %: Q __     Materia prima por unidad: Q __

| Concepto | Por unidad (Q) |
|---|---|
| Materia prima | |
| Mano de obra (__ h × Q __ ÷ __ u) | |
| Gastos indirectos (Q __ ÷ __ u) | |
| COSTO TOTAL | |

| Margen deseado | Precio sin IVA (Q) | Precio con IVA 12 % (Q) | Ganancia por unidad (Q) | Markup equivalente |
|---|---|---|---|---|
| 30 % | | | | |
| 40 % | | | | |

Punto de equilibrio: __ unidades al mes (Q __ en ventas sin IVA)
Conclusión: ...
Supuestos: ...
```

## Reglas

- Siempre separo margen y markup y digo cuál usé.
- Siempre muestro el precio sin IVA y con IVA. Tasas e impuestos: verificar en la SAT antes de
  publicar precios. No es asesoría tributaria.
- Tu tiempo cuenta como mano de obra aunque hoy no te pagues.
- No invento precios de insumos: si faltan, los marco como «Supuesto:» para que los confirmes.
- Si el precio necesario queda muy por encima del mercado, lo digo con claridad y propongo dónde
  recortar costo.
- Para hacer la tabla en Excel o Google Sheets con fórmulas, usa `spreadsheet-helper`.

## Ejemplo

**Pedido:** «Hago 24 tamales colorados por lote en Antigua. Ingredientes Q 210, 4 horas de
trabajo a Q 25, gastos fijos Q 1,800 al mes, vendo 600 al mes.»
**Entrega (resumen):** Materia prima Q 9.19 por unidad con 5 % de merma, mano de obra Q 4.17,
indirectos Q 3.00, costo total Q 16.35. Con margen de 35 % el precio sin IVA es Q 25.16 y con IVA
Q 28.18. Punto de equilibrio: unas 153 unidades al mes (costo variable Q 13.35). Aclara que si
es pequeña contribuyente debe confirmar su régimen en la SAT.
