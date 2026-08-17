# -*- coding: utf-8 -*-
"""Deck: Módulo 4 — Cómo razona un LLM.

Reglas de redacción de este deck:

1. Todo se explica como es, no como corrección de lo que se creía. La lámina
   no habla nunca del temario ni de versiones anteriores.
2. No se cita otro módulo. Si un tema se retoma después, se retoma después;
   aquí solo estorba.
3. No se adelantan conceptos que aún no se han visto. Si una idea necesita un
   término que llega más adelante, se explica con lo que ya se tiene.
4. Antes que una lámina de texto, un diagrama.
"""

from engine.diagrams import mod04 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 4 · Cómo razona un LLM",
    "footer": "Programa de AI · Módulo 4",
    "outfile": "Modulo 04 - Como razona un LLM.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 4  ·  3 HORAS",
        "title": "Cómo razona un LLM",
        "tagline": "Qué ocurre exactamente entre el prompt y la respuesta.",
        "meta": [
            "<b>Antes de esta sesión:</b> tokens y ventana de contexto",
            "<b>Al terminar:</b> sabes predecir cómo se va a comportar un modelo",
        ],
    },

    {
        "kind": "statement",
        "text": "Un modelo de lenguaje hace <em>una sola cosa</em>. "
                "Todo lo demás es consecuencia.",
        "after": "Hoy vemos cuál es esa cosa, y salimos pudiendo explicar por qué "
                 "inventa datos, por qué el orden del prompt cambia la respuesta y "
                 "por qué no recuerda nada.",
    },

    {
        "kind": "content",
        "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Qué hace y qué no hace</b> — dónde termina el modelo y dónde empieza
            todo lo que le construyes alrededor.</li>
          <li><b>La operación única</b> — predecir el siguiente token, y el bucle que
            convierte eso en un texto.</li>
          <li><b>Atención</b> — por qué el modelo pondera unas partes del prompt más
            que otras, y qué implica para cómo lo escribes.</li>
          <li><b>Cómo representa un token</b> — significado convertido en posición.</li>
          <li><b>Pesos congelados</b> — la diferencia entre entrenar y usar.</li>
          <li><b>Temperatura, top-p y top-k</b> — las tres perillas del muestreo.</li>
          <li><b>Por qué inventa</b> — la mecánica de una alucinación.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "01",
        "title": "Qué hace y qué no hace",
        "note": "Empecemos por delimitar el objeto: casi todo lo que se le atribuye "
                "a un modelo lo hace otra cosa.",
    },

    {
        "kind": "content",
        "covers": [1],
        "eyebrow": "A mano alzada",
        "title": "¿Cuáles de estas hace un modelo de lenguaje?",
        "html": """
        <div class="grid c5">
          <div class="card"><div class="k">01</div><div class="t">Busca en internet</div>
            <div class="d">Cuando no sabe algo, lo consulta.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Tiene una base de datos</div>
            <div class="d">Guarda hechos y los recupera.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Recuerda</div>
            <div class="d">Aprende de lo que le dijiste antes.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Ejecuta código</div>
            <div class="d">Corre lo que escribe para comprobarlo.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Piensa</div>
            <div class="d">Razona como una persona.</div></div>
        </div>""",
    },

    {
        "kind": "statement",
        "text": "Ninguna de las cinco.",
        "after": "Y sin embargo todas ocurren cuando usas un chat de AI. La diferencia "
                 "está en quién las hace.",
    },

    {
        "kind": "content",
        "covers": [1],
        "eyebrow": "La frontera",
        "title": "El modelo es una pieza pequeña de un sistema grande",
        "html": dg.frontera_modelo(),
    },

    {
        "kind": "content",
        "covers": [1],
        "eyebrow": "Lo que cambia en tu trabajo",
        "title": "Todo lo de fuera es tuyo",
        "html": """
        <ul class="pts">
          <li><b>Cuando un chat cita una página web</b>, un programa hizo la búsqueda,
            pegó el resultado en el prompt y el modelo escribió encima.
            <span class="n">El modelo nunca vio internet. Vio texto que alguien le puso
            delante.</span></li>
          <li><b>Cuando parece recordar la conversación</b>, alguien guardó los mensajes
            y los reenvió completos en la siguiente petición.
            <span class="n">Si dejas de reenviarlos, deja de recordar en el acto.</span></li>
          <li><b>Cuando ejecuta código</b>, el modelo escribió una petición de ejecución
            y tu programa la corrió.
            <span class="n">El modelo se quedó esperando el resultado, sin saber qué pasó.</span></li>
        </ul>
        <div class="box" style="margin-top:7mm">
          <p>Cada capacidad que quieras que tenga tu producto, la construyes tú.
          El modelo aporta el juicio sobre el texto; nada más, y nada menos.</p>
        </div>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "02",
        "title": "La operación única",
        "note": "Lo que el modelo sí hace, y cabe en una frase.",
    },

    {
        "kind": "statement",
        "text": "Recibe una secuencia de tokens y produce una <em>probabilidad para "
                "cada token posible</em> del vocabulario.",
        "after": "Una sola vez. Para producir un texto largo, el sistema lo llama "
                 "muchas veces seguidas.",
    },

    {
        "kind": "content",
        "covers": [2],
        "eyebrow": "El ciclo completo",
        "title": "Cómo una predicción se convierte en un texto",
        "html": dg.bucle_generacion(),
    },

    {
        "kind": "content",
        "covers": [3],
        "eyebrow": "Lo que devuelve una pasada",
        "title": "«el gato se subió al…»",
        "html": dg.distribucion(),
    },

    {
        "kind": "content",
        "covers": [3],
        "eyebrow": "Tres cosas que esa tabla resuelve",
        "title": "Lo que se deduce de la distribución",
        "html": """
        <ol class="pts">
          <li><b>Cualquier continuación es posible.</b>
            <span class="n">Todos los tokens reciben probabilidad, incluso los absurdos.
            Diminuta, pero nunca cero. Por eso ninguna respuesta está descartada del
            todo, por rara que sea.</span></li>
          <li><b>El modelo no elige: entrega la tabla.</b>
            <span class="n">Quien elige es el código de muestreo que hay encima. Sus
            reglas son la temperatura, el top-p y el top-k, y las controlas tú desde
            la petición.</span></li>
          <li><b>No hay plan.</b>
            <span class="n">No sabía que iba a decir «tejado» cuando empezó la frase, ni
            sabe qué va a decir después. Cada token se decide con lo que hay escrito
            hasta ese momento.</span></li>
        </ol>""",
    },

    {
        "kind": "statement",
        "text": "Un texto parece planificado por la misma razón por la que un río "
                "parece haber <em>elegido</em> su cauce.",
        "after": "Cada paso local coherente produce un recorrido global que se ve "
                 "intencionado. Nadie lo trazó.",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "03",
        "title": "Atención",
        "note": "Por qué dos prompts con las mismas palabras en distinto orden dan "
                "respuestas distintas.",
    },

    {
        "kind": "content",
        "covers": [4],
        "eyebrow": "La idea",
        "title": "Al predecir, el modelo pondera distinto cada token anterior",
        "html": dg.atencion(),
    },

    {
        "kind": "content",
        "covers": [4],
        "eyebrow": "Lo que esto cambia al escribir un prompt",
        "title": "Tres consecuencias prácticas",
        "html": """
        <ul class="pts">
          <li><b>La posición pesa.</b>
            <span class="n">Lo que va al principio y al final tiende a influir más que
            lo enterrado en medio. Las instrucciones críticas no se sepultan entre
            documentos: van arriba, o se repiten al final.</span></li>
          <li><b>El costo crece más rápido que el texto.</b>
            <span class="n">El mecanismo compara cada token con los anteriores, así que
            duplicar el contexto cuesta más del doble en cómputo. Un prompt largo no
            es solo caro: es lento.</span></li>
          <li><b>Marcar las secciones ayuda de verdad.</b>
            <span class="n">Separar instrucciones, datos y formato con etiquetas o
            encabezados le da al mecanismo fronteras claras. No es cosmética.</span></li>
        </ul>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "04",
        "title": "Cómo representa un token",
        "note": "Qué hay dentro del modelo cuando procesa una palabra.",
    },

    {
        "kind": "content",
        "covers": [5],
        "eyebrow": "De palabra a posición",
        "title": "El modelo no manipula palabras: manipula posiciones",
        "html": dg.representacion_interna(),
    },

    {
        "kind": "content",
        "covers": [5],
        "eyebrow": "Por qué importa",
        "title": "Significado convertido en números",
        "html": """
        <ul class="pts">
          <li><b>Ese espacio no lo diseñó nadie.</b>
            <span class="n">Salió del entrenamiento. Nadie puede decir qué significa la
            dimensión 412, y aun así el conjunto ordena el significado con
            consistencia.</span></li>
          <li><b>La cercanía es lo que hace que generalice.</b>
            <span class="n">Como «gato» y «felino» caen cerca, lo que el modelo aprendió
            sobre uno le sirve para el otro sin haberlo visto escrito.</span></li>
          <li><b>Es un paso interno, no una salida.</b>
            <span class="n">Estos números viven dentro del cómputo. No se guardan, no se
            devuelven y no se consultan desde fuera.</span></li>
        </ul>""",
    },

    # ── 05 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "05",
        "title": "Pesos congelados",
        "note": "La diferencia entre entrenar un modelo y usarlo.",
    },

    {
        "kind": "content",
        "covers": [6],
        "eyebrow": "Dos momentos distintos",
        "title": "Entrenar y usar no son la misma operación",
        "html": dg.entrenamiento_inferencia(),
    },

    {
        "kind": "statement",
        "text": "El modelo <em>no aprende</em> de la conversación.",
        "after": "Cada petición se procesa con el mismo archivo de números que la "
                 "anterior. Si un producto recuerda algo de la semana pasada, es porque "
                 "alguien lo guardó y lo volvió a poner en el prompt.",
    },

    # ── 06 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "06",
        "title": "De la probabilidad al texto",
        "note": "El modelo entrega la tabla. Estas tres perillas deciden qué sale de ella.",
    },

    {
        "kind": "content",
        "covers": [7],
        "eyebrow": "La misma tabla, tres muestreos",
        "title": "Qué hace la temperatura",
        "html": dg.temperatura(),
    },

    {
        "kind": "content",
        "covers": [7],
        "eyebrow": "Las tres perillas",
        "title": "Temperatura, top-p y top-k",
        "html": """
        <table>
          <thead><tr><th style="width:15%">Parámetro</th><th style="width:43%">Qué hace</th>
          <th>Cuándo moverlo</th></tr></thead>
          <tbody>
            <tr><td><b>Temperatura</b><span class="m">0 – 2</span></td>
              <td>Aplana o agudiza la tabla antes de sortear. Cerca de cero, gana casi
                  siempre el más probable.</td>
              <td>Bájala para extraer datos, clasificar o devolver un formato fijo.
                  Súbela solo para generar variantes.</td></tr>
            <tr><td><b>Top-p</b><span class="m">0 – 1</span></td>
              <td>Descarta la cola: se queda con los más probables hasta acumular
                  <i>p</i>. El número de candidatos cambia según lo segura que esté
                  la tabla.</td>
              <td>Es la palanca preferible: se adapta sola. Se ajusta esta o el top-k,
                  no las dos.</td></tr>
            <tr><td><b>Top-k</b><span class="m">1 – 100</span></td>
              <td>Se queda con los <i>k</i> primeros, siempre el mismo número, sin
                  importar cómo esté repartida la probabilidad.</td>
              <td>Cuando quieres un tope duro y predecible de candidatos.</td></tr>
          </tbody>
        </table>
        <div class="box" style="margin-top:6mm">
          <p><b>Temperatura cero no garantiza la misma respuesta siempre.</b> En un
          servicio real, el orden de las operaciones en punto flotante y el reparto
          entre servidores introducen pequeñas variaciones.</p>
        </div>""",
    },

    # ── 07 ────────────────────────────────────────────────────────────────
    {
        "kind": "section",
        "step": "07",
        "title": "Por qué inventa",
        "note": "La mecánica de una alucinación, con todo lo anterior ya en la mesa.",
    },

    {
        "kind": "content",
        "covers": [8],
        "eyebrow": "La mecánica",
        "title": "Siempre hay una tabla, y siempre sale un token de ella",
        "html": dg.sin_salida_no_se(),
    },

    {
        "kind": "statement",
        "text": "Una alucinación no es una avería: es el mecanismo funcionando "
                "<em>exactamente como fue diseñado</em>.",
        "after": "Aplicado a un caso donde no había nada que anclara la predicción. "
                 "El modelo no tiene forma de notar la diferencia entre saber y no saber.",
    },

    {
        "kind": "content",
        "covers": [8],
        "eyebrow": "Qué sí funciona",
        "title": "Cuatro formas de reducirlas",
        "sub": "Ninguna es pedirle que no invente: eso es una instrucción más "
               "compitiendo con el resto del contexto.",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Dale la información</div>
            <div class="d">Si el dato está en el prompt, la predicción tiene dónde
            anclarse. Es la palanca más grande con diferencia.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Exige la fuente</div>
            <div class="d">Pídele que señale de dónde salió cada afirmación. Si no puede
            señalarla, no la tenía.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Valida por código</div>
            <div class="d">Comprueba lo que devuelve contra tus datos antes de usarlo.
            Que el formato sea correcto no dice nada del contenido.</div></div>
          <div class="card"><div class="k">04</div><div class="t">Deja salida para «no sé»</div>
            <div class="d">Si el formato obliga a llenar un campo, el modelo lo va a
            llenar. Dale siempre una opción de abstenerse.</div></div>
        </div>""",
    },

    {
        "kind": "content",
        "covers": [9],
        "eyebrow": "Un caso aparte",
        "title": "Los modelos de razonamiento",
        "html": """
        <div class="box big">
          <p>No usan un mecanismo distinto. <b>Generan más tokens antes de dar la
          respuesta final</b>, y ese texto intermedio entra como entrada de los tokens
          siguientes. Es el mismo bucle, dándose más vueltas a sí mismo.</p>
        </div>
        <ul class="pts tight" style="margin-top:7mm">
          <li><b>Esos tokens se facturan</b> aunque no aparezcan en la respuesta, y
            suelen ser varias veces más largos que ella.</li>
          <li><b>La latencia sube</b> de forma notable: todo eso se genera antes de que
            veas la primera palabra.</li>
          <li><b>Pedirle «razona paso a paso» puede empeorar el resultado</b>, porque
            interfiere con el proceso que ya hace por su cuenta.</li>
        </ul>""",
    },

    {
        "kind": "content",
        "covers": [10],
        "eyebrow": "Cierre",
        "title": "Siete comportamientos que ahora se explican solos",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Inventa citas</div>
            <div class="d">Una cita tiene una forma muy predecible.</div></div>
          <div class="card"><div class="k">02</div><div class="t">No sabe cuándo no sabe</div>
            <div class="d">No hay un estado interno de incertidumbre.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Falla en aritmética</div>
            <div class="d">Los números se parten en tokens y no hay calculadora dentro.</div></div>
          <div class="card"><div class="k">04</div><div class="t">El orden cambia la respuesta</div>
            <div class="d">Por cómo pondera la atención.</div></div>
          <div class="card"><div class="k">05</div><div class="t">No recuerda nada</div>
            <div class="d">Los pesos están congelados.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Responde distinto dos veces</div>
            <div class="d">Porque se sortea un token de la tabla.</div></div>
          <div class="card"><div class="k">07</div><div class="t">Se degrada con prompts largos</div>
            <div class="d">La señal útil se diluye entre el ruido.</div></div>
          <div class="card no"><div class="k">CLAVE</div><div class="t">Ninguna se memoriza</div>
            <div class="d">Las siete salen de la operación única.</div></div>
        </div>""",
    },

]


