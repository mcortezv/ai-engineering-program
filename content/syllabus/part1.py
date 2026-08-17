# -*- coding: utf-8 -*-
"""Parte I — Fundamentos (módulos 1 a 4)."""


M1 = {
    "num": 1,
    "title": "Introducción",
    "tagline": "Dónde encaja la AI entre todas las formas que ya conocemos de resolver un problema con código.",
    "objetivo": "Situar la AI generativa dentro del panorama del software y explicar en qué "
                "se diferencia de otras formas de resolver problemas con código.",
    "duracion": "1.5 horas",
    "dependencias": "Ninguna. Es el módulo de entrada.",
    "contenidos": [
        "¿Qué es la inteligencia artificial? Delimitación del término frente a su uso comercial.",
        "AI tradicional frente a AI generativa: predecir o clasificar frente a generar.",
        ("Tres formas de resolver un problema con código", [
            "Programación determinista: se conocen todos los parámetros y existe una operación definida.",
            "Heurística: no se conocen todos los parámetros, pero se puede diseñar una regla razonable.",
            "Aprendizaje automático: no hay regla y se delega en el entrenamiento encontrarla.",
        ]),
        "Aprendizaje supervisado y no supervisado, en una frase cada uno.",
        "Un vistazo rápido a las redes convolucionales, y por qué este programa no va sobre ellas.",
        "Mapa del programa: qué se va a construir y en qué orden.",
    ],
    "enfoque": [
        ("sub", "El eje del módulo: la pregunta «por qué delegar»"),

        "La idea que estructura toda la sesión es la que ya estaba en el temario base y "
        "conviene conservar tal cual, porque es la mejor puerta de entrada que existe para "
        "un público de desarrolladores: la AI no es una tecnología aparte, es el tercer "
        "punto de una escala que ya se recorre todos los días al programar.",

        "Se propone presentarla con un problema único que se resuelve tres veces:",

        ("bullets", [
            "**Determinista.** Convertir grados Celsius a Fahrenheit. Se conocen todos los "
            "parámetros y existe una fórmula exacta. Escribir una red neuronal para esto "
            "sería absurdo, y decirlo en voz alta ya inocula contra el reflejo de meter AI "
            "en todas partes.",
            "**Heurística.** Decidir si un correo es spam usando reglas escritas a mano: "
            "contiene ciertas palabras, viene de cierto dominio, tiene demasiados enlaces. "
            "No hay una fórmula exacta, pero una persona puede diseñar un criterio que "
            "acierta la mayoría de las veces. El código sigue siendo legible y la razón de "
            "cada decisión es explícita.",
            "**Aprendizaje automático.** El mismo problema del spam, pero mostrando al "
            "sistema cien mil correos ya etiquetados y dejando que él encuentre el patrón. "
            "Nadie escribió la regla. La regla existe, pero está codificada en números y no "
            "se puede leer.",
        ]),

        "El salto interesante es el tercero, y conviene nombrarlo explícitamente: **lo que se "
        "delega no es el cálculo, es el diseño de la regla.** Ese es el intercambio central "
        "de todo el campo. Se gana la capacidad de resolver problemas cuya regla nadie sabe "
        "escribir, y se pierde la posibilidad de leer por qué el sistema decidió lo que "
        "decidió. Todo lo que se verá después en observabilidad, en evaluación de resultados "
        "y en seguridad existe porque se hizo ese intercambio.",

        ("sub", "AI tradicional frente a generativa"),

        "La distinción práctica que hay que dejar clara es la del tipo de salida. Un modelo "
        "de AI tradicional produce una etiqueta o un número: esto es spam, esta casa vale "
        "tanto, esta imagen contiene un gato. Un modelo generativo produce contenido nuevo "
        "que no estaba en los datos: un texto, una imagen, código.",

        "Conviene desactivar de entrada la idea de que lo generativo sustituyó a lo "
        "tradicional. No lo hizo. En la mayoría de los sistemas que se construyen en la "
        "práctica conviven: un clasificador barato y determinista decide el enrutamiento, y "
        "solo lo que realmente lo necesita llega al modelo generativo, que es varios órdenes "
        "de magnitud más caro. Esa idea vuelve en el módulo 17 como una de las buenas "
        "prácticas centrales, así que sembrarla aquí ahorra trabajo después.",

        ("sub", "Redes convolucionales: mencionarlas y seguir"),

        ("box", "correccion", "Ajuste respecto al borrador base", [
            "El temario base incluye «redes convolucionales» en la introducción, "
            "junto a la distinción entre AI tradicional y generativa. Merece una precisión, "
            "porque tal como está puede sugerir que los modelos de lenguaje son "
            "convolucionales, y no lo son.",
            "Las redes convolucionales son la arquitectura que dominó el procesamiento de "
            "imágenes durante la década pasada. Los modelos de lenguaje de los que trata "
            "este programa usan una arquitectura distinta, el **Transformer**, y su "
            "mecanismo central es la atención, no la convolución. Se recomienda mantener la "
            "mención, porque es útil para explicar qué había antes y que el campo tiene "
            "historia, pero cerrándola de forma explícita: *esto es lo que se usaba y se "
            "sigue usando para visión; el resto del programa va sobre otra cosa*.",
        ]),

        "Dedicarle cinco minutos es suficiente. La función de esta mención es evitar que "
        "alguien salga creyendo que «AI» y «modelo de lenguaje» son "
        "sinónimos, no enseñar visión por computadora.",

        ("sub", "Cerrar con el mapa"),

        "Los últimos quince minutos conviene dedicarlos a mostrar el mapa del programa "
        "completo: las cinco partes y la pregunta que responde cada una. Sirve para que la "
        "gente sepa que los temas que va a echar de menos en las primeras sesiones —costo, "
        "seguridad, memoria— sí están, y en qué momento llegan. Reduce mucho la ansiedad de "
        "«y esto cómo se paga» en la sesión tres.",
    ],
    "ejercicio": [
        "En parejas, tomar tres funcionalidades reales de un producto de la empresa y "
        "clasificar cada una en determinista, heurística o aprendizaje automático. Para cada "
        "una, escribir una frase justificando por qué **no** correspondería a las otras dos "
        "categorías.",
        "La discusión buscada es la de los casos límite: casi siempre aparece alguna "
        "funcionalidad que hoy se resuelve con AI y que en realidad sería más barata, más "
        "rápida y más confiable como heurística. Ese hallazgo es el objetivo real del "
        "ejercicio.",
    ],
    "evaluacion": [
        "Distingue las tres formas de resolver un problema y justifica la elección con el "
        "criterio de «qué se conoce y qué no se conoce», no con «cuál es más "
        "moderna».",
        "Explica el intercambio del aprendizaje automático: se gana capacidad, se pierde "
        "explicabilidad.",
        "No confunde AI generativa con AI en general, ni redes convolucionales con modelos "
        "de lenguaje.",
    ],
}


