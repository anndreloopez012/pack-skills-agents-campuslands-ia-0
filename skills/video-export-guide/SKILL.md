---
name: video-export-guide
description: "Te dice qué resolución, relación de aspecto, tasa de cuadros, duración y peso usar para exportar tu video para Instagram, TikTok, YouTube, LinkedIn y WhatsApp, con valores de referencia. Pídela con «en qué tamaño exporto», «qué formato uso para reels» o «mi video se ve borroso en Instagram»."
---

# Formatos y exportación

Evita que el video salga cortado, borroso o demasiado pesado. Da los valores de referencia para
cada red y el pedido de exportación para tu editor o tu herramienta de IA.

## Cuándo usarla

- Vas a empezar un video y quieres elegir bien el formato desde el inicio.
- Vas a exportar y no sabes qué opciones marcar.
- El video se ve borroso, con barras negras o cortado al subirlo.

## Qué necesito de ti

- En qué red o redes se publica y en qué lugar (reel, historia, feed, video largo, estado).
- Duración aproximada y si es grabación, animación o video generado con IA.
- Con qué se exporta: CapCut, Canva, DaVinci Resolve, HyperFrames, Remotion u otro.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Elijo la relación de aspecto según el lugar donde se verá; si va a varias redes, propongo
   producir en el formato principal y adaptar los demás.
2. Doy resolución, tasa de cuadros, duración recomendada y peso orientativo.
3. Recomiendo 30 fps para redes y pantallas; 24 fps si se busca aspecto de cine. Nunca mezclo
   tasas: si la grabación es de 30 fps, exporto a 30 fps.
4. Indico formato de archivo: MP4 con video H.264 y audio AAC es el más compatible (de referencia).
5. Si se exporta con HyperFrames (`npx hyperframes`, kit `hyperframes-cli`) o Remotion
   (`remotion-render`), remito a su documentación para las opciones exactas y solo indico los
   valores de resolución, duración y cuadros que hay que pedir.
6. Aviso cuánto puede tardar: exportar animaciones largas o en alta resolución puede tomar varios
   minutos y usar mucho la computadora.

## Lo que te entrego

Tabla de referencia (revisa las especificaciones vigentes de cada red; cambian seguido):

| Red y lugar | Relación | Resolución | fps | Duración sugerida | Nota |
|---|---|---|---|---|---|
| Instagram reels e historias | 9:16 | 1080x1920 | 30 | 15-60 s | Deja libres arriba y abajo |
| Instagram feed | 4:5 | 1080x1350 | 30 | 15-60 s | Ocupa más pantalla que el 1:1 |
| TikTok | 9:16 | 1080x1920 | 30 | 15-60 s | Interfaz a la derecha y abajo |
| YouTube video | 16:9 | 1920x1080 | 24 o 30 | Lo que pida el tema | Miniatura aparte |
| YouTube Shorts | 9:16 | 1080x1920 | 30 | Corto | Revisa el límite vigente |
| LinkedIn feed | 1:1 o 4:5 | 1080x1080 / 1080x1350 | 30 | 30-90 s | Subtítulos casi obligatorios |
| LinkedIn horizontal | 16:9 | 1920x1080 | 30 | 30-90 s | Para presentaciones |
| WhatsApp estados | 9:16 | 1080x1920 | 30 | Corto | Se comprime mucho; texto grande |
| WhatsApp mensaje | 9:16 o 16:9 | 1080 de lado corto | 30 | Corto | Archivo liviano |

Pedido de exportación para el proyecto:

```text
EXPORTACIÓN - <proyecto>                    Valores de referencia, revisados el <fecha>
Red y lugar: Instagram reels
Relación: 9:16   Resolución: 1080x1920   fps: 30   Duración: 0:20
Archivo: MP4 (H.264 + AAC)   Nombre: <marca>-<tema>-9x16-v1.mp4
Peso orientativo: <rango>; si pasa el límite de la red, bajar calidad, no resolución
Versiones extra: 4:5 para feed (reencuadrar, no estirar)
Herramienta: <editor / HyperFrames / Remotion> - opciones exactas en su documentación
Tiempo de exportación estimado: <minutos> - confirmar antes de exportar
```

## Reglas

- Todo valor es de referencia: revisa las especificaciones vigentes de cada red y anota la fecha.
- Nunca estires un video para cambiar el formato; reencuadra o agrega fondo.
- Exporta en la misma tasa de cuadros que la grabación.
- No afirmes opciones de HyperFrames, Remotion ni FFmpeg que no estén en su documentación.
- Exportar y publicar se hacen con aprobación de la persona.

## Ejemplo

**Pedido:** «Hice un video horizontal de mi tienda de Xela y lo quiero en reels, feed y estados».
**Entrega (resumen):** Formato principal 9:16 1080x1920 a 30 fps para reels y estados; versión 4:5
1080x1350 para el feed, reencuadrando cada toma al centro del producto. Aviso: dos tomas tienen el
letrero en el borde y se pierde en 9:16; proponer acercar o agregar el nombre como texto. MP4,
nombres de archivo por versión y recordatorio de revisar los límites vigentes de cada red.
