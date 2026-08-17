# -*- coding: utf-8 -*-
"""Diagramas del módulo 15 — Orquestación."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def uno_vs_varios():
    """Un agente con todo, frente a varios con lo justo."""
    b = [DEFS]

    b.append(_rect(10, 14, 528, 300, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(38, 50, "TODO A UN SOLO AGENTE", 15, DANGER, "700", spacing="2.2"))
    b.append(_rect(150, 74, 248, 100, fill="#ffffff", stroke=DANGER, sw=2, r=11))
    b.append(_txt(274, 116, "UN AGENTE", 17, INK, "700", "middle", spacing="1.6"))
    b.append(_txt(274, 146, "todo el contexto", 17, INK3, "400", "middle"))
    for i, lab in enumerate(["50 herramientas", "20 documentos",
                             "historial completo", "todas las reglas"]):
        y = 200 + i * 28
        b.append('<circle cx="60" cy="%d" r="5" fill="%s"/>' % (y - 5, DANGER))
        b.append(_txt(76, y, lab, 16, INK2, "400"))
    b.append(_txt(310, 222, "menos preciso", 20, DANGER, "700"))
    b.append(_txt(310, 252, "y más caro", 20, DANGER, "700"))
    b.append(_txt(310, 282, "las dos cosas a la vez", 15, INK3, "400"))

    b.append(_rect(582, 14, 528, 300, fill=OK_SOFT, stroke=OK, sw=2, r=12))
    b.append(_txt(610, 50, "DIVIDIDO POR RESPONSABILIDAD", 15, OK, "700",
                  spacing="2.2"))
    piezas = [("Buscar", "3 herramientas", "barato"),
              ("Validar", "1 herramienta", "barato"),
              ("Redactar", "0 herramientas", "capaz"),
              ("Enviar", "1 herramienta", "barato")]
    for i, (t, h, modelo) in enumerate(piezas):
        y = 78 + i * 56
        b.append(_rect(610, y, 470, 46, fill="#ffffff", stroke=OK, sw=1.6, r=9))
        b.append(_txt(632, y + 30, t, 18, INK, "700"))
        b.append(_txt(748, y + 30, h, 16, INK3, "400"))
        b.append(_txt(1060, y + 30, "modelo " + modelo, 15,
                      ACC if modelo == "capaz" else INK3, "700", "end"))
    b.append(_txt(610, 308, "cada pieza recibe solo su contexto, y una sola necesita "
                            "juicio de verdad", 16, INK3, "400"))

    b.append(_txt(560, 356, "Cada pieza debería poder describirse en una frase, sin "
                            "la palabra «y».", 20, INK, "700", "middle"))
    return _svg(378, "".join(b))


def cuando_no_dividir():
    """Cuatro casos donde partir sale peor."""
    casos = [
        ("El contexto es indivisible",
         "Si el paso B necesita todo lo que vio A, pasas el contexto entero de "
         "todos modos y lo pagas dos veces."),
        ("La tarea es corta",
         "Dos llamadas para algo que resolvía una duplican latencia y costo sin "
         "ganar precisión."),
        ("La coordinación cuesta más que la tarea",
         "Si el orquestador necesita tanta lógica como las piezas, sobra la "
         "división."),
        ("Hace falta trazabilidad simple",
         "Más piezas es más superficie donde algo puede fallar en silencio."),
    ]
    b = [DEFS]
    for i, (t, d) in enumerate(casos):
        x = 10 + (i % 2) * 560
        y = 14 + (i // 2) * 132
        b.append(_rect(x, y, 540, 116, fill="#ffffff", stroke=HAIR, sw=1.6, r=11))
        b.append('<rect x="%d" y="%d" width="5" height="116" rx="2.5" fill="%s"/>'
                 % (x, y, WARN))
        b.append(_txt(x + 28, y + 40, t, 20, INK, "700"))
        palabras, linea, lineas = d.split(), "", []
        for w in palabras:
            if len(linea + " " + w) > 52:
                lineas.append(linea)
                linea = w
            else:
                linea = (linea + " " + w).strip()
        lineas.append(linea)
        for j, ln in enumerate(lineas):
            b.append(_txt(x + 28, y + 70 + j * 24, ln, 16, INK3, "400"))
    return _svg(292, "".join(b))


def flujo_e2e():
    """Un flujo de orquestación de principio a fin."""
    b = [DEFS]
    b.append(_rect(10, 20, 180, 56, fill=ACC, stroke="none", sw=0, r=10))
    b.append(_txt(100, 54, "petición", 19, "#ffffff", "700", "middle"))
    b.append(_arrow(196, 48, 236, 48, INK3, 2))

    pasos = [
        (246, "Validar", "código", "sin modelo", INK3),
        (438, "Clasificar", "modelo barato", "tres categorías", INK2),
        (630, "Recuperar", "código", "solo si hace falta", INK3),
        (822, "Redactar", "modelo capaz", "la parte con juicio", ACC),
    ]
    for x, t, quien, nota, color in pasos:
        b.append(_rect(x, 20, 176, 92, fill="#ffffff",
                       stroke=color if color != INK3 else HAIR, sw=1.8, r=10))
        b.append(_txt(x + 88, 48, t, 18, INK, "700", "middle"))
        b.append(_txt(x + 88, 74, quien, 15, color, "700", "middle"))
        b.append(_txt(x + 88, 98, nota, 14, INK3, "400", "middle"))
        if x < 822:
            b.append(_arrow(x + 180, 66, x + 190, 66, INK3, 2))

    # rama en paralelo
    b.append('<path d="M 718 118 L 718 166 Q 718 178 730 178 L 892 178" '
             'fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 5" '
             'stroke-linecap="round" marker-end="url(#ahp)"/>' % ACC)
    b.append(_rect(900, 154, 210, 48, fill=ACC_SOFT, stroke=ACC, sw=1.6, r=9))
    b.append(_txt(1005, 184, "en paralelo", 16, ACC, "700", "middle"))

    # traza en segundo plano
    b.append('<path d="M 910 118 L 910 240 Q 910 252 898 252 L 246 252" '
             'fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 5" '
             'stroke-linecap="round" marker-end="url(#ah)"/>' % INK3)
    b.append(_rect(10, 228, 226, 48, fill="#f1f1f5", stroke=HAIR, sw=1.6, r=9))
    b.append(_txt(123, 258, "traza en segundo plano", 15, INK3, "700", "middle"))

    b.append(_rect(10, 300, 1100, 78, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, 336, "De cuatro pasos, uno necesita el modelo capaz.", 21, INK,
                  "700"))
    b.append(_txt(38, 366, "Ejecutar los cuatro con el más caro es matar moscas a "
                           "cañonazos.", 18, INK2, "400"))
    return _svg(396, "".join(b))


def donde_se_rompe():
    """Modos de fallo propios de un sistema orquestado."""
    fallos = [
        ("Error a mitad de la cadena",
         "El paso tres falla y los dos primeros ya tuvieron efectos. Reintentar, "
         "compensar o abortar es diseño, no una excepción.", DANGER),
        ("Contexto perdido en la frontera",
         "La pieza B no recibió un matiz que A sí tenía. Es el fallo más frecuente "
         "y no da error: da una respuesta peor.", WARN),
        ("Bucles entre piezas",
         "A llama a B, B devuelve a A. Los límites de iteración tienen que ser "
         "globales, no por pieza.", DANGER),
        ("Costo invisible",
         "Cada pieza parece barata y la suma no lo es. Sin atribución por paso no "
         "sabes cuál se lleva el presupuesto.", WARN),
    ]
    b = [DEFS]
    for i, (t, d, color) in enumerate(fallos):
        y = 14 + i * 86
        soft = DANGER_SOFT if color == DANGER else WARN_SOFT
        b.append(_rect(10, y, 1100, 74, fill=soft, stroke=color, sw=1.8, r=11))
        b.append(_txt(36, y + 32, t, 20, INK, "700"))
        b.append(_txt(36, y + 58, d, 16, INK2, "400"))
    return _svg(14 + len(fallos) * 86 + 14, "".join(b))
