---
name: cover-designer
description: "Prompts para portadas de reels, miniaturas de YouTube y la primera diapositiva del carrusel, con encuadre, contraste y espacio para el título, en Gemini o ChatGPT. Pídela con «hazme la portada de este reel», «miniatura para mi video de YouTube» o «la primera diapositiva no llama la atención»."
---

# Portadas y miniaturas

Diseña la imagen que decide si alguien abre tu video o tu carrusel. Prepara el prompt de imagen y el
texto corto que va encima.

## Cuándo usarla

- Vas a publicar un reel y quieres una portada que se vea bien en tu cuadrícula.
- Necesitas la miniatura de un video de YouTube.
- La primera diapositiva de tu carrusel no está deteniendo a nadie.

## Qué necesito de ti

- De qué trata la pieza y la promesa en una frase.
- Red y formato: portada de reel (9:16, con la zona central visible en la cuadrícula), miniatura de
  YouTube (16:9) o portada de carrusel (4:5 en Instagram, 1:1 o 4:5 en LinkedIn).
- Colores y tipografía de tu marca si los tienes (ver `brand-voice`).
- Si sales tú: una foto tuya. Si es un personaje, su ficha (`character-consistency`).
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Escribo 3 títulos de 2 a 5 palabras que prometan algo concreto, sin repetir el título del video.
2. Elijo una sola idea visual: una cara con emoción clara, un objeto en primer plano o un antes y
   después. Nada de collages con cinco cosas.
3. Escribo el prompt de imagen con `image-prompt-director`: sujeto, encuadre, fondo limpio, luz,
   contraste alto y espacio libre donde irá el texto (por ejemplo, «tercio superior despejado»).
4. Recomiendo poner el texto en Canva o en el editor, no dentro de la imagen generada; si la persona
   quiere probar el texto dentro, lo pido corto y entre comillas, y aviso que puede salir deformado.
5. Doy la versión para cada formato pedido y cómo comprobar que se lee en tamaño pequeño.

## Lo que te entrego

```text
PIEZA: <tema>   RED Y FORMATO: <...>
TÍTULOS PROPUESTOS (elige uno)
1. ...   2. ...   3. ...

PROMPT DE IMAGEN (Gemini o ChatGPT)
Sujeto: ...
Encuadre: ... (primer plano, mirada a cámara, sujeto a la derecha)
Fondo: ... (liso, color de marca, desenfocado)
Luz y contraste: ...
Espacio para texto: ...
Estilo: ...
Formato: 9:16 / 16:9 / 4:5
Evitar: texto en la imagen, logos ajenos, manos deformes

TEXTO ENCIMA (al editar): fuente, tamaño relativo, color, posición
PRUEBA: reducir al 20 % y comprobar que el título se lee en 1 segundo
```

## Reglas

- Máximo 5 palabras de título en portada; el detalle va en el texto de la publicación.
- La portada no promete lo que el video no da.
- Contraste alto entre texto y fondo; nada de texto amarillo sobre fondo claro.
- En portadas de reel, lo importante va al centro: Instagram recorta la vista en la cuadrícula.
- Miniaturas con Higgsfield (`higgsfield-youtube-thumbnail`) son opcionales y consumen créditos.
- No uses caras de personas reales ni marcas ajenas sin permiso. Nada se publica sin aprobación.

## Ejemplo

**Pedido:** «Miniatura para mi video "Cómo pedir tu NIT en línea"».
**Entrega (resumen):** títulos: «Tu NIT en 10 minutos», «Sin hacer cola», «NIT desde el celular».
Prompt: mujer guatemalteca de 28 años sonriendo con un celular en la mano, plano medio a la derecha,
fondo azul liso, luz de estudio suave, tercio izquierdo despejado, 16:9. Texto al editar: «Sin hacer
cola» en blanco, grueso, a la izquierda. Nota: verificar el trámite vigente en portal.sat.gob.gt
antes de publicar el video.
