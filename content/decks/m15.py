# -*- coding: utf-8 -*-
"""Deck: Módulo 15 — Orquestación."""

from engine.diagrams import mod15 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 15 · Orquestación",
    "footer": "Programa de AI · Módulo 15",
    "outfile": "Modulo 15 - Orquestacion.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 15  ·  2 HORAS",
        "title": "Orquestación",
        "tagline": "Dividir para que cada pieza reciba solo el contexto que necesita.",
        "meta": [
            "<b>Antes de esta sesión:</b> agentes y lo que cuesta el contexto",
            "<b>Al terminar:</b> decides qué dividir y qué dejar junto",
        ],
    },

    {
        "kind": "statement",
        "text": "Delegar todo a un solo agente sale <em>menos preciso y más caro</em> "
                "a la vez.",
        "after": "Y esa simultaneidad es lo que hace fuerte el argumento: no hay un "
                 "intercambio que negociar, se pierde en las dos dimensiones.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Por qué un solo agente con todo sale mal</b> — en precisión y en
            dinero.</li>
          <li><b>Dividir por responsabilidad</b> — y el criterio de la frase sin
            «y».</li>
          <li><b>Cuándo NO dividir</b> — cuatro casos donde partir empeora.</li>
          <li><b>Cargar bajo demanda</b> — el patrón que ya viste con otros
            nombres.</li>
          <li><b>Paralelo y segundo plano</b> — dos ganancias distintas.</li>
          <li><b>Un flujo completo</b> — y dónde se rompe.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Uno con todo, o varios con lo justo",
        "note": "El mismo trabajo, repartido de dos formas.",
    },

    {
        "kind": "content", "covers": [1, 2],
        "eyebrow": "La comparación",
        "title": "Qué cambia al repartir",
        "html": dg.uno_vs_varios(),
    },

    {
        "kind": "content", "covers": [1, 2],
        "eyebrow": "Por qué sale peor lo de la izquierda",
        "title": "Dos causas, y las dos ya las conoces",
        "html": """
        <ul class="pts">
          <li><b>Menos preciso, porque la instrucción relevante compite.</b>
            <span class="n">Con cincuenta herramientas y veinte documentos delante,
            lo que sí importaba en esa tarea concreta queda diluido entre el
            resto.</span></li>
          <li><b>Más caro, porque todo ese contexto se paga en cada iteración.</b>
            <span class="n">Y en un bucle con herramientas hay muchas iteraciones,
            cada una arrastrando el contexto completo.</span></li>
          <li><b>Y hay una tercera, menos obvia: no se puede probar.</b>
            <span class="n">Un agente que hace cuatro cosas tiene un espacio de
            comportamientos que no se puede enumerar. Cuatro piezas de una cosa cada
            una sí.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "La palanca de costo más grande del módulo",
        "title": "No todas las piezas necesitan el mismo modelo",
        "html": """
        <div class="box big">
          <p>En una cadena de cuatro pasos, típicamente <b>uno requiere juicio real y
          tres son mecánicos</b>. Clasificar, extraer, validar y transformar rara vez
          necesitan el modelo más capaz.</p>
        </div>
        <ul class="pts" style="margin-top:7mm">
          <li>Con el agente único no puedes elegir: todo pasa por el modelo más caro
            porque un solo paso lo necesitaba.</li>
          <li>Al dividir, cada pieza usa lo que le corresponde. Y esa decisión no
            cuesta calidad: los pasos mecánicos salen igual de bien.</li>
        </ul>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "Cuándo no dividir",
        "note": "Igual de importante, y mucho menos frecuente en lo que se publica.",
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Cuatro casos",
        "title": "Dividir también tiene un costo",
        "html": dg.cuando_no_dividir(),
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Contexto bajo demanda",
        "note": "El mismo patrón que ya has visto tres veces con nombres distintos.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Un patrón, tres apariciones",
        "title": "Traer la información cuando se usa",
        "html": """
        <div class="grid c3">
          <div class="card"><div class="k">EN LOS PROCEDIMIENTOS</div>
            <div class="t">Se cargan al activarse</div>
            <div class="d">En vez de meter todos los manuales de la empresa en las
            instrucciones fijas, entra solo el que la tarea necesita.</div></div>
          <div class="card"><div class="k">EN LA RECUPERACIÓN</div>
            <div class="t">Entra lo que la consulta pide</div>
            <div class="d">No se inyecta el corpus: se busca y se trae el fragmento
            que responde esa pregunta concreta.</div></div>
          <div class="card"><div class="k">EN LA ORQUESTACIÓN</div>
            <div class="t">Cada pieza recibe lo suyo</div>
            <div class="d">El contexto no viaja completo por toda la cadena: cada
            paso arranca con lo mínimo que necesita.</div></div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>Es la misma idea las tres veces. Nombrarla ayuda a reconocerla en
          situaciones nuevas: <b>el contexto se trae en el momento en que se usa, no
          por si acaso.</b></p>
        </div>""",
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "Dos ganancias que se confunden",
        "title": "Paralelo y segundo plano no son lo mismo",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>En paralelo</h3>
            <p>Reduce la <b>latencia total</b> cuando hay pasos independientes.</p>
            <p>Tres búsquedas que no dependen entre sí se lanzan a la vez y tardas lo
            que la más lenta, no la suma.</p>
            <p>No ahorra dinero: hace el mismo trabajo en menos tiempo.</p>
          </div>
          <div class="col">
            <h3>En segundo plano</h3>
            <p>Desacopla <b>lo que el usuario espera</b> de lo que no.</p>
            <p>La respuesta se devuelve ya; la indexación, el resumen o el envío
            ocurren después.</p>
            <p>Tampoco ahorra: mueve el trabajo fuera del camino crítico.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>La forma habitual de enterarse de que un trabajo en segundo plano terminó
          es que el servicio avise, con todas las obligaciones que eso trae.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "Una decisión de diseño muy rentable",
        "title": "Una lista de tareas explícita resuelve tres cosas a la vez",
        "html": """
        <ul class="pts">
          <li><b>Planificación.</b>
            <span class="n">El objetivo queda descompuesto en pasos concretos antes
            de empezar a ejecutar.</span></li>
          <li><b>Observación.</b>
            <span class="n">Marcar cada paso al completarlo es, de hecho, el registro
            de lo que ya se hizo. No hay que construirlo aparte.</span></li>
          <li><b>Trazabilidad para la persona.</b>
            <span class="n">Quien mira la pantalla ve dónde va el sistema y puede
            interrumpir con criterio en lugar de esperar a ciegas.</span></li>
        </ul>
        <div class="box" style="margin-top:7mm">
          <p>Es de las decisiones que más devuelven por lo poco que cuestan: una lista
          visible, mantenida por el propio sistema.</p>
        </div>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "Un flujo completo",
        "note": "Y los modos de fallo que solo aparecen cuando hay varias piezas.",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "De principio a fin",
        "title": "Cómo se ve un flujo orquestado",
        "html": dg.flujo_e2e(),
    },

    {
        "kind": "content", "covers": [8],
        "eyebrow": "Cuatro fallos propios de repartir",
        "title": "Dónde se rompe",
        "html": dg.donde_se_rompe(),
    },

    {
        "kind": "statement",
        "text": "El fallo más frecuente al orquestar <em>no da error</em>: la pieza "
                "siguiente no recibió un matiz y la respuesta sale peor.",
        "after": "Por eso repartir obliga a registrar qué entró y qué salió de cada "
                 "pieza, no solo el resultado final.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Menos preciso y más caro</div>
            <div class="d">Un agente con todo pierde en las dos.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Una frase sin «y»</div>
            <div class="d">Si no puedes describir la pieza así, son dos.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Un modelo por tarea</div>
            <div class="d">Tres de cada cuatro pasos son mecánicos.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Dividir también cuesta</div>
            <div class="d">Cuatro casos donde no conviene.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Bajo demanda</div>
            <div class="d">El mismo patrón que ya viste tres veces.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Paralelo ≠ segundo plano</div>
            <div class="d">Ninguno ahorra: mueven el tiempo.</div></div>
          <div class="card"><div class="k">07</div><div class="t">La lista de tareas</div>
            <div class="d">Resuelve plan, observación y trazabilidad.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">El fallo no da error</div>
            <div class="d">Contexto perdido en la frontera entre piezas.</div></div>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 15 · Orquestación.",
        "rows": [
            ("2", "La simultaneidad es el argumento. Si solo dices «es más caro», "
                  "suena a optimización opcional."),
            ("6", "Recorre el panel izquierdo primero y pregunta qué creen que va a "
                  "fallar. Casi siempre dicen el costo antes que la precisión."),
            ("8", "<b>La palanca del modelo por tarea es la que más dinero mueve.</b> "
                  "Pon un ejemplo con sus propios números si los tienen."),
            ("10", "Igual de importante que dividir es saber cuándo no. El sesgo del "
                   "momento empuja a partir todo."),
            ("12", "Nombra el patrón explícitamente. Que reconozcan que ya lo han "
                   "visto tres veces con nombres distintos es el objetivo."),
            ("17", "El contexto perdido en la frontera es el fallo que más tiempo "
                   "consume depurar porque no se anuncia."),
        ],
    },
]
