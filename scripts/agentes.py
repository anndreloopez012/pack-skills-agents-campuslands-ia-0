#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los agentes del pack para las tres IA, escritos una sola vez.

La fuente de cada agente es `agentes/<slug>.md` (frontmatter con `name`, `description`, `frecuencia`,
`access`, `tools` y `skills`, y las instrucciones en Markdown; ver guias/FORMATO.md). De ahí salen:

- `agentes/claude/<slug>.md`        Claude Code
- `agentes/codex/<slug>.toml`       Codex
- `agentes/antigravity/<slug>.md`   Antigravity

Cada versión lleva la marca del pack para que el instalador reconozca lo suyo y nunca pise lo ajeno.

Uso:
    python3 scripts/agentes.py generar   # escribe las tres versiones de cada agente
    python3 scripts/agentes.py revisar   # avisa si una versión quedó vieja o falta documentar una skill
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CARPETA = RAIZ / "agentes"
MARCA = "pack-skills-agents-campuslands-ia-0"
IAS = ("claude", "codex", "antigravity")

HERRAMIENTAS_CLAUDE = {
    "read": ["Read"], "write": ["Write"], "edit": ["Edit"], "search": ["Grep"], "glob": ["Glob"],
    "list": ["Glob"], "shell": ["Bash"], "web_fetch": ["WebFetch"], "web_search": ["WebSearch"],
}
HERRAMIENTAS_ANTIGRAVITY = {
    "read": ["view_file"], "write": ["write_to_file"], "edit": ["replace_file_content"],
    "search": ["grep_search"], "glob": ["find_by_name"], "list": ["list_dir"], "shell": ["run_command"],
    "web_fetch": ["read_url_content"], "web_search": ["search_web"],
}
POR_DEFECTO = ["read", "search", "glob", "list", "web_fetch", "web_search"]
_NOMBRE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def leer(texto):
    """Frontmatter y cuerpo del agente (lector simple, sin dependencias)."""
    partes = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", texto, re.DOTALL)
    if not partes:
        raise ValueError("el agente debe empezar con frontmatter entre líneas ---")
    crudo, cuerpo = partes.groups()
    meta, clave = {}, None
    for linea in crudo.splitlines():
        if not linea.strip() or linea.strip().startswith("#"):
            continue
        par = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", linea)
        if par:
            clave, valor = par.group(1).strip(), par.group(2).strip()
            if valor.startswith("[") and valor.endswith("]"):
                meta[clave] = [x.strip().strip("'\"") for x in valor[1:-1].split(",") if x.strip()]
            elif len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
                meta[clave] = valor[1:-1]
            else:
                meta[clave] = valor if valor else []
        elif linea.startswith("  - ") and clave:
            valor = linea[4:].strip().strip("'\"")
            if isinstance(meta.get(clave), list):
                meta[clave].append(valor)
            else:
                meta[clave] = [valor]
    return meta, cuerpo.strip()


def _herramientas(meta, mapa):
    pedidas = list(meta.get("tools") or POR_DEFECTO)
    if meta.get("access", "read-only") in ("write", "full"):
        pedidas += [h for h in ("write", "edit") if h not in pedidas]
    salida = []
    for herramienta in pedidas:
        for propia in mapa.get(herramienta, []):
            if propia not in salida:
                salida.append(propia)
    return salida


def validar(meta, cuerpo):
    nombre, descripcion = str(meta.get("name") or ""), str(meta.get("description") or "")
    if not _NOMBRE.match(nombre):
        raise ValueError(f"name «{nombre}» debe ser minúsculas, números y guiones")
    if not descripcion:
        raise ValueError("falta description")
    if '"' in descripcion or "\\" in descripcion:
        raise ValueError("description no puede llevar comillas dobles ni barras invertidas; usa «»")
    if "'''" in cuerpo:
        raise ValueError("las instrucciones no pueden llevar tres comillas simples seguidas")


