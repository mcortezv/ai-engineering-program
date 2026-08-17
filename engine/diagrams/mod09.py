# -*- coding: utf-8 -*-
"""Diagramas del módulo 9 — Agentes."""

import math

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def siete_componentes():
    """Lo que necesita un agente, y qué falla si falta."""
    comp = [
        ("Objetivo", "qué intenta lograr y cómo sabe que terminó",
         "no sabe cuándo parar"),
        ("Memoria", "qué recuerda dentro de la tarea y entre tareas",
         "repite pasos que ya hizo"),
        ("Herramientas", "con qué consulta el mundo y actúa sobre él",
         "solo puede hablar"),
        ("Planificación", "cómo descompone el objetivo en pasos",
         "falla en tareas de varios pasos"),
        ("Observación", "cómo lee el resultado de lo que hizo",
         "no detecta que un paso falló"),
        ("Acción", "cómo ejecuta, con qué permisos, qué es reversible",
         "o no puede nada, o puede demasiado"),
        ("Reflexión", "cómo evalúa si va bien y corrige",
         "insiste en lo que no funciona"),
    ]
    b = [DEFS]
    b.append(_txt(10, 30, "QUÉ NECESITA", 14, ACC, "700", spacing="2"))
    b.append(_txt(792, 30, "QUÉ FALLA SI NO ESTÁ", 14, DANGER, "700", spacing="2"))
    b.append('<line x1="10" y1="42" x2="1110" y2="42" stroke="%s" '
             'stroke-width="1.6"/>' % INK3)
    for i, (nombre, que, falla) in enumerate(comp):
        y = 54 + i * 46
        if i % 2 == 1:
            b.append('<rect x="10" y="%d" width="1100" height="42" rx="6" '
                     'fill="#fbfbfd"/>' % y)
        b.append('<circle cx="30" cy="%d" r="4.5" fill="%s"/>' % (y + 26, ACC))
        b.append(_txt(48, y + 32, nombre, 19, INK, "700"))
        b.append(_txt(232, y + 32, que, 17, INK2, "400"))
        b.append(_txt(792, y + 32, falla, 17, DANGER, "500"))
    return _svg(54 + len(comp) * 46 + 20, "".join(b))