M2 = {
    "num": 2,
    "title": "Qué es un LLM",
    "tagline": "El objeto con el que se va a trabajar durante todo el programa: qué contiene, quién lo fabrica y cuánto cuesta hacerlo.",
    "objetivo": "Describir qué es un modelo de lenguaje como artefacto: qué son sus "
                "parámetros, quién los produce, qué cuesta producirlos y qué hace que uno "
                "sea mejor que otro.",
    "duracion": "1.5 horas",
    "dependencias": "Módulo 1.",
    "contenidos": [
        "¿Qué es un modelo de lenguaje grande?",
        "¿A qué se refieren los miles de millones de parámetros de un modelo?",
        "El costo real de entrenar un modelo desde cero: cómputo, datos, energía y agua.",
        "Por qué prácticamente ninguna empresa entrena su propio modelo base, y qué sí puede hacer en su lugar.",
        "El panorama de proveedores: modelos cerrados por API y modelos de pesos abiertos.",
        "Qué hace mejor o peor a un modelo: capacidad, velocidad, ventana de contexto, precio y comportamiento.",
        "Por qué los benchmarks públicos informan poco sobre el caso de uso propio.",
    ],
    "enfoque": [
        ("sub", "Los parámetros, sin misticismo"),

        "La pregunta «¿a qué se refieren los millones de parámetros?» es la mejor "
        "del módulo y merece una respuesta concreta en lugar de una analogía vaga. Un "
        "parámetro es un número decimal. Nada más. Un modelo es un archivo enorme lleno de "
        "esos números, organizados en matrices, más el código que sabe en qué orden "
        "multiplicarlos.",

        "La cuenta que conviene hacer en el pizarrón, porque aterriza el concepto mejor que "
        "cualquier explicación: si un parámetro ocupa dos bytes, un modelo de 70 mil millones "
        "de parámetros son unos 140 gigabytes solo de números. Esa cifra explica de golpe por "
        "qué no cabe en una laptop, por qué la inferencia necesita hardware específico y por "
        "qué el servicio se cobra por uso.",

        "Y hay una segunda idea que conviene sembrar aquí porque se cosecha en el módulo 4: "
        "esos números no son datos, son **pesos**. No hay dentro del archivo una copia de la "
        "Wikipedia que se pueda consultar. Hay una configuración de multiplicaciones que, "
        "aplicada a un texto de entrada, tiende a producir continuaciones plausibles. La "
        "diferencia entre «guardar información» y «haber ajustado unos "
        "números hasta que las continuaciones salen bien» es sutil y es exactamente "
        "donde nace la confusión que el módulo 4 va a desmontar.",

        ("sub", "El costo de entrenar, y qué se hace con ese dato"),

        "Este es el punto donde el temario base propone hablar de consumo de agua y "
        "equivalencias en CO2, y es un buen instinto: convierte una cifra abstracta en algo "
        "discutible. Conviene mantenerlo con dos cuidados.",

        "El primero es de precisión. Las cifras de consumo energético e hídrico del "
        "entrenamiento de modelos frontera varían enormemente según la fuente, el centro de "
        "datos y la metodología, y se han vuelto un terreno de disputa. Se recomienda "
        "presentarlas como órdenes de magnitud con la fuente citada y la fecha, no como "
        "datos cerrados, y actualizarlas antes de cada impartición.",

        "El segundo es de encuadre. El dato interesante para un equipo de producto no es el "
        "costo del entrenamiento, que nadie de la sala va a pagar, sino el del **uso**: la "
        "inferencia se paga cada vez, para siempre, y ese es el número que va a aparecer en "
        "la factura. Conviene decir explícitamente que el módulo 14 se dedica entero a eso y "
        "usar esta sesión solo para dimensionar por qué existen tan pocos proveedores.",

        ("sub", "«¿Por qué no es posible tener un modelo propio?»"),

        ("box", "correccion", "Matiz respecto al borrador base", [
            "El temario base plantea la pregunta como «¿por qué no es posible tener un "
            "modelo propio?». La intuición es correcta pero la formulación se ha "
            "quedado corta, y conviene precisarla porque de lo contrario contradice al "
            "módulo 20.",
            "Lo que es inviable para prácticamente cualquier empresa es **entrenar un modelo "
            "base desde cero**: requiere miles de GPUs durante meses, un corpus de datos a "
            "escala de internet y un equipo de investigación. Eso está fuera de alcance y "
            "seguirá estándolo.",
            "Lo que sí es perfectamente posible, y cada vez más barato, es **descargar un "
            "modelo de pesos abiertos y hospedarlo**, o **adaptarlo con fine tuning**. La "
            "formulación recomendada es: *no vas a entrenar un modelo base, pero sí puedes "
            "tener uno tuyo corriendo en tu infraestructura, y el módulo 20 explica cuándo "
            "eso tiene sentido y cuánto cuesta de verdad*.",
        ]),

        ("sub", "El panorama, presentado por criterios y no por marcas"),

        "El mercado de proveedores es la parte del módulo que más rápido caduca. La forma de "
        "que no envejezca es enseñar los **ejes de decisión** en lugar de una tabla de "
        "productos, y dejar la tabla como anexo actualizable.",

        ("table",
         ["Eje", "Qué preguntar", "Por qué importa"],
         [
             ["Capacidad", "¿Resuelve la tarea con la calidad que necesito?",
              "Es condición necesaria, pero casi nunca es el criterio que decide."],
             ["Precio por token", "¿Cuánto cuestan la entrada y la salida por separado?",
              "La salida suele costar varias veces más que la entrada. Se detalla en el módulo 14."],
             ["Latencia", "¿Cuánto tarda el primer token y cuánto la respuesta completa?",
              "Determina si sirve para una interfaz interactiva o solo para procesos de fondo."],
             ["Ventana de contexto", "¿Cuánto texto acepta de una vez?",
              "Condiciona la arquitectura de contexto completa del sistema."],
             ["Comportamiento", "¿Sigue instrucciones? ¿Se niega de más? ¿Respeta formatos?",
              "Es lo que más se nota en producción y lo que menos aparece en los benchmarks."],
             ["Modalidad", "¿Acepta imágenes, audio, documentos?",
              "Amplía o cierra casos de uso completos."],
             ["Despliegue", "¿Solo por API, o se pueden descargar los pesos?",
              "Decide si el dato sale de la infraestructura propia. A veces es un requisito legal."],
         ],
         [3.0, 5.5, 8.0]),

        "Sobre los benchmarks conviene ser directo: son útiles para descartar modelos "
        "claramente insuficientes y poco más. Un modelo puede liderar una tabla pública y "
        "comportarse peor que otro en la tarea concreta que se necesita, porque esa tarea no "
        "se parece a lo que mide el benchmark. La recomendación práctica que hay que dar es "
        "la misma que se repite en el módulo 20: **armar veinte casos propios y probarlos**. "
        "Veinte ejemplos reales informan más que cualquier tabla comparativa.",
    ],
    "ejercicio": [
        "Elegir una funcionalidad concreta que el equipo quiera construir y llenar la tabla "
        "de ejes de decisión para tres modelos distintos, uno de ellos de pesos abiertos. "
        "Los precios y las capacidades hay que buscarlos en la documentación oficial del "
        "proveedor durante la sesión, no de memoria.",
        "Al final, cada equipo defiende su elección en dos minutos. La única respuesta "
        "inaceptable es «porque es el mejor» sin referencia a un eje.",
    ],
    "evaluacion": [
        "Explica qué es un parámetro y por qué el tamaño del modelo condiciona dónde puede ejecutarse.",
        "Distingue entrenar un modelo base, hospedar un modelo abierto y adaptar un modelo existente.",
        "Elige un modelo justificándolo con al menos tres ejes distintos, no solo con capacidad.",
        "Reconoce que un benchmark público no predice el desempeño en un caso de uso concreto.",
    ],
}


