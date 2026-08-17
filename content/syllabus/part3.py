# -*- coding: utf-8 -*-
"""Parte III: construir un sistema (módulos 8 a 13)."""

M8 = {
    "num": 8,
    "title": "Contexto y memoria",
    "tagline": "Si la API no recuerda nada, alguien tiene que decidir qué se guarda, qué se descarta y cuándo. Ese alguien eres tú.",
    "objetivo": "Diseñar la arquitectura de memoria de un sistema de AI decidiendo, con "
                "criterio explícito, qué información se persiste, cuál se recupera y cuál se "
                "descarta.",
    "duracion": "2 horas",
    "dependencias": "Módulo 7.",
    "contenidos": [
        "Por qué hace falta hablar de memoria: consecuencia directa de la ausencia de estado.",
        ("Los tres tipos de memoria y sus límites como metáfora", [
            "Corto plazo: la conversación en curso.",
            "Largo plazo: lo que sobrevive a la sesión.",
            "Persistente: lo que define al usuario o al espacio de trabajo.",
        ]),
        "¿Cuándo guardar y cuándo no? El problema difícil, que sigue abierto.",
        "Estrategias de historial: ventana deslizante, resumen progresivo, memoria selectiva.",
        "El triple costo de la memoria: precisión, latencia y dinero.",
        "Identificadores: sesión, usuario y espacio de trabajo.",
        "Olvidar como decisión de diseño.",
    ],
    "enfoque": [
        ("sub", "Encuadrar la memoria como consecuencia, no como tema nuevo"),

        "El módulo anterior terminó demostrando que la API no guarda nada. Este empieza "
        "aceptando la consecuencia: si el sistema tiene que parecer que recuerda, alguien "
        "tiene que construir ese recuerdo. Ese es todo el módulo.",

        "Conviene enunciar de entrada la afirmación que ordena la sesión: **la memoria de un "
        "sistema de AI no es una función del modelo, es una decisión de arquitectura.** No "
        "existe una implementación correcta universal. Existe la que corresponde al producto "
        "que se está construyendo.",

        ("sub", "La metáfora, y su honestidad"),

        "El temario base expresaba una incomodidad con los términos «corto plazo», "
        "«largo plazo» y «persistente», y esa incomodidad es correcta y "
        "vale la pena compartirla con la sala en lugar de ocultarla. Son términos prestados "
        "de la psicología humana que describen mal lo que ocurre en un sistema real: no hay "
        "consolidación, no hay decaimiento, no hay recuerdo reconstructivo. Hay una base de "
        "datos y una política de qué leer.",

        "La recomendación es mantener los tres nombres, porque son los que la industria usa "
        "y todo el mundo se va a encontrar con ellos, pero traducirlos de inmediato a lo que "
        "significan en código:",

        ("table",
         ["Nombre habitual", "Qué es en realidad", "Dónde vive"],
         [
             ["Memoria de corto plazo",
              "El historial de mensajes que se reenvía en la petición actual.",
              "En la ventana de contexto. Se paga en tokens cada vez."],
             ["Memoria de largo plazo",
              "Hechos extraídos de conversaciones anteriores que se recuperan cuando son "
              "relevantes.",
              "En una base de datos. Solo entra al prompt lo que se decide recuperar."],
             ["Memoria persistente",
              "Datos estables del usuario o del espacio de trabajo: idioma, rol, "
              "preferencias, permisos.",
              "En una base de datos, normalmente relacional. Suele inyectarse siempre."],
         ],
         [3.6, 6.8, 6.1]),

        "Con esa traducción hecha, la discusión deja de ser sobre neurociencia y pasa a ser "
        "sobre lo que realmente es: **qué se lee, de dónde, y en qué momento se pega en el "
        "prompt.**",

        ("sub", "El problema difícil: cuándo guardar"),

        "Este es el punto donde conviene ser honesto con la sala: **no está resuelto.** Es un "
        "área de investigación activa y no hay una respuesta canónica. Presentarlo como un "
        "problema abierto, en lugar de como una técnica que se enseña, es más útil y además "
        "es cierto.",

        "Lo que sí se puede dar es el mapa de las tensiones, que es lo que permite tomar "
        "decisiones razonadas:",

        ("bullets", [
            "**Guardar de más contamina.** Si se persiste todo lo que el usuario dice, en "
            "tres semanas el sistema recupera preferencias que ya cambiaron y las aplica con "
            "confianza. La memoria equivocada es peor que la falta de memoria, porque el "
            "usuario no puede ver qué está influyendo en la respuesta.",
            "**Guardar de menos frustra.** El usuario repite información que ya dio y el "
            "producto se siente tonto.",
            "**Lo que importa depende del contexto de la persona.** «Soy vegetariano» "
            "es un dato permanente en una app de recetas y ruido irrelevante en una "
            "herramienta de facturación. No hay criterio universal.",
            "**Todo lo recuperado se paga.** Cada hecho que se inyecta son tokens en cada "
            "petición, para siempre.",
        ]),

        "Los enfoques que se usan en la práctica, presentados sin recomendar uno: extracción "
        "explícita por el propio modelo tras cada sesión, memoria confirmada por el usuario "
        "—que es más lenta pero mucho más segura—, memoria derivada de acciones en lugar de "
        "declaraciones, y caducidad por tiempo o por desuso.",

        ("sub", "Estrategias de historial"),

        "Frente al problema concreto de que la conversación no cabe, hay cuatro estrategias y "
        "conviene que se conozcan las cuatro con sus costos:",

        ("table",
         ["Estrategia", "Cómo funciona", "Qué se pierde"],
         [
             ["Ventana deslizante",
              "Se conservan los últimos N mensajes o los últimos N tokens.",
              "Todo lo anterior, de golpe y sin aviso. Además rompe el caché de prompts, "
              "porque cambia el prefijo."],
             ["Resumen progresivo",
              "Al superar un umbral, se pide al modelo que resuma lo viejo y se sustituye por "
              "el resumen.",
              "Detalle. Y cada resumen se hace sobre el resumen anterior, así que el error se "
              "acumula. Cuesta una llamada extra."],
             ["Memoria selectiva",
              "Se extraen hechos concretos y se guardan aparte; el historial crudo se "
              "descarta.",
              "El matiz conversacional. Requiere resolver el problema difícil de qué "
              "extraer."],
             ["Recuperación del historial",
              "Se indexa la conversación y se recuperan solo los fragmentos relevantes al "
              "turno actual. Es RAG aplicado al historial.",
              "La continuidad narrativa. Necesita toda la infraestructura del módulo 13."],
         ],
         [3.4, 6.6, 6.5]),

        ("box", "nota", "Un detalle de implementación que ahorra dinero", [
            "Truncar el historial **por el principio** invalida el caché de prompts en cada "
            "petición, porque el prefijo cambia. Es una de las formas más comunes y menos "
            "visibles de tirar dinero.",
            "Cuando sea posible, conviene mantener estable el bloque inicial —system prompt, "
            "definiciones de herramientas, resumen consolidado— y que la parte que rota sea "
            "solo la cola. Se cuantifica en el módulo 14.",
        ]),

        ("sub", "El triple costo, que es el mensaje que hay que dejar"),

        "El temario base lo planteaba bien y conviene conservarlo como cierre: la memoria "
        "tiene tres costos simultáneos y hay que verlos juntos.",

        ("numbers", [
            "**Precisión.** Más contexto no es más precisión. Un historial largo diluye la "
            "señal relevante, y una memoria equivocada produce respuestas confiadamente "
            "incorrectas.",
            "**Latencia.** Cada token de entrada se procesa antes de generar el primero de "
            "salida. Un contexto grande se nota en el tiempo de respuesta.",
            "**Dinero.** Cada token de memoria se paga en cada petición.",
        ]),

        "De ahí sale la reformulación que conviene dejar escrita: **olvidar no es una "
        "limitación del sistema, es una función que hay que diseñar.** Un sistema que nunca "
        "olvida es un sistema que se vuelve más caro, más lento y menos preciso con cada "
        "conversación.",

        ("sub", "Identificadores"),

        "Cierra bien el módulo aterrizando en la parte concreta, que además prepara el "
        "módulo 11: para recuperar cualquier cosa hay que saber a quién pertenece. Tres "
        "niveles que conviene tener desde el primer día porque añadirlos después duele: "
        "identificador de **sesión** para reconstruir una conversación, de **usuario** para "
        "la memoria persistente, y de **espacio de trabajo** o cuenta para aislar datos "
        "entre clientes. Ese último es además un requisito de seguridad, no solo de "
        "organización.",

        "Estos mismos identificadores son los que permiten correlacionar trazas en el módulo "
        "16, así que conviene mencionarlo para que se diseñen una sola vez.",
    ],
    "ejercicio": [
        "Tomar el chat de consola del módulo 7 y añadirle memoria en tres capas:",
        ("numbers", [
            "**Corto plazo con resumen.** Al superar un umbral de tokens, resumir los "
            "mensajes antiguos con una llamada al modelo y sustituirlos por el resumen, "
            "conservando intactos los últimos turnos.",
            "**Largo plazo.** Al terminar la sesión, extraer con el modelo una lista de "
            "hechos sobre el usuario en formato estructurado y guardarlos en un archivo "
            "JSON, con fecha.",
            "**Persistente.** Al iniciar, cargar esos hechos e inyectarlos en el system "
            "prompt.",
        ]),
        "La entrega incluye una reflexión escrita de un párrafo sobre **qué hechos decidió "
        "guardar el sistema que no debería haber guardado**, después de tres sesiones de "
        "prueba. Ese hallazgo es el objetivo real del ejercicio.",
    ],
    "evaluacion": [
        "Traduce los tres tipos de memoria a decisiones concretas de almacenamiento y recuperación.",
        "Elige una estrategia de historial justificándola con sus costos, no por costumbre.",
        "Explica el triple costo de la memoria y por qué olvidar es una función a diseñar.",
        "Reconoce el riesgo de la memoria equivocada frente al de la memoria ausente.",
        "Diseña el esquema de identificadores de sesión, usuario y espacio de trabajo.",
    ],
}


