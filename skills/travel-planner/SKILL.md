---
name: travel-planner
description: "Arma el itinerario de un viaje día por día con ruta, costos aproximados en quetzales, clima, eventos, gastronomía y paisajes, con fuentes confiables y fechas verificadas. Úsala con «planéame 4 días en Petén», «itinerario para ir a Ciudad de México», «qué hago un fin de semana en Antigua»."
---

# Itinerario de viaje

Te arma un plan de viaje realista, con tiempos de traslado, presupuesto y lo que vale la pena ver
y comer, y con cada evento y precio respaldado por una fuente. Para viajes de placer dentro y fuera
de Guatemala.

## Cuándo usarla

- «Quiero ir 4 días a Petén en Semana Santa con mi familia.»
- «Fin de semana en Antigua con Q 2,500 para dos personas.»
- «Viaje a Ciudad de México en diciembre: museos, comida y algún concierto.»

## Qué necesito de ti

- Destino o región, fechas o mes, y número de días.
- Quiénes viajan (adultos, niños, adultos mayores) y su ritmo.
- Presupuesto aproximado en quetzales y cómo te mueves (carro propio, bus, vuelo, tour).
- Qué te gusta: naturaleza, historia, comida, compras, aventura, descanso, conciertos.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Investigo con `source-researcher` en fuentes confiables: INGUAT (visitguatemala.com), sitios
   oficiales de parques, museos y eventos, aerolíneas, embajadas y medios reconocidos.
2. Cada evento, horario y precio lleva su fuente, el enlace y la fecha en que lo revisé. Si no lo
   pude confirmar para tus fechas, lo marco como «Por confirmar».
3. Reviso el clima típico del mes y la temporada (lluvias de mayo a octubre en buena parte de
   Guatemala) con fuente, y lo uso para ordenar actividades.
4. Armo la ruta por días agrupando lugares cercanos y calculando traslados realistas.
5. Estimo costos por categoría: transporte, hospedaje, comida, entradas, extras. Todo en
   quetzales; si es en otra moneda, indico el tipo de cambio usado y su fecha (Banguat).
6. Incluyo gastronomía local y miradores o paisajes con la mejor hora para ir.
7. Agrego requisitos: pasaporte, visa, vacunas o permisos, siempre con la fuente oficial.
8. Dejo un plan B por día si llueve o algo cierra.

## Lo que te entrego

```
ITINERARIO: [destino] — [fechas] — [personas] — revisado el [fecha]

| Día | Mañana | Tarde | Noche | Traslados | Dónde comer | Costo aprox. (Q) |
|---|---|---|---|---|---|---|

Eventos en tus fechas
| Evento | Fecha | Lugar | Precio | Fuente (enlace) | Verificado el |
|---|---|---|---|---|---|

Presupuesto
| Rubro | Q por persona | Q total | Fuente o supuesto |
|---|---|---|---|

Clima esperado: ... (fuente)
Requisitos y documentos: ... (fuente oficial)
Plan B por día: ...
Por confirmar antes de pagar: ...
```

## Reglas

- Ningún evento, fecha ni precio sin fuente y fecha de revisión. Lo no verificado dice «Por
  confirmar» y no se presenta como seguro.
- Los precios son aproximados y cambian: confirma en la fuente antes de comprar.
- Requisitos migratorios y sanitarios solo de fuentes oficiales (embajadas, Migración Guatemala).
- No hago reservas ni pagos, y nunca pido datos de tarjeta ni pasaporte: te dejo los enlaces.
- Incluyo recomendaciones de seguridad generales y sugiero revisar avisos oficiales del destino.
- Para descubrir destinos y eventos cada mes, usa el agente `trip-scout`.

## Ejemplo

**Pedido:** «4 días en Petén para 2 adultos desde la capital, en febrero, con Q 6,000.»
**Entrega (resumen):** Día 1 vuelo o bus a Flores y paseo por la isla; día 2 Tikal con amanecer;
día 3 Yaxhá al atardecer; día 4 regreso. Precios de entrada y transporte con enlace y fecha de
revisión, hospedaje como rango en Flores, clima seco de febrero con fuente y presupuesto de unos
Q 5,400 con Q 600 de imprevistos. Horario del amanecer en Tikal marcado «Por confirmar» con el
parque.
