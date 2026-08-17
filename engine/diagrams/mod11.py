# -*- coding: utf-8 -*-
"""Diagramas del módulo 11 — Bases de datos para sistemas de AI."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def lexico_falla():
    """La consulta y el documento correcto no comparten ni una palabra."""
    b = [DEFS]
    consulta = ["cómo", "devuelvo", "un", "producto"]
    documento = ["política", "de", "reembolsos"]

    b.append(_txt(10, 34, "LO QUE ESCRIBE EL USUARIO", 14, INK3, "700",
                  spacing="2"))
    x = 10
    for w in consulta:
        wd = 24 + len(w) * 14
        b.append(_rect(x, 50, wd, 48, fill="#f1f1f5", stroke=HAIR, sw=1.3, r=7))
        b.append(_txt(x + wd / 2.0, 81, w, 20, INK2, "500", "middle"))
        x += wd + 8

    b.append(_txt(10, 152, "EL DOCUMENTO QUE RESPONDE SU PREGUNTA", 14, OK, "700",
                  spacing="2"))
    x = 10
    for w in documento:
        wd = 24 + len(w) * 14
        b.append(_rect(x, 168, wd, 48, fill=OK_SOFT, stroke=OK, sw=1.3, r=7))
        b.append(_txt(x + wd / 2.0, 199, w, 20, INK, "600", "middle"))
        x += wd + 8

    b.append(_rect(620, 44, 490, 178, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(650, 84, "PALABRAS EN COMÚN", 15, DANGER, "700", spacing="2.2"))
    b.append(_txt(650, 146, "cero", 46, DANGER, "700"))
    b.append(_txt(650, 186, "Una búsqueda por coincidencia de texto", 17, INK2,
                  "400"))
    b.append(_txt(650, 210, "no devuelve nada. Y el documento existe.", 17, INK2,
                  "400"))

    b.append(_txt(10, 268, "El problema no es de velocidad: es de criterio de "
                           "coincidencia. Por eso ningún índice tradicional lo "
                           "arregla.", 19, INK3, "400"))
    return _svg(288, "".join(b))


def tipos_db():
    """Tres formas de almacenar, tres preguntas distintas."""
    tipos = [
        ("RELACIONAL", "¿Cuál es el registro con este identificador?",
         "Rápida, exacta, transaccional y barata.",
         "Recuperar el pedido 4821. Insuperable.", INK2, "#ffffff"),
        ("GRAFOS", "¿Qué está conectado con qué, y a cuántos saltos?",
         "El camino recorrido es legible, así que la recuperación se puede "
         "explicar.",
         "Qué áreas dependen de este proveedor.", OK, OK_SOFT),
        ("VECTORIAL", "¿Qué se parece a esto, aunque esté dicho con otras "
                      "palabras?",
         "Recupera por significado, no por coincidencia de texto.",
         "Qué documento responde esta pregunta.", ACC, ACC_SOFT),
    ]
    b = [DEFS]
    for i, (t, pregunta, fuerte, ej, color, fill) in enumerate(tipos):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 272, fill=fill, stroke=color, sw=2, r=12))
        b.append(_txt(x + 24, 50, t, 15, color, "700", spacing="2.2"))
        words, line, lines = pregunta.split(), "", []
        for w in words:
            if len(line + " " + w) > 26:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(x + 24, 90 + j * 28, ln, 20, INK, "700"))
        yy = 90 + len(lines) * 28 + 8
        b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                 'stroke-width="1"/>' % (x + 24, yy, x + 324, yy, color))
        words, line, lines = fuerte.split(), "", []
        for w in words:
            if len(line + " " + w) > 36:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(x + 24, yy + 30 + j * 24, ln, 16, INK2, "400"))
        b.append(_txt(x + 24, 262, ej, 16, color, "600"))

    b.append(_txt(560, 320, "No es una evolución en la que cada una sustituye a la "
                            "anterior: en un sistema real conviven.",
                  20, INK, "700", "middle"))
    return _svg(340, "".join(b))


def aislamiento():
    """Los tres niveles de aislamiento de datos."""
    b = [DEFS]
    niveles = [
        ("espacio de trabajo", "Los datos de un cliente nunca se mezclan con los "
                               "de otro.", "requisito de seguridad", 10, 1100, ACC),
        ("usuario", "Lo que sabemos de esta persona en concreto.",
         "memoria persistente", 90, 940, INK2),
        ("sesión", "Esta conversación, de principio a fin.",
         "reconstruir y depurar", 170, 780, INK3),
    ]
    for i, (t, d, nota, x, w, color) in enumerate(niveles):
        y = 20 + i * 88
        b.append(_rect(x, y, w, 76, fill="#ffffff" if i else ACC_SOFT,
                       stroke=color, sw=2 if i == 0 else 1.5, r=11))
        b.append(_txt(x + 26, y + 32, t, 20, color, "700"))
        b.append(_txt(x + 26, y + 58, d, 17, INK2, "400"))
        b.append(_txt(x + w - 26, y + 45, nota, 15, INK3, "600", "end"))

    b.append(_txt(10, 314, "Añadir el aislamiento por cliente después obliga a "
                           "migrar todo lo que ya guardaste. Es de las decisiones "
                           "que hay que tomar el primer día.", 19, INK3, "400"))
    return _svg(334, "".join(b))
