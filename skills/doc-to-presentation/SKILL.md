---
name: doc-to-presentation
description: "Convierte un PDF, un libro, un informe o tus notas en una presentación con estructura clara, una idea por diapositiva, ejemplos y notas para quien presenta. Úsala con «haz una presentación de este capítulo», «pasa este informe a diapositivas», «necesito exponer esto el lunes»."
---

# Del documento a la presentación

Transforma texto largo en una exposición que se entiende y se recuerda. Para docentes, gerentes,
consultores y cualquiera que deba presentar ante un grupo.

## Cuándo usarla

- «Haz una presentación de 10 diapositivas de este capítulo.»
- «Paso el informe trimestral a diapositivas para la junta.»
- «Tengo estas notas para una charla a padres de familia.»

## Qué necesito de ti

- El documento o tus notas.
- Público (quiénes son y qué saben del tema), duración y número aproximado de diapositivas.
- Qué deben hacer o recordar al terminar.
- Herramienta final: PowerPoint, Google Slides, Canva o solo el guion.
- Si falta algo importante, hago como máximo 3 preguntas cortas y sigo con supuestos marcados
  como «Supuesto:» (por defecto: 1 diapositiva por cada 2 minutos).

## Cómo trabajo

1. Leo todo el documento y escribo el mensaje central en una frase.
2. Armo el hilo: problema o pregunta, 3 a 5 ideas principales, ejemplo, cierre con acción.
3. Una idea por diapositiva. El título es una frase que dice la conclusión («Las ventas de
   Xela crecieron 18 %»), no un tema suelto («Ventas»).
4. Máximo 3 viñetas cortas por diapositiva; el detalle va en las notas del presentador.
5. Propongo un apoyo visual por diapositiva (gráfico, foto, diagrama, tabla) y, si hace falta,
   el prompt para crearlo con `image-prompt-director`.
6. Agrego ejemplos cercanos al público (casos de Guatemala, cifras en quetzales).
7. Cierro con una diapositiva de acción o preguntas, no con «Gracias».

## Lo que te entrego

```
PRESENTACIÓN: [título]
Público: ...   Duración: ... min   Diapositivas: ...
Mensaje central: ...

| # | Título (frase con la idea) | Contenido en pantalla (máx. 3 viñetas) | Visual sugerido | Notas para quien presenta | Min |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

PREGUNTAS PROBABLES DEL PÚBLICO Y RESPUESTA CORTA: ...
FUENTES: [documento, páginas usadas]
```

Si tu IA tiene la skill `pptx` instalada, ofrezco generar el archivo de PowerPoint con este
contenido; en Google Slides o Canva, copias cada fila en su diapositiva.

## Reglas

- Todo lo que pongo sale del documento; si agrego un ejemplo o dato externo, lo marco.
- Nada de párrafos en pantalla: si hay que leerlo, va a las notas.
- Cifras con su fuente y fecha en la diapositiva o en las notas.
- Si el documento tiene datos de clientes, alumnos o personal, usa antes `data-shield`.
- Si es un libro protegido, resumo y explico con mis palabras; no copio páginas textuales.
- Para un público que debe decidir, primero haz un `one-pager` y la presentación sale de ahí.

## Ejemplo

**Pedido:** «Haz una presentación de 10 diapositivas del capítulo 3 del manual de servicio al
cliente, para capacitar a cajeros nuevos de una agencia en Escuintla, 20 minutos.»
**Entrega (resumen):** Mensaje central: «Cada cliente se va con su problema resuelto o con una
fecha». Diez diapositivas: la regla de los 10 segundos para saludar, cómo escuchar sin
interrumpir, tres frases para un cliente molesto, qué hacer si el sistema falla, un caso de
reclamo por cobro doble de Q 250, y cierre con un ejercicio en parejas. Cada una con notas y un
visual sugerido.
