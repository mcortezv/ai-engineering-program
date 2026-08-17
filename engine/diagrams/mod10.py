# -*- coding: utf-8 -*-
"""Diagramas del módulo 10 — Protocolos de comunicación."""

from engine.diagrams.base import (
    ACC, ACC_SOFT, DANGER, DANGER_SOFT, DEFS, HAIR, INK, INK2, INK3, MONO,
    OK, OK_SOFT, PAPER, _arrow, _rect, _svg, _txt,
)

WARN = "#8a5a06"
WARN_SOFT = "#fbf3e3"


def api_rest_http():
    """Tres palabras que se usan como sinónimos y no lo son."""
    capas = [
        ("API", "El contrato", "Qué operaciones existen, qué reciben y qué "
                               "devuelven.", ACC),
        ("REST", "Un estilo para diseñar ese contrato",
         "Recursos y verbos, sobre HTTP. Hay otros estilos.", INK2),
        ("HTTP", "El transporte", "Cómo viajan los bytes de una máquina a otra.",
         INK3),
    ]
    b = [DEFS]
    for i, (t, rol, desc, color) in enumerate(capas):
        y = 14 + i * 92
        b.append(_rect(10 + i * 40, y, 1100 - i * 80, 78, fill="#ffffff",
                       stroke=color, sw=2, r=11))
        b.append(_rect(34 + i * 40, y + 18, 118, 42, fill=color, stroke="none",
                       sw=0, r=8))
        b.append(_txt(93 + i * 40, y + 46, t, 19, "#ffffff", "700", "middle",
                      family=MONO))
        b.append(_txt(174 + i * 40, y + 36, rol, 20, INK, "700"))
        b.append(_txt(174 + i * 40, y + 62, desc, 17, INK3, "400"))

    b.append(_txt(10, 320, "Una API puede no ser REST. REST siempre necesita un "
                           "transporte debajo. Cuando alguien dice «conéctate a la "
                           "API», puede estar hablando de cualquiera de las tres.",
                  19, INK3, "400"))
    return _svg(342, "".join(b))


def pull_vs_push():
    """El cliente pregunta, o el servidor avisa."""
    b = [DEFS]

    def caja(x, y, w, h, texto, fill, stroke, fg=INK):
        return (_rect(x, y, w, h, fill=fill, stroke=stroke, sw=1.8, r=10)
                + _txt(x + w / 2.0, y + h / 2.0 + 7, texto, 18, fg, "700", "middle"))

    # pull
    b.append(_rect(10, 14, 540, 264, fill="#ffffff", stroke=INK2, sw=2, r=12))
    b.append(_txt(38, 50, "REST · MODELO PULL", 15, INK2, "700", spacing="2.2"))
    b.append(caja(38, 74, 180, 56, "tu código", "#f1f1f5", HAIR))
    b.append(caja(342, 74, 180, 56, "el servicio", "#f1f1f5", HAIR))
    for j in range(3):
        yy = 156 + j * 34
        b.append(_arrow(48, yy, 330, yy, INK3, 1.8))
        b.append(_txt(190, yy - 8, "¿ya terminó?" if j < 2 else "¿ya terminó?",
                      15, INK3, "400", "middle"))
        b.append(_txt(536, yy + 5, "no" if j < 2 else "sí", 15,
                      INK3 if j < 2 else OK, "700", "end"))
    b.append(_txt(38, 266, "Preguntas seguido y gastas. Preguntas poco y te enteras "
                           "tarde.", 16, DANGER, "600"))

    # push
    b.append(_rect(570, 14, 540, 264, fill=ACC_SOFT, stroke=ACC, sw=2, r=12))
    b.append(_txt(598, 50, "WEBHOOK · MODELO PUSH", 15, ACC, "700", spacing="2.2"))
    b.append(caja(598, 74, 180, 56, "tu servidor", "#ffffff", ACC))
    b.append(caja(902, 74, 180, 56, "el servicio", "#ffffff", ACC))
    b.append(_arrow(608, 158, 890, 158, INK3, 1.8))
    b.append(_txt(750, 150, "aquí tienes mi dirección", 15, INK3, "400", "middle"))
    b.append('<path d="M 890 214 L 620 214" stroke="%s" stroke-width="2.5" '
             'marker-end="url(#ahp)"/>' % ACC)
    b.append(_txt(750, 206, "«ya terminó»", 16, ACC, "700", "middle"))
    b.append(_txt(598, 266, "Una sola llamada, cuando de verdad hay algo que decir.",
                  16, OK, "600"))

    b.append(_txt(560, 320, "Al recibir un webhook, tu servidor se convirtió en el "
                            "servidor de alguien más.", 20, INK, "700", "middle"))
    return _svg(340, "".join(b))


