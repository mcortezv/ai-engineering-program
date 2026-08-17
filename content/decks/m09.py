# -*- coding: utf-8 -*-
"""Deck: Módulo 9 — Agentes.

El módulo está partido en dos mitades y el deck lo respeta: la primera no
menciona ni una marca; la segunda va marcada como volátil.
"""

from engine.diagrams import mod09 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 9 · Agentes",
    "footer": "Programa de AI · Módulo 9",
    "outfile": "Modulo 09 - Agentes.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 9  ·  3 HORAS",
        "title": "Agentes",
        "tagline": "Primero qué necesita un agente, que no cambia. Después con qué "
                   "se implementa hoy, que sí.",
        "meta": [
            "<b>Antes de esta sesión:</b> prompts, servicio sin estado y memoria",
            "<b>Al terminar:</b> decides si tu problema pide un agente o un flujo",
        ],
    },

    {
        "kind": "statement",
        "text": "«Un sistema que actúa de forma autónoma» no es una definición: "
                "es un <em>eslogan</em>.",
        "after": "Sirve para vender y no sirve para construir. Vamos a sustituirla "
                 "por una descomposición que además funciona como lista de "
                 "verificación de diseño.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Los siete componentes</b> — qué necesita un agente y qué falla si
            falta cada uno.</li>
          <li><b>El bucle</b> — y la condición de salida, que es parte de la
            definición.</li>
          <li><b>Qué no es un agente</b> — tres cosas que se llaman así y no lo
            son.</li>
          <li><b>Flujo o agente</b> — el criterio para decidir, que hoy casi nadie
            aplica.</li>
          <li><b>Cómo se implementa</b> — instrucciones fijas, herramientas,
            procedimientos y canales.</li>
        </ol>""",
    },

    # ══ 9.1 ══════════════════════════════════════════════════════════════
    {
        "kind": "section", "step": "PARTE 9.1",
        "title": "Qué necesita un agente",
        "note": "Esta mitad no menciona ni una marca. Es la que sigue siendo cierta "
                "dentro de tres años.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "La descomposición",
        "title": "Siete componentes, y el fallo que produce cada ausencia",
        "html": dg.siete_componentes(),
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "El ciclo",
        "title": "Cómo se encadenan, y cuándo se detiene",
        "html": dg.bucle_agente(),
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Delimitar es tan importante como definir",
        "title": "Tres cosas que se llaman agente y no lo son",
        "html": """
        <div class="grid c3">
          <div class="card no"><div class="k">NO ES</div>
            <div class="t">Un chat con instrucciones elaboradas</div>
            <div class="d">Tiene objetivo, pero no tiene herramientas, ni
            observación, ni bucle. Es un modelo con un texto fijo delante.</div></div>
          <div class="card no"><div class="k">NO ES</div>
            <div class="t">Una cadena fija de llamadas</div>
            <div class="d">Extraer, luego clasificar, luego redactar. Quien decide
            los pasos es el código, no el modelo. Y muchas veces es la solución
            correcta.</div></div>
          <div class="card no"><div class="k">NO ES</div>
            <div class="t">Una llamada con una herramienta disponible</div>
            <div class="d">Si puede invocar una función y responder, pero no hay
            iteración ni corrección, es uso de herramientas.</div></div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>Lo que convierte las tres en un agente es siempre lo mismo: <b>el
          bucle</b>. Que el resultado de una acción cambie la siguiente decisión.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "El criterio práctico",
        "title": "Cuándo conviene un agente y cuándo un flujo",
        "html": dg.flujo_vs_agente(),
    },

    {
        "kind": "statement",
        "text": "Muchas de las mejores arquitecturas son flujos deterministas con "
                "llamadas al modelo <em>solo donde hace falta juicio</em>.",
        "after": "El sesgo del momento empuja hacia el agente incluso donde "
                 "perjudica: más caro, menos predecible y mucho más difícil de "
                 "depurar.",
    },

    # ══ 9.2 ══════════════════════════════════════════════════════════════
    {
        "kind": "section", "step": "PARTE 9.2",
        "title": "Cómo se implementa hoy",
        "note": "Esta mitad describe productos concretos y va a cambiar. Conviene "
                "revisarla antes de cada impartición.",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "El objetivo se escribe",
        "title": "Las instrucciones fijas son el primer componente hecho texto",
        "html": """
        <ul class="pts">
          <li><b>Quién es, qué intenta lograr, qué puede y qué no puede hacer.</b>
            <span class="n">Es el mismo bloque estable de siempre, pero ahora carga
            con el objetivo del agente.</span></li>
          <li><b>Y tres cosas que solo aparecen cuando hay bucle:</b></li>
          <li><b>Las condiciones de terminación, explícitas.</b>
            <span class="n">Cómo sabe que ya acabó. Sin esto el agente sigue
            buscando mejoras hasta que algo lo pare desde fuera.</span></li>
          <li><b>Qué hacer cuando una herramienta falla.</b>
            <span class="n">Reintentar, probar otra vía o rendirse y reportar. Si no
            lo dices, improvisa.</span></li>
          <li><b>Qué acciones exigen confirmación.</b>
            <span class="n">Todo lo irreversible y todo lo que sale hacia
            fuera.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "El mecanismo real",
        "title": "Cómo se ejecuta una herramienta",
        "html": dg.uso_herramientas(),
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Dos observaciones que valen la sesión",
        "title": "Lo que se deduce de ese mecanismo",
        "html": """
        <ul class="pts">
          <li><b>La descripción de la herramienta es prompt engineering.</b>
            <span class="n">Es el único texto que el modelo lee para decidir si la
            usa y con qué argumentos. Una descripción ambigua produce llamadas
            erróneas, y el arreglo es reescribirla, no cambiar de modelo.</span></li>
          <li><b>Cada vuelta reenvía todo el contexto acumulado.</b>
            <span class="n">Diez pasos no cuestan diez veces uno: cuestan bastante
            más, porque en cada iteración el contexto ha crecido.</span></li>
          <li><b>Y por eso el límite de iteraciones no es una optimización.</b>
            <span class="n">Es lo que separa un agente de un proceso que gasta
            dinero sin techo.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Tres cosas que se confunden",
        "title": "Herramienta, procedimiento y canal",
        "html": dg.tool_skill_mcp(),
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Por qué existen los procedimientos cargables",
        "title": "Resuelven un problema de contexto, no de capacidad",
        "html": """
        <ul class="pts">
          <li><b>Meter todos los procedimientos de la empresa en las instrucciones
            fijas es caro y ruidoso.</b>
            <span class="n">Se pagan en cada petición y compiten por la atención
            con lo que sí importaba en esa tarea concreta.</span></li>
          <li><b>Cargarlos solo cuando la tarea los necesita cambia esa
            economía.</b>
            <span class="n">El contexto se mantiene pequeño en el caso común y
            crece solo cuando hace falta.</span></li>
          <li><b>Es el mismo patrón que vas a ver una y otra vez.</b>
            <span class="n">Traer la información en el momento en que se usa, en
            lugar de tenerla toda presente por si acaso.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Sobre el canal estandarizado",
        "title": "Por qué le importa a un agente",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>El problema</h3>
            <p>Sin un estándar, cada integración se escribe a mano para cada
            cliente de AI que la vaya a usar.</p>
            <p>Con uno, un servidor de capacidades sirve para todos los que hablen
            ese formato.</p>
          </div>
          <div class="col accent">
            <h3>Y una frontera de seguridad</h3>
            <p>El agente no toca la base de datos: le pide a un servidor que lo
            haga, y ese servidor decide qué está permitido.</p>
            <p>Las credenciales viven ahí, no en el contexto del modelo.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>Es un protocolo abierto, no una función de un proveedor. Lo veremos en
          detalle junto a los demás protocolos de comunicación, donde se entiende
          mejor por comparación.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Siete componentes</div>
            <div class="d">Objetivo, memoria, herramientas, planificación,
            observación, acción y reflexión.</div></div>
          <div class="card"><div class="k">02</div><div class="t">El bucle lo define</div>
            <div class="d">Que el resultado cambie la siguiente decisión.</div></div>
          <div class="card"><div class="k">03</div><div class="t">La salida es parte de la definición</div>
            <div class="d">Sin límite duro no es un agente.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Un flujo suele bastar</div>
            <div class="d">Y es más barato, predecible y depurable.</div></div>
          <div class="card"><div class="k">05</div><div class="t">El modelo no ejecuta</div>
            <div class="d">Pide. Tu código decide si obedece.</div></div>
          <div class="card"><div class="k">06</div><div class="t">La descripción es prompt</div>
            <div class="d">Si llama mal, reescríbela.</div></div>
          <div class="card"><div class="k">07</div><div class="t">Capacidad ≠ procedimiento ≠ canal</div>
            <div class="d">Tres cosas distintas que conviven.</div></div>
          <div class="card no"><div class="k">✓</div><div class="t">Lo de arriba dura</div>
            <div class="d">Lo de abajo caduca. Por eso van separados.</div></div>
        </div>""",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ejercicio práctico",
        "title": "Analizar uno y construir otro",
        "html": """
        <ol class="pts">
          <li><b>Analiza una herramienta de AI que uses a diario.</b>
            <span class="n">Documenta sus siete componentes con evidencia
            observable de cada uno. ¿Es un agente, un flujo o un híbrido? ¿Por
            qué?</span></li>
          <li><b>Construye un agente mínimo sin frameworks</b>, con tres
            herramientas: una de lectura, una de escritura y una de consulta
            externa.
            <span class="n">Obligatorio: límite duro de iteraciones, registro de
            cada llamada con argumentos y resultado, y confirmación explícita antes
            de cualquier acción irreversible.</span></li>
        </ol>
        <div class="box big" style="margin-top:6mm">
          <p>La entrega incluye la traza de una ejecución en la que el agente
          <b>falla y se recupera</b>. Si no falla nunca, el caso de prueba es
          demasiado fácil.</p>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 9 · Agentes — parte 9.1, conceptual.",
        "rows": [
            ("2", "Empieza por descartar la definición de eslogan. La sala llega con "
                  "ella y hay que sacarla del medio antes de construir."),
            ("6", "<b>Aplica la tabla a algo que conozcan.</b> Un agente de código "
                  "que usen a diario funciona muy bien: identifica los siete "
                  "componentes en voz alta con ellos."),
            ("7", "Dibuja el bucle y detente en la condición de salida. Es la parte "
                  "que casi nunca aparece en las definiciones y la que más "
                  "incidentes evita."),
            ("9", "<b>El criterio flujo/agente es el punto práctico del módulo.</b> "
                  "Es donde más dinero se pierde hoy por elegir por moda."),
        ],
    },
    {
        "lead": "Parte 9.2, implementación. Contenido con fecha de caducidad: "
                "revísalo contra la documentación antes de cada impartición y dilo "
                "en voz alta.",
        "rows": [
            ("12", "Avisa a la sala de que a partir de aquí lo que se cuenta va a "
                   "cambiar, y que lo anterior no. Esa advertencia es parte de la "
                   "lección."),
            ("14", "Desmitifica el mecanismo: el modelo no ejecuta nada. Es una "
                   "consecuencia directa de lo que ya saben y conviene que la "
                   "deduzcan antes de que la digas."),
            ("16", "La tabla de los tres conceptos resuelve una confusión muy "
                   "frecuente. Si solo se llevan una lámina de la segunda mitad, "
                   "que sea esta."),
            ("18", "Cierra abriendo el hilo del protocolo, sin desarrollarlo: la "
                   "sesión siguiente lo compara con los demás."),
        ],
    },
]
