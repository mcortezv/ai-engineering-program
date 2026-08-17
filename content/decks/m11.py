# -*- coding: utf-8 -*-
"""Deck: Módulo 11 — Bases de datos para sistemas de AI."""

from engine.diagrams import mod11 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 11 · Bases de datos",
    "footer": "Programa de AI · Módulo 11",
    "outfile": "Modulo 11 - Bases de datos.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 11  ·  2 HORAS",
        "title": "Bases de datos",
        "tagline": "Por qué recuperar contexto con las herramientas de siempre es "
                   "difícil, y qué aparece cuando dejan de alcanzar.",
        "meta": [
            "<b>Antes de esta sesión:</b> cómo se diseña la memoria de un sistema",
            "<b>Al terminar:</b> eliges dónde guardar cada cosa y por qué",
        ],
    },

    {
        "kind": "statement",
        "text": "En una base relacional buscas lo que <em>se escribe parecido</em>. "
                "El contexto de un sistema de AI hay que buscarlo por lo que "
                "<em>significa</em>.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Recuperación por coincidencia</b> — qué hace bien y dónde se
            rompe.</li>
          <li><b>Aislar los datos</b> — sesión, usuario y cliente.</li>
          <li><b>Índices</b> — qué aceleran, y qué no arreglan por mucho que
            aceleren.</li>
          <li><b>Grafos</b> — cuando lo que importa son las relaciones.</li>
          <li><b>Vectorial</b> — la puerta a buscar por significado.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Dónde se rompe lo que ya sabemos hacer",
        "note": "Empecemos por lo que la base relacional hace insuperablemente bien, "
                "y por el caso donde no sirve.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Un caso concreto",
        "title": "La consulta y la respuesta no comparten ni una palabra",
        "html": dg.lexico_falla(),
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Antes de seguir",
        "title": "Lo que la base relacional hace insuperablemente bien",
        "html": """
        <ul class="pts">
          <li><b>Recuperar el pedido 4821.</b>
            <span class="n">Rápida, exacta, transaccional y barata. Nada de lo que
            veremos hoy la mejora en eso, ni de lejos.</span></li>
          <li><b>Contar, sumar y agrupar.</b>
            <span class="n">«¿Cuántos clientes tenemos en Jalisco?» es una consulta,
            no una búsqueda por significado.</span></li>
          <li><b>Garantizar consistencia.</b>
            <span class="n">Si dos procesos tocan el mismo registro, la base
            relacional resuelve algo que ninguna de las alternativas resuelve
            igual de bien.</span></li>
        </ul>
        <div class="box" style="margin-top:7mm">
          <p>Lo que sigue no la sustituye. Aparece porque hay <b>un tipo de pregunta
          distinto</b> que ella no responde bien.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [3, 4],
        "eyebrow": "Un malentendido frecuente",
        "title": "Un índice no arregla esto",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Lo que sí hace un índice</h3>
            <p>Acelerar la búsqueda por un valor conocido.</p>
            <p>Convertir un recorrido de un millón de filas en un salto directo.</p>
          </div>
          <div class="col">
            <h3>Lo que no hace</h3>
            <p>No hace que la búsqueda entienda sinónimos.</p>
            <p>No encuentra un párrafo que dice lo mismo con otras palabras.</p>
            <p>No sabe que «devolver» y «reembolso» están relacionados.</p>
          </div>
        </div>
        <div class="box big" style="margin-top:7mm">
          <p>El problema de recuperar contexto <b>no es de velocidad: es de criterio
          de coincidencia</b>. Por eso ningún índice tradicional lo resuelve.</p>
        </div>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "Aislar los datos",
        "note": "Antes de recuperar bien hay que saber a quién pertenece cada cosa.",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Tres niveles",
        "title": "Qué pertenece a quién",
        "html": dg.aislamiento(),
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Otras formas de almacenar",
        "note": "Dos herramientas que resuelven preguntas que la relacional no.",
    },

    {
        "kind": "content", "covers": [5, 6, 7],
        "eyebrow": "Tres preguntas distintas",
        "title": "Cada tipo responde bien a una cosa",
        "html": dg.tipos_db(),
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "Cuándo aparece un grafo",
        "title": "Cuando la respuesta depende de las conexiones",
        "html": """
        <ul class="pts">
          <li><b>Almacena entidades como nodos y relaciones como aristas.</b>
            <span class="n">Su fortaleza es recorrer esas relaciones: «qué está
            conectado con qué, y a cuántos saltos».</span></li>
          <li><b>Aparece cuando el contexto relevante se define por pertenencia.</b>
            <span class="n">Este tema, esta área, este proyecto. O cuando la
            respuesta exigiría reconstruir relaciones con muchos joins.</span></li>
          <li><b>Y tiene una ventaja poco mencionada: el camino es legible.</b>
            <span class="n">Puedes explicar por qué recuperó lo que recuperó, cosa
            que la búsqueda por significado no ofrece con la misma
            facilidad.</span></li>
          <li><b>Su límite llega con el volumen.</b>
            <span class="n">Los nodos crecen, el contenido por nodo crece, y saber
            en qué nodo buscar vuelve a ser el problema original.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "La puerta que abre lo siguiente",
        "title": "Si el significado fuera un número, buscarlo sería fácil",
        "html": """
        <div class="box big">
          <p>Existe una forma de representar un texto como una lista de números tal
          que <b>textos con significado parecido producen listas de números
          parecidas</b>.</p>
        </div>
        <ul class="pts" style="margin-top:7mm">
          <li><b>Si eso es posible, buscar por significado se convierte en buscar
            números cercanos.</b>
            <span class="n">Y ese sí es un problema que sabemos resolver rápido,
            incluso con millones de elementos.</span></li>
          <li><b>Esa es toda la idea de una base vectorial.</b>
            <span class="n">Guardar esas listas de números y encontrar las más
            cercanas a una consulta, muy deprisa.</span></li>
        </ul>
        <div class="box" style="margin-top:6mm">
          <p><b>Cómo se producen esos números</b> es el tema de la sesión siguiente,
          y es el que hace que todo lo demás deje de parecer magia. Aquí basta con
          saber que se puede.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">La coincidencia de texto falla</div>
            <div class="d">La pregunta y la respuesta pueden no compartir ni una
            palabra.</div></div>
          <div class="card"><div class="k">02</div><div class="t">No es velocidad, es criterio</div>
            <div class="d">Por eso un índice no lo arregla.</div></div>
          <div class="card"><div class="k">03</div><div class="t">La relacional sigue ganando</div>
            <div class="d">Para identificadores, conteos y consistencia.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Aísla desde el día uno</div>
            <div class="d">Sesión, usuario y cliente. Después duele.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Grafos para relaciones</div>
            <div class="d">Y con la ventaja de que el camino se puede
            explicar.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Vectorial para significado</div>
            <div class="d">Buscar lo que se parece, no lo que se escribe
            igual.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">Conviven</div>
            <div class="d">No es una evolución. Elegir una para todo es el
            error.</div></div>
        </div>""",
    },

]


NOTES = [
    {
        "lead": "Módulo 11 · Bases de datos.",
        "rows": [
            ("5", "<b>El ejemplo de «cómo devuelvo un producto» contra «política de "
                  "reembolsos» funciona muy bien porque es real.</b> Pide otros a la "
                  "sala: cada equipo tiene los suyos y salen enseguida."),
            ("6", "Reconoce lo que la relacional hace mejor antes de criticarla. Si "
                  "no, la escalera suena a desprecio y la gente se pone a la "
                  "defensiva."),
            ("7", "El punto sobre los índices es el que más veces hay que repetir. "
                  "La intuición de un desarrollador es que todo problema de "
                  "búsqueda se arregla indexando."),
            ("12", "<b>Contén la explicación aquí.</b> La pregunta de cómo se "
                   "producen esos números va a surgir; di que la sesión siguiente "
                   "se dedica entera a eso. Explicarlo ahora, a medias, es lo que "
                   "hace que la base vectorial se perciba como magia."),
        ],
    },
]