M9 = {
    "num": 9,
    "title": "Agentes",
    "tagline": "Primero qué necesita un agente, que no cambia. Después con qué se implementa hoy, que sí cambia.",
    "objetivo": "Reconocer y diseñar un agente en términos de sus componentes conceptuales, "
                "y traducir después esos componentes a las implementaciones concretas de "
                "cada proveedor.",
    "duracion": "3 horas",
    "dependencias": "Módulos 5, 7 y 8.",
    "contenidos": [
        ("9.1 Qué necesita un agente (parte conceptual)", [
            "Los siete componentes: objetivo, memoria, herramientas, planificación, observación, acción y reflexión.",
            "El bucle: percibir, decidir, actuar, observar, corregir.",
            "Qué NO es un agente.",
            "Flujos de trabajo: por qué muchos no necesitan un agente.",
            "El criterio de decisión entre flujo determinista y agente.",
        ]),
        ("9.2 Cómo se implementa hoy (parte volátil)", [
            "System prompt: el objetivo hecho texto.",
            "Uso de herramientas: cómo el modelo pide ejecutar algo.",
            "Skills: definiciones de cómo hacer algo, y en qué se diferencian de las herramientas.",
            "Subagentes y delegación.",
            "MCP: por qué es un protocolo y no una función de producto.",
        ]),
    ],
    "enfoque": [
        ("box", "nota", "Por qué este módulo está partido en dos", [
            "El temario base listaba «system prompt, agente, flujos de trabajo, tools, "
            "MCP, skills» como una sola secuencia. El riesgo de esa estructura es que "
            "el conocimiento caduca con la herramienta: quien aprende «un agente es "
            "skills más MCP» se queda sin nada cuando cambien los nombres.",
            "La división propuesta separa lo que dura de lo que no. **La sección 9.1 no "
            "menciona ni una sola marca.** La 9.2 está llena de ellas, y está marcada como "
            "volátil para que se revise antes de cada impartición.",
        ]),

        ("h3", "9.1 · Qué necesita un agente"),

        ("sub", "Definir por composición, no por eslogan"),

        "Las definiciones de agente que circulan son inútiles porque son circulares: «un "
        "sistema que actúa de forma autónoma». Conviene sustituirlas por una "
        "descomposición, que además tiene la ventaja de ser una lista de verificación de "
        "diseño.",

        ("table",
         ["Componente", "Qué significa", "Qué falla si no está"],
         [
             ["Objetivo", "Qué se está intentando lograr, y cómo se sabe que terminó.",
              "El agente no sabe cuándo parar. Es la causa más común de bucles infinitos."],
             ["Memoria", "Qué recuerda dentro de la tarea y entre tareas.",
              "Repite pasos que ya hizo y pierde lo aprendido a mitad de camino."],
             ["Herramientas", "Con qué puede consultar el mundo y actuar sobre él.",
              "Solo puede hablar. Se convierte en un chat con instrucciones."],
             ["Planificación", "Cómo descompone el objetivo en pasos.",
              "Ataca todo de golpe y falla en tareas de varios pasos."],
             ["Observación", "Cómo lee el resultado de lo que hizo.",
              "Actúa a ciegas y no detecta que un paso falló."],
             ["Acción", "Cómo ejecuta, con qué permisos y qué es reversible.",
              "O no puede hacer nada, o puede hacer demasiado. Ambos extremos son problemas."],
             ["Reflexión", "Cómo evalúa si va bien y corrige el rumbo.",
              "Insiste en una estrategia que no funciona hasta agotar el presupuesto."],
         ],
         [2.8, 6.4, 7.3]),

        "El ejercicio que hace útil esta tabla es aplicarla a algo que la sala conozca. "
        "Tomar un agente de código que usen a diario e identificar los siete componentes en "
        "voz alta funciona muy bien: el objetivo está en la petición del usuario, la memoria "
        "en el historial y en los archivos del proyecto, las herramientas son leer y "
        "escribir archivos y ejecutar comandos, la planificación es la lista de tareas que "
        "muestra, la observación es la salida de cada comando, la acción son las "
        "modificaciones al disco, y la reflexión es lo que hace cuando una prueba falla.",

        ("sub", "El bucle"),

        "Con los componentes en la mesa, el bucle se explica solo y conviene dibujarlo:",

        ("code",
         "  objetivo\n"
         "     │\n"
         "     ▼\n"
         "  decidir  ──►  actuar  ──►  observar\n"
         "     ▲                           │\n"
         "     └───────  reflexionar  ◄────┘\n"
         "\n"
         "  (hasta cumplir el objetivo, agotar el presupuesto\n"
         "   o alcanzar el límite de iteraciones)"),

        "Lo que hay que subrayar de ese dibujo es la condición de salida. **Un bucle sin "
        "límite duro de iteraciones no es un agente, es un incidente de facturación "
        "esperando su turno.** El límite no es una optimización: es parte de la definición "
        "de un agente bien construido. Se retoma con números en el módulo 14 y como riesgo "
        "de seguridad en el 18.",

        ("sub", "Qué no es un agente"),

        "Delimitar es tan importante como definir, y el temario base ya lo pedía. Tres cosas "
        "que se llaman agente y no lo son:",

        ("bullets", [
            "**Un chat con un system prompt elaborado.** Tiene objetivo, pero no tiene "
            "herramientas, ni observación, ni bucle. Es un modelo con instrucciones.",
            "**Una cadena fija de llamadas al modelo.** Extraer, luego clasificar, luego "
            "redactar. Es un flujo de trabajo: quien decide los pasos es el código, no el "
            "modelo. Y muchas veces es la solución correcta.",
            "**Una llamada con una herramienta disponible.** Si el modelo puede llamar una "
            "función y responder, pero no hay iteración ni corrección, es uso de "
            "herramientas, no un agente.",
        ]),

        ("sub", "El criterio de decisión, que es el punto práctico del módulo"),

        "La pregunta que hay que dejar instalada es cuándo conviene un agente y cuándo un "
        "flujo determinista, porque el sesgo del momento empuja hacia el agente incluso "
        "donde perjudica.",

        ("table",
         ["Si...", "Entonces..."],
         [
             ["Los pasos se conocen de antemano y siempre son los mismos",
              "Flujo de trabajo. Más barato, más rápido, más predecible y mucho más fácil de depurar."],
             ["Los pasos dependen de lo que se vaya encontrando",
              "Agente."],
             ["El costo de un error es alto y difícil de revertir",
              "Flujo, o agente con confirmación humana antes de cada acción irreversible."],
             ["El espacio de posibles caminos es grande y no se puede enumerar",
              "Agente."],
             ["Hace falta que el resultado sea reproducible",
              "Flujo. Un agente no garantiza el mismo camino dos veces."],
         ],
         [8.0, 8.5]),

        "La frase que conviene dejar dicha: **un flujo de trabajo no necesita un agente para "
        "ser un sistema de AI.** Muchas de las mejores arquitecturas son flujos deterministas "
        "con llamadas al modelo en los puntos donde hace falta juicio, y nada más.",

        ("h3", "9.2 · Cómo se implementa hoy"),

        ("box", "volatil", "Sección con fecha de caducidad", [
            "Todo lo que sigue describe productos y protocolos concretos que cambian rápido. "
            "Conviene revisar esta sección contra la documentación oficial antes de cada "
            "impartición, y advertir a la sala de que lo está haciendo.",
            "Lo anterior —los siete componentes, el bucle, el criterio de decisión— no "
            "necesita esa revisión. Esa es la razón de la división.",
        ]),

        ("sub", "El objetivo se escribe como system prompt"),

        "El temario base acertaba al hacer del system prompt la puerta de entrada a los "
        "agentes, y conviene conservar ese orden. El puente es directo: el primer componente "
        "de la lista es el objetivo, y el objetivo se materializa como texto en el system "
        "prompt. Quién es el agente, qué está intentando lograr, qué puede y qué no puede "
        "hacer, y cómo sabe que terminó.",

        "Como el módulo 5 ya cubrió cómo se escribe un buen prompt, aquí solo hace falta "
        "añadir lo específico de un agente: las condiciones de terminación explícitas, las "
        "restricciones sobre acciones irreversibles, y qué hacer cuando una herramienta "
        "falla.",

        ("sub", "Uso de herramientas: el mecanismo real"),

        "Conviene desmitificarlo porque suena más complicado de lo que es. El modelo **no "
        "ejecuta nada**. Esto es una consecuencia directa del módulo 4 y merece repetirse.",

        ("numbers", [
            "En la petición se incluye una lista de herramientas disponibles, cada una con "
            "nombre, descripción y esquema de parámetros.",
            "El modelo, en lugar de texto, produce una salida estructurada que dice: quiero "
            "llamar a esta herramienta con estos argumentos.",
            "**El código de quien construye** ejecuta la función. El modelo se queda esperando.",
            "El resultado se añade al historial y se hace una petición nueva con todo el "
            "contexto acumulado.",
            "El modelo lee el resultado y decide: otra herramienta, o responder.",
        ]),

        "Dos observaciones que valen la sesión. La primera: **la descripción de la "
        "herramienta es prompt engineering.** Es el único texto que el modelo lee para "
        "decidir si la usa y con qué argumentos. Una descripción ambigua produce llamadas "
        "erróneas, y el arreglo es reescribirla, no cambiar el modelo. La segunda: **cada "
        "vuelta del bucle reenvía todo el contexto acumulado.** Diez pasos no cuestan diez "
        "veces uno, cuestan bastante más. Es el mismo efecto acumulativo del módulo 7, ahora "
        "multiplicado.",

        ("sub", "Skills y su diferencia con las herramientas"),

        "El temario base pedía explícitamente no confundir skills con MCP, y tenía razón "
        "porque es una confusión frecuente. La distinción que funciona es por **qué tipo de "
        "cosa es cada una**:",

        ("table",
         ["Concepto", "Qué es", "Analogía"],
         [
             ["Herramienta", "Una función que el agente puede ejecutar. Es capacidad.",
              "Un verbo: leer un archivo, consultar la base, enviar un correo."],
             ["Skill", "Instrucciones sobre cómo hacer bien algo, que se cargan cuando son "
                       "relevantes. Es conocimiento procedimental.",
              "Un manual: cómo redactamos aquí una propuesta comercial."],
             ["Servidor MCP", "Un canal estandarizado por el que llegan herramientas y datos "
                              "desde fuera. Es transporte.",
              "Un enchufe: no es la herramienta, es por donde se conecta."],
         ],
         [3.0, 7.2, 6.3]),

        "La frase que resuelve la confusión: **una skill no hace nada por sí sola, describe "
        "cómo hacerlo; una herramienta sí hace algo; MCP es por dónde llega.** Se pueden "
        "tener las tres a la vez y normalmente se tienen.",

        "El valor real de las skills, y conviene decirlo porque conecta con el módulo 17, es "
        "que resuelven un problema de contexto: en vez de meter todos los procedimientos de "
        "la empresa en el system prompt —caro y ruidoso—, se cargan solo cuando la tarea los "
        "necesita. Es carga de contexto bajo demanda, el mismo principio del módulo 15.",

        ("sub", "MCP, mencionado y aplazado"),

        "Aquí conviene resistir la tentación de explicarlo entero. Basta con situarlo: **MCP "
        "no es una función de un proveedor, es un protocolo abierto**, y por eso mismo se "
        "estudia en el módulo siguiente junto a los demás protocolos de comunicación, donde "
        "se entiende mejor por comparación.",

        "Lo único que hay que dejar dicho aquí es por qué le importa a un agente: sin un "
        "estándar, cada integración se escribe a mano para cada cliente de AI. Con uno, un "
        "servidor sirve para todos. Y el detalle de seguridad que el temario base ya "
        "señalaba con buen criterio: un servidor MCP es una frontera controlada. El agente "
        "no toca la base de datos, le pide a un servidor que lo haga, y ese servidor decide "
        "qué está permitido. El módulo 18 matiza hasta dónde llega esa protección.",
    ],
    "ejercicio": [
        "Dos partes.",
        ("numbers", [
            "**Análisis (30 min).** Elegir una herramienta de AI que el equipo use a diario "
            "y documentar sus siete componentes en una tabla, con evidencia observable de "
            "cada uno. Después responder: ¿es un agente, un flujo de trabajo, o un híbrido? "
            "¿Por qué?",
            "**Construcción.** Implementar un agente mínimo, sin frameworks, con tres "
            "herramientas: una de lectura, una de escritura y una de consulta externa. "
            "Requisitos obligatorios: límite duro de iteraciones, registro de cada llamada "
            "con sus argumentos y su resultado, y confirmación explícita antes de cualquier "
            "acción irreversible.",
        ]),
        "La entrega incluye la traza completa de una ejecución en la que el agente **falla y "
        "se recupera**. Si no falla nunca, el caso de prueba es demasiado fácil.",
    ],
    "evaluacion": [
        "Descompone cualquier sistema de AI en los siete componentes sin recurrir a nombres de producto.",
        "Justifica con criterio cuándo un problema pide un agente y cuándo un flujo determinista.",
        "Explica el mecanismo real del uso de herramientas, incluyendo que el modelo no ejecuta nada.",
        "Distingue herramienta, skill y servidor MCP.",
        "Implementa un bucle con límite de iteraciones y confirmación en acciones irreversibles.",
    ],
}


