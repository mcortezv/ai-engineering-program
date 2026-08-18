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
                 'stroke-width="1.4"/>' % (x + 24, x + 324, HAIR))
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


# ---------------------------------------------------------------------------


def red_neuronal():
    """Capa de entrada, capas ocultas y capa de salida: dónde vive la regla."""
    b = [DEFS]

    capas = [(90, 4, "ENTRADA"), (250, 6, "OCULTA"), (410, 6, "OCULTA"),
             (570, 2, "SALIDA")]
    cy, paso = 182, 42

    def ys(n):
        return [cy + (i - (n - 1) / 2.0) * paso for i in range(n)]

    # las conexiones van primero: los nodos tienen que quedar encima
    for k in range(len(capas) - 1):
        x1, n1 = capas[k][0], capas[k][1]
        x2, n2 = capas[k + 1][0], capas[k + 1][1]
        for i, y1 in enumerate(ys(n1)):
            for j, y2 in enumerate(ys(n2)):
                peso = ((i * 7 + j * 5 + k * 11) % 9) / 8.0
                b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                         'stroke="%s" stroke-width="%.2f" opacity="%.2f"/>'
                         % (x1 + 15, y1, x2 - 15, y2, ACC,
                            0.7 + peso * 3.3, 0.16 + peso * 0.52))

    for x, n, etiqueta in capas:
        for y in ys(n):
            b.append('<circle cx="%d" cy="%.1f" r="15" fill="#ffffff" '
                     'stroke="%s" stroke-width="2"/>' % (x, y, ACC))
        b.append(_txt(x, 40, etiqueta, 14, INK3, "700", "middle", spacing="1.8"))

    b.append(_txt(90, 322, "el correo", 17, INK2, "500", "middle"))
    b.append(_txt(330, 322, "donde se encuentra el patrón", 17, INK2, "500",
                  "middle"))
    b.append(_txt(570, 322, "spam o no", 17, INK2, "500", "middle"))

    b.append(_rect(700, 44, 410, 246, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(728, 82, "LO QUE HAY QUE VER AQUÍ", 15, ACC, "700",
                  spacing="2.2"))
    b.append(_txt(728, 122, "Cada conexión tiene un peso.", 19, INK, "700"))
    b.append(_txt(728, 154, "Entrenar es ajustar esos pesos", 19, INK, "700"))
    b.append(_txt(728, 180, "hasta que la salida acierta.", 19, INK, "700"))
    b.append(_txt(728, 224, "Nadie decide qué mira cada capa:", 17, INK2, "400"))
    b.append(_txt(728, 250, "eso también sale del entrenamiento.", 17, INK2,
                  "400"))
    b.append(_txt(728, 276, "Eso es delegar el diseño de la regla.", 17, ACC,
                  "600"))

    b.append(_txt(560, 372, "La regla existe, pero vive en el grosor de las "
                            "conexiones. No hay una línea que señalar.",
                  20, INK, "700", "middle"))
    return _svg(394, "".join(b))


# ---------------------------------------------------------------------------


def entrenar_probar():
    """El reparto entre datos de entrenamiento y datos de prueba."""
    b = [DEFS]
    b.append(_txt(10, 32, "TODOS LOS EJEMPLOS YA RESUELTOS QUE TIENES", 15, INK3,
                  "700", spacing="2.2"))

    b.append('<rect x="10" y="50" width="770" height="78" fill="%s"/>' % ACC)
    b.append('<rect x="780" y="50" width="330" height="78" fill="#ded6fa"/>')
    b.append(_rect(10, 50, 1100, 78, fill="none", stroke=INK, sw=2, r=0))
    b.append(_txt(395, 100, "70 %", 30, "#ffffff", "700", "middle"))
    b.append(_txt(945, 100, "30 %", 30, INK, "700", "middle"))

    b.append(_rect(10, 160, 770, 132, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(38, 196, "SE ENTRENA CON ESTOS", 14, ACC, "700", spacing="1.8"))
    b.append(_txt(38, 232, "Los pesos se ajustan millones de veces", 19, INK,
                  "400"))
    b.append(_txt(38, 262, "hasta que la salida coincide con la respuesta.", 19,
                  INK, "400"))

    b.append(_rect(790, 160, 320, 132, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(818, 196, "SE PRUEBA CON ESTOS", 14, ACC, "700", spacing="1.8"))
    b.append(_txt(818, 232, "Se apartan desde el principio", 19, INK, "400"))
    b.append(_txt(818, 262, "y el modelo no los ve nunca.", 19, INK, "400"))

    b.append(_txt(560, 344, "Si acierta igual en los que nunca vio, encontró el "
                            "patrón. Si solo acierta en el 70 %, se los aprendió "
                            "de memoria.", 19, INK, "700", "middle"))
    return _svg(366, "".join(b))
