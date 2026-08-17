# -*- coding: utf-8 -*-
"""Deck: Módulo 6 — La escalera de adaptación de un modelo."""

from engine.diagrams import mod06 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 6 · La escalera de adaptación",
    "footer": "Programa de AI · Módulo 6",
    "outfile": "Modulo 06 - La escalera de adaptacion.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 6  ·  1 HORA",
        "title": "La escalera de adaptación",
        "tagline": "Cinco formas de conseguir que un modelo haga lo que necesitas, "
                   "ordenadas por lo que cuesta equivocarse.",
        "meta": [
            "<b>Sesión corta y de criterio.</b> Sin detalle técnico.",
            "<b>Al terminar:</b> sabes en qué escalón está tu problema",
        ],
    },

    {
        "kind": "statement",
        "text": "«Quiero que responda como mi empresa» casi nunca es un problema "
                "de <em>fine tuning</em>.",
        "after": "En la enorme mayoría de los casos se resuelve en el primer escalón: "
                 "unas instrucciones bien escritas y tres ejemplos.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "El reflejo que hay que interrumpir",
        "title": "La secuencia mental que sale cara",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>Lo que se piensa</h3>
            <p style="font-size:19pt;line-height:1.5">«No responde como
            necesitamos»<br/>↓<br/><b>entrenamos un modelo</b></p>
            <p>Tres semanas, un equipo, un artefacto que mantener. Y a menudo el
            resultado no supera al punto de partida.</p>
          </div>
          <div class="col accent">
            <h3>El orden real</h3>
            <p style="font-size:19pt;line-height:1.5">Prompt → Contexto →
            Recuperación → Herramientas → <b>Fine tuning</b></p>
            <p>Cada escalón resuelve un problema distinto. Saltárselos es la causa
            número uno de proyectos de adaptación fallidos.</p>
          </div>
        </div>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Los cinco escalones",
        "note": "El orden no es estético: es económico y de velocidad de iteración.",
    },

    {
        "kind": "content", "covers": [2, 4],
        "eyebrow": "La escalera completa",
        "title": "Qué cuesta subir cada peldaño",
        "html": dg.escalera(),
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Qué resuelve cada uno",
        "title": "Cinco problemas distintos, no cinco intensidades del mismo",
        "html": """
        <table>
          <thead><tr><th style="width:17%">Escalón</th><th style="width:44%">El problema que resuelve</th>
          <th>La señal de que te quedaste corto</th></tr></thead>
          <tbody>
            <tr><td><b>Prompt</b></td>
              <td>Le falta instrucción: no sabe qué esperas de él.</td>
              <td>Hace algo razonable, pero no lo que pediste.</td></tr>
            <tr><td><b>Contexto</b></td>
              <td>Le falta información, y esa información cabe en la petición.</td>
              <td>Responde con seguridad sobre datos que no tiene.</td></tr>
            <tr><td><b>Recuperación</b></td>
              <td>Le falta información, es demasiada y además cambia.</td>
              <td>Metes documentos a mano y ya no escalas.</td></tr>
            <tr><td><b>Herramientas</b></td>
              <td>No le falta información: le falta poder consultar o actuar.</td>
              <td>Necesitas el dato de ahora mismo, no el de la última carga.</td></tr>
            <tr><td><b>Fine tuning</b></td>
              <td>Tiene todo delante y aun así no sostiene el formato, el tono o un
                  criterio propio.</td>
              <td>Has agotado los cuatro anteriores y lo has medido.</td></tr>
          </tbody>
        </table>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "El criterio que decide",
        "note": "Una sola pregunta resuelve la elección sin ambigüedad.",
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "La pregunta",
        "title": "¿No sabe, o no puede?",
        "html": dg.sabe_o_puede(),
    },

    {
        "kind": "statement",
        "text": "Se sube de escalón cuando el anterior <em>se agotó</em>, no cuando "
                "se puso difícil.",
        "after": "Y «se agotó» significa que lo mediste y no dio más, no que te "
                 "cansaste de ajustarlo.",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Dónde estamos",
        "note": "La escalera es también el mapa de lo que queda del programa.",
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "Cuándo llega cada escalón",
        "title": "El resto del programa, visto como esta escalera",
        "html": """
        <table>
          <thead><tr><th style="width:22%">Escalón</th><th style="width:34%">Cuándo lo vemos</th>
          <th>Qué construiremos ahí</th></tr></thead>
          <tbody>
            <tr><td><b>Prompt</b></td><td>Ya está visto</td>
              <td>La sesión anterior, completa.</td></tr>
            <tr><td><b>Contexto</b></td><td>Lo siguiente que viene</td>
              <td>Cómo se consume el modelo como servicio y cómo se diseña la
                  memoria de un sistema.</td></tr>
            <tr><td><b>Recuperación</b></td><td>La parte más extensa del programa</td>
              <td>Almacenamiento, representación del significado y búsqueda
                  semántica.</td></tr>
            <tr><td><b>Herramientas</b></td><td>Dentro de esa misma parte</td>
              <td>Agentes y los protocolos por los que se comunican.</td></tr>
            <tr><td><b>Fine tuning</b></td><td>La última sesión del programa</td>
              <td>El detalle técnico y el costo real de mantenerlo.</td></tr>
          </tbody>
        </table>
        <div class="box" style="margin-top:6mm">
          <p><b>Un aviso para que nadie se pierda:</b> el programa no avanza en el
          orden de la escalera. La escalera ordena por costo de adaptación; el
          programa ordena por lo que hace falta entender antes. Son dos criterios
          distintos y los dos son correctos.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ejercicio práctico",
        "title": "Seis situaciones, ¿en qué escalón está cada una?",
        "html": """
        <div class="grid c3">
          <div class="card"><div class="k">01</div><div class="t">Tono</div>
            <div class="d">«El asistente responde demasiado informal para nuestros
            clientes.»</div></div>
          <div class="card"><div class="k">02</div><div class="t">Política nueva</div>
            <div class="d">«No conoce nuestra política de devoluciones, que cambió el
            mes pasado.»</div></div>
          <div class="card"><div class="k">03</div><div class="t">Formato</div>
            <div class="d">«Necesitamos siempre el mismo formato de salida y a veces
            se lo salta.»</div></div>
          <div class="card"><div class="k">04</div><div class="t">Dato vivo</div>
            <div class="d">«No sabe cuántas unidades hay en inventario ahora
            mismo.»</div></div>
          <div class="card"><div class="k">05</div><div class="t">Volumen documental</div>
            <div class="d">«Tenemos doce mil documentos internos y necesita
            consultarlos.»</div></div>
          <div class="card"><div class="k">06</div><div class="t">Escala</div>
            <div class="d">«Prompt de cuatro mil tokens con veinte ejemplos, y dos
            millones de llamadas al mes.»</div></div>
        </div>
        <div class="box" style="margin-top:6mm">
          <p>Para cada una: escalón y <b>por qué no hace falta subir más</b>. El
          último caso es el interesante — es el único donde el escalón más alto
          tiene un argumento económico legítimo.</p>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 6 · La escalera de adaptación. Sesión corta, de criterio: "
                "resiste la tentación de entrar en detalle técnico.",
        "rows": [
            ("2", "Dilo sin matices. El módulo entero existe para romper ese "
                  "reflejo, y suavizarlo lo desactiva."),
            ("4", "Escribe las dos secuencias en el pizarrón, una encima de la otra. "
                  "El contraste visual hace más que la explicación."),
            ("6", "Recorre la escalera nombrando el tiempo de iteración de cada "
                  "peldaño. Segundos, minutos, días, días, semanas. Esa progresión "
                  "es el argumento entero."),
            ("9", "<b>La pregunta que quieres que memoricen.</b> Hazla repetir en "
                  "voz alta: ¿no sabe, o no puede? Y enseña la prueba diagnóstica: "
                  "pegar la información en el prompt y ver si con eso acierta."),
            ("12", "Di explícitamente que el programa no sigue el orden de la "
                   "escalera y por qué. Si no lo aclaras, alguien va a pensar que "
                   "hay una incoherencia."),
            ("13", "Reparte las seis situaciones y déjalos discutir. El caso 6 es el "
                   "único que justifica el escalón más alto; deja que lleguen solos "
                   "en lugar de decírselo."),
        ],
    },
]