M10 = {
    "num": 10,
    "title": "Protocolos de comunicación: API, REST, webhooks y MCP",
    "tagline": "Todos son lo mismo visto desde ángulos distintos: un contrato entre dos sistemas que no se conocen.",
    "objetivo": "Explicar los cuatro protocolos que aparecen en un sistema de AI como "
                "variaciones de una misma idea, y elegir el adecuado según quién inicia la "
                "comunicación y quién consume el mensaje.",
    "duracion": "2.5 horas",
    "dependencias": "Módulos 7 y 9.",
    "contenidos": [
        "Qué es un protocolo: quién habla primero, en qué formato, y qué pasa si falla.",
        "Tres palabras que no son sinónimos: API, REST y HTTP.",
        "REST y el modelo pull. Idempotencia y el costo del sondeo.",
        "Webhooks y el modelo push. Firmas, entrega repetida y orden no garantizado.",
        "Streaming: SSE y WebSockets.",
        "El uso de herramientas como protocolo implícito entre el modelo y el código.",
        ("MCP", [
            "El problema N × M que resuelve.",
            "Arquitectura: host, cliente y servidor.",
            "Transportes: proceso local y HTTP remoto.",
            "Las tres primitivas, explicadas por quién las controla.",
            "Por qué existe si ya hay APIs.",
            "Qué no es MCP, y su superficie de seguridad.",
        ]),
        "Los cuatro lado a lado.",
    ],
    "enfoque": [
        ("box", "nota", "Agrupación nueva respecto al borrador base", [
            "En el temario base, MCP aparecía dentro del módulo de agentes, junto a las "
            "skills. Aquí se reagrupa con REST y los webhooks siguiendo la observación de la "
            "retro: **todos son protocolos de comunicación**, y se entienden mucho mejor por "
            "comparación que por separado.",
            "El módulo se coloca **después** de agentes de forma deliberada: MCP resuelve un "
            "problema que no existe si no se ha visto antes qué es un agente con "
            "herramientas.",
        ]),

        ("sub", "El hilo conductor"),

        "El módulo tiene que sentirse como una idea vista desde cuatro ángulos, no como "
        "cuatro temas sueltos. La idea es: **un protocolo es un contrato entre dos sistemas "
        "que no se conocen entre sí.** Define quién habla primero, en qué formato, qué "
        "significa cada respuesta y qué ocurre cuando algo falla. Todo lo demás son "
        "variaciones sobre quién inicia y quién es el consumidor final del mensaje.",

        "Con ese marco, MCP deja de parecer una moda y se convierte en el siguiente escalón "
        "lógico de una serie que la sala ya conoce.",

        ("sub", "Desambiguar tres palabras"),

        "Antes de nada conviene separar tres términos que en conversación se usan como "
        "sinónimos y no lo son, porque esa confusión se lleva la mitad de las preguntas del "
        "módulo:",

        ("bullets", [
            "**API** es el contrato: qué operaciones existen, qué reciben y qué devuelven.",
            "**REST** es un estilo para diseñar ese contrato sobre HTTP, con recursos y verbos.",
            "**HTTP** es el transporte.",
        ]),

        "Una API puede no ser REST —existen GraphQL, gRPC y otras—, y REST siempre necesita "
        "un transporte debajo. Fijar esto de entrada prepara además la pregunta clave del "
        "módulo, porque MCP es un protocolo cuyo transporte puede ser HTTP o incluso la "
        "entrada y salida estándar de un proceso local.",

        ("sub", "REST: lo poco que hay que decir, y lo que sí importa"),

        "El público conoce REST, así que repasarlo entero sería desperdiciar la sesión. Solo "
        "hay dos puntos que importan para lo que viene.",

        "El primero es la **idempotencia**. En sistemas de AI los tiempos de espera se agotan "
        "con frecuencia y los reintentos son la norma. Un reintento sobre una operación no "
        "idempotente cobra dos veces, duplica un registro o envía dos correos. No es un "
        "tecnicismo: es el fallo que más veces aparece en producción.",

        "El segundo es el **modelo pull**: en REST el cliente siempre pregunta y el servidor "
        "nunca inicia. Si hace falta saber cuándo terminó algo que tarda horas, la única "
        "opción es preguntar en ciclo, y ahí aparece el compromiso incómodo de siempre. "
        "Preguntar seguido gasta peticiones y dinero para recibir casi siempre «todavía "
        "no»; preguntar poco significa enterarse tarde. Casi todo el mundo elige mal ese "
        "intervalo, y es la limitación que da origen a los webhooks.",

        ("sub", "Webhooks: la inversión, y lo que cuesta"),

        "Se presentan exactamente como esa inversión: en lugar de preguntar, se deja una "
        "dirección y el otro sistema avisa. En AI los casos son cercanos y concretos: el "
        "resultado de un lote procesado de forma asíncrona, el fin de un trabajo de fine "
        "tuning, una transcripción larga.",

        "Lo que hay que dejar claro es que no es gratis, porque el costo suele ser una "
        "sorpresa: **al recibir un webhook, el servidor propio se convirtió en el servidor "
        "de alguien más.**",

        ("bullets", [
            "**Verificar la firma es obligatorio.** Sin eso, cualquiera puede fabricar "
            "eventos falsos contra un endpoint público.",
            "**La entrega es al menos una vez.** El mismo evento va a llegar dos veces. La "
            "idempotencia deja de ser una buena práctica y pasa a ser un requisito.",
            "**El orden no está garantizado.** Puede llegar antes el evento de «completado» "
            "que el de «iniciado».",
            "**Hay que responder rápido y procesar después.** Encolar el evento y devolver "
            "de inmediato. Procesar dentro del manejador hace que el emisor agote su tiempo "
            "de espera y reenvíe todo otra vez, multiplicando el problema.",
            "**Hace falta un endpoint público**, y un túnel para poder desarrollar en local.",
        ]),

        ("sub", "Streaming, brevemente"),

        "Cinco minutos, con el objetivo de conectar con algo que ya vieron en el módulo 7: "
        "cuando los tokens aparecen uno a uno en un chat, eso es **SSE** —un canal "
        "unidireccional del servidor al cliente sobre HTTP normal—, no magia ni WebSockets. "
        "Los **WebSockets** aparecen cuando hace falta bidireccionalidad real, como en las "
        "APIs de voz.",

        ("sub", "El uso de herramientas como protocolo implícito"),

        "Vale la pena nombrarlo aquí aunque se viera en el módulo 9, porque encaja en la "
        "serie: cuando el modelo emite una llamada estructurada y el código responde con un "
        "resultado, eso también es un contrato. Tiene formato definido, tiene un iniciador —el "
        "modelo— y tiene un consumidor —el código—. Verlo como protocolo hace que MCP se "
        "entienda como su estandarización, que es exactamente lo que es.",

        ("sub", "MCP: el problema que resuelve"),

        "El problema es de multiplicación. Con tres clientes de AI distintos y quince "
        "sistemas internos, sin un estándar hacen falta cuarenta y cinco integraciones "
        "escritas a mano, cada una acoplada a su cliente. MCP define un formato común para "
        "que cualquier cliente que lo hable pueda usar cualquier servidor de capacidades.",

        "La arquitectura son tres piezas: el **host** —la aplicación de AI—, el **cliente** "
        "—la parte del host que habla el protocolo— y el **servidor** —el proceso que expone "
        "las capacidades—.",

        "De los **transportes** hay dos, y es lo primero que se decide en la práctica:",

        ("table",
         ["Transporte", "Cómo funciona", "Cuándo conviene"],
         [
             ["Proceso local (stdio)",
              "El servidor es un proceso que se comunica por entrada y salida estándar.",
              "Herramientas de escritorio y línea de comandos. Ventaja fuerte: nada sale a "
              "la red."],
             ["HTTP remoto",
              "El servidor es un servicio al que se conecta por red.",
              "Servidores compartidos y multiusuario. Requiere autenticación y autorización "
              "de verdad."],
         ],
         [4.0, 6.2, 6.3]),

        "Las **tres primitivas** conviene explicarlas por quién las controla, que es el "
        "ángulo que las vuelve comprensibles y además da criterio para diseñar un servidor "
        "propio:",

        ("table",
         ["Primitiva", "Quién la controla", "Qué es"],
         [
             ["Tools", "El modelo", "Acciones que el modelo decide invocar. Tienen efectos."],
             ["Resources", "La aplicación", "Datos de solo lectura que el host decide adjuntar al contexto."],
             ["Prompts", "El usuario", "Plantillas que la persona invoca de forma deliberada."],
         ],
         [3.0, 3.6, 9.9],
         "Sin esta tabla, la tentación es meter todo como herramientas. Con ella, hay criterio."),

        ("sub", "La pregunta que alguien va a hacer en voz alta"),

        ("box", "correccion", "¿Por qué existe MCP si ya hay APIs?", [
            "La respuesta corta es que **cambia quién lee el contrato.**",
            "Una API REST la lee una persona desarrolladora, la entiende y escribe código "
            "que la llama. El contrato se resuelve antes de ejecutar.",
            "Un servidor MCP lo lee **el modelo, en tiempo de ejecución**: pregunta qué "
            "herramientas hay, recibe descripciones escritas para ser interpretadas por un "
            "modelo, y decide cuál usar. Por eso se puede conectar un servidor nuevo a un "
            "agente y que sepa usarlo sin recompilar ni redesplegar nada.",
            "Y de ahí se sigue algo que conecta con el módulo 5: **la calidad de las "
            "descripciones de las herramientas es un problema de prompt engineering, no de "
            "documentación.**",
        ]),

        ("sub", "Qué no es MCP"),

        "Conviene cerrar bajando expectativas, porque las expectativas infladas hacen más "
        "daño que el desconocimiento:",

        ("bullets", [
            "**No reemplaza a REST.** La mayoría de los servidores MCP son una envoltura que "
            "por debajo llama a una API REST.",
            "**No es un protocolo de comunicación entre agentes.** Es entre un host de AI y "
            "un proveedor de capacidades.",
            "**No da seguridad: da un lugar donde ponerla.** Cada servidor conectado es "
            "superficie de ataque nueva, y todo lo que devuelve entra al contexto como texto "
            "que el modelo va a leer y puede obedecer. Conectar un servidor de terceros es "
            "darle acceso al contexto a código ajeno.",
        ]),

        "Ese último punto enlaza directamente con el módulo 18 y conviene enunciarlo como "
        "regla: **todo resultado de una herramienta es contenido no confiable.**",

        ("sub", "Cerrar con la comparación"),

        ("table",
         ["Protocolo", "Quién inicia", "Sincronía", "Quién consume", "Cuándo usarlo"],
         [
             ["REST", "El cliente", "Petición y respuesta", "Código",
              "Operaciones bajo demanda con respuesta inmediata."],
             ["Webhook", "El servidor remoto", "Asíncrono", "Código",
              "Eventos impredecibles o trabajos largos."],
             ["SSE / WebSocket", "El cliente abre, el servidor emite", "Flujo continuo",
              "Código o interfaz", "Streaming de tokens, voz, actualizaciones en vivo."],
             ["MCP", "El host o el agente", "Petición y respuesta", "**El modelo**",
              "Dar capacidades descubribles a un agente."],
         ],
         [2.4, 3.4, 3.0, 2.6, 5.2]),

        "La última columna de la penúltima fila es la que resume el módulo: **MCP es el único "
        "de los cuatro cuyo consumidor es el modelo y no el código.** Esa es toda la "
        "diferencia.",
    ],
    "ejercicio": [
        "Construir un servidor MCP mínimo, con transporte local, que exponga:",
        ("bullets", [
            "Una **tool** que consulte algo real del entorno de trabajo.",
            "Un **resource** de solo lectura con un documento de referencia.",
            "Un **prompt** con una plantilla de uso frecuente en el equipo.",
        ]),
        "Conectarlo a un cliente MCP real y verificar que el agente lo descubre y lo usa sin "
        "configuración adicional.",
        "La entrega escrita responde a dos preguntas: **¿por qué cada capacidad se modeló "
        "como tool, resource o prompt y no como otra cosa?** y **¿qué podría hacer un "
        "atacante que controlara el texto que devuelve la tool?**",
    ],
    "evaluacion": [
        "Explica los cuatro protocolos como variaciones de un mismo contrato de comunicación.",
        "Distingue API, REST y HTTP sin usarlos como sinónimos.",
        "Enumera las obligaciones reales de recibir un webhook, incluidas firma e idempotencia.",
        "Clasifica correctamente una capacidad como tool, resource o prompt.",
        "Articula por qué existe MCP en términos de quién lee el contrato.",
        "Reconoce que la salida de una herramienta es contenido no confiable.",
    ],
}


