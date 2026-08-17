# -*- coding: utf-8 -*-
"""Diagramas del módulo 7 — El LLM como servicio: API frente a chat."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)


def chat_vs_api():
    """Lo que hace el chat y quién tiene que hacerlo con la API."""
    filas = [
        ("Recuerda la conversación", "reenviar el historial completo"),
        ("Sabe quién eres", "guardar y recuperar de una base de datos"),
        ("Busca en internet", "llamar a un buscador y pegar los resultados"),
        ("Ejecuta código y lee archivos", "implementar las herramientas"),
        ("Corta el historial cuando no cabe", "decidir y aplicar la política"),
        ("Reintenta si el servicio falla", "manejar errores y reintentos"),
        ("Muestra la respuesta poco a poco", "consumir el flujo de streaming"),
    ]
    b = [DEFS]
    b.append(_rect(10, 14, 540, 44, fill="#f1f1f5", stroke="none", sw=0, r=8))
    b.append(_txt(38, 44, "LO QUE HACE EL CHAT", 15, INK3, "700", spacing="2.2"))
    b.append(_rect(570, 14, 540, 44, fill=ACC, stroke="none", sw=0, r=8))
    b.append(_txt(598, 44, "QUIÉN LO HACE CON LA API", 15, "#ffffff", "700",
                  spacing="2.2"))

    for i, (chat, tuyo) in enumerate(filas):
        y = 70 + i * 42
        if i % 2 == 0:
            b.append('<rect x="10" y="%d" width="1100" height="38" rx="6" '
                     'fill="#fbfbfd"/>' % y)
        b.append(_txt(38, y + 26, chat, 18, INK2, "400"))
        b.append(_txt(598, y + 26, "tu código: " + tuyo, 18, INK, "500"))

    y = 70 + len(filas) * 42
    b.append(_rect(10, y + 12, 1100, 66, fill=ACC_SOFT, stroke=ACC, sw=2, r=11))
    b.append(_txt(38, y + 48, "Un chat de AI es un producto construido encima de una "
                              "API, y ese producto es casi todo lo que no es el "
                              "modelo.", 20, INK, "700"))
    return _svg(y + 100, "".join(b))


def sin_estado():
    """Tres peticiones que demuestran que no hay sesión."""
    b = [DEFS]

    def peticion(x, titulo, lineas, respuesta, ok):
        color = OK if ok else DANGER
        out = [_rect(x, 14, 348, 250, fill="#ffffff", stroke=HAIR, sw=1.5, r=12)]
        out.append(_txt(x + 24, 48, titulo, 15, INK3, "700", spacing="2"))
        out.append(_rect(x + 20, 62, 308, 24 + len(lineas) * 26, fill=PAPER,
                         stroke=HAIR, sw=1, r=7))
        for j, ln in enumerate(lineas):
            out.append(_txt(x + 34, 88 + j * 26, ln, 15, INK2, "400", family=MONO))
        yy = 62 + 24 + len(lineas) * 26 + 22
        out.append(_rect(x + 20, yy, 308, 52, fill=OK_SOFT if ok else DANGER_SOFT,
                         stroke=color, sw=1.5, r=8))
        out.append(_txt(x + 174, yy + 33, respuesta, 18, color, "700", "middle"))
        return "".join(out)

    b.append(peticion(10, "PETICIÓN 1",
                      ['user: "Me llamo Cristian."'],
                      "«Mucho gusto, Cristian.»", True))
    b.append(peticion(382, "PETICIÓN 2 — NUEVA",
                      ['user: "¿Cómo me llamo?"'],
                      "«No lo sé.»", False))
    b.append(peticion(754, "PETICIÓN 3 — TODO OTRA VEZ",
                      ['user: "Me llamo Cristian."',
                       'assistant: "Mucho gusto…"',
                       'user: "¿Cómo me llamo?"'],
                      "«Cristian.»", True))

    b.append(_txt(560, 300, "No hay sesión, ni identificador implícito, ni nada "
                            "guardado del lado del proveedor.", 20, INK, "700",
                  "middle"))
    return _svg(320, "".join(b))


def crecimiento_historial():
    """Lo que se reenvía en cada turno de una conversación."""
    b = [DEFS]
    b.append(_txt(10, 30, "TOKENS ENVIADOS EN CADA TURNO", 15, INK3, "700",
                  spacing="2.2"))
    turnos = 12
    x0, ancho = 10, 86
    for i in range(turnos):
        x = x0 + i * (ancho + 4)
        alto = 12 + (i + 1) * 15
        b.append('<rect x="%d" y="%d" width="%d" height="%d" rx="4" fill="%s" '
                 'opacity="%.2f"/>' % (x, 244 - alto, ancho, alto, ACC,
                                       0.35 + 0.055 * i))
        b.append(_txt(x + ancho / 2.0, 266, str(i + 1), 15, INK3, "500", "middle",
                      family=MONO))
    b.append('<line x1="10" y1="246" x2="1090" y2="246" stroke="%s" '
             'stroke-width="1.5"/>' % HAIR)
    b.append(_txt(550, 292, "número de turno", 16, INK3, "400", "middle"))

    b.append(_rect(10, 314, 1100, 84, fill=ACC_SOFT, stroke=ACC, sw=2, r=11))
    b.append(_txt(38, 350, "El turno 12 no cuesta como el primero: cuesta doce veces "
                           "más.", 20, INK, "700"))
    b.append(_txt(38, 380, "Y el total de la conversación no es la suma de doce "
                           "turnos iguales, sino de doce turnos crecientes.",
                  18, INK2, "400"))
    return _svg(416, "".join(b))
