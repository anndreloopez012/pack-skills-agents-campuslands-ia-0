#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instalador del pack de skills y agentes de Campuslands (taller IA desde 0).

Lo general se instala siempre; lo especializado y los kits de la comunidad, solo lo que la persona
elige. Actúa únicamente en las IA que existen en el equipo:

| IA | Skills | Agentes |
|---|---|---|
| Claude Code | ~/.claude/skills/<slug> | ~/.claude/agents/<slug>.md |
| Codex | $CODEX_HOME/skills/<slug> (por defecto ~/.codex) | $CODEX_HOME/agents/<slug>.toml |
| Antigravity | ~/.gemini/config/skills/<slug> | ~/.gemini/config/plugins/user-agents/agents/<slug>.md |

Deja enlaces al repositorio (un `git pull` lo actualiza todo). Los kits de la comunidad se descargan
desde su repositorio original a `.terceros/` (ignorado por git), sin modificarlos. Nunca pisa lo ajeno:
si ya existe algo con ese nombre que no es de este pack, lo reporta como conflicto.

Uso:
    python3 scripts/instalar.py --lista                    # catálogo para mostrar a la persona
    python3 scripts/instalar.py                            # solo lo general
    python3 scripts/instalar.py --areas contabilidad       # lo general y TODO lo de esas áreas
    python3 scripts/instalar.py --elegir quote-builder,fiscal-calendar --terceros linkedin-skills
    python3 scripts/instalar.py --estado                   # qué quedó instalado en cada IA
    python3 scripts/instalar.py --web ~/Desktop/pack-web   # archivos para Claude.ai, ChatGPT o Gemini en la web
    python3 scripts/instalar.py --quitar                   # quita solo lo que instaló este pack

Opciones: --sin-general, --copiar (copia en vez de enlazar), --json (salida para máquinas).
Sale con 0 si todo quedó bien y con 1 si hubo conflictos o errores.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PACK = "pack-skills-agents-campuslands-ia-0"
MARCA_CARPETA = ".instalado-por-" + PACK
PLUGIN = {"name": "user-agents", "displayName": "User Agents", "version": "1.0.0",
          "description": "Agentes del usuario para Antigravity."}
_IGNORAR = shutil.ignore_patterns(".git", "__pycache__", ".DS_Store")


# ---------------------------------------------------------------- catálogo

def cargar(raiz=RAIZ):
    return json.loads((Path(raiz) / "catalogo.json").read_text(encoding="utf-8"))


def indice(cat):
    """slug → {"tipo": skill|agente, "grupo": general|<área>, ...} de todo lo propio del pack."""
    salida = {}
    for tipo, clave in (("skill", "skills"), ("agente", "agentes")):
        for item in cat["general"][clave]:
            salida[item["slug"]] = {**item, "tipo": tipo, "grupo": "general"}
        for area in cat["areas"]:
            for item in area[clave]:
                salida[item["slug"]] = {**item, "tipo": tipo, "grupo": area["id"]}
    return salida


def dependencias_de_agente(raiz, slug):
    """Skills del pack que un agente declara en su frontmatter (se instalan con él)."""
    sys.path.insert(0, str(Path(raiz) / "scripts"))
    from agentes import leer  # noqa: E402
    fuente = Path(raiz) / "agentes" / f"{slug}.md"
    if not fuente.is_file():
        return []
    return list(leer(fuente.read_text(encoding="utf-8"))[0].get("skills") or [])


def plan(cat, raiz=RAIZ, general=True, areas=(), elegir=(), terceros=()):
    """Qué instalar: {"skills": [...], "agentes": [...], "terceros": [...], "errores": [...]}."""
    idx, errores = indice(cat), []
    ids_area = {a["id"] for a in cat["areas"]}
    ids_terceros = {t["id"]: t for t in cat["terceros"]}
    pedidos = []
    if general:
        pedidos += [s for s, i in idx.items() if i["grupo"] == "general"]
    for area in areas:
        if area not in ids_area:
            errores.append(f"no existe el área «{area}». Áreas: {', '.join(sorted(ids_area))}")
            continue
        pedidos += [s for s, i in idx.items() if i["grupo"] == area]
    for slug in elegir:
        if slug in idx:
            pedidos.append(slug)
        elif slug in ids_terceros:
            terceros = list(terceros) + [slug]
        else:
            errores.append(f"no existe «{slug}» en el catálogo (usa --lista para ver los nombres)")
    skills, agentes = [], []
    for slug in pedidos:
        destino = skills if idx[slug]["tipo"] == "skill" else agentes
        if slug not in destino:
            destino.append(slug)
    for agente in list(agentes):
        for dep in dependencias_de_agente(raiz, agente):
            if dep in idx and idx[dep]["tipo"] == "skill" and dep not in skills:
                skills.append(dep)
    elegidos_t = []
    if general:
        elegidos_t += [t["id"] for t in cat["terceros"] if t["lugar"] == "general"]
    for t in terceros:
        if t not in ids_terceros:
            errores.append(f"no existe el kit de la comunidad «{t}»")
        elif t not in elegidos_t:
            elegidos_t.append(t)
    return {"skills": skills, "agentes": agentes, "terceros": elegidos_t, "errores": errores}


