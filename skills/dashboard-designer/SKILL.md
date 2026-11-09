---
name: dashboard-designer
description: "Diseña un tablero de Power BI, Excel o Looker Studio: qué indicadores mostrar, con qué gráfico, en qué orden y con qué filtros, según quién lo va a leer y qué decisión toma. Úsala cuando digas «diseña mi tablero», «qué gráfico uso» o «mi dashboard tiene demasiadas cosas»."
---

# Diseño de tablero

Te dice qué poner en el tablero, qué gráfico usar para cada dato y cómo ordenarlo para que la
persona que lo lee entienda en 10 segundos si todo va bien o dónde mirar.

## Cuándo usarla

- «Arma el diseño de un tablero de ventas para la gerencia».
- «¿Uso barras, líneas o pastel para esto?».
- «Mi tablero tiene 14 gráficos y nadie lo entiende».

## Qué necesito de ti

- Quién lo va a leer (gerencia, jefes de área, operación) y cada cuánto.
- Qué decisión toma con él (reasignar presupuesto, llamar a un cliente, reforzar una sucursal).
- Los datos disponibles: tablas y columnas, o las medidas que ya tienes.
- La herramienta: Power BI, Excel o Looker Studio.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Escribo la pregunta principal del tablero en una frase («¿Vamos a cumplir la meta de ventas
   del mes?»). Si no la hay, el tablero no está listo para diseñarse.
2. Elijo entre 3 y 5 indicadores principales (KPI) y para cada uno defino: fórmula, meta,
   comparación (contra meta, contra año anterior) y semáforo.
3. Asigno el gráfico según lo que se quiere ver:
   - Comparar categorías: barras horizontales ordenadas de mayor a menor.
   - Evolución en el tiempo: línea (o columnas si son pocos periodos).
   - Parte de un todo: barra apilada al 100 % o tabla; pastel solo con 2 o 3 partes.
   - Un número contra su meta: tarjeta con variación y color.
   - Detalle para buscar: tabla o matriz con formato condicional.
   - Ubicación: mapa por departamento solo si la geografía importa para la decisión.
4. Ordeno la página en forma de Z: arriba a la izquierda los KPI, al centro la tendencia, abajo
   el detalle. Filtros (fecha, sucursal, producto) en una franja fija.
5. Defino colores con significado: un color neutro para todo y un solo color de alerta; verde,
   amarillo y rojo solo para semáforos. Cuido contraste y no dependo solo del color.
6. Propongo la navegación: página resumen, páginas de detalle y explorar en profundidad
   (drill-down) cuando haga falta.
7. Reviso que cada elemento responda la pregunta principal; lo que no, sale o va a otra página.

## Lo que te entrego

```
Tablero: ________ · Lee: ________ · Frecuencia: ________
Pregunta principal: ¿...?

Indicadores principales
| KPI | Fórmula o medida | Meta | Compara contra | Semáforo (verde / amarillo / rojo) |

Elementos por página
| Página | Zona (arriba / centro / abajo) | Elemento | Tipo de gráfico | Dato | Por qué este gráfico |

Filtros: ________
Colores: neutro ____ · alerta ____ · semáforo solo en KPI

Bosquejo de la página resumen
+-----------+-----------+-----------+
|  KPI 1    |  KPI 2    |  KPI 3    |
+-----------+-----------+-----------+
|  Tendencia mensual vs meta        |
+-----------------------------------+
|  Detalle por sucursal (tabla)     |
+-----------------------------------+

Lo que quité y por qué
- ...
```

## Reglas

- Menos es más: máximo 6 a 8 elementos por página.
- Nada de gráficos 3D, pasteles con muchas partes ni ejes que no empiezan en cero en barras.
- Cada número con su unidad (Q, %, días) y su periodo.
- Títulos que dicen la conclusión («Ventas 8 % bajo meta en octubre»), no solo el tema.
- Si un indicador no tiene dato confiable, lo marco como pendiente en vez de inventarlo.
- Para las medidas DAX remito a `dax-helper`; para limpiar la fuente, a `data-cleaner`; para
  contar la historia en una reunión, a `data-story`.

## Ejemplo

**Pedido:** «Diseña el tablero mensual de mantenimiento para el gerente administrativo».
**Entrega (resumen):** pregunta principal «¿Estamos atendiendo a tiempo?»; 4 KPI (solicitudes
cerradas en plazo %, tiempo medio de cierre en días, costo del mes contra presupuesto en Q,
preventivos cumplidos %); línea de 12 meses, barras por edificio y tabla de pendientes vencidos.
