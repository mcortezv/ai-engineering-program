# -*- coding: utf-8 -*-
"""Deck: Módulo 13 — RAG.

El módulo más largo del programa. La sección de similitud coseno lleva la
geometría dibujada sobre un plano cartesiano real y la demostración numérica
con los mismos números que se hacen en el pizarrón.
"""

from engine.diagrams import mod13 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 13 · RAG",
    "footer": "Programa de AI · Módulo 13",
    "outfile": "Modulo 13 - RAG.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 13  ·  4 HORAS",
        "title": "Recuperación aumentada",
        "tagline": "Buscar por significado y pegar lo encontrado en el prompt. La "
                   "sesión más larga del programa.",
        "meta": [
            "<b>Antes de esta sesión:</b> qué es un embedding y qué se calcula con él",
            "<b>Al terminar:</b> diseñas la recuperación y sabes por qué falla "
            "cuando falla",
        ],
    },

    {
        "kind": "statement",
        "text": "El modelo <em>no recibe vectores</em>. Recibe texto, igual que "
                "siempre.",
        "after": "Toda la ganancia está en cómo se decide qué texto pegar. Eso es lo "
                 "que vamos a construir hoy.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>El flujo completo</b> — qué pasa una vez y qué pasa en cada
            consulta.</li>
          <li><b>Trocear</b> — la decisión que más afecta a la calidad.</li>
          <li><b>La pregunta central</b> — si el modelo recibe texto, ¿para qué
            sirven los vectores?</li>
          <li><b>La similitud coseno, en detalle</b> — qué mide exactamente, y las
            tres métricas comparadas.</li>
          <li><b>Del prototipo al sistema</b> — búsqueda híbrida, reordenamiento y
            reproceso.</li>
          <li><b>Cuándo no usarlo</b> — cuatro casos donde es la herramienta
            equivocada.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "El flujo completo",
        "note": "Dos fases. Confundirlas es el error más común al aprender esto.",
    },

    {
        "kind": "content", "covers": [1, 2],
        "eyebrow": "Las dos fases",
        "title": "Una ocurre una vez, la otra en cada consulta",
        "html": dg.flujo_rag(),
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "La decisión que más afecta a la calidad",
        "title": "Trocear: el compromiso, y el solapamiento",
        "html": dg.chunking(),
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Tres recomendaciones",
        "title": "Valen más que cualquier número mágico",
        "html": """
        <ul class="pts">
          <li><b>Corta por estructura, no por longitud.</b>
            <span class="n">Un corte en un límite de sección o de párrafo produce
            trozos coherentes. Cortar cada N caracteres parte frases a la
            mitad.</span></li>
          <li><b>Usa solapamiento.</b>
            <span class="n">Repetir el final del trozo anterior al principio del
            siguiente evita que una idea que cae justo en el corte se pierda.
            Cuesta almacenamiento y casi siempre es rentable.</span></li>
          <li><b>Enriquece el trozo con su contexto.</b>
            <span class="n">Anteponer el título del documento y la ruta de
            secciones mejora mucho la recuperación: el vector incorpora de qué va
            el documento y no solo el párrafo suelto.</span></li>
        </ul>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "La pregunta central",
        "note": "Si hay que traducir los vectores de vuelta a texto, ¿para qué "
                "sirven?",
    },

    {
        "kind": "content", "covers": [4, 5],
        "eyebrow": "La respuesta, despacio",
        "title": "No mejoran la comunicación: mejoran la búsqueda",
        "html": """
        <div class="box ok big">
          <p class="lab">Lo que NO hacen</p>
          <p>Los vectores <b>no mejoran cómo hablas con el modelo</b>. El modelo
          recibe exactamente lo mismo que recibiría si pegaras el texto a mano.</p>
        </div>
        <div class="box big" style="margin-top:6mm">
          <p class="lab">Lo que SÍ hacen</p>
          <p>Mejoran <b>cómo se decide qué texto pegar</b>. Toda la ganancia está en
          la fase de búsqueda, no en la de generación.</p>
        </div>
        <p class="sub" style="margin-top:7mm">Sin esto, todo lo que sigue se
        entiende al revés. Con esto, se entiende solo.</p>""",
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "Dos formas de buscar",
        "title": "Ninguna de las dos gana en todo",
        "html": """
        <table>
          <thead><tr><th style="width:26%"></th><th style="width:34%">Por coincidencia de texto</th>
          <th>Por significado</th></tr></thead>
          <tbody>
            <tr><td><b>Compara</b></td><td>Caracteres y palabras</td>
              <td>Posiciones en un espacio</td></tr>
            <tr><td><b>Encuentra sinónimos</b></td><td>No</td><td>Sí</td></tr>
            <tr><td><b>Encuentra un código exacto</b></td><td>Sí, perfectamente</td>
              <td>Mal: un código no tiene significado</td></tr>
            <tr><td><b>Se puede explicar</b></td><td>Sí: se ve qué palabra coincidió</td>
              <td>No directamente: solo hay un número</td></tr>
            <tr><td><b>Jerga interna y siglas</b></td><td>Bien, si coinciden</td>
              <td>Puede fallar si el modelo no las conoce</td></tr>
          </tbody>
        </table>
        <div class="box" style="margin-top:6mm">
          <p>Los casos donde la coincidencia de texto gana son reales y frecuentes:
          <b>códigos de producto, nombres propios, siglas internas, números de
          factura.</b></p>
        </div>""",
    },

    # ── 03 ═══ el corazón del módulo ══════════════════════════════════════
    {
        "kind": "section", "step": "03",
        "title": "La similitud coseno",
        "note": "La parte más detallada del programa. Aquí conviene ir despacio.",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "La geometría",
        "title": "Lo que mide es la abertura entre dos flechas",
        "html": dg.coseno_geometria(),
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "La definición",
        "title": "En símbolos y en palabras",
        "html": """
        <pre>                     A · B
  similitud(A, B) = ───────────  =  cos(θ)
                    ‖A‖ · ‖B‖

  A · B   = suma de los productos componente a componente
  ‖A‖     = longitud del vector A</pre>
        <div class="box big" style="margin-top:7mm">
          <p><b>En palabras, que es la versión que hay que llevarse:</b> mide si dos
          vectores apuntan en la misma dirección, sin importar cuán largos sean.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "La demostración",
        "title": "Alineados del todo, y separados a la vez",
        "html": dg.coseno_demo(),
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Por qué se usa esta y no la otra",
        "title": "Ignorar la magnitud es exactamente lo que se quiere",
        "html": """
        <ul class="pts">
          <li><b>B apunta en la misma dirección que A, solo que más lejos.</b>
            <span class="n">Si la dirección codifica el tema, los dos hablan de lo
            mismo.</span></li>
          <li><b>Y la magnitud depende de cosas que no te interesan.</b>
            <span class="n">Como la longitud del texto. Un párrafo largo y uno corto
            sobre el mismo asunto no deberían dejar de parecerse por eso.</span></li>
          <li><b>Por eso en recuperación de texto se compara la orientación.</b>
            <span class="n">No la separación entre las puntas.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "El rango real",
        "title": "No existe un umbral universal",
        "html": dg.umbral(),
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Cómo se calibra",
        "title": "Con tus datos, no con los de un tutorial",
        "html": """
        <ol class="pts">
          <li><b>Toma veinte consultas reales</b> y registra los puntajes de lo que
            resultó relevante y de lo que no.</li>
          <li><b>Elige el corte donde las dos nubes se separan.</b>
            <span class="n">Si no se separan, el problema no es el umbral: es el
            troceado o el modelo.</span></li>
          <li><b>Recalíbralo al cambiar de modelo de embeddings.</b>
            <span class="n">Cada espacio tiene su propia escala.</span></li>
        </ol>
        <div class="box" style="margin-top:6mm">
          <p><b>Alternativa más robusta que un umbral fijo:</b> recuperar siempre los
          K mejores y delegar el filtrado a un paso posterior de reordenamiento.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Hay tres, y casi todos los motores dejan elegir",
        "title": "Coseno, producto punto y distancia euclidiana",
        "html": dg.tres_metricas(),
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Un detalle que provoca errores difíciles de encontrar",
        "title": "Similitud o distancia: más alto no siempre es mejor",
        "html": """
        <div class="box danger">
          <p class="lab">El problema</p>
          <p>Algunos motores devuelven <b>similitud</b> —más alto es mejor— y otros
          devuelven <b>distancia</b> —más bajo es mejor—. Y algunos usan «distancia
          coseno», que es uno menos la similitud.</p>
        </div>
        <div class="box danger" style="margin-top:6mm">
          <p class="lab">La consecuencia</p>
          <p>Confundirlos hace que el sistema ordene los resultados <b>al revés</b> y
          recupere sistemáticamente lo menos parecido, <b>sin lanzar ningún
          error</b>.</p>
        </div>
        <p class="sub" style="margin-top:6mm">Verifícalo con un caso donde sepas la
        respuesta correcta antes de confiar en el orden.</p>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "Del prototipo al sistema",
        "note": "Lo que hay entre «funciona en mi máquina» y «funciona con el "
                "corpus real».",
    },

    {
        "kind": "content", "covers": [8, 9],
        "eyebrow": "Dos ajustes que casi siempre valen la pena",
        "title": "Búsqueda híbrida y búsqueda aproximada",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Híbrida</h3>
            <p>Si cada método gana en casos distintos, lanza los dos y fusiona los
            resultados.</p>
            <p><b>Casi siempre supera a cualquiera de los dos por separado</b>, sobre
            todo en dominios con jerga propia, códigos internos y nombres de
            producto.</p>
          </div>
          <div class="col">
            <h3>Aproximada</h3>
            <p>Comparar contra todos los vectores da el resultado exacto y no
            escala.</p>
            <p>Los índices aproximados cambian una fracción pequeña de exactitud por
            una mejora enorme de velocidad. <b>La búsqueda en producción es
            aproximada</b>, y conviene saberlo.</p>
          </div>
        </div>""",
    },

    {
        "kind": "content", "covers": [10],
        "eyebrow": "El patrón que más mejora la calidad",
        "title": "Recuperar mucho y quedarse con poco",
        "html": dg.reranking(),
    },

    {
        "kind": "content", "covers": [11],
        "eyebrow": "El costo recurrente",
        "title": "Reprocesar, y el bucle que hay que evitar",
        "html": """
        <ul class="pts">
          <li><b>Cualquier cambio en el contenido obliga a regenerar el vector de
            los trozos afectados.</b></li>
          <li><b>Cambiar de modelo obliga a reprocesar el corpus entero.</b>
            <span class="n">Presupuéstalo como gasto recurrente, no de
            arranque.</span></li>
          <li><b>Reprocesa por comparación de contenido, no por defecto.</b>
            <span class="n">Guarda una huella del texto de cada trozo y regenera
            solo los que cambiaron. La diferencia de costo es de órdenes de
            magnitud.</span></li>
        </ul>
        <div class="box danger" style="margin-top:7mm">
          <p class="lab">El bucle que vacía presupuestos</p>
          <p>Un proceso que al indexar dispara un evento que vuelve a indexar genera
          factura sin parar. <b>Detección de cambios reales y un tope por
          periodo</b>, siempre.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [12],
        "eyebrow": "Cierre",
        "title": "Cuatro casos donde es la herramienta equivocada",
        "html": """
        <div class="grid c4">
          <div class="card no"><div class="k">NO ES</div>
            <div class="t">Buscar un registro por identificador</div>
            <div class="d">Es una consulta a la base de datos. Aquí sale más caro,
            más lento y menos exacto.</div></div>
          <div class="card no"><div class="k">NO ES</div>
            <div class="t">Cuando todo cabe en el contexto</div>
            <div class="d">Si son diez páginas y siempre las mismas, pegarlas es más
            simple y más confiable.</div></div>
          <div class="card no"><div class="k">NO ES</div>
            <div class="t">Contar o agregar</div>
            <div class="d">«¿Cuántos clientes hay en Jalisco?» no se responde
            recuperando trozos.</div></div>
          <div class="card no"><div class="k">NO ES</div>
            <div class="t">Datos que cambian al segundo</div>
            <div class="d">Eso es una herramienta que consulta el sistema real, no
            un índice.</div></div>
        </div>""",
    },

]


NOTES = [
    {
        "lead": "Módulo 13 · RAG — láminas 1 a 10. Cuatro horas: hay espacio para ir "
                "despacio y conviene usarlo.",
        "rows": [
            ("2", "Abre con lo que el modelo recibe. Si eso queda claro desde el "
                  "principio, la pregunta central de la lámina 10 se responde sola."),
            ("6", "<b>Dibuja las dos fases en el pizarrón antes de proyectarlas.</b> "
                  "La mitad de las preguntas del módulo se responden con ese "
                  "diagrama delante."),
            ("7", "El compromiso del troceado no tiene número correcto. Resiste dar "
                  "uno: da los tres criterios y que midan con su corpus."),
            ("10", "<b>Momento pedagógico clave.</b> Deja que la pregunta salga de la "
                   "sala antes de responderla: «si hay que traducirlo de vuelta a "
                   "texto, ¿para qué sirve?». La respuesta reordena todo el módulo."),
        ],
    },
    {
        "lead": "Láminas 12 a 19, la sección de similitud coseno. Es la parte más "
                "detallada del programa.",
        "rows": [
            ("13", "<b>La figura correcta son dos flechas desde el origen y la "
                   "abertura entre ellas.</b> Dibújala tú en el pizarrón y alarga "
                   "una de las flechas delante de ellos para que vean que el ángulo "
                   "no cambia. Ese gesto vale más que la fórmula."),
            ("14", "Da la fórmula y tradúcela inmediatamente a palabras. Nadie "
                   "necesita la fórmula para decidir nada; la necesitan para no "
                   "sentir que se les oculta algo."),
            ("15", "<b>Haz los números en el pizarrón con ellos.</b> Que salga 1.0 "
                   "de similitud y 5 de distancia sobre los mismos dos vectores es "
                   "la demostración entera. No la proyectes sin hacerla."),
            ("17", "El umbral es donde más sistemas se rompen en producción. "
                   "Insiste: se calibra con datos propios y se recalibra al cambiar "
                   "de modelo."),
            ("20", "El detalle de similitud contra distancia parece menor y produce "
                   "un fallo silencioso que puede tardar meses en detectarse."),
        ],
    },
    {
        "lead": "Láminas 21 a 26.",
        "rows": [
            ("23", "El reordenamiento es de las poquísimas optimizaciones sin "
                   "contrapartida. Merece énfasis: baja el costo y sube la calidad "
                   "a la vez."),
            ("24", "El bucle de reproceso no es teórico. Si alguien de la sala ha "
                   "vivido uno, deja que lo cuente."),
            ("25", "Cierra con los cuatro casos donde no se usa. Evita que salgan "
                   "queriendo aplicarlo a todo, que es el efecto habitual de una "
                   "sesión de cuatro horas sobre un tema."),
        ],
    },
]
