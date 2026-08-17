# -*- coding: utf-8 -*-
"""Diagramas del modulo 1 - Introduccion."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3,
    MONO, OK, OK_SOFT, PAPER, SANS, W, _arrow, _rect, _svg, _txt,
)



def tres_formas():
    """Determinista, heurística y aprendizaje: qué se delega en cada una."""
    b = [DEFS]
    cols = [
        ("PROGRAMACIÓN DETERMINISTA",
         "Conoces todos los parámetros\ny existe una operación exacta.",
         "Convertir °C a °F", "La regla la escribes tú", INK2, "#ffffff"),
        ("HEURÍSTICA",
         "No conoces todos los parámetros,\npero puedes diseñar un criterio.",
         "Marcar spam con reglas", "La regla la escribes tú", INK2, "#ffffff"),
        ("APRENDIZAJE AUTOMÁTICO",
         "No hay una regla que nadie\nsepa escribir a mano.",
         "Marcar spam con 100 000 ejemplos",
         "La regla la encuentra el entrenamiento", ACC, ACC_SOFT),
    ]
    for i, (t, d, ej, quien, color, fill) in enumerate(cols):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 252, fill=fill,
                       stroke=color if fill != "#ffffff" else HAIR,
                       sw=2 if fill != "#ffffff" else 1.5, r=12))
        b.append(_txt(x + 24, 48, t, 14, color, "700", spacing="1.6"))
        for j, line in enumerate(d.split("\n")):
            b.append(_txt(x + 24, 82 + j * 26, line, 18, INK, "400"))
        b.append('<line x1="%d" y1="150" x2="%d" y2="150" stroke="%s" '
                 'stroke-width="1"/>' % (x + 24, x + 324, HAIR))
        b.append(_txt(x + 24, 178, "EJEMPLO", 13, INK3, "700", spacing="1.6"))
        b.append(_txt(x + 24, 204, ej, 17, INK2, "600"))
        b.append(_txt(x + 24, 242, quien, 16, color, "700"))

    b.append('<path d="M 30 300 L 1088 300" stroke="%s" stroke-width="2" '
             'marker-end="url(#ahp)"/>' % ACC)
    b.append(_txt(30, 290, "sabes cada vez menos del problema", 17, INK3, "400"))
    b.append(_txt(1088, 290, "delegas cada vez más", 17, ACC, "700", "end"))
    b.append(_txt(560, 344, "Lo que se delega en el tercer caso no es el cálculo: "
                            "es el diseño de la regla.", 20, INK, "700", "middle"))
    return _svg(366, "".join(b))


def tradicional_generativa():
    """La diferencia práctica está en el tipo de salida."""
    b = [DEFS]

    def panel(x, titulo, entrada, salidas, color, fill):
        out = [_rect(x, 14, 528, 250, fill=fill,
                     stroke=color, sw=2, r=14)]
        out.append(_txt(x + 28, 50, titulo, 15, color, "700", spacing="2.2"))
        out.append(_rect(x + 28, 72, 180, 52, fill="#ffffff", stroke=HAIR, sw=1.5,
                         r=8))
        out.append(_txt(x + 118, 104, entrada, 18, INK2, "500", "middle"))
        out.append(_arrow(x + 216, 98, x + 268, 98, color, 2.5))
        for j, s in enumerate(salidas):
            out.append(_rect(x + 276, 72 + j * 62, 224, 52, fill="#ffffff",
                             stroke=color, sw=1.5, r=8))
            out.append(_txt(x + 388, 104 + j * 62, s, 18, INK, "600", "middle"))
        return "".join(out)

    b.append(panel(10, "AI TRADICIONAL", "una imagen",
                   ["«gato»", "87 % de probabilidad"], INK2, "#ffffff"))
    b.append(panel(582, "AI GENERATIVA", "una instrucción",
                   ["un texto nuevo", "que no estaba en los datos"], ACC, ACC_SOFT))
    b.append(_txt(274, 218, "elige entre opciones", 17, INK3, "400", "middle"))
    b.append(_txt(846, 218, "construye algo", 17, ACC, "600", "middle"))
    b.append(_rect(10, 286, 1100, 72, fill="#fbfbfd", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(38, 320, "Lo generativo no sustituyó a lo tradicional: conviven.",
                  20, INK, "700"))
    b.append(_txt(38, 346, "Un clasificador barato decide el enrutamiento y solo lo "
                           "que lo necesita llega al modelo generativo, que es "
                           "órdenes de magnitud más caro.", 17, INK3, "400"))
    return _svg(376, "".join(b))


# ── Módulo 3 ────────────────────────────────────────────────────────────────

