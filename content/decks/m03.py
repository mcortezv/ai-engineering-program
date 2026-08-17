# -*- coding: utf-8 -*-
"""Deck: Módulo 3 — Conceptos básicos: tokens y ventana de contexto."""

from engine.diagrams import mod03 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 3 · Tokens y ventana de contexto",
    "footer": "Programa de AI · Módulo 3",
    "outfile": "Modulo 03 - Tokens y ventana de contexto.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 3  ·  2 HORAS",
        "title": "Tokens y ventana de contexto",
        "tagline": "Las dos unidades con las que se mide todo lo demás: lo que el "
                   "modelo lee y lo que cabe.",
        "meta": [
            "<b>Antes de esta sesión:</b> qué es un modelo y quién lo fabrica",
            "<b>Al terminar:</b> sabes estimar el consumo de una funcionalidad",
        ],
    },

    {
        "kind": "statement",
        "text": "El modelo <em>nunca ve</em> las palabras que escribes.",
        "after": "Ve números enteros. Y de ese detalle, que parece técnico y menor, "
                 "salen el precio, los errores de formato raros y la razón de que "
                 "sea malo con la aritmética.",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Qué es un token</b> — y por qué no es ni una palabra ni una
            letra.</li>
          <li><b>Tokenización en vivo</b> — cuatro cosas que solo se ven jugando
            con un tokenizador.</li>
          <li><b>El token como unidad de cobro</b> — la aritmética que hay que
            saber hacer.</li>
          <li><b>La ventana de contexto</b> — qué cabe, y todo lo que ocupa espacio
            sin que te des cuenta.</li>
          <li><b>Los tres modos de fallo</b> — y por qué el peor no da error.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "01",
        "title": "Qué es un token",
        "note": "El texto se parte en fragmentos y cada fragmento se cambia por su "
                "número en un vocabulario.",
    },

    {
        "kind": "content",
        "covers": [1, 2],
        "eyebrow": "El mismo significado, dos idiomas",
        "title": "Un token no es una palabra",
        "html": dg.tokenizacion(),
    },

    {
        "kind": "content",
        "covers": [2],
        "eyebrow": "Lo que se descubre jugando con un tokenizador",
        "title": "Cuatro hallazgos que valen media sesión",
        "html": """
        <ul class="pts">
          <li><b>Las palabras frecuentes son un token; las raras se parten.</b>
            <span class="n">Un nombre propio poco común puede costar cinco o seis
            piezas. Tu jerga interna es cara.</span></li>
          <li><b>El espacio pertenece al token.</b>
            <span class="n">La misma palabra al principio de una frase y en medio
            produce tokens distintos. Explica errores de formato que si no se sabe
            parecen embrujos.</span></li>
          <li><b>El español cuesta más que el inglés.</b>
            <span class="n">Los vocabularios se entrenaron sobre todo con inglés.
            El mismo producto es más caro de operar en español, y no es
            opinable.</span></li>
          <li><b>Los números y el código se fragmentan de forma extraña.</b>
            <span class="n">Una cifra larga puede partirse sin lógica aparente. Es
            una de las razones de que la aritmética exacta se le dé mal.</span></li>
        </ul>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "02",
        "title": "El token como unidad de cobro",
        "note": "Es la unidad de medida del sistema y la unidad de la factura.",
    },

    {
        "kind": "content",
        "covers": [3, 6],
        "eyebrow": "La aritmética que hay que saber hacer",
        "title": "De caracteres a pesos",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>Reglas de bolsillo</h3>
            <p>Un token ronda los <b>cuatro caracteres</b> en inglés, y algo menos
            en español.</p>
            <p>Una página de texto está en el orden de <b>500 a 700 tokens</b>.</p>
            <p>Son aproximaciones gruesas: para decidir, se mide con el tokenizador
            del proveedor.</p>
          </div>
          <div class="col accent">
            <h3>Lo que se cobra</h3>
            <p>Los tokens que <b>entran</b> y los que <b>salen</b>, con precios
            distintos.</p>
            <p>Lo que sale suele costar varias veces más que lo que entra.</p>
            <p>Consecuencia inmediata: acortar la respuesta ahorra más que acortar
            la pregunta.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p><b>Mide antes de estimar.</b> Todos los proveedores publican su
          tokenizador. Contar sobre el texto real de tu producto toma cinco minutos
          y evita presupuestos que fallan por un factor de dos.</p>
        </div>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "03",
        "title": "La ventana de contexto",
        "note": "El máximo de tokens que el modelo puede tener presentes en una "
                "sola petición. Casi nadie sabe qué cuenta dentro.",
    },

    {
        "kind": "content",
        "covers": [4],
        "eyebrow": "Qué ocupa el espacio en realidad",
        "title": "La pregunta del usuario es la parte pequeña",
        "html": dg.ventana_contexto(),
    },

    {
        "kind": "content",
        "covers": [5],
        "eyebrow": "Tres situaciones distintas",
        "title": "Qué pasa cuando el contexto se llena",
        "html": dg.fallos_contexto(),
    },

    {
        "kind": "statement",
        "text": "Una ventana de contexto más grande <em>no es automáticamente "
                "mejor</em>.",
        "after": "Llenar un millón de tokens con documentos por si acaso produce "
                 "respuestas peores y facturas más altas que enviar los tres "
                 "párrafos que hacían falta.",
    },

    {
        "kind": "content",
        "covers": [4],
        "eyebrow": "Una aclaración que evita meses de confusión",
        "title": "La ventana de contexto no es memoria",
        "html": """
        <ul class="pts">
          <li><b>No hay nada que persista entre una petición y la siguiente.</b>
            <span class="n">La ventana se llena, se procesa y se descarta. La
            siguiente petición empieza vacía.</span></li>
          <li><b>La sensación de que un chat «recuerda» viene de otro sitio.</b>
            <span class="n">La aplicación guarda los mensajes y los reenvía
            completos cada vez. Sin ese reenvío no hay memoria de ningún
            tipo.</span></li>
          <li><b>Por eso el turno veinte cuesta mucho más que el primero.</b>
            <span class="n">Cada turno arrastra todo lo anterior. El costo de una
            conversación no crece de forma lineal con su longitud.</span></li>
        </ul>""",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">El modelo lee números</div>
            <div class="d">El texto se parte en tokens y cada uno se cambia por su
            índice.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Un token no es una palabra</div>
            <div class="d">Y el español gasta notablemente más que el inglés.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Entrada y salida cuestan distinto</div>
            <div class="d">Acortar la respuesta ahorra más que acortar el
            prompt.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Casi todo lo que ocupa lo pusiste tú</div>
            <div class="d">Instrucciones, herramientas, historial y la respuesta que
            aún no existe.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Tres modos de fallo</div>
            <div class="d">Error, truncado silencioso y dilución. El tercero es el
            caro.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Más ventana no es mejor</div>
            <div class="d">Llenarla por si acaso empeora la respuesta y sube la
            factura.</div></div>
          <div class="card"><div class="k">07</div><div class="t">La ventana no es memoria</div>
            <div class="d">Nada persiste entre peticiones.</div></div>
          <div class="card no"><div class="k">✓</div><div class="t">Mide, no estimes</div>
            <div class="d">El tokenizador del proveedor está a un clic.</div></div>
        </div>""",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Ejercicio práctico",
        "title": "Mide tu propio consumo",
        "html": """
        <ol class="pts">
          <li><b>Toma el prompt más largo que tengas en producción</b> y mídelo con
            el tokenizador oficial del proveedor.</li>
          <li><b>Calcula una conversación de veinte turnos</b> reenviando el
            historial completo cada vez.
            <span class="n">El total no es veinte veces el primero. Averigua
            cuánto es.</span></li>
          <li><b>Traduce el mismo texto al inglés</b>, vuelve a medirlo y anota la
            diferencia porcentual.</li>
          <li><b>Estima el costo mensual</b> asumiendo mil conversaciones, con los
            precios vigentes del proveedor.</li>
        </ol>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 3 · Tokens y ventana de contexto.",
        "rows": [
            ("2", "Abre con la afirmación desnuda y deja que incomode un momento "
                  "antes de explicarla."),
            ("5", "<b>Proyecta un tokenizador y pega frases que proponga la sala.</b> "
                  "La lámina sirve de apoyo, pero la sesión gana muchísimo si lo "
                  "ven funcionar en vivo con sus propias palabras. Pide un nombre "
                  "propio raro y un número largo."),
            ("6", "Los cuatro hallazgos salen solos del tokenizador. Deja que los "
                  "descubran ellos antes de leerlos."),
            ("8", "La regla de los cuatro caracteres es una aproximación y hay que "
                  "decir que lo es. El punto real es el de abajo: medir toma cinco "
                  "minutos."),
            ("10", "Enumera en voz alta todo lo que cuenta dentro de la ventana "
                   "antes de mostrar el gráfico. Casi todo el mundo asume que la "
                   "ventana es «para mi texto», y la sorpresa es el aprendizaje."),
            ("11", "Detente en el tercer modo de fallo. Es el que no da error, no "
                   "aparece en ninguna métrica y se lleva el presupuesto."),
            ("13", "Cierra insistiendo en que la ventana no es memoria. Es la "
                   "confusión más cara de las que se arrastran desde aquí."),
        ],
    },
]
