---
name: market-brief
description: "Arma un panorama de un sector o mercado con tendencias, cifras y riesgos, cada dato con su fuente y fecha. Es información para decidir, nunca una recomendación de inversión. Úsala con «dame el panorama del sector café», «qué está pasando con las tasas», «riesgos del sector construcción»."
---

# Panorama de mercado

Reúne en una o dos páginas lo que está pasando en un sector: tendencias, cifras clave, riesgos y
señales a vigilar, todo con fuentes. Para directores y gerentes que necesitan contexto antes de una
reunión, un comité o una visita a un cliente.

## Cuándo usarla

- «Mañana visito a un exportador de cardamomo, dame el panorama del sector.»
- «Qué está pasando con remesas, inflación y tipo de cambio este trimestre.»
- «Riesgos del sector construcción en Guatemala para el próximo año.»

## Qué necesito de ti

- El sector o tema, el país o región y el periodo que te interesa.
- Para qué lo usarás (reunión, comité, visita) y cuánto tiempo tienes para leerlo.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Busco en fuentes confiables y recientes, en este orden: oficiales (Banguat, INE, MINECO,
   Superintendencia de Bancos, MINFIN), gremiales (Agexport, Anacafé, Cámaras), organismos
   (CEPAL, FMI, Banco Mundial) y medios con reputación. Me apoyo en `source-researcher`.
2. Anoto cada dato con su fuente, enlace y fecha de publicación. Dato sin fuente no entra.
3. Separo lo confirmado de lo estimado o proyectado, y lo que no pude verificar.
4. Agrupo en: cifras clave, 3 a 5 tendencias, riesgos, oportunidades y señales a vigilar.
5. Cierro con preguntas útiles para la reunión, no con consejos de compra o venta.

## Lo que te entrego

```
PANORAMA: [sector] — [país] — revisado el [fecha]

Cifras clave
| Indicador | Valor | Periodo | Fuente (enlace) | Fecha de publicación |
|---|---|---|---|---|

Tendencias (3–5)
1. [tendencia] — qué significa — fuente
Riesgos
| Riesgo | Por qué importa | Señal temprana | Fuente |
|---|---|---|---|
Oportunidades: ...
Señales a vigilar en las próximas semanas: ...
Preguntas para la reunión: ...
No se pudo verificar: ...

Aviso: esto es información para decidir con fuentes. No es una recomendación de inversión ni
asesoría financiera personalizada.
```

## Reglas

- Esta skill NUNCA da recomendaciones personalizadas de inversión: no dice qué comprar, vender,
  en qué invertir ni cuánto. Si se lo piden, explica que no es asesoría financiera y sugiere
  consultar a un asesor autorizado.
- Cada cifra lleva fuente y fecha; si la fuente tiene más de 12 meses, lo marco como «dato viejo».
- No invento cifras, proyecciones ni citas. Si no hay dato, escribo «sin dato verificado».
- Las proyecciones se presentan como lo que son, con quién las hizo.
- En banca, no mezcles con este panorama datos de clientes, cartera ni tasas internas. Usa solo la
  IA que tu institución haya aprobado.
- Para recibirlo cada semana sin pedirlo, usa el agente `market-weekly`.

## Ejemplo

**Pedido:** «Panorama del sector café en Guatemala para una visita a una finca en Huehuetenango.»
**Entrega (resumen):** Cifras de exportación y precio internacional con fuente Anacafé e ICE y su
fecha; tendencias: demanda de cafés especiales, costo de mano de obra en cosecha, roya y clima;
riesgos: volatilidad de precio y lluvias; preguntas para la visita: cómo financian la cosecha y qué
porcentaje venden como especial. Aviso de que no es recomendación de inversión.
