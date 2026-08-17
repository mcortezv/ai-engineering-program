# -*- coding: utf-8 -*-
"""Diagramas del modulo 2 - Que es un LLM."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3,
    MONO, OK, OK_SOFT, PAPER, SANS, W, _arrow, _rect, _svg, _txt,
)

from engine.diagrams.brands import _mark, icon_path


def parametro_peso():
    """Qué es un parámetro y por qué el tamaño decide dónde cabe el modelo."""
    b = [DEFS]
    b.append(_rect(10, 14, 500, 188, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(38, 50, "UN PARÁMETRO ES UN NÚMERO", 15, INK3, "700",
                  spacing="2.2"))
    for i, v in enumerate(["0.0231", "−0.4417", "0.1893", "0.0072",
                           "−0.2264", "0.3310", "−0.0918", "0.1247"]):
        b.append(_txt(46 + (i % 4) * 116, 98 + (i // 4) * 40, v, 21, ACC, "500",
                      family=MONO))
    b.append(_txt(38, 184, "Nada más. Un archivo lleno de estos.", 18, INK2, "400"))

    b.append(_rect(548, 14, 562, 188, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(576, 50, "LA CUENTA QUE LO ATERRIZA", 15, ACC, "700",
                  spacing="2.2"))
    b.append(_txt(576, 98, "70 000 000 000", 29, INK, "700", family=MONO))
    b.append(_txt(576, 126, "parámetros × 2 bytes cada uno", 18, INK3, "400"))
    b.append('<line x1="576" y1="144" x2="1082" y2="144" stroke="%s" '
             'stroke-width="1.6"/>' % ACC)
    b.append(_txt(576, 184, "≈ 140 GB solo de números", 26, ACC, "700"))

    y = 244
    b.append(_txt(10, y - 12, "MEMORIA DISPONIBLE, A ESCALA", 15, INK3, "700",
                  spacing="2.2"))
    for i, (label, gb, fill, fg) in enumerate(
            [("Una laptop", 16, "#f1f1f5", INK3),
             ("Un servidor con GPU", 80, "#ded6fa", INK2),
             ("El modelo", 140, ACC, "#ffffff")]):
        yy = y + i * 46
        w = 40 + gb * 6.2
        b.append(_rect(10, yy, w, 34, fill=fill, stroke="none", sw=0, r=6))
        b.append(_txt(26, yy + 24, label, 18, fg, "600"))
        b.append(_txt(w + 26, yy + 24, "%d GB" % gb, 18, INK3, "600", family=MONO))
    b.append(_txt(10, y + 156, "Por eso no corre en tu equipo, por eso necesita "
                               "hardware específico y por eso se cobra por uso.",
                  19, INK3, "400"))
    return _svg(y + 178, "".join(b))


def costo_entrenamiento():
    """Entrenar cuesta una vez; usar cuesta siempre."""
    b = [DEFS]
    b.append(_txt(10, 32, "ENTRENAR UN MODELO FRONTERA — ÓRDENES DE MAGNITUD",
                  15, INK3, "700", spacing="2.2"))
    tarjetas = [
        ("Energía", "decenas\nde GWh",
         "el consumo anual de\nvarios miles de hogares"),
        ("CO₂", "cientos a miles\nde toneladas",
         "compensarlo pide del orden de\ncien mil árboles creciendo un año"),
        ("Agua", "millones\nde litros",
         "refrigeración del centro de datos\nmientras dura el entrenamiento"),
        ("Dinero", "decenas a cientos\nde millones USD",
         "solo el cómputo, sin contar\nel equipo ni los datos"),
    ]
    for i, (t, cifra, nota) in enumerate(tarjetas):
        x = 10 + i * 280
        b.append(_rect(x, 50, 260, 180, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
        b.append(_txt(x + 24, 84, t.upper(), 15, ACC, "700", spacing="2"))
        for j, line in enumerate(cifra.split("\n")):
            b.append(_txt(x + 24, 120 + j * 28, line, 21, INK, "700"))
        for j, line in enumerate(nota.split("\n")):
            b.append(_txt(x + 24, 188 + j * 22, line, 15, INK3, "400"))

    b.append(_rect(10, 252, 1100, 90, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, 288, "Pero ese no es el número que vas a pagar.", 22, INK,
                  "700"))
    b.append(_txt(38, 320, "El entrenamiento lo pagó el proveedor, una vez. Tú pagas "
                           "la inferencia: cada petición, para siempre.", 19, INK2,
                  "400"))
    b.append(_txt(10, 372, "Cifras como orden de magnitud, no como dato cerrado: "
                           "varían mucho según fuente y metodología.",
                  16, INK3, "400"))
    return _svg(390, "".join(b))


def ai_como_servicio():
    """Quién es dueño de cada capa cuando consumes AI."""
    b = [DEFS]
    capas = [
        ("Tu producto", "la interfaz, las reglas de negocio, tus datos",
         "#ffffff", INK, "TÚ", ACC),
        ("Tu orquestación", "qué se manda, en qué orden, con qué contexto",
         "#ffffff", INK, "TÚ", ACC),
        ("La API", "el contrato: modelo, mensajes, parámetros",
         ACC_SOFT, INK, "COMPARTIDO", INK2),
        ("El modelo", "los pesos entrenados", ACC, "#ffffff", "EL PROVEEDOR", INK3),
        ("El cómputo", "las GPU, el centro de datos, la energía",
         "#f1f1f5", INK2, "EL PROVEEDOR", INK3),
    ]
    for i, (t, d, fill, fg, dueno, dcolor) in enumerate(capas):
        y = 14 + i * 64
        b.append(_rect(10, y, 830, 54, fill=fill,
                       stroke=ACC if fill in (ACC, ACC_SOFT) else HAIR,
                       sw=2 if fill in (ACC, ACC_SOFT) else 1.5, r=10))
        b.append(_txt(36, y + 25, t, 20, fg, "700"))
        b.append(_txt(36, y + 46, d, 16, "#d9ccff" if fill == ACC else INK3, "400"))
        b.append(_txt(872, y + 34, dueno, 15, dcolor, "700", spacing="1.8"))
    b.append('<line x1="854" y1="14" x2="854" y2="332" stroke="%s" '
             'stroke-width="1.6" stroke-dasharray="5 5"/>' % HAIR)
    b.append(_txt(10, 374, "Comprar AI como servicio es comprar las dos capas de "
                           "abajo. Las tres de arriba siguen siendo tu trabajo.",
                  19, INK3, "400"))
    return _svg(392, "".join(b))


# ── Módulo 1 ────────────────────────────────────────────────────────────────


def proveedores():
    """Panorama de proveedores, separado por cómo se consume el modelo."""
    cerrados = [("openai", "AI", "OpenAI", "GPT"),
                ("anthropic", "A", "Anthropic", "Claude"),
                ("googlegemini", "G", "Google", "Gemini"),
                (None, "xAI", "xAI", "Grok")]
    abiertos = [("meta", "M", "Meta", "Llama"),
                ("mistralai", "M", "Mistral AI", "Mistral, Mixtral"),
                ("deepseek", "D", "DeepSeek", "DeepSeek V y R"),
                ("qwen", "Q", "Alibaba", "Qwen")]
    b = [DEFS]

    def grupo(x0, titulo, subtitulo, items, color, fill):
        out = [_rect(x0, 10, 528, 322, fill=fill, stroke=color, sw=2, r=14)]
        out.append(_txt(x0 + 26, 46, titulo, 15, color, "700", spacing="2.2"))
        out.append(_txt(x0 + 26, 72, subtitulo, 17, INK3, "400"))
        for i, (slug, mono, nombre, familia) in enumerate(items):
            cx = x0 + 26 + (i % 2) * 250
            cy = 96 + (i // 2) * 112
            out.append(_rect(cx, cy, 234, 94, fill="#ffffff", stroke=HAIR, sw=1.5,
                             r=10))
            out.append(_mark(slug, mono, cx + 44, cy + 47, 36))
            out.append(_txt(cx + 80, cy + 42, nombre, 19, INK, "700"))
            out.append(_txt(cx + 80, cy + 68, familia, 16, INK3, "400"))
        return "".join(out)

    b.append(grupo(10, "SOLO POR API", "Los pesos no salen del proveedor",
                   cerrados, ACC, "#ffffff"))
    b.append(grupo(582, "PESOS ABIERTOS", "Se pueden descargar y hospedar",
                   abiertos, OK, OK_SOFT))
    b.append(_txt(560, 366, "La lista cambia cada pocos meses. La pregunta no: "
                            "¿el dato puede salir de tu infraestructura?",
                  19, INK3, "400", "middle"))
    return _svg(386, "".join(b))

