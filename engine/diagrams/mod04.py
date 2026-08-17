# -*- coding: utf-8 -*-
"""Diagramas del modulo 4 - Como razona un LLM."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3,
    MONO, OK, OK_SOFT, PAPER, SANS, W, _arrow, _rect, _svg, _txt,
)



def frontera_modelo():
    """Qué queda dentro del modelo y qué queda en el sistema que lo rodea."""
    b = [DEFS]
    # contenedor: el sistema
    b.append(_rect(10, 10, 1100, 300, fill="#fbfbfd", stroke=HAIR, sw=2, r=16,
                   dash="7 6"))
    b.append(_txt(36, 48, "EL SISTEMA QUE CONSTRUYES", 15, INK3, "700",
                  spacing="2.4"))

    piezas = [
        (56, 86, "Buscador web"),
        (56, 156, "Base de datos"),
        (56, 226, "Historial guardado"),
        (834, 86, "Ejecutor de código"),
        (834, 156, "Herramientas"),
        (834, 226, "Validación"),
    ]
    for x, y, label in piezas:
        b.append(_rect(x, y, 224, 58, fill="#ffffff", stroke=HAIR, sw=1.5, r=9))
        b.append(_txt(x + 112, y + 36, label, 18, INK2, "600", "middle"))

    # el modelo, sólido, en el centro y alineado con las piezas
    b.append(_rect(408, 110, 304, 156, fill=ACC, stroke=ACC, sw=0, r=14))
    b.append(_txt(560, 158, "EL MODELO", 17, "#ffffff", "700", "middle",
                  spacing="2.4"))
    b.append(_txt(560, 196, "entra texto", 20, "#d9ccff", "400", "middle"))
    b.append(_txt(560, 226, "salen probabilidades", 20, "#d9ccff", "400", "middle"))

    # flechas de entrada y salida
    b.append(_arrow(292, 188, 398, 188, ACC, 2.5))
    b.append(_txt(345, 174, "prompt", 16, ACC, "600", "middle"))
    b.append(_arrow(722, 188, 828, 188, ACC, 2.5))
    b.append(_txt(775, 174, "tokens", 16, ACC, "600", "middle"))

    b.append(_txt(560, 352, "Todo lo de fuera lo escribes tú. El modelo no lo hace, "
                            "ni sabe que existe.", 19, INK3, "400", "middle"))
    return _svg(374, "".join(b))


# ---------------------------------------------------------------------------


def bucle_generacion():
    """El ciclo que convierte una sola predicción en un texto largo."""
    b = [DEFS]
    pasos = [
        (30, "Texto", "«el gato se\nsubió al»"),
        (250, "Tokens", "[el][ gato]\n[ se][ subió][ al]"),
        (470, "Modelo", "una pasada"),
        (690, "Distribución", "probabilidad de\ncada token"),
        (910, "Muestreo", "elige uno:\n« tejado»"),
    ]
    for i, (x, titulo, detalle) in enumerate(pasos):
        acc = (i == 2)
        fill = ACC if acc else "#ffffff"
        b.append(_rect(x, 60, 180, 108, fill=fill, stroke=ACC if acc else HAIR,
                       sw=2 if acc else 1.5, r=12))
        b.append(_txt(x + 90, 92, titulo, 18, "#ffffff" if acc else INK, "700",
                      "middle"))
        for j, line in enumerate(detalle.split("\n")):
            b.append(_txt(x + 90, 120 + j * 22, line, 16,
                          "#d9ccff" if acc else INK3, "400", "middle",
                          family=MONO if i == 1 else SANS))
        if i < len(pasos) - 1:
            b.append(_arrow(x + 186, 114, x + 244, 114, INK3, 2))

    # retorno del bucle
    b.append('<path d="M 1000 174 L 1000 226 Q 1000 240 986 240 L 134 240 '
             'Q 120 240 120 226 L 120 180" fill="none" stroke="%s" '
             'stroke-width="2.5" marker-end="url(#ahp)"/>' % ACC)
    b.append(_rect(420, 224, 280, 34, fill="#ffffff", stroke="none", sw=0, r=0))
    b.append(_txt(560, 248, "se añade al texto y otra vez", 18, ACC, "600",
                  "middle"))

    b.append(_txt(560, 300, "Una palabra de veinte tokens son veinte pasadas "
                            "completas por el modelo.", 18, INK3, "400", "middle"))
    return _svg(320, "".join(b))


# ---------------------------------------------------------------------------


def distribucion():
    """La distribución de probabilidad sobre el vocabulario."""
    filas = [
        ("tejado", 0.31), ("sofá", 0.22), ("árbol", 0.14),
        ("coche", 0.07), ("escritorio", 0.04), ("regazo", 0.02),
    ]
    b = [DEFS]
    x0, bw = 250, 640
    for i, (tok, p) in enumerate(filas):
        y = 30 + i * 44
        b.append(_txt(228, y + 22, tok, 20, INK, "600", "end", family=MONO))
        b.append(_rect(x0, y, bw, 30, fill="#f1f1f5", stroke="none", sw=0, r=6))
        b.append(_rect(x0, y, bw * p / 0.31, 30, fill=ACC, stroke="none", sw=0, r=6))
        b.append(_txt(x0 + bw + 18, y + 22, "%.2f" % p, 20, INK2, "700",
                      family=MONO))
    y = 30 + len(filas) * 44
    b.append(_txt(228, y + 22, "…", 20, INK3, "600", "end", family=MONO))
    b.append(_txt(x0, y + 22, "y así para los ~100 000 tokens restantes, "
                              "todos con probabilidad diminuta pero distinta de cero",
                  17, INK3, "400"))
    return _svg(y + 50, "".join(b))


# ---------------------------------------------------------------------------


def atencion():
    """Cuánto pesa cada token anterior al predecir el siguiente."""
    palabras = [("la", .08), ("llave", .95), ("que", .05), ("compré", .22),
                ("ayer", .07), ("en", .04), ("la", .04), ("ferretería", .38),
                ("no", .61)]
    b = [DEFS]
    x = 40
    base = 190
    for w, peso in palabras:
        ancho = 26 + len(w) * 15
        alto = 16 + peso * 118
        b.append(_rect(x, base - alto, ancho, alto, fill=ACC, stroke="none", sw=0,
                       r=6))
        b.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="6" '
                 'fill="#ffffff" opacity="%.2f"/>' % (x, base - alto, ancho, alto,
                                                      1 - (0.25 + peso * 0.75)))
        b.append(_txt(x + ancho / 2, base + 30, w, 20, INK2, "500", "middle"))
        x += ancho + 12

    # el token que se está prediciendo
    b.append(_rect(x + 10, base - 56, 108, 56, fill="#ffffff", stroke=ACC, sw=2.5,
                   r=8, dash="6 5"))
    b.append(_txt(x + 64, base - 20, "abre", 22, ACC, "700", "middle"))
    b.append(_txt(x + 64, base + 30, "¿?", 20, ACC, "700", "middle"))

    b.append(_txt(40, 44, "ALTURA = CUÁNTO PESA ESA PALABRA AL PREDECIR LA SIGUIENTE",
                  15, INK3, "700", spacing="2.2"))
    b.append(_txt(40, base + 78, "«llave» decide que lo que sigue es «abre». «ayer» "
                                 "casi no participa, aunque esté más cerca.",
                  19, INK2, "400"))
    return _svg(base + 100, "".join(b))


# ---------------------------------------------------------------------------


def representacion_interna():
    """Un token se convierte en una posición dentro del modelo."""
    b = [DEFS]
    # token
    b.append(_rect(20, 92, 150, 60, fill="#ffffff", stroke=HAIR, sw=1.5, r=10))
    b.append(_txt(95, 130, "« gato»", 22, INK, "600", "middle", family=MONO))
    b.append(_arrow(178, 122, 232, 122, INK3, 2))

    # vector
    b.append(_rect(240, 74, 250, 96, fill=PAPER, stroke=HAIR, sw=1.5, r=10))
    b.append(_txt(365, 104, "0.023  −0.441  0.189", 17, ACC, "500", "middle",
                  family=MONO))
    b.append(_txt(365, 128, "0.007  …  −0.226", 17, ACC, "500", "middle",
                  family=MONO))
    b.append(_txt(365, 156, "cientos de números", 15, INK3, "400", "middle"))
    b.append(_arrow(498, 122, 552, 122, INK3, 2))

    # mapa de significado
    b.append(_rect(560, 30, 540, 250, fill="#fbfbfd", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(580, 58, "UN ESPACIO DE SIGNIFICADO", 14, INK3, "700",
                  spacing="2.2"))
    puntos = [
        (664, 128, "gato", ACC, True), (668, 92, "mascota", ACC, False),
        (700, 176, "perro", ACC, False), (628, 196, "felino", ACC, False),
        (938, 214, "servidor", INK3, False), (982, 152, "router", INK3, False),
        (916, 116, "kernel", INK3, False),
    ]
    for x, y, label, color, big in puntos:
        b.append('<circle cx="%d" cy="%d" r="%d" fill="%s" opacity="%s"/>'
                 % (x, y, 8 if big else 5, color, "1" if big else ".55"))
        b.append(_txt(x + 14, y + 6, label, 17, INK2 if color == ACC else INK3,
                      "700" if big else "400"))
    b.append('<ellipse cx="672" cy="146" rx="104" ry="84" fill="none" stroke="%s" '
             'stroke-width="1.5" stroke-dasharray="6 5" opacity=".65"/>' % ACC)

    b.append(_txt(560, 332, "Las que significan cosas parecidas caen cerca. "
                            "Esa cercanía es lo que hace que generalice.",
                  19, INK3, "400", "middle"))
    return _svg(356, "".join(b))


# ---------------------------------------------------------------------------


def entrenamiento_inferencia():
    """Los pesos cambian una vez; después están congelados."""
    b = [DEFS]

    def grid(x0, y0, color, opacity):
        out = []
        for r in range(4):
            for c in range(6):
                out.append('<rect x="%d" y="%d" width="30" height="24" rx="4" '
                           'fill="%s" opacity="%.2f"/>'
                           % (x0 + c * 38, y0 + r * 32, color,
                              opacity * (0.35 + 0.16 * ((r + c) % 4))))
        return "".join(out)

    # entrenamiento
    b.append(_rect(20, 20, 520, 280, fill="#ffffff", stroke=HAIR, sw=1.5, r=14))
    b.append(_txt(48, 58, "ENTRENAMIENTO", 15, INK3, "700", spacing="2.4"))
    b.append(_txt(48, 88, "Los pesos cambian", 24, INK, "700"))
    b.append(grid(48, 116, ACC, 1))
    for y in (140, 200):
        b.append(_arrow(300, y, 340, y, ACC, 2))
    b.append(_txt(352, 146, "se ajustan", 18, ACC, "600"))
    b.append(_txt(352, 206, "millones de veces", 18, INK3, "400"))
    b.append(_txt(48, 278, "Ocurrió una vez, meses atrás, en el proveedor.",
                  17, INK3, "400"))

    # inferencia
    b.append(_rect(580, 20, 520, 280, fill=ACC_SOFT, stroke=ACC, sw=2, r=14))
    b.append(_txt(608, 58, "INFERENCIA", 15, ACC, "700", spacing="2.4"))
    b.append(_txt(608, 88, "Los pesos NO cambian", 24, INK, "700"))
    b.append(grid(608, 116, ACC, 1))
    # candado
    b.append(_rect(872, 140, 76, 62, fill="#ffffff", stroke=ACC, sw=2.5, r=10))
    b.append('<path d="M 895 140 v -14 a 15 15 0 0 1 30 0 v 14" fill="none" '
             'stroke="%s" stroke-width="4"/>' % ACC)
    b.append('<circle cx="910" cy="168" r="7" fill="%s"/>' % ACC)
    b.append(_txt(910, 224, "congelados", 18, ACC, "600", "middle"))
    b.append(_txt(608, 278, "Es lo que pasa cada vez que lo usas. Siempre el mismo "
                            "archivo.", 17, INK3, "400"))
    return _svg(320, "".join(b))


# ---------------------------------------------------------------------------


def temperatura():
    """La misma distribución, muestreada con tres temperaturas."""
    base = [0.31, 0.22, 0.14, 0.07, 0.04, 0.02]
    escenarios = [
        ("temperatura 0.2", [0.86, 0.11, 0.02, 0.01, 0.00, 0.00],
         "casi siempre gana el más probable"),
        ("temperatura 1.0", base, "la distribución tal cual"),
        ("temperatura 1.8", [0.24, 0.21, 0.18, 0.15, 0.12, 0.10],
         "las opciones raras ganan a menudo"),
    ]
    b = [DEFS]
    for i, (titulo, vals, pie) in enumerate(escenarios):
        x0 = 20 + i * 372
        b.append(_rect(x0, 20, 340, 250, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
        b.append(_txt(x0 + 24, 54, titulo.upper(), 15, ACC if i == 1 else INK3,
                      "700", spacing="1.8"))
        for j, v in enumerate(vals):
            bx = x0 + 30 + j * 50
            h = max(3, v * 165)
            b.append('<rect x="%d" y="%.1f" width="34" height="%.1f" rx="4" '
                     'fill="%s" opacity="%.2f"/>'
                     % (bx, 235 - h, h, ACC, 1 if j == 0 else 0.72))
        b.append('<line x1="%d" y1="236" x2="%d" y2="236" stroke="%s" '
                 'stroke-width="1.5"/>' % (x0 + 24, x0 + 316, HAIR))
        b.append(_txt(x0 + 170, 262, pie, 16, INK3, "400", "middle"))
    b.append(_txt(560, 312, "La temperatura no hace al modelo más listo: lo hace "
                            "menos predecible.", 19, INK2, "600", "middle"))
    return _svg(330, "".join(b))


# ---------------------------------------------------------------------------


def sin_salida_no_se():
    """Por qué siempre sale una respuesta, haya o no con qué respaldarla."""
    b = [DEFS]

    def rama(x, titulo, sub, color, soft, ok):
        b.append(_rect(x, 96, 470, 150, fill=soft, stroke=color, sw=2, r=12))
        b.append(_txt(x + 28, 138, titulo, 22, color, "700"))
        for j, line in enumerate(sub.split("\n")):
            b.append(_txt(x + 28, 174 + j * 26, line, 18, INK2, "400"))

    b.append(_rect(400, 14, 320, 56, fill=ACC, stroke="none", sw=0, r=10))
    b.append(_txt(560, 50, "llega una pregunta", 20, "#ffffff", "700", "middle"))
    b.append(_arrow(470, 74, 340, 92, ACC, 2))
    b.append(_arrow(650, 74, 780, 92, ACC, 2))

    rama(20, "Tiene con qué anclarse", "La información está en el contexto.\n"
                                       "Sale una distribución y se muestrea un token.",
         OK, OK_SOFT, True)
    rama(630, "No tiene con qué anclarse", "La información no está en ninguna parte.\n"
                                           "Sale una distribución y se muestrea un token.",
         DANGER, DANGER_SOFT, False)

    b.append(_rect(300, 278, 520, 58, fill="#ffffff", stroke=INK3, sw=2, r=10,
                   dash="7 6"))
    b.append(_txt(560, 314, "no existe una tercera salida: «no lo sé»", 20, INK,
                  "700", "middle"))
    return _svg(356, "".join(b))

