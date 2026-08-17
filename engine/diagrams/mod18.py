# -*- coding: utf-8 -*-
"""Diagramas del módulo 18 — Seguridad."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def capas_control():
    """Dónde se pone un control y cuánto se puede confiar en él."""
    capas = [
        ("En la ejecución", "permisos, límites, confirmación humana, "
                            "operaciones reversibles",
         "ALTA", "es la única que resiste a un modelo comprometido", OK, OK_SOFT),
        ("Sobre la salida", "validación de esquema, de contenido y de reglas "
                            "de negocio",
         "ALTA", "si es código. Es la capa que de verdad protege", OK, OK_SOFT),
        ("Sobre la entrada", "filtrado y clasificación antes de llegar al modelo",
         "MEDIA", "detecta lo evidente y poco más", WARN, WARN_SOFT),
        ("En el prompt", "instrucciones de comportamiento y límites declarados",
         "BAJA", "es una petición al modelo, no una restricción del sistema",
         DANGER, DANGER_SOFT),
    ]
    b = [DEFS]
    for i, (t, d, fiab, nota, color, fill) in enumerate(capas):
        y = 14 + i * 100
        ancho = 1100 - i * 60
        b.append(_rect(10, y, ancho, 90, fill=fill, stroke=color, sw=1.8, r=11))
        b.append(_txt(36, y + 30, t, 20, INK, "700"))
        b.append(_txt(36, y + 54, d, 16, INK2, "400"))
        b.append(_txt(36, y + 76, nota, 15, color, "600"))
        b.append(_rect(ancho - 116, y + 24, 92, 40, fill=color, stroke="none",
                       sw=0, r=8))
        b.append(_txt(ancho - 70, y + 51, fiab, 15, "#ffffff", "700", "middle",
                      spacing="1.4"))

    b.append(_txt(10, 448, "Cuanto más cerca del código y más lejos del modelo, más "
                           "fiable es el control.", 20, INK, "700"))
    b.append(_txt(10, 474, "Un guardrail que depende de que el modelo obedezca no es "
                           "un control: es una expectativa.", 18, INK3, "400"))
    return _svg(492, "".join(b))


def inyeccion_indirecta():
    """El atacante no habla con el sistema: deja el texto donde lo va a leer."""
    b = [DEFS]
    b.append(_rect(10, 20, 220, 66, fill=DANGER, stroke="none", sw=0, r=11))
    b.append(_txt(120, 50, "el atacante", 18, "#ffffff", "700", "middle"))
    b.append(_txt(120, 72, "nunca te escribe", 15, "#f3c9c9", "400", "middle"))

    b.append(_arrow(236, 54, 288, 54, DANGER, 2.5))

    fuentes = [
        ("un documento", "que vas a indexar"),
        ("una página web", "que una herramienta consulta"),
        ("un ticket", "que el agente procesa"),
        ("un registro", "de tu propia base de datos"),
    ]
    for i, (t, d) in enumerate(fuentes):
        y = 14 + i * 62
        b.append(_rect(298, y, 300, 52, fill=DANGER_SOFT, stroke=DANGER, sw=1.6,
                       r=9))
        b.append(_txt(318, y + 24, t, 17, INK, "700"))
        b.append(_txt(318, y + 44, d, 15, INK2, "400"))
        b.append('<path d="M 604 %d L 660 %d" stroke="%s" stroke-width="2" '
                 'stroke-linecap="round" marker-end="url(#ah)"/>'
                 % (y + 26, 150, DANGER))

    b.append(_rect(670, 112, 200, 78, fill="#ffffff", stroke=INK, sw=2, r=11))
    b.append(_txt(770, 146, "TU CONTEXTO", 15, INK, "700", "middle", spacing="1.6"))
    b.append(_txt(770, 172, "el modelo lo lee", 16, INK3, "400", "middle"))
    b.append(_arrow(878, 150, 926, 150, DANGER, 2.5))

    b.append(_rect(936, 112, 174, 78, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=11))
    b.append(_txt(1023, 146, "acciones", 18, INK, "700", "middle"))
    b.append(_txt(1023, 172, "en tu nombre", 16, DANGER, "700", "middle"))

    b.append(_rect(10, 268, 1100, 100, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(38, 304, "No existe una defensa completa, y conviene decirlo.",
                  21, INK, "700"))
    b.append(_txt(38, 332, "El problema es estructural: el modelo no puede distinguir "
                           "de forma fiable instrucciones", 18, INK2, "400"))
    b.append(_txt(38, 356, "de datos cuando los dos son texto en el mismo contexto.",
                  18, INK2, "400"))
    return _svg(388, "".join(b))


def triada_peligrosa():
    """Las tres condiciones que juntas abren una vía de exfiltración."""
    b = [DEFS]
    items = [
        ("Datos no confiables", "contenido que no escribiste tú entra al contexto"),
        ("Capacidad de actuar", "herramientas con efectos sobre sistemas reales"),
        ("Salida hacia fuera", "puede enviar, publicar o llamar a un tercero"),
    ]
    for i, (t, d) in enumerate(items):
        x = 10 + i * 372
        b.append(_rect(x, 20, 348, 130, fill=DANGER_SOFT, stroke=DANGER, sw=1.8,
                       r=12))
        b.append('<circle cx="%d" cy="60" r="18" fill="%s"/>' % (x + 42, DANGER))
        b.append(_txt(x + 42, 67, str(i + 1), 18, "#ffffff", "700", "middle"))
        b.append(_txt(x + 74, 67, t, 19, INK, "700"))
        palabras, linea, lineas = d.split(), "", []
        for w in palabras:
            if len(linea + " " + w) > 40:
                lineas.append(linea)
                linea = w
            else:
                linea = (linea + " " + w).strip()
        lineas.append(linea)
        for j, ln in enumerate(lineas):
            b.append(_txt(x + 24, 104 + j * 24, ln, 16, INK2, "400"))
        if i < 2:
            b.append(_txt(x + 358, 92, "+", 30, DANGER, "700", "middle"))

    b.append(_rect(10, 178, 1100, 86, fill="#ffffff", stroke=INK, sw=2, r=12))
    b.append(_txt(560, 216, "Si las tres coinciden, hay una vía de exfiltración.",
                  22, INK, "700", "middle"))
    b.append(_txt(560, 248, "Rompe una de las tres y el ataque deja de tener salida.",
                  18, INK3, "400", "middle"))

    b.append(_txt(10, 306, "En la práctica se rompe la segunda o la tercera: separa "
                           "el agente que lee contenido ajeno del que puede actuar.",
                  19, INK3, "400"))
    return _svg(330, "".join(b))


def riesgos_costo():
    """Vaciar el presupuesto es una denegación de servicio."""
    riesgos = [
        ("Bucle de reproceso", "Indexar dispara un evento que vuelve a indexar.",
         "detección de cambios reales y tope por periodo"),
        ("Bucle con herramientas", "El agente itera sin condición de salida.",
         "límite duro de iteraciones, global"),
        ("Amplificación por entrada", "Un documento enorme dispara un "
                                      "procesamiento costoso.",
         "límites de tamaño y presupuesto por usuario"),
        ("Reintentos sin techo", "El proveedor falla y tu código insiste.",
         "espera creciente, tope de intentos y presupuesto"),
    ]
    b = [DEFS]
    for i, (t, d, fix) in enumerate(riesgos):
        y = 14 + i * 90
        b.append(_rect(10, y, 1100, 78, fill="#ffffff", stroke=HAIR, sw=1.6, r=11))
        b.append('<rect x="10" y="%d" width="5" height="78" rx="2.5" fill="%s"/>'
                 % (y, DANGER))
        b.append(_txt(36, y + 32, t, 19, INK, "700"))
        b.append(_txt(36, y + 60, d, 16, INK3, "400"))
        b.append(_rect(640, y + 16, 452, 46, fill=OK_SOFT, stroke=OK, sw=1.6, r=8))
        b.append(_txt(660, y + 45, fix, 16, OK, "700"))
    b.append(_txt(10, 14 + len(riesgos) * 90 + 30,
                  "Una vulnerabilidad que vacía el presupuesto es una denegación de "
                  "servicio con otro nombre.", 20, INK, "700"))
    return _svg(14 + len(riesgos) * 90 + 52, "".join(b))
