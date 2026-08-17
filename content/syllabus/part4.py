# -*- coding: utf-8 -*-
"""Parte IV: operar un sistema (módulos 14 a 18)."""

M14 = {
    "num": 14,
    "title": "Costos de un sistema de AI",
    "tagline": "La mayoría de los sistemas de AI que se abandonan no se abandonan porque no funcionen, sino porque no se pueden pagar.",
    "objetivo": "Estimar el costo mensual de una funcionalidad antes de construirla, y "
                "elegir con criterio qué palanca mover para reducirlo.",
    "duracion": "2.5 horas",
    "dependencias": "Módulos 7, 9 y 13.",
    "contenidos": [
        "Tokens de entrada y de salida: precios asimétricos.",
        "Tokens de razonamiento: lo que se paga y no se ve.",
        "Caché de prompts: cómo funciona, cuánto ahorra y cómo se rompe sin querer.",
        "Procesamiento por lotes.",
        "Embeddings: el costo no está en generar, está en regenerar.",
        "Almacenamiento vectorial: la cuenta de memoria que casi nadie hace.",
        "Recuperación: el costo real no es la consulta, es lo que inyecta.",
        "Multimodal: cuántos tokens cuesta una imagen.",
        "Llamadas a herramientas y el costo de un bucle agéntico.",
        "El crecimiento cuadrático del historial conversacional.",
        "Cómo estimar el costo de una funcionalidad antes de construirla.",
        "Diez palancas ordenadas por impacto, y las guardas obligatorias.",
    ],
    "enfoque": [
        ("box", "nota", "Módulo nuevo respecto al borrador base", [
            "En el temario base el costo aparecía mencionado dentro de otros módulos —tokens, "
            "memoria, buenas prácticas— pero sin un lugar propio donde sumarlo todo.",
            "Se convierte en módulo porque las fuentes de gasto solo se pueden comparar entre "
            "sí en un mismo sitio, y porque el objetivo declarado —que nadie construya un "
            "sistema imposible de pagar— requiere hacer un cálculo completo de principio a "
            "fin, no notas al pie.",
        ]),

        ("box", "alerta", "Advertencia sobre las cifras de este módulo", [
            "Los precios de los proveedores cambian con frecuencia, casi siempre a la baja. "
            "Todas las cifras que aparecen aquí están dadas como **órdenes de magnitud** y "
            "deben traerse frescas de la documentación oficial el día de la impartición.",
            "Lo que no cambia son las relaciones: que la salida cuesta más que la entrada, "
            "que leer del caché cuesta una fracción de procesar, que el historial crece de "
            "forma cuadrática. El módulo enseña las relaciones, no los números.",
        ]),

        ("sub", "Abrir con la afirmación incómoda"),

        "La apertura recomendada: **la mayoría de los sistemas de AI que se abandonan no se "
        "abandonan porque no funcionen, sino porque no se pueden pagar.** El prototipo cuesta "
        "centavos porque lo usan tres personas. El producto cuesta miles porque lo usan tres "
        "mil, y el descubrimiento llega con la factura.",

        "El objetivo del módulo es que la sala salga con la capacidad de calcular el costo de "
        "una funcionalidad **antes de escribirla**. Es una habilidad que casi nadie enseña y "
        "que en la práctica decide qué se construye y qué no.",

        ("sub", "Entrada, salida y razonamiento"),

        "Se cobra distinto por token de entrada y por token de salida, y la salida cuesta "
        "varias veces más. De ahí sale la primera palanca, que es contraintuitiva: **acortar "
        "la respuesta ahorra más que acortar el prompt.**",

        "Los **tokens de razonamiento** son donde la gente se lleva el susto. En un modelo de "
        "razonamiento, el pensamiento intermedio se factura como salida aunque no aparezca en "
        "la respuesta, y puede ser varias veces más largo que la respuesta final. Un modelo "
        "de razonamiento con esfuerzo alto puede costar un orden de magnitud más que el mismo "
        "modelo sin razonamiento para la misma pregunta. Conviene enunciarlo así: **el "
        "presupuesto de razonamiento no es solo una perilla de calidad, es la palanca de "
        "costo más grande que existe en esos modelos.**",

        "Y conviene recordar qué cuenta como entrada, porque la lista sorprende: el system "
        "prompt, las definiciones de todas las herramientas, el historial completo, el "
        "contexto recuperado y los resultados de las herramientas ya ejecutadas.",

        ("sub", "Caché de prompts: la optimización con mejor relación esfuerzo-beneficio"),

        "Merece tiempo porque casi nadie la aprovecha bien. Funciona por **prefijo exacto**: "
        "el proveedor guarda el estado ya procesado de los primeros tokens y, si la siguiente "
        "petición empieza exactamente igual, se lo salta. Escribir al caché tiene un recargo "
        "sobre el precio de entrada; leerlo tiene un descuento fuerte, del orden de una "
        "décima parte en varios proveedores.",

        ("box", "correccion", "La consecuencia de diseño que hay que dejar grabada", [
            "**Todo lo estable va al principio del prompt y todo lo variable al final.** "
            "System prompt, definiciones de herramientas y documentos fijos primero; la "
            "pregunta del usuario al final.",
        ]),

        "Y las trampas, que son la parte que hay que enseñar porque son invisibles:",

        ("bullets", [
            "**Una marca de tiempo en el system prompt invalida el caché en cada llamada.** "
            "Es el error más común y el más fácil de cometer.",
            "**Reordenar las herramientas lo invalida**, aunque sean las mismas.",
            "**Truncar el historial por el principio lo invalida**, que es justo lo que hace "
            "la ventana deslizante del módulo 8.",
            "**Si el prefijo es corto o la reutilización es baja, no conviene.** Pagar el "
            "recargo de escritura sin llegar a leer sale más caro que no cachear.",
        ]),

        ("sub", "Lotes"),

        "El mensaje es simple: **si el trabajo no necesita respuesta inmediata, se está "
        "pagando de más.** El procesamiento por lotes ofrece descuentos fuertes, del orden de "
        "la mitad, a cambio de aceptar una ventana de entrega de hasta un día.",

        "Aquí conviene usar el ejemplo interno que el temario base ya menciona: el análisis "
        "masivo de candidatos de la herramienta interna de la empresa no es una operación "
        "interactiva. Nadie está mirando la pantalla esperando. Es exactamente el caso de uso "
        "del procesamiento por lotes, y probablemente hoy se esté pagando el doble por él.",

        ("sub", "Embeddings, almacenamiento y recuperación"),

        "Los embeddings son órdenes de magnitud más baratos que la generación, tanto que "
        "indexar un corpus completo suele ser trivial. **El costo no está en generar, está en "
        "regenerar**, y eso hay que presupuestarlo como gasto recurrente y no como costo de "
        "arranque: los documentos cambian, y tarde o temprano se va a querer cambiar de "
        "modelo de embeddings, lo que obliga a reprocesar todo.",

        "Para el almacenamiento vectorial conviene hacer la cuenta en el pizarrón, porque el "
        "resultado sorprende:",

        ("code",
         "  bytes por vector ≈ dimensiones × 4      (números de 32 bits)\n"
         "\n"
         "  1 536 dimensiones × 4 bytes  ≈  6 KB por vector\n"
         "  1 000 000 de vectores        ≈  6 GB solo de datos\n"
         "                                  + el sobrecosto del índice\n"
         "\n"
         "  Y el índice vive en memoria: lo que se paga en realidad es RAM."),

        "De ahí salen dos palancas concretas: **reducir dimensiones** —algunos modelos "
        "permiten truncar el vector con una pérdida de calidad sorprendentemente pequeña, que "
        "hay que medir y no suponer— y **cuantizar** a menor precisión, que reduce mucho la "
        "memoria a cambio de exhaustividad, recuperable en parte con un paso de "
        "reordenamiento.",

        ("box", "correccion", "El punto más contraintuitivo del módulo", [
            "**El costo del RAG no está en la base de datos, está en el prompt.**",
            "La búsqueda vectorial es barata. Pero si se recuperan diez trozos de quinientos "
            "tokens, se acaban de añadir cinco mil tokens de entrada a **cada** petición.",
            "Por eso recuperar menos y mejor —con reordenamiento, como en el módulo 13— "
            "**baja el costo y sube la calidad a la vez**. Es de las poquísimas "
            "optimizaciones sin contrapartida.",
        ]),

        ("sub", "Multimodal y herramientas"),

        "Las imágenes se convierten a tokens según su resolución, y una imagen grande puede "
        "costar como varios miles de tokens de texto. La palanca es directa y casi siempre se "
        "olvida: **reducir la resolución antes de enviar.**",

        "Sobre las herramientas hay que hacer explícito algo que ya se vio en el módulo 9: "
        "cada llamada es un viaje completo de ida y vuelta. Se manda todo el contexto, el "
        "modelo responde con la invocación, el código ejecuta, y **se vuelve a mandar todo el "
        "contexto más el resultado**. Un bucle de diez pasos no cuesta diez veces un paso: "
        "cuesta bastante más, porque el contexto crece en cada iteración.",

        ("sub", "El crecimiento cuadrático del historial"),

        "Conviene derivarlo en el pizarrón, porque el resultado es la mejor justificación de "
        "todo el módulo 8 y es mucho más persuasivo que decir «cuida el contexto»:",

        ("code",
         "  Si cada turno añade T tokens y se reenvía el historial completo:\n"
         "\n"
         "     turno 1 → T        turno 2 → 2T       turno 3 → 3T   ...\n"
         "\n"
         "     total tras N turnos = T · N(N+1)/2\n"
         "\n"
         "  Con N = 20:  210·T  en lugar de  20·T   →  diez veces más."),

        "**El costo de una conversación crece con el cuadrado de su longitud.** Ese solo dato "
        "justifica truncar, resumir y usar el caché.",

        ("sub", "Estimar antes de construir"),

        "La fórmula, que conviene dejar escrita:",

        ("code",
         "  costo_petición = entrada_sin_caché  × precio_entrada\n"
         "                 + entrada_cacheada   × precio_lectura_caché\n"
         "                 + (salida + razonamiento) × precio_salida\n"
         "\n"
         "  costo_mensual  = costo_petición\n"
         "                 × peticiones_por_sesión\n"
         "                 × sesiones_por_usuario_al_mes\n"
         "                 × usuarios_activos\n"
         "                 + costos_fijos (almacenamiento, reindexación, APIs externas)"),

        "Pero el método importa más que la fórmula: **ejecutar veinte o treinta casos reales, "
        "leer el campo de uso de cada respuesta, sacar el promedio y el percentil 95, y "
        "multiplicar.** El percentil 95 importa porque hay usuarios que sostienen "
        "conversaciones de ochenta turnos y son los que se comen el presupuesto. Las "
        "peticiones por sesión no se adivinan: se miden con el prototipo.",

        ("sub", "Las diez palancas, y las guardas"),

        ("numbers", [
            "**No llamar al modelo.** Si una regla, una consulta SQL o un caché exacto "
            "resuelve el caso, es infinitamente más barato.",
            "**Recuperar y meter menos contexto irrelevante.**",
            "**Estabilizar el prefijo** para explotar el caché de prompts.",
            "**Enrutar al modelo adecuado por tarea**, reservando el caro para donde importa.",
            "**Limitar la salida** con un máximo de tokens y con formato estructurado en "
            "lugar de prosa.",
            "**Procesar por lotes** todo lo que no sea interactivo.",
            "**Truncar y resumir el historial.**",
            "**Reducir viajes de ida y vuelta** en los bucles agénticos.",
            "**Reducir dimensiones y cuantizar** en el almacenamiento vectorial.",
            "**Reindexar de forma incremental** por comparación de contenido, nunca completa "
            "por defecto.",
        ]),

        ("box", "alerta", "Guardas que no son opcionales", [
            "Presupuesto máximo por sesión, por usuario y por día, **con corte automático**.",
            "Límite duro de iteraciones en cualquier bucle agéntico.",
            "Atribución de costo por funcionalidad y por cliente, para saber qué recortar "
            "cuando la factura suba.",
            "Alertas por desviación respecto a la tendencia, no solo por umbral absoluto.",
            "Un agente sin tope de iteraciones no es un riesgo teórico: es un incidente de "
            "facturación esperando su turno.",
        ]),
    ],
    "ejercicio": [
        "Estimar de principio a fin el costo de una funcionalidad real que el equipo quiera "
        "construir o ya tenga en producción:",
        ("numbers", [
            "Ejecutar veinte casos reales registrando el campo de uso de cada respuesta.",
            "Calcular el costo por petición promedio y en el percentil 95.",
            "Estimar el costo mensual con la fórmula, incluyendo los costos fijos.",
            "Aplicar tres palancas de la lista y volver a medir sobre los mismos veinte casos.",
            "Presentar el antes y el después con el porcentaje de ahorro y el impacto en "
            "calidad, si lo hubo.",
        ]),
        "La entrega debe incluir el costo por usuario activo al mes. Es el número que permite "
        "decidir si la funcionalidad es viable con el modelo de negocio del producto.",
    ],
    "evaluacion": [
        "Enumera las fuentes de gasto de un sistema de AI más allá de los tokens.",
        "Explica cómo funciona el caché de prompts y nombra al menos dos formas de romperlo sin querer.",
        "Deriva el crecimiento cuadrático del historial y lo usa para justificar una decisión de diseño.",
        "Estima el costo mensual de una funcionalidad con datos medidos, no supuestos.",
        "Sabe que el costo del RAG está en el prompt y no en la base de datos.",
        "Define guardas de presupuesto y límites de iteración.",
    ],
}


