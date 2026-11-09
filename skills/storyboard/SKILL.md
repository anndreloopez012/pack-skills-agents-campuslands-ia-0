---
name: storyboard
description: "Divide tu idea de video en escenas de unos 8 segundos con lo que se ve, lo que se dice, el texto en pantalla y el prompt de cada toma, listo para Veo y Flow. Pídela con «arma el guion gráfico de mi video», «divide esta idea en tomas» o «quiero un video de 30 segundos, ¿cómo lo armo?»."
---

# Guion gráfico

Ordena una idea en tomas cortas antes de gastar créditos generando video. Sirve para reels, anuncios,
videos de clase y presentaciones de producto.

## Cuándo usarla

- Tienes la idea pero no sabes cuántas tomas necesita ni qué va en cada una.
- Vas a generar varias tomas en Veo o Flow y quieres que cuenten una historia.
- Quieres revisar el video con alguien (cliente, jefe, compañera) antes de producirlo.

## Qué necesito de ti

- La idea y el objetivo: vender, enseñar, invitar a un evento, contar una historia.
- Duración total (15, 30, 60 segundos) y formato (9:16 vertical o 16:9 horizontal).
- Personajes, producto o lugar que deben aparecer; fotos de referencia si las tienes.
- Con qué IA vas a generar: Gemini o Flow (Veo), Kling, Runway, Sora. Si usas Claude, recuerda que
  Claude no genera video: te deja los prompts para pegarlos en Flow o Gemini.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Escribo la historia en tres partes: gancho (primeros 2 o 3 segundos), desarrollo y cierre con
   llamado a la acción.
2. Calculo el número de tomas: duración total entre 8 segundos, redondeando hacia arriba. Un video de
   30 segundos son 4 tomas de unos 8 segundos.
3. Para cada toma defino: lo que se ve, la acción única, el plano y el movimiento de cámara, lo que se
   oye (diálogo, ambiente, música), el texto en pantalla que se agrega al editar y la transición.
4. Escribo el prompt de cada toma con los bloques de `video-prompt-engineering` y repito literalmente
   la descripción del personaje y del lugar (ver `character-consistency` y `video-continuity`).
5. Marco cuáles tomas conviene generar desde una imagen inicial (producto, persona real con permiso) y
   cuáles desde texto.
6. Cierro con la lista de lo que hay que tener antes de generar: fotos, logo, frases aprobadas, música.

## Lo que te entrego

| Toma | Seg. | Lo que se ve | Cámara y movimiento | Audio y diálogo | Texto en pantalla | Transición |
|---|---|---|---|---|---|---|
| 1 | 0-8 | ... | ... | ... | ... | corte / sigue desde el último cuadro |

Después de la tabla, un bloque por toma:

```text
TOMA 1 (0-8 s) - Gancho
Prompt para Veo/Flow:
<prompt completo, con la ficha del personaje y del lugar copiada igual en cada toma>
Generar desde: texto / imagen de referencia (cuál)
Revisar al generar: manos, cara, logo, texto
```

Y al final: «Lista antes de generar» y «Montaje»: orden de tomas, dónde va la música, subtítulos
(ver `voiceover-script`) y dónde se edita (CapCut, Canva, Flow o `hyperframes` si tienes Claude Code,
Codex o Antigravity instalado).

## Reglas

- Una acción principal por toma; el gancho va en la primera toma, no en la tercera.
- Diálogo corto: una frase por toma de 8 segundos, unas 15 a 20 palabras como máximo.
- Logos, precios y textos largos se ponen al editar, no dentro del prompt.
- No uses la cara ni la voz de una persona real sin su permiso por escrito.
- La persona aprueba el guion gráfico antes de generar; nada se publica sin su visto bueno.

## Ejemplo

**Pedido:** «Video de 24 segundos para promocionar mis tamales de los sábados en Mixco, Q12 cada uno».
**Entrega (resumen):** 3 tomas. Toma 1 (gancho): primer plano de una hoja de maxán que se abre y sale
vapor, travelling lento, sonido de olla; texto: «Sábado de tamales». Toma 2: doña Rosa, 55 años,
delantal verde, sirve tamales en una mesa de patio con mantel típico, plano medio, luz de mañana; dice
«Colorados y negros, recién salidos». Toma 3: familia comiendo en la mesa, cámara fija; texto al
editar: «Q12 c/u. Pedidos por WhatsApp». Prompts para Veo con la ficha de doña Rosa repetida, y nota:
el precio y el número se agregan en Canva, no en el prompt.
