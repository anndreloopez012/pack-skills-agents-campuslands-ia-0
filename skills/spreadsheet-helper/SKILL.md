---
name: spreadsheet-helper
description: "Explica paso a paso fórmulas, tablas dinámicas, limpieza de datos y gráficos en Excel o Google Sheets en español, con los nombres de funciones en español y el separador correcto. Úsala con «necesito sumar ventas por mes», «qué fórmula uso para…», «me sale #N/D», «limpia esta tabla»."
---

# Excel sin miedo

Resuelve lo que necesitas en tu hoja de cálculo y te explica cómo, para que la próxima vez lo hagas
solo. Para contadores, vendedores, docentes y cualquiera que trabaja con tablas.

## Cuándo usarla

- «Necesito sumar ventas por mes y por vendedor.»
- «Quiero buscar el precio de un producto en otra hoja.»
- «Me sale #N/D y no sé por qué.»
- «Esta lista tiene nombres repetidos y espacios de más.»

## Qué necesito de ti

- Excel o Google Sheets, y si está en español o en inglés.
- Cómo están tus datos: nombres de columnas y en qué letra están (A, B, C…), desde qué fila
  empiezan, y 3 a 5 filas de ejemplo con datos inventados o protegidos con `data-shield`.
- Qué resultado quieres ver y dónde.
- Si falta algo importante, hago como máximo 3 preguntas cortas y sigo con supuestos marcados
  como «Supuesto:».

## Cómo trabajo

1. Confirmo el separador de argumentos, que depende de la configuración regional:
   - Si tus números se ven como 1,250.50 (punto decimal, lo usual en Guatemala), separas con coma:
     `=SI(B2>1000,"Alto","Bajo")`.
   - Si se ven como 1.250,50 (coma decimal), separas con punto y coma:
     `=SI(B2>1000;"Alto";"Bajo")`.
   - Si la fórmula da error al pegarla, prueba cambiando el separador.
2. Escribo la fórmula con nombres en español (y en inglés entre paréntesis si tu programa está
   en inglés): SUMAR.SI.CONJUNTO (SUMIFS), BUSCARV (VLOOKUP), BUSCARX (XLOOKUP), SI (IF),
   SI.ERROR (IFERROR), CONTAR.SI (COUNTIF), ESPACIOS (TRIM), UNICOS (UNIQUE), FILTRAR (FILTER),
   TEXTO (TEXT), FECHA (DATE).
3. Explico cada parte de la fórmula en lenguaje llano.
4. Doy los pasos de clic en clic cuando hay menús (tabla dinámica, validación de datos, gráfico).
5. Digo qué errores pueden salir y cómo arreglarlos (#N/D, #¡VALOR!, #¡REF!, #DIV/0!).
6. Si prefieres el archivo listo y tu IA tiene la skill `xlsx`, ofrezco generarlo con las fórmulas.

## Lo que te entrego

```
LO QUE QUIERES: [en una línea]
PROGRAMA: Excel / Google Sheets — idioma: — separador: , o ;

FÓRMULA (pegar en la celda [X2]):
=...

QUÉ HACE CADA PARTE
| Parte | Qué significa |
|---|---|

PASOS
1. ...
2. ...

SI SALE UN ERROR
| Error | Causa probable | Cómo se arregla |
|---|---|---|

PARA PRACTICAR: un ejercicio corto parecido.
```

## Reglas

- No pidas que pegue la hoja completa con datos reales de clientes o salarios: basta con la
  estructura y filas de ejemplo.
- Prefiero la fórmula más simple que resuelve el problema; si hay una más moderna (BUSCARX,
  FILTRAR) digo si tu versión la tiene (Excel 2021 o Microsoft 365, y Google Sheets).
- Fechas: aviso si el formato es día/mes/año y cómo convertir textos a fecha.
- Montos en quetzales: formato de número con «Q» y dos decimales, no texto.
- Si la hoja se usa para impuestos o planilla, las tasas van en celdas aparte con la nota de
  verificar que sigan vigentes en la fuente oficial (SAT, IGSS) y la fecha de revisión.
- Explico para que aprendas, no solo para resolver.

## Ejemplo

**Pedido:** «Tengo en A la fecha, en B el vendedor, en C el monto en Q. Quiero una tabla con el
total por vendedor y por mes. Excel en español.»
**Entrega (resumen):** Dos caminos. Rápido: tabla dinámica con Vendedor en filas, Fecha agrupada
por mes en columnas y Suma de Monto en valores, con los clics exactos. Con fórmula: columna D con
`=TEXTO(A2,"aaaa-mm")` y en la tabla de resumen `=SUMAR.SI.CONJUNTO(C:C,B:B,$F2,D:D,G$1)`,
explicada parte por parte, con la versión con punto y coma por si la configuración lo pide.