M11 = {
    "num": 11,
    "title": "Bases de datos para sistemas de AI",
    "tagline": "Por qué recuperar contexto con las herramientas de siempre es difícil, y qué aparece cuando dejan de alcanzar.",
    "objetivo": "Identificar las limitaciones de la recuperación léxica para gestionar "
                "contexto, y situar cada tipo de base de datos según el problema que "
                "resuelve.",
    "duracion": "2 horas",
    "dependencias": "Módulo 8.",
    "contenidos": [
        "Recuperación léxica en una base de datos tradicional: por coincidencia y por identificador.",
        "Control de contexto por sesión y por espacio de trabajo.",
        "Índices: qué aceleran y qué no.",
        "Por qué una base relacional gestiona mal el contexto de un sistema de AI.",
        "Bases de datos de grafos: cuando lo que importa son las relaciones.",
        "Bases de datos vectoriales: introducción como puente al módulo 12.",
        "La base de datos depende de lo que se quiera almacenar.",
    ],
    "enfoque": [
        ("sub", "El encuadre: qué problema tiene lo que ya sabemos hacer"),

        "El temario base plantea este módulo como una escalera de limitaciones —qué le falta "
        "a la arquitectura de datos habitual para servir a un sistema de AI, y qué aparece "
        "cuando eso no alcanza— y ese encuadre se conserva íntegro porque funciona bien con "
        "un público que ya conoce SQL.",

        "El punto de partida es concreto: en una base relacional se recupera por coincidencia "
        "exacta, por patrón o por identificador. Se busca lo que **se parece a nivel de "
        "caracteres**, no lo que significa lo mismo. Un usuario que pregunta por «cómo "
        "devuelvo un producto» no encuentra el documento titulado «política de "
        "reembolsos» aunque sea exactamente lo que necesita, porque no comparten ni una "
        "palabra clave.",

        "Conviene reconocer también lo que sí hace bien, para que la escalera no suene a "
        "desprecio: para recuperar el pedido 4821, la base relacional es insuperable. Rápida, "
        "exacta, transaccional y barata. **Nadie debería usar recuperación semántica para "
        "buscar un registro por identificador**, y esa frase hay que decirla aquí porque en "
        "el módulo 13 va a hacer falta.",

        ("sub", "Sesiones, espacios de trabajo e índices"),

        "Esta parte es la que conecta con el módulo 8 y conviene tratarla como diseño, no "
        "como repaso de SQL. Un sistema de AI multiusuario necesita, como mínimo, poder "
        "responder tres preguntas: qué se dijo en esta conversación, qué sabemos de este "
        "usuario, y qué datos pertenecen a este cliente y no pueden mezclarse con los de "
        "otro.",

        "Sobre los índices, el mensaje útil es qué **no** resuelven. Un índice acelera la "
        "búsqueda por un valor conocido. No hace que la búsqueda entienda sinónimos, ni que "
        "encuentre un párrafo que dice lo mismo con otras palabras. **El problema de la "
        "recuperación de contexto no es de velocidad, es de criterio de coincidencia**, y "
        "por eso ningún índice tradicional lo resuelve.",

        ("sub", "El diagnóstico que justifica el resto de la parte"),

        "Vale la pena enunciarlo con claridad porque es la bisagra del módulo. Los registros "
        "de una base de datos son datos planos: tienen un valor y ya. El contexto de un "
        "sistema de AI tiene **significado**, y el significado no se indexa por coincidencia "
        "de caracteres. Cargar el contexto correcto por métodos léxicos es impreciso y "
        "lento, y en cuanto el volumen crece deja de ser viable.",

        ("sub", "Bases de datos de grafos"),

        ("box", "correccion", "Errata corregida respecto al borrador base", [
            "En el párrafo de enfoque del temario base se lee: «comenzando con las bases "
            "de datos vectoriales que nos permiten guardar contexto por temas o por áreas, "
            "para que su recuperación sea más sencilla y precisa, si yo sé que un nodo "
            "corresponde al tema que necesito solo recupero eso», y a continuación "
            "«ahí sí escalar a las bases de datos vectoriales».",
            "La misma expresión aparece dos veces para dos cosas distintas. Por el contenido "
            "—nodos, temas, áreas— el primer caso describe **bases de datos de grafos**. La "
            "escalera que el temario propone es tradicional → **grafos** → vectorial, y así "
            "queda corregida.",
            "El orden y el argumento del temario base se conservan sin cambios: solo se "
            "corrige el nombre.",
        ]),

        "Una base de grafos almacena entidades como nodos y relaciones como aristas, y su "
        "fortaleza es recorrer esas relaciones. La pregunta que resuelve bien no es «qué "
        "documento habla de esto» sino «qué está conectado con qué, y a cuántos "
        "saltos».",

        "En sistemas de AI aparece en dos casos claros: cuando el contexto relevante se "
        "define por pertenencia —este tema, esta área, este proyecto— y cuando la respuesta "
        "depende de relaciones que habría que reconstruir con muchos joins. Un grafo también "
        "tiene una ventaja que conviene mencionar de cara al módulo 16: **el camino "
        "recorrido es legible**, y eso hace que la recuperación sea explicable, algo que la "
        "búsqueda vectorial no ofrece con la misma facilidad.",

        "Y tiene el límite que el temario base ya identificaba: los nodos crecen, el contexto "
        "por nodo crece, y llega un punto en que saber en qué nodo buscar vuelve a ser el "
        "problema original.",

        ("sub", "Bases de datos vectoriales, solo como puerta"),

        "Aquí conviene contenerse deliberadamente. Este módulo solo abre la puerta; el "
        "contenido está en los dos siguientes.",

        "Lo que hay que dejar dicho es la idea, no el mecanismo: existe una forma de "
        "representar un texto como una lista de números tal que **textos con significado "
        "parecido producen listas de números parecidas**. Si eso es posible, entonces buscar "
        "por significado se convierte en buscar números cercanos, que es un problema "
        "computacional que sí sabemos resolver rápido.",

        ("box", "alerta", "Contener la explicación aquí", [
            "Es tentador explicar los embeddings en este momento porque la pregunta va a "
            "surgir. Conviene resistirlo y decir explícitamente que el módulo siguiente se "
            "dedica entero a eso.",
            "El motivo es que una base vectorial sin entender embeddings se percibe como "
            "magia, y eso es exactamente lo que este programa intenta evitar. Primero el "
            "embedding, después dónde se guarda.",
        ]),

        ("sub", "Cerrar con la idea que da nombre al módulo"),

        "El temario base termina este bloque con «la base de datos depende de lo que "
        "queramos almacenar», y es un buen cierre. Conviene reforzarlo con una "
        "aclaración: no se está describiendo una evolución en la que cada tecnología "
        "sustituye a la anterior. **En un sistema real conviven.** Los pedidos en la "
        "relacional, las relaciones entre entidades en el grafo si hace falta, y los "
        "documentos indexados por significado en la vectorial. Elegir una para todo es el "
        "error, no elegir la más nueva.",
    ],
    "ejercicio": [
        "Sobre una base de datos real del equipo, o una de ejemplo con documentos de texto:",
        ("numbers", [
            "Escribir cinco preguntas que un usuario haría en lenguaje natural.",
            "Intentar responderlas con búsqueda léxica y registrar cuántas se resuelven bien, "
            "cuántas devuelven ruido y cuántas no devuelven nada.",
            "Para cada fallo, escribir por qué falló: sinonimia, paráfrasis, "
            "contexto implícito, o dispersión de la respuesta entre varios documentos.",
            "Diseñar el esquema de aislamiento por sesión, usuario y espacio de trabajo para "
            "ese caso.",
        ]),
        "La tabla de fallos de la fase 3 es el material con el que se abre el módulo 13.",
    ],
    "evaluacion": [
        "Explica por qué la recuperación léxica es insuficiente para contexto, y por qué un índice no lo arregla.",
        "Reconoce los casos donde la base relacional sigue siendo la respuesta correcta.",
        "Describe qué problema resuelve una base de grafos y cuál es su límite.",
        "Sostiene que los tipos de base de datos conviven en lugar de sustituirse.",
        "Diseña el aislamiento de datos por sesión, usuario y espacio de trabajo.",
    ],
}