def obligaciones_webhook():
    """Lo que hay que hacer sí o sí al recibir eventos."""
    obl = [
        ("Verificar la firma", "Sin eso, cualquiera puede fabricar eventos falsos "
                               "contra un endpoint público.", DANGER),
        ("Ser idempotente", "La entrega es al menos una vez: el mismo evento va a "
                            "llegar dos veces.", DANGER),
        ("No asumir orden", "Puede llegar antes «completado» que «iniciado».", WARN),
        ("Responder rápido, procesar después", "Encola y devuelve. Si procesas en el "
                                               "manejador, el emisor reintenta todo.", WARN),
    ]
    b = [DEFS]
    for i, (t, d, color) in enumerate(obl):
        y = 14 + i * 82
        b.append(_rect(10, y, 1100, 70, fill="#ffffff", stroke=HAIR, sw=1.5, r=11))
        b.append('<rect x="10" y="%d" width="5" height="70" rx="2.5" fill="%s"/>'
                 % (y, color))
        b.append('<circle cx="52" cy="%d" r="15" fill="%s"/>' % (y + 35, color))
        b.append(_txt(52, y + 41, str(i + 1), 16, "#ffffff", "700", "middle"))
        b.append(_txt(84, y + 32, t, 20, INK, "700"))
        b.append(_txt(84, y + 57, d, 17, INK3, "400"))
    return _svg(14 + len(obl) * 82 + 16, "".join(b))


def problema_nxm():
    """Por qué existe un estándar."""
    b = [DEFS]

    def malla(x0, titulo, conectar_todo, color):
        out = [_txt(x0 + 240, 42, titulo, 17, color, "700", "middle", spacing="1.6")]
        clientes = [(x0 + 60, 90 + i * 62) for i in range(3)]
        sistemas = [(x0 + 420, 78 + i * 46) for i in range(4)]
        if conectar_todo:
            for cx, cy in clientes:
                for sx, sy in sistemas:
                    out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                               'stroke-width="1.4" opacity=".4"/>'
                               % (cx + 46, cy, sx - 40, sy, DANGER))
        else:
            hub = (x0 + 240, 152)
            for cx, cy in clientes:
                out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                           'stroke-width="1.8"/>'
                           % (cx + 46, cy, hub[0] - 42, hub[1], ACC))
            for sx, sy in sistemas:
                out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                           'stroke-width="1.8"/>'
                           % (hub[0] + 42, hub[1], sx - 40, sy, ACC))
            out.append(_rect(hub[0] - 42, hub[1] - 24, 84, 48, fill=ACC,
                             stroke="none", sw=0, r=9))
            out.append(_txt(hub[0], hub[1] + 6, "MCP", 17, "#ffffff", "700",
                            "middle", family=MONO))
        for cx, cy in clientes:
            out.append('<circle cx="%d" cy="%d" r="22" fill="#ffffff" stroke="%s" '
                       'stroke-width="1.8"/>' % (cx, cy, INK3))
            out.append(_txt(cx, cy + 6, "AI", 14, INK2, "700", "middle"))
        for sx, sy in sistemas:
            out.append(_rect(sx - 20, sy - 15, 40, 30, fill="#f1f1f5", stroke=HAIR,
                             sw=1.5, r=6))
        return "".join(out)

    b.append(_rect(10, 14, 528, 300, fill=DANGER_SOFT, stroke=DANGER, sw=2, r=12))
    b.append(malla(10, "SIN ESTÁNDAR · 3 × 4 = 12 INTEGRACIONES", True, DANGER))
    b.append(_rect(582, 14, 528, 300, fill=OK_SOFT, stroke=OK, sw=2, r=12))
    b.append(malla(582, "CON ESTÁNDAR · 3 + 4 = 7 CONEXIONES", False, OK))
    b.append(_txt(560, 352, "Con tres clientes de AI y quince sistemas internos, la "
                            "diferencia es 45 integraciones a mano contra 18.",
                  19, INK3, "400", "middle"))
    return _svg(372, "".join(b))