M15 = {
    "num": 15,
    "title": "Orquestación",
    "tagline": "Dividir para que cada pieza reciba solo el contexto que necesita: más preciso, más rápido y más barato a la vez.",
    "objetivo": "Decidir cuándo dividir un sistema en varios agentes o pasos, y diseñar el "
                "flujo de orquestación completo.",
    "duracion": "2 horas",
    "dependencias": "Módulos 9 y 14.",
    "contenidos": [
        "Por qué delegar todo a un solo agente sale mal.",
        "División por responsabilidad: cada pieza con su contexto mínimo.",
        "Cuándo NO conviene dividir.",
        "Carga de contexto bajo demanda.",
        "Tareas en segundo plano y paralelismo.",
        "Cadenas de ejecución y listas de tareas.",
        "Un flujo de orquestación de principio a fin.",
        "Dónde se rompe: propagación de errores y estado parcial.",
    ],
    "enfoque": [
        ("box", "nota", "Por qué este módulo va después de costos", [
            "El temario base situaba la orquestación antes. Se mueve después del módulo 14 "
            "por una razón concreta: el argumento central de la orquestación es que **menos "
            "contexto por pieza es más preciso y más barato**, y con el módulo de costos ya "
            "visto ese argumento se sostiene con números en lugar de con intuición.",
        ]),

        ("sub", "El problema, planteado como el temario base lo plantea"),

        "El punto de partida es correcto y conviene conservarlo: si se le delega todo a un "
        "solo agente, con todas las herramientas y todo el contexto disponible, el resultado "
        "es **menos preciso y más caro**. Las dos cosas a la vez, y esa simultaneidad es lo "
        "que hace fuerte el argumento.",

        "Menos preciso porque la instrucción relevante compite con cincuenta herramientas y "
        "veinte documentos por la atención del modelo, que es exactamente el tercer modo de "
        "fallo del módulo 3. Más caro porque todo ese contexto se paga en cada iteración del "
        "bucle, que es el efecto acumulativo del módulo 14.",

        ("sub", "Dividir por responsabilidad"),

        "La analogía que funciona con un público de desarrolladores es la de la "
        "responsabilidad única, y conviene usarla porque traslada un criterio que ya tienen: "
        "**cada agente debería poder describirse en una frase, sin la palabra «y».**",

        "Un agente que «busca información, la valida, redacta el resumen y lo envía por "
        "correo» son cuatro agentes. La división da tres cosas: cada uno recibe solo el "
        "contexto y las herramientas que necesita, cada uno se puede probar por separado, y "
        "cada uno puede usar un modelo distinto según lo difícil que sea su tarea.",

        "Ese último punto merece énfasis porque es la palanca de costo más grande del "
        "módulo. En una cadena de cuatro pasos, típicamente uno requiere juicio real y tres "
        "son mecánicos. Ejecutar los cuatro con el modelo más caro es, como decía el temario "
        "base, matar moscas a cañonazos.",

        ("sub", "Cuándo NO dividir"),

        "Igual de importante, y menos frecuente en los materiales que circulan:",

        ("bullets", [
            "**Cuando el contexto es indivisible.** Si el paso B necesita todo lo que vio el "
            "paso A, dividir obliga a pasar el contexto entero de todos modos y se paga dos "
            "veces.",
            "**Cuando la tarea es corta.** Dos llamadas al modelo para algo que resolvía una "
            "duplican la latencia y el costo sin ganar precisión.",
            "**Cuando la coordinación cuesta más que la tarea.** Si el orquestador necesita "
            "tanta lógica como los agentes, probablemente sobra la división.",
            "**Cuando hace falta trazabilidad simple.** Más piezas es más superficie donde "
            "algo puede fallar en silencio.",
        ]),

        ("sub", "Carga de contexto bajo demanda"),

        "El temario base lo llama «carga por goteo» y la idea es exacta: en lugar de "
        "inyectar todo el contexto posible al arrancar, se carga solo cuando la tarea lo "
        "pide.",

        "Conviene señalar que esto ya apareció dos veces en el programa con otros nombres: es "
        "lo que hacen las skills del módulo 9 —procedimientos que se activan cuando son "
        "relevantes— y es lo que hace el RAG del módulo 13 —documentos que entran solo si la "
        "consulta los pide—. Nombrar el patrón común ayuda a que se reconozca en situaciones "
        "nuevas.",

        ("sub", "Segundo plano y paralelismo"),

        "Dos ganancias distintas que conviene no confundir. El **paralelismo** reduce la "
        "latencia total cuando hay pasos independientes: tres búsquedas que no dependen entre "
        "sí se lanzan a la vez. El **segundo plano** desacopla lo que el usuario espera de lo "
        "que no: la respuesta se devuelve ya, y la indexación, el resumen o el envío ocurren "
        "después.",

        "Aquí conecta bien el módulo 10: la forma habitual de enterarse de que un trabajo en "
        "segundo plano terminó es un webhook, con todas las obligaciones que eso implica.",

        ("sub", "Cadenas de ejecución"),

        "El temario base menciona el estilo de los agentes de código que mantienen una lista "
        "de tareas visible, y es un ejemplo excelente porque la sala lo tiene delante todos "
        "los días. Conviene desarmarlo en clase: el agente descompone el objetivo en una "
        "lista, la marca conforme avanza, y esa lista funciona a la vez como plan, como "
        "memoria de trabajo y como interfaz para la persona.",

        "Las tres funciones simultáneas son el aprendizaje: **una lista de tareas explícita "
        "resuelve la planificación, la observación y la trazabilidad al mismo tiempo**, y es "
        "de las decisiones de diseño más rentables que existen en un sistema agéntico.",

        ("sub", "Dónde se rompe"),

        "Cerrar con los modos de fallo propios de un sistema orquestado, que son distintos de "
        "los de un agente único:",

        ("bullets", [
            "**Error a mitad de la cadena.** El paso tres falla y los pasos uno y dos ya "
            "tuvieron efectos. Hay que decidir si se reintenta, si se compensa o si se "
            "aborta, y eso es diseño, no una excepción.",
            "**Contexto perdido en la frontera.** El agente B no recibió un matiz que A sí "
            "tenía. Es el fallo más frecuente y el más difícil de ver: no da error, da una "
            "respuesta peor.",
            "**Bucles entre agentes.** A llama a B, B devuelve a A. Los límites de "
            "iteración tienen que ser globales, no por agente.",
            "**Costo invisible.** Cada agente parece barato y la suma no lo es. Sin "
            "atribución por paso, no hay forma de saber cuál se lleva el presupuesto. Es la "
            "conexión directa con el módulo 16.",
        ]),
    ],
    "ejercicio": [
        "Tomar el agente único del módulo 9 y refactorizarlo en un sistema orquestado:",
        ("numbers", [
            "Identificar las responsabilidades y separarlas de forma que cada pieza se "
            "describa en una frase sin la palabra «y».",
            "Asignar a cada pieza el contexto mínimo y solo las herramientas que necesita.",
            "Usar un modelo más barato en al menos una de las piezas.",
            "Ejecutar los pasos independientes en paralelo.",
            "Medir, sobre los mismos casos de prueba: latencia total, costo total y calidad "
            "del resultado, antes y después.",
        ]),
        "Se pide reportar honestamente si la refactorización **empeoró** algo. Con frecuencia "
        "la latencia sube por la coordinación aunque el costo baje, y reconocer ese "
        "intercambio es parte del objetivo.",
    ],
    "evaluacion": [
        "Justifica una división con el doble argumento de precisión y costo.",
        "Identifica al menos dos situaciones donde dividir es contraproducente.",
        "Reconoce la carga bajo demanda como un patrón común a skills, RAG y orquestación.",
        "Distingue la ganancia del paralelismo de la del procesamiento en segundo plano.",
        "Anticipa los modos de fallo de un sistema orquestado, incluido el contexto perdido en la frontera.",
    ],
}


