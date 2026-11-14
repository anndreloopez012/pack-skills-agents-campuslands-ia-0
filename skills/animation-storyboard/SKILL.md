---
name: animation-storyboard
description: "Divide tu video animado en escenas con tiempo de inicio y fin, texto en pantalla, el movimiento de cada elemento, la transición y el audio, listo para pedírselo a HyperFrames o Remotion. Pídela con «arma el guion animado», «divide mi video en escenas con tiempos» o «qué se mueve en cada momento del video»."
---

# Guion animado

Convierte un brief en una lista de escenas con tiempos exactos y lo que se mueve en cada una. Es lo
que se le entrega a la IA que anima (HyperFrames o Remotion) para que no tenga que adivinar.

## Cuándo usarla

- Ya tienes el brief (`video-brief`) y vas a hacer un video de texto animado, cifras o gráficos.
- Quieres revisar con tu jefe o cliente qué dice y qué se mueve en cada segundo antes de animar.
- Para video generado con IA por tomas de unos 8 segundos, usa mejor `storyboard`.

## Qué necesito de ti

- El brief o, al menos: objetivo, duración, formato y llamado a la acción.
- Los textos exactos que deben salir (precios, fechas, nombres) y el material: logo, fotos, música.
- La guía de estilo si existe (`motion-style-guide`); si no, uso un estilo sobrio y lo marco.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Reparto la duración: gancho en los primeros 2 o 3 segundos, desarrollo y cierre con llamado a
   la acción que dure al menos 2 segundos en pantalla.
2. Divido en escenas de 2 a 6 segundos; una idea por escena.
3. Para cada escena defino: tiempo de inicio y fin, lo que se ve, el texto exacto en pantalla,
   cómo entra, se mueve y sale cada elemento, la transición a la siguiente y el audio.
4. Reviso el tiempo de lectura: cada texto debe quedar en pantalla lo suficiente para leerlo
   (regla práctica: 1 segundo por cada 3 o 4 palabras, nunca menos de 1,5 segundos).
5. Sumo los tiempos y compruebo que coincidan con la duración total, sin huecos ni encimes.
6. Escribo el pedido para la herramienta en lenguaje llano (no código), con el formato, la
   duración, el estilo y la tabla de escenas.
7. Si una escena necesita imagen o video realista que no existe, la marco para generarla con
   `google-flow-veo-director` antes de animar.

## Lo que te entrego

```text
GUION ANIMADO - <proyecto>   Formato: 9:16 (1080x1920)   Duración: 20 s   Estilo: <guía o supuesto>
Música: <pista y licencia>   Voz: <sí/no, ver voiceover-script>   Subtítulos: <sí/no>
```

| Esc. | Inicio | Fin | Lo que se ve | Texto en pantalla | Movimiento de cada elemento | Transición | Audio |
|---|---|---|---|---|---|---|---|
| 1 | 0:00 | 0:03 | Fondo crema, taza al centro | «¿Ya probaste café de altura?» | Taza entra desde abajo; texto aparece palabra por palabra | Corte | Música entra suave |
| 2 | 0:03 | 0:08 | ... | ... | ... | Barrido a la izquierda | ... |

Después de la tabla:

- **Lista de recursos:** archivo, dónde está y si tiene permiso o licencia.
- **Pedido para la herramienta:** un párrafo que la persona pega en Claude Code o Codex, por
  ejemplo: «Usa /hyperframes. Crea un video 9:16 de 20 segundos con este guion animado y esta guía de
  estilo. Muéstrame la vista previa antes de exportar».
- **Pendientes:** textos por confirmar, cifras sin fuente, imágenes por generar.

## Reglas

- Una idea por escena; el texto en pantalla, máximo 8 a 10 palabras por escena.
- Tiempos en formato m:ss, continuos: el fin de una escena es el inicio de la siguiente.
- Describe el movimiento con palabras simples (entra, sube, crece, se desvanece, se desliza) y deja
  los detalles técnicos a la herramienta y a su documentación.
- Textos importantes lejos de los bordes: respeta las zonas seguras de `video-qa-checklist`.
- Precios, fechas y cifras exactamente como la persona los dio; nunca redondees ni inventes.
- La persona aprueba el guion antes de animar; nada se exporta ni se publica sin su visto bueno.

## Ejemplo

**Pedido:** «Video de 15 segundos para anunciar mi curso de contabilidad básica en Xela, empieza el
3 de febrero, Q350».
**Entrega (resumen):** 4 escenas. 0:00-0:03 pregunta «¿Tu negocio lleva sus cuentas en un
cuaderno?» que aparece palabra por palabra; 0:03-0:07 tres íconos (libro, calculadora, factura) que
suben en cascada con el texto «Aprende a llevar tus libros»; 0:07-0:11 fecha y precio que crecen al
centro: «Inicia 3 de febrero - Q350»; 0:11-0:15 logo y «Inscríbete por WhatsApp» fijo 4 segundos.
Pedido listo para `/hyperframes` y pendiente: confirmar número de WhatsApp.