# ---------------------------------------------------------------- destinos

def ias(home, codex_home=None):
    """Las IA presentes: [(nombre, carpeta_skills, carpeta_agentes, extension_agente)]."""
    home = Path(home)
    codex = Path(codex_home) if codex_home else home / ".codex"
    salida = []
    if (home / ".claude").is_dir():
        salida.append(("claude", home / ".claude" / "skills", home / ".claude" / "agents", ".md"))
    if codex.is_dir():
        salida.append(("codex", codex / "skills", codex / "agents", ".toml"))
    if (home / ".gemini").is_dir():
        salida.append(("antigravity", home / ".gemini" / "config" / "skills",
                       home / ".gemini" / "config" / "plugins" / "user-agents" / "agents", ".md"))
    return salida


def _mismo(a, b):
    return os.path.realpath(a) == os.path.realpath(b)


def _apunta_al_pack(destino, raiz):
    """Un enlace que lleva a este repositorio (o a otra copia suya del mismo nombre)."""
    real = os.path.realpath(destino)
    return real.startswith(os.path.realpath(raiz) + os.sep)


def _es_nuestro(destino, es_carpeta, raiz):
    if destino.is_symlink():
        return _apunta_al_pack(destino, raiz) or PACK in os.readlink(destino)
    if es_carpeta:
        return (destino / MARCA_CARPETA).is_file()
    try:
        return PACK in destino.read_text(encoding="utf-8", errors="replace")[:200000]
    except OSError:
        return False


def _borrar(ruta):
    if ruta.is_symlink() or ruta.is_file():
        ruta.unlink()
    elif ruta.is_dir():
        shutil.rmtree(ruta)


def _poner(origen, destino, es_carpeta, copiar):
    destino.parent.mkdir(parents=True, exist_ok=True)
    if not copiar:
        try:
            os.symlink(origen, destino, target_is_directory=es_carpeta)
            return "enlazado"
        except OSError:
            pass  # Windows sin permiso para enlaces: se copia
    if es_carpeta:
        shutil.copytree(origen, destino, ignore=_IGNORAR)
        (destino / MARCA_CARPETA).write_text(f"Copia instalada por {PACK}; se reemplaza al reinstalar.\n",
                                             encoding="utf-8")
    else:
        shutil.copy2(origen, destino)
    return "copiado"


def _colocar(origen, destino, es_carpeta, copiar, raiz, acciones, conflictos):
    if destino.is_symlink() or destino.exists():
        if destino.is_symlink() and _mismo(destino, origen) and not copiar:
            acciones.append((str(destino), "ya estaba"))
            return
        if not _es_nuestro(destino, es_carpeta, raiz):
            conflictos.append(str(destino))
            return
        _borrar(destino)
        _poner(origen, destino, es_carpeta, copiar)
        acciones.append((str(destino), "actualizado"))
        return
    acciones.append((str(destino), _poner(origen, destino, es_carpeta, copiar)))


# ---------------------------------------------------------------- terceros

def descargar_tercero(t, raiz=RAIZ, git="git"):
    """Clona (o actualiza) el repositorio original del kit en .terceros/<id>. Devuelve (ruta, error)."""
    carpeta = Path(raiz) / ".terceros" / t["id"]
    if not t.get("repo"):
        return None, "no tiene repositorio"
    if shutil.which(git) is None:
        return None, "falta git; instálalo y vuelve a correr el instalador"
    url = f"https://github.com/{t['repo']}.git"
    try:
        if (carpeta / ".git").is_dir():
            subprocess.run([git, "-C", str(carpeta), "pull", "--ff-only", "--quiet"], check=True,
                           capture_output=True, timeout=300)
        else:
            carpeta.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run([git, "clone", "--depth", "1", "--quiet", url, str(carpeta)], check=True,
                           capture_output=True, timeout=600)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        detalle = getattr(exc, "stderr", b"") or b""
        return None, f"no se pudo descargar {url}: {detalle.decode(errors='replace').strip()[:200]}"
    return carpeta, None


