# -*- coding: utf-8 -*-
"""Anexo de correcciones respecto al borrador base.

RETIRADO del documento a peticion del autor. Este archivo NO se importa
desde build_syllabus.py, asi que su contenido no aparece en el PDF.
Para volver a incluirlo: importarlo en build_syllabus.build_document() y
anadir ANEXO_CORRECCIONES a la lista ANEXOS de syllabus_anexos.py.
"""

ANEXO_CORRECCIONES = {
    "title": "Anexo B · Registro de correcciones respecto al borrador base",
    "blocks": [
        ("lead", "Cada cambio de fondo respecto al documento «Programa de AI» "
                 "original, con la afirmación tal como estaba, por qué se modificó y cómo "
                 "quedó. El objetivo es que los cambios se puedan auditar uno por uno."),

        ("h2", "B.1 · Correcciones críticas"),

        "Tres afirmaciones del borrador eran técnicamente incorrectas y podían producir "
        "aprendizaje erróneo. Se detallan aparte porque merecen revisión atenta.",

        ("h3", "B.1.1 · La similitud coseno no calcula una hipotenusa"),

        ("box", "alerta", "Texto del borrador", [
            "«Se utiliza una función trigonométrica que se llama coseno, porque para los "
            "que saben geometría y trigonometría el coseno te saca la hipotenusa y el cateto "
            "adyacente.»",
        ]),

        "**Por qué es incorrecto.** El coseno de un ángulo es la razón entre el cateto "
        "adyacente y la hipotenusa en un triángulo rectángulo. No «saca» ninguno de "
        "los dos: es un cociente entre ellos. Y, sobre todo, esa no es la operación que se "
        "realiza al comparar dos embeddings. La similitud coseno entre dos vectores es el "
        "producto punto dividido entre el producto de sus magnitudes, y lo que devuelve es el "
        "coseno del ángulo que forman: una medida de **orientación**.",

        "**Cómo quedó.** El módulo 13 desarrolla la definición correcta, con la fórmula, la "
        "explicación en palabras, la figura geométrica adecuada —dos flechas desde el origen "
        "y la abertura entre ellas, no un triángulo rectángulo— y una demostración numérica.",

        ("h3", "B.1.2 · La similitud coseno no devuelve una distancia euclidiana"),

        ("box", "alerta", "Texto del borrador", [
            "«...ya con eso la función de coseno nos puede devolver la distancia "
            "euclidiana que hay entre los embeddings.»",
        ]),

        "**Por qué es incorrecto.** Son dos medidas distintas y pueden discrepar por "
        "completo. La distancia euclidiana mide separación y es sensible a la magnitud de los "
        "vectores; la similitud coseno mide orientación y la ignora. El contraejemplo que se "
        "usa en el módulo 13: los vectores (3, 4) y (6, 8) tienen similitud coseno 1.0 —la "
        "máxima posible— y una distancia euclidiana de 5. Están alineados y separados a la "
        "vez.",

        "**Cómo quedó.** El módulo 13 incluye una sección propia que compara las tres "
        "métricas de uso habitual, explica el matiz de que con vectores normalizados las tres "
        "producen el mismo orden, y advierte sobre motores que devuelven distancia en lugar "
        "de similitud, un error que hace que el sistema ordene los resultados al revés sin "
        "lanzar ninguna excepción.",

        ("h3", "B.1.3 · Las alucinaciones no se originan en la ventana de contexto"),

        ("box", "alerta", "Texto del borrador", [
            "«...explicar de forma sencilla por qué un modelo alucina en base a la "
            "ventana de contexto.»",
        ]),

        "**Por qué es incorrecto.** La causa es el mecanismo de generación: el modelo siempre "
        "produce una distribución de probabilidad y siempre se muestrea un token de ella. No "
        "existe un estado interno de «no lo sé» que interrumpa la generación. La "
        "ventana de contexto es un **agravante** real —si la información no está en el "
        "prompt, no hay nada que ancle la predicción— pero no es el origen.",

        "**Cómo quedó.** La explicación se movió al módulo 4, donde ya está el mecanismo "
        "sobre la mesa, con la ventana de contexto presentada como factor de riesgo.",

        ("h2", "B.2 · Correcciones de precisión"),

        ("table",
         ["Dónde", "Qué decía el borrador", "Cómo quedó"],
         [
             ["Módulo 1",
              "«Redes convolucionales», listado junto a AI tradicional y generativa "
              "sin delimitar.",
              "Se mantiene la mención pero se cierra explícitamente: es la arquitectura de "
              "visión por computadora; los modelos de lenguaje usan Transformers y su "
              "mecanismo es la atención. Evita que se asocien ambas cosas."],
             ["Módulo 2",
              "«¿Por qué no es posible tener un modelo propio?»",
              "Se precisa: lo inviable es **entrenar un modelo base desde cero**. Hospedar un "
              "modelo de pesos abiertos o adaptarlo con fine tuning sí es posible, y el "
              "módulo 20 lo desarrolla. Sin este matiz, el módulo 2 contradice al 20."],
             ["Módulo 11",
              "«Comenzando con las bases de datos vectoriales que nos permiten guardar "
              "contexto por temas o por áreas... si yo sé que un nodo corresponde al tema que "
              "necesito», y después «ahí sí escalar a las bases de datos "
              "vectoriales».",
              "El primer caso describe **bases de datos de grafos** —habla de nodos, temas y "
              "áreas—. Se corrige el nombre. La escalera del borrador se conserva intacta: "
              "tradicional → grafos → vectorial."],
             ["Módulo 12",
              "Subtema «distancia euclidiana para embedding».",
              "Se reformula como «operaciones sobre vectores: magnitud, distancia y "
              "ángulo». Presentar solo la distancia aquí prepara mal el módulo 13, donde "
              "el error central era confundir la similitud coseno con una distancia."],
             ["Módulos 4 y 12",
              "El borrador no distingue los embeddings internos del modelo de los embeddings "
              "de recuperación.",
              "Se añade la distinción explícita en el módulo 4 y se cierra en el 12. El "
              "propio borrador identifica esta confusión como un error que su autor cometió "
              "al empezar."],
             ["Módulo 19",
              "«Style encoder» como alternativa al system prompt.",
              "Se precisa que es un término de síntesis de voz, imagen y transferencia de "
              "estilo, y que en modelos de lenguaje por API no existe un componente con ese "
              "nombre. Se sustituye por las cuatro formas reales de controlar el estilo, "
              "conservando la intención original."],
             ["Módulo 19",
              "La latencia geográfica «se resuelve por CDN o infraestructura propia».",
              "Se matiza: una CDN cachea contenido estático, y la inferencia no lo es. Lo que "
              "reduce la latencia geográfica es elegir la región del proveedor más cercana. "
              "La CDN sí ayuda con todo lo que rodea a la llamada."],
             ["Módulo 18",
              "Prompt injection tratado solo como manipulación directa del usuario.",
              "Se añade la **inyección indirecta** —instrucciones ocultas en contenido "
              "recuperado o en respuestas de herramientas—, que es la forma peligrosa en "
              "sistemas agénticos, y se dice explícitamente que no tiene defensa completa."],
         ],
         [2.6, 6.2, 7.7]),

        ("h2", "B.3 · Cambios de estructura"),

        ("table",
         ["Cambio", "Dónde estaba", "Dónde está", "Motivo"],
         [
             ["Módulo «Cómo razona un LLM»", "No existía", "Módulo 4",
              "Sin el mecanismo, todo lo posterior se aprende como recetas imposibles de "
              "depurar."],
             ["Prompt engineering", "Disperso, sobre todo dentro de agentes", "Módulo 5",
              "El prompt es la única interfaz con el modelo y todo lo posterior es un "
              "prompt."],
             ["Temperatura, top-p y top-k", "Conceptos básicos", "Módulo 4",
              "Son parámetros sobre una distribución de probabilidad. Antes de explicarla se "
              "enseñan como perillas mágicas."],
             ["Fine tuning", "Al final, en conceptos avanzados",
              "Módulos 6 y 20",
              "El mito que hay que romper aparece el primer día. El módulo 6 lo desmitifica y "
              "el 20 conserva todo el detalle técnico."],
             ["MCP", "Dentro de agentes, junto a skills", "Módulo 10",
              "Es un protocolo de comunicación y se entiende mejor comparado con REST y "
              "webhooks. Se coloca después de agentes porque resuelve un problema que sin "
              "agentes no existe."],
             ["Agentes", "Una sola secuencia con herramientas concretas",
              "Módulo 9, partido en 9.1 y 9.2",
              "Separa lo conceptual, que dura, de lo que caduca con los productos. La 9.2 "
              "está marcada como sección volátil."],
             ["Observabilidad", "Una viñeta en conceptos avanzados", "Módulo 16",
              "Decide si un sistema se puede operar o solo lanzar. La lista de lo que hay que "
              "registrar no cabe en una viñeta."],
             ["Costos", "Mencionado dentro de varios módulos", "Módulo 14",
              "Las fuentes de gasto solo se pueden comparar entre sí en un mismo lugar, y "
              "hace falta un cálculo completo de principio a fin."],
             ["Orquestación", "Antes de costos", "Después de costos, módulo 15",
              "Su argumento central es que menos contexto es más preciso y más barato. Con "
              "los costos ya vistos, se sostiene con números."],
         ],
         [3.8, 3.9, 3.2, 5.6]),

        ("h2", "B.4 · Ortografía y terminología"),

        "El borrador base alterna varias grafías del mismo término. En esta versión se "
        "unifican:",

        ("table",
         ["En el borrador", "Forma unificada"],
         [
             ["embedings · enbeddings · enbedding · embeddigns", "embedding / embeddings"],
             ["guardriels", "guardrails"],
             ["promt · promtp", "prompt"],
             ["tolos", "tools / herramientas"],
             ["semantica", "semántica"],
             ["Orquestacion", "Orquestación"],
             ["reraking", "reranking / reordenamiento"],
             ["style enconder", "style encoder (y ver B.2, módulo 19)"],
             ["incapie", "hincapié"],
         ],
         [8.0, 8.5]),

        ("h2", "B.5 · Propuestas de la retro que se descartaron"),

        "Se registran para dejar constancia de que la omisión fue una decisión y no un "
        "olvido, por si en una revisión futura se quiere reconsiderar alguna.",

        ("table",
         ["Propuesta", "Estado", "Consecuencia en el documento"],
         [
             ["Replantear el bloque de bases de datos como «¿qué queremos "
              "almacenar?», presentando SQL, documental, vectorial y grafos como "
              "herramientas paralelas en lugar de una escalera.",
              "Descartada",
              "El módulo 11 conserva íntegra la narrativa escalonada del borrador. Solo se "
              "corrigió la errata de grafos por vectoriales."],
             ["Invertir el orden para ver embeddings antes que bases de datos.",
              "Descartada",
              "Embeddings sigue después, en el módulo 12. Se mitigó con un cierre explícito "
              "en el módulo 11 que anuncia que el tema llega en el siguiente."],
             ["Añadir un módulo completo de evaluación de sistemas de AI: precisión, "
              "exhaustividad, conjuntos de referencia, evaluación automática y humana.",
              "Descartada",
              "No aparece. Se dejó una nota explícita al cerrar el módulo 16 señalando que "
              "una traza dice qué pasó pero no si estuvo bien, para que la ausencia sea "
              "visible."],
             ["Añadir un módulo final de arquitecturas reales, desarmando productos "
              "conocidos del mercado.",
              "Descartada",
              "No aparece. El módulo 17 cierra con un ejemplo de arquitectura limpia, que "
              "cubre parcialmente la misma función."],
         ],
         [5.6, 2.4, 8.5]),

        ("box", "nota", "Una aclaración sobre la palabra «evaluación»", [
            "El formato de este documento incluye una sección de **criterios de evaluación** "
            "en cada módulo. Eso se refiere a cómo se comprueba que la persona participante "
            "alcanzó el objetivo de aprendizaje.",
            "No tiene relación con el módulo de **evaluación de sistemas de AI** que se "
            "descartó, que trataría de cómo medir la calidad de un sistema en producción.",
        ]),
    ],
}