def construir(texto):
    """Las tres versiones del agente como texto: {"claude", "codex", "antigravity"}."""
    meta, cuerpo = leer(texto)
    validar(meta, cuerpo)
    nombre, descripcion = meta["name"], meta["description"]
    skills = list(meta.get("skills") or [])
    pie = f"\n\n<!-- {MARCA} -->"

    claude = ["---", f"name: {nombre}", f'description: "{descripcion}"']
    claude.append(f"tools: {', '.join(_herramientas(meta, HERRAMIENTAS_CLAUDE))}")
    if skills:
        claude += ["skills:"] + [f"  - {s}" for s in skills]
    claude += ["model: inherit", "---", "", cuerpo + pie]

    agy = ["---", f"name: {nombre}", f'description: "{descripcion}"', "tools:"]
    agy += [f"  - {h}" for h in _herramientas(meta, HERRAMIENTAS_ANTIGRAVITY)]
    if skills:
        agy += ["skills:"] + [f"  - {s}" for s in skills]
    agy += ["mainAgent: true", "subagent: true", "commandExecutionPolicy: auto", "---", "", cuerpo + pie]

    nota = ""
    if skills:
        nota = ("\n\n### Skills que usa\nConsulta estas skills cuando apliquen:\n"
                + "\n".join(f"- `{s}`" for s in skills))
    sandbox = "workspace-write" if meta.get("access") in ("write", "full") else "read-only"
    codex = (f"# {MARCA}\n"
             f'name = "{nombre}"\ndescription = "{descripcion}"\nsandbox_mode = "{sandbox}"\n'
             f"model_reasoning_effort = \"medium\"\n\ndeveloper_instructions = '''\n{cuerpo + nota}\n'''\n")
    return {"claude": "\n".join(claude) + "\n", "codex": codex, "antigravity": "\n".join(agy) + "\n"}


def fuentes(carpeta=CARPETA):
    return sorted(p for p in Path(carpeta).glob("*.md") if p.name != "README.md")


def destinos(carpeta, nombre):
    carpeta = Path(carpeta)
    return {"claude": carpeta / "claude" / f"{nombre}.md", "codex": carpeta / "codex" / f"{nombre}.toml",
            "antigravity": carpeta / "antigravity" / f"{nombre}.md"}


def generar(carpeta=CARPETA):
    """Escribe las tres versiones de cada agente y borra las de agentes que ya no existen."""
    carpeta, escritos, vivos = Path(carpeta), [], set()
    for fuente in fuentes(carpeta):
        texto = fuente.read_text(encoding="utf-8")
        hechos = construir(texto)
        for ia, ruta in destinos(carpeta, leer(texto)[0]["name"]).items():
            ruta.parent.mkdir(parents=True, exist_ok=True)
            ruta.write_text(hechos[ia], encoding="utf-8")
            escritos.append(ruta)
            vivos.add(ruta)
    for ia in IAS:
        for viejo in (carpeta / ia).glob("*") if (carpeta / ia).is_dir() else []:
            if viejo not in vivos:
                viejo.unlink()
    return escritos


def revisar(carpeta=CARPETA):
    """Errores: versiones que no coinciden con su fuente y skills sin documentar."""
    errores, carpeta = [], Path(carpeta)
    for fuente in fuentes(carpeta):
        texto = fuente.read_text(encoding="utf-8")
        try:
            meta, cuerpo = leer(texto)
            hechos = construir(texto)
        except ValueError as exc:
            errores.append(f"agentes/{fuente.name}: {exc}")
            continue
        if meta["name"] != fuente.stem:
            errores.append(f"agentes/{fuente.name}: name «{meta['name']}» no coincide con el nombre del archivo")
        for ia, ruta in destinos(carpeta, meta["name"]).items():
            actual = ruta.read_text(encoding="utf-8") if ruta.is_file() else None
            if actual != hechos[ia]:
                errores.append(f"agentes/{ia}/{ruta.name}: no coincide con su fuente; "
                               "corre python3 scripts/agentes.py generar")
        for skill in meta.get("skills") or []:
            if f"`{skill}`" not in cuerpo:
                errores.append(f"agentes/{fuente.name}: la skill {skill} no aparece en la tabla «Tus skills»")
    return errores


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    accion = args[0] if args else "revisar"
    if accion == "generar":
        escritos = generar()
        print(f"● {len(escritos)} archivos escritos para {len(fuentes())} agentes.")
        errores = revisar()
    elif accion == "revisar":
        errores = revisar()
        if not errores:
            print(f"● Los {len(fuentes())} agentes y sus tres versiones están al día.")
    else:
        print(__doc__)
        return 2
    for error in errores:
        print("✕", error)
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
