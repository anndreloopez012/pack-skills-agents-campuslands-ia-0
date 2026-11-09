# Formato de las skills y los agentes del pack

Guía para quien escribe o corrige una skill o un agente de este repositorio. Todo va en español de
Guatemala, en lenguaje llano: lo usan personas que están aprendiendo IA desde cero (contadores,
vendedores, docentes, gerentes, emprendedores). Solo los nombres propios (slugs, productos) quedan en
inglés.

La fuente de la verdad es `catalogo.json`: el `slug`, el nombre y la descripción corta de cada pieza
salen de ahí. Si cambias el alcance de una pieza, cámbialo también en el catálogo.

## Skill: `skills/<slug>/SKILL.md`

```markdown
---
name: <slug>
description: "<Qué hace y cuándo usarla, en una o dos frases. Incluye frases con las que la persona la pediría: «ordena mi bandeja», «resume esto». Sin comillas dobles ni barras invertidas dentro; usa «»>"
---

# <Nombre en español>

<Una o dos líneas: qué resuelve y para quién.>

## Cuándo usarla

- <situaciones o frases que la activan>

## Qué necesito de ti

- <insumos>. Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos
  marcados como «Supuesto:».

## Cómo trabajo

1. <pasos concretos, en orden, que la IA sigue siempre>

## Lo que te entrego

<El formato exacto de la salida, con una plantilla en bloque de código o tabla.>

## Reglas

- <reglas del oficio y de cuidado>

## Ejemplo

**Pedido:** «...»
**Entrega (resumen):** ...
```

Reglas para escribirla:

- Entre 50 y 140 líneas. Concreta y accionable: la IA debe poder seguirla sin adivinar.
- La plantilla de «Lo que te entrego» es obligatoria y específica del oficio (columnas reales, campos
  reales), nunca genérica.
- Contexto de Guatemala cuando aplique: quetzales (Q), SAT, IGSS, IRTRA, INTECAP, MINFIN, SEGEPLAN,
  Guatecompras, Código de Trabajo, días hábiles.
- Toda cifra legal (tasas, porcentajes, plazos) va con la indicación de verificar que siga vigente en
  la fuente oficial (por ejemplo, `portal.sat.gob.gt`, `igssgt.org`) y con la fecha en que se revisó.
  Nunca inventes una ley, un artículo o un formulario.
- Datos personales: antes de trabajar documentos con nombres, DPI, NIT, cuentas o salarios, propone
  usar la skill `data-shield`. Nunca pidas contraseñas, tokens ni datos de tarjetas.
- La IA prepara; la persona decide. Nada se envía, publica, firma ni paga sin su aprobación.
- Sin emojis, sin relleno («en el mundo actual…»), sin promesas de resultados.
- Si la skill se apoya en otra del pack, nómbrala con su slug entre comillas invertidas.

## Agente: `agentes/<slug>.md`

Es la fuente única; `python3 scripts/agentes.py generar` escribe las versiones para Claude Code,
Codex y Antigravity en `agentes/claude/`, `agentes/codex/` y `agentes/antigravity/`. No edites esas
carpetas a mano.

```markdown
---
name: <slug>
description: "<Qué hace, cada cuánto y qué entrega. Sin comillas dobles ni barras invertidas; usa «»>"
frecuencia: <Diario | Semanal | Quincenal | Mensual | Al iniciar un encargo>
access: read-only
tools: [read, search, glob, list, web_fetch, web_search]
skills: [<slugs del pack que usa>]
---

# <Nombre en español>

<Una o dos líneas: qué encargo cumple.>

## Cuándo corre

- <frecuencia y disparador; cómo se lo pide la persona si no está programado>

## Lo que revisa

- <fuentes: lo que la persona le pega, sus archivos, la web con fuentes>

## Pasos

1. <pasos concretos>

## Lo que entrega

<Plantilla exacta del resultado.>

## Reglas

- Prepara y propone; nunca envía, publica, paga ni borra nada sin aprobación explícita.
- <reglas del oficio>

## Tus skills

| Skill | Para qué la usa |
|---|---|
| `<slug>` | <uso> |

## Programarlo

Para que corra solo, usa la función de tareas programadas de tu IA (en la app de Claude, «Tareas
programadas»; en ChatGPT, «Tareas»; en Gemini, «Acciones programadas»). Si tu IA no la tiene,
pídeselo cuando toque: «corre el agente <slug>».
```

Reglas para escribirlo:

- `access: read-only` salvo que el agente deba escribir archivos en la carpeta de trabajo; entonces
  `access: write` y agrega `write` y `edit` a `tools`.
- Toda skill de `skills:` debe aparecer en la tabla «Tus skills» con su slug entre comillas invertidas
  (lo revisa `scripts/verificar.py`).
- Las instrucciones no pueden llevar tres comillas simples seguidas (cierran el texto de Codex).
- Entre 40 y 110 líneas.
