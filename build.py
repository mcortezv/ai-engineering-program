#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Punto de entrada único de compilación del programa.

    python build.py syllabus        el documento completo (docx + pdf)
    python build.py deck 04         una presentación
    python build.py decks           todas las presentaciones registradas
    python build.py all             todo
    python build.py list            qué hay registrado y qué falta
    python build.py check           cobertura del temario y texto fuera de lienzo
    python build.py layout          desborde y solapes en los PDF ya construidos

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


def _contenidos(module):
    """Los contenidos del módulo, aplanados y numerados desde 1."""
    out = []
    for c in module["contenidos"]:
        out.append(c[0] if isinstance(c, (list, tuple)) else c)
    return out


def cmd_check():
    """Cada punto de 'contenidos' debe tener al menos una lámina que lo cubra.

    El contrato es explícito: las láminas declaran `covers` con los números de
    los contenidos que abordan. Comparar por palabras clave no sirve, porque un
    término puede aparecer en la agenda sin que el tema llegue a explicarse.
    """
    problemas = 0
    revisados = 0
    for m in registered():
        deck = _deck_module(m["num"])
        if deck is None:
            continue
        revisados += 1
        items = _contenidos(m)
        cubiertos = set()
        for slide in deck.SLIDES:
            for n in slide.get("covers", []):
                cubiertos.add(n)

        sin_declarar = [s.get("title", "?") for s in deck.SLIDES
                        if s.get("kind") == "content" and "covers" not in s]
        faltan = [(i, t) for i, t in enumerate(items, 1) if i not in cubiertos]
        fuera = [n for n in cubiertos if n < 1 or n > len(items)]

        if faltan or fuera:
            problemas += 1
            print("\n  Módulo %d · %s" % (m["num"], m["title"]))
            for i, t in faltan:
                print("     SIN LÁMINA   %d. %s" % (i, t[:78]))
            for n in fuera:
                print("     NO EXISTE    covers=%d (el temario tiene %d puntos)"
                      % (n, len(items)))
        if sin_declarar:
            print("\n  Módulo %d · láminas sin declarar 'covers':" % m["num"])
            for t in sin_declarar:
                print("     · %s" % t[:78])

    print("\n%d presentaciones revisadas · %d con huecos"
          % (revisados, problemas))
    return problemas


_SVG_TEXT = None
_METRICAS = {}


def _ancho_texto(texto, size, negrita, mono):
    """Ancho real en unidades de lienzo, medido con las métricas de la fuente."""
    from fontTools.ttLib import TTFont

    clave = ("mono" if mono else ("bold" if negrita else "regular"))
    if clave not in _METRICAS:
        archivo = {
            "regular": "figtree-latin-400-normal.woff2",
            "bold": "figtree-latin-700-normal.woff2",
        }.get(clave)
        if archivo is None:      # Consolas es monoespaciada: 0.55 em por glifo
            _METRICAS[clave] = ("mono", 0.55)
        else:
            f = TTFont(os.path.join(ROOT, "assets", "fonts", archivo))
            upm = f["head"].unitsPerEm
            cmap = f.getBestCmap()
            hmtx = f["hmtx"]
            _METRICAS[clave] = ("real", (cmap, hmtx, upm))

    tipo, datos = _METRICAS[clave]
    if tipo == "mono":
        return len(texto) * size * datos

    cmap, hmtx, upm = datos
    total = 0
    for ch in texto:
        nombre = cmap.get(ord(ch))
        total += hmtx[nombre][0] if nombre else int(upm * 0.5)
    return total / float(upm) * size