M12 = {
    "num": 12,
    "title": "Embeddings",
    "tagline": "La base de todo el RAG. Si esto queda claro, el módulo siguiente se explica solo.",
    "objetivo": "Explicar qué es un embedding, cómo se genera y por qué convertir texto en "
                "números permite operaciones que sobre texto serían imposibles.",
    "duracion": "2.5 horas",
    "dependencias": "Módulos 4 y 11.",
    "contenidos": [
        "¿Qué es un embedding? Una posición en un espacio de significado.",
        "Dimensiones y matrices: la intuición desde el plano cartesiano.",
        "Por qué los temas relacionados quedan en posiciones cercanas.",
        "Cómo se genera un embedding: el texto pasa por un modelo.",
        "Modelos y proveedores de embeddings. Por qué no son intercambiables.",
        "Puente con el módulo 4: embeddings internos frente a embeddings de recuperación.",
        "Dónde se almacenan: bases de datos vectoriales.",
        "Operaciones sobre vectores: magnitud, distancia y ángulo.",
        "Por qué un embedding no se puede editar.",
    ],
    "enfoque": [
        ("box", "nota", "Este módulo merece tiempo", [
            "El temario base identifica los embeddings como «la base de todo el RAG» "
            "y pide darles bastante énfasis. Es un juicio correcto y esta versión lo "
            "mantiene con una duración generosa.",
            "La razón es económica en términos de esfuerzo docente: cada minuto invertido "
            "aquí ahorra tres en el módulo 13. Un RAG explicado sobre embeddings mal "
            "entendidos se convierte en una lista de pasos que nadie puede depurar.",
        ]),

        ("sub", "Construir la intuición desde dos dimensiones"),

        "La estrategia que mejor funciona es empezar en un plano cartesiano, donde todo se "
        "puede dibujar, y solo después subir de dimensión.",

        "Se propone en el pizarrón un espacio de dos ejes inventados —por ejemplo, cuánto "
        "tiene que ver con animales y cuánto con tecnología— y se colocan palabras: perro "
        "arriba a la izquierda, servidor abajo a la derecha, y algo como «ratón» "
        "en un punto intermedio ambiguo. La sala ve de inmediato que **la posición codifica "
        "significado** y que **la cercanía codifica parecido**.",

        "Un embedding es exactamente eso, con dos diferencias: los ejes no son dos sino "
        "cientos o miles, y nadie los eligió. Salieron del entrenamiento y no tienen nombre. "
        "Nadie puede decir qué significa la dimensión 412.",

        ("sub", "El salto a muchas dimensiones"),

        "Aquí conviene apoyarse en la analogía que el temario base ya proponía y que funciona "
        "bien: una posición en un espacio que no se puede visualizar pero que existe y opera "
        "con normalidad. La comparación con la cuarta dimensión espacial ayuda, siempre que "
        "se cierre rápido para no derivar en física.",

        "Lo que hay que evitar es que la falta de visualización se perciba como falta de "
        "entendimiento. La frase que resuelve esa ansiedad: **no hace falta imaginar mil "
        "dimensiones para operar con ellas.** Las operaciones que se van a usar —distancia, "
        "ángulo, magnitud— son las mismas en dos dimensiones que en mil. Se calculan igual y "
        "significan lo mismo.",

        "Y conviene aterrizar la representación, porque para un público de desarrolladores es "
        "tranquilizador: un embedding es un arreglo de números decimales.",

        ("code",
         "[0.0231, -0.4417, 0.1893, 0.0072, ..., -0.2264]\n"
         "   (por ejemplo, 1536 números en una sola lista)"),

        ("sub", "Cómo se genera"),

        "El texto entra a un modelo de embeddings —una red entrenada específicamente para "
        "esta tarea— y sale un vector. Tres precisiones que evitan malentendidos:",

        ("bullets", [
            "**No es una tabla de consulta.** No hay un diccionario de palabra a vector. Un "
            "párrafo completo produce un solo vector que representa el significado del "
            "conjunto.",
            "**Es determinista.** El mismo texto con el mismo modelo produce siempre el mismo "
            "vector. Esto lo diferencia de la generación, que es probabilística.",
            "**Es barato y rápido** en comparación con generar texto, varios órdenes de "
            "magnitud. Ese dato importa para el módulo 14.",
        ]),

        ("sub", "Los proveedores no son intercambiables"),

        "Este punto ya estaba bien planteado en el temario base y merece conservarse tal "
        "cual, porque tiene una consecuencia operativa fuerte. Como el espacio vectorial "
        "nace del entrenamiento, **cada modelo de embeddings define su propio espacio**. Los "
        "vectores de dos modelos distintos no son comparables aunque tengan el mismo número "
        "de dimensiones.",

        ("box", "alerta", "La consecuencia práctica", [
            "**Toda la base vectorial tiene que estar generada con el mismo modelo, y la "
            "consulta también.** Mezclar modelos no da un error: da resultados sin sentido, "
            "silenciosamente.",
            "Y cambiar de modelo de embeddings obliga a **reprocesar el corpus completo**. No "
            "es una migración de configuración, es volver a generar todos los vectores. Ese "
            "costo hay que presupuestarlo antes de elegir, y se cuantifica en el módulo 14.",
        ]),

        "Los ejes para elegir modelo son las dimensiones —más no es automáticamente mejor y "
        "sí es más caro de almacenar—, el idioma con el que se entrenó, la longitud máxima "
        "de entrada, y si es un servicio o se puede ejecutar en infraestructura propia.",

        ("sub", "El puente con el módulo 4"),

        ("box", "correccion", "Cerrar la confusión anunciada en el módulo 4", [
            "En el módulo 4 se advirtió que existen dos cosas llamadas embedding. Este es el "
            "momento de cerrar el círculo, porque ahora se pueden comparar de verdad.",
            "**Embeddings internos:** representaciones de cada token dentro del modelo "
            "generativo, durante el cómputo. Son un paso intermedio, no se exponen y no "
            "sirven para buscar.",
            "**Embeddings de recuperación:** un vector por fragmento de texto, producido por "
            "un modelo distinto y entrenado para que la cercanía refleje parecido semántico. "
            "Son los que se guardan y se comparan.",
            "La idea de fondo —representar significado como posición en un espacio— es la "
            "misma. El propósito es distinto, y por eso los modelos son distintos.",
        ]),

        ("sub", "Operaciones sobre vectores"),

        ("box", "correccion", "Reformulación respecto al borrador base", [
            "El temario base incluía el subtema «distancia euclidiana para embedding», "
            "con la indicación de no detallarlo aquí y de usarlo para mostrar que al ser "
            "numéricos se pueden hacer operaciones matemáticas.",
            "La intención se conserva íntegra, pero el subtema se reformula como "
            "**«operaciones sobre vectores: magnitud, distancia y ángulo»**. El "
            "motivo es que presentar solo la distancia euclidiana aquí prepara mal el módulo "
            "13, donde el error central del borrador consistía precisamente en confundir la "
            "similitud coseno con una distancia. Nombrando las tres operaciones desde el "
            "principio, esa confusión no llega a formarse.",
        ]),

        "La idea que hay que dejar es la que el temario base ya perseguía, y es una idea "
        "potente: **al dejar de ser texto y pasar a ser números, el significado se vuelve "
        "operable.** Sobre texto no se puede calcular un parecido; sobre vectores sí. Y las "
        "operaciones disponibles son tres, cada una respondiendo una pregunta distinta:",

        ("table",
         ["Operación", "Qué pregunta responde", "Nota"],
         [
             ["Magnitud", "¿Qué tan largo es este vector?",
              "Depende de factores como la longitud del texto. Casi nunca es lo que interesa."],
             ["Distancia euclidiana", "¿Qué tan separados están estos dos puntos?",
              "Es la distancia en línea recta. Es sensible a la magnitud."],
             ["Ángulo", "¿Apuntan en la misma dirección?",
              "Ignora la magnitud por completo. Es la base de la similitud coseno del módulo 13."],
         ],
         [3.6, 5.4, 7.5]),

        "No hace falta desarrollarlas aquí. Basta con que los tres nombres estén sobre la "
        "mesa y que quede claro que **son preguntas distintas y pueden dar respuestas "
        "distintas sobre los mismos dos vectores.** Ese es exactamente el punto de partida "
        "del módulo siguiente.",

        ("sub", "Por qué un embedding no se puede editar"),

        "Conviene cerrar con esta consecuencia, que el temario base ya señalaba y que tiene "
        "impacto directo en la arquitectura y en la factura. Un embedding se produce pasando "
        "el texto por un modelo. Si el texto cambia, aunque sea una palabra, hay que volver a "
        "pasarlo y sustituir el vector completo. **No se pueden ajustar los números a mano.**",

        "De ahí se sigue que todo sistema con contenido que cambia necesita un proceso de "
        "reindexación, y que ese proceso es un costo recurrente y una fuente de riesgo. Es la "
        "conexión directa con el módulo 13 y con la advertencia de bucles del módulo 18.",
    ],
    "ejercicio": [
        "Trabajo directo con vectores, sin base de datos todavía:",
        ("numbers", [
            "Generar embeddings de quince frases: cinco de un tema, cinco de otro y cinco "
            "ambiguas.",
            "Calcular la matriz de similitud entre todas y verificar que los grupos aparecen.",
            "Reducir a dos dimensiones y graficarlas. La imagen del agrupamiento es el "
            "objetivo del ejercicio.",
            "Tomar dos frases que signifiquen lo mismo con palabras distintas y dos que "
            "compartan muchas palabras pero signifiquen cosas distintas. Comprobar cuál par "
            "queda más cerca y explicar por qué.",
            "Repetir la fase 1 con un modelo de embeddings de otro proveedor e intentar "
            "comparar vectores entre ambos. Documentar por qué el resultado no tiene sentido.",
        ]),
        "La fase 5 es la que fija el aprendizaje más importante del módulo.",
    ],
    "evaluacion": [
        "Explica qué es un embedding como posición en un espacio de significado, sin recurrir a «es un número».",
        "Justifica por qué no hace falta visualizar mil dimensiones para operar con ellas.",
        "Sabe que los espacios de dos proveedores no son comparables, y qué implica cambiar de modelo.",
        "Distingue embeddings internos de embeddings de recuperación.",
        "Nombra las tres operaciones sobre vectores y sabe que responden preguntas distintas.",
        "Explica por qué un embedding no se edita y qué obliga eso a construir.",
    ],
}


