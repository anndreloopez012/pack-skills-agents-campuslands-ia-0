#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisa que el pack esté completo y coherente antes de publicarlo.

- Cada skill y agente del catálogo tiene su archivo, con `name` igual al slug y descripción válida.
- No sobra ninguna carpeta en skills/ ni ningún agente en agentes/ que no esté en el catálogo.
- No hay slugs repetidos (incluidos los de los kits de la comunidad).
- Las tres versiones de cada agente están al día y sus skills existen.
- docs/index.html coincide con el catálogo.
- La skill de instalación está igual en .agents/skills y .claude/skills.
- Prueba el instalador en un equipo simulado (carpeta temporal): instala, respeta lo ajeno y quita.

Uso:
    python3 scripts/verificar.py
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "scripts"))

import agentes as A  # noqa: E402
import instalar as I  # noqa: E402
import landing as L  # noqa: E402

_NOMBRE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _frontmatter(texto):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", texto, re.DOTALL)
    if not m:
        return None
    meta = {}
    for linea in m.group(1).splitlines():
        par = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", linea)
        if par:
            meta[par.group(1)] = par.group(2).strip()
    return meta


def revisar_catalogo(cat):
    errores, vistos = [], {}
    idx = I.indice(cat)
    nombres = list(idx) + [s["slug"] for t in cat["terceros"] for s in t["skills"]]
    for n in nombres:
        vistos[n] = vistos.get(n, 0) + 1
        if not _NOMBRE.match(n):
            errores.append(f"catálogo: slug inválido «{n}»")
    errores += [f"catálogo: slug repetido «{n}»" for n, k in vistos.items() if k > 1]
    for clave in ("descripcion", "nombre"):
        errores += [f"catálogo: {s} no tiene {clave}" for s, i in idx.items() if not i.get(clave)]
    errores += [f"catálogo: el agente {s} no tiene frecuencia" for s, i in idx.items()
                if i["tipo"] == "agente" and not i.get("frecuencia")]
    ids = {a["id"] for a in cat["areas"]} | {"general"}
    errores += [f"catálogo: el kit {t['id']} va a un lugar que no existe ({t['lugar']})"
                for t in cat["terceros"] if t["lugar"] not in ids]
    return errores


def revisar_archivos(cat):
    errores, avisos = [], []
    idx = I.indice(cat)
    skills = {s for s, i in idx.items() if i["tipo"] == "skill"}
    agentes = {s for s, i in idx.items() if i["tipo"] == "agente"}
    for slug in sorted(skills):
        ruta = RAIZ / "skills" / slug / "SKILL.md"
        if not ruta.is_file():
            errores.append(f"falta skills/{slug}/SKILL.md")
            continue
        texto = ruta.read_text(encoding="utf-8")
        meta = _frontmatter(texto)
        if not meta:
            errores.append(f"skills/{slug}/SKILL.md: sin frontmatter")
            continue
        if meta.get("name") != slug:
            errores.append(f"skills/{slug}/SKILL.md: name «{meta.get('name')}» no coincide con el slug")
        desc = meta.get("description", "")
        if not desc:
            errores.append(f"skills/{slug}/SKILL.md: falta description")
        elif desc.startswith('"') and ('"' in desc[1:-1] or not desc.endswith('"')):
            errores.append(f"skills/{slug}/SKILL.md: la description tiene comillas dobles dentro; usa «»")
        lineas = texto.count("\n")
        if lineas < 35:
            avisos.append(f"skills/{slug}/SKILL.md: muy corta ({lineas} líneas)")
    sobrantes = {p.name for p in (RAIZ / "skills").iterdir() if p.is_dir()} - skills
    errores += [f"skills/{s}: no está en el catálogo" for s in sorted(sobrantes)]
    fuentes = {p.stem for p in A.fuentes(RAIZ / "agentes")}
    errores += [f"falta agentes/{s}.md" for s in sorted(agentes - fuentes)]
    errores += [f"agentes/{s}.md: no está en el catálogo" for s in sorted(fuentes - agentes)]
    errores += A.revisar(RAIZ / "agentes")
    todas = skills | {s["slug"] for t in cat["terceros"] for s in t["skills"]}
    for s in sorted(fuentes & agentes):
        for dep in I.dependencias_de_agente(RAIZ, s):
            if dep not in todas:
                errores.append(f"agentes/{s}.md: usa la skill «{dep}», que no está en el pack")
    return errores, avisos


