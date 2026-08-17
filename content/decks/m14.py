# -*- coding: utf-8 -*-
"""Deck: Módulo 14 — Costos de un sistema de AI."""

from engine.diagrams import mod14 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 14 · Costos",
    "footer": "Programa de AI · Módulo 14",
    "outfile": "Modulo 14 - Costos.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 14  ·  2.5 HORAS",
        "title": "Costos",
        "tagline": "Calcular lo que va a costar una funcionalidad antes de "
                   "construirla.",
        "meta": [
            "<b>Antes de esta sesión:</b> tokens, herramientas y recuperación",
            "<b>Al terminar:</b> sabes qué palanca mover y cuánto ahorra",
        ],
    },

    {
        "kind": "statement",
        "text": "La mayoría de los sistemas de AI que se abandonan no se abandonan "
                "porque no funcionen: se abandonan porque <em>no se pueden "
                "pagar</em>.",
        "after": "El prototipo cuesta centavos porque lo usan tres personas. El "
                 "producto cuesta miles porque lo usan tres mil, y el descubrimiento "
                 "llega con la factura.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Qué se factura</b> — entrada, salida y razonamiento.</li>
          <li><b>El caché de prompts</b> — la optimización con mejor relación
            esfuerzo-beneficio, y cómo se rompe sin darse cuenta.</li>
          <li><b>Lo que cuesta el resto del sistema</b> — vectores,
            recuperación, imágenes y herramientas.</li>
          <li><b>El crecimiento cuadrático</b> — por qué una conversación larga se
            dispara.</li>
          <li><b>Estimar antes de construir</b> — la fórmula y el método.</li>
          <li><b>Diez palancas y cuatro guardas</b> — ordenadas por impacto.</li>
        </ol>""",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Una advertencia sobre las cifras de hoy",
        "title": "Órdenes de magnitud, no datos cerrados",
        "html": """
        <ul class="pts">
          <li><b>Los precios cambian con frecuencia, y casi siempre a la baja.</b>
            <span class="n">Cualquier número concreto que digamos hoy estará
            desactualizado en unos meses. Tráelos frescos de la documentación
            oficial el día que hagas el cálculo.</span></li>
          <li><b>Lo que no cambia son las relaciones.</b>
            <span class="n">Que la salida cuesta más que la entrada. Que leer del
            caché cuesta una fracción de procesar. Que el historial crece de forma
            cuadrática. Esas proporciones son lo que hay que llevarse.</span></li>
        </ul>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Qué se factura",
        "note": "Antes de optimizar, saber exactamente qué se está pagando.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Anatomía de una petición",
        "title": "La pregunta del usuario es la parte pequeña",
        "html": dg.anatomia_peticion(),
    },

    {
        "kind": "content", "covers": [1, 2],
        "eyebrow": "Tres precios distintos",
        "title": "Entrada, salida y razonamiento",
        "html": """
        <div class="grid c3">
          <div class="card"><div class="k">ENTRADA</div>
            <div class="t">Todo lo que mandas</div>
            <div class="d">Instrucciones, herramientas, historial, contexto
            recuperado y resultados. Es el volumen grande y el precio bajo.</div></div>
          <div class="card"><div class="k">SALIDA</div>
            <div class="t">Lo que genera</div>
            <div class="d">Del orden de tres a cinco veces más caro por token. Es el
            volumen pequeño y el precio alto.</div></div>
          <div class="card no"><div class="k">RAZONAMIENTO</div>
            <div class="t">Lo que piensa y no ves</div>
            <div class="d">Se factura como salida aunque no aparezca en la
            respuesta, y puede ser varias veces más largo que ella.</div></div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p><b>De ahí sale la primera palanca, que es contraintuitiva:</b> acortar la
          respuesta ahorra más que acortar el prompt.</p>
        </div>""",
    },

    {
        "kind": "statement",
        "text": "El presupuesto de razonamiento no es solo una perilla de calidad: es "
                "la <em>palanca de costo más grande</em> que existe en esos modelos.",
        "after": "Un modelo de razonamiento con esfuerzo alto puede costar un orden de "
                 "magnitud más que el mismo modelo sin él, para la misma pregunta.",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "El caché de prompts",
        "note": "La optimización con mejor relación esfuerzo-beneficio, y la que "
                "casi nadie aprovecha bien.",
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Funciona por prefijo exacto",
        "title": "Lo estable arriba, lo variable abajo",
        "html": dg.cache_prefijo(),
    },

    {
        "kind": "content", "covers": [3, 4],
        "eyebrow": "Dos descuentos que hay que conocer",
        "title": "Caché y procesamiento por lotes",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Caché de prompts</h3>
            <p><b>Escribir</b> al caché tiene un recargo sobre el precio de entrada.
            <b>Leer</b> tiene un descuento fuerte.</p>
            <p>No conviene siempre: si el prefijo es corto o la reutilización es
            baja, pagas el recargo sin llegar a aprovecharlo.</p>
          </div>
          <div class="col">
            <h3>Procesamiento por lotes</h3>
            <p>Descuento fuerte a cambio de aceptar una ventana de entrega de hasta
            un día.</p>
            <p>Si el trabajo no necesita respuesta inmediata, <b>estás pagando de
            más</b>. Enriquecer datos, clasificar en masa, analizar archivos
            históricos.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p><b>La pregunta que hay que hacerse:</b> ¿hay alguien mirando la pantalla
          esperando esto? Si no, no es interactivo, y no debería pagarse como si lo
          fuera.</p>
        </div>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Lo que cuesta el resto",
        "note": "Vectores, recuperación, imágenes y herramientas.",
    },

    {
        "kind": "content", "covers": [5, 6],
        "eyebrow": "Vectores",
        "title": "El costo no está en generar: está en regenerar y en guardar",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>Generar</h3>
            <p>Órdenes de magnitud más barato que producir texto. Indexar un corpus
            completo suele ser trivial.</p>
            <p><b>Lo caro es reprocesar</b>, y eso hay que presupuestarlo como gasto
            recurrente, no de arranque.</p>
          </div>
          <div class="col accent">
            <h3>Guardar</h3>
            <p>Un vector ocupa <b>dimensiones × 4 bytes</b>. Con 1 536 dimensiones
            son unos 6 KB.</p>
            <p>Un millón de vectores son del orden de 6 GB, más el índice. Y el
            índice <b>vive en memoria</b>: lo que pagas en realidad es RAM.</p>
            <p>Palancas: reducir dimensiones y cuantizar.</p>
          </div>
        </div>""",
    },

    {
        "kind": "content", "covers": [7, 8, 9],
        "eyebrow": "Tres costos que se subestiman",
        "title": "Recuperación, imágenes y herramientas",
        "html": """
        <ul class="pts">
          <li><b>La recuperación no cuesta por la consulta: cuesta por lo que
            inyecta.</b>
            <span class="n">Diez trozos de 500 tokens son 5 000 tokens de entrada
            añadidos a cada petición. El costo está en el prompt, no en la base de
            datos.</span></li>
          <li><b>Una imagen se convierte en tokens según su resolución.</b>
            <span class="n">Una imagen grande puede costar como varios miles de
            tokens de texto. La palanca es directa y casi siempre se olvida: reducir
            la resolución antes de enviarla.</span></li>
          <li><b>Cada llamada a una herramienta es un viaje completo de ida y
            vuelta.</b>
            <span class="n">Mandas todo el contexto, el modelo pide, ejecutas, y
            vuelves a mandar todo el contexto más el resultado. Diez pasos no cuestan
            diez veces uno: cuestan bastante más.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Una consecuencia poco común",
        "title": "Recuperar menos y mejor mejora las dos cosas",
        "html": """
        <div class="box big">
          <p>Casi toda optimización de costo cuesta calidad, y casi toda mejora de
          calidad cuesta dinero. <b>El reordenamiento es una de las poquísimas
          excepciones.</b></p>
        </div>
        <ul class="pts" style="margin-top:7mm">
          <li>Recuperas amplio, filtras con precisión y mandas cinco trozos en lugar
            de cincuenta.</li>
          <li><b>Baja el costo</b> porque inyectas muchos menos tokens.</li>
          <li><b>Sube la calidad</b> porque el contexto relevante deja de estar
            diluido en ruido.</li>
        </ul>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "El historial",
        "note": "La cuenta que justifica todo lo que hemos dicho sobre acotar el "
                "contexto.",
    },

    {
        "kind": "content", "covers": [10],
        "eyebrow": "Lo que se acumula al reenviar",
        "title": "El costo crece con el cuadrado de la longitud",
        "html": dg.crecimiento_cuadratico(),
    },

    # ── 05 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "05",
        "title": "Estimar antes de construir",
        "note": "La habilidad que decide qué se construye y qué no.",
    },

    {
        "kind": "content", "covers": [11],
        "eyebrow": "La fórmula",
        "title": "Cómo se calcula",
        "html": """
        <pre>costo_petición = entrada_sin_caché       × precio_entrada
               + entrada_cacheada        × precio_lectura_caché
               + (salida + razonamiento) × precio_salida

costo_mensual  = costo_petición
               × peticiones_por_sesión
               × sesiones_por_usuario_al_mes
               × usuarios_activos
               + costos_fijos  (almacenamiento, reproceso, APIs externas)</pre>
        <div class="box" style="margin-top:7mm">
          <p><b>El método importa más que la fórmula:</b> ejecuta veinte o treinta
          casos reales, lee el campo de uso de cada respuesta, saca el promedio y el
          percentil 95, y multiplica.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [11],
        "eyebrow": "Tres detalles que arruinan una estimación",
        "title": "Lo que se suele calcular mal",
        "html": """
        <ul class="pts">
          <li><b>Usar el promedio y no el percentil 95.</b>
            <span class="n">Hay usuarios que sostienen conversaciones de ochenta
            turnos. Son pocos y se comen el presupuesto.</span></li>
          <li><b>Adivinar las peticiones por sesión.</b>
            <span class="n">No se estima: se mide con el prototipo. La diferencia
            entre tres y ocho peticiones por sesión es un factor de tres en la
            factura.</span></li>
          <li><b>Olvidar los costos fijos.</b>
            <span class="n">El almacenamiento vectorial y el reproceso se pagan
            aunque nadie use el producto ese mes.</span></li>
        </ul>
        <div class="box" style="margin-top:6mm">
          <p>El número que hay que poder decir en una frase es el <b>costo por usuario
          activo al mes</b>. Es el que permite saber si la funcionalidad es viable con
          el modelo de negocio.</p>
        </div>""",
    },

    # ── 06 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "06",
        "title": "Palancas y guardas",
        "note": "Qué mover, en qué orden, y qué topes poner siempre.",
    },

    {
        "kind": "content", "covers": [12],
        "eyebrow": "Ordenadas por impacto",
        "title": "Diez palancas",
        "html": dg.palancas(),
    },

    {
        "kind": "content", "covers": [12],
        "eyebrow": "Y cuatro que no son opcionales",
        "title": "Guardas",
        "html": dg.guardas(),
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">La salida cuesta más</div>
            <div class="d">Acortar la respuesta ahorra más que acortar el
            prompt.</div></div>
          <div class="card"><div class="k">02</div><div class="t">El razonamiento se factura</div>
            <div class="d">Aunque no lo veas, y puede ser lo más largo.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Prefijo estable</div>
            <div class="d">Una marca de tiempo arriba tira el caché cada
            llamada.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Lo no interactivo, por lotes</div>
            <div class="d">Si nadie espera, no se paga como si esperara.</div></div>
          <div class="card"><div class="k">05</div><div class="t">El RAG cuesta en el prompt</div>
            <div class="d">No en la base de datos.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Crecimiento cuadrático</div>
            <div class="d">Veinte turnos son 210 veces T, no 20.</div></div>
          <div class="card"><div class="k">07</div><div class="t">Mide, no adivines</div>
            <div class="d">Veinte casos reales y el percentil 95.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">La palanca mayor es no llamar</div>
            <div class="d">Si una regla lo resuelve, es infinitamente más
            barato.</div></div>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 14 · Costos.",
        "rows": [
            ("2", "Abre con la afirmación incómoda y déjala respirar. Es cierta y "
                  "cambia la actitud del resto de la sesión."),
            ("4", "<b>Trae las cifras frescas ese día</b> y di en voz alta que son "
                  "órdenes de magnitud. Lo que se lleva la sala son las relaciones, "
                  "no los números."),
            ("7", "El dato del razonamiento sorprende siempre. Si hay tiempo, "
                  "muestra el campo de uso de una respuesta real con razonamiento "
                  "alto."),
            ("11", "<b>El caché es la optimización con mejor relación esfuerzo "
                   "beneficio y casi nadie la usa bien.</b> Detente en las tres "
                   "formas de romperlo: son errores de una línea."),
            ("17", "Deriva el crecimiento cuadrático en el pizarrón antes de "
                   "proyectar la gráfica. Ver salir 210 frente a 20 es el momento "
                   "del módulo."),
            ("19", "Insiste en el percentil 95. Es la diferencia entre un "
                   "presupuesto que aguanta y uno que se rompe el primer mes."),
            ("23", "La palanca uno es la más importante y la más ignorada: no llamar "
                   "al modelo."),
        ],
    },
]
