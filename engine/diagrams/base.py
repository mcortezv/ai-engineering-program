# -*- coding: utf-8 -*-
"""Primitivas de dibujo y tokens de color compartidos por los diagramas.

Se dibujan con los mismos tokens de color del sistema de HyperLabs. Van
inlineados en el HTML: el PDF tiene que ser reproducible sin red y el vector
se imprime nítido a cualquier tamaño.

Cada función devuelve un <svg> completo con viewBox; la lámina lo escala al
ancho disponible (~1120 unidades ≈ 298 mm).
"""

INK = "#16161a"
INK2 = "#3d3d46"
INK3 = "#6d6d78"
ACC = "#5b3bd6"
ACC_SOFT = "#f1edff"
HAIR = "#d8d8e0"
OK = "#0f7a52"
OK_SOFT = "#e9f5f0"
DANGER = "#b91c1c"
DANGER_SOFT = "#fdecec"
PAPER = "#f7f7fa"

SANS = "Figtree, 'Segoe UI', sans-serif"
MONO = "Consolas, 'SFMono-Regular', monospace"

W = 1120



def _svg(height, body):
    return (
        '<svg viewBox="0 0 %d %d" width="100%%" xmlns="http://www.w3.org/2000/svg" '
        'style="display:block;height:auto">%s</svg>' % (W, height, body))

def _txt(x, y, s, size=19, fill=INK, weight="400", anchor="start", family=SANS,
         spacing=None, opacity=None):
    extra = ""
    if spacing:
        extra += ' letter-spacing="%s"' % spacing
    if opacity:
        extra += ' opacity="%s"' % opacity
    return ('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
            'font-weight="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, family, size, fill, weight, anchor, extra, s))

def _rect(x, y, w, h, fill="none", stroke=HAIR, sw=1.5, r=10, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="%s" '
            'stroke="%s" stroke-width="%s"%s/>' % (x, y, w, h, r, fill, stroke, sw, d))

def _arrow(x1, y1, x2, y2, color=INK3, sw=2, head=True):
    marker = ' marker-end="url(#ah)"' if head else ""
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, color, sw, marker))


DEFS = (
    '<defs>'
    '<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
    'markerHeight="7" orient="auto-start-reverse">'
    '<path d="M 0 0 L 10 5 L 0 10 z" fill="%s"/></marker>'
    '<marker id="ahp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
    'markerHeight="7" orient="auto-start-reverse">'
    '<path d="M 0 0 L 10 5 L 0 10 z" fill="%s"/></marker>'
    '</defs>' % (INK3, ACC)
)


# ---------------------------------------------------------------------------
