# -*- coding: utf-8 -*-
"""Diagramas del módulo 5 — Prompt engineering."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, SANS, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def roles():
    """Los tres roles de una petición y qué carga cada uno."""
    filas = [
        ("system", "Quién es, qué reglas sigue, qué formato produce",
         "estable entre peticiones", ACC, ACC_SOFT),
        ("user", "La petición concreta y el material que la acompaña",
         "cambia cada vez", INK2, "#ffffff"),
        ("assistant", "Lo que respondió antes — y lo que le pones en la boca",
         "guía el formato", INK2, "#ffffff"),
    ]
    b = [DEFS]
    b.append(_txt(10, 32, "UNA PETICIÓN NO ES UNA CADENA DE TEXTO: ES UNA LISTA DE "
                          "MENSAJES CON ROL", 15, INK3, "700", spacing="2.2"))
    for i, (rol, que, nota, color, fill) in enumerate(filas):
        y = 52 + i * 86
        b.append(_rect(10, y, 1100, 74, fill=fill, stroke=color, sw=2 if i == 0 else 1.5,
                       r=11))
        b.append(_rect(30, y + 18, 152, 38, fill=color, stroke="none", sw=0, r=7))
        b.append(_txt(106, y + 44, rol, 19, "#ffffff", "700", "middle", family=MONO))
        b.append(_txt(206, y + 34, que, 19, INK, "500"))
        b.append(_txt(206, y + 58, nota, 16, INK3, "400"))
    b.append('<path d="M 1070 52 L 1090 52 L 1090 300 L 1070 300" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    b.append(_txt(10, 348, "Lo estable va arriba y lo variable abajo. Esa disciplina "
                           "sirve para la calidad y, más adelante, también para el "
                           "bolsillo.", 19, INK3, "400"))
    return _svg(368, "".join(b))


def anatomia_prompt():
    """Un prompt delimitado, bloque por bloque."""
    b = [DEFS]
    bloques = [
        ("instrucciones", "qué hacer, en positivo y con criterios medibles", ACC),
        ("documento", "el material de referencia, separado del resto", INK3),
        ("formato_salida", "la forma exacta que debe tener la respuesta", OK),
    ]
    y = 20
    for nombre, desc, color in bloques:
        b.append(_rect(10, y, 700, 88, fill="#f7f7fa", stroke=HAIR, sw=1.5, r=8))
        b.append('<rect x="10" y="%d" width="4" height="88" rx="2" fill="%s"/>'
                 % (y, color))
        b.append(_txt(36, y + 32, "&lt;%s&gt;" % nombre, 19, color, "600",
                      family=MONO))
        b.append(_txt(52, y + 60, "…", 19, INK3, "400", family=MONO))
        b.append(_txt(36, y + 82, "&lt;/%s&gt;" % nombre, 19, color, "600",
                      family=MONO))
        b.append(_txt(740, y + 50, desc, 18, INK2, "400"))
        y += 104

    b.append(_rect(10, y + 8, 1100, 76, fill=ACC_SOFT, stroke=ACC, sw=2, r=11))
    b.append(_txt(36, y + 42, "Los delimitadores no funcionan porque el modelo "
                              "«entienda XML».", 20, INK, "700"))
    b.append(_txt(36, y + 70, "Funcionan porque marcan fronteras inequívocas en la "
                              "secuencia, y eso le da señales claras de dónde empieza "
                              "y termina cada bloque.", 17, INK2, "400"))
    return _svg(y + 106, "".join(b))


def rigor_salida():
    """Tres niveles de garantía en una salida estructurada."""
    niveles = [
        ("PEDIRLO EN EL PROMPT", "«Responde solo con JSON»",
         "Nada.", "Funciona casi siempre y falla justo cuando hay volumen: añade "
                  "texto alrededor, cercas de código o disculpas.",
         DANGER, DANGER_SOFT),
        ("MODO JSON", "Un parámetro de la petición",
         "Que parsea.", "No que tenga los campos que esperabas ni los tipos "
                        "correctos. Solo que es JSON válido.",
         WARN, WARN_SOFT),
        ("ESQUEMA FORZADO", "Se declara la forma y el proveedor la impone",
         "Estructura y tipos.", "Sigue sin garantizar que el contenido sea "
                                "verdadero. Eso no lo da ningún mecanismo.",
         OK, OK_SOFT),
    ]
    b = [DEFS]
    for i, (t, como, garantiza, nota, color, fill) in enumerate(niveles):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 268, fill=fill, stroke=color, sw=2, r=12))
        b.append(_txt(x + 24, 48, t, 14, color, "700", spacing="1.6"))
        b.append(_txt(x + 24, 80, como, 17, INK2, "500"))
        b.append('<line x1="%d" y1="98" x2="%d" y2="98" stroke="%s" '
                 'stroke-width="1"/>' % (x + 24, x + 324, color))
        b.append(_txt(x + 24, 126, "QUÉ GARANTIZA", 13, INK3, "700", spacing="1.6"))
        b.append(_txt(x + 24, 156, garantiza, 21, INK, "700"))
        words, line, lines = nota.split(), "", []
        for w in words:
            if len(line + " " + w) > 36:
                lines.append(line); line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for j, ln in enumerate(lines):
            b.append(_txt(x + 24, 190 + j * 24, ln, 16, INK3, "400"))
        if i < 2:
            b.append(_arrow(x + 352, 148, x + 372, 148, INK3, 2))

    b.append(_rect(10, 300, 1100, 62, fill="#ffffff", stroke=INK, sw=2, r=11))
    b.append(_txt(560, 338, "El esquema garantiza la forma, nunca la verdad.",
                  22, INK, "700", "middle"))
    return _svg(378, "".join(b))


def ejemplos_vs_instrucciones():
    """Qué comunica mejor cada herramienta."""
    b = [DEFS]
    b.append(_rect(10, 14, 540, 230, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, 50, "LOS EJEMPLOS COMUNICAN", 15, ACC, "700", spacing="2.2"))
    b.append(_txt(38, 96, "FORMA", 34, INK, "700"))
    b.append(_txt(38, 134, "Cómo debe verse la salida. Si te cuesta", 18, INK2, "400"))
    b.append(_txt(38, 160, "describirlo con palabras, enséñalo.", 18, INK2, "400"))
    b.append(_txt(38, 206, "tono · estructura · longitud · estilo", 17, ACC, "600"))

    b.append(_rect(570, 14, 540, 230, fill="#ffffff", stroke=HAIR, sw=1.5, r=12))
    b.append(_txt(598, 50, "LAS INSTRUCCIONES COMUNICAN", 15, INK3, "700",
                  spacing="2.2"))
    b.append(_txt(598, 96, "CRITERIO", 34, INK, "700"))
    b.append(_txt(598, 134, "Cuándo aplicar una regla y cuándo no.", 18, INK2, "400"))
    b.append(_txt(598, 160, "Si te cuesta enseñarlo, explícalo.", 18, INK2, "400"))
    b.append(_txt(598, 206, "condiciones · excepciones · límites", 17, INK3, "600"))

    b.append(_txt(560, 288, "Casi todos los prompts que fallan intentan comunicar "
                            "forma con instrucciones.", 20, INK, "700", "middle"))
    return _svg(310, "".join(b))
