# -*- coding: utf-8 -*-
"""Diagramas del módulo 12 — Embeddings.

Es el módulo con lo más difícil de imaginar del programa, así que casi todo se
resuelve con figuras: primero dos ejes que sí se pueden dibujar, después tres,
y solo entonces el salto a las que no se ven.
"""

import math

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def plano_2d():
    """La intuición completa en un espacio de dos ejes inventados."""
    b = [DEFS]
    ox, oy, size = 90, 320, 280
    b.append(_arrow(ox, oy, ox, oy - size - 20, INK3, 2))
    b.append(_arrow(ox, oy, ox + size + 400, oy, INK3, 2))
    b.append(_txt(ox - 12, oy - size - 26, "tiene que ver con ANIMALES", 15, INK3,
                  "700"))
    b.append(_txt(ox + size + 250, oy + 28, "tiene que ver con TECNOLOGÍA", 15,
                  INK3, "700"))

    puntos = [
        ("perro", .10, .88, ACC), ("gato", .18, .80, ACC),
        ("veterinario", .30, .62, ACC),
        ("servidor", .84, .26, INK2), ("router", .96, .12, INK2),
        ("centro de datos", .66, .05, INK2),
        ("ratón", .52, .50, DANGER),
    ]
    for nombre, fx, fy, color in puntos:
        x = ox + fx * (size + 380)
        y = oy - fy * size
        b.append('<circle cx="%.1f" cy="%.1f" r="8" fill="%s"/>' % (x, y, color))
        b.append(_txt(x + 15, y + 6, nombre, 19, color, "600"))

    # el ambiguo
    b.append('<circle cx="%.1f" cy="%.1f" r="26" fill="none" stroke="%s" '
             'stroke-width="1.6" stroke-dasharray="5 4"/>'
             % (ox + .52 * (size + 380), oy - .50 * size, DANGER))

    b.append(_rect(700, 40, 410, 150, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(728, 78, "LO QUE HAY QUE VER AQUÍ", 15, ACC, "700", spacing="2.2"))
    b.append(_txt(728, 112, "La posición codifica significado.", 19, INK, "700"))
    b.append(_txt(728, 142, "La cercanía codifica parecido.", 19, INK, "700"))
    b.append(_txt(728, 174, "«ratón» cae en medio: es ambiguo.", 17, DANGER, "600"))
    return _svg(360, "".join(b))


def subir_dimensiones():
    """De dos ejes a los que no se pueden dibujar."""
    b = [DEFS]

    # 2D
    b.append(_rect(10, 14, 348, 260, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(38, 50, "2 DIMENSIONES", 15, INK3, "700", spacing="2"))
    b.append(_arrow(60, 230, 60, 90, INK3, 1.8))
    b.append(_arrow(60, 230, 320, 230, INK3, 1.8))
    for fx, fy, c in ((.25, .70, ACC), (.35, .60, ACC), (.80, .20, INK3)):
        b.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s"/>'
                 % (60 + fx * 250, 230 - fy * 135, c))
    b.append(_txt(38, 262, "se dibuja sin problema", 17, INK2, "400"))

    # 3D
    b.append(_rect(382, 14, 348, 260, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(410, 50, "3 DIMENSIONES", 15, INK3, "700", spacing="2"))
    b.append(_arrow(450, 230, 450, 92, INK3, 1.8))
    b.append(_arrow(450, 230, 700, 230, INK3, 1.8))
    b.append(_arrow(450, 230, 372 + 190, 230 - 78, INK3, 1.8))
    for fx, fy, fz, c in ((.30, .60, .2, ACC), (.42, .48, .3, ACC),
                          (.78, .22, .1, INK3)):
        x = 450 + fx * 240 + fz * 70
        y = 230 - fy * 130 - fz * 40
        b.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s"/>' % (x, y, c))
    b.append(_txt(410, 262, "todavía se puede dibujar, con esfuerzo", 17, INK2,
                  "400"))

    # N-D
    b.append(_rect(754, 14, 356, 260, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(782, 50, "1 536 DIMENSIONES", 15, ACC, "700", spacing="2"))
    for i, v in enumerate(["0.0231", "−0.4417", "0.1893", "0.0072", "−0.2264",
                           "0.3310", "−0.0918", "0.1247", "…"]):
        b.append(_txt(782 + (i % 3) * 108, 100 + (i // 3) * 40, v, 19, ACC, "500",
                      family=MONO))
    b.append(_txt(782, 234, "no se dibuja, y no hace falta", 19, INK, "700"))
    b.append(_txt(782, 262, "existe igual y opera igual", 17, INK2, "400"))

    b.append(_rect(10, 300, 1100, 66, fill="#ffffff", stroke=INK, sw=2, r=11))
    b.append(_txt(560, 342, "Distancia, ángulo y magnitud se calculan igual con dos "
                            "ejes que con mil quinientos.", 21, INK, "700",
                  "middle"))
    return _svg(386, "".join(b))


def generar_embedding():
    """El texto entra a un modelo específico y sale un vector."""
    b = [DEFS]
    b.append(_rect(10, 60, 250, 96, fill="#ffffff", stroke=HAIR, sw=1.5, r=11))
    b.append(_txt(135, 100, "«política de", 19, INK, "500", "middle"))
    b.append(_txt(135, 126, "reembolsos…»", 19, INK, "500", "middle"))
    b.append(_txt(135, 178, "un párrafo entero", 16, INK3, "400", "middle"))
    b.append(_arrow(268, 108, 328, 108, INK3, 2))

    b.append(_rect(336, 48, 300, 120, fill=ACC, stroke="none", sw=0, r=12))
    b.append(_txt(486, 92, "MODELO DE", 15, "#d9ccff", "700", "middle",
                  spacing="2"))
    b.append(_txt(486, 122, "EMBEDDINGS", 22, "#ffffff", "700", "middle"))
    b.append(_txt(486, 150, "distinto del generativo", 15, "#d9ccff", "400",
                  "middle"))
    b.append(_arrow(644, 108, 704, 108, INK3, 2))

    b.append(_rect(712, 60, 398, 96, fill=PAPER, stroke=ACC, sw=1.5, r=11))
    b.append(_txt(736, 96, "[0.023, −0.441, 0.189, …]", 20, ACC, "500",
                  family=MONO))
    b.append(_txt(736, 134, "un vector, siempre del mismo tamaño", 16, INK3, "400"))

    props = [
        ("No es una tabla de consulta", "no hay un diccionario de palabra a vector"),
        ("Es determinista", "el mismo texto da siempre el mismo vector"),
        ("Es barato", "órdenes de magnitud menos que generar texto"),
    ]
    for i, (t, d) in enumerate(props):
        x = 10 + i * 372
        b.append(_rect(x, 204, 348, 86, fill="#ffffff", stroke=HAIR, sw=1.5, r=10))
        b.append(_txt(x + 24, 240, t, 19, INK, "700"))
        b.append(_txt(x + 24, 268, d, 16, INK3, "400"))
    return _svg(310, "".join(b))


def espacios_incompatibles():
    """Cada modelo define su propio espacio."""
    b = [DEFS]

    def espacio(x0, titulo, color, fill, semilla):
        out = [_rect(x0, 14, 500, 248, fill=fill, stroke=color, sw=2, r=12)]
        out.append(_txt(x0 + 28, 50, titulo, 15, color, "700", spacing="2.2"))
        pos = [(.22, .30), (.34, .52), (.58, .24), (.72, .66), (.46, .78)]
        etiquetas = ["gato", "perro", "router", "factura", "cliente"]
        for i, ((fx, fy), lab) in enumerate(zip(pos, etiquetas)):
            fx = (fx * 3 + semilla * (i + 1) * 0.11) % 0.86 + 0.06
            fy = (fy * 2 + semilla * (i + 2) * 0.17) % 0.74 + 0.10
            x, y = x0 + 30 + fx * 440, 76 + fy * 168
            out.append('<circle cx="%.1f" cy="%.1f" r="6" fill="%s"/>' % (x, y, color))
            out.append(_txt(x + 12, y + 5, lab, 16, INK2, "400"))
        return "".join(out)

    b.append(espacio(10, "MODELO DE EMBEDDINGS A", ACC, ACC_SOFT, 0.31))
    b.append(espacio(610, "MODELO DE EMBEDDINGS B", OK, OK_SOFT, 0.77))
    b.append('<line x1="540" y1="40" x2="540" y2="236" stroke="%s" '
             'stroke-width="2" stroke-dasharray="6 5"/>' % DANGER)
    b.append(_rect(10, 284, 1100, 88, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(38, 320, "Los vectores de dos modelos no son comparables, aunque "
                           "tengan el mismo número de dimensiones.", 20, INK,
                  "700"))
    b.append(_txt(38, 352, "Mezclarlos no da error: da resultados sin sentido, en "
                           "silencio. Y cambiar de modelo obliga a reprocesar todo "
                           "el corpus.", 18, INK2, "400"))
    return _svg(392, "".join(b))


def tres_operaciones():
    """Magnitud, distancia y ángulo sobre los mismos dos vectores."""
    b = [DEFS]
    ox, oy = 120, 300
    ax, ay = ox + 250, oy - 190
    bx, by = ox + 330, oy - 70

    # ejes
    b.append(_arrow(ox, oy, ox, oy - 250, HAIR, 1.6))
    b.append(_arrow(ox, oy, ox + 420, oy, HAIR, 1.6))

    # vectores
    b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3" '
             'marker-end="url(#ahp)"/>' % (ox, oy, ax, ay, ACC))
    b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3" '
             'marker-end="url(#ahp)"/>' % (ox, oy, bx, by, ACC))
    b.append(_txt(ax - 16, ay - 14, "A", 24, ACC, "700"))
    b.append(_txt(bx + 14, by + 8, "B", 24, ACC, "700"))

    # distancia entre puntas
    b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" '
             'stroke-dasharray="6 5"/>' % (ax, ay, bx, by, OK))
    b.append(_txt((ax + bx) / 2 + 18, (ay + by) / 2, "distancia", 17, OK, "700"))

    # arco del angulo
    r = 78
    a1 = math.atan2(ay - oy, ax - ox)
    a2 = math.atan2(by - oy, bx - ox)
    b.append('<path d="M %.1f %.1f A %d %d 0 0 1 %.1f %.1f" fill="none" '
             'stroke="%s" stroke-width="2.5"/>'
             % (ox + r * math.cos(a1), oy + r * math.sin(a1), r, r,
                ox + r * math.cos(a2), oy + r * math.sin(a2), DANGER))
    b.append(_txt(ox + 96, oy - 96, "ángulo", 17, DANGER, "700"))

    ops = [
        ("MAGNITUD", "¿Qué tan largo es?",
         "Depende de la longitud del texto. Casi nunca interesa.", ACC),
        ("DISTANCIA", "¿Qué tan separadas están las puntas?",
         "En línea recta. Es sensible a la magnitud.", OK),
        ("ÁNGULO", "¿Apuntan en la misma dirección?",
         "Ignora la magnitud por completo.", DANGER),
    ]
    for i, (t, pregunta, nota, color) in enumerate(ops):
        y = 40 + i * 100
        b.append(_rect(600, y, 510, 86, fill="#ffffff", stroke=color, sw=2, r=11))
        b.append(_txt(628, y + 32, t, 15, color, "700", spacing="2.2"))
        b.append(_txt(628, y + 58, pregunta, 19, INK, "600"))
        b.append(_txt(628, y + 78, nota, 15, INK3, "400"))

    b.append(_txt(10, 360, "Son tres preguntas distintas sobre los mismos dos "
                           "vectores, y pueden dar respuestas distintas.",
                  20, INK, "700"))
    return _svg(384, "".join(b))


def no_editable():
    """Cambiar una palabra obliga a regenerar el vector entero."""
    b = [DEFS]
    b.append(_rect(10, 20, 500, 110, fill="#ffffff", stroke=HAIR, sw=1.5, r=11))
    b.append(_txt(38, 60, "«devolución en 30 días»", 21, INK, "500"))
    b.append(_txt(38, 100, "[0.023, −0.441, 0.189, …]", 18, ACC, "500",
                  family=MONO))

    b.append(_arrow(255, 148, 255, 186, DANGER, 2.5))
    b.append(_txt(275, 174, "cambias una palabra", 17, DANGER, "700"))

    b.append(_rect(10, 200, 500, 110, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=11))
    b.append(_txt(38, 240, "«devolución en 15 días»", 21, INK, "500"))
    b.append(_txt(38, 280, "[0.019, −0.402, 0.204, …]", 18, DANGER, "500",
                  family=MONO))
    b.append(_txt(38, 306, "vector nuevo, entero", 15, DANGER, "700"))

    b.append(_rect(570, 20, 540, 290, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(598, 58, "LO QUE ESTO OBLIGA A CONSTRUIR", 15, ACC, "700",
                  spacing="2.2"))
    for j, (t, d) in enumerate([
            ("No se editan los números a mano",
             "el vector se produce pasando el texto por el modelo"),
            ("Todo contenido que cambia necesita reproceso",
             "y eso es un costo recurrente, no de arranque"),
            ("Conviene detectar qué cambió de verdad",
             "regenerar solo lo modificado, no el corpus entero")]):
        y = 98 + j * 72
        b.append('<circle cx="614" cy="%d" r="5" fill="%s"/>' % (y - 6, ACC))
        b.append(_txt(632, y, t, 18, INK, "700"))
        b.append(_txt(632, y + 24, d, 16, INK3, "400"))
    return _svg(330, "".join(b))
