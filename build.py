#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Punto de entrada único de compilación del programa.

    python build.py syllabus        el documento completo (docx + pdf)
    python build.py deck 04         una presentación
    python build.py decks           todas las presentaciones registradas
    python build.py all             todo
    python build.py list            qué hay registrado y qué falta

Los artefactos se escriben en dist/. Nada más de este archivo necesita tocarse
al añadir un módulo: el registro vive en content/program.py.
"""

import importlib
import os
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

DIST = os.path.join(ROOT, "dist")


def _deck_module(num):
    """Devuelve el módulo del deck NN, o None si aún no existe."""
    try:
        return importlib.import_module("content.decks.m%02d" % num)
    except ModuleNotFoundError:
        return None


def build_syllabus(pdf=True):
    from engine import syllabus_doc
    path = syllabus_doc.build_document()
    print("  docx  %s" % os.path.basename(path))
    if pdf:
        syllabus_doc.export_pdf(path, syllabus_doc.PDF_PATH)
        print("  pdf   %s" % os.path.basename(syllabus_doc.PDF_PATH))
    return path


def build_deck(num):
    from engine import deck
    if _deck_module(num) is None:
        print("  m%02d   (sin escribir todavía)" % num)
        return None
    path = deck.build("m%02d" % num)
    return path


def registered():
    """Módulos declarados en el programa, en orden."""
    from content import program
    from content.syllabus import part1, part2, part3, part4, part5
    out = []
    for mod in (part1, part2, part3, part4, part5):
        for part in mod.PARTS:
            for m in part["modules"]:
                out.append(m)
    return out


def cmd_list():
    mods = registered()
    hechos = sum(1 for m in mods if _deck_module(m["num"]))
    print("%d módulos registrados · %d presentaciones escritas\n" % (len(mods), hechos))
    for m in mods:
        mark = "■" if _deck_module(m["num"]) else "□"
        print("  %s  %2d  %-52s %s" % (mark, m["num"], m["title"], m["duracion"]))
    print("\n  ■ presentación escrita   □ pendiente")


def main(argv):
    cmd = argv[0] if argv else "all"
    os.makedirs(DIST, exist_ok=True)
    t0 = time.time()

    if cmd == "list":
        cmd_list()
        return

    if cmd == "syllabus":
        build_syllabus()

    elif cmd == "deck":
        if len(argv) < 2:
            sys.exit("uso: python build.py deck <número de módulo>")
        build_deck(int(argv[1]))

    elif cmd == "decks":
        for m in registered():
            build_deck(m["num"])

    elif cmd == "all":
        build_syllabus()
        for m in registered():
            build_deck(m["num"])

    else:
        sys.exit(__doc__)

    print("\nlisto en %.1fs · dist/" % (time.time() - t0))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1:])
