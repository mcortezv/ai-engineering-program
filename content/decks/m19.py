# -*- coding: utf-8 -*-
"""Deck: Módulo 19 — Conceptos avanzados."""

from engine.diagrams import mod19 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 19 · Conceptos avanzados",
    "footer": "Programa de AI · Módulo 19",
    "outfile": "Modulo 19 - Conceptos avanzados.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 19  ·  2 HORAS",
        "title": "Conceptos avanzados",
        "tagline": "Las técnicas que aparecen cuando el sistema ya funciona y hay que "
                   "empujarlo un poco más lejos.",
        "meta": [
            "<b>Antes de esta sesión:</b> el sistema operado, medido y protegido",
            "<b>Al terminar:</b> sabes cuándo cada técnica está justificada",
        ],
    },

    {
        "kind": "statement",
        "text": "Todo lo de hoy solo tiene sentido <em>sobre un sistema que ya "
                "funciona</em>.",
        "after": "Aplicar compresión de contexto a un prototipo es optimizar algo que "
                 "todavía no sabes si vas a conservar.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Control avanzado del contexto</b> — compresión, redundancia y
            agrupamiento.</li>
          <li><b>Control del estilo</b> — cuatro formas de fijar la voz de un
            sistema.</li>
          <li><b>Conversaciones como grafo</b> — cuando la charla tiene un objetivo y
            una estructura.</li>
          <li><b>Volumen</b> — tres formas de procesar cien elementos.</li>
          <li><b>Latencia</b> — de qué depende y en qué puedes intervenir.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Control del contexto",
        "note": "Tres técnicas para la tensión que atraviesa todo el programa: hace "
                "falta contexto y el contexto cuesta.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Tres técnicas",
        "title": "Qué hace cada una, cuándo y qué cuesta",
        "html": dg.control_contexto(),
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "El agrupamiento merece un comentario",
        "title": "Los K más parecidos pueden ser el mismo párrafo cinco veces",
        "html": """
        <ul class="pts">
          <li><b>Es un fallo real de la recuperación y no es obvio.</b>
            <span class="n">Si el mismo texto aparece repetido en cinco documentos,
            los cinco mejores resultados son el mismo contenido y has gastado cinco
            huecos en una sola idea.</span></li>
          <li><b>Y encima deja fuera lo que sí faltaba.</b>
            <span class="n">La perspectiva distinta que habría completado la
            respuesta se queda en el puesto seis.</span></li>
          <li><b>Recuperar diversidad en lugar de solo parecido lo arregla.</b>
            <span class="n">Se agrupan los candidatos por tema y se toma un
            representante de cada grupo. Mejora sobre todo las preguntas
            amplias.</span></li>
        </ul>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "Control del estilo",
        "note": "Cuatro formas de conseguir que un sistema suene como tu "
                "organización.",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "De lo más barato a lo más costoso",
        "title": "Cuatro formas de fijar la voz",
        "html": dg.control_estilo(),
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Una precisión de vocabulario",
        "title": "Dónde sí existe un componente que codifica el estilo",
        "html": """
        <ul class="pts">
          <li><b>En síntesis de voz, generación de imágenes y transferencia de
            estilo, sí.</b>
            <span class="n">Existe un componente que toma una referencia y produce un
            vector que condiciona la generación. Es real y funciona
            exactamente así.</span></li>
          <li><b>En modelos de lenguaje por API, no hay nada equivalente.</b>
            <span class="n">No hay un parámetro donde metas «esta es nuestra voz» y
            el modelo la adopte. Lo que hay son las cuatro formas de la lámina
            anterior.</span></li>
          <li><b>Conviene saberlo para no buscar algo que no existe.</b>
            <span class="n">Y para no aceptar una propuesta que prometa
            eso.</span></li>
        </ul>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Conversaciones con objetivo",
        "note": "Un tipo de sistema que se construye mucho y se documenta poco.",
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "La observación de partida",
        "title": "Una conversación con objetivo no es libre: tiene estructura",
        "html": dg.pipeline_conversacional(),
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Lo que compra modelarlo así",
        "title": "Tres problemas resueltos con una sola decisión",
        "html": """
        <div class="grid c3">
          <div class="card"><div class="k">PREDECIBILIDAD</div>
            <div class="t">El conjunto de estados es conocido</div>
            <div class="d">Puedes enumerar por dónde puede pasar la conversación y
            probarlo, en lugar de esperar a ver qué sale.</div></div>
          <div class="card"><div class="k">TRAZABILIDAD</div>
            <div class="t">Cada nodo es una operación registrable</div>
            <div class="d">La traza sale de la propia estructura: no hay que
            inventarse dónde poner los puntos de medición.</div></div>
          <div class="card"><div class="k">COSTO</div>
            <div class="t">Cada nodo carga solo su contexto</div>
            <div class="d">No viaja la conversación entera por todas las etapas:
            cada una arranca con lo mínimo.</div></div>
        </div>
        <div class="box warn" style="margin-top:7mm">
          <p class="lab">Y la contrapartida</p>
          <p>Un grafo rígido maneja mal lo inesperado. El diseño realista combina
          nodos deterministas para el camino principal con capacidad de salirse del
          guion cuando el usuario hace algo que no estaba previsto.</p>
        </div>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "Volumen y latencia",
        "note": "Procesar mucho, y responder rápido.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Procesar cien elementos",
        "title": "Tres estrategias con perfiles muy distintos",
        "html": dg.tres_estrategias_volumen(),
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Un caso que ya conocen en la casa",
        "title": "El análisis masivo de candidatos",
        "html": """
        <ul class="pts">
          <li><b>Analizar cientos de perfiles no es una operación interactiva.</b>
            <span class="n">Nadie está mirando la pantalla esperando el
            resultado.</span></li>
          <li><b>Y sin embargo se suele resolver como si lo fuera.</b>
            <span class="n">Es el patrón por inercia: se escribió cuando eran diez
            perfiles y nunca se revisó al llegar a quinientos.</span></li>
          <li><b>Es exactamente el caso del procesamiento por lotes.</b>
            <span class="n">Del orden de la mitad de costo, misma calidad, y la
            ventana de horas no molesta a nadie porque el informe se consulta al día
            siguiente.</span></li>
        </ul>
        <div class="box" style="margin-top:7mm">
          <p>Vale la pena revisar cualquier proceso masivo que exista hoy con esta
          pregunta: <b>¿hay alguien esperando?</b> Es de los ahorros más fáciles que
          se pueden conseguir.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "Qué se puede hacer con la latencia",
        "title": "Separar lo que controlas de lo que no",
        "html": dg.latencia_factores(),
    },

    {
        "kind": "statement",
        "text": "En una arquitectura compleja la latencia es la <em>suma de muchas "
                "partes</em>, y casi siempre domina una: el número de peticiones "
                "encadenadas.",
        "after": "Es también la que más se puede reducir, y la última que la gente "
                 "mira.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Sobre algo que funciona</div>
            <div class="d">Estas técnicas no arreglan un prototipo.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Eliminar redundancia</div>
            <div class="d">La optimización más limpia de las tres.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Diversidad, no solo parecido</div>
            <div class="d">Los K mejores pueden ser el mismo párrafo.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Estilo con ejemplos</div>
            <div class="d">Los adjetivos no lo comunican.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Grafo de nodos</div>
            <div class="d">Predecible, medible y más barato a la vez.</div></div>
          <div class="card"><div class="k">06</div><div class="t">¿Hay alguien esperando?</div>
            <div class="d">Decide entre paralelo y lotes.</div></div>
          <div class="card"><div class="k">07</div><div class="t">La CDN no acelera inferencia</div>
            <div class="d">Cada respuesta se calcula en el momento.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">Menos peticiones encadenadas</div>
            <div class="d">El factor dominante de la latencia.</div></div>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 19 · Conceptos avanzados.",
        "rows": [
            ("2", "Enmarca la sesión para que nadie salga aplicando compresión de "
                  "contexto a un prototipo de dos semanas."),
            ("7", "El fallo del párrafo repetido cinco veces sorprende. Si alguien "
                  "tiene un sistema de recuperación en marcha, pídele que revise sus "
                  "cinco mejores resultados de una consulta amplia."),
            ("10", "<b>Precisión de vocabulario, no corrección.</b> Explica dónde sí "
                   "existe ese componente para que sepan situar el término cuando lo "
                   "encuentren."),
            ("12", "Este tipo de sistema se construye mucho y se documenta poco. Si "
                   "tienen alguno, modélalo en el pizarrón con ellos."),
            ("15", "El ejemplo del análisis masivo es interno y cercano. Deja que "
                   "alguien haga la cuenta del ahorro en voz alta."),
            ("17", "Ordena los factores por controlabilidad, no por importancia. Es "
                   "lo que convierte la explicación en algo accionable."),
        ],
    },
]
