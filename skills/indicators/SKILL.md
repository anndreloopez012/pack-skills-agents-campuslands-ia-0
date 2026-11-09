---
name: indicators
description: "Diseña indicadores de gestión y de resultados con fórmula, línea base, meta, fuente, frecuencia y semáforo, y los ordena en un tablero. Úsala cuando digas «define indicadores para este resultado», «arma la ficha técnica del indicador» o «haz un semáforo de metas»."
---

# Indicadores y tableros

Convierte metas y resultados en indicadores que se pueden medir de verdad, con su ficha técnica y
un semáforo simple para seguirlos cada mes o cuatrimestre.

## Cuándo usarla

- «Necesito indicadores para los resultados del PEI».
- «Arma la ficha técnica de este indicador para SEGEPLAN».
- «Haz un tablero con semáforo para el comité de dirección».

## Qué necesito de ti

- El resultado, producto o proceso que quieres medir.
- Los datos que ya registras (sistema, hoja de cálculo, libro) y cada cuánto se actualizan.
- Metas que ya se comprometieron, si existen.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Ubico qué se mide en la cadena de resultados de la Gestión por Resultados: insumo (gasto),
   producto (lo que se entrega), resultado (cambio en la población) o impacto. Propongo al menos
   un indicador de producto y uno de resultado.
2. Defino el tipo: eficacia (cuánto se logró de la meta), eficiencia (costo o tiempo por unidad),
   calidad (satisfacción, cumplimiento de estándar) o economía (ejecución presupuestaria).
3. Escribo la fórmula exacta con numerador, denominador y unidad. Ejemplo: «(Expedientes
   resueltos en plazo / Expedientes ingresados) × 100».
4. Fijo línea base (valor, año y fuente), meta y plazo. Si no hay línea base, propongo cómo
   levantarla en el primer periodo.
5. Reviso con criterio SMART y con la prueba CREMA (claro, relevante, económico, medible,
   adecuado).
6. Defino el semáforo: verde, amarillo y rojo con umbrales numéricos explícitos, y el sentido del
   indicador (si es mejor que suba o que baje).
7. Ordeno los indicadores en un tablero: arriba los de resultado, abajo los de producto y
   proceso. Para construirlo en Excel o Sheets, apóyate en `spreadsheet-helper`.

## Lo que te entrego

```
Ficha técnica del indicador
- Nombre:
- Nivel (producto / resultado / impacto):
- Tipo (eficacia / eficiencia / calidad / economía):
- Fórmula:
- Unidad de medida:
- Sentido (ascendente / descendente):
- Línea base (valor, año, fuente):
- Meta (valor, plazo):
- Frecuencia de medición:
- Fuente de datos y responsable:
- Desagregación (sexo, edad, municipio, pueblo):
- Semáforo: verde ≥ __ · amarillo __ a __ · rojo < __
- Limitaciones:

Tablero
| Indicador | Meta | Valor del periodo | % de avance | Semáforo | Comentario |
```

## Reglas

- Un indicador mide una sola cosa. Si la fórmula tiene «y», probablemente son dos.
- No cuento actividades como resultados: «talleres realizados» mide producto, no cambio.
- La meta debe poder lograrse con el presupuesto y el plazo; si se ve inalcanzable, lo digo.
- Desagrega por sexo, edad, territorio y pueblo cuando el dato exista; lo piden muchos
  lineamientos públicos.
- No invento líneas base ni datos nacionales. Para buscarlos uso `source-researcher` con fuente y
  fecha.
- Formatos de fichas de SEGEPLAN o del ente rector: verificar el vigente; revisado: noviembre de
  2026.

## Ejemplo

**Pedido:** «Indicador para el resultado: reducir el tiempo de respuesta a solicitudes de
información pública».
**Entrega (resumen):** «Porcentaje de solicitudes respondidas dentro del plazo legal» = (respondidas
en plazo / recibidas en el periodo) × 100, sentido ascendente, línea base pendiente del registro de
la unidad de información, meta 95 %, semáforo verde ≥ 95, amarillo 85 a 94, rojo < 85; plazo legal
a verificar en la ley vigente.
