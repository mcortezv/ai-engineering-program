# -*- coding: utf-8 -*-
"""Deck: Módulo 17 — Buenas prácticas."""

from engine.diagrams import mod17 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 17 · Buenas prácticas",
    "footer": "Programa de AI · Módulo 17",
    "outfile": "Modulo 17 - Buenas practicas.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 17  ·  1.5 HORAS",
        "title": "Buenas prácticas",
        "tagline": "El equivalente al código limpio, pero para sistemas de AI.",
        "meta": [
            "<b>Antes de esta sesión:</b> memoria, costos, orquestación y trazas",
            "<b>Al terminar:</b> puedes auditar una arquitectura ajena con criterio",
        ],
    },

    {
        "kind": "statement",
        "text": "Ninguna de estas prácticas es una regla absoluta: todas son "
                "<em>criterios que resuelven una tensión concreta</em>.",
        "after": "Y como toda buena práctica, tienen excepciones que hay que saber "
                 "reconocer. Aquí no se introduce nada nuevo: se consolida en "
                 "criterios lo que ya se demostró.",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Las ocho prácticas",
        "note": "Cada una con el hecho que la sostiene, no con una autoridad.",
    },

    {
        "kind": "content", "covers": [1, 2, 3, 5, 6, 7, 8],
        "eyebrow": "El cuadro completo",
        "title": "Qué hacer, y por qué",
        "html": dg.practicas(),
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "La primera, desarrollada",
        "title": "No todo va en las instrucciones fijas",
        "html": """
        <ul class="pts">
          <li><b>Se paga en cada petición, para siempre.</b>
            <span class="n">Un bloque de instrucciones que creció por acumulación
            durante seis meses se multiplica por el número de llamadas del
            producto.</span></li>
          <li><b>Y compite por la atención con lo que sí importaba.</b>
            <span class="n">Cuarenta reglas de las cuales dos aplican a esta tarea
            hacen que esas dos pesen menos.</span></li>
          <li><b>El síntoma:</b> nadie se atreve a borrar una línea por si acaso.
            <span class="n">Cuando ya no sabes qué hace cada párrafo del prompt, el
            prompt dejó de ser mantenible.</span></li>
        </ul>
        <div class="box" style="margin-top:7mm">
          <p><b>La salida es dividir por dominio y cargar por demanda:</b> lo estable y
          transversal arriba, lo específico de la tarea cuando la tarea llega.</p>
        </div>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "La que más se incumple",
        "note": "Y la que más dinero cuesta ignorar.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Seis casos que no necesitan al modelo",
        "title": "Si se puede resolver por código, se resuelve por código",
        "html": dg.por_codigo(),
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Por qué se incumple tanto",
        "title": "El modelo hace de todo, y eso es la trampa",
        "html": """
        <ul class="pts">
          <li><b>Funciona a la primera, y eso convence.</b>
            <span class="n">Pedirle al modelo que ordene una lista funciona en la
            demo. Con volumen sale caro, lento, y a veces devuelve la lista
            incompleta.</span></li>
          <li><b>Escribir la regla parece más trabajo.</b>
            <span class="n">Y lo es, la primera vez. Después es determinista, gratis y
            no hay que volver a mirarla.</span></li>
          <li><b>Nadie mide la alternativa.</b>
            <span class="n">Se compara el prompt con otro prompt, nunca con la versión
            sin modelo.</span></li>
        </ul>
        <div class="box big" style="margin-top:7mm">
          <p>Reserva el modelo para lo que requiere <b>juicio sobre lenguaje natural
          ambiguo</b>. Todo lo demás tiene una solución más barata y más
          confiable.</p>
        </div>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Una arquitectura limpia",
        "note": "Las prácticas aplicadas a un flujo real, de principio a fin.",
    },

    {
        "kind": "content", "covers": [9],
        "eyebrow": "El ejemplo integrador",
        "title": "Cómo se ve cuando está bien puesto",
        "html": dg.arquitectura_limpia(),
    },

    {
        "kind": "content", "covers": [9],
        "eyebrow": "Cómo se lee ese diagrama",
        "title": "Qué justifica cada pieza",
        "html": """
        <ul class="pts tight">
          <li><b>La validación y el enrutamiento van por código</b> porque la entrada
            es estructurada y las categorías son fijas.</li>
          <li><b>La recuperación es condicional</b>: no se paga contexto en las
            peticiones que no lo necesitan.</li>
          <li><b>Hay dos modelos</b> porque tres de los cuatro pasos son mecánicos y
            uno requiere juicio.</li>
          <li><b>La salida se valida por código</b> antes de actuar, porque un formato
            correcto no dice nada del contenido.</li>
          <li><b>La traza sale de forma asíncrona</b> para no meter latencia en el
            camino del usuario.</li>
          <li><b>Y hay cuatro invariantes</b> que aplican en todo el flujo: prefijo
            estable, historial acotado, límite de iteraciones y presupuesto por
            sesión.</li>
        </ul>""",
    },

    {
        "kind": "statement",
        "text": "Si puedes señalar qué práctica justifica cada línea de un diagrama, "
                "sabes <em>auditar</em> una arquitectura.",
        "after": "Y eso es más útil que saber construir una, porque casi siempre vas a "
                 "llegar a sistemas que ya existen.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Todas tienen un porqué</div>
            <div class="d">Ninguna es una regla por autoridad.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Y todas tienen excepción</div>
            <div class="d">Reconocer un incumplimiento justificado es parte del
            criterio.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Por código si se puede</div>
            <div class="d">La que más se incumple y la que más cuesta.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Bajo demanda</div>
            <div class="d">Lo específico entra cuando la tarea llega.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Un modelo por tarea</div>
            <div class="d">No todo pasa por el más caro.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Valida la salida</div>
            <div class="d">La forma correcta no garantiza el contenido.</div></div>
          <div class="card"><div class="k">07</div><div class="t">Cuatro invariantes</div>
            <div class="d">Prefijo, historial, iteraciones, presupuesto.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">Saber auditar</div>
            <div class="d">Vale más que saber construir de cero.</div></div>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 17 · Buenas prácticas. Sesión de síntesis: no hay conceptos "
                "nuevos y conviene decirlo.",
        "rows": [
            ("2", "Enmárcalo como consolidación. Si suena a lista de consejos, pierde "
                  "la fuerza que le da venir de lo ya demostrado."),
            ("5", "Recorre el cuadro leyendo la columna derecha, no la izquierda. El "
                  "porqué es lo que hace que la práctica se recuerde."),
            ("9", "<b>Es la que más dinero mueve y la que más se incumple.</b> Pide "
                  "ejemplos de su propio código: siempre sale alguno donde el modelo "
                  "está haciendo trabajo de una expresión regular."),
            ("12", "<b>Dedica la última media hora a este diagrama con un caso real de "
                   "la empresa.</b> Dibújalo en el pizarrón y pide que señalen qué "
                   "práctica justifica cada pieza."),
            ("14", "Si pueden auditar el diagrama señalando el porqué de cada línea, "
                   "el programa está cumpliendo su función."),
        ],
    },
]
