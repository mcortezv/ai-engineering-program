# -*- coding: utf-8 -*-
"""Diagramas del módulo 6 — La escalera de adaptación de un modelo."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, _arrow, _rect, _svg, _txt,
)


def escalera():
    """Los cinco escalones, con su costo de iteración."""
    pasos = [
        ("Prompt", ["cambiar las instrucciones"], "segundos", "total"),
        ("Contexto", ["meter la información", "en la petición"], "minutos", "total"),
        ("RAG", ["recuperar lo relevante", "en automático"], "días", "alta"),
        ("Herramientas", ["dejar que consulte", "y actúe"], "días", "alta"),
        ("Fine tuning", ["modificar los pesos"], "semanas", "baja"),
    ]
    b = [DEFS]
    n = len(pasos)
    bw, bh, gap, rise, base = 208, 86, 12, 38, 200
    for i, (nombre, lineas, tiempo, rev) in enumerate(pasos):
        x = 10 + i * (bw + gap)
        y = base - i * rise
        ultimo = i == n - 1
        b.append(_rect(x, y, bw, bh, fill=ACC if ultimo else "#ffffff",
                       stroke=ACC if ultimo else HAIR,
                       sw=2 if ultimo else 1.5, r=10))
        b.append(_txt(x + bw / 2.0, y + 30, nombre, 20,
                      "#ffffff" if ultimo else INK, "700", "middle"))
        y0 = y + (58 if len(lineas) == 1 else 52)
        for j, ln in enumerate(lineas):
            b.append(_txt(x + bw / 2.0, y0 + j * 20, ln, 14,
                          "#d9ccff" if ultimo else INK3, "400", "middle"))
        # peldaño
        if i < n - 1:
            b.append('<path d="M %d %d L %d %d" stroke="%s" stroke-width="2" '
                     'stroke-dasharray="4 4"/>'
                     % (x + bw, y + bh / 2, x + bw + gap, y + bh / 2 - rise, HAIR))
        b.append(_txt(x + bw / 2.0, y + bh + 26, tiempo, 15, INK3, "600", "middle",
                      family=MONO))
        b.append(_txt(x + bw / 2.0, y + bh + 46, "reversible: " + rev, 14,
                      OK if rev == "total" else (INK3 if rev == "alta" else DANGER),
                      "600", "middle"))

    b.append('<path d="M 20 372 L 1100 372" stroke="%s" stroke-width="2" '
             'marker-end="url(#ahp)"/>' % ACC)
    b.append(_txt(20, 362, "más barato y más rápido de deshacer", 17, INK3, "400"))
    b.append(_txt(1100, 362, "más caro y más difícil de deshacer", 17, ACC, "700",
                  "end"))
    b.append(_txt(560, 414, "Se sube de escalón cuando el anterior se agotó, "
                            "no cuando se puso difícil.", 21, INK, "700", "middle"))
    return _svg(434, "".join(b))


def sabe_o_puede():
    """La pregunta que resuelve la decisión, y su prueba diagnóstica."""
    b = [DEFS]
    b.append(_rect(360, 12, 400, 62, fill=ACC, stroke="none", sw=0, r=11))
    b.append(_txt(560, 52, "el modelo no hace lo que necesito", 20, "#ffffff",
                  "700", "middle"))
    b.append(_arrow(470, 78, 300, 104, ACC, 2.5))
    b.append(_arrow(650, 78, 820, 104, ACC, 2.5))

    b.append(_rect(10, 110, 530, 176, fill="#ffffff", stroke=INK3, sw=2, r=12))
    b.append(_txt(40, 150, "NO SABE", 15, INK3, "700", spacing="2.2"))
    b.append(_txt(40, 186, "Le falta la información", 24, INK, "700"))
    b.append(_txt(40, 218, "Tus precios, tus documentos, lo que", 18, INK2, "400"))
    b.append(_txt(40, 242, "pasó ayer. No está en ninguna parte.", 18, INK2, "400"))
    b.append(_txt(40, 272, "→ contexto, recuperación, herramientas", 18, INK3, "700"))

    b.append(_rect(580, 110, 530, 176, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(610, 150, "NO PUEDE", 15, ACC, "700", spacing="2.2"))
    b.append(_txt(610, 186, "Tiene todo y aun así falla", 24, INK, "700"))
    b.append(_txt(610, 218, "No sostiene el formato, no mantiene", 18, INK2, "400"))
    b.append(_txt(610, 242, "el tono, falla en un criterio propio.", 18, INK2, "400"))
    b.append(_txt(610, 272, "→ aquí entra el fine tuning en la conversación",
                  18, ACC, "700"))

    b.append(_rect(10, 306, 1100, 78, fill=OK_SOFT, stroke=OK, sw=2, r=12))
    b.append(_txt(40, 342, "La prueba diagnóstica", 20, OK, "700"))
    b.append(_txt(40, 370, "Pega la información directamente en el prompt. Si con eso "
                           "acierta, tu problema era de contexto y acabas de "
                           "ahorrarte tres semanas.", 18, INK2, "400"))
    return _svg(400, "".join(b))
