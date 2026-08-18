# -*- coding: utf-8 -*-
"""Deck: Módulo 2 — Qué es un LLM.

Mismas reglas de redacción que el resto de los decks: todo se explica como es,
no se cita otro módulo, no se adelantan conceptos que aún no se han visto, y
antes que una lámina de texto va un diagrama.
"""

from engine.diagrams import mod02 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 2 · Qué es un LLM",
    "footer": "Programa de AI · Módulo 2",
    "outfile": "Modulo 02 - Que es un LLM.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 2  ·  1.5 HORAS",
        "title": "Qué es un LLM",
        "tagline": "El objeto con el que vas a trabajar: qué contiene, quién lo "
                   "fabrica y cuánto cuesta.",
        "meta": [
            "<b>Antes de esta sesión:</b> dónde encaja la AI entre las formas de "
            "resolver un problema",
            "<b>Al terminar:</b> sabes elegir un proveedor con criterio propio",
        ],
    },

    {
        "kind": "statement",
        "text": "Un modelo de lenguaje es <em>un archivo de números</em> y el código "
                "que sabe en qué orden multiplicarlos.",
        "after": "Suena decepcionante. Pero de ahí salen el precio, el tamaño, la "
                 "latencia y la razón de que existan tan pocos proveedores.",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Qué hay dentro</b> — qué son los miles de millones de parámetros
            y por qué el tamaño decide dónde puede ejecutarse.</li>
          <li><b>Qué cuesta fabricar uno</b> — cómputo, datos, energía y agua,
            en órdenes de magnitud.</li>
          <li><b>AI como servicio</b> — qué compras exactamente cuando pagas una API,
            y qué sigue siendo tu trabajo.</li>
          <li><b>El panorama</b> — quién fabrica modelos hoy y en qué se diferencian
            los que se descargan de los que no.</li>
          <li><b>Cómo elegir</b> — los siete ejes que deciden, y por qué las tablas
            comparativas públicas ayudan menos de lo que parece.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "01",
        "title": "Qué hay dentro",
        "note": "La pregunta que todo el mundo hace: ¿a qué se refieren los miles "
                "de millones de parámetros?",
    },

    {
        "kind": "content",
        "covers": [2],
        "eyebrow": "La respuesta concreta",
        "title": "Un parámetro es un número decimal",
        "html": dg.parametro_peso(),
    },

    {
        "kind": "content",
        "covers": [1, 2],
        "eyebrow": "Una distinción que importa",
        "title": "Son pesos, no datos",
        "html": """
        <ul class="pts">
          <li><b>Dentro del archivo no hay una copia de la Wikipedia.</b>
            <span class="n">No hay un índice que consultar ni una tabla de hechos.
            Hay una configuración de multiplicaciones que, aplicada a un texto,
            tiende a producir continuaciones plausibles.</span></li>
          <li><b>El modelo no «guarda» información: quedó ajustado por ella.</b>
            <span class="n">Los hechos que reproduce bien son los que aparecieron
            muchas veces durante el entrenamiento. Los que aparecieron poco los
            reproduce mal, y sin avisar de la diferencia.</span></li>
          <li><b>Por eso el tamaño y la capacidad no son lo mismo.</b>
            <span class="n">Un modelo más grande no es automáticamente mejor: importa
            con qué datos y con qué método se ajustaron esos números.</span></li>
        </ul>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "02",
        "title": "Qué cuesta fabricar uno",
        "note": "Para dimensionar por qué hay cinco proveedores serios y no quinientos.",
    },

    {
        "kind": "content",
        "covers": [3],
        "eyebrow": "El costo de entrenar desde cero",
        "title": "Cuatro maneras de medir lo mismo",
        "html": dg.costo_entrenamiento(),
    },

    {
        "kind": "content",
        "covers": [3],
        "eyebrow": "Qué hacer con ese dato",
        "title": "El costo del que nadie habla es el otro",
        "html": """
        <div class="cols uneven">
          <div class="col">
            <h3>Entrenamiento</h3>
            <p><b>Lo paga el proveedor.</b> Una vez, meses antes de que tú existas
            como cliente.</p>
            <p>Es un costo hundido: enorme, espectacular en los titulares, y
            completamente ajeno a tu presupuesto.</p>
          </div>
          <div class="col accent">
            <h3>Inferencia</h3>
            <p><b>La pagas tú.</b> Cada petición, cada usuario, cada mes, mientras
            el producto exista.</p>
            <p>Se cobra por la cantidad de texto que entra y por la que sale, y las
            dos tienen precios distintos.</p>
            <p>Es el número que va a aparecer en tu factura.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>La cifra de entrenamiento sirve para entender <b>por qué el mercado tiene
          la forma que tiene</b>. Para decidir si tu producto es viable, el número que
          hay que calcular es el otro.</p>
        </div>""",
    },

    {
        "kind": "content",
        "covers": [4],
        "eyebrow": "La etapa que falta",
        "title": "Un modelo recién entrenado no se comporta como un chat",
        "html": dg.comportamiento_aprendido(),
    },

    {
        "kind": "content",
        "covers": [4],
        "eyebrow": "Lo que se explica solo con esto",
        "title": "Cuatro cosas que no vienen del texto, vienen de la calificación",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Sabe cuándo parar</div>
            <div class="d">Detenerse no se deduce de predecir texto. Es un
            comportamiento que alguien premió.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Responde en viñetas</div>
            <div class="d">Un formato que los calificadores puntuaron alto, no una
            propiedad del lenguaje.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Cada modelo tiene carácter</div>
            <div class="d">El texto de entrenamiento se parece entre proveedores. Lo
            que cambia es quién calificó y con qué criterio.</div></div>
          <div class="card"><div class="k">04</div><div class="t">A veces se niega de más</div>
            <div class="d">Las negativas también se aprendieron. Calibrarlas es de
            las cosas más difíciles de hacer bien.</div></div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p><b>Es la respuesta corta a por qué no todos los modelos se sienten
          igual.</b> Dos modelos con capacidad equivalente pueden ser muy distintos
          de usar, y esa diferencia no aparece en ninguna tabla comparativa.</p>
        </div>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "03",
        "title": "AI como servicio",
        "note": "Qué compras exactamente cuando pagas una API, y qué no.",
    },

    {
        "kind": "content",
        "covers": [5],
        "eyebrow": "La pila completa",
        "title": "Quién es dueño de cada capa",
        "html": dg.ai_como_servicio(),
    },

    {
        "kind": "content",
        "covers": [5],
        "eyebrow": "El modelo de negocio",
        "title": "Estás alquilando capacidad de cómputo, medida en texto",
        "html": """
        <ul class="pts">
          <li><b>No compras el modelo: compras acceso.</b>
            <span class="n">Los pesos no se te entregan. Si el proveedor sube el
            precio, retira el modelo o cambia su comportamiento, tu producto lo
            nota el mismo día.</span></li>
          <li><b>Pagas por uso, sin mínimo y sin infraestructura.</b>
            <span class="n">Es la razón real de que la AI se haya vuelto accesible:
            hace cinco años había que comprar servidores; hoy se empieza con una
            clave y una tarjeta.</span></li>
          <li><b>El dato viaja al proveedor.</b>
            <span class="n">Todo lo que mandas sale de tu infraestructura. Para
            algunos sectores eso es un requisito legal, no una preferencia, y es
            lo que hace que los modelos descargables sigan importando.</span></li>
          <li><b>Los modelos se deprecan.</b>
            <span class="n">El que uses hoy tendrá fecha de retiro. Conviene diseñar
            para poder cambiarlo, no para depender de uno.</span></li>
        </ul>""",
    },

    {
        "kind": "content",
        "covers": [6],
        "eyebrow": "Tres cosas que suelen confundirse",
        "title": "«Tener un modelo propio» significa tres cosas distintas",
        "html": """
        <div class="grid c3">
          <div class="card no"><div class="k">INVIABLE</div>
            <div class="t">Entrenar un modelo base desde cero</div>
            <div class="d">Miles de GPU durante meses, un corpus a escala de internet
            y un equipo de investigación. Fuera del alcance de prácticamente
            cualquier empresa, y va a seguir estándolo.</div></div>
          <div class="card"><div class="k">POSIBLE</div>
            <div class="t">Hospedar un modelo de pesos abiertos</div>
            <div class="d">Descargas los pesos y los corres en tu infraestructura.
            El dato no sale de casa. Pagas GPU por hora, la uses o no, así que
            sale a cuenta con tráfico alto y constante.</div></div>
          <div class="card"><div class="k">POSIBLE</div>
            <div class="t">Adaptar un modelo existente</div>
            <div class="d">Partes de un modelo ya entrenado y lo ajustas con
            ejemplos propios para que se comporte como necesitas. Mucho más
            barato que lo anterior, y con sus propias condiciones.</div></div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p>Cuando alguien dice «queremos nuestro propio modelo», casi siempre está
          hablando de la tercera y creyendo que habla de la primera.</p>
        </div>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "04",
        "title": "El panorama",
        "note": "Quién fabrica modelos hoy, y la única división que de verdad "
                "cambia tu arquitectura.",
    },

    {
        "kind": "content",
        "covers": [7],
        "eyebrow": "Quién fabrica modelos hoy",
        "title": "La división que importa no es por marca",
        "html": dg.proveedores(),
    },

    {
        "kind": "content",
        "covers": [7],
        "eyebrow": "Dos mundos con economías distintas",
        "title": "Por API o descargado: qué cambia de verdad",
        "html": """
        <table>
          <thead><tr><th style="width:22%"></th><th style="width:39%">Por API</th>
          <th>Pesos abiertos, hospedados por ti</th></tr></thead>
          <tbody>
            <tr><td><b>Cómo pagas</b></td>
              <td>Por texto procesado. Sin mínimo.</td>
              <td>GPU por hora, la uses o no.</td></tr>
            <tr><td><b>Cuándo sale a cuenta</b></td>
              <td>Tráfico bajo o irregular. Casi siempre al empezar.</td>
              <td>Tráfico alto y constante, donde el costo fijo se reparte.</td></tr>
            <tr><td><b>Dónde vive el dato</b></td>
              <td>Sale a un tercero.</td>
              <td>No sale de tu infraestructura.</td></tr>
            <tr><td><b>Quién opera</b></td>
              <td>El proveedor. No hay nada que mantener.</td>
              <td>Tú: escalado, actualizaciones, caídas, hardware.</td></tr>
            <tr><td><b>Techo de calidad</b></td>
              <td>El estado del arte, disponible el día que sale.</td>
              <td>Detrás, aunque la distancia se acorta rápido.</td></tr>
          </tbody>
        </table>""",
    },

    # ── 05 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "05",
        "title": "Cómo elegir",
        "note": "Siete ejes. La capacidad es solo uno, y casi nunca es el que decide.",
    },

    {
        "kind": "content",
        "covers": [8],
        "eyebrow": "Los ejes de decisión",
        "title": "Qué preguntar antes de casarte con un modelo",
        "html": """
        <table>
          <thead><tr><th style="width:19%">Eje</th><th style="width:37%">Qué preguntar</th>
          <th>Por qué importa</th></tr></thead>
          <tbody>
            <tr><td><b>Capacidad</b></td><td>¿Resuelve mi tarea con la calidad que
              necesito?</td><td>Condición necesaria, pero casi nunca la que decide.</td></tr>
            <tr><td><b>Precio</b></td><td>¿Cuánto cuestan por separado el texto que
              entra y el que sale?</td><td>Lo que sale suele costar varias veces
              más.</td></tr>
            <tr><td><b>Latencia</b></td><td>¿Cuánto tarda en empezar a responder y
              en terminar?</td><td>Decide si sirve para una interfaz o solo para
              procesos de fondo.</td></tr>
            <tr><td><b>Cuánto texto acepta</b></td><td>¿Cuánto cabe en una sola
              petición?</td><td>Condiciona toda la arquitectura que construyas
              encima.</td></tr>
            <tr><td><b>Comportamiento</b></td><td>¿Sigue instrucciones? ¿Se niega de
              más? ¿Respeta formatos?</td><td>Lo que más se nota en producción y lo
              que menos aparece en las comparativas.</td></tr>
            <tr><td><b>Modalidad</b></td><td>¿Acepta imágenes, audio,
              documentos?</td><td>Abre o cierra casos de uso completos.</td></tr>
            <tr><td><b>Despliegue</b></td><td>¿Solo API, o puedo descargar los
              pesos?</td><td>Decide si el dato sale de casa. A veces es un requisito
              legal.</td></tr>
          </tbody>
        </table>""",
    },

    {
        "kind": "content",
        "covers": [9],
        "eyebrow": "Sobre las comparativas públicas",
        "title": "Un buen puesto en una tabla no predice tu resultado",
        "html": """
        <ul class="pts">
          <li><b>Miden tareas que no son la tuya.</b>
            <span class="n">Exámenes de opción múltiple, problemas de competición,
            preguntas de conocimiento general. Tu caso probablemente no se parece
            a ninguno.</span></li>
          <li><b>Se saturan y se contaminan.</b>
            <span class="n">Cuando una prueba se vuelve importante, acaba
            apareciendo en los datos de entrenamiento y deja de discriminar.</span></li>
          <li><b>Sirven para descartar, no para elegir.</b>
            <span class="n">Un modelo claramente por debajo se puede eliminar de la
            lista. Entre los que quedan arriba, la tabla ya no informa.</span></li>
        </ul>
        <div class="box big" style="margin-top:7mm">
          <p><b>Arma veinte casos tuyos y pásalos por tres modelos.</b> Veinte
          ejemplos reales de tu producto informan más que cualquier comparativa
          publicada.</p>
        </div>""",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Un parámetro es un número</div>
            <div class="d">Y setenta mil millones de ellos son unos 140 GB. De ahí
            sale todo lo demás.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Son pesos, no datos</div>
            <div class="d">No hay una base de hechos dentro que se pueda consultar.</div></div>
          <div class="card"><div class="k">03</div><div class="t">El entrenamiento no lo pagas tú</div>
            <div class="d">Tu factura es la inferencia, y se repite para siempre.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Compras acceso, no el modelo</div>
            <div class="d">Las capas de arriba de la pila siguen siendo tu trabajo.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Entrenar, hospedar y adaptar</div>
            <div class="d">Son tres cosas distintas. Solo la primera es inviable.</div></div>
          <div class="card"><div class="k">06</div><div class="t">API o pesos abiertos</div>
            <div class="d">La pregunta de fondo es dónde puede vivir el dato.</div></div>
          <div class="card"><div class="k">07</div><div class="t">Siete ejes, no uno</div>
            <div class="d">La capacidad rara vez es el criterio que decide.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">Mide con tus casos</div>
            <div class="d">Veinte ejemplos propios ganan a cualquier tabla.</div></div>
        </div>""",
    },

]


NOTES = [
    {
        "lead": "Módulo 2 · Qué es un LLM — láminas 1 a 10.",
        "rows": [
            ("2", "Di la frase tal cual, sin suavizarla. La decepción inicial es "
                  "parte del método: desmonta la caja mágica antes de construir "
                  "nada encima."),
            ("5", "<b>Haz la cuenta en el pizarrón, no la proyectes solamente.</b> "
                  "Setenta mil millones por dos bytes. Que salga el número delante "
                  "de ellos es lo que convierte «modelo grande» en algo con tamaño "
                  "físico."),
            ("6", "La distinción peso/dato es sutil y es la que prepara todo lo que "
                  "viene después. Si alguien pregunta «¿y entonces cómo sabe "
                  "cosas?», la respuesta corta es: quedó ajustado por ellas, no las "
                  "guarda."),
            ("8", "<b>Trae las cifras frescas el día de la clase.</b> Varían mucho "
                  "por fuente y metodología, y se han vuelto terreno de disputa. "
                  "Preséntalas como órdenes de magnitud y di en voz alta que lo son."),
            ("9", "El giro del módulo. La sala llega interesada en el número "
                  "espectacular; sácalos de ahí y llévalos al número que sí van a "
                  "pagar."),
            ("10", "<b>Lee el panel del medio en voz alta antes de explicar nada.</b> "
                   "Que un modelo recién entrenado conteste una pregunta con otra "
                   "pregunta parecida suele sorprender, y es la mejor puerta de "
                   "entrada. "
                   "<span class='say'>«El comportamiento conversacional no se "
                   "programó: se calificó.»</span>"),
            ("11", "Aquí es donde la sala conecta el mecanismo con cosas que ya ha "
                   "vivido. Deja que digan ellos qué otras rarezas creen que salen de "
                   "esta etapa. Evita las cifras concretas de cuántas personas y en "
                   "qué países: casi ninguna es verificable."),
        ],
    },
    {
        "lead": "Láminas 11 a 20.",
        "rows": [
            ("13", "Recorre la pila de abajo arriba y detente en la línea de "
                   "propiedad. La pregunta que quieres provocar: «¿entonces qué "
                   "estamos comprando exactamente?»."),
            ("15", "<b>Lámina clave para conversaciones con dirección.</b> El "
                   "«queremos nuestro propio modelo» aparece en todas las empresas. "
                   "Que salgan sabiendo separar las tres opciones evita meses de "
                   "trabajo mal dirigido."),
            ("17", "Los logos son para orientar, no para memorizar. Di explícitamente "
                   "que la lista caduca y que lo que no caduca es el eje: "
                   "¿el dato puede salir de tu infraestructura?"),
            ("20", "Si hay tiempo, abre la documentación de precios de dos "
                   "proveedores en vivo y compárala. Ver que los números no "
                   "coinciden con lo que la gente recordaba es más persuasivo que "
                   "advertirlo."),
            ("21", "Insiste en el cierre: veinte casos propios. Es la misma "
                   "disciplina que van a necesitar para cualquier decisión técnica "
                   "del resto del programa."),
        ],
    },
]
