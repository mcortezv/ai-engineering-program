# -*- coding: utf-8 -*-
"""Deck: Módulo 1 — Introducción."""

from engine.diagrams import mod01 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 1 · Introducción",
    "footer": "Programa de AI · Módulo 1",
    "outfile": "Modulo 01 - Introduccion.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 1  ·  1.5 HORAS",
        "title": "Introducción",
        "tagline": "Dónde encaja la AI entre todas las formas que ya conocemos de "
                   "resolver un problema con código.",
        "meta": [
            "<b>Primera sesión del programa.</b> No requiere nada previo.",
            "<b>Al terminar:</b> sabes cuándo un problema pide AI y cuándo no",
        ],
    },

    {
        "kind": "statement",
        "text": "La AI no es una tecnología aparte. Es el tercer punto de una escala "
                "que ya recorres <em>todos los días</em> al programar.",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Qué es la inteligencia artificial</b> — y qué se ha vuelto la
            palabra en el uso comercial.</li>
          <li><b>Tres formas de resolver un problema</b> — determinista, heurística
            y aprendizaje automático, con el mismo problema resuelto tres
            veces.</li>
          <li><b>Tradicional frente a generativa</b> — la diferencia está en el tipo
            de salida, y las dos conviven.</li>
          <li><b>Supervisado y no supervisado</b> — en una frase cada uno.</li>
          <li><b>El mapa del programa</b> — qué vamos a construir y en qué orden.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "01",
        "title": "Qué es la inteligencia artificial",
        "note": "Empecemos por delimitar la palabra, porque en el uso comercial ha "
                "dejado de significar algo concreto.",
    },

    {
        "kind": "content",
        "covers": [1],
        "eyebrow": "Delimitar el término",
        "title": "Una palabra que en marketing ya no distingue nada",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Qué es, con precisión</h3>
            <p>El conjunto de técnicas que permiten a un programa <b>resolver
            tareas que normalmente requerirían juicio humano</b>: reconocer,
            clasificar, predecir, generar.</p>
            <p>La familia es antigua y muy amplia. Los modelos de lenguaje son
            una rama reciente de ella, no su totalidad.</p>
          </div>
          <div class="col">
            <h3>Qué se le llama hoy</h3>
            <p>Casi cualquier cosa. Un filtro de fotos, una regla de negocio con
            tres condiciones, una consulta ordenada por relevancia.</p>
            <p>Cuando un proveedor dice «con AI», <b>no te ha dicho nada</b>
            todavía. La pregunta útil es qué técnica hay debajo.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p><b>El criterio que usaremos en todo el programa:</b> no importa cómo se
          llame. Importa si el sistema sigue una regla que alguien escribió, o una
          que encontró él solo a partir de ejemplos.</p>
        </div>""",
    },

    {
        "kind": "content",
        "covers": [1],
        "eyebrow": "Un poco de perspectiva",
        "title": "No es nueva: lo nuevo es que funciona",
        "html": """
        <ul class="pts">
          <li><b>El término tiene setenta años.</b>
            <span class="n">Se acuñó en los años cincuenta, y desde entonces el
            campo ha pasado por varios ciclos de entusiasmo y decepción.</span></li>
          <li><b>Lo que cambió no fue la idea, fueron tres cosas materiales.</b>
            <span class="n">Muchísimos más datos disponibles, hardware capaz de
            procesarlos en paralelo, y arquitecturas que aprovechan bien ese
            hardware.</span></li>
          <li><b>Por eso conviene desconfiar de las dos posturas extremas.</b>
            <span class="n">Ni magia inminente ni humo pasajero. Es una herramienta
            con capacidades concretas y limitaciones concretas, y este programa va
            sobre distinguir unas de otras.</span></li>
        </ul>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "02",
        "title": "Tres formas de resolver un problema",
        "note": "El mismo problema, resuelto tres veces. La diferencia está en "
                "cuánto sabes de él antes de empezar.",
    },

    {
        "kind": "content",
        "covers": [3],
        "eyebrow": "La escala completa",
        "title": "Cuánto sabes, cuánto delegas",
        "html": dg.tres_formas(),
    },

    {
        "kind": "content",
        "covers": [3],
        "eyebrow": "El caso más claro",
        "title": "Celsius a Fahrenheit no necesita una red neuronal",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>Lo que sabes</h3>
            <p>Conoces la entrada, conoces la salida y existe una operación exacta
            que las relaciona.</p>
            <p>Puedes verificar el resultado sin ejecutar nada: la fórmula es la
            demostración.</p>
          </div>
          <div class="col accent">
            <h3>Por qué importa decirlo</h3>
            <p>Escribir un modelo para esto sería absurdo, y todo el mundo lo ve.</p>
            <p>Pero el mismo error se comete todos los días con problemas
            ligeramente menos obvios.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p><b>La pregunta que hay que hacerse siempre:</b> ¿existe una regla que yo
          pueda escribir? Si existe, escríbela. Sale más barata, más rápida y más
          fácil de depurar.</p>
        </div>""",
    },

    {
        "kind": "statement",
        "text": "Lo que se delega en el tercer caso no es el cálculo: es el "
                "<em>diseño de la regla</em>.",
        "after": "Ese es el intercambio central de todo el campo. Se gana la capacidad "
                 "de resolver problemas cuya regla nadie sabe escribir, y se pierde "
                 "poder leer por qué el sistema decidió lo que decidió.",
    },

    {
        "kind": "content",
        "covers": [3],
        "eyebrow": "El precio del intercambio",
        "title": "Lo que ganas y lo que pierdes al delegar",
        "html": """
        <div class="grid c3">
          <div class="card"><div class="k">GANAS</div>
            <div class="t">Problemas sin regla escribible</div>
            <div class="d">Reconocer una cara, entender una frase ambigua, valorar
            una casa con veinte variables que interactúan.</div></div>
          <div class="card"><div class="k">GANAS</div>
            <div class="t">Que mejore con más datos</div>
            <div class="d">Una heurística se queda como la escribiste. Un modelo
            entrenado con más ejemplos puede acertar más.</div></div>
          <div class="card no"><div class="k">PIERDES</div>
            <div class="t">Poder leer la decisión</div>
            <div class="d">La regla existe, pero está codificada en números.
            No hay una línea de código que señalar cuando falla.</div></div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>Todo lo que veremos después sobre validar salidas, medir resultados y
          proteger el sistema existe <b>porque se hizo este intercambio</b>.</p>
        </div>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "03",
        "title": "Tradicional y generativa",
        "note": "La diferencia práctica está en el tipo de salida, no en la época.",
    },

    {
        "kind": "content",
        "covers": [2],
        "eyebrow": "Dos tipos de salida",
        "title": "Elegir entre opciones, o construir algo nuevo",
        "html": dg.tradicional_generativa(),
    },

    {
        "kind": "content",
        "covers": [4],
        "eyebrow": "Supervisado y no supervisado",
        "title": "Con etiquetas o sin ellas",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Aprendizaje supervisado</h3>
            <p>Le muestras ejemplos <b>ya resueltos</b>: cien mil correos marcados
            como spam o no spam.</p>
            <p>El sistema busca qué distingue unos de otros.</p>
            <p>Necesitas los datos etiquetados, y etiquetarlos cuesta.</p>
          </div>
          <div class="col">
            <h3>Aprendizaje no supervisado</h3>
            <p>Le muestras los datos <b>sin resolver</b> y le pides que encuentre
            estructura.</p>
            <p>Agrupar clientes parecidos sin decirle qué grupos existen.</p>
            <p>No necesitas etiquetas, pero tampoco sabes de antemano qué va a
            encontrar.</p>
          </div>
        </div>""",
    },

    {
        "kind": "content",
        "covers": [5],
        "eyebrow": "Una precisión de vocabulario",
        "title": "Redes convolucionales: qué son y por qué no van aquí",
        "html": """
        <ul class="pts">
          <li><b>Son la arquitectura que domina el procesamiento de imágenes.</b>
            <span class="n">Detectar objetos, clasificar fotografías, leer una placa.
            Siguen siendo el estándar en visión por computadora.</span></li>
          <li><b>Los modelos de lenguaje usan otra arquitectura distinta.</b>
            <span class="n">Se llama Transformer y su mecanismo central es la
            atención, no la convolución. Son cosas diferentes.</span></li>
          <li><b>Se menciona para que la palabra «AI» no se confunda con «modelo de
            lenguaje».</b>
            <span class="n">El campo es más grande que lo que vamos a ver, y este
            programa cubre una parte concreta de él.</span></li>
        </ul>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "04",
        "title": "El mapa",
        "note": "Qué vamos a construir, en qué orden y por qué ese orden.",
    },

    {
        "kind": "content",
        "covers": [6],
        "eyebrow": "Cinco partes, cuarenta y cuatro horas",
        "title": "Cada parte cierra una pregunta que la siguiente necesita resuelta",
        "html": """
        <table>
          <thead><tr><th style="width:26%">Parte</th><th style="width:50%">Pregunta que responde</th>
          <th>Horas</th></tr></thead>
          <tbody>
            <tr><td><b>I · Fundamentos</b></td>
              <td>¿Qué es y qué no es un modelo de lenguaje?</td><td>8</td></tr>
            <tr><td><b>II · Cómo se le habla</b></td>
              <td>¿Cómo consigo que haga lo que necesito?</td><td>6</td></tr>
            <tr><td><b>III · Construir</b></td>
              <td>¿Cómo le doy memoria, información y capacidad de actuar?</td><td>16</td></tr>
            <tr><td><b>IV · Operar</b></td>
              <td>¿Cómo lo hago pagable, observable y seguro?</td><td>10</td></tr>
            <tr><td><b>V · Más allá</b></td>
              <td>¿Qué hago cuando todo lo anterior se queda corto?</td><td>4</td></tr>
          </tbody>
        </table>
        <div class="box" style="margin-top:6mm">
          <p>Los temas que vas a echar de menos en las primeras sesiones —el costo,
          la seguridad, la memoria— <b>sí están</b>. Llegan cuando hay con qué
          entenderlos.</p>
        </div>""",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Tres formas, no una</div>
            <div class="d">Determinista, heurística y aprendizaje. Se eligen por lo
            que sabes del problema.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Delegas la regla</div>
            <div class="d">No el cálculo. Ese es el intercambio de fondo.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Pierdes explicabilidad</div>
            <div class="d">Y de ahí sale casi todo lo difícil de operar un sistema
            de AI.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Tradicional y generativa conviven</div>
            <div class="d">Lo barato filtra, lo caro solo donde hace falta.</div></div>
          <div class="card no"><div class="k">✓</div><div class="t">Si puedes escribir la regla, escríbela</div>
            <div class="d">Es el criterio que más dinero ahorra en todo el
            programa.</div></div>
        </div>""",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Ejercicio práctico",
        "title": "Clasifica tres funcionalidades reales",
        "html": """
        <ol class="pts">
          <li><b>En parejas, tomen tres funcionalidades de un producto de la
            empresa</b> y clasifiquen cada una como determinista, heurística o
            aprendizaje automático.</li>
          <li><b>Para cada una, escriban una frase justificando por qué NO
            corresponde a las otras dos categorías.</b>
            <span class="n">La justificación es el ejercicio. La clasificación
            sola no enseña nada.</span></li>
        </ol>
        <div class="box big" style="margin-top:7mm">
          <p>Casi siempre aparece alguna funcionalidad que hoy se resuelve con AI y
          que sería <b>más barata, más rápida y más confiable</b> como heurística.
          Encontrarla es el objetivo real del ejercicio.</p>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 1 · Introducción — la sesión de apertura del programa.",
        "rows": [
            ("2", "Es la frase que ordena la sesión. Dila antes de cualquier "
                  "definición: sitúa la AI dentro de algo que la sala ya hace, en "
                  "lugar de presentarla como territorio ajeno."),
            ("5", "<b>Resuelve el mismo problema tres veces en el pizarrón.</b> El "
                  "spam funciona muy bien porque las tres versiones son creíbles. "
                  "No pases al diagrama hasta que las tres estén escritas."),
            ("7", "El salto interesante es el tercero. Nómbralo explícitamente: lo "
                  "que se delega es el diseño de la regla. Si la sala se lleva una "
                  "sola frase de la sesión, que sea esta."),
            ("8", "Aquí se siembra la justificación de media Parte IV. No lo "
                  "desarrolles: basta con que quede la deuda planteada."),
            ("11", "Cinco minutos y seguir. La función de esta lámina es evitar que "
                   "alguien salga creyendo que «AI» y «modelo de lenguaje» son "
                   "sinónimos, no enseñar visión por computadora."),
            ("13", "Dedica los últimos quince minutos al mapa. Reduce mucho la "
                   "ansiedad de «¿y esto cómo se paga?» en la sesión tres."),
        ],
    },
]
