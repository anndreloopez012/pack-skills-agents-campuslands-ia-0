# Instalar el pack (instrucciones para la IA que instala)

Sirve en macOS, Windows y Linux, con Claude Code, Codex o Antigravity. Antes de cada paso que
cambie el equipo, dile a la persona qué vas a hacer. La guía conversacional completa está en la
skill `instalar-pack` (`.agents/skills/instalar-pack/SKILL.md`).

## 1. Requisitos

- `git` y Python 3.9 o superior (`python3 --version`; en Windows, `py --version`). Si falta alguno,
  pide permiso antes de instalarlo.
- Al menos una IA de escritorio: Claude Code (`~/.claude`), Codex (`~/.codex` o `$CODEX_HOME`) o
  Antigravity (`~/.gemini`). Sin ninguna, usa el modo web (paso 5).

## 2. Clonar

```bash
git clone https://github.com/anndreloopez012/pack-skills-agents-campuslands-ia-0.git
cd pack-skills-agents-campuslands-ia-0
```

## 3. Instalar lo general

```bash
python3 scripts/instalar.py
```

| IA | Skills | Agentes |
|---|---|---|
| Claude Code | `~/.claude/skills/<slug>` | `~/.claude/agents/<slug>.md` |
| Codex | `$CODEX_HOME/skills/<slug>` | `$CODEX_HOME/agents/<slug>.toml` |
| Antigravity | `~/.gemini/config/skills/<slug>` | `~/.gemini/config/plugins/user-agents/agents/<slug>.md` |

Deja enlaces al repositorio, así un `git pull` lo actualiza todo. En Windows sin permiso para crear
enlaces, copia (también con `--copiar`); con copias hay que volver a correr el instalador después de
cada actualización. En Codex, los agentes necesitan los subagentes activos (`multi_agent = true` en
`[features]` de `~/.codex/config.toml`): pregunta antes de cambiar esa configuración.

## 4. Áreas y kits de la comunidad

```bash
python3 scripts/instalar.py --lista                                    # para mostrar las opciones
python3 scripts/instalar.py --sin-general --areas contabilidad         # un área completa
python3 scripts/instalar.py --sin-general --elegir quote-builder,fiscal-calendar --terceros linkedin-skills
```

Los kits de la comunidad se descargan con `git` desde su repositorio original a `.terceros/`
(ignorado por git) y se enlazan sin modificarlos.

## 5. Sin IA de escritorio (Claude.ai, ChatGPT o Gemini en la web)

```bash
python3 scripts/instalar.py --web ~/Desktop/pack-ia0 --areas docencia
```

Deja un `.zip` por skill para subir en Claude.ai (Configuración → Capacidades → Skills) y las
instrucciones en Markdown para pegar en un Proyecto, un GPT o un Gem, con un `LEEME.md`.

## 6. Verificar, actualizar y quitar

```bash
python3 scripts/instalar.py --estado   # qué hay del pack en cada IA
git pull --ff-only                     # actualizar
python3 scripts/instalar.py --quitar   # quita solo lo que instaló el pack
```

**Nunca pisa lo ajeno:** si ya hay algo con el mismo nombre que no es del pack, lo reporta como
conflicto y no lo toca. Míralo y decide con la persona.