def cmd_svg():
    """Busca texto que se sale del lienzo de un diagrama.

    Un `<text>` demasiado largo no desborda la lámina: lo recorta el propio
    viewBox del SVG, así que el PDF no lo delata y la revisión por bloques de
    texto tampoco lo ve. El ancho se mide con las métricas reales de Figtree,
    no con una estimación por número de caracteres.
    """
    global _SVG_TEXT
    import re
    if _SVG_TEXT is None:
        _SVG_TEXT = re.compile(
            r'<text x="([\d.]+)"[^>]*?font-family="([^"]*)"[^>]*?'
            r'font-size="([\d.]+)"[^>]*?font-weight="(\d+)"[^>]*?'
            r'text-anchor="(\w+)"[^>]*>(.*?)</text>')

    LIENZO = 1120.0
    problemas = 0

    for nombre in sorted(os.listdir(os.path.join(ROOT, "engine", "diagrams"))):
        if not nombre.startswith("mod") or not nombre.endswith(".py"):
            continue
        mod = importlib.import_module("engine.diagrams.%s" % nombre[:-3])
        for fn in sorted(d for d in dir(mod) if not d.startswith("_")):
            obj = getattr(mod, fn)
            if not callable(obj) or getattr(obj, "__module__", "") != mod.__name__:
                continue
            try:
                svg = obj()
            except TypeError:
                continue
            for x, familia, size, peso, anchor, texto in _SVG_TEXT.findall(svg):
                plano = re.sub(r"<[^>]+>", "", texto)
                plano = plano.replace("&lt;", "<").replace("&gt;", ">")
                ancho = _ancho_texto(plano, float(size), int(peso) >= 600,
                                     "Consolas" in familia)
                x = float(x)
                fin = x + ancho if anchor == "start" else (
                    x + ancho / 2 if anchor == "middle" else x)
                if fin > LIENZO:
                    problemas += 1
                    print("  %-34s se sale %3d u : %s"
                          % ("%s.%s" % (nombre[:-3], fn), int(fin - LIENZO),
                             plano[:52]))

    print("\n%d textos de diagrama fuera del lienzo" % problemas)
    return problemas


ALTO_PT = 190.5 * 2.8345          # la lámina, en puntos PDF
PAD_TOP = 17 * 2.8345
PAD_BOT = 15 * 2.8345
BANDA_PIE = ALTO_PT - 34          # por debajo de aquí solo vive el pie


def _sup(caja):
    return max(0.0, caja[2] - caja[0]) * max(0.0, caja[3] - caja[1])


def cmd_layout():
    """Desborde vertical y solapes de texto en los PDF ya construidos.

    Son los dos fallos que `check` no puede ver. El primero ocurre cuando el
    cuerpo de una lámina no cabe: `.body` está centrado, así que el contenido
    sobra por arriba y por abajo a la vez y acaba tapando el titular. El
    segundo, cuando dos etiquetas de un diagrama caen encima. Ninguno da error
    al compilar y los dos se ven fatal proyectados.
    """
    import fitz

    desbordes = solapes = 0
    for m in registered():
        deck = _deck_module(m["num"])
        if deck is None:
            continue
        ruta = os.path.join(DIST, deck.DECK["outfile"])
        if not os.path.exists(ruta):
            continue
        doc = fitz.open(ruta)
        for n, pg in enumerate(doc, 1):
            texto = pg.get_text()
            # fuera del area util
            for blq in pg.get_text("blocks"):
                y0, y1, txt = blq[1], blq[3], blq[4].strip()
                if not txt or y0 > BANDA_PIE:
                    continue
                if y0 < PAD_TOP - 6 or y1 > ALTO_PT - PAD_BOT + 4:
                    desbordes += 1
                    print("     DESBORDE   %s lám %d · %s"
                          % (deck.DECK["outfile"][:34], n,
                             txt.replace(chr(10), " ")[:46]))
            # texto encima de texto; en los separadores el numeral
            # gigante comparte sitio con el titular por diseño
            if "S E C C I" in texto:
                continue
            pal = [(w[:4], w[4]) for w in pg.get_text("words")
                   if w[4].strip() and w[1] < BANDA_PIE]
            for i in range(len(pal)):
                for j in range(i + 1, len(pal)):
                    a, ta = pal[i]
                    b, tb = pal[j]
                    if a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1]:
                        continue
                    inter = _sup((max(a[0], b[0]), max(a[1], b[1]),
                                  min(a[2], b[2]), min(a[3], b[3])))
                    menor = min(_sup(a), _sup(b))
                    if menor > 0 and inter / menor > 0.45:
                        solapes += 1
                        print("     SOLAPE     %s lám %d · «%s» sobre «%s»"
                              % (deck.DECK["outfile"][:34], n, ta[:20], tb[:20]))

    print()
    print("%d bloques desbordados · %d solapes de texto"
          % (desbordes, solapes))
    return desbordes + solapes


def main(argv):
    cmd = argv[0] if argv else "all"
    os.makedirs(DIST, exist_ok=True)
    t0 = time.time()

    if cmd == "list":
        cmd_list()
        return

    if cmd == "check":
        fallos = cmd_check() + cmd_svg()
        sys.exit(1 if fallos else 0)

    if cmd == "layout":
        sys.exit(1 if cmd_layout() else 0)

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
