---
name: voiceover-script
description: "Escribe el texto de la voz en off con sus tiempos y prepara los subtítulos listos para pegar (formato SRT), cuidando que cada frase quepa en su toma. Pídela con «escribe la locución de mi video», «hazme los subtítulos» o «cuánto texto cabe en 30 segundos»."
---

# Locución y subtítulos

Prepara lo que se dice y lo que se lee en un video corto, con tiempos que calzan con las tomas. Para
reels, video-clases, anuncios y presentaciones.

## Cuándo usarla

- Tienes las tomas y necesitas la voz en off que las acompañe.
- Quieres subtítulos para que el video se entienda sin sonido.
- Vas a grabar tu voz, usar la voz del video de Veo o una voz sintética.

## Qué necesito de ti

- El guion gráfico o la lista de tomas con su duración (si no, primero `storyboard`).
- El mensaje principal y el público.
- Quién pone la voz: tú, otra persona, la voz generada por Veo o una voz sintética.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Calculo cuánto texto cabe: en español, a ritmo natural, unas 2 a 2.5 palabras por segundo. Para
   8 segundos, de 16 a 20 palabras; dejo medio segundo de aire al inicio y al final.
2. Escribo la locución en frases cortas, para el oído: una idea por frase, verbos activos, números
   redondos («casi la mitad» en vez de «48.7 %»).
3. Marco pausas con «/» y la palabra que se enfatiza en MAYÚSCULAS, solo en la versión de grabación.
4. Leo cada frase contra su toma: si no cabe, recorto el texto, nunca acelero la voz.
5. Armo los subtítulos: máximo 2 líneas, unos 35 a 42 caracteres por línea, entre 1 y 6 segundos en
   pantalla, cortes donde la frase respira.
6. Entrego el archivo SRT y la versión limpia para leer o para pegar en la herramienta de voz.

## Lo que te entrego

| Toma | Inicio | Fin | Lo que se ve | Locución | Palabras |
|---|---|---|---|---|---|
| 1 | 00:00 | 00:08 | ... | ... | 18 |

```text
VERSIÓN PARA GRABAR
Toma 1: Cada mañana / más de cien familias / compran AQUÍ su pan.

SUBTÍTULOS (SRT)
1
00:00:00,500 --> 00:00:03,800
Cada mañana, más de cien familias

2
00:00:03,800 --> 00:00:07,500
compran aquí su pan.
```

Al final, las indicaciones de voz: tono, ritmo, energía y cómo pronunciar nombres propios (por
ejemplo «Xela», «Q'eqchi'»).

## Reglas

- Si el diálogo lo genera Veo dentro del clip, la frase va en el prompt entre comillas y debe caber
  en la toma; la locución externa se usa cuando hay narrador.
- Voces sintéticas: con ElevenLabs (`text-to-speech`) requiere cuenta. Nunca clones la voz de otra
  persona sin su permiso por escrito.
- Subtítulos fieles a lo que se dice; corrige ortografía y tildes.
- Sin frases de relleno ni muletillas de IA; revisa con `human-voice`.
- Nada se publica sin la aprobación de la persona.

## Ejemplo

**Pedido:** «Locución de 24 segundos para el video de mi panadería en Cobán».
**Entrega (resumen):** 3 tomas de 8 s con 17, 18 y 16 palabras: «Desde las cuatro de la mañana, en
Cobán, ya huele a pan dulce.» / «Champurradas, pirujos y cubiertos, hechos a mano como los hacía mi
abuela.» / «Pasá antes de las siete y llevátelos calientitos.» Versión con pausas, SRT de 6 bloques e
indicaciones: voz cálida, ritmo tranquilo, sonrisa en la última frase.
