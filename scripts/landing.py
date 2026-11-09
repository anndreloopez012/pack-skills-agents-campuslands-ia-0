#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La landing del pack, generada desde catalogo.json.

La plantilla es `guias/landing.plantilla.html` (el cuerpo de la página, con `/*CATALOGO*/null` donde va
el catálogo). De ahí sale `docs/index.html`, la página que publica GitHub Pages.

Uso:
    python3 scripts/landing.py generar             # escribe docs/index.html
    python3 scripts/landing.py revisar             # avisa si docs/index.html quedó viejo
    python3 scripts/landing.py artefacto <ruta>    # escribe el cuerpo sin <head> (para publicarlo en otra parte)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PLANTILLA = RAIZ / "guias" / "landing.plantilla.html"
SALIDA = RAIZ / "docs" / "index.html"
CABEZA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
PIE = "\n</body>\n</html>\n"


def cuerpo(raiz=RAIZ):
    catalogo = json.loads((Path(raiz) / "catalogo.json").read_text(encoding="utf-8"))
    datos = json.dumps(catalogo, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    plantilla = (Path(raiz) / "guias" / "landing.plantilla.html").read_text(encoding="utf-8")
    if "/*CATALOGO*/null" not in plantilla:
        raise ValueError("la plantilla no tiene el marcador /*CATALOGO*/null")
    return plantilla.replace("/*CATALOGO*/null", datos)


def pagina(raiz=RAIZ):
    return CABEZA + cuerpo(raiz) + PIE


def revisar(raiz=RAIZ):
    salida = Path(raiz) / "docs" / "index.html"
    actual = salida.read_text(encoding="utf-8") if salida.is_file() else None
    return [] if actual == pagina(raiz) else ["docs/index.html no coincide con el catálogo; corre python3 scripts/landing.py generar"]


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    accion = args[0] if args else "revisar"
    if accion == "generar":
        SALIDA.parent.mkdir(parents=True, exist_ok=True)
        SALIDA.write_text(pagina(), encoding="utf-8")
        print("● docs/index.html generado desde catalogo.json")
        return 0
    if accion == "artefacto" and len(args) > 1:
        Path(args[1]).write_text(cuerpo(), encoding="utf-8")
        print(f"● {args[1]}")
        return 0
    if accion == "revisar":
        errores = revisar()
        for e in errores:
            print("✕", e)
        if not errores:
            print("● docs/index.html está al día con el catálogo.")
        return 1 if errores else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
