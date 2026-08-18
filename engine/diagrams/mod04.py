# -*- coding: utf-8 -*-
"""Diagramas del modulo 4 - Como razona un LLM.

Todo el modulo trabaja sobre una sola frase, «el gato maulla y el perro...»,
desde el acertijo de apertura hasta la tabla de temperaturas. Si se cambia la
frase en un diagrama hay que cambiarla en los cinco.
"""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3,
    MONO, OK, OK_SOFT, PAPER, SANS, W, _arrow, _rect, _svg, _txt,
)

FRASE = [("el", .05), ("gato", .72), ("maúlla", .95), ("y", .04), ("el", .05),
         ("perro", .88)]
SIGUIENTE = "ladra"


def acertijo():
    """La frase incompleta, y la palabra que la sala pone sola."""
    b = [DEFS]
    b.append(_txt(560, 34, "COMPLÉTALA EN VOZ ALTA", 15, INK3, "700", "middle",
                  spacing="2.4"))

    palabras = [p for p, _ in FRASE]
    anchos = [34 + len(p) * 24 for p in palabras] + [150]
    x = (1120 - sum(anchos) - 16 * (len(anchos) - 1)) / 2.0
    for i, w in enumerate(anchos):
        hueco = (i == len(anchos) - 1)
        b.append(_rect(x, 62, w, 84, fill="#ffffff",
                       stroke=ACC if hueco else HAIR, sw=2.5 if hueco else 1.5,
                       r=10, dash="7 6" if hueco else None))
        if not hueco:
            b.append(_txt(x + w / 2.0, 116, palabras[i], 30, INK, "600", "middle"))
        x += w + 16

    hueco_cx = x - 16 - 150 / 2.0
    b.append('<path d="M %.1f 152 L %.1f 186 Q %.1f 200 %.1f 200 L 690 200" '
             'fill="none" stroke="%s" stroke-width="2.5" '
             'marker-end="url(#ahp)"/>'
             % (hueco_cx, hueco_cx, hueco_cx, hueco_cx - 14, ACC))
    b.append(_rect(450, 164, 220, 76, fill=ACC, stroke="none", sw=0, r=12))
    b.append(_txt(560, 214, SIGUIENTE, 34, "#ffffff", "700", "middle"))
    b.append(_txt(560, 292, "Lo que contesta la sala, casi sin pensarlo.", 20, INK2,
                  "600", "middle"))
    b.append(_txt(560, 326, "«corre», «se asusta» y «también» encajan igual de bien "
                            "en la gramática. Nadie las dijo.", 19, INK3, "400",
                  "middle"))
    b.append(_txt(560, 378, "Lo resolviste sin leer las seis palabras con el mismo "
                            "cuidado. Miraste dos.", 22, INK, "700", "middle"))
    return _svg(400, "".join(b))