NOTES = [
    {
        "lead": "Módulo 4 · Cómo razona un LLM — láminas 1 a 14.",
        "rows": [
            ("2", "Abre por la promesa. La sesión resuelve una tensión, no expone un "
                  "temario."),
            ("5", "<b>Encuesta real, a mano alzada, una por una.</b> Casi siempre hay "
                  "manos levantadas en varias, incluso entre desarrolladores con "
                  "experiencia. Eso convierte el resto del módulo en la resolución de "
                  "algo. No la saltes por ganar tiempo."),
            ("6–8", "El matiz va inmediatamente después del «ninguna de las cinco», o "
                    "creas un malentendido nuevo. "
                    "<span class='say'>«Un modelo no busca ni ejecuta código, pero un "
                    "sistema construido alrededor de un modelo sí puede hacer ambas "
                    "cosas.»</span>"),
            ("11", "Recorre el diagrama con el dedo, paso por paso, y detente en la "
                   "flecha de retorno: ahí es donde la gente entiende que un párrafo "
                   "son cientos de pasadas."),
            ("12", "Además de proyectarla, escribe dos o tres filas a mano en el "
                   "pizarrón. Ver aparecer los números uno a uno es lo que hace clic."),
            ("13", "El tercer punto —no hay plan— genera resistencia. Insiste: de él "
                   "se deduce casi todo lo demás."),
            ("14", "Analogía del río. Si alguien la repite después con sus palabras, "
                   "el concepto quedó."),
        ],
    },
    {
        "lead": "Láminas 15 a 29.",
        "rows": [
            ("16", "<b>Regla dura: cero matrices, cero query-key-value, cero softmax.</b> "
                   "El diagrama de alturas es suficiente. El detalle matemático no "
                   "cambia ninguna decisión que esta sala vaya a tomar."),
            ("19", "Pregunta antes de avanzar: «¿por qué creen que el modelo generaliza "
                   "a palabras que casi no vio?». La respuesta —cercanía en ese "
                   "espacio— sale sola con el diagrama delante."),
            ("22", "Enlaza con algo que ya vivieron: por qué el mismo prompt en un chat "
                   "da respuestas distintas cada vez."),
            ("24", "Diez minutos bastan. Las tres perillas se explican solas porque la "
                   "tabla lleva media hora en la conversación."),
            ("26", "<b>Núcleo del módulo.</b> Deja el diagrama en pantalla y pregunta "
                   "qué falta en él. La respuesta que buscas es la caja de abajo: no "
                   "hay una tercera salida."),
            ("28", "Menciona el costo y la latencia con orden de magnitud, sin cifras "
                   "cerradas: cambian cada pocos meses."),
            ("29", "<b>No la proyectes de entrada.</b> Constrúyela con la sala en el "
                   "pizarrón y revélala al final para comparar. Si pueden derivar las "
                   "siete solos, el módulo cumplió."),
        ],
    },
]
