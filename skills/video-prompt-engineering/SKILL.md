---
name: video-prompt-engineering
description: "Escribe un prompt de video profesional y lo adapta a Veo y Flow, Kling, Runway o Sora, con sujeto, acción, cámara, luz y audio; también diagnostica y arregla el prompt que no salió. Pídela con «pasa este prompt a Kling», «mi video salió raro, arréglalo» o «hazme el prompt de esta escena»."
---

# Prompts para cualquier plataforma

Convierte una idea de escena en un prompt de video completo y lo traduce al estilo de cada herramienta.
Sirve a quien crea videos cortos para su negocio, su clase o su marca personal.

## Cuándo usarla

- Tienes una idea de escena y no sabes cómo describirla para la IA.
- Un prompt funcionó en Veo y quieres probarlo en Kling, Runway o Sora (o al revés).
- El video salió con caras deformes, movimiento raro, texto ilegible o algo que no pediste.

## Qué necesito de ti

- La escena en tus palabras: quién, qué hace, dónde y qué debe sentir quien la ve.
- La herramienta que vas a usar: Gemini o Flow (Veo), Kling, Runway, Sora u otra.
- Formato final: vertical 9:16 (reel, TikTok, estado) u horizontal 16:9 (YouTube, presentación).
- Si ya generaste algo que no salió: el prompt que usaste y qué falló.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Separo la idea en los 9 bloques del prompt: sujeto, acción, escenario, cámara y lente, movimiento de
   cámara, luz, estilo, audio y diálogo, duración.
2. Reviso que haya una sola acción principal por toma. Si hay más, propongo partirla en varias tomas
   (Veo genera clips de unos 8 segundos; con Flow se encadenan; para eso usa `storyboard` y
   `video-continuity`).
3. Escribo el prompt base en español, en prosa ordenada, con detalles concretos y visibles (colores,
   materiales, hora del día), no adjetivos vagos como «increíble» o «épico».
4. Lo adapto a la herramienta pedida con la tabla de abajo, sin inventar parámetros técnicos: si no
   estoy seguro de que una opción exista en esa versión, digo «revisa en la herramienta si tiene X».
5. Agrego una lista corta de lo que no debe aparecer (texto deformado, manos extra, logos ajenos).
6. Si es una corrección, nombro la causa probable y cambio solo lo necesario.

### Cómo cambia el prompt por herramienta

| Herramienta | Qué le funciona mejor |
|---|---|
| Veo en Gemini o Flow | Prosa descriptiva con cámara, luz y audio. Acepta diálogo entre comillas y sonido ambiente. Flow permite seguir una toma desde el último cuadro y usar imágenes como ingredientes. |
| Kling | Descripción clara del sujeto y un movimiento a la vez; parte bien de una imagen inicial. El sonido conviene agregarlo después si la versión no lo genera. |
| Runway | Prompt corto y directo, centrado en el movimiento de cámara y de sujeto; rinde mejor con imagen de referencia. |
| Sora | Escenas narrativas con detalle del ambiente; describe la toma como lo haría un guionista. |
| ChatGPT o Claude | No sirven para generar el video en este flujo: preparan y corrigen los prompts que luego pegas en Gemini, Flow u otra herramienta. ChatGPT sí genera imágenes de referencia. |

Las opciones de cada herramienta cambian seguido. Antes de prometer duración, resolución o audio,
revisa lo que muestra tu cuenta hoy.

## Lo que te entrego

```text
PROMPT BASE (español)
Sujeto: ...
Acción: ... (una sola acción principal)
Escenario: ... (lugar, hora, clima, detalles)
Cámara y lente: ... (plano medio, primer plano, gran angular, 35 mm, 85 mm...)
Movimiento de cámara: ... (fija, travelling lento hacia adelante, paneo, cámara en mano)
Luz: ... (luz de ventana suave, atardecer dorado, neón, luz de mediodía dura)
Estilo: ... (documental realista, comercial limpio, cine cálido, animación 3D)
Audio y diálogo: ... (ambiente, música, frase exacta entre comillas y quién la dice)
Duración y formato: ~8 s, 9:16
Evitar: ...

VERSIÓN PARA <herramienta>
<prompt listo para copiar>

SI NO SALE BIEN
- Problema probable -> qué cambiar
```

## Reglas

- Una acción principal por toma; si son tres cosas, son tres tomas.
- El diálogo va entre comillas, corto (una frase cabe en 8 segundos) y con quién lo dice.
- No pidas texto largo dentro del video: la IA lo deforma. El texto se pone después al editar.
- No uses caras ni voces de personas reales sin su permiso, ni marcas ajenas.
- Si hay una persona que debe repetirse en varios videos, usa `character-consistency`.
- No prometas resultados: cada generación varía; propón 2 o 3 intentos y elegir el mejor.

## Ejemplo

**Pedido:** «Quiero un video de mi cafetería en Antigua, que se vea el café y la gente tranquila».
**Entrega (resumen):** prompt base: barista guatemalteca de 30 años, delantal café, sirve un capuchino
con arte latte en una barra de madera; escenario: cafetería en casa colonial de Antigua Guatemala, arcos
de piedra, el Volcán de Agua al fondo por la ventana, 7 de la mañana; cámara: primer plano a la taza,
lente 50 mm; movimiento: travelling lento hacia la taza; luz: sol bajo entrando de lado; estilo:
comercial cálido realista; audio: máquina de espresso, murmullo suave, sin música; 8 s, 9:16. Versión
para Veo en Flow, versión para Kling partiendo de una foto real del local y tres arreglos si la espuma
sale deformada.
