# -*- coding: utf-8 -*-
"""Diagramas del módulo 13 — RAG.

La geometría de la similitud coseno se dibuja sobre un plano cartesiano real,
con los mismos números que se hacen en el pizarrón, porque es el punto del
programa donde una figura mal elegida instala un error que dura años.
"""

import math

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def flujo_rag():
    """Las dos fases: una ocurre una vez, la otra en cada consulta."""
    b = [DEFS]

    def fase(y, etiqueta, nota, pasos, color, fill):
        out = [_rect(10, y, 1100, 116, fill=fill, stroke=color, sw=2, r=12)]
        out.append(_txt(34, y + 32, etiqueta, 15, color, "700", spacing="2.2"))
        out.append(_txt(34 + 260, y + 32, nota, 15, INK3, "400"))
        x = 34
        for i, p in enumerate(pasos):
            w = 26 + len(p) * 9.6
            out.append(_rect(x, y + 48, w, 48, fill="#ffffff", stroke=color,
                             sw=1.4, r=8))
            out.append(_txt(x + w / 2.0, y + 78, p, 16, INK, "500", "middle"))
            x += w
            if i < len(pasos) - 1:
                out.append(_arrow(x + 6, y + 72, x + 30, y + 72, INK3, 1.8))
                x += 36
        return "".join(out)

    b.append(fase(14, "INDEXACIÓN", "una vez, y cada vez que cambia el contenido",
                  ["documento", "trocear", "embedding por trozo",
                   "guardar vector + texto"], INK2, "#ffffff"))
    b.append(fase(154, "RECUPERACIÓN", "en cada consulta",
                  ["pregunta", "embedding", "buscar los más parecidos",
                   "recuperar SU TEXTO", "pegarlo en el prompt"], ACC, ACC_SOFT))

    b.append(_txt(10, 312, "El error más común al aprender esto es confundir lo que "
                           "pasa una vez con lo que pasa en cada consulta.",
                  19, INK3, "400"))
    return _svg(332, "".join(b))


def chunking():
    """El compromiso del tamaño, y para qué sirve el solapamiento."""
    b = [DEFS]
    b.append(_txt(10, 32, "TROZOS PEQUEÑOS", 15, ACC, "700", spacing="2.2"))
    for i in range(8):
        b.append(_rect(10 + i * 138, 46, 128, 44, fill=ACC_SOFT, stroke=ACC,
                       sw=1.3, r=6))
    b.append(_txt(10, 112, "recuperación precisa · pero cada trozo puede quedar "
                           "incomprensible sin lo que había alrededor",
                  17, INK3, "400"))

    b.append(_txt(10, 168, "TROZOS GRANDES", 15, INK2, "700", spacing="2.2"))
    for i in range(3):
        b.append(_rect(10 + i * 372, 182, 348, 44, fill="#f1f1f5", stroke=HAIR,
                       sw=1.3, r=6))
    b.append(_txt(10, 248, "contexto de sobra · pero el vector se vuelve un promedio "
                           "difuso y recupera peor, y cada trozo mete más tokens al "
                           "prompt", 17, INK3, "400"))

    b.append(_txt(10, 306, "CON SOLAPAMIENTO", 15, OK, "700", spacing="2.2"))
    for i in range(5):
        x = 10 + i * 208
        b.append(_rect(x, 320, 250, 44, fill=OK_SOFT, stroke=OK, sw=1.3, r=6))
        if i:
            b.append('<rect x="%d" y="320" width="42" height="44" fill="%s" '
                     'opacity=".35"/>' % (x, OK))
    b.append(_txt(10, 386, "las zonas sombreadas se repiten: una idea que cae justo "
                           "en el corte no se pierde", 17, INK3, "400"))
    return _svg(406, "".join(b))


def _plano(ox, oy, unidad, maxx, maxy):
    """Rejilla cartesiana con ejes."""
    out = []
    for i in range(maxx + 1):
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                   'stroke-width="1" opacity=".55"/>'
                   % (ox + i * unidad, oy, ox + i * unidad, oy - maxy * unidad, HAIR))
    for j in range(maxy + 1):
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                   'stroke-width="1" opacity=".55"/>'
                   % (ox, oy - j * unidad, ox + maxx * unidad, oy - j * unidad, HAIR))
    out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
               'stroke-width="2"/>' % (ox, oy, ox + maxx * unidad, oy, INK3))
    out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
               'stroke-width="2"/>' % (ox, oy, ox, oy - maxy * unidad, INK3))
    return "".join(out)