M3 = {
    "num": 3,
    "title": "Conceptos básicos: tokens y ventana de contexto",
    "tagline": "Las dos unidades con las que se mide todo lo demás: lo que el modelo lee y lo que cabe.",
    "objetivo": "Manejar con soltura las dos unidades operativas de un sistema de AI —el "
                "token y la ventana de contexto— y usarlas para estimar consumo.",
    "duracion": "2 horas",
    "dependencias": "Módulos 1 y 2.",
    "contenidos": [
        "¿Qué es un token? Por qué el modelo no lee ni palabras ni letras.",
        "Tokenización en la práctica: cómo se parten las palabras y por qué el español gasta más tokens que el inglés.",
        "El token como unidad de medida y como unidad de cobro.",
        "La ventana de contexto: qué cabe y qué ocupa espacio dentro de ella.",
        "Qué pasa cuando el contexto se llena: truncado, error y degradación de la atención.",
        "Contar tokens antes de enviar: por qué es la primera herramienta de control de costo.",
    ],
    "enfoque": [
        ("box", "nota", "Cambio de ubicación respecto al borrador base", [
            "El temario base incluía en este módulo la temperatura, el top-p, el top-k y la "
            "explicación de por qué alucinan los modelos. Los cuatro temas se han movido al "
            "**módulo 4**.",
            "El motivo es que los tres primeros son parámetros que operan sobre una "
            "distribución de probabilidad, y las alucinaciones son una consecuencia de cómo "
            "se genera esa distribución. Enseñarlos aquí obliga a describirlos como perillas "
            "sin explicación —«súbele la temperatura para que sea más creativo»—, "
            "que es exactamente el tipo de conocimiento de receta que este programa intenta "
            "evitar. En el módulo 4, después de explicar el mecanismo, se entienden solos.",
        ]),

        ("sub", "Empezar por el hecho contraintuitivo"),

        "La forma más eficiente de abrir el módulo es con la afirmación desnuda: **el modelo "
        "nunca ve las palabras que se escriben.** Ve números enteros. El texto se parte en "
        "fragmentos llamados tokens y cada fragmento se sustituye por su índice en un "
        "vocabulario. Lo que entra al modelo es una lista de enteros, y lo que sale también.",

        "Esto conviene mostrarlo, no contarlo. Hay tokenizadores interactivos en la web de "
        "los principales proveedores y la biblioteca correspondiente en Python permite "
        "hacerlo en vivo. La sesión gana muchísimo si se proyecta un tokenizador y se pegan "
        "frases que la sala proponga.",

        ("sub", "Los cuatro descubrimientos que hay que provocar"),

        "Al jugar con el tokenizador en vivo aparecen cuatro hallazgos que valen más que "
        "media hora de explicación. Conviene buscarlos deliberadamente:",

        ("bullets", [
            "**Un token no es una palabra.** Las palabras frecuentes suelen ser un token "
            "entero; las raras se parten en pedazos. Un nombre propio poco común puede "
            "costar cinco o seis tokens.",
            "**El espacio pertenece al token.** Escribir una palabra al principio de una "
            "frase o en medio produce tokens distintos. Esto explica errores raros de "
            "formato que si no se sabe parecen embrujos.",
            "**El español cuesta más que el inglés.** Los vocabularios de la mayoría de los "
            "modelos están sesgados hacia el inglés, así que el mismo texto traducido gasta "
            "notablemente más tokens en español. La consecuencia es directa y hay que "
            "decirla: **el mismo producto cuesta más caro operando en español.**",
            "**Los números y el código se fragmentan de forma extraña.** Una cifra larga "
            "puede partirse en varios tokens sin lógica aparente. Esto explica por qué los "
            "modelos son históricamente malos en aritmética exacta y por qué conviene "
            "delegar los cálculos a una herramienta, idea que reaparece en el módulo 9.",
        ]),

        ("sub", "El token como unidad de cobro"),

        "Una vez que se ve el tokenizador funcionando, la conexión con el dinero es "
        "inmediata y no requiere insistencia: se cobra por token de entrada y por token de "
        "salida, con precios distintos. La regla práctica que conviene dejar apuntada, "
        "sabiendo que es una aproximación gruesa que varía por idioma y por modelo, es que "
        "**un token ronda los cuatro caracteres en inglés y algo menos en español**, y que "
        "una página de texto está en el orden de quinientos a setecientos tokens.",

        "Aquí basta con dejar la unidad clara. El desglose completo del costo —entrada "
        "contra salida, caché, razonamiento, herramientas— es el módulo 14, y anticiparlo "
        "aquí satura.",

        ("sub", "La ventana de contexto y lo que realmente ocupa"),

        "La ventana de contexto es el número máximo de tokens que el modelo puede tener "
        "presentes en una sola petición. Es el concepto que más se malinterpreta del módulo, "
        "por dos razones que conviene atacar de frente.",

        "La primera es **qué cuenta dentro de la ventana**. No es solo la pregunta del "
        "usuario. Es la suma del system prompt, las definiciones de todas las herramientas "
        "disponibles, el historial completo de la conversación, el contexto recuperado, los "
        "resultados de las herramientas ya ejecutadas y, además, la respuesta que el modelo "
        "va a generar. Enumerar esa lista en el pizarrón suele producir un momento de "
        "sorpresa, porque casi todo el mundo asume que la ventana es «para mi "
        "texto».",

        "La segunda es **qué pasa cuando se llena**, y aquí conviene ser preciso porque hay "
        "tres situaciones distintas que suelen confundirse:",

        ("table",
         ["Situación", "Qué ocurre realmente"],
         [
             ["Se excede el límite duro",
              "La API devuelve un error. No hay degradación elegante: la petición falla."],
             ["Se trunca el historial por decisión propia",
              "El sistema descarta mensajes antiguos para que quepa. El modelo no lo sabe: "
              "simplemente deja de tener esa información y actúa como si nunca hubiera existido."],
             ["Se llena de contexto irrelevante",
              "La petición funciona y cuesta más, pero la calidad baja: la información útil "
              "queda diluida entre ruido. Es el fallo más caro porque es silencioso."],
         ],
         [5.2, 11.3]),

        "El tercer caso es el importante y conviene dedicarle tiempo, porque contradice la "
        "intuición dominante. **Una ventana de contexto más grande no es automáticamente "
        "mejor.** Llenar un millón de tokens con documentos por si acaso produce respuestas "
        "peores y facturas más altas que enviar los tres párrafos que hacían falta. Esa idea "
        "es la semilla de todo el módulo 17 y de buena parte de la justificación del RAG, así "
        "que hay que dejarla plantada con claridad.",

        ("box", "nota", "Una precisión que evita un malentendido frecuente", [
            "Conviene aclarar aquí, aunque se desarrolle en el módulo 7, que la ventana de "
            "contexto **no es memoria**. No hay nada que persista entre una petición y la "
            "siguiente. La sensación de que el chat «recuerda» viene de que la "
            "aplicación reenvía el historial completo cada vez. Sin ese reenvío no hay "
            "memoria de ningún tipo.",
        ]),
    ],
    "ejercicio": [
        "Tomar el prompt real más largo que alguien del equipo tenga en producción —o, si no "
        "hay, el system prompt de cualquier herramienta interna— y medirlo con el "
        "tokenizador oficial del proveedor. Después:",
        ("bullets", [
            "Calcular cuántos tokens consume una conversación de veinte turnos reenviando el "
            "historial completo cada vez.",
            "Traducir el mismo texto al inglés, volver a medirlo y anotar la diferencia "
            "porcentual.",
            "Estimar el costo mensual asumiendo mil conversaciones al mes, con los precios "
            "vigentes del proveedor.",
        ]),
        "El resultado suele sorprender a la sala y es la mejor preparación posible para el "
        "módulo 14.",
    ],
    "evaluacion": [
        "Explica qué es un token sin decir «es una palabra» y anticipa qué textos "
        "van a consumir más de lo esperado.",
        "Enumera todo lo que ocupa espacio en la ventana de contexto, incluido lo que no es "
        "texto del usuario.",
        "Distingue los tres modos de fallo por contexto y reconoce cuál es silencioso.",
        "Estima el consumo de tokens de un caso real con un margen de error razonable.",
    ],
}


