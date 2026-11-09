# Pack IA desde 0

Skills y agentes de IA para el trabajo de todos los días, del taller **IA desde 0** de Campuslands
Guatemala. Lo general se instala solo; lo de tu área lo eliges tú, sabiendo antes qué hace cada
herramienta.

**Catálogo visual:** https://anndreloopez012.github.io/pack-skills-agents-campuslands-ia-0/

## Instalar

Pega esto en tu IA (Claude Code, Codex o Antigravity):

```text
Instala el pack github.com/anndreloopez012/pack-skills-agents-campuslands-ia-0
```

La IA clona el repositorio, instala lo general, te pregunta en qué áreas trabajas y te muestra lo de
cada área con lo que hace, para que elijas. Las instrucciones para la IA están en
[INSTALAR.md](INSTALAR.md) y en la skill [`instalar-pack`](.agents/skills/instalar-pack/SKILL.md).

¿Usas Claude, ChatGPT o Gemini solo en la web? Abre la carpeta [skills](skills/), copia el texto de
la skill que quieras y pégalo como instrucciones de un Proyecto, un GPT o un Gem.

## Skill o agente

- **Skill:** una receta que tu IA sigue cuando se la pides, siempre con el mismo formato. Ejemplo:
  le pegas 15 correos y le dices «ordena mi bandeja».
- **Agente:** un encargado que trabaja solo cada día, semana o mes y te deja el resultado listo. Lo
  que sale hacia afuera siempre lo apruebas tú.

## Qué trae

| Parte | Contenido |
|---|---|
| General (se instala solo) | 14 skills y 6 agentes: bandeja, procesos, investigación con fuentes, resumen de una página, reuniones, redacción, presentaciones, Excel, semana, prompts, voz humana, protección de datos, Veo y Flow, imágenes con IA |
| Especializados (eliges) | 11 áreas: contabilidad, ventas, marketing, contenido con IA, docencia, datos, gestión pública, infraestructura, dirección, emprendimiento y desarrollo personal |
| Comunidad | 11 kits de otros autores con su crédito y su licencia ([CREDITOS.md](CREDITOS.md)) |

El detalle de cada pieza está en [catalogo.json](catalogo.json) y en el catálogo visual.

## Reglas de todas las herramientas

- **Tú apruebas:** nada se envía, publica ni paga sin tu visto bueno.
- **Con fuentes:** todo dato investigado trae de dónde salió y su fecha.
- **Datos cuidados:** nombres, DPI, NIT, cuentas y datos de clientes se reemplazan por etiquetas
  antes de trabajarlos. Si tu empresa tiene reglas sobre IA, esas mandan.
- **En tu idioma:** español de Guatemala, con quetzales, leyes y fechas locales.

## Para quien mantiene el pack

```bash
npm run generar     # versiones de los agentes para cada IA y la landing (docs/index.html)
npm run verificar   # catálogo, archivos, agentes, landing y prueba del instalador
```

Formato de skills y agentes: [guias/FORMATO.md](guias/FORMATO.md). Cambios: [CHANGELOG.md](CHANGELOG.md).

Licencia MIT para el contenido propio del pack. Los kits de la comunidad conservan la suya.
