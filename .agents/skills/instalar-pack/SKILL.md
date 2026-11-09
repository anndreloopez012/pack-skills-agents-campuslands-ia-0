---
name: instalar-pack
description: "Instala el pack de skills y agentes del taller IA desde 0 de Campuslands. Úsala cuando la persona pegue «Instala el pack github.com/anndreloopez012/pack-skills-agents-campuslands-ia-0», el nombre pack-skills-agents-campuslands-ia-0, o pida instalar, actualizar, ampliar o quitar skills y agentes del pack."
---

# Instalar el pack IA desde 0

Guía la instalación como una conversación corta con alguien que está aprendiendo IA desde cero:
lo general se instala solo y después la persona elige lo de su área, sabiendo antes qué hace cada
herramienta. Habla en español sencillo, sin jerga, y di qué vas a hacer antes de cada paso que
cambie el equipo.

## 1. Tener el repositorio

- Si ya estás dentro del repositorio (existe `catalogo.json` y `scripts/instalar.py`), sigue.
- Si no, clónalo en la carpeta de documentos de la persona (pregúntale si prefiere otra):
  `git clone https://github.com/anndreloopez012/pack-skills-agents-campuslands-ia-0.git`
  Si ya existe, actualízalo con `git -C <carpeta> pull --ff-only`.
- Requisitos: `git` y Python 3.9 o superior (`python3 --version`; en Windows, `py --version`). Si
  falta alguno, explica qué es y pide permiso antes de instalarlo.

## 2. Instalar lo general, sin preguntar

```bash
python3 scripts/instalar.py
```

Instala las skills y los agentes generales y los kits de la comunidad marcados como generales
(Superpowers, Agent Skills, Diagram Design y documentos de oficina), solo en las IA que existen en
el equipo (Claude Code, Codex o Antigravity). Cuéntale el resultado en dos o tres líneas, por
ejemplo: «Listo, ya tienes 14 skills y 6 agentes generales. Puedes pedirme "ordena mi bandeja" o
"resume este documento en una página"».

Si el instalador dice que no encontró ninguna IA de escritorio, la persona usa la IA en la web:
corre `python3 scripts/instalar.py --web <carpeta>` y explícale el `LEEME.md` que queda ahí (subir
los .zip en Claude.ai o pegar las instrucciones en un Proyecto, GPT o Gem).

## 3. Preguntar por sus áreas

Corre `python3 scripts/instalar.py --lista` y muéstrale **solo las áreas**, numeradas, con su
nombre y para quién son (la línea «ÁREA …»). Pregunta: «¿En qué áreas trabajas o te interesan?
Puedes elegir varias o ninguna».

Si la persona pegó un pedido armado en la landing (trae líneas «Áreas:», «Skills especializadas:»,
«Agentes especializados:» o «De la comunidad:»), no vuelvas a preguntar: confirma la lista en una
línea y pasa al paso 5.

## 4. Mostrar lo de cada área para que elija

Por cada área elegida, muestra sus skills, sus agentes y sus kits de la comunidad con el nombre en
español y lo que hace (una línea cada uno). En los agentes di cada cuánto trabajan. En los kits de
la comunidad di el autor, la licencia y lo que requieren (cuenta propia, Python o un programa de
IA en la computadora). Pregunta cuáles quiere: todas, ninguna o algunas por número.

## 5. Instalar lo elegido

```bash
python3 scripts/instalar.py --sin-general --elegir <slugs separados por comas> --terceros <ids>
```

Para instalar un área completa: `--sin-general --areas <id>`. Los agentes instalan solos las skills
del pack que necesitan. Los kits de la comunidad se descargan desde su repositorio original, sin
modificarlos.

## 6. Cerrar

- Resume qué quedó, en qué IA, y cómo usar dos o tres herramientas con ejemplos de pedidos.
- Explica cómo programar un agente: con las tareas programadas de su IA (en la app de Claude,
  «Tareas programadas»; en ChatGPT, «Tareas»; en Gemini, «Acciones programadas»), o pidiéndolo
  cuando toque: «corre el agente weekly-review».
- Recuérdale abrir una sesión nueva para que la IA tome lo instalado.

## Reglas

- **Nunca pises lo ajeno.** Si el instalador reporta un conflicto (ya existe algo con ese nombre
  que no es del pack), no lo borres: explícale a la persona qué es y decidan juntos.
- No instales nada que la persona no eligió (salvo lo general) ni cambies la configuración de sus
  IA sin preguntar.
- Nunca pidas ni escribas contraseñas, tokens ni claves. Los kits que requieren cuenta (Higgsfield,
  ElevenLabs) los conecta la persona en su propio navegador.
- Actualizar: `git pull` en el repositorio (con copias, volver a correr el instalador).
- Ver qué hay: `python3 scripts/instalar.py --estado`. Quitar todo lo del pack:
  `python3 scripts/instalar.py --quitar` (solo borra lo que instaló el pack).
