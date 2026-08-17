# -*- coding: utf-8 -*-
"""Diagramas del módulo 17 — Buenas prácticas."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def practicas():
    """Cada práctica con el hecho que la sostiene."""
    filas = [
        ("No meter todo en las instrucciones fijas",
         "se paga en cada petición y diluye la señal"),
        ("Dividir el contexto por dominio",
         "cada pieza recibe lo suyo: más preciso y más barato"),
        ("Cargar contexto solo cuando hace falta",
         "el mismo patrón de los procedimientos y de la recuperación"),
        ("Resolver por código lo que se pueda",
         "una regla determinista es más barata, rápida y confiable"),
        ("Reducir el número de peticiones",
         "cada viaje reenvía el contexto acumulado"),
        ("Acotar el historial por mensajes y tokens",
         "el costo crece con el cuadrado de la longitud"),
        ("Usar modelos distintos según la tarea",
         "tres de cada cuatro pasos suelen ser mecánicos"),
        ("Versionar los prompts",
         "sin versión no puedes responder qué cambió"),
    ]
    b = [DEFS]
    b.append(_txt(10, 30, "LA PRÁCTICA", 14, ACC, "700", spacing="2"))
    b.append(_txt(560, 30, "EL HECHO QUE LA SOSTIENE", 14, INK3, "700", spacing="2"))
    b.append('<line x1="10" y1="42" x2="1110" y2="42" stroke="%s" '
             'stroke-width="1.6"/>' % INK3)
    for i, (t, d) in enumerate(filas):
        y = 54 + i * 40
        if i % 2 == 1:
            b.append('<rect x="10" y="%d" width="1100" height="36" rx="7" '
                     'fill="#fbfbfd"/>' % y)
        b.append('<circle cx="30" cy="%d" r="4.5" fill="%s"/>' % (y + 18, ACC))
        b.append(_txt(48, y + 24, t, 18, INK, "600"))
        b.append(_txt(560, y + 24, d, 17, INK3, "400"))
    return _svg(54 + len(filas) * 40 + 18, "".join(b))


def por_codigo():
    """Qué no necesita al modelo."""
    casos = [
        ("Validar un formato", "una expresión regular"),
        ("Ordenar, filtrar o contar", "una consulta a la base"),
        ("Enrutar por categorías fijas", "un diccionario o un switch"),
        ("Calcular", "una función, no la aritmética del modelo"),
        ("Buscar por identificador", "un índice"),
        ("Rellenar una plantilla", "interpolación de cadenas"),
    ]
    b = [DEFS]
    for i, (t, d) in enumerate(casos):
        x = 10 + (i % 3) * 372
        y = 14 + (i // 3) * 104
        b.append(_rect(x, y, 348, 88, fill=OK_SOFT, stroke=OK, sw=1.7, r=11))
        b.append(_txt(x + 24, y + 38, t, 19, INK, "700"))
        b.append(_txt(x + 24, y + 66, d, 16, OK, "600"))
    b.append(_rect(10, 234, 1100, 84, fill="#ffffff", stroke=INK, sw=2, r=12))
    b.append(_txt(38, 270, "Si la entrada es estructurada y la regla es escribible, "
                           "no hace falta el modelo.", 21, INK, "700"))
    b.append(_txt(38, 300, "El modelo se reserva para lo que requiere juicio sobre "
                           "lenguaje natural ambiguo.", 18, INK2, "400"))
    return _svg(338, "".join(b))


def arquitectura_limpia():
    """El flujo completo con las prácticas aplicadas."""
    b = [DEFS]
    b.append(_rect(10, 18, 176, 54, fill=ACC, stroke="none", sw=0, r=10))
    b.append(_txt(98, 52, "entrada", 19, "#ffffff", "700", "middle"))

    pasos = [
        (206, "Validación", "por código", INK3, "#ffffff"),
        (206, "Enrutamiento", "por reglas", INK3, "#ffffff"),
    ]
    y = 18
    for x, t, q, color, fill in pasos:
        b.append(_rect(x, y, 210, 54, fill=fill, stroke=HAIR, sw=1.6, r=10))
        b.append(_txt(x + 20, y + 26, t, 18, INK, "700"))
        b.append(_txt(x + 20, y + 46, q, 15, INK3, "400"))
        y += 66
    b.append(_arrow(192, 46, 202, 46, INK3, 2))

    b.append(_rect(436, 18, 232, 120, fill=OK_SOFT, stroke=OK, sw=1.7, r=10))
    b.append(_txt(456, 46, "¿Hace falta", 18, INK, "700"))
    b.append(_txt(456, 68, "contexto externo?", 18, INK, "700"))
    b.append(_txt(456, 96, "recuperación +", 16, OK, "600"))
    b.append(_txt(456, 118, "reordenamiento", 16, OK, "600"))
    b.append(_txt(456, 134, "poco y bueno", 14, INK3, "400"))

    b.append(_rect(690, 18, 210, 54, fill="#f1f1f5", stroke=HAIR, sw=1.6, r=10))
    b.append(_txt(710, 46, "Modelo barato", 18, INK, "700"))
    b.append(_txt(710, 66, "clasificar, extraer", 15, INK3, "400"))
    b.append(_rect(690, 84, 210, 54, fill=ACC, stroke="none", sw=0, r=10))
    b.append(_txt(710, 112, "Modelo capaz", 18, "#ffffff", "700"))
    b.append(_txt(710, 132, "la parte con juicio", 15, "#d9ccff", "400"))

    b.append(_rect(922, 18, 188, 54, fill=DANGER_SOFT, stroke=DANGER, sw=1.7, r=10))
    b.append(_txt(942, 46, "Validar salida", 18, INK, "700"))
    b.append(_txt(942, 66, "esquema + reglas", 15, INK2, "400"))
    b.append(_rect(922, 84, 188, 54, fill="#f1f1f5", stroke=HAIR, sw=1.6, r=10))
    b.append(_txt(942, 112, "Traza", 18, INK, "700"))
    b.append(_txt(942, 132, "asíncrona", 15, INK3, "400"))

    b.append(_arrow(676, 78, 686, 78, INK3, 2))
    b.append(_arrow(906, 78, 916, 78, INK3, 2))

    invariantes = [
        "prefijo estable al inicio del prompt", "historial acotado",
        "límite de iteraciones", "presupuesto por sesión",
    ]
    b.append('<line x1="10" y1="176" x2="1110" y2="176" stroke="%s" '
             'stroke-width="1.6"/>' % HAIR)
    b.append(_txt(10, 208, "EN TODO EL FLUJO, SIEMPRE", 14, INK3, "700",
                  spacing="2"))
    for i, t in enumerate(invariantes):
        x = 10 + i * 278
        b.append(_rect(x, 224, 262, 52, fill=ACC_SOFT, stroke=ACC, sw=1.6, r=9))
        b.append(_txt(x + 131, 256, t, 16, ACC, "700", "middle"))
    return _svg(296, "".join(b))