M16 = {
    "num": 16,
    "title": "Observabilidad",
    "tagline": "En un sistema de AI el fallo típico no es una excepción: es una respuesta correcta en forma y equivocada en fondo.",
    "objetivo": "Instrumentar un sistema de AI con las trazas y métricas suficientes para "
                "responder por qué produjo una respuesta concreta, y detectar los modos de "
                "fallo que no lanzan errores.",
    "duracion": "2 horas",
    "dependencias": "Módulos 13, 14 y 15.",
    "contenidos": [
        "Por qué la observabilidad tradicional no alcanza.",
        "Trazas y spans: modelar una petición como un árbol.",
        "Qué registrar en un span de modelo, de recuperación y de herramienta.",
        "Logs: el prompt renderizado, no la plantilla.",
        "Métricas: costo, latencia con percentiles, errores, iteraciones.",
        "Versionado de prompts: el prompt es código.",
        "Correlación: trazas, sesiones y usuarios.",
        "Privacidad y retención de las trazas.",
        "Muestreo y el costo de observar.",
        "Panorama de herramientas, por estilo de integración.",
        "Qué instrumentar primero si solo hay un día.",
    ],
    "enfoque": [
        ("box", "nota", "Ascenso respecto al borrador base", [
            "En el temario base, la observabilidad era una viñeta dentro de conceptos "
            "avanzados, mencionada junto a una herramienta concreta.",
            "Se convierte en módulo propio porque es lo que decide si un sistema de AI se "
            "puede operar o solo se puede lanzar, y porque la lista de cosas que hay que "
            "registrar no cabe en una viñeta.",
        ]),

        ("sub", "La diferencia que justifica el módulo"),

        "Conviene abrir con el contraste, sin adornos: en software tradicional, cuando algo "
        "falla hay una excepción, un rastro de pila y una línea de código culpable. **En un "
        "sistema de AI el modo de fallo típico es una respuesta correcta en forma y "
        "equivocada en fondo.** No hay excepción, no hay error, y desde fuera todo se ve sano.",

        "Y como el sistema no es determinista, el mismo caso puede fallar una de cada diez "
        "veces, así que ni siquiera se puede reproducir a voluntad. La conclusión hay que "
        "decirla sin suavizarla: **si no se instrumentó, no se está depurando, se está "
        "adivinando.**",

        ("sub", "La traza como árbol"),

        "El concepto central. Una petición del usuario es la raíz, y de ella cuelgan todas "
        "las operaciones: la llamada al modelo, la búsqueda vectorial, cada herramienta, cada "
        "subagente con su propio subárbol.",

        ("code",
         "petición del usuario                          1 240 ms · $0.014\n"
         "├── recuperación                                180 ms\n"
         "│   ├── embedding de la consulta                 40 ms\n"
         "│   └── búsqueda vectorial (k=10)               140 ms\n"
         "├── llamada al modelo (planificación)           420 ms · 3 100 tokens\n"
         "├── herramienta: consultar_inventario           210 ms · error\n"
         "├── herramienta: consultar_inventario (reintento) 190 ms · ok\n"
         "└── llamada al modelo (respuesta final)         240 ms · 4 800 tokens"),

        "Cuando se ve una traza así, la pregunta «¿por qué el agente respondió esto?» "
        "deja de ser filosófica y se vuelve mecánica: se abre el árbol y se ve qué se "
        "recuperó, qué se le mandó y qué contestó en cada paso. Conviene enseñarlo "
        "proyectando una traza real de un flujo con RAG y dos herramientas, y desarmándola "
        "en pantalla.",

        ("sub", "Qué registrar en cada tipo de span"),

        ("table",
         ["Tipo de span", "Qué guardar"],
         [
             ["Llamada al modelo",
              "Modelo y versión exacta, parámetros, mensajes completos de entrada y salida, "
              "tokens de entrada, salida, razonamiento y caché, latencia, tiempo hasta el "
              "primer token, costo calculado y motivo de finalización."],
             ["Recuperación",
              "La consulta, la consulta reescrita si la hubo, los K documentos **con sus "
              "puntajes**, el umbral aplicado, y si hubo reordenamiento, cómo cambió el orden."],
             ["Herramienta",
              "Nombre, argumentos, resultado, duración, error si lo hubo, y número de reintento."],
         ],
         [3.6, 12.9]),

        ("box", "correccion", "El campo que más veces salva una depuración", [
            "**Los puntajes de similitud de los documentos recuperados.**",
            "Sin ellos, cuando un RAG da una mala respuesta no se puede distinguir entre "
            "«el trozo correcto no se recuperó» y «sí se recuperó y el modelo "
            "lo ignoró». Son dos problemas completamente distintos, con soluciones "
            "opuestas: uno se arregla en la indexación y el otro en el prompt.",
            "Guardar los K documentos con su puntaje convierte esa pregunta en una mirada de "
            "tres segundos. Es el campo que más implementaciones caseras olvidan.",
        ]),

        ("sub", "Métricas: el promedio miente"),

        "El punto pedagógico de esta sección. Las latencias de los modelos tienen colas "
        "largas y asimétricas: un promedio de dos segundos puede esconder que uno de cada "
        "veinte usuarios espera quince. Por eso **siempre percentiles 50, 95 y 99**, nunca "
        "solo el promedio.",

        "Con streaming hay que separar el **tiempo hasta el primer token** de la latencia "
        "total, porque son dos experiencias distintas y el usuario percibe la primera.",

        "Las métricas que conviene tener desde el principio: costo por petición, sesión, "
        "usuario y funcionalidad; latencia en percentiles; tasa de error y de reintento; "
        "tokens por petición y ocupación de la ventana de contexto; tasa de fallo por "
        "herramienta; tasa de recuperación vacía o bajo umbral; y una que casi nadie mide y "
        "debería: **la distribución de iteraciones de los bucles agénticos**, porque un "
        "promedio de tres puede esconder que el dos por ciento de las sesiones da veinte "
        "vueltas y se lleva la mitad del presupuesto.",

        ("sub", "El prompt es código"),

        "Una afirmación simple con consecuencias concretas: el prompt vive en el repositorio, "
        "se revisa en una solicitud de cambios, tiene versión, y **cada traza registra qué "
        "versión se usó**.",

        "Lo que eso compra es poder responder la pregunta más frecuente en producción —«ayer "
        "funcionaba, hoy no, ¿qué cambió?»— y poder revertir un prompt igual que se "
        "revierte un despliegue.",

        "Y el anti-patrón que conviene señalar por nombre: editar el prompt en la interfaz "
        "web de una herramienta, sin control de versiones, en producción. Es exactamente "
        "equivalente a editar código en el servidor por FTP.",

        ("sub", "Correlación"),

        "Un identificador de traza que no se propaga no sirve. Tiene que viajar a los "
        "servicios externos y, donde el proveedor permita enviar metadatos en la petición, "
        "hay que enviarlo: es lo que después permite cruzar las trazas propias con la "
        "facturación del proveedor y responder de qué se compone la factura.",

        "El identificador de **sesión** reconstruye una conversación completa y el de "
        "**usuario** convierte un reporte vago de un cliente en diez trazas concretas que se "
        "pueden revisar. Son los mismos identificadores que se diseñaron en el módulo 8, y "
        "conviene decirlo para que se definan una sola vez.",

        ("sub", "Privacidad: la parte que casi siempre se pasa por alto"),

        ("box", "alerta", "Todo lo que va en el prompt termina en las trazas", [
            "Si se están inyectando datos de clientes por RAG, el sistema de observabilidad "
            "acaba de convertirse en un repositorio de datos personales, con su propio "
            "control de acceso, su política de retención y su superficie de auditoría.",
            "La redacción de datos sensibles tiene que ocurrir **antes** de emitir la traza, "
            "no como limpieza posterior.",
            "Y si un secreto se filtró al prompt, ahora está en dos sistemas más. Enlaza "
            "directamente con el módulo siguiente.",
        ]),

        ("sub", "El costo de observar"),

        "Guardar el cien por ciento de prompts y respuestas es caro en almacenamiento. La "
        "estrategia razonable es **muestreo con sesgo**: el cien por ciento de los errores, "
        "el cien por ciento de lo lento, y un porcentaje del resto. Y el sobrecosto de "
        "latencia debe ser asíncrono: emitir trazas nunca debe estar en el camino crítico de "
        "la respuesta al usuario.",

        ("sub", "Panorama de herramientas, sin casarse con ninguna"),

        "Conviene presentarlo por **estilo de integración** en lugar de por marca, porque el "
        "espacio se mueve rápido y una recomendación concreta envejece mal.",

        ("bullets", [
            "**Instrumentación en el código**, con un SDK o decoradores: da control fino y "
            "contexto semántico, pero hay que tocar el código.",
            "**Intercepción por proxy o pasarela**: se instala en minutos y no requiere "
            "cambios, pero ve menos de la lógica propia.",
        ]),

        "Sobre esa base se puede nombrar el panorama sin ranking: **OpenTelemetry** con sus "
        "convenciones para AI generativa como la apuesta neutral, y herramientas como "
        "Langfuse —de código abierto y autohospedable—, LangSmith —natural si ya se vive en "
        "ese ecosistema—, Braintrust, Phoenix de Arize y Helicone con enfoque de proxy.",

        "El criterio que hay que dar no es cuál elegir sino qué preguntar: ¿hace falta "
        "autohospedaje por regulación? ¿se quiere tocar código o no? ¿qué tan atado se queda "
        "el equipo si mañana quiere migrar? La única recomendación de arquitectura que "
        "conviene dar: **emitir en un formato estándar y mantener el backend "
        "intercambiable.**",

        ("sub", "Si solo hay un día"),

        "Nadie instrumenta todo desde el principio. El mínimo que resuelve la mayoría de las "
        "depuraciones: por cada petición, registrar el prompt final renderizado, la respuesta "
        "completa, el modelo y su versión, los tokens de entrada y salida, la latencia y —si "
        "hay RAG— los documentos recuperados con sus puntajes. Todo amarrado con un "
        "identificador de traza y uno de sesión. Son unos pocos campos en una tabla.",

        ("box", "nota", "Una ausencia deliberada", [
            "Este programa no incluye un módulo de evaluación de sistemas de AI —métricas de "
            "calidad, conjuntos de referencia, jueces automáticos—. La ausencia es una "
            "decisión, no un olvido.",
            "Conviene decirlo en clase al cerrar este módulo: **una traza dice qué pasó, no "
            "si estuvo bien.** Medir la calidad es un tema propio y extenso que este "
            "programa no cubre, y quien vaya a operar un sistema en producción va a "
            "necesitarlo.",
        ]),
    ],
    "ejercicio": [
        "Instrumentar el sistema orquestado del módulo 15:",
        ("numbers", [
            "Emitir una traza por petición, con spans anidados para modelo, recuperación y "
            "cada herramienta.",
            "Registrar en cada span los campos de la tabla, **incluidos los puntajes de "
            "recuperación**.",
            "Propagar un identificador de traza y uno de sesión por todo el flujo.",
            "Construir un tablero mínimo con costo por sesión, latencia en percentiles 50 y "
            "95, y tasa de fallo por herramienta.",
            "Introducir a propósito tres fallos —un trozo relevante que no se recupera, una "
            "herramienta que devuelve datos inútiles sin error, y un bucle que da demasiadas "
            "vueltas— y **diagnosticar los tres usando solo las trazas**.",
        ]),
        "La fase 5 es el ejercicio real. Si los tres fallos no se pueden diagnosticar desde "
        "la traza, la instrumentación está incompleta y hay que volver a la fase 2.",
    ],
    "evaluacion": [
        "Explica por qué la observabilidad tradicional no basta en un sistema no determinista.",
        "Modela una petición como un árbol de spans e identifica qué guardar en cada tipo.",
        "Registra los puntajes de recuperación y distingue un fallo de recuperación de uno de generación.",
        "Usa percentiles en lugar de promedios y justifica por qué.",
        "Versiona los prompts y correlaciona trazas por sesión y por usuario.",
        "Reconoce que las trazas son una superficie de datos personales.",
    ],
}