def revisar_espejos():
    a = RAIZ / ".agents" / "skills" / "instalar-pack" / "SKILL.md"
    b = RAIZ / ".claude" / "skills" / "instalar-pack" / "SKILL.md"
    if not a.is_file() or not b.is_file():
        return ["falta la skill instalar-pack en .agents/skills o .claude/skills"]
    return [] if a.read_bytes() == b.read_bytes() else [".agents/skills/instalar-pack y .claude/skills/instalar-pack no son iguales"]


def probar_instalador(cat):
    """Instala en un equipo simulado con las tres IA, sin red (los kits de la comunidad se simulan)."""
    errores = []
    with tempfile.TemporaryDirectory() as tmp:
        home = Path(tmp) / "casa"
        for d in (".claude", ".codex", ".gemini"):
            (home / d).mkdir(parents=True)
        falso = Path(tmp) / "terceros"

        def simulado(t):
            carpeta = falso / t["id"]
            for s in t["skills"]:
                ruta = carpeta / s["ruta"]
                ruta.mkdir(parents=True, exist_ok=True)
                (ruta / "SKILL.md").write_text(f"---\nname: {s['slug']}\ndescription: prueba\n---\n", encoding="utf-8")
            return carpeta, None

        ajeno = home / ".claude" / "skills" / "inbox-triage"
        ajeno.mkdir(parents=True)
        (ajeno / "SKILL.md").write_text("de otra persona\n", encoding="utf-8")

        primera_area = cat["areas"][0]["id"]
        plan = I.plan(cat, areas=[primera_area], terceros=["linkedin-skills"])
        r = I.instalar(plan, cat, home=home, origen_terceros=simulado)
        if r["errores"]:
            errores += [f"instalador: {e}" for e in r["errores"]]
        if str(ajeno) not in r["conflictos"] or (ajeno / "SKILL.md").read_text() != "de otra persona\n":
            errores.append("instalador: pisó o no reportó una skill ajena con el mismo nombre")
        for ia, c_skills, c_agentes, ext in I.ias(home):
            for slug in plan["skills"]:
                if ia == "claude" and slug == "inbox-triage":
                    continue
                if not (c_skills / slug / "SKILL.md").is_file():
                    errores.append(f"instalador: no quedó la skill {slug} en {ia}")
            for slug in plan["agentes"]:
                if not (c_agentes / f"{slug}{ext}").is_file():
                    errores.append(f"instalador: no quedó el agente {slug} en {ia}")
            if not (c_skills / "linkedin-post-writer" / "SKILL.md").is_file():
                errores.append(f"instalador: no quedó el kit linkedin-skills en {ia}")
        segunda = I.instalar(plan, cat, home=home, origen_terceros=simulado)
        if any(est not in ("ya estaba",) for _, est in segunda["acciones"]):
            errores.append("instalador: la segunda instalación cambió cosas (debe decir «ya estaba»)")
        I.quitar(cat, home=home)
        quedan = I.estado(cat, home=home)
        if any(d["agentes"] or d["skills"] for d in quedan.values()):
            errores.append(f"instalador: --quitar dejó restos: {quedan}")
        if not (ajeno / "SKILL.md").is_file():
            errores.append("instalador: --quitar borró una skill ajena")
        web = Path(tmp) / "web"
        hechos = I.para_la_web(I.plan(cat), cat, web)
        if not hechos or not (web / "LEEME.md").is_file() or not list((web / "claude-ai").glob("*.zip")):
            errores.append("instalador: --web no preparó los archivos")
    return errores


def main():
    cat = json.loads((RAIZ / "catalogo.json").read_text(encoding="utf-8"))
    errores = revisar_catalogo(cat)
    e2, avisos = revisar_archivos(cat)
    errores += e2 + L.revisar() + revisar_espejos()
    if not errores:
        errores += probar_instalador(cat)
    idx = I.indice(cat)
    for a in avisos:
        print("· aviso:", a)
    for e in errores:
        print("✕", e)
    if not errores:
        sk = sum(1 for i in idx.values() if i["tipo"] == "skill")
        ag = len(idx) - sk
        print(f"● Todo en verde: {sk} skills, {ag} agentes, {len(cat['areas'])} áreas y "
              f"{len(cat['terceros'])} kits de la comunidad. El instalador pasó la prueba en un equipo simulado.")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
