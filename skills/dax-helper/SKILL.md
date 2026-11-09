---
name: dax-helper
description: "Escribe y explica medidas DAX para Power BI, revisa el modelo de datos (tablas de hechos, dimensiones, relaciones y tabla de fechas) y corrige fórmulas que dan totales raros. Úsala cuando digas «hazme la medida de ventas del año anterior», «por qué mi total no cuadra» o «cómo armo la tabla calendario»."
---

# Power BI y DAX

Te da medidas DAX correctas, con la explicación de cada parte en lenguaje llano, y revisa que el
modelo de datos esté armado para que esas medidas funcionen.

## Cuándo usarla

- «Necesito ventas acumuladas del año y comparación con el año anterior».
- «Mi medida da el mismo número en todas las filas» o «el total no es la suma de las filas».
- «¿Cómo hago la tabla de fechas?» o «¿columna calculada o medida?».

## Qué necesito de ti

- Las tablas del modelo con sus columnas (nombre y tipo) y cómo se relacionan. Una captura de la
  vista de modelo o la lista sirve.
- Qué quieres calcular, en una frase, y cómo lo vas a mostrar (tarjeta, tabla por mes, por
  vendedor).
- La fórmula que ya intentaste, si existe, y qué resultado te da.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Reviso el modelo: tablas de hechos (ventas, gastos) y dimensiones (cliente, producto, fecha),
   relaciones de uno a varios desde la dimensión hacia el hecho, filtro en una sola dirección
   salvo razón clara. Si hay relaciones de varios a varios o bidireccionales, lo señalo.
2. Verifico la tabla de fechas: continua (sin días faltantes), que cubra todo el rango de los
   datos, relacionada por una columna de tipo fecha y marcada como tabla de fechas. Si no existe,
   la entrego:
   `Calendario = ADDCOLUMNS(CALENDAR(DATE(2024,1,1), DATE(2026,12,31)), "Año", YEAR([Date]), "Mes", FORMAT([Date], "mmmm"), "MesNum", MONTH([Date]))`
3. Escribo primero las medidas base explícitas (`Ventas = SUM(Ventas[Monto])`) y construyo las
   demás sobre ellas.
4. Uso CALCULATE para cambiar el contexto de filtro y explico qué filtro agrega, quita o
   reemplaza:
   - Año anterior: `Ventas AA = CALCULATE([Ventas], SAMEPERIODLASTYEAR(Calendario[Date]))`
   - Acumulado del año: `Ventas YTD = TOTALYTD([Ventas], Calendario[Date])`
   - Variación %: `Var % = DIVIDE([Ventas] - [Ventas AA], [Ventas AA])`
   - Participación: `% del total = DIVIDE([Ventas], CALCULATE([Ventas], ALL(Producto)))`
   - Con filtro fijo: `Ventas Contado = CALCULATE([Ventas], Ventas[Tipo] = "Contado")`
5. Explico el contexto de fila y el contexto de filtro con el caso concreto, y por qué un total
   no cuadra (por ejemplo, un promedio de promedios; se corrige con SUMX o AVERAGEX sobre la
   tabla correcta).
6. Indico si va como medida (se calcula según los filtros del visual) o como columna calculada
   (se guarda fila por fila), y prefiero medidas para todo lo que se suma o compara.
7. Propongo cómo probarla: una tabla con Año y Mes y comparar dos o tres valores a mano.

## Lo que te entrego

```
Revisión del modelo
| Tabla | Tipo (hecho/dimensión) | Llave | Relación con | Cardinalidad | Dirección | Observación |

Medidas
| Medida | DAX | Qué hace, en llano | Depende de | Dónde usarla |

Explicación paso a paso de la medida principal
1. CALCULATE toma [Ventas] ...
2. El filtro SAMEPERIODLASTYEAR mueve las fechas ...

Cómo comprobarla
- Filtra marzo de 2026: [Ventas AA] debe ser igual a [Ventas] de marzo de 2025 = Q ____

Supuestos
- Supuesto: ...
```

## Reglas

- Siempre DIVIDE en lugar de «/» para evitar errores al dividir entre cero.
- Las funciones de inteligencia de tiempo solo funcionan bien con una tabla de fechas continua y
  marcada; si no la hay, lo digo antes que cualquier otra cosa.
- Nombres de medidas claros y en español; un formato por medida (Q con 2 decimales, porcentaje).
- No recomiendo filtros bidireccionales ni ALL sobre toda la tabla de hechos sin explicar el
  efecto.
- Si el separador de argumentos en la configuración regional de la persona es punto y coma,
  ajusto las fórmulas.
- Si la tabla tiene datos personales o salarios, propone `data-shield` antes de pegarla.
- Para preparar los datos antes del modelo, remito a `data-cleaner`; para fórmulas de Excel,
  a `spreadsheet-helper`.

## Ejemplo

**Pedido:** «Quiero ver ventas de este año contra el año pasado por vendedor, y mi medida me da
el total en todas las filas».
**Entrega (resumen):** detecto que la tabla Vendedor no está relacionada con Ventas; propongo la
relación por CodigoVendedor, la tabla Calendario marcada, y las medidas Ventas, Ventas AA, Var %
y Ventas YTD con su explicación y una prueba con marzo.
