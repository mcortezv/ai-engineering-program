# -*- coding: utf-8 -*-
"""Marcas de proveedor.

Los SVG salen de simple-icons (CC0). OpenAI no esta en ese paquete: la
retiraron a peticion de la propia empresa. Para esa y para cualquier otra
que falte se dibuja un monograma tipografico, nunca una imitacion.
"""

import os
import re

from engine.diagrams.base import INK, _txt

# Los iconos los instala npm; ver package.json y `npm install`.
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ICON_DIR = os.path.join(_ROOT, "node_modules", "simple-icons", "icons")
_CACHE = {}


def icon_path(slug):
    """Devuelve el `d` del path SVG de la marca, o None si no está disponible."""
    if slug not in _CACHE:
        f = os.path.join(_ICON_DIR, "%s.svg" % slug)
        d = None
        if os.path.exists(f):
            with open(f, encoding="utf-8") as fh:
                m = re.search(r'\sd="([^"]+)"', fh.read())
            d = m.group(1) if m else None
        _CACHE[slug] = d
    return _CACHE[slug]


def _mark(slug, monograma, cx, cy, size, color=INK):
    """Marca oficial centrada en (cx, cy). Si no existe, monograma en círculo."""
    d = icon_path(slug) if slug else None
    if d:
        return ('<g transform="translate(%.2f,%.2f) scale(%.4f)">'
                '<path d="%s" fill="%s"/></g>'
                % (cx - size / 2.0, cy - size / 2.0, size / 24.0, d, color))
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" '
            'stroke-width="1.8"/>%s'
            % (cx, cy, size / 2.0, color,
               _txt(cx, cy + size * 0.23, monograma, size * 0.52, color, "700",
                    "middle")))


# ── Módulo 2 ────────────────────────────────────────────────────────────────

