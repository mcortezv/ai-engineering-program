# -*- coding: utf-8 -*-
"""Deck: Módulo 18 — Seguridad."""

from engine.diagrams import mod18 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 18 · Seguridad",
    "footer": "Programa de AI · Módulo 18",
    "outfile": "Modulo 18 - Seguridad.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 18  ·  2 HORAS",
        "title": "Seguridad",
        "tagline": "Todo lo que entra al contexto es contenido no confiable, incluida "
                   "la respuesta de una herramienta.",
        "meta": [
            "<b>Antes de esta sesión:</b> agentes, protocolos, recuperación y trazas",
            "<b>Al terminar:</b> sabes en qué capa poner cada control y qué no tiene "
            "arreglo",
        ],
    },

    {
        "kind": "statement",
        "text": "El sistema toma decisiones a partir de texto, y ese texto <em>puede "
                "venir de fuera</em>.",
        "after": "En software tradicional los datos son datos y el código es código. "
                 "Aquí un texto que llega como dato puede acabar funcionando como "
                 "instrucción. Esa confusión de planos es el origen de casi todo.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Dónde se pone un control</b> — cuatro capas, y cuánto se puede
            confiar en cada una.</li>
          <li><b>Validar la salida</b> — y la regla que nunca se rompe.</li>
          <li><b>Inyección de prompts</b> — la directa, la indirecta, y por qué no
            tiene solución completa.</li>
          <li><b>Secretos</b> — tres reglas concretas.</li>
          <li><b>Riesgos de costo</b> — que también son de seguridad.</li>
          <li><b>Lista de verificación</b> — para pegar en el repositorio.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Dónde se pone el control",
        "note": "La misma regla puede ser un control real o una expectativa, según "
                "dónde viva.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Cuatro capas",
        "title": "Cuánto se puede confiar en cada una",
        "html": dg.capas_control(),
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "La analogía que sí funciona",
        "title": "Un guardrail no dirige: evita que te salgas",
        "html": """
        <ul class="pts">
          <li><b>En la carretera no te llevan a ningún sitio: impiden que el coche se
            descarrile.</b>
            <span class="n">Lo mismo aquí: no hacen que el sistema haga lo correcto,
            hacen que no pueda hacer lo catastrófico.</span></li>
          <li><b>Y por eso van en el sitio donde no se pueden negociar.</b>
            <span class="n">Un guardrail pintado en el suelo no sujeta nada. Uno
            escrito en el prompt es exactamente eso: una petición al modelo que
            compite con todo el resto del contexto.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [2, 3],
        "eyebrow": "La salida estructurada como control",
        "title": "Reduce lo que el sistema puede llegar a hacer",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Lo que sí consigue</h3>
            <p>Si la respuesta solo puede ser una de tres acciones enumeradas, el
            modelo <b>no puede pedir una cuarta</b>.</p>
            <p>No es comodidad de parseo: es reducir el espacio de lo posible.</p>
          </div>
          <div class="col">
            <h3>Lo que no</h3>
            <p>Una salida perfectamente válida puede contener un dato inventado o una
            acción legítima aplicada al registro equivocado.</p>
            <p>La forma no dice nada del contenido.</p>
          </div>
        </div>
        <div class="box danger" style="margin-top:7mm">
          <p class="lab">La regla que nunca se rompe</p>
          <p><b>Ninguna decisión de autorización se toma a partir de un campo que
          devolvió el modelo.</b> Si responde que el usuario es administrador, eso no
          es una autorización: es una cadena de texto que alguien pudo inducir. La
          autorización se resuelve en el servidor, con la sesión real, antes de
          ejecutar.</p>
        </div>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "Inyección de prompts",
        "note": "La parte incómoda de la sesión: hay un problema sin solución "
                "completa.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Dos formas, muy distintas",
        "title": "La directa y la indirecta",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>Directa</h3>
            <p>El usuario escribe algo para que el sistema se comporte como no debe.</p>
            <p><b>Es la menos peligrosa:</b> solo puede afectar a su propia sesión, y
            normalmente solo consigue hacerse daño a sí mismo.</p>
          </div>
          <div class="col accent">
            <h3>Indirecta</h3>
            <p>El atacante <b>no habla con el sistema</b>: deja el texto donde el
            sistema lo va a leer.</p>
            <p>Un documento que vas a indexar, una página que una herramienta
            consulta, un ticket que el agente procesa.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>La segunda es la que importa, y es la que casi nunca se contempla al
          diseñar.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "El camino del ataque",
        "title": "Cómo llega sin hablar contigo",
        "html": dg.inyeccion_indirecta(),
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "La combinación peligrosa",
        "title": "Tres condiciones que juntas abren una salida",
        "html": dg.triada_peligrosa(),
    },

    {
        "kind": "content", "covers": [4, 8],
        "eyebrow": "Lo que sí se puede hacer",
        "title": "Seis defensas parciales que juntas sirven",
        "html": """
        <ul class="pts tight">
          <li><b>Privilegios mínimos por tarea.</b> El agente que resume tickets no
            necesita poder borrar registros.</li>
          <li><b>Separar quien lee de quien actúa.</b> Un agente procesa contenido
            ajeno y produce una propuesta; otro, sin acceso a ese contenido, la
            ejecuta.</li>
          <li><b>Confirmación humana en lo irreversible</b> y en todo lo que sale
            hacia fuera.</li>
          <li><b>Delimitar y etiquetar el contenido externo</b> en el prompt, para que
            al menos esté marcado como lo que es.</li>
          <li><b>Validar todas las acciones en el servidor</b>, con la sesión real.</li>
          <li><b>Registrarlo todo</b>, porque es lo único que permite detectar que
            ocurrió.</li>
        </ul>
        <div class="box danger" style="margin-top:6mm">
          <p>Ninguna de las seis lo resuelve. Juntas hacen que el ataque necesite mucha
          más suerte, y que se note cuando pasa.</p>
        </div>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Secretos y presupuesto",
        "note": "Dos superficies que se pasan por alto por parecer aburridas.",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Tres reglas concretas",
        "title": "Las credenciales no entran al contexto",
        "html": """
        <ol class="pts">
          <li><b>Nunca pases credenciales al modelo.</b>
            <span class="n">Ni en las instrucciones fijas, ni como argumento de una
            herramienta, ni dentro de un documento indexado. El modelo no las
            necesita: las necesita el código que ejecuta la herramienta.</span></li>
          <li><b>Viven en el servidor de la herramienta</b>, no en el contexto del
            agente.
            <span class="n">Es el argumento fuerte a favor de exponer capacidades a
            través de un canal con frontera propia.</span></li>
          <li><b>Todo lo que entra al prompt puede salir.</b>
            <span class="n">Un secreto en el contexto es un secreto que puede aparecer
            en una respuesta, en un registro y en una traza. Tres sistemas en lugar de
            uno.</span></li>
        </ol>""",
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "Cuatro riesgos que vacían el presupuesto",
        "title": "Agotar recursos también es un ataque",
        "html": dg.riesgos_costo(),
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lista de verificación",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Credenciales fuera del contexto</div>
            <div class="d">Viven en el servidor de la herramienta.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Validación por código</div>
            <div class="d">Antes de actuar sobre cualquier salida.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Autorización en el servidor</div>
            <div class="d">Nunca con un campo que devolvió el modelo.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Permisos mínimos</div>
            <div class="d">Por tarea, no por sistema.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Confirmación humana</div>
            <div class="d">En lo irreversible y en lo que sale hacia fuera.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Topes</div>
            <div class="d">Iteraciones, tamaño de entrada y presupuesto.</div></div>
          <div class="card"><div class="k">07</div><div class="t">Contenido externo marcado</div>
            <div class="d">Delimitado y tratado como no confiable.</div></div>
          <div class="card no"><div class="k">08</div><div class="t">Trazas redactadas</div>
            <div class="d">Los datos sensibles se quitan antes de emitir.</div></div>
        </div>""",
    },

    {
        "kind": "statement",
        "text": "No existe una defensa completa contra la inyección indirecta, y "
                "conviene <em>decirlo en voz alta</em>.",
        "after": "El problema es estructural: el modelo no puede distinguir de forma "
                 "fiable instrucciones de datos cuando los dos son texto en el mismo "
                 "contexto. Se diseña asumiendo que va a pasar.",
    },
]


NOTES = [
    {
        "lead": "Módulo 18 · Seguridad.",
        "rows": [
            ("2", "El encuadre de la confusión de planos es lo que hace que el resto "
                  "se entienda. Sin él, la inyección parece un truco y no un problema "
                  "estructural."),
            ("6", "<b>Recorre la tabla de abajo arriba</b> y pregunta dónde están sus "
                  "controles hoy. Casi siempre en la capa menos fiable."),
            ("9", "La regla de la autorización merece decirse dos veces. Es el error "
                  "que más daño hace y el más fácil de cometer."),
            ("12", "<b>Núcleo de la sesión.</b> La inyección indirecta casi nunca se "
                   "contempla al diseñar. Que quede claro que el atacante no "
                   "necesita hablar con el sistema."),
            ("13", "La tríada da un criterio operativo: basta con romper una de las "
                   "tres. Es lo más accionable del módulo."),
            ("17", "Los riesgos de costo suelen tratarse como tema de finanzas. "
                   "Plantéalos como denegación de servicio y cambia la conversación."),
            ("19", "<b>Cierra con la honestidad, no con la lista.</b> Un equipo que "
                   "sabe que esto no tiene solución completa diseña mejor que uno que "
                   "cree estar cubierto."),
        ],
    },
]