def coseno_geometria():
    """Lo que mide la similitud coseno: la abertura entre dos flechas."""
    b = [DEFS]
    ox, oy, u = 90, 300, 30
    b.append(_plano(ox, oy, u, 9, 8))

    ax, ay = ox + 7 * u, oy - 3 * u
    bx, by = ox + 3 * u, oy - 7 * u
    for (px, py, lab) in ((ax, ay, "A"), (bx, by, "B")):
        b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="3.5" marker-end="url(#ahp)"/>'
                 % (ox, oy, px, py, ACC))
        b.append(_txt(px + 14, py - 4, lab, 24, ACC, "700"))

    r = 62
    a1 = math.atan2(ay - oy, ax - ox)
    a2 = math.atan2(by - oy, bx - ox)
    b.append('<path d="M %.1f %.1f A %d %d 0 0 0 %.1f %.1f" fill="none" '
             'stroke="%s" stroke-width="3"/>'
             % (ox + r * math.cos(a1), oy + r * math.sin(a1), r, r,
                ox + r * math.cos(a2), oy + r * math.sin(a2), DANGER))
    b.append(_txt(ox + 72, oy - 58, "θ", 26, DANGER, "700"))

    b.append(_rect(430, 24, 680, 128, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(458, 62, "LO QUE MIDE", 15, ACC, "700", spacing="2.2"))
    b.append(_txt(458, 104, "La abertura entre las dos flechas.", 26, INK, "700"))
    b.append(_txt(458, 136, "Nada más. Ni dónde acaban, ni cuánto miden.", 18, INK2,
                  "400"))

    b.append(_rect(430, 172, 680, 128, fill="#ffffff", stroke=INK, sw=2, r=12))
    b.append(_txt(458, 210, "EL DETALLE QUE HACE CLIC", 15, INK3, "700",
                  spacing="2.2"))
    b.append(_txt(458, 248, "Alarga una de las flechas todo lo que quieras.", 20,
                  INK, "600"))
    b.append(_txt(458, 280, "El ángulo no cambia.", 22, ACC, "700"))

    b.append(_txt(430, 344, "Cerradas del todo: similitud 1.  ·  Perpendiculares: 0."
                            "  ·  Opuestas: −1.", 19, INK3, "400"))
    return _svg(368, "".join(b))


def coseno_demo():
    """La demostración numérica: alineados y separados a la vez."""
    b = [DEFS]
    ox, oy, u = 70, 300, 26
    b.append(_plano(ox, oy, u, 9, 9))

    ax, ay = ox + 3 * u, oy - 4 * u
    bx, by = ox + 6 * u, oy - 8 * u
    b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width="3.5" marker-end="url(#ahp)"/>' % (ox, oy, bx, by, ACC))
    b.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s"/>' % (ax, ay, DANGER))
    b.append(_txt(ax + 12, ay + 22, "A (3, 4)", 19, DANGER, "700"))
    b.append(_txt(bx + 12, by - 6, "B (6, 8)", 19, ACC, "700"))
    b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width="2.5" stroke-dasharray="5 4"/>' % (ax, ay, bx, by, OK))
    b.append(_txt(ax + 66, ay - 42, "5", 20, OK, "700"))
    b.append(_txt(ox - 4, oy + 26, "0", 16, INK3, "400"))

    b.append(_rect(370, 20, 740, 150, fill=PAPER, stroke=HAIR, sw=1.5, r=11))
    b.append('<rect x="370" y="20" width="5" height="150" rx="2.5" fill="%s"/>' % ACC)
    for j, ln in enumerate([
            "A · B  = 3·6 + 4·8 = 18 + 32 = 50",
            "‖A‖    = √(9 + 16)   = 5",
            "‖B‖    = √(36 + 64)  = 10"]):
        b.append(_txt(400, 58 + j * 34, ln, 20, INK2, "500", family=MONO))
    b.append(_txt(400, 158, "similitud = 50 / (5 · 10)", 20, INK2, "500",
                  family=MONO))

    b.append(_rect(370, 188, 360, 112, fill=ACC_SOFT, stroke=ACC, sw=2, r=11))
    b.append(_txt(398, 226, "SIMILITUD COSENO", 14, ACC, "700", spacing="2"))
    b.append(_txt(398, 276, "1.0", 46, ACC, "700"))
    b.append(_txt(490, 276, "la máxima posible", 17, INK2, "400"))

    b.append(_rect(750, 188, 360, 112, fill=OK_SOFT, stroke=OK, sw=2, r=11))
    b.append(_txt(778, 226, "DISTANCIA EUCLIDIANA", 14, OK, "700", spacing="2"))
    b.append(_txt(778, 276, "5", 46, OK, "700"))
    b.append(_txt(820, 276, "nada cerca", 17, INK2, "400"))

    b.append(_txt(10, 344, "Los mismos dos vectores: alineados del todo y separados "
                           "a la vez. Son dos medidas distintas.", 20, INK, "700"))
    return _svg(368, "".join(b))


def tres_metricas():
    """Las tres métricas de uso habitual."""
    m = [
        ("Similitud coseno", "cosine", "El ángulo: la orientación.", "No",
         "Recuperación de texto en general. El valor por defecto razonable.", ACC),
        ("Producto punto", "dot · inner product · ip",
         "Orientación y magnitud a la vez.", "Sí",
         "Cuando la magnitud codifica algo útil. Es la más barata de calcular.",
         INK2),
        ("Distancia euclidiana", "euclidean · L2", "La separación en línea recta.",
         "Sí", "Cuando la posición absoluta importa. Frecuente fuera del texto.",
         OK),
    ]
    b = [DEFS]
    for t, x in (("MÉTRICA", 30), ("QUÉ MIDE", 350), ("¿MAGNITUD?", 610),
                 ("CUÁNDO CONVIENE", 740)):
        b.append(_txt(x, 32, t, 13, INK3, "700", spacing="1.8"))
    b.append('<line x1="10" y1="44" x2="1110" y2="44" stroke="%s" '
             'stroke-width="1.5"/>' % INK3)
    for i, (nombre, slug, mide, mag, cuando, color) in enumerate(m):
        y = 56 + i * 82
        if i % 2 == 1:
            b.append('<rect x="10" y="%d" width="1100" height="78" rx="8" '
                     'fill="#fbfbfd"/>' % y)
        b.append(_txt(30, y + 34, nombre, 19, color, "700"))
        b.append(_txt(30, y + 60, slug, 15, INK3, "500", family=MONO))
        b.append(_txt(350, y + 44, mide, 17, INK2, "400"))
        b.append(_txt(610, y + 44, mag, 19, DANGER if mag == "Sí" else OK, "700"))
        words, line, lines = cuando.split(), "", []
        for w in words:
            if len(line + " " + w) > 40:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(740, y + 34 + j * 22, ln, 16, INK2, "400"))

    y = 56 + len(m) * 82
    b.append(_rect(10, y + 12, 1100, 92, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, y + 50, "Si los vectores están normalizados a longitud 1, las "
                              "tres ordenan igual.", 21, INK, "700"))
    b.append(_txt(38, y + 82, "El producto punto ES la similitud coseno, y la "
                              "distancia produce el mismo orden. La elección deja de "
                              "afectar a qué recuperas.", 17, INK2, "400"))
    return _svg(y + 126, "".join(b))