# ---------------------------------------------------------------------------


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
        (30, "Texto", "«el gato maúlla\ny el perro»"),
        (250, "Tokens", "[el][ gato][ maúlla]\n[ y][ el][ perro]"),
        (470, "Modelo", "una pasada"),
        (690, "Distribución", "probabilidad de\ncada token"),
        (910, "Muestreo", "elige uno:\n« ladra»"),
    ]
    for i, (x, titulo, detalle) in enumerate(pasos):
        acc = (i == 2)
        fill = ACC if acc else "#ffffff"
        b.append(_rect(x, 60, 180, 108, fill=fill, stroke=ACC if acc else HAIR,
                       sw=2 if acc else 1.5, r=12))
        b.append(_txt(x + 90, 92, titulo, 18, "#ffffff" if acc else INK, "700",
                      "middle"))
        for j, line in enumerate(detalle.split("\n")):
            b.append(_txt(x + 90, 120 + j * 22, line, 14 if i == 1 else 16,
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
        ("ladra", 0.61), ("gruñe", 0.12), ("corre", 0.07),
        ("se", 0.05), ("también", 0.04), ("maúlla", 0.01),
    ]
    b = [DEFS]
    x0, bw = 250, 620
    for i, (tok, p) in enumerate(filas):
        y = 24 + i * 44
        b.append(_txt(228, y + 22, tok, 20, INK, "600", "end", family=MONO))
        b.append(_rect(x0, y, bw, 30, fill="#f1f1f5", stroke="none", sw=0, r=6))
        b.append(_rect(x0, y, max(4, bw * p / 0.61), 30, fill=ACC, stroke="none",
                       sw=0, r=6))
        b.append(_txt(x0 + bw + 18, y + 22, "%.2f" % p, 20, INK2, "700",
                      family=MONO))
    y = 24 + len(filas) * 44
    b.append(_txt(228, y + 22, "…", 20, INK3, "600", "end", family=MONO))
    b.append(_txt(x0, y + 22, "y así para los ~100 000 tokens restantes, todos con "
                              "probabilidad diminuta pero distinta de cero",
                  17, INK3, "400"))
    b.append(_txt(10, y + 76, "«maúlla» sigue en la lista. Es absurdo y aun así tiene "
                              "su número: nada queda descartado del todo.",
                  19, INK2, "600"))
    return _svg(y + 100, "".join(b))


# ---------------------------------------------------------------------------


def atencion():
    """Cuánto pesa cada token anterior al predecir el siguiente."""
    b = [DEFS]
    base = 224
    b.append(_txt(40, 32, "ALTURA = CUÁNTO PESA ESA PALABRA AL PREDECIR LA SIGUIENTE",
                  15, INK3, "700", spacing="2.2"))

    x = 40
    for w, peso in FRASE:
        ancho = 40 + len(w) * 26
        alto = 20 + peso * 152
        b.append(_rect(x, base - alto, ancho, alto, fill=ACC, stroke="none", sw=0,
                       r=6))
        b.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="6" '
                 'fill="#ffffff" opacity="%.2f"/>' % (x, base - alto, ancho, alto,
                                                      1 - (0.25 + peso * 0.75)))
        b.append(_txt(x + ancho / 2.0, base + 34, w, 24, INK2, "500", "middle"))
        x += ancho + 16

    # el token que se está prediciendo
    b.append(_rect(x, base - 70, 160, 70, fill="#ffffff", stroke=ACC, sw=2.5, r=10,
                   dash="6 5"))
    b.append(_txt(x + 80, base - 26, SIGUIENTE, 26, ACC, "700", "middle"))
    b.append(_txt(x + 80, base + 34, "¿?", 24, ACC, "700", "middle"))

    b.append(_txt(40, 296, "«maúlla» decide la respuesta aunque quede lejos. «y» no "
                           "aporta nada aunque esté pegada.", 20, INK, "700"))

    pasos = [
        ("1", "SE PARTE DE LA ÚLTIMA", "«perro». Todo arranca de ahí."),
        ("2", "SE BUSCAN LAS QUE IMPORTAN", "«maúlla» y «gato», no las vecinas."),
        ("3", "DE ESA MEZCLA SALE UNA", "Y la mezcla apunta a «ladra»."),
    ]
    for i, (n, titulo, linea) in enumerate(pasos):
        px = 10 + i * 372
        b.append(_rect(px, 322, 348, 78, fill="#fbfbfd", stroke=HAIR, sw=1.5, r=11))
        b.append('<circle cx="%d" cy="362" r="16" fill="%s"/>' % (px + 34, ACC))
        b.append(_txt(px + 34, 369, n, 17, "#ffffff", "700", "middle"))
        b.append(_txt(px + 64, 354, titulo, 13, ACC, "700", spacing="1.6"))
        b.append(_txt(px + 64, 382, linea, 17, INK2, "400"))
    return _svg(418, "".join(b))


# ---------------------------------------------------------------------------