M17 = {
    "num": 17,
    "title": "Buenas prácticas",
    "tagline": "El equivalente al código limpio, pero para sistemas de AI.",
    "objetivo": "Aplicar un conjunto de criterios de diseño que mantienen un sistema de AI "
                "mantenible, barato y preciso conforme crece.",
    "duracion": "1.5 horas",
    "dependencias": "Módulos 8, 14, 15 y 16.",
    "contenidos": [
        "No todo va en el system prompt.",
        "División de contexto por dominio.",
        "Cargar contexto solo cuando es necesario.",
        "Lo que se pueda resolver por código, se resuelve por código.",
        "Menos peticiones y menos contexto.",
        "Límites del historial conversacional.",
        "Usar modelos distintos según la tarea.",
        "El prompt como artefacto versionado.",
        "Ejemplo de una arquitectura limpia de principio a fin.",
    ],
    "enfoque": [
        ("sub", "El encuadre que el temario base ya propone"),

        "La comparación con la literatura de código limpio es acertada y conviene "
        "conservarla como marco del módulo. Estas no son reglas absolutas: son criterios "
        "que resuelven tensiones concretas, y como toda buena práctica tienen excepciones "
        "que hay que saber reconocer.",

        "La diferencia con este módulo y los anteriores es que aquí no se introducen "
        "conceptos nuevos: **se consolida en criterios lo que ya se demostró en los módulos "
        "previos.** Conviene decirlo, porque hace que la sesión se sienta como una síntesis "
        "y no como una lista de consejos sueltos.",

        ("sub", "Las prácticas, cada una con su porqué ya demostrado"),

        ("table",
         ["Práctica", "Por qué, y dónde se demostró"],
         [
             ["No meter todo en el system prompt",
              "Cuesta en cada petición y diluye la señal. Módulos 3 y 14."],
             ["Dividir el contexto por dominio",
              "Cada pieza recibe solo lo suyo: más preciso y más barato. Módulo 15."],
             ["Cargar contexto bajo demanda",
              "El mismo patrón que las skills y el RAG. Módulos 9, 13 y 15."],
             ["Resolver por código lo que se pueda",
              "Una regla determinista es más barata, más rápida y más confiable que una "
              "llamada al modelo. Módulos 1 y 14."],
             ["Reducir el número de peticiones",
              "Cada viaje de ida y vuelta reenvía el contexto acumulado. Módulos 9 y 14."],
             ["Limitar el historial por mensajes y por tokens",
              "El costo crece con el cuadrado de la longitud. Módulos 8 y 14."],
             ["Usar modelos distintos según la tarea",
              "Tres de cada cuatro pasos de una cadena suelen ser mecánicos. Módulo 15."],
             ["Versionar los prompts",
              "Sin versión no hay forma de responder qué cambió. Módulo 16."],
         ],
         [5.4, 11.1]),

        ("sub", "La práctica que más se incumple"),

        "Merece desarrollo propio porque es la que más dinero cuesta y la que más veces se "
        "ignora: **si se puede resolver por código, se resuelve por código.**",

        "Los casos concretos que conviene enumerar, porque son reales y frecuentes: validar "
        "un formato con una expresión regular en lugar de pedírselo al modelo; ordenar, "
        "filtrar o contar con una consulta en lugar de pasarle la lista al modelo; enrutar "
        "por reglas cuando las categorías son fijas; calcular con una función en lugar de "
        "confiar en la aritmética del modelo, que el módulo 4 explicó por qué falla.",

        "El criterio de decisión: **si la entrada es estructurada y la regla es escribible, "
        "no hace falta el modelo.** El modelo se reserva para lo que requiere juicio sobre "
        "lenguaje natural ambiguo. Es la misma distinción del módulo 1, ahora aplicada a "
        "decisiones de arquitectura.",

        ("sub", "El ejemplo integrador"),

        "El temario base pide cerrar con un ejemplo de arquitectura limpia, y es la mejor "
        "forma de terminar la parte IV. Conviene dedicarle la última media hora completa y "
        "usar un caso real de la empresa, dibujando el flujo en el pizarrón y señalando en "
        "cada punto qué práctica se está aplicando y qué módulo la justificó.",

        ("code",
         "  entrada del usuario\n"
         "        │\n"
         "        ├── validación por código          (nada de modelo todavía)\n"
         "        ├── enrutamiento por reglas        (categorías fijas)\n"
         "        │\n"
         "        ├── ¿necesita contexto externo?\n"
         "        │      └── recuperación + reordenamiento   (poco y bueno)\n"
         "        │\n"
         "        ├── modelo barato: clasificar / extraer\n"
         "        ├── modelo capaz: la parte que requiere juicio\n"
         "        │\n"
         "        ├── validación de la salida por código      (esquema + reglas)\n"
         "        └── traza emitida de forma asíncrona\n"
         "\n"
         "  prefijo estable al inicio del prompt · historial acotado ·\n"
         "  límite de iteraciones · presupuesto por sesión"),

        "El ejercicio de lectura que conviene hacer con la sala: pedirles que identifiquen "
        "qué módulo justifica cada línea del diagrama. Si pueden hacerlo, el programa está "
        "cumpliendo su función.",
    ],
    "ejercicio": [
        "Revisión por pares de una arquitectura real. Cada equipo presenta un sistema de AI "
        "propio —en producción o en diseño— y otro equipo lo audita contra la tabla de "
        "prácticas, señalando para cada incumplimiento:",
        ("bullets", [
            "Qué práctica se está incumpliendo.",
            "Cuál es el costo concreto estimado, en dinero, latencia o precisión.",
            "Cuál sería el cambio mínimo para corregirlo.",
            "Si es un incumplimiento justificado, porque también los hay.",
        ]),
        "La entrega es un informe de auditoría de una página por sistema.",
    ],
    "evaluacion": [
        "Justifica cada buena práctica con el mecanismo o el cálculo que la sostiene, no como regla.",
        "Identifica en un sistema existente al menos tres decisiones que deberían resolverse por código.",
        "Reconoce cuándo un incumplimiento está justificado.",
        "Lee un diagrama de arquitectura y señala qué práctica aplica cada componente.",
    ],
}


