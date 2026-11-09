---
name: google-flow-veo-director
description: "Convierte tu idea en prompts de video para Veo y Flow de Google: sujeto, acción, escenario, cámara, luz, estilo, audio y diálogo, en clips de unos 8 segundos que se encadenan en una historia con el mismo personaje. Úsala con «haz un video de mi negocio», «quiero un video de 16 segundos para Instagram», «dame el prompt para Veo»."
---

# Director de Veo y Flow

Te ayuda a pasar de una idea suelta a prompts de video que funcionan, aunque nunca hayas hecho un
video con IA. Para emprendedoras, docentes y equipos de comunicación que quieren videos cortos.

## Cuándo usarla

- «Haz un video de 16 segundos de mi café en Antigua para Instagram.»
- «Quiero un video corto del primer día de clases para los papás.»
- «Dame el prompt para Veo de un anuncio de mi tienda de llantas.»

## Qué necesito de ti

- La idea: qué quieres mostrar y qué debe sentir o hacer quien lo vea.
- Dónde se publica (Reels, TikTok, YouTube, WhatsApp) y duración total.
- Qué IA tienes: Gemini (con Veo), Flow, ChatGPT o Claude.
- Si hay una persona o mascota que debe repetirse, sus rasgos o una foto de referencia.
- Si falta algo importante, hago como máximo 3 preguntas cortas y sigo con supuestos marcados
  como «Supuesto:» (por defecto: vertical 9:16, estilo realista, español de Guatemala).

## Cómo trabajo

1. Escribo la historia en una frase y la divido en tomas de unos 8 segundos (16 s = 2 tomas,
   24 s = 3). Cada toma muestra una sola acción principal.
2. Creo la **ficha del personaje**: una descripción fija (edad aproximada, ropa, cabello, rasgo
   distintivo) que copio igual en cada toma. Nunca la cambio entre tomas.
3. Para cada toma armo el prompt con 9 partes, en este orden:
   1. **Sujeto** (la ficha fija)  2. **Acción** (un verbo claro)  3. **Escenario** (lugar, hora)
   4. **Cámara y lente** (plano general, medio o cercano; 35 mm, 50 mm)  5. **Movimiento**
   (fija, acercamiento lento, paneo, cámara en mano)  6. **Luz** (mañana suave, atardecer,
   interior cálido)  7. **Estilo** (realista, documental, animación 3D)  8. **Audio** (ambiente,
   música, efectos)  9. **Diálogo** entre comillas, corto, máximo unas 20 palabras por toma.
4. Escribo el prompt en inglés para mejor resultado y el diálogo en español entre comillas, con
   una traducción al español del prompt para que entiendas qué pediste.
5. Para encadenar en **Flow**: la toma 1 se genera normal; la toma 2 empieza donde terminó la 1
   (usa «Extender» o el último fotograma como imagen inicial) y repite la ficha del personaje,
   la luz y el estilo. Indico el corte entre tomas (por mirada, por movimiento o por objeto).
6. Adapto la entrega a tu IA:
   - **Gemini (Veo):** un prompt por toma; generas cada clip y los unes en CapCut o similar.
   - **Flow:** prompts encadenados con las instrucciones de extender y de imagen inicial.
   - **ChatGPT:** si tu plan genera video, ajusto el prompt; si no, te lo dejo listo para Gemini
     o Flow.
   - **Claude:** Claude no genera video; te dejo todo listo para pegar en Gemini o Flow.
7. Reviso que nada pida logos complejos, texto largo en pantalla ni rostros de personas reales.

## Lo que te entrego

```
VIDEO: [título] — [duración] s — [9:16 / 16:9] — para [red]
Historia en una frase: ...
FICHA DEL PERSONAJE (copiar igual en cada toma): ...

TOMA 1 (0–8 s)
Prompt (inglés): [sujeto], [acción], [escenario], [plano y lente], [movimiento], [luz], [estilo].
Audio: ... Dialogue: "..."
Qué pediste (español): ...
Cómo se genera: [Gemini / Flow, pasos]

TOMA 2 (8–16 s)
Empieza desde: último fotograma de la toma 1 / Extender
Prompt (inglés): ...
Corte: ...

TEXTO Y MÚSICA PARA EDITAR APARTE: [títulos, logo, subtítulos]
SI SALE MAL: [qué cambiar en el prompt]
```

## Reglas

- La IA prepara los prompts; tú generas, revisas y decides qué se publica.
- Los límites de duración, cantidad de videos y funciones dependen del plan de cada herramienta
  y cambian seguido: revisa lo que tu cuenta permite hoy.
- Nada de personas reales sin su permiso, menores identificables, marcas ajenas ni música con
  derechos. El logo y los textos largos se agregan al editar, no en el prompt.
- Sin emojis en guiones ni prompts.
- Para que el personaje se mantenga en imagen fija (portada, miniatura), usa
  `image-prompt-director` con la misma ficha.
- Para el texto de la publicación, usa `human-voice` sobre el borrador.

## Ejemplo

**Pedido:** «Haz un video de 16 segundos de mi café en Antigua para Instagram. Tengo Gemini.»
**Entrega (resumen):** Ficha: barista de unos 30 años, delantal verde oliva, cabello recogido,
pulsera de hilo rojo. Toma 1: plano general de la calle empedrada con el Arco de Santa Catalina
al fondo a las 7:00, la barista abre la puerta de madera, acercamiento lento, luz dorada, ambiente
de calle y campanas lejanas. Toma 2: plano cercano de sus manos sirviendo un café de olla, vapor,
dice «Aquí el día empieza despacio». Texto final «Abrimos a las 7:00» para agregar al editar.
