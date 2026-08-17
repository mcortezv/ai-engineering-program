# -*- coding: utf-8 -*-
"""Deck: Módulo 20 — Fine tuning en detalle.

Cierra el arco que abrió la escalera de adaptación: aquí va todo el detalle
técnico y económico que aquella sesión aplazó a propósito.
"""

from engine.diagrams import mod20 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 20 · Fine tuning en detalle",
    "footer": "Programa de AI · Módulo 20",
    "outfile": "Modulo 20 - Fine tuning en detalle.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 20  ·  2 HORAS",
        "title": "Fine tuning en detalle",
        "tagline": "El programa termina donde mucha gente quería empezar.",
        "meta": [
            "<b>Antes de esta sesión:</b> los cuatro escalones anteriores, y saber "
            "medir",
            "<b>Al terminar:</b> emites una recomendación justificada, incluso si es "
            "negativa",
        ],
    },

    {
        "kind": "statement",
        "text": "El problema no es que ajustar un modelo sea difícil: es que <em>casi "
                "nunca resuelve el problema</em> que la gente cree que resuelve.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>La pregunta que decide</b> — ¿no sabe, o no puede?</li>
          <li><b>Qué sí y qué no arregla</b> — y el efecto perverso de forzarlo.</li>
          <li><b>Cómo se hace hoy</b> — ajuste completo, métodos eficientes y
            destilación.</li>
          <li><b>El dataset es el proyecto</b> — cantidad, calidad y distribución.</li>
          <li><b>Cómo saber si funcionó</b> — la línea base obligatoria.</li>
          <li><b>El costo completo</b> — incluido el que nadie presupuesta.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "La pregunta que decide",
        "note": "Una sola pregunta resuelve la elección sin ambigüedad.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "El criterio",
        "title": "¿No sabe, o no puede?",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>No sabe</h3>
            <p>Le falta la información: tus precios, tus documentos, lo que pasó
            ayer.</p>
            <p>La solución es contexto, recuperación o herramientas.</p>
            <p><b>Ajustar los pesos no aplica</b>, y forzarlo puede empeorar las
            cosas.</p>
          </div>
          <div class="col accent">
            <h3>No puede</h3>
            <p>Tiene toda la información delante y aun así no produce el formato, no
            sostiene el tono, o falla de forma consistente en un criterio propio.</p>
            <p><b>Aquí entra en la conversación</b>, después de haber agotado el
            prompt.</p>
          </div>
        </div>
        <div class="box ok" style="margin-top:7mm">
          <p class="lab">La prueba diagnóstica, que es trivial</p>
          <p>Pega la información directamente en el prompt. <b>Si con eso acierta, tu
          problema era de contexto</b> y acabas de ahorrarte tres semanas.</p>
        </div>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "Qué sí y qué no",
        "note": "Y el efecto contraintuitivo de intentar lo segundo.",
    },

    {
        "kind": "content", "covers": [2, 3],
        "eyebrow": "Los dos lados",
        "title": "Qué arregla y qué no",
        "html": dg.si_y_no(),
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "El caso con el mejor argumento económico",
        "title": "Reducir tokens de prompt se paga solo con aritmética",
        "html": """
        <ul class="pts">
          <li><b>Si tu prompt tiene cuatro mil tokens de instrucciones y veinte
            ejemplos, y haces un millón de llamadas al mes…</b>
            <span class="n">…mover eso a los pesos y quedarte con doscientos tokens es
            un ahorro enorme, y además baja la latencia.</span></li>
          <li><b>Es muy distinto de «quiero que sepa de mi empresa».</b>
            <span class="n">Aquí no estás intentando añadir conocimiento: estás
            comprimiendo instrucciones que ya funcionan.</span></li>
        </ul>
        <div class="box warn" style="margin-top:7mm">
          <p class="lab">Un matiz honesto</p>
          <p>El caché de prompts se come buena parte de este argumento: si el prefijo
          es estable, esos cuatro mil tokens ya se cobran a una fracción del precio.
          <b>Haz la cuenta con caché antes de decidir.</b></p>
        </div>""",
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "El punto contraintuitivo",
        "title": "Entrenar con conocimiento puede aumentar las invenciones",
        "html": dg.efecto_perverso(),
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Cómo se hace hoy",
        "note": "Dos formas de ajustar, y el camino que más se usa en la práctica.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Completo o eficiente",
        "title": "Las dos formas, comparadas",
        "html": dg.lora_vs_completo(),
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "El camino más práctico",
        "title": "Destilación",
        "html": dg.destilacion(),
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "El dataset es el proyecto",
        "note": "El entrenamiento es la parte fácil, y también la más barata.",
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "Cuatro cosas que decidir",
        "title": "Cantidad, calidad, distribución y conjunto de prueba",
        "html": """
        <ul class="pts">
          <li><b>Cantidad.</b>
            <span class="n">Para métodos eficientes en una tarea estrecha, del orden
            de cientos a unos pocos miles de ejemplos de calidad. Es un orden de
            magnitud a calibrar, no una cifra.</span></li>
          <li><b>Calidad sobre cantidad.</b>
            <span class="n">Trescientos ejemplos curados superan a diez mil sucios, y
            no por poco.</span></li>
          <li><b>Distribución.</b>
            <span class="n">Los ejemplos tienen que parecerse a lo que verás en
            producción, incluidos los casos raros. Un conjunto solo de casos fáciles
            produce un modelo que falla justo donde importa.</span></li>
          <li><b>Conjunto de prueba apartado desde el principio.</b>
            <span class="n">Nunca visto durante el entrenamiento. Sin esto no hay
            proyecto: hay una impresión.</span></li>
        </ul>
        <div class="box" style="margin-top:6mm">
          <p><b>De dónde salen los datos:</b> registros de producción, generación
          sintética con filtrado, y anotación humana. Casi siempre una mezcla.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "El paso que más proyectos se saltan",
        "title": "La línea base obligatoria",
        "html": """
        <div class="box big">
          <p>Antes de comparar nada, mide <b>el mismo modelo sin ajustar, pero bien
          prompteado</b>, sobre el conjunto de prueba apartado.</p>
        </div>
        <ul class="pts" style="margin-top:7mm">
          <li><b>Con una frecuencia incómoda, la línea base gana.</b>
            <span class="n">Y descubrirlo antes de invertir tres semanas es
            exactamente el valor de esta sesión.</span></li>
          <li><b>Y hacen falta pruebas de regresión.</b>
            <span class="n">Verificar que el ajuste no rompió lo que antes
            funcionaba. Un modelo que mejora la tarea nueva y empeora las tres
            anteriores no es una mejora.</span></li>
        </ul>""",
    },

    # ── 05 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "05",
        "title": "El costo completo",
        "note": "Incluido el que nadie presupuesta.",
    },

    {
        "kind": "content", "covers": [8],
        "eyebrow": "Dónde se va el esfuerzo",
        "title": "El entrenamiento es lo más barato del proyecto",
        "html": dg.costo_completo(),
    },

    {
        "kind": "content", "covers": [9],
        "eyebrow": "Antes de decidir",
        "title": "Cuatro alternativas que suelen ganarle",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div>
            <div class="t">Prompt con ejemplos, más caché</div>
            <div class="d">Elimina buena parte del argumento de ahorrar tokens, y no
            hay nada que mantener.</div></div>
          <div class="card"><div class="k">02</div>
            <div class="t">Recuperación con reordenamiento</div>
            <div class="d">Si el problema era de conocimiento, esto lo resuelve y
            además se actualiza solo.</div></div>
          <div class="card"><div class="k">03</div>
            <div class="t">Un modelo más nuevo</div>
            <div class="d">Y más barato que el que estabas usando. Sale uno cada pocos
            meses.</div></div>
          <div class="card"><div class="k">04</div>
            <div class="t">Enrutamiento</div>
            <div class="d">Modelo pequeño para lo fácil, grande para lo difícil. Sin
            entrenar nada.</div></div>
        </div>
        <div class="box warn" style="margin-top:7mm">
          <p>Hay bastantes equipos que ajustaron un modelo para igualar la calidad de
          uno grande, y seis meses después <b>el modelo pequeño de nueva generación
          del mismo proveedor ya lo superaba de fábrica</b>, con un prompt y sin
          mantener nada.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [10],
        "eyebrow": "Cierre del módulo",
        "title": "Cinco preguntas antes de empezar",
        "html": dg.checklist(),
    },

    {
        "kind": "statement",
        "text": "Terminamos donde mucha gente quería <em>empezar</em>.",
        "after": "Y la diferencia es que ahora puedes justificar por qué empezar aquí "
                 "habría sido un error, o por qué en tu caso concreto sí tiene "
                 "sentido. Ese criterio es todo el programa.",
    },
]


NOTES = [
    {
        "lead": "Módulo 20 · Fine tuning en detalle. Cierra el programa.",
        "rows": [
            ("2", "Dilo sin suavizarlo. El módulo entero existe para romper ese "
                  "reflejo, y ya se sembró en la sesión de la escalera."),
            ("6", "<b>La pregunta y la prueba diagnóstica son lo que hay que "
                  "memorizar.</b> Hazlas repetir en voz alta."),
            ("8", "El caso de reducir tokens de prompt es el único con argumento "
                  "económico sólido. Y da el matiz del caché: es honesto y evita una "
                  "decisión mal fundada."),
            ("10", "<b>El efecto perverso es el punto más valioso de la sesión.</b> "
                   "Recorre el diagrama paso por paso: no aprende los hechos, "
                   "aprende el patrón de responder con seguridad."),
            ("13", "De LoRA basta la idea: congelas el modelo y entrenas unas "
                   "matrices que se suman. Nada de matemática."),
            ("14", "Menciona los términos de servicio. Es un riesgo legal real y "
                   "casi nadie lo comprueba."),
            ("17", "La línea base es el paso que más proyectos se saltan y el que más "
                   "los salva. Insiste en que a menudo gana."),
            ("19", "El costo oculto —el modelo base va a cambiar— es lo que convierte "
                   "esto de proyecto en compromiso de mantenimiento."),
            ("22", "Cierra el programa con la frase. Han recorrido cuarenta y cuatro "
                   "horas para poder tomar esta decisión con criterio."),
        ],
    },
]
