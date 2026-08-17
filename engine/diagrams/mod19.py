# -*- coding: utf-8 -*-
"""Diagramas del módulo 19 — Conceptos avanzados."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def control_contexto():
    """Tres técnicas para la misma tensión: hace falta contexto y el contexto cuesta."""
    tecnicas = [
        ("COMPRESIÓN", "Reescribe el contexto en menos tokens conservando lo esencial.",
         "Historiales largos y documentos que se reutilizan mucho.",
         "Una llamada extra, y pérdida de detalle que no siempre se nota.", ACC),
        ("ELIMINAR REDUNDANCIA", "Descarta fragmentos que dicen lo mismo antes de "
                                 "enviarlos.",
         "Corpus con mucha duplicación: documentación versionada, hilos de correo.",
         "Poco. Es de las optimizaciones más limpias que existen.", OK),
        ("AGRUPAMIENTO", "Agrupa por tema y toma representantes en vez de los K más "
                         "parecidos.",
         "Cuando la recuperación devuelve diez variantes de la misma idea.",
         "Complejidad: hay que ajustar el número de grupos.", INK2),
    ]
    b = [DEFS]
    for i, (t, que, cuando, cuesta, color) in enumerate(tecnicas):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 300, fill="#ffffff", stroke=color, sw=1.8, r=12))
        b.append(_rect(x, 14, 348, 44, fill=color, stroke="none", sw=0, r=12))
        b.append('<rect x="%d" y="44" width="348" height="14" fill="%s"/>' % (x, color))
        b.append(_txt(x + 22, 43, t, 15, "#ffffff", "700", spacing="1.8"))

        y = 84
        for etiqueta, texto, limite, size, col in (
                ("QUÉ HACE", que, 34, 16, INK),
                ("CUÁNDO", cuando, 36, 15, INK2),
                ("QUÉ CUESTA", cuesta, 36, 15, INK3)):
            b.append(_txt(x + 22, y, etiqueta, 12, color, "700", spacing="1.6"))
            palabras, linea, lineas = texto.split(), "", []
            for w in palabras:
                if len(linea + " " + w) > limite:
                    lineas.append(linea)
                    linea = w
                else:
                    linea = (linea + " " + w).strip()
            lineas.append(linea)
            for j, ln in enumerate(lineas):
                b.append(_txt(x + 22, y + 24 + j * 22, ln, size, col, "400"))
            y += 34 + len(lineas) * 22

    b.append(_txt(10, 350, "Las tres responden a la misma tensión: hace falta "
                           "contexto, y el contexto cuesta dinero, latencia y "
                           "precisión.", 19, INK3, "400"))
    return _svg(370, "".join(b))


def control_estilo():
    """Cuatro formas de fijar la voz, de la más barata a la más costosa."""
    opciones = [
        ("Describirlo con palabras", "«tono profesional pero cercano»",
         "Barato y reversible, pero las descripciones de estilo son imprecisas.",
         INK3, "#ffffff"),
        ("Mostrar ejemplos", "dos o tres fragmentos escritos con la voz deseada",
         "Mejor que describirla: el estilo se enseña con muestras.", ACC,
         ACC_SOFT),
        ("Recuperar la guía de estilo", "el documento de voz de marca, cuando aplica",
         "Para organizaciones con una guía real y extensa que no cabe en el prompt.",
         OK, OK_SOFT),
        ("Ajustar los pesos", "entrenar con ejemplos escritos en esa voz",
         "Solo cuando lo anterior se agotó y el volumen lo justifica.", WARN,
         WARN_SOFT),
    ]
    b = [DEFS]
    for i, (t, como, nota, color, fill) in enumerate(opciones):
        y = 14 + i * 84
        b.append(_rect(10, y, 1100, 72, fill=fill, stroke=color, sw=1.8, r=11))
        b.append('<circle cx="46" cy="%d" r="16" fill="%s"/>' % (y + 36, color))
        b.append(_txt(46, y + 42, str(i + 1), 17, "#ffffff", "700", "middle"))
        b.append(_txt(76, y + 30, t, 20, INK, "700"))
        b.append(_txt(76, y + 56, como, 16, color, "600"))
        b.append(_txt(560, y + 44, nota, 16, INK3, "400"))

    b.append('<path d="M 1096 24 L 1096 320" stroke="%s" stroke-width="2" '
             'stroke-dasharray="6 5" stroke-linecap="round"/>' % HAIR)
    b.append(_txt(10, 372, "Para estilo, los ejemplos ganan a las descripciones casi "
                           "siempre.", 20, INK, "700"))
    b.append(_txt(10, 398, "El estilo es forma, y la forma se enseña mostrándola.",
                  18, INK3, "400"))
    return _svg(418, "".join(b))


def pipeline_conversacional():
    """Una conversación con objetivo modelada como grafo de nodos."""
    b = [DEFS]
    nodos = [
        (40, 120, "saludo", "pregunta", INK3),
        (240, 120, "calificar", "pregunta", ACC),
        (440, 60, "presupuesto", "carga contexto", ACC),
        (440, 190, "descartar", "acción", INK3),
        (650, 60, "agendar", "acción", ACC),
        (860, 120, "confirmar", "artefacto", OK),
    ]
    aristas = [(0, 1), (1, 2), (1, 3), (2, 4), (4, 5)]
    for a, z in aristas:
        x1, y1 = nodos[a][0] + 150, nodos[a][1] + 26
        x2, y2 = nodos[z][0], nodos[z][1] + 26
        b.append('<path d="M %d %d C %d %d %d %d %d %d" fill="none" stroke="%s" '
                 'stroke-width="2.2" stroke-linecap="round" '
                 'marker-end="url(#ahp)"/>'
                 % (x1, y1, x1 + 26, y1, x2 - 26, y2, x2 - 6, y2, ACC))
    for x, y, nombre, tipo, color in nodos:
        b.append(_rect(x, y, 150, 52, fill="#ffffff", stroke=color, sw=1.8, r=11))
        b.append(_txt(x + 75, y + 26, nombre, 17, INK, "700", "middle"))
        b.append(_txt(x + 75, y + 44, tipo, 13, color, "600", "middle"))

    b.append(_rect(10, 268, 1100, 78, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, 304, "En cada nodo pasa una de cinco cosas.", 21, INK, "700"))
    b.append(_txt(38, 332, "Se pregunta, se responde, se carga contexto, se ejecuta "
                           "una acción o se delega.", 18, INK2, "400"))

    b.append(_txt(10, 384, "Modelarlo así da predecibilidad, trazabilidad y control "
                           "de costo a la vez: el conjunto de estados es conocido, "
                           "cada nodo", 17, INK3, "400"))
    b.append(_txt(10, 406, "es una operación registrable, y cada uno carga solo su "
                           "contexto.", 17, INK3, "400"))
    return _svg(426, "".join(b))


def tres_estrategias_volumen():
    """Procesar cien elementos: tres perfiles muy distintos."""
    est = [
        ("UNA SOLA LLAMADA", "todo en el mismo prompt",
         ["simple de escribir", "contexto enorme", "la calidad se degrada",
          "si falla, se pierde todo"], DANGER, DANGER_SOFT),
        ("EN PARALELO", "una llamada por elemento",
         ["contexto limpio en cada una", "tolera fallos parciales",
          "se puede mostrar conforme llega", "latencia baja percibida"], ACC,
         ACC_SOFT),
        ("POR LOTES", "asíncrono, ventana de horas",
         ["del orden de la mitad de costo", "misma calidad que en paralelo",
          "no sirve si alguien espera", "requiere avisar al terminar"], OK, OK_SOFT),
    ]
    b = [DEFS]
    for i, (t, como, puntos, color, fill) in enumerate(est):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 244, fill=fill, stroke=color, sw=1.8, r=12))
        b.append(_txt(x + 24, 50, t, 15, color, "700", spacing="2"))
        b.append(_txt(x + 24, 78, como, 17, INK, "600"))
        b.append('<line x1="%d" y1="96" x2="%d" y2="96" stroke="%s" '
                 'stroke-width="1.4"/>' % (x + 24, x + 324, color))
        for j, p in enumerate(puntos):
            b.append('<circle cx="%d" cy="%d" r="4" fill="%s"/>'
                     % (x + 30, 124 + j * 30 - 5, color))
            b.append(_txt(x + 44, 124 + j * 30, p, 16, INK2, "400"))

    b.append(_rect(10, 280, 1100, 66, fill="#ffffff", stroke=INK, sw=2, r=12))
    b.append(_txt(560, 320, "El criterio: si hay una persona esperando, en paralelo. "
                            "Si no la hay, por lotes.", 21, INK, "700", "middle"))
    return _svg(366, "".join(b))


def latencia_factores():
    """De qué depende la latencia, y en qué se puede intervenir."""
    factores = [
        ("Peticiones encadenadas", "SÍ", "El factor dominante y el más ignorado. "
                                         "Reducir viajes de ida y vuelta.", ACC),
        ("Tamaño del contexto", "SÍ", "Todo se procesa antes de emitir el primer "
                                      "token.", ACC),
        ("Tokens de salida y razonamiento", "SÍ", "Se generan de uno en uno. Limitar "
                                                  "longitud y esfuerzo.", ACC),
        ("Elección de modelo", "SÍ", "Los modelos pequeños son notablemente más "
                                     "rápidos.", ACC),
        ("Ubicación geográfica", "EN PARTE", "Elegir la región del proveedor más "
                                             "cercana a los usuarios.", WARN),
        ("Carga del proveedor", "NO", "Reintentos, alternativas y degradación "
                                      "elegante.", INK3),
    ]
    b = [DEFS]
    b.append(_txt(10, 30, "FACTOR", 13, INK3, "700", spacing="1.8"))
    b.append(_txt(400, 30, "¿LO CONTROLAS?", 13, INK3, "700", spacing="1.8"))
    b.append(_txt(560, 30, "QUÉ SE PUEDE HACER", 13, INK3, "700", spacing="1.8"))
    b.append('<line x1="10" y1="42" x2="1110" y2="42" stroke="%s" '
             'stroke-width="1.6"/>' % INK3)
    for i, (t, control, que, color) in enumerate(factores):
        y = 54 + i * 44
        if i % 2 == 1:
            b.append('<rect x="10" y="%d" width="1100" height="40" rx="7" '
                     'fill="#fbfbfd"/>' % y)
        b.append(_txt(28, y + 26, t, 18, INK, "600"))
        b.append(_rect(400, y + 8, 108, 26, fill=color, stroke="none", sw=0, r=7))
        b.append(_txt(454, y + 26, control, 13, "#ffffff", "700", "middle",
                      spacing="1.2"))
        b.append(_txt(560, y + 26, que, 16, INK3, "400"))

    y = 54 + len(factores) * 44
    b.append(_rect(10, y + 12, 1100, 96, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(38, y + 48, "Una red de distribución de contenido no acelera la "
                              "inferencia.", 20, INK, "700"))
    b.append(_txt(38, y + 76, "Cada respuesta se calcula en el momento y es distinta, "
                              "así que no se puede cachear en el borde. Sí ayuda con "
                              "todo lo que rodea", 17, INK2, "400"))
    b.append(_txt(38, y + 98, "a la llamada: la aplicación y sus recursos estáticos.",
                  17, INK2, "400"))
    return _svg(y + 132, "".join(b))
