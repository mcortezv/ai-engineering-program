# -*- coding: utf-8 -*-
"""Deck: Módulo 8 — Contexto y memoria."""

from engine.diagrams import mod08 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 8 · Contexto y memoria",
    "footer": "Programa de AI · Módulo 8",
    "outfile": "Modulo 08 - Contexto y memoria.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 8  ·  2 HORAS",
        "title": "Contexto y memoria",
        "tagline": "Si nada persiste entre peticiones, alguien tiene que decidir qué "
                   "se guarda y qué se descarta.",
        "meta": [
            "<b>Antes de esta sesión:</b> cómo se consume un modelo como servicio",
            "<b>Al terminar:</b> diseñas la arquitectura de memoria de un producto",
        ],
    },

    {
        "kind": "statement",
        "text": "La memoria de un sistema de AI no es una función del modelo: es una "
                "<em>decisión de arquitectura</em>.",
        "after": "No existe una implementación correcta universal. Existe la que "
                 "corresponde al producto que estás construyendo.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Los tres tipos de memoria</b> — y qué son en realidad, más allá del
            nombre prestado.</li>
          <li><b>Cuándo guardar y cuándo no</b> — el problema difícil, que sigue
            abierto.</li>
          <li><b>Cuatro estrategias de historial</b> — y qué pierde cada una.</li>
          <li><b>El triple costo</b> — precisión, latencia y dinero, siempre a la
            vez.</li>
          <li><b>Identificadores</b> — sesión, usuario y espacio de trabajo.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "De dónde sale el problema",
        "note": "Es la consecuencia directa de algo que ya sabemos: cada petición "
                "empieza de cero.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "El punto de partida",
        "title": "Si el servicio no guarda nada, la memoria la construyes tú",
        "html": """
        <ul class="pts">
          <li><b>Todo lo que quieras que el sistema «recuerde» tiene que estar en la
            petición.</b>
            <span class="n">No hay otro lugar. La memoria de un producto de AI es,
            literalmente, qué texto decides incluir cada vez.</span></li>
          <li><b>Eso convierte una función de producto en una decisión técnica con
            precio.</b>
            <span class="n">«Que se acuerde de mis preferencias» no es una casilla
            que se activa: es una base de datos, una política de escritura y unos
            tokens que se pagan en cada llamada.</span></li>
          <li><b>Y en una decisión de producto con consecuencias visibles.</b>
            <span class="n">Un sistema que recuerda de más incomoda; uno que recuerda
            de menos frustra. El punto medio no lo elige el modelo.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Los tres nombres, traducidos",
        "title": "Qué son en realidad",
        "html": dg.tres_memorias(),
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Una honestidad que conviene tener",
        "title": "Los nombres vienen prestados y describen mal lo que pasa",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>Lo que sugiere el nombre</h3>
            <p>Un cerebro que consolida, que olvida gradualmente, que reconstruye
            recuerdos y que decide solo qué es importante.</p>
          </div>
          <div class="col accent">
            <h3>Lo que hay</h3>
            <p>Una base de datos, unas consultas y una política que alguien
            escribió sobre qué leer y cuándo.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>Conviene usar los tres nombres porque son los que vas a encontrar en
          cualquier documentación, pero <b>traducirlos mentalmente a lo que son</b>.
          Con la traducción hecha, la discusión deja de ser sobre neurociencia y
          pasa a ser sobre qué se lee, de dónde y en qué momento.</p>
        </div>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "El problema difícil",
        "note": "Cuándo guardar algo y cuándo no. No está resuelto, y conviene "
                "decirlo.",
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Las cuatro tensiones",
        "title": "No hay criterio universal, y no lo va a haber",
        "html": """
        <ul class="pts">
          <li><b>Guardar de más contamina.</b>
            <span class="n">Si persistes todo lo que el usuario dice, en tres
            semanas el sistema recupera preferencias que ya cambiaron y las aplica
            con confianza. Y el usuario no puede ver qué está influyendo.</span></li>
          <li><b>Guardar de menos frustra.</b>
            <span class="n">El usuario repite información que ya dio y el producto
            se siente tonto.</span></li>
          <li><b>Lo que importa depende del contexto de la persona.</b>
            <span class="n">«Soy vegetariano» es un dato permanente en una app de
            recetas y ruido irrelevante en una de facturación.</span></li>
          <li><b>Todo lo que recuperas se paga.</b>
            <span class="n">Cada hecho inyectado son tokens en cada petición, para
            siempre.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Enfoques que se usan en la práctica",
        "title": "Cuatro formas de decidir qué se guarda",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div>
            <div class="t">Extracción automática</div>
            <div class="d">Al terminar la sesión, el propio modelo extrae los hechos
            que valen la pena. Barato y escalable; se equivoca sin avisar.</div></div>
          <div class="card"><div class="k">02</div>
            <div class="t">Confirmada por el usuario</div>
            <div class="d">«¿Guardo esto?». Más lenta y mucho más segura. La única
            que el usuario puede auditar.</div></div>
          <div class="card"><div class="k">03</div>
            <div class="t">Derivada de acciones</div>
            <div class="d">No de lo que dice, sino de lo que hace. Más fiable que
            las declaraciones, y más difícil de interpretar.</div></div>
          <div class="card"><div class="k">04</div>
            <div class="t">Con caducidad</div>
            <div class="d">Por tiempo o por desuso. Complemento de cualquiera de
            las anteriores, no alternativa.</div></div>
        </div>
        <div class="box" style="margin-top:6mm">
          <p><b>Es un área de investigación abierta.</b> Preséntalo como una decisión
          de diseño con criterios, no como una técnica con respuesta correcta.</p>
        </div>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Estrategias de historial",
        "note": "El problema concreto: la conversación ya no cabe. Cuatro salidas.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Cuatro formas de hacer que quepa",
        "title": "Cada una tira algo distinto",
        "html": dg.estrategias_historial(),
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Un detalle de implementación que cuesta dinero",
        "title": "Cortar por el principio tiene un efecto que no se ve",
        "html": """
        <ul class="pts">
          <li><b>Los proveedores cobran mucho más barato la parte del prompt que
            ya han procesado antes</b>, siempre que empiece exactamente igual.</li>
          <li><b>Truncar el historial por el principio cambia ese inicio en cada
            petición.</b>
            <span class="n">Con lo cual esa ventaja desaparece justo en las
            conversaciones largas, que son las que más se beneficiarían.</span></li>
          <li><b>La forma de evitarlo es mantener estable el bloque inicial.</b>
            <span class="n">Instrucciones, definiciones y resumen consolidado
            arriba, y que lo que rote sea solo la cola.</span></li>
        </ul>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "Lo que cuesta recordar",
        "note": "Tres costos que se pagan a la vez y conviene ver juntos.",
    },

    {
        "kind": "content", "covers": [5, 7],
        "eyebrow": "El triple costo",
        "title": "Toda memoria se paga tres veces",
        "html": dg.triple_costo(),
    },

    {
        "kind": "statement",
        "text": "Un sistema que nunca olvida se vuelve <em>más caro, más lento y "
                "menos preciso</em> con cada conversación.",
        "after": "Por eso el olvido no es un fallo que haya que compensar: es una "
                 "función del producto que hay que especificar igual que las demás.",
    },

    # ── 05 ────────────────────────────────────────────────────────────────
    {
        "kind": "content", "covers": [6],
        "eyebrow": "Lo concreto",
        "title": "Tres identificadores que conviene tener desde el primer día",
        "html": """
        <table>
          <thead><tr><th style="width:22%">Identificador</th><th style="width:38%">Para qué</th>
          <th>Por qué desde el principio</th></tr></thead>
          <tbody>
            <tr><td><b>sesión</b></td>
              <td>Reconstruir una conversación completa.</td>
              <td>Es lo que después permite depurar «este usuario dice que la
                  respuesta fue mala».</td></tr>
            <tr><td><b>usuario</b></td>
              <td>Recuperar lo que sabemos de esa persona.</td>
              <td>Sin él no hay memoria persistente posible.</td></tr>
            <tr><td><b>espacio de trabajo</b></td>
              <td>Aislar los datos de un cliente de los de otro.</td>
              <td>No es organización: es seguridad. Añadirlo después obliga a migrar
                  todo lo guardado.</td></tr>
          </tbody>
        </table>
        <div class="box" style="margin-top:6mm">
          <p>Estos mismos identificadores son los que permiten después atribuir el
          gasto y seguir el rastro de una petición de principio a fin. Diseñarlos
          una vez sirve para las tres cosas.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">La memoria la construyes tú</div>
            <div class="d">No es una función del modelo.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Los tres nombres son prestados</div>
            <div class="d">Debajo hay una base de datos y una política.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Qué guardar sigue abierto</div>
            <div class="d">Hay criterios, no respuesta correcta.</div></div>
          <div class="card"><div class="k">04</div><div class="t">La memoria equivocada es peor</div>
            <div class="d">Que la memoria ausente, y encima es invisible.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Cuatro estrategias</div>
            <div class="d">Cada una tira algo. Elige sabiendo qué.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Triple costo</div>
            <div class="d">Precisión, latencia y dinero, siempre juntos.</div></div>
          <div class="card"><div class="k">07</div><div class="t">Tres identificadores</div>
            <div class="d">Sesión, usuario y espacio de trabajo. Desde el día uno.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">Olvidar se diseña</div>
            <div class="d">No es una limitación que se sufre.</div></div>
        </div>""",
    },

]


NOTES = [
    {
        "lead": "Módulo 8 · Contexto y memoria.",
        "rows": [
            ("2", "Encuadra la sesión como consecuencia de lo anterior, no como "
                  "tema nuevo. La pregunta ya está sobre la mesa desde la sesión "
                  "pasada."),
            ("7", "<b>Comparte la incomodidad con los términos en vez de "
                  "ocultarla.</b> Que el material reconozca que un vocabulario es "
                  "flojo genera más confianza que fingir que es preciso."),
            ("9", "Di explícitamente que no está resuelto. Es cierto, y evita que "
                  "alguien salga buscando la técnica canónica que no existe."),
            ("12", "Recorre las cuatro estrategias preguntando cuál usan hoy. Casi "
                   "siempre es la primera, y casi nunca eligieron: se quedó así."),
            ("13", "El detalle del truncado por el principio es de los que ahorran "
                   "dinero de verdad y casi nadie conoce. Merece su minuto."),
            ("15", "<b>El triple costo es el cierre argumental del módulo.</b> Que "
                   "los tres se paguen a la vez es lo que convierte «cuida el "
                   "contexto» en una decisión de ingeniería."),
            ("18", "Insiste en los identificadores. Añadirlos después obliga a "
                   "migrar todo lo guardado, y siempre se descubre tarde."),
        ],
    },
]