M13 = {
    "num": 13,
    "title": "RAG: recuperación aumentada de contexto",
    "tagline": "El módulo más detallado del programa, y donde se corrige el error técnico más importante del temario base.",
    "objetivo": "Diseñar un sistema de recuperación por significado, explicando con "
                "precisión qué mide cada métrica de similitud y eligiendo la adecuada con "
                "criterio.",
    "duracion": "4 horas",
    "dependencias": "Módulos 11 y 12. Especialmente el 12.",
    "contenidos": [
        "¿Qué es un RAG y qué problema resuelve?",
        "El flujo completo: indexación y recuperación.",
        "Chunking: tamaño, cortes y solapamiento.",
        "El modelo no recibe vectores, recibe el texto recuperado.",
        "«¿Entonces para qué sirven los embeddings?» La pregunta central del módulo.",
        "Recuperación léxica frente a semántica.",
        ("Similitud coseno, en detalle", [
            "Qué mide realmente: el ángulo entre dos vectores.",
            "Por qué no es una distancia y por qué ignora la magnitud.",
            "El rango de valores y cómo interpretarlo.",
            "Coseno, producto punto y distancia euclidiana comparados.",
            "Cómo elegir la métrica, y qué permite cada base vectorial.",
        ]),
        "Búsqueda híbrida: combinar lo semántico y lo léxico.",
        "Indexación aproximada: por qué la búsqueda no es exhaustiva.",
        "Reordenamiento: recuperar mucho y quedarse con poco.",
        "Reindexación y sus riesgos.",
        "Cuándo NO usar RAG.",
    ],
    "enfoque": [
        ("sub", "Abrir con el flujo completo antes de entrar en detalles"),

        "Conviene dibujar las dos fases en el pizarrón antes de explicar nada, porque el "
        "error más común al aprender RAG es confundir lo que pasa una vez con lo que pasa en "
        "cada consulta.",

        ("code",
         "INDEXACIÓN  (una vez, y cada vez que cambia el contenido)\n"
         "  documento → trocear → embedding por trozo → guardar vector + texto\n"
         "\n"
         "RECUPERACIÓN  (en cada consulta)\n"
         "  pregunta → embedding de la pregunta → buscar los vectores más\n"
         "  parecidos → recuperar SU TEXTO → pegarlo en el prompt → generar"),

        "Con ese dibujo delante, la mitad de las preguntas del módulo se responden solas.",

        ("sub", "Chunking: la decisión que más afecta a la calidad"),

        "Un documento entero produce un solo vector que representa un promedio difuso de "
        "todo lo que dice, y eso recupera mal. Por eso se trocea. Pero trocear tiene costos "
        "en ambas direcciones, y conviene presentarlo como el compromiso que es.",

        ("table",
         ["Trozos pequeños", "Trozos grandes"],
         [
             ["Recuperación más precisa: el vector representa una idea concreta.",
              "Más contexto alrededor: la respuesta se entiende sin buscar más."],
             ["Se pierde el contexto circundante y pueden quedar incomprensibles.",
              "El vector se vuelve un promedio difuso y recupera peor."],
             ["Hacen falta más trozos para responder, y hay más ruido.",
              "Cada trozo recuperado mete más tokens al prompt. Cuesta más."],
         ],
         [8.2, 8.3]),

        "Tres recomendaciones prácticas que valen más que cualquier número mágico:",

        ("bullets", [
            "**Cortar por estructura, no por longitud.** Un corte en un límite de sección, "
            "de párrafo o de encabezado produce trozos coherentes. Cortar cada N caracteres "
            "parte frases a la mitad.",
            "**Usar solapamiento.** Repetir un fragmento del final del trozo anterior al "
            "principio del siguiente evita que una idea que cae justo en el corte se pierda. "
            "Cuesta almacenamiento y es casi siempre rentable.",
            "**Enriquecer el trozo con su contexto.** Anteponer el título del documento y la "
            "ruta de secciones al texto del trozo mejora mucho la recuperación, porque el "
            "vector incorpora de qué va el documento y no solo el párrafo suelto.",
        ]),

        ("sub", "La pregunta central del módulo"),

        "El temario base identifica aquí un momento pedagógico excelente y hay que "
        "conservarlo tal cual, porque es la pregunta que ordena todo el resto: si el modelo "
        "no entiende los embeddings, y hay que traducirlos de vuelta a texto para "
        "enviárselos, **¿para qué sirven los embeddings?**",

        ("box", "correccion", "La respuesta, que conviene decir despacio", [
            "Los embeddings **no mejoran la comunicación con el modelo.** El modelo recibe "
            "exactamente lo mismo que recibiría si se le pegara el texto a mano: texto.",
            "Lo que mejoran es **cómo se decide qué texto pegar.** Toda la ganancia está en "
            "la fase de búsqueda, no en la de generación.",
            "El temario base señala que su autor creyó al principio que el modelo entendía "
            "embeddings, y que esa creencia es un error frecuente. Vale la pena contarlo así "
            "en clase: los errores de quien enseña se recuerdan mejor que las definiciones.",
        ]),

        ("sub", "Léxico frente a semántico"),

        "Con la tabla de fallos del ejercicio del módulo 11 sobre la mesa, esta comparación "
        "es inmediata:",

        ("table",
         ["", "Recuperación léxica", "Recuperación semántica"],
         [
             ["Compara", "Caracteres y palabras", "Significado, mediante vectores"],
             ["Encuentra sinónimos", "No", "Sí"],
             ["Encuentra un identificador exacto", "Sí, perfectamente", "Mal. Un código no tiene significado semántico"],
             ["Explicable", "Sí: se ve qué palabra coincidió", "No directamente: solo hay un número de similitud"],
             ["Costo de indexar", "Bajo", "Hay que generar un embedding por trozo"],
             ["Términos raros y jerga propia", "Bien, si coinciden exactamente", "Puede fallar si el modelo no los conoce"],
         ],
         [3.4, 5.2, 7.9]),

        "La conclusión que se deduce de la tabla, y que anticipa la búsqueda híbrida: "
        "**ninguna de las dos gana en todo.** Los casos donde la léxica gana son reales y "
        "frecuentes: códigos de producto, nombres propios, siglas internas, números de "
        "factura.",

        ("h3", "13.1 · Similitud coseno, en detalle"),

        ("box", "correccion", "Corrección crítica respecto al borrador base", [
            "Esta es la corrección más importante de toda la revisión, y afecta justo a la "
            "sección que el temario base pedía explicar con más detalle.",
            "**El borrador dice:** «se utiliza una función trigonométrica que se llama "
            "coseno, porque para los que saben geometría y trigonometría el coseno te saca "
            "la hipotenusa y el cateto adyacente».",
            "**No es correcto.** El coseno de un ángulo es la razón entre el cateto "
            "adyacente y la hipotenusa en un triángulo rectángulo, pero no «saca» "
            "ninguno de los dos, y sobre todo: **no es eso lo que hace la similitud coseno "
            "entre embeddings.**",
            "**El borrador también dice:** «la función de coseno nos puede devolver la "
            "distancia euclidiana que hay entre los embeddings».",
            "**Tampoco es correcto.** La similitud coseno **no devuelve una distancia**. "
            "Devuelve el coseno del ángulo entre dos vectores, que es una medida de "
            "orientación. Son dos cosas distintas y pueden discrepar por completo, como se "
            "demuestra más abajo.",
        ]),

        ("sub", "Qué mide realmente"),

        "La definición correcta, y basta con esta:",

        ("code",
         "                     A · B\n"
         "  similitud(A, B) = ───────────\n"
         "                    ‖A‖ · ‖B‖\n"
         "\n"
         "  A · B   = suma de los productos componente a componente\n"
         "  ‖A‖     = longitud (magnitud) del vector A\n"
         "\n"
         "  El resultado es cos(θ), donde θ es el ángulo entre A y B."),

        "En palabras, que es la versión que hay que asegurar que todo el mundo se lleve: "
        "**mide si dos vectores apuntan en la misma dirección, sin importar cuán largos "
        "sean.**",

        ("sub", "La analogía geométrica correcta"),

        "El temario base proponía dibujar dos puntos en un plano y trazar un triángulo "
        "rectángulo cuya hipotenusa fuera la distancia entre ellos. Esa figura describe la "
        "**distancia euclidiana**, no la similitud coseno, y usarla aquí es lo que produce "
        "el error.",

        ("box", "nota", "La figura que sí funciona", [
            "Dibujar el origen. Desde el origen, dos **flechas** hasta los dos puntos. Lo "
            "que mide la similitud coseno es **la abertura entre esas dos flechas**.",
            "Cerradas del todo, apuntando al mismo lado: similitud 1. Perpendiculares: "
            "similitud 0. Opuestas: similitud −1.",
            "El detalle que hace clic: **la longitud de las flechas no interviene**. Se "
            "puede alargar una de ellas todo lo que se quiera y la abertura no cambia.",
        ]),

        ("sub", "La demostración numérica que cierra el tema"),

        "Conviene hacerla en el pizarrón con números pequeños, porque un ejemplo concreto "
        "convence más que cualquier explicación:",

        ("code",
         "  A = (3, 4)        B = (6, 8)\n"
         "\n"
         "  A · B  = 3·6 + 4·8 = 18 + 32 = 50\n"
         "  ‖A‖    = √(9 + 16)   = 5\n"
         "  ‖B‖    = √(36 + 64)  = 10\n"
         "\n"
         "  similitud coseno = 50 / (5 · 10) = 1.0     ← idénticos en dirección\n"
         "  distancia euclidiana = √(3² + 4²) = 5      ← nada cerca\n"),

        "Los dos vectores tienen **la máxima similitud posible y a la vez están separados**. "
        "Es la demostración de que coseno y distancia no son la misma cosa. Y la "
        "interpretación es la que importa: B apunta exactamente en la misma dirección que A, "
        "solo que más lejos. Si la dirección codifica el tema y la magnitud depende de cosas "
        "como la longitud del texto, entonces **ignorar la magnitud es exactamente lo que se "
        "quiere**. Por eso se usa coseno y no distancia en recuperación de texto.",

        ("sub", "El rango de valores, y cómo interpretarlo"),

        "En teoría, el coseno va de −1 a 1: uno si apuntan igual, cero si son "
        "perpendiculares, menos uno si son opuestos.",

        "En la práctica con modelos de embeddings modernos, los valores casi nunca son "
        "negativos y tienden a concentrarse en una franja alta. Los embeddings de un modelo "
        "ocupan una región relativamente estrecha del espacio, así que dos textos sin "
        "relación aparente rara vez dan cero: pueden dar 0.6 o 0.7 y aun así no tener nada "
        "que ver.",

        ("box", "alerta", "La consecuencia práctica del rango real", [
            "**No existe un umbral universal.** Un 0.8 puede ser buena señal con un modelo y "
            "ruido con otro. Fijar «recuperamos todo lo que supere 0.75» copiado de "
            "un tutorial es una de las causas más comunes de un RAG que devuelve basura con "
            "aparente confianza.",
            "El umbral se **calibra** con casos propios: se toman veinte consultas reales, "
            "se miran los puntajes de lo que sí era relevante y de lo que no, y se elige el "
            "corte donde se separan. Y se recalibra al cambiar de modelo de embeddings.",
            "Alternativa más robusta que un umbral fijo: recuperar siempre los K mejores y "
            "delegar el filtrado a un paso de reordenamiento.",
        ]),

        ("sub", "Coseno, producto punto y distancia euclidiana"),

        ("box", "correccion", "Segunda corrección del borrador", [
            "El temario base da a entender que el coseno es el método de la recuperación "
            "semántica. La retro lo señala con razón: **hay tres métricas de uso común y la "
            "mayoría de las bases vectoriales permiten elegir.** Además, el proveedor del "
            "modelo de embeddings suele recomendar una en su documentación, y conviene "
            "seguirla.",
        ]),

        ("table",
         ["Métrica", "Qué mide", "Sensible a la magnitud", "Cuándo conviene"],
         [
             ["**Similitud coseno**\n`cosine`", "El ángulo: la orientación.", "No",
              "Recuperación de texto en general. Es el valor por defecto razonable."],
             ["**Producto punto**\n`dot product` · `inner product` · `ip`",
              "Orientación y magnitud a la vez.", "Sí",
              "Cuando la magnitud codifica algo útil, como relevancia o popularidad "
              "aprendidas. Es la más barata de calcular."],
             ["**Distancia euclidiana**\n`euclidean` · `L2`", "La separación en línea recta.", "Sí",
              "Cuando la posición absoluta importa. Frecuente fuera del texto: imágenes, "
              "señales, agrupamiento."],
         ],
         [3.9, 3.8, 2.6, 6.2],
         "La segunda línea de cada fila es el nombre con el que aparece la métrica al "
         "configurar el índice en la mayoría de las bases vectoriales."),

        ("sub", "El matiz de la normalización, que simplifica todo"),

        "Hay un hecho que conviene enseñar porque elimina la mayor parte de la ansiedad "
        "sobre qué métrica elegir: **si los vectores están normalizados a longitud 1, las "
        "tres métricas ordenan igual.**",

        ("code",
         "  Con ‖A‖ = ‖B‖ = 1:\n"
         "\n"
         "     producto punto      = cos(θ)              ← son la misma operación\n"
         "     distancia euclidiana = √(2 − 2·cos(θ))    ← decrece cuando cos(θ) crece\n"),

        "Es decir: con vectores normalizados, el producto punto **es** la similitud coseno, y "
        "la distancia euclidiana produce **exactamente el mismo orden** de resultados. La "
        "elección deja de afectar a qué se recupera y pasa a ser una cuestión de eficiencia.",

        "Muchos modelos de embeddings ya devuelven vectores normalizados. La recomendación "
        "práctica: comprobarlo —basta con calcular la magnitud de un vector y ver si da "
        "uno—, y si lo están, elegir la métrica por rendimiento sin preocuparse por la "
        "calidad.",

        ("sub", "Qué permite cada base vectorial"),

        "Conviene mencionar que esto es configurable y no una propiedad fija del sistema. Las "
        "bases vectoriales de uso habitual —la extensión vectorial de PostgreSQL, así como "
        "Pinecone, Qdrant, Weaviate, Chroma, Milvus y las capacidades vectoriales de varios "
        "motores de búsqueda— permiten elegir la métrica al crear el índice.",

        ("box", "alerta", "Un detalle que provoca errores difíciles de encontrar", [
            "Algunos motores devuelven **similitud** —más alto es mejor— y otros devuelven "
            "**distancia** —más bajo es mejor—. Y algunos usan «distancia coseno», "
            "definida como uno menos la similitud coseno.",
            "Confundirlos hace que el sistema ordene los resultados **al revés** y recupere "
            "sistemáticamente lo menos parecido, sin lanzar ningún error. Hay que leer la "
            "documentación del motor concreto y verificarlo con un caso donde se sepa la "
            "respuesta correcta.",
        ]),

        ("h3", "13.2 · Del prototipo al sistema"),

        ("sub", "Búsqueda híbrida"),

        "Se deduce de la tabla anterior: si cada método gana en casos distintos, conviene "
        "ejecutar los dos y combinar los resultados. En la práctica se lanzan ambas "
        "búsquedas en paralelo y se fusionan las listas, ya sea con una fórmula que combina "
        "posiciones o con pesos ajustados al caso.",

        "El argumento a favor es empírico y fuerte: **la búsqueda híbrida casi siempre supera "
        "a cualquiera de las dos por separado**, sobre todo en dominios con jerga propia, "
        "códigos internos y nombres de producto, que es la situación normal de una empresa.",

        ("sub", "Indexación aproximada"),

        "Comparar la consulta contra todos los vectores da el resultado exacto y no escala. "
        "Los índices aproximados —de los cuales el basado en grafos jerárquicos es el más "
        "extendido— cambian una fracción pequeña de exactitud por una mejora enorme de "
        "velocidad.",

        "Lo importante no es el algoritmo sino aceptar la consecuencia: **la búsqueda "
        "vectorial en producción es aproximada.** Puede no devolver el mejor resultado "
        "absoluto. Hay parámetros que permiten mover el compromiso entre velocidad y "
        "exhaustividad, y conviene saber que existen porque explican comportamientos "
        "aparentemente erráticos.",

        ("sub", "Reordenamiento"),

        "El patrón que más mejora la calidad de un RAG con el menor esfuerzo: recuperar de "
        "forma amplia —cincuenta candidatos— y pasarlos por un modelo de reordenamiento que "
        "evalúa cada par de consulta y documento con mucha más precisión, para quedarse con "
        "los cinco mejores.",

        "Es más caro por consulta que la búsqueda vectorial y **mucho más barato que meter "
        "cincuenta trozos en el prompt**. Y tiene una propiedad poco común que conviene "
        "señalar: recuperar menos y mejor **baja el costo y sube la calidad al mismo "
        "tiempo**. Casi ninguna optimización hace las dos cosas.",

        ("sub", "Reindexación y sus riesgos"),

        "Del módulo 12 ya se sabe que un embedding no se edita. De ahí se sigue todo lo que "
        "hay que decir aquí:",

        ("bullets", [
            "**Cualquier cambio en el contenido obliga a regenerar el vector** de los trozos "
            "afectados.",
            "**Cambiar de modelo de embeddings obliga a reprocesar todo el corpus.**",
            "**Reindexar por comparación de contenido, no por defecto.** Guardar una huella "
            "del texto de cada trozo y regenerar solo los que cambiaron. La diferencia de "
            "costo entre reindexar todo y reindexar lo modificado es de órdenes de magnitud.",
            "**Poner límites duros.** Un proceso que reindexa, y al reindexar dispara un "
            "evento que vuelve a reindexar, es un bucle que genera factura sin parar. El "
            "temario base ya lo señalaba como riesgo de seguridad y tiene razón: se retoma "
            "en el módulo 18.",
        ]),

        ("sub", "Cuándo NO usar RAG"),

        "Cerrar con esto evita que la sala salga queriendo aplicarlo a todo:",

        ("bullets", [
            "**Cuando se busca un registro concreto por identificador.** Es una consulta a "
            "la base de datos. Usar RAG aquí es más caro, más lento y menos exacto.",
            "**Cuando toda la información cabe en el contexto.** Si son diez páginas y "
            "siempre son las mismas, pegarlas es más simple, más barato con caché de prompts "
            "y más confiable.",
            "**Cuando la respuesta requiere agregar o contar.** «¿Cuántos clientes "
            "tenemos en Jalisco?» es SQL. Recuperar trozos no responde preguntas "
            "cuantitativas.",
            "**Cuando el dato es transaccional y tiene que estar al día al segundo.** Eso es "
            "una herramienta que consulta el sistema real, módulo 9.",
        ]),
    ],
    "ejercicio": [
        "Construir un RAG completo sobre documentación real del equipo, y evaluarlo:",
        ("numbers", [
            "**Indexar** con dos estrategias de troceado distintas: cortes fijos sin "
            "solapamiento, y cortes por estructura con solapamiento.",
            "**Consultar** con veinte preguntas reales y registrar, para cada una, los "
            "trozos recuperados **con sus puntajes**.",
            "**Comparar las tres métricas** sobre las mismas veinte consultas. Verificar "
            "empíricamente si los vectores del modelo elegido están normalizados y, si lo "
            "están, comprobar que el orden de resultados coincide.",
            "**Calibrar el umbral** con los puntajes registrados en la fase 2, en lugar de "
            "copiar un número.",
            "**Añadir reordenamiento** y medir el cambio en calidad y en tokens enviados al "
            "modelo.",
        ]),
        "La entrega es una tabla comparativa de las cinco configuraciones y una recomendación "
        "escrita y justificada. Se exige explícitamente reportar **un caso en el que el RAG "
        "recuperó el trozo correcto y el modelo aun así respondió mal**, y otro en el que no "
        "lo recuperó: distinguir esos dos fallos es la habilidad central del módulo.",
    ],
    "evaluacion": [
        "Dibuja el flujo completo de indexación y recuperación, y sabe qué ocurre en cada fase.",
        "Responde con precisión para qué sirven los embeddings, sabiendo que el modelo recibe texto.",
        "**Explica que la similitud coseno mide el ángulo entre dos vectores, no una distancia, "
        "y demuestra con un ejemplo que dos vectores pueden tener similitud 1 y estar lejos.**",
        "Compara coseno, producto punto y distancia euclidiana, y sabe que con vectores "
        "normalizados ordenan igual.",
        "Calibra un umbral con datos propios en lugar de copiarlo, y sabe que depende del modelo.",
        "Justifica el troceado y el solapamiento en términos de precisión frente a contexto.",
        "Distingue un fallo de recuperación de un fallo de generación.",
        "Identifica al menos tres situaciones en las que RAG es la herramienta equivocada.",
    ],
}


PARTS = [
    {
        "kicker": "PARTE III",
        "title": "Construir un sistema",
        "intro": "La parte más extensa del programa. Aquí se construye todo lo que el "
                 "modelo no trae: memoria, capacidad de actuar, canales de comunicación y "
                 "acceso a información que no cabe en el contexto. Termina en el módulo más "
                 "detallado de todos, la recuperación por significado. Dieciséis horas.",
        "modules": [M8, M9, M10, M11, M12, M13],
    },
]