def umbral():
    """Por qué no existe un umbral universal."""
    b = [DEFS]
    b.append(_txt(10, 30, "PUNTAJES DE 40 RESULTADOS REALES", 15, INK3, "700",
                  spacing="2.2"))
    ox, oy, w = 40, 250, 1040
    b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="1.8"/>' % (ox, oy, ox + w, oy, INK3))
    for i in range(6):
        x = ox + i * w / 5.0
        b.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                 'stroke-width="1.5"/>' % (x, oy, x, oy + 8, INK3))
        b.append(_txt(x, oy + 30, "%.1f" % (0.5 + i * 0.1), 16, INK3, "400",
                      "middle", family=MONO))

    import random
    rnd = random.Random(7)
    for _ in range(26):
        s = rnd.uniform(0.52, 0.79)
        x = ox + (s - 0.5) * w / 0.5
        b.append('<circle cx="%.1f" cy="%.1f" r="6" fill="%s" opacity=".7"/>'
                 % (x, oy - 26 - rnd.uniform(0, 58), INK3))
    for _ in range(9):
        s = rnd.uniform(0.81, 0.96)
        x = ox + (s - 0.5) * w / 0.5
        b.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s"/>'
                 % (x, oy - 26 - rnd.uniform(0, 58), OK))

    xc = ox + (0.80 - 0.5) * w / 0.5
    b.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
             'stroke-width="2.5" stroke-dasharray="7 5"/>' % (xc, 58, xc, oy, ACC))
    b.append(_txt(xc + 14, 76, "tu corte, calibrado", 17, ACC, "700"))

    b.append('<circle cx="40" cy="300" r="6" fill="%s" opacity=".7"/>' % INK3)
    b.append(_txt(56, 306, "no era relevante", 17, INK3, "400"))
    b.append('<circle cx="260" cy="300" r="7" fill="%s"/>' % OK)
    b.append(_txt(276, 306, "sí era relevante", 17, OK, "600"))

    b.append(_rect(10, 330, 1100, 88, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(38, 366, "Dos textos sin relación rara vez dan cero: pueden dar "
                           "0.6 o 0.7.", 20, INK, "700"))
    b.append(_txt(38, 398, "Copiar «recuperamos todo lo que supere 0.75» de un "
                           "tutorial es una de las causas más comunes de un RAG que "
                           "devuelve basura con aparente confianza.", 18, INK2,
                  "400"))
    return _svg(438, "".join(b))


def reranking():
    """Recuperar mucho y quedarse con poco."""
    b = [DEFS]
    b.append(_rect(10, 40, 300, 180, fill="#ffffff", stroke=HAIR, sw=1.5, r=11))
    b.append(_txt(38, 76, "BÚSQUEDA VECTORIAL", 14, INK3, "700", spacing="2"))
    b.append(_txt(38, 132, "50", 48, INK2, "700"))
    b.append(_txt(110, 132, "candidatos", 20, INK2, "400"))
    b.append(_txt(38, 172, "barata y aproximada", 17, INK3, "400"))
    b.append(_txt(38, 200, "ordena más o menos bien", 17, INK3, "400"))

    b.append(_arrow(322, 130, 388, 130, ACC, 2.5))

    b.append(_rect(400, 40, 300, 180, fill=ACC, stroke="none", sw=0, r=11))
    b.append(_txt(428, 76, "REORDENAMIENTO", 14, "#d9ccff", "700", spacing="2"))
    b.append(_txt(428, 132, "evalúa", 34, "#ffffff", "700"))
    b.append(_txt(428, 168, "cada par consulta-documento", 17, "#d9ccff", "400"))
    b.append(_txt(428, 196, "con mucha más precisión", 17, "#d9ccff", "400"))

    b.append(_arrow(712, 130, 778, 130, ACC, 2.5))

    b.append(_rect(790, 40, 320, 180, fill=OK_SOFT, stroke=OK, sw=2, r=11))
    b.append(_txt(818, 76, "AL PROMPT", 14, OK, "700", spacing="2"))
    b.append(_txt(818, 132, "5", 48, OK, "700"))
    b.append(_txt(858, 132, "trozos", 20, INK2, "400"))
    b.append(_txt(818, 172, "los que de verdad", 17, INK3, "400"))
    b.append(_txt(818, 200, "responden la pregunta", 17, INK3, "400"))

    b.append(_rect(10, 248, 1100, 92, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, 286, "Recuperar menos y mejor baja el costo y sube la calidad "
                           "al mismo tiempo.", 21, INK, "700"))
    b.append(_txt(38, 318, "Es de las poquísimas optimizaciones que no tienen "
                           "contrapartida: cuesta más por consulta que la búsqueda, "
                           "y mucho menos que meter 50 trozos en el prompt.",
                  18, INK2, "400"))
    return _svg(360, "".join(b))
