# -*- coding: utf-8 -*-
"""Diagramas del modulo 3 - Tokens y ventana de contexto."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3,
    MONO, OK, OK_SOFT, PAPER, SANS, W, _arrow, _rect, _svg, _txt,
)



def tokenizacion():
    """El mismo significado, partido en tokens en dos idiomas."""
    b = [DEFS]

    def fila(y, etiqueta, piezas, color):
        out = [_txt(10, y - 12, etiqueta, 15, INK3, "700", spacing="2")]
        x = 10
        for p in piezas:
            w = 24 + len(p) * 13
            out.append(_rect(x, y, w, 48, fill=ACC_SOFT if color == ACC else "#f1f1f5",
                             stroke=color, sw=1.5, r=6))
            out.append(_txt(x + w / 2.0, y + 31, p.replace(" ", "·"), 18, INK,
                            "500", "middle", family=MONO))
            x += w + 7
        out.append(_txt(x + 16, y + 31, "%d tokens" % len(piezas), 21, color, "700",
                        family=MONO))
        return "".join(out)

    b.append(fila(44, "ESPAÑOL", ["El", " mur", "cié", "la", "go", " voló"], ACC))
    b.append(fila(146, "INGLÉS", ["The", " bat", " flew"], INK3))
    b.append(_rect(10, 222, 1100, 96, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, 258, "El mismo significado cuesta el doble en español.", 22,
                  INK, "700"))
    b.append(_txt(38, 288, "Los vocabularios se entrenaron sobre todo con inglés.",
                  19, INK2, "400"))
    b.append(_txt(38, 312, "Consecuencia directa: el mismo producto es más caro de "
                           "operar en español.", 19, INK2, "400"))
    return _svg(348, "".join(b))


def ventana_contexto():
    """Qué ocupa realmente la ventana de contexto."""
    partes = [
        ("System prompt", 8, "#6f52dd"),
        ("Definiciones de herramientas", 14, "#8a70e6"),
        ("Historial de la conversación", 34, ACC),
        ("Contexto recuperado", 22, "#a892ee"),
        ("Resultados de herramientas", 12, "#c4b6f4"),
        ("La respuesta que va a generar", 10, "#ded6fa"),
    ]
    b = [DEFS]
    b.append(_txt(10, 32, "TODO ESTO COMPARTE EL MISMO ESPACIO", 15, INK3, "700",
                  spacing="2.2"))
    x = 10.0
    for nombre, pct, color in partes:
        w = 1100 * pct / 100.0
        b.append('<rect x="%.1f" y="50" width="%.1f" height="76" fill="%s"/>'
                 % (x, w, color))
        b.append(_txt(x + w / 2.0, 96, "%d%%" % pct, 20,
                      "#ffffff" if pct >= 12 else INK2, "700", "middle"))
        x += w
    b.append(_rect(10, 50, 1100, 76, fill="none", stroke=INK, sw=2, r=0))

    for i, (nombre, pct, color) in enumerate(partes):
        px = 10 + (i % 3) * 372
        py = 158 + (i // 3) * 40
        b.append('<rect x="%d" y="%d" width="20" height="20" rx="4" fill="%s"/>'
                 % (px, py, color))
        b.append(_txt(px + 30, py + 16, nombre, 18, INK2, "400"))

    b.append(_txt(10, 272, "La pregunta del usuario es la parte pequeña. Casi todo "
                           "el espacio lo ocupa lo que tú decidiste meter.",
                  19, INK3, "400"))
    return _svg(292, "".join(b))


def fallos_contexto():
    """Tres cosas distintas pasan cuando el contexto se llena."""
    casos = [
        ("Se excede el límite duro", "La API devuelve un error.",
         "La petición falla. No hay degradación elegante.",
         "#b91c1c", "#fdecec", "RUIDOSO"),
        ("Truncas el historial", "El sistema descarta mensajes viejos.",
         "El modelo no lo sabe: actúa como si nunca hubieran existido.",
         "#8a5a06", "#fbf3e3", "INVISIBLE"),
        ("Lo llenas de ruido", "Funciona y cuesta más.",
         "La calidad baja: lo útil queda diluido. Es el fallo más caro.",
         ACC, ACC_SOFT, "SILENCIOSO"),
    ]
    b = [DEFS]
    for i, (t, q, d, color, fill, etiqueta) in enumerate(casos):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 250, fill=fill, stroke=color, sw=2, r=12))
        b.append(_txt(x + 24, 48, etiqueta, 14, color, "700", spacing="1.8"))
        b.append(_txt(x + 24, 90, t, 21, INK, "700"))
        b.append(_txt(x + 24, 128, q, 18, INK2, "600"))
        words, line, lines = d.split(), "", []
        for w in words:
            if len(line + " " + w) > 34:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(x + 24, 168 + j * 26, ln, 17, INK3, "400"))
    b.append(_txt(560, 306, "El tercero no da error y no se ve en ninguna métrica. "
                            "Por eso es el que más dinero cuesta.",
                  20, INK, "700", "middle"))
    return _svg(326, "".join(b))


def vocabulario_finito():
    """El vocabulario es una lista cerrada, y cada pieza es un número."""
    b = [DEFS]
    b.append(_txt(10, 34, "UNA PALABRA, LAS PIEZAS QUE LA FORMAN Y SU NÚMERO EN LA "
                          "LISTA", 15, INK3, "700", spacing="2.2"))

    b.append(_rect(10, 50, 250, 58, fill="#ffffff", stroke=HAIR, sw=1.5, r=9))
    b.append(_txt(135, 88, "satisfacción", 23, INK, "600", "middle"))
    b.append(_arrow(270, 79, 316, 79, INK3, 2))

    piezas = [("sat", "13 802"), ("is", "271"), ("f", "69"), ("acción", "9 402")]
    x = 332
    for pieza, indice in piezas:
        w = 44 + len(pieza) * 15
        b.append(_rect(x, 50, w, 58, fill=ACC_SOFT, stroke=ACC, sw=1.5, r=9))
        b.append(_txt(x + w / 2.0, 88, pieza, 21, INK, "600", "middle",
                      family=MONO))
        b.append(_txt(x + w / 2.0, 138, indice, 19, ACC, "700", "middle",
                      family=MONO))
        x += w + 16

    b.append(_txt(332, 176, "Lo que entra al modelo son esos cuatro números. Las "
                            "letras se quedan fuera.", 18, INK2, "400"))
    b.append(_txt(332, 202, "«acción» es una pieza por sí sola, y por eso aparece "
                            "dentro de otras palabras.", 18, INK3, "400"))

    b.append(_rect(10, 234, 540, 132, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(38, 270, "LAS COMBINACIONES DE LETRAS SON CASI INFINITAS", 14,
                  INK3, "700", spacing="1.8"))
    b.append(_txt(38, 306, "El vocabulario no lo es.", 24, INK, "700"))
    b.append(_txt(38, 340, "Es una lista cerrada, fijada una vez antes de entrenar.",
                  18, INK2, "400"))

    b.append(_rect(570, 234, 540, 132, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(598, 270, "CUÁNTAS PIEZAS TIENE ESA LISTA", 14, ACC, "700",
                  spacing="1.8"))
    b.append(_txt(598, 310, "~50 000", 27, ACC, "700", family=MONO))
    b.append(_txt(598, 340, "un vocabulario típico", 17, INK2, "400"))
    b.append(_txt(852, 310, "~256 000", 27, ACC, "700", family=MONO))
    b.append(_txt(852, 340, "los modelos más grandes", 17, INK2, "400"))

    b.append(_txt(560, 410, "Todo el lenguaje escrito, partido en unas decenas de "
                            "miles de piezas que se repiten.", 20, INK, "700",
                  "middle"))
    return _svg(430, "".join(b))