def bucle_agente():
    """El ciclo, y la condición de salida que lo define."""
    b = [DEFS]
    cx, cy, r, nr = 300, 196, 116, 44
    etapas = [("decidir", -90), ("actuar", -18), ("observar", 54),
              ("reflexionar", 126), ("recordar", 198)]
    pts = []
    for nombre, ang in etapas:
        a = math.radians(ang)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a), nombre))

    # Flechas rectas entre los bordes de cada par: se ven mucho mejor que arcos.
    for i, (x, y, _) in enumerate(pts):
        nx, ny, _ = pts[(i + 1) % len(pts)]
        dx, dy = nx - x, ny - y
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="2.5" marker-end="url(#ahp)"/>'
                 % (x + ux * (nr + 5), y + uy * (nr + 5),
                    x + ux * (d - nr - 10), y + uy * (d - nr - 10), ACC))

    for x, y, nombre in pts:
        b.append('<circle cx="%.1f" cy="%.1f" r="%d" fill="#ffffff" stroke="%s" '
                 'stroke-width="2"/>' % (x, y, nr, ACC))
        b.append(_txt(x, y + 6, nombre, 15, INK, "700", "middle"))
    b.append('<circle cx="%d" cy="%d" r="48" fill="%s"/>' % (cx, cy, ACC))
    b.append(_txt(cx, cy - 2, "OBJETIVO", 13, "#ffffff", "700", "middle",
                  spacing="1.4"))
    b.append(_txt(cx, cy + 20, "y su fin", 13, "#d9ccff", "400", "middle"))

    b.append(_rect(560, 56, 550, 284, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(590, 96, "LA CONDICIÓN DE SALIDA", 15, DANGER, "700",
                  spacing="2.2"))
    b.append(_txt(590, 136, "El bucle termina cuando:", 20, INK, "700"))
    for j, ln in enumerate(["se cumple el objetivo",
                            "se agota el presupuesto",
                            "se alcanza el límite de iteraciones"]):
        b.append('<circle cx="600" cy="%d" r="4" fill="%s"/>' % (170 + j * 32, DANGER))
        b.append(_txt(616, 176 + j * 32, ln, 18, INK2, "400"))
    b.append('<line x1="590" y1="278" x2="1082" y2="278" stroke="%s" '
             'stroke-width="1.4"/>' % DANGER)
    b.append(_txt(590, 306, "Sin límite duro no es un agente:", 17, DANGER, "700"))
    b.append(_txt(590, 328, "es un incidente de facturación esperando su turno.",
                  17, DANGER, "700"))
    return _svg(370, "".join(b))


def flujo_vs_agente():
    """Cuándo conviene cada uno."""
    filas = [
        ("Los pasos se conocen de antemano y siempre son los mismos", "flujo"),
        ("Los pasos dependen de lo que se vaya encontrando", "agente"),
        ("El costo de un error es alto y difícil de revertir", "flujo"),
        ("El espacio de caminos posibles es grande y no se puede enumerar", "agente"),
        ("Hace falta que el resultado sea reproducible", "flujo"),
    ]
    b = [DEFS]
    b.append(_rect(760, 14, 168, 44, fill=INK2, stroke="none", sw=0, r=8))
    b.append(_txt(844, 44, "FLUJO", 16, "#ffffff", "700", "middle", spacing="2"))
    b.append(_rect(942, 14, 168, 44, fill=ACC, stroke="none", sw=0, r=8))
    b.append(_txt(1026, 44, "AGENTE", 16, "#ffffff", "700", "middle", spacing="2"))

    for i, (cond, cual) in enumerate(filas):
        y = 70 + i * 50
        if i % 2 == 0:
            b.append('<rect x="10" y="%d" width="1100" height="46" rx="7" '
                     'fill="#fbfbfd"/>' % y)
        b.append(_txt(30, y + 30, cond, 18, INK2, "400"))
        x = 844 if cual == "flujo" else 1026
        color = INK2 if cual == "flujo" else ACC
        b.append('<circle cx="%d" cy="%d" r="12" fill="%s"/>' % (x, y + 24, color))
        # Marca dibujada: Figtree no trae el glifo y Chrome metia una fuente
        # de respaldo como Type3, que se imprime mal definida.
        b.append('<path d="M %d %d l 3.4 3.6 l 6.2 -7" fill="none" stroke="#fff" '
                 'stroke-width="2.4" stroke-linecap="round" '
                 'stroke-linejoin="round"/>' % (x - 5, y + 24))

    y = 70 + len(filas) * 50
    b.append(_rect(10, y + 12, 1100, 62, fill=ACC_SOFT, stroke=ACC, sw=2, r=11))
    b.append(_txt(560, y + 50, "Un flujo de trabajo no necesita un agente para ser "
                               "un sistema de AI.", 21, INK, "700", "middle"))
    return _svg(y + 96, "".join(b))


def tool_skill_mcp():
    """Tres conceptos que se confunden todo el tiempo."""
    items = [
        ("HERRAMIENTA", "Una función que el agente puede ejecutar.", "Es capacidad.",
         "un verbo", "leer un archivo, consultar la base, enviar un correo", ACC),
        ("SKILL", "Instrucciones sobre cómo hacer bien algo.",
         "Es conocimiento procedimental.",
         "un manual", "cómo redactamos aquí una propuesta comercial", OK),
        ("SERVIDOR MCP", "Un canal estandarizado por el que llegan herramientas "
                         "y datos.", "Es transporte.",
         "un enchufe", "no es la herramienta: es por donde se conecta", INK2),
    ]
    b = [DEFS]
    for i, (t, que, tipo, analogia, ej, color) in enumerate(items):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 268, fill="#ffffff", stroke=color, sw=2, r=12))
        b.append(_txt(x + 24, 50, t, 15, color, "700", spacing="2"))
        words, line, lines = que.split(), "", []
        for w in words:
            if len(line + " " + w) > 32:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(x + 24, 88 + j * 26, ln, 18, INK, "500"))
        yy = 88 + len(lines) * 26 + 10
        b.append(_txt(x + 24, yy, tipo, 18, color, "700"))
        b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                 'stroke-width="1.4"/>' % (x + 24, yy + 18, x + 324, yy + 18, HAIR))
        b.append(_txt(x + 24, yy + 46, "Es como…", 14, INK3, "700", spacing="1.6"))
        b.append(_txt(x + 24, yy + 74, analogia, 22, INK, "700"))
        words, line, lines = ej.split(), "", []
        for w in words:
            if len(line + " " + w) > 36:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(x + 24, yy + 104 + j * 22, ln, 15, INK3, "400"))

    b.append(_txt(560, 320, "Una skill no hace nada por sí sola: describe cómo "
                            "hacerlo. Una herramienta sí hace algo. MCP es por "
                            "dónde llega.", 20, INK, "700", "middle"))
    return _svg(342, "".join(b))


def uso_herramientas():
    """El mecanismo real: el modelo no ejecuta nada."""
    pasos = [
        ("1", "Le pasas la lista", "nombre, descripción y parámetros\nde cada herramienta"),
        ("2", "El modelo pide", "en vez de texto, produce\n«quiero llamar a X con Y»"),
        ("3", "TU CÓDIGO ejecuta", "el modelo se queda esperando\nsin saber qué pasa"),
        ("4", "Devuelves el resultado", "se añade al historial y se hace\nuna petición nueva"),
        ("5", "El modelo decide", "otra herramienta,\no responder"),
    ]
    b = [DEFS]
    for i, (n, t, d) in enumerate(pasos):
        x = 10 + i * 224
        destacado = i == 2
        b.append(_rect(x, 30, 204, 158, fill=ACC if destacado else "#ffffff",
                       stroke=ACC if destacado else HAIR,
                       sw=2 if destacado else 1.5, r=11))
        b.append('<circle cx="%d" cy="%d" r="16" fill="%s"/>'
                 % (x + 30, 62, "#ffffff" if destacado else ACC))
        b.append(_txt(x + 30, 68, n, 16, ACC if destacado else "#ffffff", "700",
                      "middle"))
        b.append(_txt(x + 58, 68, t, 17, "#ffffff" if destacado else INK, "700"))
        for j, ln in enumerate(d.split("\n")):
            b.append(_txt(x + 22, 112 + j * 24, ln, 15,
                          "#d9ccff" if destacado else INK3, "400"))
        if i < len(pasos) - 1:
            b.append(_arrow(x + 208, 109, x + 230, 109, INK3, 2))

    b.append(_rect(10, 214, 1100, 62, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=11))
    b.append(_txt(560, 252, "El modelo no ejecuta nada. Pide, y tu código decide si "
                            "obedece.", 21, INK, "700", "middle"))
    b.append(_txt(560, 306, "Y cada vuelta del bucle reenvía todo el contexto "
                            "acumulado: diez pasos no cuestan diez veces uno.",
                  18, INK3, "400", "middle"))
    return _svg(326, "".join(b))
