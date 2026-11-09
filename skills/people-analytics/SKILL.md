---
name: people-analytics
description: "Calcula e interpreta indicadores de personas: rotación, rotación voluntaria, ausentismo, antigüedad y resultados de encuestas de clima, solo con datos autorizados, anonimizados o sintéticos. Úsala cuando digas «calcula la rotación del trimestre», «cuánto ausentismo tenemos» o «analiza la encuesta de clima»."
---

# People Analytics

Convierte los registros de recursos humanos en indicadores claros de rotación, ausentismo y clima,
con su fórmula, para tomar decisiones sobre equipos y no sobre personas sueltas.

## Cuándo usarla

- «Calcula la rotación mensual y anual por área».
- «¿Cuánto ausentismo tuvimos y en qué área se concentra?».
- «Resume la encuesta de clima y dime qué mejorar primero».
- «Quiero practicar con datos de ejemplo»: genero un dataset sintético.

## Qué necesito de ti

- Confirmación de que los datos están autorizados por la empresa para este análisis, o que son
  de práctica. Sin esa confirmación, solo trabajo con datos sintéticos.
- Altas y bajas del periodo (fecha y tipo de baja: voluntaria o involuntaria), plantilla al
  inicio y al final, y área.
- Para ausentismo: días u horas perdidas por causa (enfermedad, suspensión IGSS, permiso, falta)
  y días u horas programados.
- Para clima: preguntas, escala y respuestas sin nombre.
- Antes de pegar cualquier listado con nombres, DPI, salarios o diagnósticos, usa `data-shield`.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Verifico la autorización y que no haya identificadores. Reemplazo nombres por códigos.
2. Calculo plantilla promedio = (plantilla al inicio + plantilla al final) / 2.
3. Calculo rotación:
   - Rotación del periodo % = bajas del periodo / plantilla promedio × 100.
   - Rotación voluntaria % = bajas voluntarias / plantilla promedio × 100 (renuncias).
   - Rotación anualizada (si el periodo es un mes) ≈ rotación mensual × 12, aclarando que es
     aproximada; mejor sumar las bajas de 12 meses sobre la plantilla promedio del año.
   - Rotación temprana % = bajas con menos de 6 meses de antigüedad / ingresos del periodo × 100.
4. Calculo ausentismo:
   - Tasa de ausentismo % = días (u horas) perdidos / días (u horas) programados × 100.
   - Frecuencia = número de ausencias / plantilla promedio (cuántas veces falta cada persona en
     promedio).
   - Separo ausencias justificadas por suspensión del IGSS de las no justificadas.
5. Para clima: porcentaje favorable por pregunta (respuestas 4 y 5 en escala de 1 a 5), por
   dimensión y por área, sin mostrar grupos de menos de 5 personas.
6. Comparo por área, puesto, antigüedad y periodo; señalo dónde se concentra el problema.
7. Propongo 2 o 3 hipótesis de causa para validar con entrevistas o encuesta, sin señalar
   personas.

## Lo que te entrego

```
People Analytics · Periodo: ________ · Datos: autorizados / sintéticos · Plantilla promedio: ___

Rotación
| Área | Plantilla prom. | Bajas | Voluntarias | Rotación % | Rot. voluntaria % | Rot. temprana % |

Ausentismo
| Área | Días programados | Días perdidos | Tasa % | Frecuencia | Causa principal |

Clima (solo grupos de 5 o más)
| Dimensión | % favorable | Cambio vs anterior | Área más baja |

Lo que dicen los números
- ...
Hipótesis para validar
- ...
Acciones sugeridas (las decide RR. HH.)
- ...
Fórmulas usadas: (las de arriba, escritas)
```

## Reglas

- Nunca analizo, ordeno ni predigo el comportamiento de una persona identificable («quién se va a
  ir»). El análisis es por grupo.
- No muestro resultados de grupos de menos de 5 personas para no revelar a nadie.
- Datos de salud, sanciones o salarios son sensibles: solo agregados y con autorización.
- Si no hay autorización, genero un dataset sintético realista (área, fecha de ingreso, fecha de
  baja, tipo de baja, días de ausencia) y lo marco como tal.
- Las reglas legales de suspensiones, permisos y prestaciones dependen del Código de Trabajo y
  del IGSS: si una conclusión depende de ellas, indico verificar en `mintrabajo.gob.gt` e
  `igssgt.org` (revisado: noviembre de 2026).
- Para tablas y medidas en Power BI remito a `dax-helper`; para presentar a la gerencia, a
  `data-story`.

## Ejemplo

**Pedido:** «Datos sintéticos: 180 personas al inicio, 172 al final, 21 bajas (14 voluntarias),
1,140 días de ausencia de 40,000 programados».
**Entrega (resumen):** plantilla promedio 176; rotación 11.9 %; voluntaria 8.0 %; ausentismo
2.85 %; tabla por área con Bodega concentrando la mitad de las renuncias y tres hipótesis para
validar (horario, distancia, liderazgo), sin datos de personas.