def primitivas_mcp():
    """Las tres primitivas, explicadas por quién las controla."""
    prim = [
        ("TOOLS", "el modelo", "Acciones que el modelo decide invocar.",
         "Tienen efectos.", ACC),
        ("RESOURCES", "la aplicación", "Datos de solo lectura que el host adjunta.",
         "No tienen efectos.", INK2),
        ("PROMPTS", "el usuario", "Plantillas que la persona invoca a propósito.",
         "Se disparan a mano.", OK),
    ]
    b = [DEFS]
    for i, (t, quien, que, nota, color) in enumerate(prim):
        x = 10 + i * 372
        b.append(_rect(x, 14, 348, 224, fill="#ffffff", stroke=color, sw=2, r=12))
        b.append(_rect(x, 14, 348, 52, fill=color, stroke="none", sw=0, r=12))
        b.append('<rect x="%d" y="50" width="348" height="16" fill="%s"/>' % (x, color))
        b.append(_txt(x + 24, 48, t, 19, "#ffffff", "700", family=MONO))
        b.append(_txt(x + 24, 104, "LAS CONTROLA", 13, INK3, "700", spacing="1.6"))
        b.append(_txt(x + 24, 138, quien, 26, color, "700"))
        b.append('<line x1="%d" y1="158" x2="%d" y2="158" stroke="%s" '
                 'stroke-width="1.4"/>' % (x + 24, x + 324, HAIR))
        b.append(_txt(x + 24, 186, que, 17, INK2, "400"))
        b.append(_txt(x + 24, 214, nota, 17, color, "600"))
    b.append(_txt(560, 278, "Sin esta distinción, la tentación es meterlo todo como "
                            "herramientas. Con ella, hay criterio.",
                  19, INK3, "400", "middle"))
    return _svg(298, "".join(b))


def cuatro_protocolos():
    """Los cuatro lado a lado."""
    filas = [
        ("REST", "el cliente", "petición y respuesta", "tu código",
         "operaciones bajo demanda", INK2),
        ("Webhook", "el servidor remoto", "asíncrono", "tu código",
         "eventos y trabajos largos", INK2),
        ("SSE / WebSocket", "el cliente abre", "flujo continuo", "tu código o la interfaz",
         "streaming de tokens, voz", INK2),
        ("MCP", "el host o el agente", "petición y respuesta", "EL MODELO",
         "dar capacidades descubribles", ACC),
    ]
    b = [DEFS]
    cols = [("PROTOCOLO", 30), ("QUIÉN INICIA", 250), ("SINCRONÍA", 470),
            ("QUIÉN LO CONSUME", 680), ("CUÁNDO USARLO", 890)]
    for t, x in cols:
        b.append(_txt(x, 32, t, 13, INK3, "700", spacing="1.8"))
    b.append('<line x1="10" y1="44" x2="1110" y2="44" stroke="%s" '
             'stroke-width="1.6"/>' % INK3)
    for i, (p, inicia, sinc, consume, cuando, color) in enumerate(filas):
        y = 56 + i * 58
        destacado = color == ACC
        if destacado:
            b.append('<rect x="10" y="%d" width="1100" height="54" rx="8" '
                     'fill="%s"/>' % (y, ACC_SOFT))
        elif i % 2 == 1:
            b.append('<rect x="10" y="%d" width="1100" height="54" rx="8" '
                     'fill="#fbfbfd"/>' % y)
        b.append(_txt(30, y + 34, p, 19, color, "700"))
        b.append(_txt(250, y + 34, inicia, 17, INK2, "400"))
        b.append(_txt(470, y + 34, sinc, 17, INK2, "400"))
        b.append(_txt(680, y + 34, consume, 17, ACC if destacado else INK2,
                      "700" if destacado else "400"))
        b.append(_txt(890, y + 34, cuando, 17, INK2, "400"))

    y = 56 + len(filas) * 58
    b.append(_txt(10, y + 40, "MCP es el único de los cuatro cuyo consumidor es el "
                              "modelo y no tu código. Esa es toda la diferencia.",
                  20, INK, "700"))
    return _svg(y + 62, "".join(b))
