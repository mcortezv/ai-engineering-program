# -*- coding: utf-8 -*-
"""Diagramas del módulo 8 — Contexto y memoria."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def tres_memorias():
    """Los nombres prestados de la psicología, traducidos a lo que son en código."""
    filas = [
        ("Memoria de corto plazo", "El historial que reenvías en esta petición",
         "en la ventana de contexto", "se paga en tokens cada vez"),
        ("Memoria de largo plazo", "Hechos extraídos de conversaciones anteriores",
         "en una base de datos", "solo entra lo que decides recuperar"),
        ("Memoria persistente", "Datos estables: idioma, rol, permisos",
         "en una base de datos", "suele inyectarse siempre"),
    ]
    b = [DEFS]
    b.append(_txt(10, 30, "EL NOMBRE PRESTADO", 14, INK3, "700", spacing="2"))
    b.append(_txt(392, 30, "QUÉ ES EN REALIDAD", 14, INK3, "700", spacing="2"))
    b.append(_txt(792, 30, "DÓNDE VIVE", 14, ACC, "700", spacing="2"))
    b.append('<line x1="10" y1="42" x2="1110" y2="42" stroke="%s" '
             'stroke-width="1.6"/>' % INK3)

    for i, (nombre, real, donde, nota) in enumerate(filas):
        y = 58 + i * 96
        if i % 2 == 1:
            b.append('<rect x="10" y="%d" width="1100" height="86" rx="8" '
                     'fill="#fbfbfd"/>' % y)
        b.append(_txt(28, y + 38, nombre, 19, INK2, "600"))
        b.append(_txt(28, y + 64, "(término prestado)", 15, INK3, "400"))
        b.append(_txt(392, y + 44, real, 18, INK, "500"))
        b.append(_rect(792, y + 16, 300, 54, fill=ACC_SOFT, stroke=ACC, sw=1.5, r=8))
        b.append(_txt(812, y + 40, donde, 17, ACC, "700"))
        b.append(_txt(812, y + 60, nota, 14, INK3, "400"))

    b.append(_txt(10, 388, "No hay consolidación, ni decaimiento, ni recuerdo "
                           "reconstructivo. Hay una base de datos y una política de "
                           "qué leer.", 19, INK3, "400"))
    return _svg(408, "".join(b))


def estrategias_historial():
    """Cuatro formas de que la conversación quepa, y qué pierde cada una."""
    est = [
        ("Ventana deslizante", "Conservas los últimos N mensajes.",
         "Todo lo anterior, de golpe y sin aviso.", DANGER),
        ("Resumen progresivo", "Resumes lo viejo y sustituyes.",
         "Detalle. Y el error se acumula resumen sobre resumen.", WARN),
        ("Memoria selectiva", "Extraes hechos y tiras el resto.",
         "El matiz conversacional.", WARN),
        ("Recuperar del historial", "Indexas y traes solo lo relevante.",
         "La continuidad narrativa.", INK3),
    ]
    b = [DEFS]
    for i, (nombre, como, pierde, color) in enumerate(est):
        x = 10 + (i % 2) * 560
        y = 14 + (i // 2) * 168
        b.append(_rect(x, y, 540, 152, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
        b.append('<rect x="%d" y="%d" width="4" height="152" rx="2" fill="%s"/>'
                 % (x, y, color))
        b.append(_txt(x + 28, y + 40, nombre, 21, INK, "700"))
        b.append(_txt(x + 28, y + 70, como, 18, INK2, "400"))
        b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                 'stroke-width="1.4"/>' % (x + 28, y + 88, x + 512, y + 88, HAIR))
        b.append(_txt(x + 28, y + 112, "QUÉ PIERDES", 13, color, "700", spacing="1.6"))
        b.append(_txt(x + 28, y + 136, pierde, 17, INK3, "400"))
    return _svg(348, "".join(b))


def triple_costo():
    """Toda memoria se paga tres veces."""
    costos = [
        ("PRECISIÓN", "Más contexto no es más precisión",
         "Un historial largo diluye la señal. Y una memoria equivocada produce "
         "respuestas confiadamente incorrectas.", ACC),
        ("LATENCIA", "Todo se procesa antes de responder",
         "Cada token de entrada se procesa antes de generar el primero de salida. "
         "Se nota en el tiempo de respuesta.", INK2),
        ("DINERO", "Cada token se paga en cada petición",
         "No una vez: en todas. Un hecho que inyectas siempre lo pagas siempre, "
         "lo use o no la respuesta.", INK3),
    ]
    b = [DEFS]
    for i, (t, titular, nota, color) in enumerate(costos):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 232, fill="#ffffff", stroke=color, sw=2, r=12))
        b.append(_txt(x + 24, 50, t, 15, color, "700", spacing="2.2"))
        words, line, lines = titular.split(), "", []
        for w in words:
            if len(line + " " + w) > 22:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(x + 24, 92 + j * 30, ln, 22, INK, "700"))
        yy = 92 + len(lines) * 30 + 12
        words, line, lines = nota.split(), "", []
        for w in words:
            if len(line + " " + w) > 38:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(x + 24, yy + j * 24, ln, 16, INK3, "400"))

    b.append(_rect(10, 264, 1100, 66, fill=ACC_SOFT, stroke=ACC, sw=2, r=11))
    b.append(_txt(560, 306, "Olvidar no es una limitación: es una función que hay "
                            "que diseñar.", 22, INK, "700", "middle"))
    return _svg(348, "".join(b))
