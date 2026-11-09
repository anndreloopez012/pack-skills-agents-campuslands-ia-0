---
name: experiment-card
description: "Documenta un análisis o experimento con datos en una ficha fija: problema, hipótesis, dataset, herramientas, metodología, validación, hallazgos, limitaciones, aplicación, contenido derivado y estado. Úsala cuando digas «arma la ficha de este análisis», «documenta mi experimento» o «quiero esto en mi portafolio»."
---

# Ficha de experimento

Deja cada análisis documentado igual que el anterior, para repetirlo, mostrarlo en tu portafolio
o convertirlo en una publicación sin depender de la memoria.

## Cuándo usarla

- «Terminé un análisis en Power BI, documéntalo».
- «Quiero probar si las ventas suben con la promoción; arma la ficha antes de empezar».
- «Pasa este notebook o estas notas a una ficha para mi portafolio».
- La usa el agente `data-lab` en cada experimento.

## Qué necesito de ti

- La pregunta o el problema, aunque sea en borrador.
- De dónde salen los datos (archivo, sistema, dataset público con su enlace y licencia).
- Lo que ya hiciste: pasos, fórmulas, gráficos, resultados, aunque estén desordenados.
- Si los datos son de personas (empleados, clientes, pacientes), confirma que son autorizados o
  sintéticos y propone `data-shield` antes de pegarlos.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Escribo el problema como una decisión o pregunta concreta, con quién la necesita.
2. Formulo la hipótesis en forma comprobable: «Si ___, entonces ___, medido con ___». Si es
   exploratorio, lo digo y escribo la pregunta guía en lugar de hipótesis.
3. Describo el dataset: fuente, periodo, filas, columnas clave, licencia y si tiene datos
   personales.
4. Listo herramientas con versión cuando importe (Excel, Power BI, Python, Sheets).
5. Escribo la metodología en pasos que otra persona pueda repetir: limpieza (con `data-cleaner`),
   transformación, cálculo, modelo o comparación.
6. Defino la validación antes de ver resultados: contra qué se compara (periodo anterior, grupo
   control, cálculo a mano), qué umbral considero suficiente y cómo verifiqué que no hubo error.
7. Escribo hallazgos con número, unidad y periodo, separando lo que el dato muestra de lo que
   interpreto. Correlación no es causa: lo digo cuando aplique.
8. Escribo limitaciones honestas: tamaño de muestra, sesgos, datos faltantes, periodo corto.
9. Propongo la aplicación práctica y quién la decide.
10. Propongo contenido derivado (publicación de LinkedIn, carrusel, caso de portafolio) con
    `data-story`, cuidando no exponer datos confidenciales.
11. Marco el estado.

## Lo que te entrego

```
Ficha de experimento · ID: EXP-AAAA-NN · Fecha: __/__/____ · Autor: ________

Problema:          ...
Hipótesis:         Si ___, entonces ___, medido con ___. (o «Exploratorio: pregunta guía ...»)
Dataset:           Fuente ___ · Periodo ___ · Filas ___ · Licencia ___ · Datos personales: sí/no (cómo se protegieron)
Herramientas:      ...
Metodología:       1. ... 2. ... 3. ...
Validación:        Compara contra ___ · Criterio de éxito ___ · Comprobación ___
Hallazgos:         - [Dato] ...  - [Interpretación] ...
Limitaciones:      - ...
Aplicación:        Qué se haría · Quién decide · Costo o esfuerzo estimado
Contenido derivado: - Publicación ... - Caso de portafolio ...
Estado:            Idea / En curso / Validado / Descartado / Publicado
```

## Reglas

- Todos los campos van siempre, en ese orden. Si uno no aplica o no se sabe, escribo «Pendiente»
  o «No aplica», nunca lo borro.
- La validación se define antes de mirar resultados para no acomodar la conclusión.
- Un experimento con hipótesis rechazada también es un hallazgo y se documenta.
- No invento cifras: si la persona no me dio el resultado, el campo queda «Pendiente».
- Datos de personas solo autorizados, anonimizados o sintéticos; nunca nombres reales en el
  contenido derivado.
- Dataset público: siempre con enlace, fecha de consulta y licencia.

## Ejemplo

**Pedido:** «Probé si los clientes que reciben recordatorio por WhatsApp pagan antes. Tengo dos
grupos de 120 facturas cada uno».
**Entrega (resumen):** ficha EXP-2026-07 con hipótesis «si se envía recordatorio 3 días antes del
vencimiento, los días promedio de atraso bajan», validación contra el grupo sin recordatorio,
hallazgo 6.1 contra 9.4 días de atraso, limitación de un solo mes y estado «Validado», con idea
de publicación para LinkedIn sin datos de clientes.
