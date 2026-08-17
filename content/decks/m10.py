# -*- coding: utf-8 -*-
"""Deck: Módulo 10 — Protocolos de comunicación."""

from engine.diagrams import mod10 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 10 · Protocolos de comunicación",
    "footer": "Programa de AI · Módulo 10",
    "outfile": "Modulo 10 - Protocolos de comunicacion.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 10  ·  2.5 HORAS",
        "title": "Protocolos de comunicación",
        "tagline": "API, REST, webhooks y MCP: la misma idea vista desde cuatro "
                   "ángulos.",
        "meta": [
            "<b>Antes de esta sesión:</b> qué necesita un agente con herramientas",
            "<b>Al terminar:</b> eliges el protocolo por quién inicia y quién "
            "consume",
        ],
    },

    {
        "kind": "statement",
        "text": "Un protocolo es un <em>contrato entre dos sistemas que no se "
                "conocen</em>.",
        "after": "Quién habla primero, en qué formato, qué significa cada respuesta y "
                 "qué pasa si algo falla. Todo lo demás son variaciones sobre eso.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Tres palabras que no son sinónimos</b> — API, REST y HTTP.</li>
          <li><b>El modelo pull</b> — y el compromiso incómodo del sondeo.</li>
          <li><b>El modelo push</b> — webhooks y lo que cuesta recibirlos.</li>
          <li><b>Streaming</b> — de dónde salen los tokens que aparecen uno a
            uno.</li>
          <li><b>MCP</b> — qué problema resuelve, sus transportes y sus tres
            primitivas.</li>
          <li><b>Los cuatro lado a lado</b> — y la diferencia que de verdad
            importa.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Tres palabras distintas",
        "note": "En conversación se usan como sinónimos, y esa confusión se lleva "
                "la mitad de las preguntas del tema.",
    },

    {
        "kind": "content", "covers": [1, 2],
        "eyebrow": "Desambiguar antes de empezar",
        "title": "API, REST y HTTP son tres capas, no tres nombres",
        "html": dg.api_rest_http(),
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "Pull y push",
        "note": "Quién pregunta y quién avisa. De ahí sale casi todo lo demás.",
    },

    {
        "kind": "content", "covers": [3, 4],
        "eyebrow": "Los dos modelos",
        "title": "El cliente pregunta, o el servidor avisa",
        "html": dg.pull_vs_push(),
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Lo poco que hay que decir de REST",
        "title": "Idempotencia: el detalle que sí importa aquí",
        "html": """
        <ul class="pts">
          <li><b>En sistemas de AI los tiempos de espera se agotan con frecuencia y
            los reintentos son la norma.</b>
            <span class="n">Las peticiones tardan segundos o minutos, los servicios
            se saturan, y tu código reintenta.</span></li>
          <li><b>Un reintento sobre una operación no idempotente cobra dos veces.</b>
            <span class="n">O duplica un registro, o envía dos correos. No es un
            tecnicismo: es el fallo que más veces aparece en producción.</span></li>
          <li><b>La solución es una clave de operación, no rezar.</b>
            <span class="n">Un identificador que el servidor usa para reconocer que
            esa petición ya la procesó.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Lo que cuesta recibir eventos",
        "title": "Cuatro obligaciones que no son opcionales",
        "html": dg.obligaciones_webhook(),
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "El tercer patrón",
        "title": "Streaming: de dónde salen los tokens uno a uno",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>SSE</h3>
            <p>Un canal <b>unidireccional</b> del servidor al cliente, sobre HTTP
            normal.</p>
            <p>Es lo que usan las APIs de modelos para el streaming. Cuando ves los
            tokens aparecer uno a uno, es esto.</p>
            <p>Simple de operar: no necesita infraestructura especial.</p>
          </div>
          <div class="col">
            <h3>WebSocket</h3>
            <p>Un canal <b>bidireccional</b> y permanente.</p>
            <p>Aparece cuando hace falta hablar en los dos sentidos a la vez, como
            en las APIs de voz.</p>
            <p>Más potente y bastante más caro de operar.</p>
          </div>
        </div>""",
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "Un protocolo que ya usaste sin llamarlo así",
        "title": "Pedir una herramienta también es un contrato",
        "html": """
        <ul class="pts">
          <li><b>El modelo emite una llamada estructurada y tu código responde con
            un resultado.</b>
            <span class="n">Tiene formato definido, tiene un iniciador —el modelo—
            y tiene un consumidor —tu código—. Eso es un protocolo.</span></li>
          <li><b>Verlo así hace que lo siguiente se entienda solo.</b>
            <span class="n">Si eso es un contrato, estandarizarlo permite que
            cualquier sistema de AI hable con cualquier proveedor de
            capacidades.</span></li>
        </ul>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "MCP",
        "note": "Qué problema resuelve, cómo se transporta y quién controla cada "
                "cosa.",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "El problema que resuelve",
        "title": "Multiplicación contra suma",
        "html": dg.problema_nxm(),
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Cómo se conecta",
        "title": "Dos transportes, y es lo primero que se decide",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Proceso local</h3>
            <p>El servidor es un proceso en la misma máquina que se comunica por
            entrada y salida estándar.</p>
            <p>Ideal para herramientas de escritorio y línea de comandos.</p>
            <p><b>Ventaja fuerte:</b> nada sale a la red.</p>
          </div>
          <div class="col">
            <h3>HTTP remoto</h3>
            <p>El servidor es un servicio al que te conectas por red.</p>
            <p>Necesario para servidores compartidos y multiusuario.</p>
            <p><b>Y por tanto:</b> autenticación y autorización de verdad, no como
            añadido.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>La arquitectura son tres piezas: el <b>host</b> —tu aplicación de AI—,
          el <b>cliente</b> —la parte del host que habla el protocolo— y el
          <b>servidor</b> —el proceso que expone las capacidades.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Las tres primitivas",
        "title": "Se entienden por quién las controla",
        "html": dg.primitivas_mcp(),
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "La pregunta que alguien va a hacer en voz alta",
        "title": "¿Por qué existe esto si ya hay APIs?",
        "html": """
        <div class="box big">
          <p>Porque <b>cambia quién lee el contrato</b>.</p>
        </div>
        <div class="cols" style="margin-top:7mm">
          <div class="col">
            <h3>Una API REST</h3>
            <p>La lee una persona desarrolladora, la entiende y escribe código que
            la llama.</p>
            <p>El contrato se resuelve <b>antes</b> de ejecutar.</p>
          </div>
          <div class="col accent">
            <h3>Un servidor de capacidades</h3>
            <p>Lo lee el modelo, <b>en tiempo de ejecución</b>: pregunta qué hay,
            recibe descripciones escritas para ser interpretadas por un modelo, y
            decide cuál usar.</p>
            <p>Conectas uno nuevo y el agente sabe usarlo sin recompilar nada.</p>
          </div>
        </div>
        <div class="box" style="margin-top:6mm">
          <p>Y de ahí se sigue algo concreto: <b>la calidad de las descripciones es
          un problema de prompt engineering</b>, no de documentación.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Bajar expectativas",
        "title": "Qué no es",
        "html": """
        <div class="grid c3">
          <div class="card no"><div class="k">NO</div>
            <div class="t">No reemplaza a REST</div>
            <div class="d">La gran mayoría de estos servidores son una envoltura
            que por debajo llama a una API REST de toda la vida.</div></div>
          <div class="card no"><div class="k">NO</div>
            <div class="t">No comunica agentes entre sí</div>
            <div class="d">Es entre un host de AI y un proveedor de capacidades.
            Otra cosa es otro problema.</div></div>
          <div class="card no"><div class="k">NO</div>
            <div class="t">No da seguridad</div>
            <div class="d">Da un lugar donde ponerla. Cada servidor conectado es
            superficie de ataque nueva.</div></div>
        </div>
        <div class="box alerta" style="margin-top:7mm">
          <p class="lab">La regla que hay que llevarse</p>
          <p>Todo lo que devuelve una herramienta <b>entra a tu contexto como texto
          que el modelo va a leer</b>. Conectar un servidor de terceros es darle
          acceso a tu contexto a código ajeno.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [8],
        "eyebrow": "Cierre",
        "title": "Los cuatro lado a lado",
        "html": dg.cuatro_protocolos(),
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ejercicio práctico",
        "title": "Construye un servidor de capacidades mínimo",
        "html": """
        <ol class="pts">
          <li><b>Expón una capacidad de cada tipo:</b> una acción que consulte algo
            real de tu entorno, un recurso de solo lectura con un documento de
            referencia, y una plantilla de uso frecuente en el equipo.</li>
          <li><b>Conéctalo a un cliente real</b> y verifica que el agente lo
            descubre y lo usa sin configuración adicional.</li>
        </ol>
        <div class="box big" style="margin-top:7mm">
          <p>La entrega responde a dos preguntas: <b>¿por qué modelaste cada
          capacidad como acción, recurso o plantilla y no como otra cosa?</b> y
          <b>¿qué podría hacer un atacante que controlara el texto que devuelve tu
          herramienta?</b></p>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 10 · Protocolos de comunicación — láminas 1 a 11.",
        "rows": [
            ("2", "El hilo conductor de toda la sesión. Si se pierde, el módulo se "
                  "convierte en cuatro temas sueltos."),
            ("6", "<b>Desambigua antes de nada.</b> Media hora de preguntas se evita "
                  "con esta lámina, y además prepara la de los transportes: un "
                  "protocolo puede ir sobre HTTP o sobre un proceso local."),
            ("8", "El público conoce REST; no lo repases. Ve directo al compromiso "
                  "del sondeo, que es lo que da origen a lo siguiente."),
            ("10", "<b>Insiste en las cuatro obligaciones.</b> La de responder rápido "
                   "y procesar después es la que más veces se incumple, y produce "
                   "tormentas de reintentos que parecen un ataque."),
        ],
    },
    {
        "lead": "Láminas 12 a 20, sobre MCP.",
        "rows": [
            ("13", "Haz la cuenta con números suyos: cuántos clientes de AI y "
                   "cuántos sistemas internos tienen. El resultado convence más que "
                   "el diagrama genérico."),
            ("15", "<b>Las tres primitivas se explican por quién las controla.</b> "
                   "Es el ángulo que da criterio para diseñar un servidor propio en "
                   "lugar de meterlo todo como acciones."),
            ("16", "La pregunta del «¿para qué, si ya hay APIs?» va a salir sola. "
                   "Déjala salir antes de contestarla."),
            ("17", "Cierra bajando expectativas. Las expectativas infladas hacen más "
                   "daño que el desconocimiento, y el punto de seguridad enlaza con "
                   "lo que viene después en el programa."),
            ("18", "La última columna de la última fila resume el módulo entero: es "
                   "el único cuyo consumidor es el modelo."),
        ],
    },
]
