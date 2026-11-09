# pack-skills-agents-campuslands-ia-0

Pack de skills y agentes de IA del taller **IA desde 0** de Campuslands Guatemala. Lo leen Codex y
Antigravity (Claude Code lo toma desde `CLAUDE.md`).

## Si te piden instalarlo

Sigue la skill `instalar-pack` (`.agents/skills/instalar-pack/SKILL.md`, con espejo en
`.claude/skills/instalar-pack/`). En corto:

1. Instala lo general sin preguntar: `python3 scripts/instalar.py`.
2. Pregunta en qué áreas trabaja la persona (`python3 scripts/instalar.py --lista`).
3. Muestra lo de esas áreas con lo que hace cada pieza y deja que elija.
4. Instala lo elegido: `python3 scripts/instalar.py --sin-general --elegir <slugs> --terceros <ids>`.

Nunca pises lo ajeno: si el instalador reporta un conflicto, decide con la persona.

## Si te piden cambiar el pack

- `catalogo.json` es la fuente de la verdad: slug, nombre, descripción, áreas y kits de la comunidad.
- Cada skill vive en `skills/<slug>/SKILL.md` y cada agente en `agentes/<slug>.md`, con el formato de
  `guias/FORMATO.md`.
- Las versiones de los agentes para cada IA (`agentes/claude`, `agentes/codex`,
  `agentes/antigravity`) y la landing (`docs/index.html`) se generan: `npm run generar`. No las
  edites a mano; la landing se edita en `guias/landing.plantilla.html`.
- Los kits de la comunidad no se copian al repositorio: el instalador los baja de su repositorio
  original. Al agregar uno, verifica autor, licencia y la ruta real de cada `SKILL.md`, y anótalo en
  `CREDITOS.md`.
- Antes de subir cualquier cambio: `npm run verificar` (o `python3 scripts/verificar.py`) en verde.
- Todo el texto va en español; solo los nombres propios quedan en inglés.
- Flujo de git: una rama por cambio (`feat/…` o `fix/…`), después `merge --no-ff` en `dev` y en
  `main`, y se empujan ambas. Los commits no llevan coautorías ni menciones a herramientas de IA.
