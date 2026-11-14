---
name: video-edit-plan
description: "A partir de tu grabación o tus tomas arma el plan de edición: orden de cortes con marca de tiempo, cuánto dura cada parte, qué se quita y dónde van textos, música y subtítulos. Pídela con «ayúdame a editar este video», «qué le corto a mi grabación» o «arma el plan de cortes»."
---

# Plan de edición

Convierte una grabación larga o varias tomas sueltas en un plan de cortes que cualquiera puede
seguir: tú en CapCut, otra persona, o la IA con HyperFrames o FFmpeg.

## Cuándo usarla

- Grabaste un video (clase, testimonio, receta, recorrido) y no sabes qué dejar y qué quitar.
- Tienes varias tomas y quieres ordenarlas en una historia corta.
- Vas a sacar un reel corto de un video largo.

## Qué necesito de ti

- La grabación o la lista de archivos, con su duración.
- La transcripción con marcas de tiempo (si no la tienes, ver `subtitles-pro`) o tus notas de lo
  que pasa en cada minuto.
- Duración final, red donde se publica y objetivo del video.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Leo la transcripción o las notas y marco las partes con contenido útil, las repetidas, los
   silencios largos, las muletillas y los errores.
2. Elijo el gancho: la frase o imagen más fuerte va al inicio, aunque se haya grabado al final.
3. Ordeno los cortes con marca de tiempo de origen (en la grabación) y de destino (en el video
   final), y compruebo que la suma dé la duración pedida.
4. Marco lo que se quita y por qué.
5. Indico dónde van textos en pantalla, música, efectos de sonido, subtítulos y el cierre con logo.
6. Indico cómo se hará: editor visual (CapCut, Canva, DaVinci Resolve), o con IA en Claude Code o
   Codex usando el kit HyperFrames (punto de entrada `/hyperframes`; necesita Node.js y FFmpeg) o
   FFmpeg directo para cortes simples.
7. Si la grabación es de 16:9 y se publica en 9:16, indico cómo se reencuadra cada parte (centro,
   seguir a la persona) y aviso si algo importante queda fuera.

## Lo que te entrego

```text
PLAN DE EDICIÓN - <proyecto>
Archivo(s) de origen: <nombre, duración>   Duración final: <seg>   Formato: <9:16 / 16:9>
Objetivo: ...   Gancho elegido: «<frase>» (origen 03:42)
```

| # | Archivo | Origen inicio | Origen fin | Final inicio | Final fin | Qué pasa | Texto en pantalla | Audio |
|---|---|---|---|---|---|---|---|---|
| 1 | toma2.mp4 | 03:42 | 03:46 | 0:00 | 0:04 | «Así se tuesta…» | «Café de altura» | Voz + música baja |
| 2 | toma1.mp4 | 00:15 | 00:24 | 0:04 | 0:13 | ... | - | Voz |

**Lo que se quita:**

| Origen | Motivo |
|---|---|
| 00:00-00:15 | Preparación antes de grabar |
| 01:10-01:32 | Se repite la idea del corte 2 |

Al final: música (pista, licencia, volumen), subtítulos (sí/no, estilo), reencuadre, herramienta
recomendada y «Pendientes para el visto bueno».

## Reglas

- Las marcas de tiempo salen de la grabación o de la transcripción; si no las tengo, lo digo y
  pido que la persona las confirme. Nunca invento lo que dice el video.
- No cambies el sentido de lo que dice una persona al cortar; en testimonios, no unas frases para
  que diga algo que no dijo.
- Primero el gancho, después el contexto; el llamado a la acción al final.
- Si aparecen personas, clientes o datos sensibles, recuerda permisos y `data-shield`.
- El plan se aprueba antes de editar; exportar y publicar requieren visto bueno.

## Ejemplo

**Pedido:** «Grabé 6 minutos de mi clase de Excel para una academia en Escuintla; quiero un reel de
30 segundos para invitar al curso».
**Entrega (resumen):** Gancho en 02:10 («Con esta fórmula ya no sumas a mano»). 5 cortes: 02:10-
02:14, 02:40-02:52 (demostración), 04:05-04:11 (resultado), 05:20-05:26 (invitación), más 2 s de
cierre con logo. Se quita la introducción (00:00-00:45) y la pausa por el proyector (03:00-03:30).
Reencuadre a 9:16 siguiendo la pantalla. Subtítulos con `subtitles-pro` y texto «Inscripciones
abiertas» en el cierre.
