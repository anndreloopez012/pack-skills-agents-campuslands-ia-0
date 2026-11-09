---
name: data-cleaner
description: "Revisa una tabla de Excel, CSV o Power Query y detecta duplicados, vacíos, tipos mal puestos, fechas y montos con formato distinto y valores fuera de rango, y te dice cómo corregir cada problema. Úsala cuando digas «limpia esta base», «tengo duplicados» o «Power BI no me suma esta columna»."
---

# Limpieza de datos

Encuentra lo que está sucio en una tabla antes de analizarla y te da los pasos exactos para
corregirlo en Excel, Google Sheets o Power Query, sin perder el dato original.

## Cuándo usarla

- «Limpia esta base de ventas antes de meterla a Power BI».
- «Tengo clientes repetidos con nombres escritos distinto».
- «La columna de montos no suma» o «las fechas salen en desorden».
- Antes de usar `dax-helper`, `dashboard-designer` o `people-analytics`.

## Qué necesito de ti

- La tabla (pegada, o una muestra de 20 a 50 filas con los encabezados) y cuántas filas tiene en
  total.
- Qué representa cada fila (una venta, un empleado, una solicitud) y cuál es la llave que la
  identifica (número de factura, código de empleado).
- Dónde la vas a usar: Excel, Google Sheets o Power BI.
- Si la tabla trae nombres, DPI, NIT, teléfonos o salarios, propón primero `data-shield`.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Describo la tabla: filas, columnas, tipo esperado de cada columna (texto, número, fecha,
   categoría) y la llave.
2. Reviso en este orden, columna por columna:
   - Duplicados exactos y duplicados por llave (misma factura dos veces).
   - Vacíos: cuántos y si son «no aplica», «no se sabe» o un error de captura.
   - Tipos: números guardados como texto (Q 1,250.00 con «Q» o comas), fechas como texto,
     formatos mezclados (dd/mm/aaaa y mm/dd/aaaa).
   - Texto inconsistente: espacios de más, mayúsculas, tildes, variantes («Guatemala», «Guate»,
     «GUATEMALA »), departamentos y municipios mal escritos.
   - Valores fuera de rango: montos negativos donde no caben, edades de 150, fechas futuras.
   - Columnas combinadas (nombre y apellido juntos, «Zona 10, Guatemala»).
3. Para cada problema cuento cuántas filas afecta y muestro 2 o 3 ejemplos.
4. Propongo la corrección en la herramienta que usa la persona: fórmula de Excel (ESPACIOS,
   NOMPROPIO, VALOR, FECHA, BUSCARX), paso de Power Query (Quitar duplicados, Reemplazar valores,
   Cambiar tipo con configuración regional «Español (Guatemala)», Dividir columna) o función de
   Sheets.
5. Separo lo que se corrige con regla de lo que necesita decisión humana (dos clientes parecidos
   que quizá son distintos).
6. Cierro con una regla de calidad para que el problema no vuelva (lista desplegable, validación
   de datos, formulario).

## Lo que te entrego

```
Diagnóstico de limpieza · Tabla: ________ · Filas: ____ · Columnas: ____
Llave: ________ · Destino: Excel / Sheets / Power BI

| # | Columna | Problema | Filas afectadas | Ejemplo | Corrección propuesta | Herramienta | Decide |
|---|---------|----------|-----------------|---------|----------------------|-------------|--------|
| 1 | Monto   | Texto con «Q» y comas | 312 | «Q 1,250.00» | Reemplazar «Q » y «,» y cambiar tipo a decimal | Power Query | Regla |
| 2 | Cliente | Variantes del mismo nombre | 18 | «Ferretería El Sol» / «Ferreteria el sol» | Unificar con tabla de equivalencias | Excel BUSCARX | Persona |

Orden sugerido de corrección
1. ...

Reglas para que no vuelva a pasar
- ...

Supuestos
- Supuesto: ...
```

## Reglas

- Nunca borro ni sobrescribo el dato original: recomiendo trabajar en una copia o en una columna
  nueva, y en Power Query los pasos quedan registrados.
- No invento valores para llenar vacíos. Si propongo imputar (promedio, «Sin dato»), lo digo y
  explico el efecto en el análisis.
- Montos en quetzales con punto decimal y coma de miles, salvo que la persona use otro formato.
- Si un duplicado podría ser legítimo (dos compras iguales el mismo día), lo marco para revisión.
- Si la base trae datos personales, no los repito en mi respuesta más allá de lo necesario.

## Ejemplo

**Pedido:** «Limpia esta base de 4,000 ventas que exporté del sistema; Power BI no suma Monto».
**Entrega (resumen):** diagnóstico con 6 problemas: Monto como texto con «Q» (todas las filas),
fechas mezcladas en 230 filas, 41 facturas duplicadas por llave, 3 variantes de «Quetzaltenango»,
12 montos negativos que son notas de crédito y 90 vendedores vacíos. Pasos de Power Query en orden
y una lista desplegable de departamentos para la captura.
