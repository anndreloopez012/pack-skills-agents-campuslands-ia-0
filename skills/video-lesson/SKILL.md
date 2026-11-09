---
name: video-lesson
description: "Estructura y guion para grabar una video-clase corta (de 3 a 10 minutos) que se entienda sola, con objetivo, lo que dices, lo que se ve en pantalla, ejemplos y una actividad final. Pídela con «guion para grabar mi clase», «quiero hacer un video de este tema para mis alumnos» o «cápsula de capacitación de 5 minutos»."
---

# Guion de video-clase

Prepara una clase grabada que el estudiante puede ver sin el docente al lado. Para clases a distancia,
cápsulas de capacitación y tutoriales.

## Cuándo usarla

- Vas a grabar una clase para quienes faltaron o para repaso.
- Das capacitación y quieres cápsulas cortas que se vean a cualquier hora.
- Quieres un tutorial paso a paso (por ejemplo, cómo usar una herramienta).

## Qué necesito de ti

- Tema, público y el único objetivo de aprendizaje del video.
- Duración deseada (lo recomendado: de 3 a 8 minutos por video).
- Cómo grabarás: tu cara a cámara, pantalla de la computadora con voz, diapositivas con voz o mezcla.
- El material base (libro, apuntes, presentación).
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Defino un objetivo de aprendizaje por video. Si el tema tiene tres objetivos, son tres videos.
2. Estructura: gancho (problema o pregunta, 15 a 30 s), qué aprenderás, explicación por pasos, ejemplo
   resuelto, error frecuente, resumen y actividad para hacer después.
3. Escribo el guion hablado: frases cortas, unas 130 a 150 palabras por minuto, tono de conversación.
4. Para cada bloque indico lo que se ve: cara, pizarra, diapositiva, pantalla, objeto.
5. Marco dónde hacer pausas para que el estudiante piense («pausá el video y resolvé...»).
6. Preparo la actividad de cierre (con `quiz-game` si conviene), el texto del enlace y los subtítulos
   (`voiceover-script`).
7. Si quiere tomas de apoyo generadas con IA, propongo prompts con `video-prompt-engineering`.

## Lo que te entrego

```text
VIDEO-CLASE: <título>   Duración: 6 min   Público: ...
Objetivo: al terminar, el estudiante podrá ...
Requisitos previos: ...
Materiales para grabar: ...
```

| Tiempo | Bloque | Lo que digo | Lo que se ve | Pausa o pregunta |
|---|---|---|---|---|
| 0:00-0:25 | Gancho | ... | cara a cámara | - |
| 0:25-0:45 | Qué aprenderás | ... | diapositiva con 3 puntos | - |
| 0:45-4:00 | Explicación | ... | pizarra / pantalla | «pausá y...» |
| 4:00-5:15 | Ejemplo resuelto | ... | ... | ... |
| 5:15-6:00 | Resumen y actividad | ... | ... | ... |

```text
ACTIVIDAD PARA DESPUÉS: ...
TEXTO PARA COMPARTIR EL ENLACE: ...
CONSEJOS DE GRABACIÓN: luz de frente, micrófono cerca o de solapa, fondo ordenado, celular horizontal
para clases (16:9) y vertical solo para cápsulas en redes
```

## Reglas

- Un video, un objetivo; mejor tres videos de 5 minutos que uno de 15.
- El video se entiende solo: nada de «como vimos en clase» sin explicarlo.
- Contenido fiel al material base; datos legales o científicos con fuente y fecha.
- Si aparecen estudiantes o pantallas con datos personales, pide permiso o difumina.
- El docente revisa el guion antes de grabar y decide qué publica y dónde.

## Ejemplo

**Pedido:** «Video de 5 minutos para mis alumnos de 3.º básico sobre cómo calcular porcentajes».
**Entrega (resumen):** gancho: «En la tienda de la esquina, un par de tenis de Q300 tiene 20 % de
descuento. ¿Cuánto pagás?». Explicación en 3 pasos con pizarra, ejemplo resuelto con el recibo de luz,
error frecuente (restar 20 quetzales en vez de 20 %), pausa para que resuelvan un ejercicio, resumen y
5 ejercicios para el cuaderno.
