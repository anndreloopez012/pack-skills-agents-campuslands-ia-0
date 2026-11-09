---
name: video-continuity
description: "Encadena clips de unos 8 segundos en Veo y Flow sin que cambien la ropa, la luz, el lugar o la posición entre una toma y otra, con una hoja de continuidad y el prompt de cada toma. Pídela con «une estos clips sin que se note», «en la segunda toma cambió todo» o «quiero un video de 24 segundos seguido»."
---

# Continuidad entre clips

Hace que varias tomas cortas se vean como un solo video. Útil cuando la herramienta genera clips de
unos 8 segundos y tu historia dura más.

## Cuándo usarla

- Vas a unir 2 o más clips de Veo en Flow (o en un editor) y deben parecer la misma escena.
- En la toma siguiente cambió la ropa, la hora del día, el fondo o el lado por donde entra la persona.
- Quieres extender una toma desde su último cuadro.

## Qué necesito de ti

- El guion gráfico o la lista de tomas (si no lo tienes, primero `storyboard`).
- La ficha del personaje si hay uno (`character-consistency`).
- Los prompts ya usados y, si existe, una descripción de cómo terminó la última toma generada.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con «Supuesto:».

## Cómo trabajo

1. Armo la hoja de continuidad: lo que debe quedar igual en todas las tomas (personaje, vestuario,
   lugar, hora, clima, luz, paleta, estilo, lente) en bloques de texto fijos.
2. Para cada corte defino el «cuadro de salida» de una toma y el «cuadro de entrada» de la siguiente:
   dónde está la persona, hacia dónde mira, qué tiene en la mano, de qué lado entra la luz.
3. Respeto la regla de los 180 grados: si en la toma 1 la persona mira a la derecha de cámara, en la
   toma 2 sigue a la derecha salvo que la cámara cruce a la vista del público.
4. Escribo cada prompt con los bloques fijos copiados igual y solo cambio acción, plano y movimiento.
5. Indico el método de enlace por toma: «extender desde el último cuadro» en Flow cuando la acción
   sigue; corte directo cuando cambia el plano; imagen inicial cuando hay que volver a un encuadre.
6. Dejo la lista de revisión para comparar cada clip generado antes de aceptarlo.

## Lo que te entrego

```text
HOJA DE CONTINUIDAD
Personaje (bloque fijo): "..."
Vestuario (bloque fijo): "..."
Lugar (bloque fijo): "..."
Hora y luz (bloque fijo): "... la luz entra desde la izquierda de cámara"
Estilo y lente (bloque fijo): "..."
Objetos que viajan entre tomas: taza en mano derecha, bolsa al hombro izquierdo
```

| Corte | Sale la toma anterior con... | Entra la siguiente con... | Enlace | Riesgo |
|---|---|---|---|---|
| 1 -> 2 | ... | ... | extender / corte / imagen inicial | ... |

Después, el prompt completo de cada toma y esta lista de revisión: misma ropa y accesorios, mismo lado
de la luz, mismo fondo, misma mano para el objeto, mirada hacia el mismo lado, mismo color de imagen.

## Reglas

- Los bloques fijos se copian literalmente; cualquier sinónimo puede cambiar el resultado.
- No cambies dos cosas a la vez entre tomas: si cambia el plano, que no cambie la luz.
- Lo que no se puede arreglar al generar se arregla al editar: corrección de color, recorte o un
  plano de detalle para disimular el corte.
- Las funciones de cada herramienta cambian; confirma en tu cuenta que existe «extender» o
  «último cuadro» antes de planear todo con ellas.
- Nada se publica sin la aprobación de la persona.

## Ejemplo

**Pedido:** «Mi video de la tienda de artesanías de Chichicastenango tiene 3 clips; en el segundo la
vendedora aparece con otro güipil».
**Entrega (resumen):** hoja de continuidad con el bloque fijo del güipil (rojo con figuras de aves
blancas y amarillas, faja azul), mercado de día nublado con luz suave, la vendedora a la izquierda del
encuadre mirando a la derecha. Tabla de cortes: 1 a 2 extender desde el último cuadro porque sigue
doblando un tejido; 2 a 3 corte a primer plano de las manos para disimular el cambio. Prompts
reescritos de las tomas 2 y 3 y lista de revisión.
