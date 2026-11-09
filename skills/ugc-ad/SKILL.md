---
name: ugc-ad
description: "Guion y prompts de un anuncio corto estilo testimonio, como si un cliente real hablara de tu producto a la cámara del celular, con aviso claro de que es contenido creado con IA. Pídela con «haz un anuncio tipo testimonio», «quiero un video de cliente feliz para mi producto» o «anuncio UGC para Instagram»."
---

# Anuncio tipo testimonio

Prepara un anuncio de 16 a 32 segundos con la estética de un video grabado por un cliente: cámara en
mano, luz natural y lenguaje sencillo. Para emprendimientos y pequeños negocios.

## Cuándo usarla

- Quieres un anuncio que se sienta cercano, no de agencia.
- Tienes un producto o servicio concreto y sabes qué problema resuelve.
- Vas a generar el video en Gemini o Flow (Veo), o vas a grabarlo con una persona real usando el guion.

## Qué necesito de ti

- Producto o servicio, precio en quetzales y dónde se compra.
- El problema que resuelve y la razón principal por la que tus clientes lo eligen.
- Opiniones reales de clientes (mensajes, reseñas) si las tienes: de ahí sale el lenguaje.
- Si será persona generada con IA o una persona real que lo grabará.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Elijo la estructura: problema, descubrimiento, prueba, resultado y llamado a la acción.
2. Escribo el diálogo como habla la gente de verdad en Guatemala: frases cortas, sin tecnicismos ni
   superlativos («el mejor del mundo»). Reviso con `human-voice`.
3. Divido en tomas de unos 8 segundos (Veo) con una o dos frases por toma.
4. Creo la ficha del vocero con `character-consistency` y repito su bloque fijo en cada prompt.
5. Escribo los prompts con estética de celular: cámara en mano a la altura del pecho, selfie o apoyado
   en una mesa, luz de ventana, fondo de casa o negocio real, sonido ambiente.
6. Agrego el texto en pantalla y el aviso de contenido creado con IA para poner al editar.
7. Si la persona prefiere una persona real, entrego el mismo guion como guía de grabación con
   indicaciones de encuadre.

## Lo que te entrego

```text
ANUNCIO: <producto>  Duración: 24 s  Formato: 9:16  Red: Instagram / TikTok / Facebook
Promesa (una frase verificable): ...
Vocero: <bloque fijo del personaje>

TOMA 1 (0-8 s) Problema
Diálogo: "..."
Prompt para Veo/Flow: ...
Texto en pantalla: ...

TOMA 2 (8-16 s) Descubrimiento y prueba
...

TOMA 3 (16-24 s) Resultado y llamado a la acción
...

AVISO EN PANTALLA: "Video creado con IA" (o la etiqueta que pida la red)
COPY PARA LA PUBLICACIÓN: ...
VERSIÓN PARA GRABAR CON PERSONA REAL: encuadre, luz, frases
```

## Reglas

- Nunca presentes a una persona generada con IA como cliente real: el aviso de IA va en el video o en
  el texto, y se activa la etiqueta de contenido con IA si la red la ofrece.
- No inventes testimonios ni cifras: la promesa debe ser algo que el producto cumple. Sin «cura»,
  «garantizado» ni afirmaciones de salud o dinero que no puedas probar.
- No uses la cara ni la voz de personas reales sin su permiso por escrito.
- Respeta las políticas de anuncios de cada red; revisa la vigente antes de pautar.
- Nada se publica ni se pauta sin aprobación de la persona.

## Ejemplo

**Pedido:** «Anuncio para mi crema de manos de café hecha en Huehuetenango, Q45».
**Entrega (resumen):** 24 s en 3 tomas. Vocera: Lucía, 34 años, maestra, suéter mostaza, cocina de
casa. Toma 1: se mira las manos resecas después de lavar trastes: «Con el frío de diciembre se me
rajan las manos». Toma 2: abre el frasco de vidrio ámbar, lo huele: «Me la recomendó mi cuñada, huele
a café de verdad». Toma 3: sonríe con la taza en la mano: «Q45 y me dura el mes. Pedila por WhatsApp».
Aviso «Video creado con IA» y versión para grabarla con una clienta real.