M4 = {
    "num": 4,
    "title": "Cómo razona un LLM",
    "tagline": "El módulo bisagra del programa: qué ocurre exactamente entre el prompt y la respuesta.",
    "objetivo": "Explicar el mecanismo de generación de un modelo de lenguaje y derivar de "
                "él las consecuencias prácticas que gobiernan el resto del programa.",
    "duracion": "3 horas",
    "dependencias": "Módulos 1 a 3. Es requisito para todo lo que sigue.",
    "contenidos": [
        ("Los cinco mitos que hay que desmontar antes de empezar", [
            "Que busca en internet.",
            "Que tiene una base de datos dentro.",
            "Que recuerda las conversaciones anteriores.",
            "Que ejecuta código por sí mismo.",
            "Que piensa como una persona.",
        ]),
        "La operación única: predecir el siguiente token.",
        "La distribución de probabilidad sobre el vocabulario completo.",
        "Atención: por qué el modelo pondera unas partes del prompt más que otras.",
        "Embeddings internos: cómo el modelo representa un token, y en qué se diferencian de los embeddings de recuperación del módulo 12.",
        "Entrenamiento frente a inferencia: por qué los pesos están congelados.",
        "De la probabilidad al texto: temperatura, top-p y top-k.",
        "Por qué alucinan los modelos, con la causa correcta.",
        "Los modelos de razonamiento: qué son realmente.",
        "Siete consecuencias prácticas que se derivan del mecanismo.",
    ],
    "enfoque": [
        ("box", "nota", "Por qué este módulo existe y dónde está colocado", [
            "Este módulo es nuevo respecto al temario base y es, probablemente, el cambio de "
            "mayor impacto de toda la revisión.",
            "Está situado **antes** del módulo de API de forma deliberada. Todo lo que viene "
            "después —el prompt engineering, la arquitectura de contexto, el RAG, los "
            "agentes— consiste en manipular la predicción del siguiente token. Sin este "
            "módulo, esas técnicas se aprenden como recetas que funcionan por razones "
            "desconocidas, y en cuanto una deja de funcionar no hay forma de diagnosticar "
            "por qué. Con este módulo, todas se deducen.",
        ]),

        ("sub", "Abrir por los mitos, no por la teoría"),

        "La apertura recomendada es una encuesta a mano alzada con las cinco afirmaciones "
        "del temario: ¿busca en Google? ¿tiene una base de datos? ¿recuerda? ¿ejecuta "
        "código? ¿piensa? Casi siempre hay manos levantadas en varias, incluso entre "
        "desarrolladores con experiencia, y eso convierte el resto del módulo en la "
        "resolución de una tensión en lugar de una exposición.",

        "Las cinco respuestas son «no», con un matiz importante que hay que dar de "
        "inmediato para no crear un malentendido nuevo: **un modelo no busca ni ejecuta "
        "código, pero un sistema construido alrededor de un modelo sí puede hacer ambas "
        "cosas.** Cuando un chat comercial cita una página web, lo que ocurrió es que un "
        "programa hizo la búsqueda, pegó los resultados en el prompt y el modelo escribió "
        "encima. Esa distinción entre *el modelo* y *el sistema alrededor del modelo* es la "
        "distinción más útil de todo el programa, y este es el momento de instalarla.",

        ("sub", "La operación única"),

        "El corazón del módulo cabe en una frase: **un modelo de lenguaje recibe una "
        "secuencia de tokens y produce una probabilidad para cada token posible del "
        "vocabulario.** Eso es todo lo que hace. Una sola vez. Para producir un texto largo, "
        "el sistema lo llama muchas veces seguidas, añadiendo cada vez el token elegido al "
        "final de la entrada.",

        "Conviene ejecutarlo en el pizarrón con una frase incompleta, por ejemplo *«el "
        "gato se subió al»*, y escribir a mano una distribución plausible:",

        ("code",
         "tejado      0.31\n"
         "sofá        0.22\n"
         "árbol       0.14\n"
         "coche       0.07\n"
         "escritorio  0.04\n"
         "...         (y así para los ~100 000 tokens restantes)"),

        "Tres observaciones que hay que hacer explícitas sobre esa tabla, porque cada una "
        "resuelve una confusión distinta:",

        ("numbers", [
            "**La lista incluye el vocabulario entero.** Todos los tokens reciben una "
            "probabilidad, incluso los absurdos. La mayoría reciben valores minúsculos pero "
            "no cero, y eso importa: significa que cualquier continuación es posible, solo "
            "que improbable.",
            "**El modelo no elige.** El modelo entrega la distribución. Quien elige es el "
            "código de muestreo que hay encima, y sus reglas son la temperatura, el top-p y "
            "el top-k. Esa separación es la que hace que esos tres parámetros dejen de ser "
            "magia.",
            "**No hay plan.** El modelo no sabía que iba a decir «tejado» cuando "
            "empezó la frase, ni sabe qué va a decir después. Cada token se decide con lo "
            "que hay escrito hasta ese momento y nada más.",
        ]),

        "El tercer punto suele generar resistencia y merece insistencia, porque de él se "
        "deduce casi todo lo demás. Un texto de un modelo parece planificado por la misma "
        "razón por la que un río parece haber elegido su cauce: cada paso local coherente "
        "produce un recorrido global que se ve intencionado.",

        ("sub", "Atención, sin álgebra"),

        "La atención es el mecanismo que permite que, al calcular la probabilidad del "
        "siguiente token, el modelo pondere de forma distinta cada token anterior. En una "
        "frase como *«la llave que compré ayer en la ferretería no abre»*, al "
        "procesar «abre» el modelo pondera mucho «llave» y poco "
        "«ayer».",

        "La regla de impartición aquí es dura y conviene respetarla: **cero matrices, cero "
        "query-key-value, cero softmax.** El público objetivo incluye personas no técnicas y "
        "el detalle no aporta nada a las decisiones que van a tomar. La analogía suficiente "
        "es la de leer una frase larga y volver la vista atrás a las palabras que importan "
        "para entender la última.",

        "Lo que sí hay que extraer, porque tiene consecuencias directas de diseño:",

        ("bullets", [
            "**La posición importa.** Lo que está al principio y al final del prompt tiende "
            "a pesar más que lo que queda enterrado en medio. De ahí sale la recomendación "
            "práctica de poner las instrucciones críticas al principio o al final, nunca "
            "sepultadas entre documentos.",
            "**El costo crece más rápido que el texto.** El mecanismo compara cada token con "
            "los anteriores, así que duplicar el contexto cuesta más que el doble en "
            "cómputo. Es una de las razones de fondo por las que los prompts largos son "
            "lentos, y no solo caros.",
            "**Los delimitadores ayudan de verdad.** Marcar las secciones del prompt con "
            "etiquetas o encabezados le da al mecanismo señales claras de dónde empieza y "
            "termina cada bloque. Esto justifica la mitad del módulo 5.",
        ]),

        ("sub", "Embeddings internos, y la confusión que hay que prevenir"),

        "Cada token, antes de entrar al modelo, se convierte en un vector de números. Eso es "
        "un embedding interno. Es el formato en el que el modelo representa el significado.",

        ("box", "alerta", "La confusión que este párrafo previene", [
            "En el módulo 12 aparecerán otros embeddings: los que produce un modelo de "
            "embeddings para guardar documentos en una base vectorial. **No son lo mismo y "
            "hay que decirlo aquí, por adelantado.**",
            "Los **embeddings internos** son representaciones de un token dentro del modelo, "
            "durante el cómputo. No se exponen, no se guardan y no sirven para buscar.",
            "Los **embeddings de recuperación** son un vector por fragmento de texto, "
            "producido por un modelo distinto y específico, diseñado para que textos con "
            "significado parecido queden cerca. Son los que se almacenan y se comparan.",
            "Sin esta aclaración, mucha gente concluye que el modelo «entiende "
            "embeddings» y que por eso el RAG funciona. Esa creencia hace que el módulo "
            "13 se entienda al revés, y el propio temario base la señala como un error que "
            "su autor cometió al empezar.",
        ]),

        ("sub", "Entrenamiento contra inferencia"),

        "La distinción se resuelve en cinco minutos y elimina una cantidad enorme de "
        "malentendidos: durante el **entrenamiento** los pesos cambian; durante la "
        "**inferencia** están congelados. Cada vez que se usa el modelo, se usa exactamente "
        "el mismo archivo de números.",

        "De ahí se deduce de forma inmediata algo que casi todo el mundo pregunta: **el "
        "modelo no aprende de la conversación.** No hay nada que se quede. Si un chat "
        "recuerda algo de la semana pasada es porque un sistema lo guardó en una base de "
        "datos y lo volvió a meter en el prompt. Esa es exactamente la arquitectura que se "
        "diseña en el módulo 8, y anunciarlo aquí le da sentido de antemano.",

        ("sub", "De la probabilidad al texto: los tres parámetros"),

        "Con la distribución ya en el pizarrón, los tres parámetros que el temario base "
        "situaba en el módulo 3 se explican en diez minutos y sin analogías forzadas:",

        ("table",
         ["Parámetro", "Qué hace exactamente", "Cuándo moverlo"],
         [
             ["Temperatura",
              "Aplana o agudiza la distribución antes de muestrear. Cerca de 0 el token más "
              "probable gana casi siempre; valores altos reparten la probabilidad y permiten "
              "que ganen opciones raras.",
              "Bajarla para extracción de datos, clasificación y salidas estructuradas. "
              "Subirla solo para generación creativa."],
             ["Top-p",
              "Se queda solo con los tokens más probables hasta acumular una probabilidad p, "
              "y descarta el resto. El número de candidatos varía según lo segura que esté "
              "la distribución.",
              "Es la palanca preferible frente al top-k porque se adapta al caso. Se suele "
              "ajustar una u otra, no ambas."],
             ["Top-k",
              "Se queda con los k tokens más probables, siempre el mismo número, sin importar "
              "cómo esté repartida la probabilidad.",
              "Más rígido. Útil cuando se quiere un límite duro y predecible de candidatos."],
         ],
         [2.6, 7.0, 6.9]),

        "Vale la pena señalar que **la temperatura no controla la calidad ni la "
        "creatividad**: controla la aleatoriedad del muestreo. Un modelo con temperatura "
        "alta no es más listo, es menos predecible. Y conviene mencionar que temperatura "
        "cero no garantiza determinismo perfecto en un servicio real, porque el orden de las "
        "operaciones en punto flotante y el enrutamiento entre servidores introducen "
        "variaciones pequeñas.",

        ("sub", "Por qué alucinan, con la causa correcta"),

        ("box", "correccion", "Corrección respecto al borrador base", [
            "El temario base propone «explicar de forma sencilla por qué un modelo "
            "alucina en base a la ventana de contexto». La ventana de contexto es un "
            "**agravante**, no la causa.",
            "La causa es el mecanismo mismo. El modelo siempre produce una distribución de "
            "probabilidad y siempre se muestrea un token de ella. No existe un estado "
            "interno de «no lo sé» que interrumpa la generación: la continuación "
            "estadísticamente plausible se produce igual, haya o no información que la "
            "respalde. Una alucinación no es un fallo del sistema, es el sistema "
            "funcionando exactamente como fue diseñado, aplicado a un caso donde no tenía "
            "con qué anclarse.",
            "La ventana de contexto interviene de forma indirecta y real: si la información "
            "correcta no está en el prompt —porque nunca se incluyó, porque se truncó el "
            "historial o porque quedó diluida entre ruido—, entonces no hay nada que ancle "
            "la predicción y la probabilidad de inventar sube. Es un factor de riesgo, no el "
            "origen.",
        ]),

        "La consecuencia práctica es la que hay que dejar grabada, porque es el argumento "
        "que sostiene el módulo 13 completo: **no se eliminan las alucinaciones pidiéndole "
        "al modelo que no invente.** Se reducen dándole la información en el contexto, "
        "obligándolo a citar la fuente, validando la salida por código, y dejando siempre "
        "una vía explícita para responder que no sabe. Esa última es la más olvidada: si el "
        "formato de salida no permite decir «no encontrado», el modelo va a llenar "
        "el campo con algo.",

        ("sub", "Los modelos de razonamiento"),

        "Conviene cerrar desinflando otro mito. Un modelo de razonamiento no usa un "
        "mecanismo distinto: **genera más tokens antes de dar la respuesta final.** Ese "
        "texto intermedio entra como entrada de los tokens siguientes, y ese bucle es lo que "
        "mejora el resultado en problemas de varios pasos.",

        "Tiene tres consecuencias que hay que anunciar porque reaparecen más adelante: esos "
        "tokens se facturan aunque no se muestren, la latencia sube de forma notable, y —lo "
        "más contraintuitivo— **pedirle explícitamente que razone paso a paso puede empeorar "
        "el resultado**, porque interfiere con el proceso que ya hace por su cuenta. Esto se "
        "retoma en el módulo 5 y el costo en el módulo 14.",

        ("sub", "Cerrar con la lista de consecuencias"),

        "Los últimos veinte minutos conviene dedicarlos a construir con la sala, en el "
        "pizarrón, la lista de cosas que ahora se explican solas. El objetivo es que la lista "
        "la digan ellos:",

        ("bullets", [
            "Inventa citas y referencias porque una cita tiene una forma muy predecible.",
            "No sabe cuándo no sabe, porque no hay un estado interno de incertidumbre que interrumpa nada.",
            "Es malo en aritmética exacta, porque los números se fragmentan en tokens y no hay calculadora dentro.",
            "El orden del prompt cambia la respuesta, por la atención.",
            "No recuerda nada, porque los pesos están congelados.",
            "Cambia de respuesta ante la misma pregunta, por el muestreo.",
            "Se degrada con prompts larguísimos, porque la señal útil se diluye.",
        ]),

        "Si la sala puede derivar esas siete consecuencias del mecanismo, el módulo cumplió "
        "su función y el resto del programa se apoya en terreno firme.",
    ],
    "ejercicio": [
        "Dos partes, una individual y una en grupo.",
        ("numbers", [
            "**Ver la distribución.** Con la API de cualquier proveedor que exponga las "
            "probabilidades de los tokens generados, lanzar la misma frase incompleta cinco "
            "veces con temperatura 0 y cinco veces con temperatura 1, y comparar tanto las "
            "salidas como las probabilidades. Escribir en tres líneas qué cambió y por qué.",
            "**Provocar una alucinación a propósito.** Preguntar al modelo por un detalle "
            "muy específico de algo que existe pero es oscuro —una cláusula de un documento "
            "interno, la versión exacta de una dependencia de un proyecto propio—. Registrar "
            "la respuesta. Después volver a preguntar pegando el documento real en el "
            "prompt. Contrastar ambas y explicar la diferencia usando el mecanismo, no la "
            "intuición.",
        ]),
    ],
    "evaluacion": [
        "Explica qué produce un modelo en una sola pasada, y que produce texto largo por repetición.",
        "Rechaza los cinco mitos y distingue el modelo del sistema construido a su alrededor.",
        "Explica temperatura, top-p y top-k en términos de la distribución, no con analogías de creatividad.",
        "Atribuye las alucinaciones al mecanismo de generación, y sitúa la ventana de contexto como agravante.",
        "Distingue embeddings internos de embeddings de recuperación.",
        "Deriva al menos cuatro consecuencias prácticas del mecanismo sin haberlas memorizado.",
    ],
}


PARTS = [
    {
        "kicker": "PARTE I",
        "title": "Fundamentos: qué es y qué no es un modelo",
        "intro": "Esta parte construye el modelo mental sobre el que se apoya todo lo demás. "
                 "Cierra con la pregunta que da sentido al resto del programa: qué ocurre "
                 "exactamente entre el momento en que se envía un prompt y el momento en que "
                 "llega una respuesta. Ocho horas.",
        "modules": [M1, M2, M3, M4],
    },
]