def representacion_interna():
    """El espacio de significado, levantado un eje a la vez."""
    b = [DEFS]
    y0, h = 26, 300

    def marco(x, etiqueta, sub):
        out = [_rect(x, y0, 356, h, fill="#ffffff", stroke=HAIR, sw=1.5, r=12)]
        out.append(_txt(x + 26, y0 + 36, etiqueta, 15, INK3, "700", spacing="2"))
        out.append(_txt(x + 26, y0 + 62, sub, 16, INK3, "400"))
        return out

    # ── un eje ─────────────────────────────────────────────────────────────
    b += marco(10, "UN EJE", "¿cuánto tiene que ver con un animal?")
    b.append(_arrow(60, 200, 348, 200, INK3, 2))
    b.append(_txt(60, 240, "nada", 16, INK3, "400"))
    b.append(_txt(348, 240, "mucho", 16, INK3, "400", "end"))
    for nombre, valor in (("servidor", 0.05), ("veterinario", 0.58),
                          ("gato", 0.97)):
        px = 60 + valor * 280
        acc = (nombre == "gato")
        b.append('<circle cx="%.1f" cy="200" r="8" fill="%s"/>'
                 % (px, ACC if acc else INK3))
        b.append(_txt(px, 172, nombre, 17, INK2, "600", "middle"))
        b.append(_txt(px, 278, "%.2f" % valor, 18, ACC if acc else INK3, "700",
                      "middle", family=MONO))
    b.append(_txt(38, 306, "Un eje es un número por palabra.", 17, INK, "700"))

    # ── dos ejes ───────────────────────────────────────────────────────────
    b += marco(382, "DOS EJES", "y ahora, ¿cuánto tiene que ver con el cariño?")
    ox, oy, ew, eh = 434, 290, 240, 162
    b.append(_arrow(ox, oy, ox, oy - eh - 14, INK3, 1.8))
    b.append(_arrow(ox, oy, ox + ew + 14, oy, INK3, 1.8))
    puntos = [("gato", .76, .74, ACC), ("perro", .90, .58, ACC),
              ("felino", .62, .44, ACC), ("bebé", .14, .90, INK2),
              ("servidor", .06, .24, INK3), ("router", .42, .12, INK3)]
    for nombre, fx, fy, color in puntos:
        px, py = ox + fx * ew, oy - fy * eh
        b.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s"/>' % (px, py, color))
        b.append(_txt(px + 12, py + 6, nombre, 16, color, "600"))
    b.append('<ellipse cx="%.1f" cy="%.1f" rx="70" ry="56" fill="none" stroke="%s" '
             'stroke-width="1.6" stroke-dasharray="6 5" opacity=".7"/>'
             % (ox + .76 * ew, oy - .58 * eh, ACC))

    # ── cientos de ejes ────────────────────────────────────────────────────
    b += marco(754, "CIENTOS DE EJES", "el mismo cálculo, muchas más veces")
    b.append(_rect(786, 124, 150, 52, fill=PAPER, stroke=HAIR, sw=1.5, r=9))
    b.append(_txt(861, 158, "« gato»", 21, INK, "600", "middle", family=MONO))
    b.append(_arrow(861, 184, 861, 212, INK3, 2))
    for i, v in enumerate(["0.023", "-0.441", "0.189", "0.007", "-0.226", "…"]):
        b.append(_txt(786 + (i % 3) * 106, 246 + (i // 3) * 32, v, 18, ACC, "500",
                      family=MONO))
    b.append(_txt(786, 306, "No se dibuja, y no hace falta.", 18, INK, "700"))

    b.append(_txt(560, 366, "Nadie eligió qué mide cada eje: salió del entrenamiento. "
                            "Lo que cuenta es que lo parecido cae cerca.",
                  20, INK, "700", "middle"))
    return _svg(390, "".join(b))


# ---------------------------------------------------------------------------


def aritmetica_vectores():
    """Si el significado es posición, la relación es dirección."""
    b = [DEFS]

    b.append(_rect(10, 20, 540, 250, fill="#fbfbfd", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(38, 52, "EL MISMO PASO, DOS PARES DISTINTOS", 15, INK3, "700",
                  spacing="2"))
    pares = [(("hombre", 78, 152), ("mujer", 248, 88)),
             (("rey", 312, 152), ("reina", 482, 88))]
    for (n1, x1, y1), (n2, x2, y2) in pares:
        b.append(_arrow(x1 + 12, y1 - 6, x2 - 14, y2 + 8, ACC, 2.5))
        b.append('<circle cx="%d" cy="%d" r="8" fill="%s"/>' % (x1, y1, INK3))
        b.append('<circle cx="%d" cy="%d" r="8" fill="%s"/>' % (x2, y2, ACC))
        b.append(_txt(x1, y1 + 30, n1, 18, INK2, "600", "middle"))
        b.append(_txt(x2, y2 - 18, n2, 18, ACC, "700", "middle"))
    b.append(_txt(38, 214, "Las dos flechas apuntan igual.", 20, INK, "700"))
    b.append(_txt(38, 240, "Esa dirección compartida es lo que en el", 17, INK2,
                  "400"))
    b.append(_txt(38, 262, "lenguaje llamamos género.", 17, INK2, "400"))

    b.append(_rect(570, 20, 540, 250, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(598, 52, "Y UNA DIRECCIÓN SE PUEDE LLEVAR A OTRA PARTE", 15, ACC,
                  "700", spacing="1.8"))
    filas = [("género", "rey - hombre + mujer", "reina"),
             ("país y capital", "Roma - Italia + Colombia", "Bogotá"),
             ("tiempo verbal", "nadé - nadar + caminar", "caminé")]
    for i, (relacion, izq, der) in enumerate(filas):
        y = 100 + i * 56
        b.append(_txt(598, y, relacion.upper(), 13, INK3, "700", spacing="1.6"))
        b.append(_txt(598, y + 28, izq, 19, INK2, "500", family=MONO))
        b.append(_txt(1082, y + 28, "= " + der, 19, ACC, "700", "end",
                      family=MONO))

    b.append(_txt(560, 308, "El significado es una posición. La relación entre dos "
                            "palabras es una dirección.", 20, INK, "700", "middle"))
    return _svg(328, "".join(b))


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
    base = [0.61, 0.12, 0.07, 0.05, 0.04, 0.01]
    escenarios = [
        ("temperatura 0.2", [0.95, 0.03, 0.01, 0.01, 0.00, 0.00],
         "gana «ladra» casi siempre"),
        ("temperatura 1.0", base, "la distribución tal cual"),
        ("temperatura 1.8", [0.30, 0.19, 0.16, 0.14, 0.12, 0.09],
         "«maúlla» empieza a salir"),
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
                 'stroke-width="1.6"/>' % (x0 + 24, x0 + 316, HAIR))
        b.append(_txt(x0 + 170, 262, pie, 16, INK3, "400", "middle"))
    b.append(_txt(560, 312, "La temperatura no hace al modelo más listo: lo hace "
                            "menos predecible.", 20, INK, "700", "middle"))
    b.append(_txt(560, 344, "Y algo de eso hace falta: un sistema que siempre elige "
                            "lo más probable no escribe nunca nada nuevo.",
                  18, INK3, "400", "middle"))
    return _svg(364, "".join(b))


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
