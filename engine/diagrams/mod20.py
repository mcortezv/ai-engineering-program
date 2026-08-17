# -*- coding: utf-8 -*-
"""Diagramas del módulo 20 — Fine tuning en detalle."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def si_y_no():
    """Qué arregla y qué no."""
    si = [
        ("Formato muy específico y consistente", "cuando el esquema forzado no basta"),
        ("Tono y voz sostenidos", "a lo largo de textos largos"),
        ("Una tarea estrecha y repetitiva", "clasificar, extraer, transformar"),
        ("Reducir tokens de prompt", "mover instrucciones y ejemplos a los pesos"),
        ("Enseñar un protocolo propio", "cómo usar tus herramientas, tu flujo"),
    ]
    no = [
        ("Agregar conocimiento fresco", "eso es recuperación"),
        ("Corregir hechos puntuales", "no es un editor de hechos"),
        ("Reemplazar autorización", "ni validación, ni seguridad"),
        ("Arreglar un prompt mal escrito", "empieza por arreglar el prompt"),
    ]
    b = [DEFS]
    b.append(_rect(10, 14, 540, 306, fill=OK_SOFT, stroke=OK, sw=2, r=12))
    b.append(_txt(38, 50, "LO QUE SÍ ARREGLA", 15, OK, "700", spacing="2.2"))
    for i, (t, d) in enumerate(si):
        y = 82 + i * 48
        b.append('<circle cx="46" cy="%d" r="5" fill="%s"/>' % (y - 5, OK))
        b.append(_txt(62, y, t, 18, INK, "700"))
        b.append(_txt(62, y + 20, d, 15, INK3, "400"))

    b.append(_rect(582, 14, 528, 306, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(610, 50, "LO QUE NO ARREGLA", 15, DANGER, "700", spacing="2.2"))
    for i, (t, d) in enumerate(no):
        y = 82 + i * 48
        b.append('<circle cx="618" cy="%d" r="5" fill="%s"/>' % (y - 5, DANGER))
        b.append(_txt(634, y, t, 18, INK, "700"))
        b.append(_txt(634, y + 20, d, 15, INK3, "400"))

    b.append(_txt(610, 296, "El conocimiento va en el contexto.", 17, DANGER, "700"))
    b.append(_txt(38, 356, "Y el caso con el argumento económico más sólido es el "
                           "cuarto de la izquierda: reducir tokens de prompt.",
                  19, INK3, "400"))
    return _svg(376, "".join(b))


def efecto_perverso():
    """Entrenar con hechos que no conocía puede aumentar las invenciones."""
    b = [DEFS]
    pasos = [
        (10, "Le entrenas con hechos", "que apenas aparecían\nen sus datos", INK3),
        (300, "No aprende los hechos", "aprende el PATRÓN de\nresponder con seguridad",
         WARN),
        (590, "Llega una pregunta nueva", "parecida, sobre algo que\nno estaba en el "
                                          "conjunto", INK3),
        (880, "Responde con la misma\nseguridad", "e inventa", DANGER),
    ]
    for x, t, d, color in pasos:
        b.append(_rect(x, 30, 230, 118, fill="#ffffff", stroke=color, sw=1.8, r=11))
        for j, ln in enumerate(t.split("\n")):
            b.append(_txt(x + 20, 66 + j * 24, ln, 18, INK, "700"))
        base = 66 + len(t.split("\n")) * 24 + 8
        for j, ln in enumerate(d.split("\n")):
            b.append(_txt(x + 20, base + j * 22, ln, 15, color, "600"))
        if x < 880:
            b.append(_arrow(x + 236, 89, x + 294, 89, color, 2.2))

    b.append(_rect(10, 176, 1100, 90, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(38, 212, "Es exactamente el resultado opuesto al que se buscaba.",
                  21, INK, "700"))
    b.append(_txt(38, 242, "Entrenar con conocimiento que el modelo no dominaba puede "
                           "aumentar sus invenciones, no reducirlas.", 18, INK2,
                  "400"))

    b.append(_rect(10, 284, 1100, 62, fill="#ffffff", stroke=INK, sw=2, r=12))
    b.append(_txt(560, 322, "El conocimiento va en el contexto. El comportamiento va "
                            "en los pesos.", 21, INK, "700", "middle"))
    return _svg(366, "".join(b))


def lora_vs_completo():
    """Las dos formas de ajustar, comparadas."""
    filas = [
        ("Qué se modifica", "todos los pesos", "un conjunto pequeño de matrices "
                                               "añadidas"),
        ("Tamaño del artefacto", "un modelo entero, gigabytes", "un adaptador, "
                                                                "megabytes"),
        ("Cómputo necesario", "alto", "bajo; cabe en hardware modesto"),
        ("Riesgo de olvidar", "real", "mucho menor: el modelo base queda intacto"),
        ("Servir varias variantes", "un despliegue por variante",
         "varios adaptadores intercambiables sobre un base"),
        ("Cuándo elegirlo", "volumen grande y cambio real de capacidad",
         "prácticamente siempre como primer intento"),
    ]
    b = [DEFS]
    b.append(_rect(400, 14, 340, 44, fill=INK2, stroke="none", sw=0, r=9))
    b.append(_txt(570, 44, "AJUSTE COMPLETO", 15, "#ffffff", "700", "middle",
                  spacing="2"))
    b.append(_rect(756, 14, 354, 44, fill=ACC, stroke="none", sw=0, r=9))
    b.append(_txt(933, 44, "MÉTODOS EFICIENTES · LoRA", 15, "#ffffff", "700",
                  "middle", spacing="2"))
    for i, (campo, completo, lora) in enumerate(filas):
        y = 70 + i * 48
        if i % 2 == 0:
            b.append('<rect x="10" y="%d" width="1100" height="44" rx="7" '
                     'fill="#fbfbfd"/>' % y)
        b.append(_txt(28, y + 28, campo, 17, INK, "600"))
        b.append(_txt(400, y + 28, completo, 16, INK3, "400"))
        b.append(_txt(756, y + 28, lora, 16, ACC if i == 5 else INK2,
                      "700" if i == 5 else "400"))
    y = 70 + len(filas) * 48
    b.append(_txt(10, y + 34, "LoRA congela el modelo y entrena unas matrices que se "
                              "suman al resultado. No hace falta más matemática que "
                              "eso.", 19, INK3, "400"))
    return _svg(y + 56, "".join(b))


def destilacion():
    """Un modelo grande genera los datos de uno pequeño."""
    b = [DEFS]
    b.append(_rect(10, 40, 240, 110, fill=INK2, stroke="none", sw=0, r=12))
    b.append(_txt(130, 84, "MODELO GRANDE", 15, "#ffffff", "700", "middle",
                  spacing="1.8"))
    b.append(_txt(130, 114, "genera y etiqueta", 17, "#d8d8e0", "400", "middle"))
    b.append(_arrow(258, 95, 316, 95, INK3, 2.2))

    b.append(_rect(324, 40, 240, 110, fill=WARN_SOFT, stroke=WARN, sw=2, r=12))
    b.append(_txt(444, 78, "FILTRADO", 15, WARN, "700", "middle", spacing="1.8"))
    b.append(_txt(444, 106, "agresivo, por calidad", 17, INK, "600", "middle"))
    b.append(_txt(444, 132, "este paso decide el resultado", 14, INK3, "400",
                  "middle"))
    b.append(_arrow(572, 95, 630, 95, INK3, 2.2))

    b.append(_rect(638, 40, 240, 110, fill=ACC, stroke="none", sw=0, r=12))
    b.append(_txt(758, 84, "MODELO PEQUEÑO", 15, "#ffffff", "700", "middle",
                  spacing="1.8"))
    b.append(_txt(758, 114, "se entrena con eso", 17, "#d9ccff", "400", "middle"))
    b.append(_arrow(886, 95, 944, 95, INK3, 2.2))

    b.append(_rect(952, 40, 158, 110, fill=OK_SOFT, stroke=OK, sw=2, r=12))
    b.append(_txt(1031, 84, "barato", 20, OK, "700", "middle"))
    b.append(_txt(1031, 114, "y rápido", 20, OK, "700", "middle"))

    b.append(_rect(10, 184, 1100, 90, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(38, 220, "Revisa los términos de servicio del proveedor.", 21, INK,
                  "700"))
    b.append(_txt(38, 250, "Varios prohíben usar sus salidas para entrenar modelos "
                           "competidores. Es un riesgo legal real, no un "
                           "tecnicismo.", 18, INK2, "400"))
    return _svg(294, "".join(b))


def costo_completo():
    """Dónde está de verdad el gasto de un proyecto de ajuste."""
    partidas = [
        ("Datos y curación", 34, "el grueso del esfuerzo: semanas de trabajo humano",
         ACC),
        ("Medición", 14, "sin línea base no sabes si mejoró", ACC),
        ("Entrenamiento", 6, "lo más barato del proyecto", INK3),
        ("Hospedaje", 28, "GPU por hora la uses o no, o precio por token más alto",
         WARN),
        ("Mantenimiento", 18, "versionado, reversión, monitoreo", WARN),
    ]
    b = [DEFS]
    b.append(_txt(10, 30, "DÓNDE SE VA EL ESFUERZO DE UN PROYECTO DE AJUSTE", 15,
                  INK3, "700", spacing="2.2"))
    x = 10.0
    for nombre, pct, nota, color in partidas:
        w = 1100 * pct / 100.0
        b.append('<rect x="%.1f" y="50" width="%.1f" height="70" fill="%s" '
                 'opacity="%.2f"/>' % (x, w, color, .55 + pct / 100.0))
        b.append(_txt(x + w / 2.0, 92, "%d%%" % pct, 20, "#ffffff", "700", "middle"))
        x += w
    b.append(_rect(10, 50, 1100, 70, fill="none", stroke=INK, sw=2, r=0))

    for i, (nombre, pct, nota, color) in enumerate(partidas):
        y = 152 + i * 34
        b.append('<rect x="10" y="%d" width="20" height="20" rx="5" fill="%s" '
                 'opacity="%.2f"/>' % (y - 15, color, .55 + pct / 100.0))
        b.append(_txt(40, y, nombre, 18, INK, "600"))
        b.append(_txt(280, y, nota, 16, INK3, "400"))

    b.append(_rect(10, 336, 1100, 96, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(38, 372, "Y el que nadie presupuesta: el modelo base va a cambiar.",
                  21, INK, "700"))
    b.append(_txt(38, 402, "En seis o doce meses saldrá uno mejor o el tuyo se "
                           "deprecará. El adaptador no se transfiere: hay que volver a "
                           "entrenar,", 18, INK2, "400"))
    b.append(_txt(38, 424, "volver a evaluar y volver a desplegar.", 18, INK2, "400"))
    return _svg(452, "".join(b))


def checklist():
    """Cinco preguntas antes de empezar."""
    preguntas = [
        "¿Probaste un prompt bien diseñado con ejemplos, y lo mediste?",
        "¿El problema es de conocimiento? Si lo es, es recuperación.",
        "¿Tienes cientos de ejemplos de calidad y un conjunto de prueba apartado?",
        "¿Puedes medir objetivamente la mejora contra la línea base?",
        "¿El volumen justifica el hospedaje y reentrenar cuando cambie el base?",
    ]
    b = [DEFS]
    for i, q in enumerate(preguntas):
        y = 14 + i * 62
        b.append(_rect(10, y, 1100, 50, fill="#ffffff", stroke=HAIR, sw=1.6, r=11))
        b.append('<circle cx="44" cy="%d" r="15" fill="%s"/>' % (y + 25, ACC))
        b.append(_txt(44, y + 31, str(i + 1), 16, "#ffffff", "700", "middle"))
        b.append(_txt(74, y + 31, q, 19, INK, "600"))
        b.append(_rect(1000, y + 12, 92, 26, fill=OK_SOFT, stroke=OK, sw=1.4, r=6))
        b.append(_txt(1046, y + 30, "SÍ", 14, OK, "700", "middle", spacing="1.2"))

    y = 14 + len(preguntas) * 62
    b.append(_rect(10, y + 10, 1100, 66, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(560, y + 50, "Si alguna es no, el escalón anterior todavía tiene "
                               "algo que darte.", 21, INK, "700", "middle"))
    return _svg(y + 96, "".join(b))
