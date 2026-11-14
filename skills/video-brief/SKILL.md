---
name: video-brief
description: "Convierte tu idea de video en un brief claro: objetivo, público, duración, formato por red, tono, material disponible, lo que falta conseguir y con qué herramienta conviene hacerlo. Pídela con «quiero hacer un video para mi negocio», «arma el brief de este video» o «no sé por dónde empezar mi video animado»."
---

# Brief de video

Ordena la idea antes de animar, grabar o generar nada. Es la primera página de cualquier video:
evita repetir trabajo y deja claro qué se necesita y con qué herramienta se hará.

## Cuándo usarla

- Tienes una idea («quiero un video de mi café») pero no sabes cuánto debe durar ni qué poner.
- Te encargaron un video y quieres dejar por escrito lo que se acordó antes de empezar.
- Vas a pedirle a Claude Code o Codex que anime algo y necesitas darle instrucciones claras.

## Qué necesito de ti

- Qué quieres lograr: vender, enseñar, invitar, explicar un proceso, contar tu historia.
- A quién va dirigido y en qué red se publica (Instagram, TikTok, YouTube, LinkedIn, WhatsApp).
- Qué material ya tienes: logo, fotos, grabaciones, música, textos, cifras.
- Fecha de entrega y si hay presupuesto para música, voz o créditos de IA.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con supuestos marcados «Supuesto:».

## Cómo trabajo

1. Resumo la idea en una frase: «Un video de X segundos para que <público> haga <acción>».
2. Defino un solo objetivo y un solo llamado a la acción. Si hay dos, propongo dos videos.
3. Elijo duración y formato según la red (ver `video-export-guide`): vertical 9:16 para reels y
   TikTok, 4:5 para el feed, 16:9 para YouTube y presentaciones.
4. Clasifico el tipo de video y recomiendo la herramienta:
   - Texto animado, cifras, gráficos, logo, presentación en movimiento: kit HyperFrames (punto de
     entrada `/hyperframes`). Necesita Claude Code, Codex o Antigravity instalado y Node.js.
   - Lo mismo, si la persona ya programa en React: kit Remotion. Necesita Node.js y pide licencia
     comercial a empresas de más de 3 personas; revisa su licencia antes de usarlo en un negocio.
   - Escenas realistas que no se pueden grabar (personas, lugares, producto en uso): video
     generado con Veo o Flow, con `google-flow-veo-director`.
   - Grabación propia (celular, cámara, pantalla): edición con `video-edit-plan`.
   - GIF corto para chat: kit de Anthropic `slack-gif-creator`.
5. Hago el inventario de material: lo que hay, lo que falta y quién lo consigue.
6. Anoto riesgos: música con derechos, personas que salen sin permiso, cifras sin fuente.
7. Cierro con los siguientes pasos: `motion-style-guide` (si no hay estilo), `animation-storyboard`
   o `storyboard` (guion por escenas) y `voiceover-script` (si lleva voz).

## Lo que te entrego

```text
BRIEF DE VIDEO - <nombre del proyecto>          Fecha: <dd/mm/aaaa>   Estado: Borrador
En una frase: Un video de <seg> segundos para que <público> <acción>.
Objetivo único: ...
Público: <quién, edad, qué le importa, dónde lo ve>
Red y formato: <red> - <relación de aspecto> - <duración> - con/sin voz
Mensaje clave (máx. 12 palabras): ...
Llamado a la acción: ...
Tono: <cercano / formal / divertido / inspirador>   Referencias: <enlaces o descripciones>
Tipo de video: <texto animado / generado con IA / grabación editada / mixto>
Herramienta recomendada: <HyperFrames / Remotion / Veo-Flow / editor> - por qué
Requisitos para producir: <Claude Code o Codex, Node.js, FFmpeg, cuenta de Flow, etc.>
Fecha de entrega: ...
```

| Material | Lo tengo | Falta | Quién lo consigue | Para cuándo |
|---|---|---|---|---|
| Logo en PNG con fondo transparente | Sí | - | - | - |
| Música con licencia | No | Sí | ... | ... |

Al final: «Riesgos y permisos» y «Siguientes pasos» con el slug de cada skill.

## Reglas

- Un video, un objetivo, un llamado a la acción.
- No prometas alcance ni ventas; el brief describe lo que se hará, no resultados.
- Cifras, precios y datos legales salen de la persona o de una fuente citada, nunca inventados.
- Si el video muestra clientes o empleados con nombre, DPI o datos sensibles, propone `data-shield`.
- Si la persona no tiene Claude Code, Codex ni Antigravity instalado, recomienda Veo-Flow o un editor
  sencillo (CapCut, Canva) en lugar de HyperFrames o Remotion.
- La persona aprueba el brief antes de pasar al guion.

## Ejemplo

**Pedido:** «Quiero un video para Instagram de mi café en Antigua; vendemos café de altura en bolsas
de una libra a Q85».
**Entrega (resumen):** En una frase: video de 20 segundos para que turistas y chapines que visitan
Antigua pidan su bolsa por WhatsApp. Formato 9:16, sin voz, con texto en pantalla y música suave.
Tipo mixto: tomas propias del tueste (edición) más título animado y precio con HyperFrames. Falta:
música con licencia y foto de la bolsa con fondo limpio. Riesgo: un barista sale en las tomas y hay
que pedirle permiso por escrito. Siguientes pasos: `motion-style-guide` y `animation-storyboard`.
