# -*- coding: utf-8 -*-
"""
Genera el PDF de diapositivas de un modulo.

Mismo pipeline que hyperlabs-press/paper/build-pdf.ps1: HTML + slides.css ->
Chrome headless --print-to-pdf. Se usa Chrome y no Word porque las laminas
necesitan flexbox, grid y color a sangre, que Word no da.

    python build_slides.py m04
"""

import base64
import glob
import importlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Figtree va versionada en el repo: el build no debe depender de node_modules
# ni de ningún proyecto hermano para producir un PDF idéntico.
FONT_DIR = os.path.join(ROOT, "assets", "fonts")

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def find_chrome():
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    raise SystemExit("No se encontró Chrome ni Edge para imprimir el PDF.")


def font_faces():
    """Figtree inlineada: el PDF debe ser reproducible sin red."""
    faces = []
    for style in ("normal", "italic"):
        for subset in ("latin", "latin-ext"):
            path = os.path.join(FONT_DIR, "figtree-%s-wght-%s.woff2" % (subset, style))
            if not os.path.exists(path):
                continue
            with open(path, "rb") as fh:
                b64 = base64.b64encode(fh.read()).decode("ascii")
            faces.append(
                "@font-face{font-family:'Figtree';font-style:%s;font-weight:300 900;"
                "font-display:block;src:url(data:font/woff2;base64,%s) "
                "format('woff2-variations')}" % (style, b64))
    if not faces:
        print("  aviso: Figtree no encontrada, se usará Segoe UI", file=sys.stderr)
    return "\n".join(faces)


# ------------------------------------------------------------------ laminas --

def foot(deck, index, total):
    """Pie con identidad, numero y barra de avance."""
    pct = 100.0 * index / max(total - 1, 1)
    return (
        '<div class="foot"><span>%s</span><span>%d / %d</span></div>'
        '<div class="bar" style="width:%.1f%%"></div>'
    ) % (deck["footer"], index + 1, total, pct)


def render_slide(deck, slide, index, total):
    kind = slide["kind"]
    inner = ""
    extra_class = ""

    if kind == "cover":
        extra_class = "cover"
        inner = (
            '<div class="mark">%s</div>'
            '<p class="modnum">%s</p>'
            '<h1>%s</h1>'
            '<p class="tag">%s</p>'
            '<div class="rule"></div>'
            '<div class="meta">%s</div>'
        ) % (deck["mark"], slide["kicker"], slide["title"], slide["tagline"],
             "<br/>".join(slide["meta"]))

    elif kind == "section":
        extra_class = "section"
        inner = '<p class="step">%s</p><h2>%s</h2>' % (slide["step"], slide["title"])
        if slide.get("note"):
            inner += "<p>%s</p>" % slide["note"]

    elif kind == "statement":
        extra_class = "statement"
        inner = "<blockquote>%s</blockquote>" % slide["text"]
        if slide.get("after"):
            inner += '<p class="after">%s</p>' % slide["after"]

    else:
        head = ""
        if slide.get("eyebrow"):
            head += '<p class="eyebrow">%s</p>' % slide["eyebrow"]
        head += '<h2 class="title">%s</h2>' % slide["title"]
        if slide.get("sub"):
            head += '<p class="sub">%s</p>' % slide["sub"]
        inner = head + '<div class="body">%s</div>' % slide["html"]

    return '<section class="slide %s">%s%s</section>' % (
        extra_class, inner, foot(deck, index, total))


def render_notes(deck, pages):
    out = []
    for page in pages:
        rows = "".join(
            '<div class="row"><div class="sn">%s</div><div class="tx">%s</div></div>'
            % (sn, tx) for sn, tx in page["rows"])
        out.append(
            '<section class="slide notes">'
            '<h2>Guion del instructor</h2>'
            '<p class="lead">%s</p>'
            '<div class="rows">%s</div>'
            '</section>' % (page["lead"], rows))
    return "".join(out)


def build(module_key):
    deck_mod = importlib.import_module("content.decks.%s" % module_key)
    deck = deck_mod.DECK
    slides = deck_mod.SLIDES
    notes = getattr(deck_mod, "NOTES", [])

    with open(os.path.join(HERE, "slides.css"), encoding="utf-8") as fh:
        css = fh.read()

    body = "".join(render_slide(deck, s, i, len(slides))
                   for i, s in enumerate(slides))
    body += render_notes(deck, notes)

    html = (
        '<!doctype html><html lang="es"><head><meta charset="utf-8"/>'
        '<title>%s</title><style>%s\n%s</style></head><body>%s</body></html>'
    ) % (deck["title"], font_faces(), css, body)

    tmp = os.path.join(ROOT, "dist", "_%s.html" % module_key)
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(html)

    pdf = os.path.join(ROOT, "dist", deck["outfile"])
    for stale in glob.glob(pdf):
        os.remove(stale)

    subprocess.run([
        find_chrome(), "--headless=new", "--disable-gpu",
        "--no-pdf-header-footer", "--print-to-pdf-no-header",
        "--virtual-time-budget=8000",
        "--print-to-pdf=%s" % pdf,
        "file:///" + tmp.replace("\\", "/"),
    ], capture_output=True)

    if not os.path.exists(pdf):
        raise SystemExit("Chrome no generó el PDF.")

    os.remove(tmp)
    print("laminas : %d  (+%d de guion)" % (len(slides), len(notes)))
    print("PDF     : %s (%.1f KB)" % (pdf, os.path.getsize(pdf) / 1024))
    return pdf
