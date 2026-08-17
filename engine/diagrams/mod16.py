# -*- coding: utf-8 -*-
"""Diagramas del módulo 16 — Observabilidad."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def fallo_silencioso():
    """El modo de fallo típico no lanza excepción."""
    b = [DEFS]

    b.append(_rect(10, 14, 528, 250, fill="#ffffff", stroke=HAIR, sw=1.6, r=12))
    b.append(_txt(38, 50, "SOFTWARE TRADICIONAL", 15, INK3, "700", spacing="2.2"))
    b.append(_rect(38, 74, 460, 60, fill=DANGER_SOFT, stroke=DANGER, sw=1.6, r=9))
    b.append(_txt(60, 112, "Excepción · rastro de pila · línea culpable", 18, INK,
                  "600"))
    for j, ln in enumerate(["El fallo se anuncia solo.",
                            "Se reproduce cuando quieras.",
                            "Hay un sitio concreto que arreglar."]):
        b.append(_txt(38, 176 + j * 30, ln, 17, INK2, "400"))

    b.append(_rect(582, 14, 528, 250, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(_txt(610, 50, "SISTEMA DE AI", 15, DANGER, "700", spacing="2.2"))
    b.append(_rect(610, 74, 460, 60, fill="#ffffff", stroke=OK, sw=1.6, r=9))
    b.append(_txt(632, 112, "200 OK · con una respuesta mala", 18, INK, "600"))
    for j, ln in enumerate(["No hay excepción, y desde fuera se ve sano.",
                            "No es determinista: falla una de cada diez.",
                            "Sin el prompt exacto no se reproduce."]):
        b.append(_txt(610, 176 + j * 30, ln, 17, INK2, "400"))

    b.append(_txt(560, 310, "Si no instrumentaste, no estás depurando: estás "
                            "adivinando.", 22, INK, "700", "middle"))
    return _svg(332, "".join(b))


def traza_arbol():
    """Una petición modelada como árbol de operaciones."""
    filas = [
        (0, "petición del usuario", "1 240 ms", "$0.014", ACC, True),
        (1, "recuperación", "180 ms", "", INK2, False),
        (2, "embedding de la consulta", "40 ms", "", INK3, False),
        (2, "búsqueda vectorial · k=10", "140 ms", "10 puntajes", INK3, False),
        (1, "llamada al modelo · planificación", "420 ms", "3 100 tokens", ACC, False),
        (1, "herramienta · consultar_inventario", "210 ms", "error", DANGER, False),
        (1, "herramienta · consultar_inventario (reintento)", "190 ms", "ok", OK, False),
        (1, "llamada al modelo · respuesta final", "240 ms", "4 800 tokens", ACC, False),
    ]
    b = [DEFS]
    for i, (nivel, nombre, ms, extra, color, raiz) in enumerate(filas):
        y = 18 + i * 42
        x = 10 + nivel * 42
        if raiz:
            b.append(_rect(x, y, 1100 - nivel * 42, 36, fill=ACC_SOFT, stroke=ACC,
                           sw=1.8, r=9))
        elif i % 2 == 1:
            b.append('<rect x="%d" y="%d" width="%d" height="36" rx="8" '
                     'fill="#fbfbfd"/>' % (x, y, 1100 - nivel * 42))
        # guía del árbol
        if nivel:
            b.append('<path d="M %d %d L %d %d L %d %d" fill="none" stroke="%s" '
                     'stroke-width="1.6" stroke-linecap="round"/>'
                     % (x - 20, y - 8, x - 20, y + 18, x - 6, y + 18, HAIR))
        b.append('<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (x + 16, y + 18, color))
        b.append(_txt(x + 32, y + 24, nombre, 18, INK if raiz else INK2,
                      "700" if raiz else "500", family=MONO if nivel else None))
        b.append(_txt(940, y + 24, ms, 16, INK3, "500", "end", family=MONO))
        b.append(_txt(1100, y + 24, extra, 16,
                      DANGER if extra == "error" else (OK if extra == "ok" else INK3),
                      "700" if extra in ("error", "ok") else "400", "end"))

    y = 18 + len(filas) * 42
    b.append(_txt(10, y + 34, "Con esto delante, «¿por qué respondió esto?» deja de "
                              "ser filosófica y se vuelve mecánica.", 19, INK, "700"))
    return _svg(y + 56, "".join(b))


def promedio_miente():
    """La latencia tiene cola larga: el promedio esconde el problema."""
    b = [DEFS]
    b.append(_txt(10, 30, "DISTRIBUCIÓN DE LATENCIAS DE 200 PETICIONES", 15, INK3,
                  "700", spacing="2.2"))
    ox, oy, w, h = 40, 250, 1060, 180
    alturas = [.06, .30, .72, 1.0, .86, .58, .36, .22, .14, .10, .08, .06,
               .05, .04, .04, .03, .03, .02, .02, .02]
    bw = w / len(alturas)
    for i, a in enumerate(alturas):
        x = ox + i * bw
        b.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" '
                 'fill="%s" opacity="%.2f"/>'
                 % (x + 2, oy - a * h, bw - 4, a * h, ACC, .45 + .5 * a))
    b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="2"/>' % (ox, oy, ox + w, oy, INK3))

    marcas = [(3.4, "promedio\n2 s", INK3), (10.5, "p95\n8 s", WARN),
              (16.5, "p99\n15 s", DANGER)]
    for pos, lab, color in marcas:
        x = ox + pos * bw
        b.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                 'stroke-width="2.5" stroke-dasharray="6 4"/>' % (x, 56, x, oy, color))
        for j, ln in enumerate(lab.split("\n")):
            b.append(_txt(x + 10, 78 + j * 22, ln, 16, color, "700"))

    b.append(_rect(10, 286, 1100, 84, fill=WARN_SOFT, stroke=WARN, sw=2, r=12))
    b.append(_txt(38, 322, "Un promedio de dos segundos esconde que uno de cada "
                           "veinte usuarios espera ocho.", 20, INK, "700"))
    b.append(_txt(38, 352, "Por eso siempre p50, p95 y p99. Y con streaming, el "
                           "tiempo al primer token aparte de la latencia total.",
                  18, INK2, "400"))
    return _svg(388, "".join(b))


def que_registrar():
    """Los campos por tipo de operación."""
    grupos = [
        ("LLAMADA AL MODELO", ACC,
         ["modelo y versión exacta", "parámetros de muestreo",
          "mensajes completos de entrada y salida",
          "tokens de entrada, salida, razonamiento y caché",
          "latencia y tiempo al primer token", "costo calculado",
          "motivo de finalización"]),
        ("RECUPERACIÓN", OK,
         ["la consulta tal cual", "la consulta reescrita, si la hubo",
          "los K documentos CON SUS PUNTAJES", "el umbral aplicado",
          "si hubo reordenamiento y cómo cambió el orden"]),
        ("HERRAMIENTA", INK2,
         ["nombre", "argumentos", "resultado", "duración",
          "error, si lo hubo", "número de reintento"]),
    ]
    b = [DEFS]
    for i, (t, color, campos) in enumerate(grupos):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 296, fill="#ffffff", stroke=color, sw=1.8, r=12))
        b.append(_rect(x, 14, 348, 46, fill=color, stroke="none", sw=0, r=12))
        b.append('<rect x="%d" y="46" width="348" height="14" fill="%s"/>' % (x, color))
        b.append(_txt(x + 22, 44, t, 15, "#ffffff", "700", spacing="2"))
        for j, c in enumerate(campos):
            destacado = c.isupper() or "PUNTAJES" in c
            b.append('<circle cx="%d" cy="%d" r="4" fill="%s"/>'
                     % (x + 28, 90 + j * 32 - 5, color))
            b.append(_txt(x + 42, 90 + j * 32, c, 16,
                          INK if destacado else INK2,
                          "700" if destacado else "400"))
    b.append(_txt(560, 348, "Guardar los puntajes de recuperación es el campo que más "
                            "veces salva una depuración.", 20, INK, "700", "middle"))
    return _svg(370, "".join(b))


def fallo_recuperacion_o_generacion():
    """Sin los puntajes no se puede distinguir el fallo."""
    b = [DEFS]
    b.append(_rect(400, 14, 320, 56, fill=DANGER, stroke="none", sw=0, r=10))
    b.append(_txt(560, 50, "la respuesta fue mala", 20, "#ffffff", "700", "middle"))
    b.append(_arrow(470, 76, 300, 104, DANGER, 2.5))
    b.append(_arrow(650, 76, 820, 104, DANGER, 2.5))

    b.append(_rect(10, 112, 530, 150, fill=WARN_SOFT, stroke=WARN, sw=2, r=12))
    b.append(_txt(38, 150, "EL TROZO CORRECTO NO SE RECUPERÓ", 14, WARN, "700",
                  spacing="1.8"))
    b.append(_txt(38, 190, "Se arregla en la indexación", 22, INK, "700"))
    b.append(_txt(38, 222, "troceado, modelo de embeddings,", 17, INK2, "400"))
    b.append(_txt(38, 246, "umbral, búsqueda híbrida", 17, INK2, "400"))

    b.append(_rect(580, 112, 530, 150, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(608, 150, "SÍ SE RECUPERÓ Y EL MODELO LO IGNORÓ", 14, ACC, "700",
                  spacing="1.8"))
    b.append(_txt(608, 190, "Se arregla en el prompt", 22, INK, "700"))
    b.append(_txt(608, 222, "posición del contexto, instrucciones,", 17, INK2, "400"))
    b.append(_txt(608, 246, "obligar a citar la fuente", 17, INK2, "400"))

    b.append(_rect(10, 288, 1100, 74, fill="#ffffff", stroke=INK, sw=2, r=12))
    b.append(_txt(560, 322, "Son dos problemas distintos con soluciones opuestas.",
                  21, INK, "700", "middle"))
    b.append(_txt(560, 350, "Sin los puntajes guardados no puedes saber en cuál estás.",
                  18, INK3, "400", "middle"))
    return _svg(382, "".join(b))
