# -*- coding: utf-8 -*-
"""Deck: Módulo 12 — Embeddings.

Es el módulo con lo más difícil de imaginar del programa. La estrategia es
subir de dimensión poco a poco: primero dos ejes que se dibujan, después tres,
y solo entonces el salto a las que no se ven.
"""

from engine.diagrams import mod12 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 12 · Embeddings",
    "footer": "Programa de AI · Módulo 12",
    "outfile": "Modulo 12 - Embeddings.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 12  ·  2.5 HORAS",
        "title": "Embeddings",
        "tagline": "Significado convertido en posición. Es la pieza que hace posible "
                   "buscar por lo que algo quiere decir.",
        "meta": [
            "<b>Antes de esta sesión:</b> por qué la coincidencia de texto no basta",
            "<b>Al terminar:</b> entiendes qué se guarda y qué se puede calcular "
            "con ello",
        ],
    },

    {
        "kind": "statement",
        "text": "Un embedding es <em>una posición</em>. Y la cercanía entre "
                "posiciones es parecido de significado.",
        "after": "Toda la sesión consiste en hacer creíble esa frase, empezando por "
                 "un espacio de dos ejes que sí se puede dibujar.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>La intuición en dos ejes</b> — donde todo se puede dibujar.</li>
          <li><b>El salto de dimensión</b> — de dos a tres, y de tres a mil
            quinientas.</li>
          <li><b>Cómo se produce</b> — el texto pasa por un modelo específico.</li>
          <li><b>Por qué no son intercambiables</b> — cada modelo define su propio
            espacio.</li>
          <li><b>Qué se puede calcular</b> — magnitud, distancia y ángulo.</li>
          <li><b>Por qué no se editan</b> — y qué obliga eso a construir.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "La intuición, en dos ejes",
        "note": "Empecemos donde todo se puede ver, y solo después subamos.",
    },

    {
        "kind": "content", "covers": [1, 3],
        "eyebrow": "Un espacio con dos ejes inventados",
        "title": "La posición codifica significado",
        "html": dg.plano_2d(),
    },

    {
        "kind": "content", "covers": [1, 3],
        "eyebrow": "Lo que hay que notar",
        "title": "Tres cosas que ya están en ese dibujo",
        "html": """
        <ul class="pts">
          <li><b>Palabras relacionadas caen juntas sin que nadie las agrupe.</b>
            <span class="n">No hay una etiqueta «animales» en ningún sitio: la
            cercanía sale de dónde quedó cada una.</span></li>
          <li><b>Lo ambiguo cae en medio, y eso es correcto.</b>
            <span class="n">«Ratón» está entre los dos grupos porque de verdad
            pertenece a los dos. La posición captura la ambigüedad en lugar de
            forzar una elección.</span></li>
          <li><b>La cercanía es lo que permite generalizar.</b>
            <span class="n">Lo que el sistema sabe de «perro» le sirve para «gato»
            sin habérselo visto, porque están al lado.</span></li>
        </ul>
        <div class="box" style="margin-top:7mm">
          <p>Un embedding real es exactamente esto, con dos diferencias: los ejes no
          son dos sino cientos o miles, y <b>nadie los eligió</b>. Salieron del
          entrenamiento y no tienen nombre.</p>
        </div>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "El salto de dimensión",
        "note": "La parte que cuesta imaginar, y que resulta que no hace falta "
                "imaginar.",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "De lo que se dibuja a lo que no",
        "title": "Dos, tres, y mil quinientas",
        "html": dg.subir_dimensiones(),
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "La ansiedad que hay que desactivar",
        "title": "No hace falta visualizarlo para operar con ello",
        "html": """
        <ul class="pts">
          <li><b>Nadie puede imaginar mil quinientas dimensiones, y da igual.</b>
            <span class="n">Las operaciones que vamos a usar —distancia, ángulo,
            magnitud— se calculan exactamente igual con dos ejes que con mil
            quinientos, y significan lo mismo.</span></li>
          <li><b>Nadie puede decir qué significa la dimensión 412.</b>
            <span class="n">Los ejes no son interpretables uno a uno. Lo que tiene
            sentido es el conjunto, y el conjunto ordena el significado con
            consistencia.</span></li>
          <li><b>Para un desarrollador, la representación es tranquilizadora.</b>
            <span class="n">Un arreglo de números decimales, siempre del mismo
            tamaño. Nada más exótico que eso.</span></li>
        </ul>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Cómo se produce",
        "note": "Un modelo distinto del que genera texto, entrenado para otra cosa.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "El proceso",
        "title": "Texto entra, vector sale",
        "html": dg.generar_embedding(),
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "Dos cosas distintas con el mismo nombre",
        "title": "El vector que se guarda y la representación interna",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>El vector que se almacena</h3>
            <p>Un vector por fragmento de texto, producido por un modelo
            <b>específico para esto</b>.</p>
            <p>Se guarda, se compara y se usa para buscar. Es de lo que va esta
            sesión.</p>
          </div>
          <div class="col">
            <h3>La representación interna</h3>
            <p>Cómo un modelo generativo representa cada token <b>durante su
            cómputo</b>.</p>
            <p>Es un paso intermedio: no se expone, no se guarda y no sirve para
            buscar.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>La idea de fondo —representar significado como posición— es la misma.
          <b>El propósito es distinto, y por eso los modelos son distintos.</b></p>
        </div>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "content", "covers": [5],
        "eyebrow": "Una consecuencia operativa fuerte",
        "title": "Cada modelo define su propio espacio",
        "html": dg.espacios_incompatibles(),
    },

    {
        "kind": "content", "covers": [5, 7],
        "eyebrow": "Cómo se elige",
        "title": "Cuatro ejes, y una decisión que cuesta revertir",
        "html": """
        <table>
          <thead><tr><th style="width:24%">Eje</th><th style="width:38%">Qué preguntar</th>
          <th>Por qué importa</th></tr></thead>
          <tbody>
            <tr><td><b>Dimensiones</b></td>
              <td>¿Cuántos números por vector?</td>
              <td>Más no es automáticamente mejor, y sí es más caro de almacenar y
                  de buscar.</td></tr>
            <tr><td><b>Idioma</b></td>
              <td>¿Con qué se entrenó?</td>
              <td>Un modelo entrenado sobre todo en inglés agrupa peor el
                  español.</td></tr>
            <tr><td><b>Longitud de entrada</b></td>
              <td>¿Cuánto texto acepta de una vez?</td>
              <td>Condiciona cómo tienes que trocear el contenido.</td></tr>
            <tr><td><b>Despliegue</b></td>
              <td>¿Servicio, o puedo ejecutarlo yo?</td>
              <td>Si el corpus no puede salir de casa, decide por ti.</td></tr>
          </tbody>
        </table>
        <div class="box" style="margin-top:6mm">
          <p><b>¿Y dónde se guardan?</b> En una base vectorial: junto a cada
          vector se almacena el texto del que salió, porque es ese texto —y no
          los números— lo que se acaba usando.</p>
        </div>
        <div class="box alerta" style="margin-top:6mm">
          <p class="lab">Presupuéstalo antes de elegir</p>
          <p>Cambiar de modelo no es cambiar una configuración: es <b>volver a
          generar todos los vectores del corpus</b>.</p>
        </div>""",
    },

    # ── 05 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "Qué se puede calcular",
        "note": "Al dejar de ser texto y pasar a ser números, el significado se "
                "vuelve operable.",
    },

    {
        "kind": "content", "covers": [8],
        "eyebrow": "Tres operaciones sobre los mismos dos vectores",
        "title": "Magnitud, distancia y ángulo",
        "html": dg.tres_operaciones(),
    },

    {
        "kind": "statement",
        "text": "Sobre texto no se puede calcular un parecido. Sobre vectores "
                "<em>sí</em>.",
        "after": "Esa es toda la ganancia. Las tres operaciones responden preguntas "
                 "distintas, y elegir cuál usar es la decisión de la sesión "
                 "siguiente.",
    },

    {
        "kind": "content", "covers": [9],
        "eyebrow": "Una limitación con consecuencias",
        "title": "Un embedding no se edita",
        "html": dg.no_editable(),
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Es una posición</div>
            <div class="d">Y la cercanía es parecido de significado.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Nadie eligió los ejes</div>
            <div class="d">Salieron del entrenamiento y no tienen nombre.</div></div>
          <div class="card"><div class="k">03</div><div class="t">No hace falta imaginarlo</div>
            <div class="d">Las operaciones son las mismas en 2 que en 1536.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Lo produce otro modelo</div>
            <div class="d">Distinto del generativo, y determinista.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Los espacios no se mezclan</div>
            <div class="d">Y mezclarlos no da error: da ruido.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Tres operaciones</div>
            <div class="d">Magnitud, distancia y ángulo. Preguntas distintas.</div></div>
          <div class="card"><div class="k">07</div><div class="t">No se edita</div>
            <div class="d">Cambia el texto, se regenera el vector entero.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">El significado se vuelve operable</div>
            <div class="d">Eso es lo que compra todo esto.</div></div>
        </div>""",
    },

]


NOTES = [
    {
        "lead": "Módulo 12 · Embeddings. El módulo merece su tiempo: cada minuto "
                "aquí ahorra tres en la sesión siguiente.",
        "rows": [
            ("6", "<b>Dibuja el plano en el pizarrón antes de proyectarlo</b> y pide "
                  "a la sala que coloque las palabras. Que discutan dónde va «ratón» "
                  "es exactamente el aprendizaje."),
            ("7", "El punto de la ambigüedad es sutil y valioso: la posición no "
                  "fuerza una elección, la representa. Ahí se entiende por qué esto "
                  "funciona mejor que las etiquetas."),
            ("9", "<b>El salto de dimensión es donde se pierde la gente.</b> Ve "
                  "panel por panel y remata con la frase de abajo: las operaciones "
                  "son las mismas. No entres en la cuarta dimensión física ni en "
                  "analogías de ciencia ficción; desvían y no ayudan."),
            ("13", "La incompatibilidad entre proveedores sorprende siempre. "
                   "Insiste en que no da error: da resultados sin sentido en "
                   "silencio, que es mucho peor."),
            ("16", "Las tres operaciones sobre la misma figura son la preparación "
                   "directa de la sesión siguiente. Que quede claro que son "
                   "preguntas distintas y pueden dar respuestas distintas."),
            ("18", "Cierra con lo que no se puede editar: es de donde sale todo el "
                   "trabajo de reproceso que van a tener que presupuestar."),
        ],
    },
]
