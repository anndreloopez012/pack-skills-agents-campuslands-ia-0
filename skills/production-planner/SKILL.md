---
name: production-planner
description: "Arma el plan de producción de la semana o del mes: qué producir, cuánto y qué día, según tus pedidos, tu inventario y tu capacidad. Úsala con «cuánto produzco esta semana», «tengo 40 pedidos, organízame», «qué materia prima necesito para estos pedidos»."
---

# Plan de producción

Convierte tus pedidos en un calendario de producción realista, con la materia prima que necesitas
y sin pasarte de lo que tú y tu equipo pueden hacer. Para talleres, cocinas y pequeñas fábricas.

## Cuándo usarla

- «Tengo 40 pedidos para la feria de Navidad y no sé por dónde empezar.»
- «¿Cuánto chocolate tengo que producir esta semana?»
- «¿Qué materia prima me falta para cumplir estos pedidos?»

## Qué necesito de ti

- Pedidos: producto, cantidad y fecha de entrega.
- Receta o ficha de cada producto: materia prima por unidad y tiempo de producción.
- Capacidad: personas, horas por día, días disponibles, equipo (hornos, máquinas) y su límite.
- Inventario actual de materia prima y de producto terminado.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Ordeno los pedidos por fecha de entrega y luego por tamaño.
2. Resto el producto terminado que ya tienes: produzco solo lo que falta.
3. Calculo horas necesarias por producto y las comparo con las horas disponibles por día.
4. Reparto la producción por día, terminando cada pedido al menos un día antes de la entrega.
5. Agrupo productos parecidos el mismo día para ahorrar preparación y limpieza.
6. Calculo la materia prima total y la comparo con el inventario: lo que falta va a la lista de
   compras con fecha límite según los días de entrega del proveedor.
7. Si la capacidad no alcanza, lo digo y propongo opciones: horas extra, ayuda temporal, mover
   fechas con el cliente o rechazar pedidos.
8. Dejo un día de colchón por semana para imprevistos.

## Lo que te entrego

```
PLAN DE PRODUCCIÓN — semana del [fecha]
Capacidad: __ personas × __ h/día = __ h/día   Necesario: __ h   Uso: __ %

| Día | Producto | Cantidad | Horas | Para el pedido | Entrega |
|---|---|---|---|---|---|

Materia prima
| Insumo | Necesito | Tengo | Falta | Comprar antes de |
|---|---|---|---|---|

Alertas: [pedidos en riesgo, días sobrecargados]
Opciones si no alcanza: ...
Supuestos: ...
```

## Reglas

- No planifico más del 85 % de la capacidad: el resto es colchón.
- Respeto tiempos de reposo, secado u horneado aunque no ocupen mano de obra.
- Si hay personal contratado, las horas extra deben pagarse según el Código de Trabajo vigente;
  verificar con el Ministerio de Trabajo (mintrabajo.gob.gt) antes de programarlas.
- No acepto ni rechazo pedidos por ti: te doy las opciones y tú decides.
- Para el costo de cada producto, usa `product-costing`; para existencias y reorden,
  `inventory-control`.

## Ejemplo

**Pedido:** «Hago chocolate artesanal en Cobán con una ayudante, 6 horas al día. Tengo 300
barras para el viernes y 150 bombones para el sábado. Cada barra lleva 6 minutos y cada bombón 4.»
**Entrega (resumen):** Necesita 30 h para barras y 10 h para bombones: 40 h contra 60 h
disponibles de lunes a viernes (67 %). Barras de lunes a miércoles, bombones el jueves, viernes de
colchón y empaque. Lista de compras: 8 libras de cacao y 200 cajitas antes del martes.
