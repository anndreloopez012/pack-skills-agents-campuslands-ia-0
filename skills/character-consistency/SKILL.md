---
name: character-consistency
description: "Crea la ficha fija de un personaje (persona, mascota de marca o avatar) y las frases que se copian igual en cada prompt para que salga igual en todas las imágenes y videos. Pídela con «quiero que mi personaje salga siempre igual», «hazme la ficha de mi mascota» o «en cada video cambia de cara»."
---

# Mismo personaje

Evita que tu personaje cambie de cara, ropa o edad entre una imagen y otra. Sirve para series de
videos, mascotas de marca, cursos con un presentador fijo y anuncios con varias tomas.

## Cuándo usarla

- Vas a hacer más de una imagen o video con el mismo personaje.
- El personaje sale distinto en cada generación (pelo, ropa, tono de piel, edad).
- Quieres una mascota o un vocero para tu marca y necesitas su «documento de identidad».

## Qué necesito de ti

- Quién es: persona inventada, mascota, avatar ilustrado o una persona real (solo con su permiso).
- Rasgos que no pueden cambiar: edad aproximada, complexión, pelo, ropa, accesorios, voz.
- Estilo: realista, ilustración, 3D tipo animación, acuarela.
- Una foto o imagen de referencia si la tienes.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Armo la ficha fija con rasgos concretos y visibles: «pelo negro recogido en moño bajo», no
   «pelo bonito». Nada de rasgos que la IA no pueda ver (personalidad va aparte).
2. Escribo el **bloque de identidad**: un párrafo de 40 a 60 palabras que se copia literalmente, sin
   cambiar ni una palabra, al inicio de cada prompt de imagen o video.
3. Escribo el **bloque de voz** si habla: tono, ritmo y acento descritos igual en cada prompt.
4. Defino el vestuario por escena (si cambia de ropa) como bloques también fijos: «Vestuario A»,
   «Vestuario B».
5. Propongo la hoja de referencia: una imagen de frente, perfil y cuerpo entero sobre fondo neutro,
   generada en Gemini o ChatGPT, que luego se usa como imagen de referencia en Flow, Kling o Runway.
6. Dejo la lista de cosas que suelen romper la consistencia y cómo evitarlas.

## Lo que te entrego

```text
FICHA DEL PERSONAJE: <nombre>
Rol: ...            Estilo visual: ...
Edad aparente: ...  Complexión y estatura: ...
Cara: ...           Pelo: ...
Piel: ...           Rasgos distintivos: ... (lunar, lentes, cicatriz)
Vestuario A: ...    Vestuario B: ...
Voz (si habla): ...
Lo que nunca cambia: ...

BLOQUE DE IDENTIDAD (copiar igual en cada prompt)
"<párrafo fijo de 40 a 60 palabras>"

BLOQUE DE VOZ (copiar igual)
"<descripción fija de la voz>"

PROMPT PARA HOJA DE REFERENCIA
<prompt: frente, perfil y cuerpo entero, fondo gris claro, luz pareja>

ROMPE LA CONSISTENCIA -> CÓMO EVITARLO
- Cambiar una palabra del bloque -> copiarlo y pegarlo, no reescribirlo
- ...
```

## Reglas

- El bloque de identidad se copia literalmente; parafrasearlo es la causa número uno de que el
  personaje cambie.
- Mismo estilo visual en toda la serie: no mezcles realista con caricatura.
- Si la herramienta acepta imagen de referencia o «ingredientes» (como Flow), úsala además del texto.
- Con Higgsfield se puede entrenar un personaje con `higgsfield-soul-id`; requiere cuenta y consume
  créditos, así que se usa solo si la persona lo decide.
- Personas reales: solo con permiso por escrito; nunca figuras públicas, menores ni compañeros sin
  autorización.
- Revisa cada resultado contra la ficha antes de usarlo; descarta el que se desvió.

## Ejemplo

**Pedido:** «Quiero una mascota para mi academia de inglés en Quetzaltenango que salga en todos los
reels».
**Entrega (resumen):** ficha de «Profe Quetzi», quetzal ilustrado en 3D estilo animación, plumaje verde
esmeralda brillante, pecho rojo carmesí, cola larga de dos plumas, lentes redondos de marco café,
corbatín azul marino, ojos grandes color miel. Bloque de identidad de 52 palabras para copiar igual,
bloque de voz «voz cálida de adulto joven, ritmo pausado, acento guatemalteco suave», prompt de hoja de
referencia y cinco errores comunes (cambiar «carmesí» por «rojo», olvidar los lentes, mezclar estilos).
