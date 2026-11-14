---
name: subtitles-pro
description: "Transcribe, corrige y parte tus subtítulos en líneas cortas con buen ritmo de lectura, para videos verticales y horizontales, y te entrega el archivo SRT. Pídela con «hazme los subtítulos», «corrige esta transcripción» o «pásalo a SRT»."
---

# Subtítulos que se leen

La mayoría ve los videos sin sonido. Esta skill deja subtítulos correctos, cortos y a buen ritmo,
listos para cargar en la red o quemar en el video.

## Cuándo usarla

- Tienes un video con voz y necesitas subtítulos.
- La transcripción automática salió con errores o con líneas larguísimas.
- Necesitas el archivo SRT para YouTube, LinkedIn, un editor o HyperFrames.

## Qué necesito de ti

- La transcripción con marcas de tiempo, o el audio o video para transcribir con una herramienta
  que ya tengas: subtítulos automáticos de CapCut o YouTube, transcripción de Word, Whisper si lo
  tienes instalado, o la transcripción de tu IA si acepta audio.
- Nombres propios, marcas y términos que se dicen (para escribirlos bien).
- Formato: vertical 9:16 u horizontal 16:9.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Si no hay transcripción, indico cómo sacarla con las herramientas que la persona tiene. No
   transcribo de memoria ni invento lo que se dice.
2. Corrijo ortografía, tildes, nombres propios y cifras; quito muletillas solo si no cambia el
   sentido.
3. Parto en bloques de máximo 2 líneas: unos 32 caracteres por línea en vertical y unos 42 en
   horizontal (de referencia).
4. Reviso el ritmo: lectura cómoda de 15 a 17 caracteres por segundo; cada bloque entre 1 y 6
   segundos en pantalla. Si un bloque va muy rápido, lo divido o lo resumo y lo marco.
5. Corto donde se respira: después de comas y puntos, nunca entre artículo y sustantivo, nunca
   partiendo un nombre propio, una cifra, una fecha ni un precio («Q1,250» va completo).
6. Ajusto los tiempos para que cada bloque entre con la voz y no se encime con el siguiente.
7. Entrego el SRT y una tabla de revisión con los bloques dudosos.

## Lo que te entrego

Primero, tabla de revisión:

| # | Inicio | Fin | Texto | Car./seg. | Revisar |
|---|---|---|---|---|---|
| 1 | 00:00:00,000 | 00:00:02,400 | Bienvenidos a Café La Ceiba, | 12 | - |
| 4 | 00:00:08,100 | 00:00:09,300 | más de 20 años tostando en Antigua | 28 | Muy rápido: dividir |

Después, el archivo SRT (se guarda como `subtitulos.srt`):

```text
1
00:00:00,000 --> 00:00:02,400
Bienvenidos a Café La Ceiba,

2
00:00:02,400 --> 00:00:05,600
donde tostamos café de altura
en Antigua Guatemala.
```

Al final: estilo sugerido si se queman en el video (tipografía de `motion-style-guide`, fondo o
contorno para contraste, posición dentro de la zona segura de `video-qa-checklist`).

## Reglas

- Máximo 2 líneas por bloque; la línea de arriba, si se puede, más corta que la de abajo.
- No partas nombres propios, cifras, fechas, precios ni siglas (SAT, IGSS, INTECAP).
- Subtítulos fieles a lo que se dice; si resumes por ritmo, márcalo para revisión.
- Siempre hay revisión humana: la persona escucha el video completo con los subtítulos antes de
  publicar. Lo dudoso o inaudible se marca como «[inaudible]», nunca se adivina.
- Formato de tiempo SRT: horas:minutos:segundos,milisegundos, con coma.
- Los límites de caracteres son de referencia; cada red puede mostrarlos distinto.

## Ejemplo

**Pedido:** «Te pego la transcripción automática de mi video de 40 segundos sobre cómo emitir una
factura electrónica FEL; está toda pegada».
**Entrega (resumen):** 14 bloques corregidos («fel» pasa a «FEL», «sat» a «SAT», «Q1250» a
«Q1,250»), ninguno de más de 32 caracteres por línea, tres bloques marcados como rápidos (19 a 21
car./seg.) con propuesta de división, archivo `subtitulos.srt` y recordatorio: escucha el video
completo con los subtítulos antes de publicar.