# ---------------------------------------------------------------- instalar y quitar

def instalar(elegido, cat, raiz=RAIZ, home=None, codex_home=None, copiar=False, origen_terceros=None):
    """Instala lo elegido. Devuelve {"acciones", "conflictos", "errores"}."""
    raiz, home = Path(raiz), Path(home) if home else Path.home()
    acciones, conflictos, errores = [], [], list(elegido.get("errores", []))
    destinos = ias(home, codex_home)
    if not destinos:
        return {"acciones": [], "conflictos": [], "errores": errores, "sin_ias": True}
    skills_locales = [(raiz / "skills" / s, s) for s in elegido["skills"]]
    for origen, slug in skills_locales:
        if not (origen / "SKILL.md").is_file():
            errores.append(f"falta skills/{slug}/SKILL.md en el repositorio")
    skills_terceros = []
    descargar = origen_terceros or (lambda t: descargar_tercero(t, raiz))
    por_id = {t["id"]: t for t in cat["terceros"]}
    for tid in elegido["terceros"]:
        carpeta, error = descargar(por_id[tid])
        if error:
            errores.append(f"{por_id[tid]['nombre']}: {error}")
            continue
        for s in por_id[tid]["skills"]:
            origen = Path(carpeta) / s["ruta"]
            if (origen / "SKILL.md").is_file():
                skills_terceros.append((origen, s["slug"]))
            else:
                errores.append(f"{por_id[tid]['nombre']}: no encontré {s['ruta']}/SKILL.md en su repositorio")
    for nombre_ia, c_skills, c_agentes, ext in destinos:
        for origen, slug in skills_locales + skills_terceros:
            if (origen / "SKILL.md").is_file():
                _colocar(origen, c_skills / slug, True, copiar, raiz, acciones, conflictos)
        for slug in elegido["agentes"]:
            origen = raiz / "agentes" / nombre_ia / f"{slug}{ext}"
            if not origen.is_file():
                errores.append(f"falta agentes/{nombre_ia}/{slug}{ext}; corre python3 scripts/agentes.py generar")
                continue
            _colocar(origen, c_agentes / f"{slug}{ext}", False, copiar, raiz, acciones, conflictos)
        if nombre_ia == "antigravity" and elegido["agentes"]:
            plugin = c_agentes.parent / "plugin.json"
            if not plugin.exists():
                plugin.parent.mkdir(parents=True, exist_ok=True)
                plugin.write_text(json.dumps(PLUGIN, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                acciones.append((str(plugin), "creado"))
    return {"acciones": acciones, "conflictos": conflictos, "errores": errores}


def _todos_los_nombres(cat):
    idx = indice(cat)
    skills = [s for s, i in idx.items() if i["tipo"] == "skill"]
    skills += [s["slug"] for t in cat["terceros"] for s in t["skills"]]
    agentes = [s for s, i in idx.items() if i["tipo"] == "agente"]
    return skills, agentes


def quitar(cat, raiz=RAIZ, home=None, codex_home=None):
    """Quita solo lo que instaló este pack (enlaces a él o copias con su marca)."""
    raiz, home = Path(raiz), Path(home) if home else Path.home()
    skills, agentes = _todos_los_nombres(cat)
    acciones = []
    for _, c_skills, c_agentes, ext in ias(home, codex_home):
        for slug in skills:
            destino = c_skills / slug
            if (destino.is_symlink() or destino.exists()) and _es_nuestro(destino, True, raiz):
                _borrar(destino)
                acciones.append((str(destino), "quitado"))
        for slug in agentes:
            destino = c_agentes / f"{slug}{ext}"
            if (destino.is_symlink() or destino.exists()) and _es_nuestro(destino, False, raiz):
                _borrar(destino)
                acciones.append((str(destino), "quitado"))
    return {"acciones": acciones, "conflictos": [], "errores": []}


def estado(cat, raiz=RAIZ, home=None, codex_home=None):
    """{ia: {"skills": [...], "agentes": [...]}} con lo del pack que hay instalado."""
    raiz, home = Path(raiz), Path(home) if home else Path.home()
    skills, agentes = _todos_los_nombres(cat)
    salida = {}
    for nombre_ia, c_skills, c_agentes, ext in ias(home, codex_home):
        salida[nombre_ia] = {
            "skills": [s for s in skills if (c_skills / s).exists() and _es_nuestro(c_skills / s, True, raiz)],
            "agentes": [a for a in agentes if (c_agentes / f"{a}{ext}").exists()
                        and _es_nuestro(c_agentes / f"{a}{ext}", False, raiz)],
        }
    return salida


# ---------------------------------------------------------------- para la web

def para_la_web(elegido, cat, carpeta, raiz=RAIZ):
    """Prepara lo elegido para la IA en la web.

    - `claude-ai/<slug>.zip`: se sube en Claude.ai → Configuración → Capacidades → Skills.
    - `instrucciones/<slug>.md`: se pega en un Proyecto de ChatGPT, un GPT o un Gem de Gemini.
    Los kits de la comunidad no se empaquetan: se enlazan a su repositorio original en el LEEME.
    """
    raiz, carpeta = Path(raiz), Path(carpeta).expanduser()
    (carpeta / "claude-ai").mkdir(parents=True, exist_ok=True)
    (carpeta / "instrucciones").mkdir(parents=True, exist_ok=True)
    idx, hechos = indice(cat), []
    for slug in elegido["skills"]:
        origen = raiz / "skills" / slug
        if not (origen / "SKILL.md").is_file():
            continue
        with zipfile.ZipFile(carpeta / "claude-ai" / f"{slug}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for archivo in sorted(origen.rglob("*")):
                if archivo.is_file() and archivo.name != ".DS_Store":
                    z.write(archivo, Path(slug) / archivo.relative_to(origen))
        (carpeta / "instrucciones" / f"{slug}.md").write_text(
            (origen / "SKILL.md").read_text(encoding="utf-8"), encoding="utf-8")
        hechos.append(slug)
    for slug in elegido["agentes"]:
        fuente = raiz / "agentes" / f"{slug}.md"
        if fuente.is_file():
            (carpeta / "instrucciones" / f"agente-{slug}.md").write_text(fuente.read_text(encoding="utf-8"),
                                                                        encoding="utf-8")
            hechos.append(slug)
    lineas = [f"# {cat['pack']['titulo']} para la IA en la web", "",
              "## Claude.ai", "Configuración → Capacidades → Skills → Subir skill: sube cada .zip de `claude-ai/`.", "",
              "## ChatGPT o Gemini",
              "Crea un Proyecto o un GPT (ChatGPT) o un Gem (Gemini) por herramienta y pega como instrucciones "
              "el archivo de `instrucciones/` que corresponda. Los agentes se programan con las Tareas de ChatGPT "
              "o las Acciones programadas de Gemini.", "", "## Incluido", ""]
    lineas += [f"- `{s}`: {idx[s]['nombre']}" for s in hechos if s in idx]
    terceros = [t for t in cat["terceros"] if t["id"] in elegido["terceros"]]
    if terceros:
        lineas += ["", "## Kits de la comunidad (desde su repositorio original)", ""]
        lineas += [f"- {t['nombre']}, de {t['autor']} ({t['licencia']}): https://github.com/{t['repo']}"
                   for t in terceros if t.get("repo")]
    (carpeta / "LEEME.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return hechos


# ---------------------------------------------------------------- salida

def lista_texto(cat):
    idx = indice(cat)
    lineas = [f"{cat['pack']['titulo']} · {cat['pack']['nombre']}", "", "GENERAL (se instala siempre)"]
    for s, i in idx.items():
        if i["grupo"] == "general":
            extra = f" [{i['frecuencia']}]" if i["tipo"] == "agente" else ""
            lineas.append(f"  {i['tipo']:6} {s}: {i['nombre']}{extra}. {i['descripcion']}")
    for t in cat["terceros"]:
        if t["lugar"] == "general":
            lineas.append(f"  kit    {t['id']}: {t['nombre']}, de {t['autor']} ({t['licencia']}). {t['que']}")
    for area in cat["areas"]:
        lineas += ["", f"ÁREA {area['id']}: {area['nombre']}. {area['para']}"]
        for s, i in idx.items():
            if i["grupo"] == area["id"]:
                extra = f" [{i['frecuencia']}]" if i["tipo"] == "agente" else ""
                lineas.append(f"  {i['tipo']:6} {s}: {i['nombre']}{extra}. {i['descripcion']}")
        for t in cat["terceros"]:
            if t["lugar"] == area["id"]:
                req = f" Requiere: {t['requiere']}" if t.get("requiere") else ""
                lineas.append(f"  kit    {t['id']}: {t['nombre']}, de {t['autor']} ({t['licencia']}, {t['nivel']}). "
                              f"{t['que']}{req}")
    return "\n".join(lineas)


def _corta(ruta):
    casa = str(Path.home())
    return "~" + ruta[len(casa):] if ruta.startswith(casa) else ruta


def _separar(valor):
    return [x.strip() for x in (valor or "").split(",") if x.strip()]


def main(argv=None):
    p = argparse.ArgumentParser(description=f"Instalador de {PACK}.")
    p.add_argument("--lista", action="store_true", help="muestra el catálogo")
    p.add_argument("--areas", help="instala todo lo de estas áreas (separadas por comas)")
    p.add_argument("--elegir", help="slugs de skills, agentes o kits a instalar (separados por comas)")
    p.add_argument("--terceros", help="ids de kits de la comunidad (separados por comas)")
    p.add_argument("--sin-general", action="store_true", help="no instala lo general")
    p.add_argument("--copiar", action="store_true", help="copia en vez de enlazar")
    p.add_argument("--estado", action="store_true", help="muestra qué hay instalado")
    p.add_argument("--quitar", action="store_true", help="quita lo que instaló este pack")
    p.add_argument("--web", metavar="CARPETA", help="prepara archivos para la IA en la web")
    p.add_argument("--json", action="store_true", help="salida en JSON")
    a = p.parse_args(argv)
    cat = cargar()
    codex_home = os.environ.get("CODEX_HOME") or None

    if a.lista:
        print(json.dumps(cat, ensure_ascii=False, indent=2) if a.json else lista_texto(cat))
        return 0
    if a.estado:
        e = estado(cat, codex_home=codex_home)
        if a.json:
            print(json.dumps(e, ensure_ascii=False, indent=2))
        elif not e:
            print("No encontré Claude Code, Codex ni Antigravity en este equipo.")
        for ia, d in e.items() if not a.json else []:
            print(f"● {ia}: {len(d['skills'])} skills y {len(d['agentes'])} agentes del pack")
        return 0
    if a.quitar:
        r = quitar(cat, codex_home=codex_home)
        for ruta, est in r["acciones"]:
            print(f"● {est}: {_corta(ruta)}")
        print(f"Listo: {len(r['acciones'])} elementos quitados.")
        return 0

    elegido = plan(cat, general=not a.sin_general, areas=_separar(a.areas), elegir=_separar(a.elegir),
                   terceros=_separar(a.terceros))
    if a.web:
        hechos = para_la_web(elegido, cat, a.web)
        for err in elegido["errores"]:
            print("✕", err)
        print(f"● {len(hechos)} herramientas listas para la web en {_corta(str(Path(a.web).expanduser()))} "
              "(lee el LEEME.md de esa carpeta).")
        return 1 if elegido["errores"] else 0

    r = instalar(elegido, cat, codex_home=codex_home, copiar=a.copiar)
    if a.json:
        print(json.dumps({**r, "plan": elegido}, ensure_ascii=False, indent=2))
        return 1 if (r["conflictos"] or r["errores"]) else 0
    if r.get("sin_ias"):
        print("No encontré Claude Code (~/.claude), Codex (~/.codex) ni Antigravity (~/.gemini) en este equipo.\n"
              "Si usas la IA en la web, prepara los archivos con: python3 scripts/instalar.py --web <carpeta>")
        return 1
    nuevos = [x for x in r["acciones"] if x[1] != "ya estaba"]
    for ruta, est in nuevos:
        print(f"● {est}: {_corta(ruta)}")
    ya = len(r["acciones"]) - len(nuevos)
    if ya:
        print(f"● {ya} elementos ya estaban instalados.")
    for ruta in r["conflictos"]:
        print(f"✕ conflicto: {_corta(ruta)} ya existe y no es de este pack. No lo toqué; decide con la persona.")
    for err in r["errores"]:
        print("✕", err)
    print(f"Resumen: {len(elegido['skills'])} skills, {len(elegido['agentes'])} agentes y "
          f"{len(elegido['terceros'])} kits de la comunidad para {', '.join(i[0] for i in ias(Path.home(), codex_home))}.")
    if any(est == "copiado" for _, est in r["acciones"]):
        print("Quedó copiado: vuelve a correr el instalador después de cada actualización del pack.")
    print("Abre una sesión nueva de tu IA para que tome lo instalado.")
    return 1 if (r["conflictos"] or r["errores"]) else 0


if __name__ == "__main__":
    sys.exit(main())