M18 = {
    "num": 18,
    "title": "Seguridad",
    "tagline": "Todo lo que entra al contexto es contenido no confiable, incluida la respuesta de una herramienta.",
    "objetivo": "Identificar las vulnerabilidades propias de un sistema de AI y aplicar las "
                "defensas correspondientes, sabiendo cuáles son parciales.",
    "duracion": "2 horas",
    "dependencias": "Módulos 9, 10, 13 y 16.",
    "contenidos": [
        "Guardrails: qué son y dónde se colocan.",
        "Salidas estructuradas como control de seguridad.",
        "Validación de la respuesta antes de actuar sobre ella.",
        ("Inyección de prompts", [
            "Directa: el usuario intenta manipular el comportamiento.",
            "Indirecta: el contenido recuperado o la respuesta de una herramienta contiene instrucciones.",
            "Por qué no tiene solución completa.",
        ]),
        "Exfiltración de datos y secretos.",
        "Bucles de reindexación y otros riesgos de costo.",
        "Variables de entorno y manejo de credenciales.",
        "Permisos y acciones irreversibles.",
    ],
    "enfoque": [
        ("sub", "El encuadre"),

        "El temario base lo plantea bien: igual que en el software tradicional, en AI hay "
        "vulnerabilidades explotables. La diferencia que conviene añadir es cuál es la "
        "superficie nueva, porque es lo que hace que las defensas conocidas no basten.",

        "La superficie nueva es esta: **el sistema toma decisiones a partir de texto, y ese "
        "texto puede venir de fuera.** En software tradicional los datos son datos y el "
        "código es código. En un sistema de AI, un texto que llega como dato puede acabar "
        "funcionando como instrucción. Esa confusión de planos es el origen de casi todo lo "
        "que sigue.",

        ("sub", "Guardrails"),

        "La analogía de la carretera que propone el temario base funciona bien y conviene "
        "conservarla: no dirigen el vehículo, evitan que se salga. Lo que hay que añadir es "
        "**dónde** se colocan, porque un guardrail solo en el prompt es un guardrail pintado "
        "en el suelo.",

        ("table",
         ["Dónde", "Qué controla", "Fiabilidad"],
         [
             ["En el prompt", "Instrucciones de comportamiento y límites declarados.",
              "Baja. Es una petición al modelo, no una restricción del sistema."],
             ["Sobre la entrada", "Filtrado y clasificación antes de llegar al modelo.",
              "Media. Detecta lo evidente."],
             ["Sobre la salida", "Validación de esquema, de contenido y de reglas de negocio.",
              "Alta si es código. Es la capa que de verdad protege."],
             ["En la ejecución", "Permisos, límites de tasa, confirmación humana, "
                                 "operaciones reversibles.",
              "Alta. Es la única que resiste a un modelo comprometido."],
         ],
         [3.2, 6.6, 6.7]),

        "La regla que ordena la tabla: **cuanto más cerca del código y más lejos del modelo, "
        "más fiable es el control.** Un guardrail que depende de que el modelo obedezca no "
        "es un control de seguridad, es una expectativa.",

        ("sub", "Salidas estructuradas y validación"),

        "Aquí se cobra lo del módulo 5. Un esquema de salida no es solo comodidad de "
        "parseo: es una reducción del espacio de lo que el sistema puede hacer. Si la salida "
        "solo puede ser una de tres acciones enumeradas, el modelo no puede pedir una cuarta.",

        ("box", "alerta", "La regla que hay que repetir", [
            "**El esquema garantiza la forma, nunca la verdad.** Y de ahí se sigue la regla "
            "operativa más importante del módulo: **ninguna decisión de autorización se toma "
            "a partir de un campo que devolvió el modelo.**",
            "Si el modelo devuelve `usuario_es_administrador: true`, eso no es una "
            "autorización: es una cadena de texto que un atacante puede haber inducido. La "
            "autorización se resuelve del lado del servidor, con la sesión real del usuario, "
            "antes de ejecutar nada.",
        ]),

        ("sub", "Inyección de prompts, en sus dos formas"),

        "La **directa** es la que todo el mundo conoce: el usuario escribe algo para que el "
        "sistema se comporte como no debe. Es la menos peligrosa, porque el atacante solo "
        "puede afectar a su propia sesión.",

        "La **indirecta** es la que importa y la que el temario base no cubría. El atacante "
        "no habla con el sistema: **deja el texto donde el sistema lo va a leer.** Un "
        "documento que se va a indexar en el RAG. Una página web que una herramienta va a "
        "consultar. Un ticket que un agente va a procesar. Un campo de un registro de la base "
        "de datos.",

        ("box", "alerta", "Por qué esto es grave en un sistema agéntico", [
            "En el módulo 10 se dijo que todo resultado de una herramienta es contenido no "
            "confiable. Este es el momento de cobrarlo.",
            "Un agente con herramientas que lee un documento envenenado puede acabar "
            "ejecutando acciones reales en nombre de un atacante que nunca habló con él. La "
            "combinación peligrosa es siempre la misma: **acceso a datos no confiables + "
            "capacidad de actuar + capacidad de comunicarse hacia fuera.** Si las tres "
            "coinciden, hay una vía de exfiltración.",
            "Y hay que ser honestos con la sala: **no existe una defensa completa.** No hay "
            "un filtro que resuelva esto, porque el problema es estructural: el modelo no "
            "puede distinguir de forma fiable entre instrucciones y datos cuando ambos son "
            "texto en el mismo contexto.",
        ]),

        "Lo que sí se puede hacer, y es lo que hay que enseñar: reducir privilegios al "
        "mínimo por tarea; separar el agente que lee contenido no confiable del que tiene "
        "capacidad de actuar; exigir confirmación humana para cualquier acción irreversible o "
        "que envíe datos hacia fuera; delimitar y etiquetar el contenido externo en el prompt "
        "para que al menos esté marcado; validar todas las acciones del lado del servidor; y "
        "registrar todo, porque el módulo 16 es lo que permite detectar que ocurrió.",

        ("sub", "Secretos y variables de entorno"),

        "Tres reglas concretas, en orden de importancia:",

        ("numbers", [
            "**Nunca pasar credenciales al modelo.** Ni en el system prompt, ni como "
            "argumento de una herramienta, ni en un documento indexado. El modelo no las "
            "necesita: las necesita el código que ejecuta la herramienta.",
            "**Las credenciales viven en el servidor de la herramienta**, no en el contexto "
            "del agente. Es exactamente el argumento a favor de los servidores MCP que "
            "señalaba el temario base.",
            "**Todo lo que entra al prompt puede salir.** Un secreto en el contexto es un "
            "secreto que puede aparecer en una respuesta, en un log o en una traza. Enlaza "
            "con la advertencia de privacidad del módulo 16.",
        ]),

        ("sub", "Los riesgos de costo como riesgos de seguridad"),

        "El temario base incluye aquí los bucles de reindexación y es una decisión acertada "
        "que conviene mantener y ampliar: **una vulnerabilidad que vacía el presupuesto es "
        "una denegación de servicio.**",

        ("bullets", [
            "**Bucles de reindexación.** Un proceso que al indexar dispara un evento que "
            "vuelve a indexar. Se corrige con detección de cambios reales por comparación de "
            "contenido y con un tope de reindexaciones por periodo.",
            "**Bucles agénticos sin tope.** Ya visto en los módulos 9 y 14. El límite de "
            "iteraciones es un control de seguridad, no una optimización.",
            "**Amplificación por entrada del usuario.** Un usuario que pega un documento "
            "enorme y dispara un procesamiento costoso. Se corrige con límites de tamaño y "
            "presupuesto por usuario.",
            "**Reintentos sin límite** ante un fallo del proveedor.",
        ]),

        ("sub", "Cerrar con la lista de verificación"),

        "Conviene terminar con algo accionable que se pueda pegar en el repositorio: "
        "credenciales fuera del contexto; validación de salida por código antes de actuar; "
        "autorización del lado del servidor; permisos mínimos por herramienta; confirmación "
        "humana en lo irreversible; límites de iteraciones, de tamaño y de presupuesto; "
        "contenido externo delimitado y tratado como no confiable; y trazas con datos "
        "sensibles redactados antes de emitirse.",
    ],
    "ejercicio": [
        "Ejercicio de equipo rojo sobre el sistema construido en los módulos anteriores. Se "
        "trabaja en parejas cruzadas: cada equipo ataca el sistema de otro.",
        ("numbers", [
            "**Inyección indirecta.** Introducir en el corpus indexado un documento que "
            "contenga instrucciones dirigidas al agente e intentar que las siga.",
            "**Exfiltración.** Intentar que el sistema revele parte de su system prompt, un "
            "dato de otro usuario o el contenido de una variable de entorno.",
            "**Abuso de herramientas.** Intentar que el agente ejecute una acción para la "
            "que el usuario no debería tener permiso.",
            "**Agotamiento de recursos.** Intentar disparar un bucle o un procesamiento "
            "desproporcionado con una entrada pequeña.",
        ]),
        "Cada equipo entrega un informe con lo que consiguió, lo que no, y la corrección "
        "propuesta para cada hallazgo indicando **en qué capa** de la tabla de guardrails "
        "debe implementarse. Después se aplican las correcciones y se repite el ataque.",
    ],
    "evaluacion": [
        "Distingue inyección directa de indirecta y explica por qué la segunda es más grave.",
        "Coloca cada control en la capa correcta y sabe cuáles dependen de que el modelo obedezca.",
        "Sostiene que ninguna decisión de autorización se toma con un campo devuelto por el modelo.",
        "Reconoce la combinación de datos no confiables, capacidad de actuar y salida hacia fuera.",
        "Trata los bucles y el agotamiento de presupuesto como problemas de seguridad.",
        "Mantiene las credenciales fuera del contexto del modelo.",
    ],
}


PARTS = [
    {
        "kicker": "PARTE IV",
        "title": "Operar un sistema",
        "intro": "Un sistema que funciona en la demo y uno que sobrevive en producción se "
                 "diferencian en cuatro cosas: cuánto cuesta, cómo se divide, si se puede "
                 "ver qué está haciendo y si se puede romper desde fuera. Esta parte cubre "
                 "las cuatro. Diez horas.",
        "modules": [M14, M15, M16, M17, M18],
    },
]
