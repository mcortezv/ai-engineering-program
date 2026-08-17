# -*- coding: utf-8 -*-
"""Diagramas del módulo 14 — Costos de un sistema de AI."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def anatomia_peticion():
    """Todo lo que se factura como entrada, y lo poco que escribió el usuario."""
    partes = [
        ("Instrucciones fijas", 10, "#6f52dd"),
        ("Definiciones de herramientas", 17, "#8a70e6"),
        ("Historial de la conversación", 31, ACC),
        ("Contexto recuperado", 24, "#a892ee"),
        ("Resultados de herramientas", 13, "#c4b6f4"),
        ("La pregunta del usuario", 5, "#ded6fa"),
    ]
    b = [DEFS]
    b.append(_txt(10, 32, "LO QUE SE FACTURA COMO ENTRADA EN CADA PETICIÓN", 15,
                  INK3, "700", spacing="2.2"))
    x = 10.0
    for nombre, pct, color in partes:
        w = 1100 * pct / 100.0
        b.append('<rect x="%.1f" y="50" width="%.1f" height="78" fill="%s"/>'
                 % (x, w, color))
        if pct >= 10:
            b.append(_txt(x + w / 2.0, 96, "%d%%" % pct, 21,
                          "#ffffff" if pct >= 17 else INK2, "700", "middle"))
        x += w
    b.append(_rect(10, 50, 1100, 78, fill="none", stroke=INK, sw=2, r=0))

    for i, (nombre, pct, color) in enumerate(partes):
        px = 10 + (i % 3) * 372
        py = 160 + (i // 3) * 42
        b.append('<rect x="%d" y="%d" width="22" height="22" rx="5" fill="%s"/>'
                 % (px, py, color))
        b.append(_txt(px + 32, py + 17, "%s · %d%%" % (nombre, pct), 18, INK2, "400"))

    b.append(_rect(10, 260, 1100, 78, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, 296, "La pregunta del usuario es el 5%. El resto lo pusiste tú.",
                  21, INK, "700"))
    b.append(_txt(38, 326, "Y la salida se cobra aparte, del orden de tres a cinco "
                           "veces más caro por token que la entrada.", 18, INK2,
                  "400"))
    return _svg(358, "".join(b))


def cache_prefijo():
    """Cómo funciona el caché y qué lo rompe."""
    b = [DEFS]
    b.append(_txt(10, 30, "UNA PETICIÓN, VISTA POR EL CACHÉ", 15, INK3, "700",
                  spacing="2.2"))
    bloques = [
        ("Instrucciones fijas", 330, True), ("Herramientas", 230, True),
        ("Documentos fijos", 220, True), ("Historial", 190, False),
        ("Pregunta", 118, False),
    ]
    x = 10
    for nombre, w, estable in bloques:
        fill = OK_SOFT if estable else "#f1f1f5"
        stroke = OK if estable else HAIR
        b.append(_rect(x, 48, w, 62, fill=fill, stroke=stroke, sw=1.6, r=9))
        b.append(_txt(x + w / 2.0, 84, nombre, 16, INK, "600", "middle"))
        x += w + 6
    b.append('<path d="M 10 122 L 800 122" stroke="%s" stroke-width="2.5"/>' % OK)
    b.append(_txt(10, 148, "PREFIJO ESTABLE — se lee del caché, del orden de una "
                           "décima parte del precio", 16, OK, "700"))
    b.append('<path d="M 812 122 L 1110 122" stroke="%s" stroke-width="2.5"/>' % INK3)
    b.append(_txt(812, 148, "cambia cada vez — se paga completo", 16, INK3, "700"))

    rompe = [
        ("Una marca de tiempo en las instrucciones", "invalida el caché en cada llamada"),
        ("Reordenar las herramientas", "aunque sean exactamente las mismas"),
        ("Truncar el historial por el principio", "cambia el inicio del prompt"),
    ]
    b.append(_txt(10, 202, "TRES FORMAS DE ROMPERLO SIN DARSE CUENTA", 15, DANGER,
                  "700", spacing="2.2"))
    for i, (t, d) in enumerate(rompe):
        x = 10 + i * 372
        b.append(_rect(x, 218, 348, 96, fill=DANGER_SOFT, stroke=DANGER, sw=1.6,
                       r=11))
        b.append(_txt(x + 22, 252, t, 17, INK, "700"))
        b.append(_txt(x + 22, 282, d, 15, INK2, "400"))

    b.append(_txt(10, 352, "La consecuencia de diseño: todo lo estable al principio "
                           "del prompt, todo lo variable al final.", 20, INK, "700"))
    return _svg(374, "".join(b))


def crecimiento_cuadratico():
    """Lo que se acumula al reenviar el historial completo."""
    b = [DEFS]
    b.append(_txt(10, 30, "TOKENS ACUMULADOS AL CABO DE N TURNOS", 15, INK3, "700",
                  spacing="2.2"))
    ox, oy, w, h = 60, 268, 1000, 200
    b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="2"/>' % (ox, oy, ox + w, oy, INK3))
    b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="2"/>' % (ox, oy, ox, oy - h - 12, INK3))

    # lineal contra cuadratica
    puntos_lin, puntos_cua = [], []
    for n in range(0, 21):
        x = ox + n * w / 20.0
        puntos_lin.append("%.1f,%.1f" % (x, oy - (n / 20.0) * 20 / 210.0 * h))
        puntos_cua.append("%.1f,%.1f" % (x, oy - (n * (n + 1) / 2.0) / 210.0 * h))
    b.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.5" '
             'stroke-dasharray="7 5" stroke-linecap="round"/>'
             % (" ".join(puntos_lin), INK3))
    b.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="4" '
             'stroke-linecap="round"/>' % (" ".join(puntos_cua), ACC))

    b.append(_txt(ox + w - 6, oy - h + 4, "lo que de verdad pagas", 18, ACC, "700",
                  "end"))
    b.append(_txt(ox + w - 6, oy - 22, "lo que crees que pagas", 17, INK3, "600",
                  "end"))
    for n, lab in ((0, "1"), (10, "10"), (20, "20")):
        x = ox + n * w / 20.0
        b.append(_txt(x, oy + 26, lab, 16, INK3, "400", "middle", family=MONO))
    b.append(_txt(ox + w / 2.0, oy + 52, "turno", 16, INK3, "400", "middle"))

    b.append(_rect(10, 306, 1100, 76, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, 342, "En veinte turnos has enviado 210 veces T, no 20 veces T.",
                  21, INK, "700"))
    b.append(_txt(38, 370, "El costo de una conversación crece con el cuadrado de su "
                           "longitud.", 18, INK2, "400"))
    return _svg(400, "".join(b))


def palancas():
    """Las diez palancas, ordenadas por impacto."""
    filas = [
        ("No llamar al modelo", "una regla, una consulta o un caché exacto",
         "infinito", ACC),
        ("Recuperar menos y mejor", "menos trozos irrelevantes en el prompt",
         "muy alto", ACC),
        ("Estabilizar el prefijo", "para que el caché se aproveche", "muy alto", ACC),
        ("Rutear por tarea", "el modelo caro solo donde importa", "alto", INK2),
        ("Limitar la salida", "tope de tokens y formato estructurado", "alto", INK2),
        ("Procesar por lotes", "todo lo que no sea interactivo", "alto", INK2),
        ("Truncar y resumir", "el historial no puede crecer sin techo", "medio", INK2),
        ("Menos viajes de ida y vuelta", "en los bucles con herramientas", "medio", INK2),
        ("Reducir dimensiones", "y cuantizar el almacenamiento vectorial", "medio", INK3),
        ("Reprocesar por diferencias", "nunca el corpus completo por defecto",
         "medio", INK3),
    ]
    b = [DEFS]
    for i, (t, d, impacto, color) in enumerate(filas):
        y = 14 + i * 40
        if i % 2 == 0:
            b.append('<rect x="10" y="%d" width="1100" height="36" rx="7" '
                     'fill="#fbfbfd"/>' % y)
        b.append('<circle cx="34" cy="%d" r="13" fill="%s"/>' % (y + 18, color))
        b.append(_txt(34, y + 24, "%02d" % (i + 1), 14, "#ffffff", "700", "middle",
                      family=MONO))
        b.append(_txt(60, y + 24, t, 19, INK, "700"))
        b.append(_txt(430, y + 24, d, 17, INK3, "400"))
        b.append(_txt(1100, y + 24, impacto, 16, color, "700", "end"))
    return _svg(14 + len(filas) * 40 + 14, "".join(b))


def guardas():
    """Los topes que no son opcionales."""
    items = [
        ("Presupuesto por sesión, usuario y día", "con corte automático, no con alerta"),
        ("Límite duro de iteraciones", "en cualquier bucle con herramientas"),
        ("Atribución por funcionalidad y cliente", "para saber qué recortar cuando suba"),
        ("Alertas por desviación", "contra la tendencia, no contra un umbral fijo"),
    ]
    b = [DEFS]
    for i, (t, d) in enumerate(items):
        x = 10 + (i % 2) * 560
        y = 14 + (i // 2) * 104
        b.append(_rect(x, y, 540, 88, fill=DANGER_SOFT, stroke=DANGER, sw=1.8, r=11))
        b.append(_txt(x + 26, y + 38, t, 19, INK, "700"))
        b.append(_txt(x + 26, y + 66, d, 17, INK2, "400"))
    b.append(_txt(560, 250, "Un agente sin tope de iteraciones no es un riesgo "
                            "teórico: es un incidente de facturación esperando su "
                            "turno.", 20, INK, "700", "middle"))
    return _svg(272, "".join(b))
