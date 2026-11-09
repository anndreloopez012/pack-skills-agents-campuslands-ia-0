---
name: inventory-control
description: "Lleva entradas, salidas y existencias de materia prima y producto terminado, con mínimos, punto de reorden y aviso de lo que se está acabando. Úsala con «cuánto me queda de harina», «arma mi control de inventario», «qué tengo que comprar»."
---

# Inventario y materia prima

Ordena lo que entra, lo que sale y lo que queda en bodega, y te avisa a tiempo qué se está
acabando. Para negocios pequeños que producen o revenden y hoy cuentan «a ojo».

## Cuándo usarla

- «Se me acabó el cacao en plena temporada y perdí pedidos.»
- «Quiero un control sencillo de inventario en Excel o en un cuaderno.»
- «Con estas compras y ventas del mes, ¿cuánto me queda de cada cosa?»

## Qué necesito de ti

- Lista de artículos (materia prima, empaque, producto terminado) con su unidad: libra, unidad,
  galón, rollo.
- Existencia inicial, compras (entradas) y consumos o ventas (salidas) del periodo.
- Cuánto usas por semana o por día, en promedio, y cuántos días tarda tu proveedor en entregar.
- Costo de compra por unidad, si quieres saber cuánto dinero tienes en bodega.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Armo la lista de artículos con código corto, unidad y proveedor.
2. Calculo existencia final = inicial + entradas − salidas, artículo por artículo.
3. Calculo el consumo diario promedio = salidas del periodo ÷ días del periodo.
4. Defino el stock de seguridad: consumo diario × días de colchón (uso 3 a 7 días según qué tan
   confiable es el proveedor; lo marco como supuesto).
5. Calculo el punto de reorden = consumo diario × días de entrega + stock de seguridad.
6. El mínimo es el stock de seguridad; el máximo, lo que cabe y conviene tener (si no lo sabes,
   uso consumo de 30 días).
7. Pongo el semáforo: rojo si está en el mínimo o debajo, amarillo si llegó al punto de reorden,
   verde si está arriba.
8. Para lo que está en rojo o amarillo sugiero cuánto pedir: máximo − existencia actual.
9. Si hay diferencias entre lo contado y lo calculado, las listo para revisar (merma, error de
   registro o pérdida).

## Lo que te entrego

```
INVENTARIO — periodo [del __ al __] — contado el [fecha]

| Código | Artículo | Unidad | Inicial | Entradas | Salidas | Final | Consumo/día | Días de entrega | Mínimo | Punto de reorden | Máximo | Estado | Pedir |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  | Rojo / Amarillo / Verde |  |

Valor en bodega: Q __ (a costo de compra)
Diferencias contra el conteo físico: ...
Supuestos: ...
```

Registro diario sugerido (para llenar en el cuaderno o la hoja):

```
| Fecha | Código | Movimiento (Entrada/Salida) | Cantidad | Motivo (compra, producción, venta, merma) | Quién |
```

## Reglas

- Una sola unidad por artículo: si compras por quintal y usas por libra, convierto y lo dejo
  escrito (1 quintal = 100 libras).
- Primero en entrar, primero en salir para alimentos y todo lo que vence; señalo fechas de
  vencimiento cercanas.
- Las cifras de días de colchón y de entrega son supuestos hasta que tú las confirmes.
- No hago pedidos a proveedores: te digo qué y cuánto pedir y tú decides.
- Para la hoja con fórmulas y semáforo automático, usa `spreadsheet-helper`. Para el aviso cada
  semana, el agente `restock-alert`.

## Ejemplo

**Pedido:** «Panadería en Mixco. Harina: tenía 12 quintales, compré 20, usé 24 en el mes. El
proveedor tarda 3 días.»
**Entrega (resumen):** Existencia final 8 quintales. Consumo diario 0.8 quintales (30 días).
Stock de seguridad con 4 días de colchón: 3.2. Punto de reorden: 0.8 × 3 + 3.2 = 5.6 quintales.
Estado verde por ahora; máximo 24 quintales, así que al bajar de 5.6 conviene pedir unos 18.
