---
name: image-prompt-director
description: "Escribe prompts para crear imágenes en Gemini o ChatGPT: sujeto, estilo, encuadre, luz, colores y texto legible entre comillas, con versiones en 1:1, 4:5, 9:16 y 16:9 para cada red. Úsala con «crea la portada de mi carrusel», «quiero una imagen para mi anuncio», «dame el prompt para la imagen»."
---

# Imágenes con IA

Te da prompts listos para pegar y conseguir imágenes que sirven para tu negocio o tu clase, sin
probar veinte veces. Para quien hace publicaciones, presentaciones o material sin diseñador.

## Cuándo usarla

- «Crea la portada de mi carrusel sobre cómo ahorrar en quetzales.»
- «Necesito una imagen para anunciar la promoción de inscripciones.»
- «Quiero ilustrar mi presentación con una imagen de una finca de café.»

## Qué necesito de ti

- Para qué es la imagen y dónde se publica.
- Qué debe verse y qué texto debe llevar (si lleva).
- Colores o estilo de tu marca, si los tienes, o una imagen de referencia.
- Qué IA usas: Gemini o ChatGPT (Claude no crea imágenes: te dejo el prompt para pegar en ellas).
- Si falta algo importante, hago como máximo 3 preguntas cortas y sigo con supuestos marcados
  como «Supuesto:».

## Cómo trabajo

1. Defino el formato según el uso:
   - **1:1** publicación cuadrada (Instagram, Facebook).
   - **4:5** carrusel y publicación vertical de Instagram (la que más ocupa la pantalla).
   - **9:16** historias, Reels, TikTok, estados de WhatsApp.
   - **16:9** YouTube, presentaciones, portada de LinkedIn o web.
2. Armo el prompt en este orden: tipo de imagen (fotografía, ilustración plana, 3D) → sujeto y
   acción → escenario → encuadre (plano general, medio, detalle) → luz → paleta de colores →
   estilo → espacio libre para texto → formato.
3. El texto que debe aparecer va **entre comillas y corto** (máximo 6 a 8 palabras), con dónde
   va y qué tamaño: `titular grande arriba: "Ahorra Q 500 al mes"`. Los textos largos se agregan
   después en Canva o PowerPoint.
4. Escribo el prompt en español (Gemini y ChatGPT lo entienden bien) y agrego una versión en
   inglés si buscas más precisión.
5. Para una serie (carrusel), fijo un bloque de estilo que se repite igual en todas las imágenes.
6. Si se repite un personaje, uso una ficha fija (la misma de `google-flow-veo-director` si hay
   video).
7. Doy 2 variantes y qué cambiar si sale mal (texto torcido, manos raras, colores distintos).

## Lo que te entrego

```
IMAGEN: [para qué] — IA: [Gemini / ChatGPT]
Bloque de estilo (repetir en la serie): ...

PROMPT PRINCIPAL — [formato]
Crea una [tipo] de [sujeto y acción] en [escenario]. Encuadre: ... Luz: ... Colores: ...
Estilo: ... Texto en la imagen, legible y sin errores: [posición] "..." 
Deja espacio libre en [zona]. Formato [proporción].

OTRAS VERSIONES
| Formato | Uso | Ajuste al prompt |
|---|---|---|
| 1:1 | | |
| 4:5 | | |
| 9:16 | | |
| 16:9 | | |

VARIANTE B: ...
SI SALE MAL: [problema → qué cambiar]
TEXTO PARA AGREGAR AL EDITAR: ...
```

## Reglas

- Revisa siempre la ortografía del texto que genera la IA: si sale mal, pide solo la imagen sin
  texto y agrégalo tú al editar.
- No pido imágenes de personas reales identificables, logos ni personajes con derechos de autor.
  Tu logo se coloca después, no se genera.
- No imito el estilo de un artista vivo por su nombre.
- Montos en quetzales con «Q» y cifras verificadas antes de publicar.
- La IA prepara; tú decides qué se publica.
- Para el texto que acompaña la publicación, usa `human-voice`.

## Ejemplo

**Pedido:** «Crea la portada de mi carrusel sobre cómo ahorrar en quetzales. Uso Gemini. Mi marca
usa azul marino y amarillo.»
**Entrega (resumen):** Formato 4:5. Prompt: ilustración plana de una mujer joven en un mercado de
Totonicapán guardando billetes de quetzal en un sobre, plano medio, luz de mañana, paleta azul
marino, amarillo y blanco, estilo editorial limpio, titular grande arriba: "Ahorra Q 500 al mes",
espacio libre abajo para el logo. Bloque de estilo para las 6 láminas, versión 9:16 para historia,
y aviso: si el billete sale deformado, pedir «sobre con monedas» en su lugar.
