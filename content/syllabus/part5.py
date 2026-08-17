# -*- coding: utf-8 -*-
"""Parte V: más allá (módulos 19 y 20)."""

M19 = {
    "num": 19,
    "title": "Conceptos avanzados",
    "tagline": "Las técnicas que aparecen cuando el sistema ya funciona y hay que empujarlo un poco más lejos.",
    "objetivo": "Reconocer un conjunto de técnicas avanzadas de gestión de contexto, diseño "
                "conversacional y rendimiento, y saber cuándo cada una está justificada.",
    "duracion": "2 horas",
    "dependencias": "Toda la parte IV.",
    "contenidos": [
        ("Control avanzado del contexto", [
            "Compresión de contexto.",
            "Eliminación de redundancia.",
            "Agrupamiento para selección de contexto.",
        ]),
        "Control del estilo: las cuatro formas de fijar la voz de un sistema.",
        ("Agentes conversacionales como pipelines", [
            "Nodos y artefactos.",
            "Por qué una conversación con objetivo tiene estructura.",
            "Qué ocurre en cada nodo.",
        ]),
        "Streaming y respuestas por fases: el caso interno de análisis masivo.",
        "Latencia: de qué depende y qué se puede hacer con ella.",
    ],
    "enfoque": [
        ("box", "nota", "Módulo aligerado respecto al borrador base", [
            "Este módulo era el cajón de sastre del temario original. Dos de sus temas se "
            "ascendieron a módulos propios —la observabilidad al 16 y el fine tuning al 20— "
            "porque su peso lo justificaba.",
            "Lo que queda son técnicas genuinamente avanzadas: útiles, pero que solo tienen "
            "sentido sobre un sistema que ya funciona. Conviene enmarcarlo así en clase, "
            "para que nadie salga intentando aplicar compresión de contexto a un prototipo.",
        ]),

        ("sub", "Control avanzado del contexto"),

        "Las tres técnicas responden a la misma tensión que atraviesa el programa desde el "
        "módulo 3: hace falta contexto, y el contexto cuesta dinero, latencia y precisión.",

        ("table",
         ["Técnica", "Qué hace", "Cuándo se justifica", "Qué cuesta"],
         [
             ["Compresión",
              "Reescribe el contexto en menos tokens conservando lo esencial. Puede hacerlo "
              "otro modelo más barato.",
              "Historiales largos, documentos extensos que se reutilizan mucho.",
              "Una llamada extra, y pérdida de detalle que no siempre se nota hasta que "
              "importa."],
             ["Eliminación de redundancia",
              "Detecta y descarta fragmentos que dicen lo mismo antes de enviarlos.",
              "Corpus con mucha duplicación: documentación versionada, correos en hilo, "
              "actas repetitivas.",
              "Poco. Es de las optimizaciones más limpias que existen."],
             ["Agrupamiento",
              "Agrupa los fragmentos recuperados por tema y toma representantes de cada "
              "grupo en lugar de los K más parecidos.",
              "Cuando la recuperación devuelve diez variantes de la misma idea y deja fuera "
              "una perspectiva distinta que sí hacía falta.",
              "Complejidad. Hay que ajustar el número de grupos."],
         ],
         [2.8, 4.6, 4.6, 4.5]),

        "El agrupamiento merece un comentario porque resuelve un fallo real del RAG que no es "
        "obvio: los K más parecidos pueden ser **todos el mismo párrafo repetido en cinco "
        "documentos**. Recuperar diversidad en lugar de solo similitud mejora las respuestas "
        "a preguntas amplias.",

        ("sub", "Control del estilo"),

        ("box", "correccion", "Precisión terminológica respecto al borrador base", [
            "El temario base menciona el **style encoder** como alternativa al system prompt "
            "para que un agente se comporte de cierta forma. Conviene precisar el término "
            "antes de enseñarlo, porque puede llevar a buscar algo que no existe con ese "
            "nombre.",
            "**Style encoder** es un término establecido en síntesis de voz, generación de "
            "imágenes y transferencia de estilo: un componente que codifica el estilo de una "
            "referencia en un vector que condiciona la generación. En esos dominios es real "
            "y es exactamente eso.",
            "**En modelos de lenguaje por API no existe un componente con ese nombre.** Lo "
            "que sí existe son cuatro formas de controlar el estilo, y conviene enseñarlas "
            "como el abanico real de opciones. La intención del temario base —que hay "
            "alternativas al system prompt para fijar el comportamiento— es correcta; solo "
            "hay que darle los nombres que se van a encontrar en la documentación.",
        ]),

        ("table",
         ["Opción", "Cómo funciona", "Cuándo conviene"],
         [
             ["Descripción en el system prompt",
              "Se describe la voz con palabras.",
              "Punto de partida. Barato y reversible, pero las descripciones de estilo son "
              "notoriamente imprecisas."],
             ["Ejemplos de estilo (few-shot)",
              "Se muestran dos o tres fragmentos escritos con la voz deseada.",
              "**Casi siempre mejor que describirla.** El estilo se enseña mejor con "
              "muestras que con adjetivos."],
             ["Guía de estilo recuperada",
              "El documento de voz de marca se recupera cuando la tarea lo requiere.",
              "Organizaciones con una guía real y extensa que no cabe en el prompt."],
             ["Fine tuning",
              "Se ajustan los pesos con ejemplos escritos en esa voz.",
              "Solo cuando lo anterior se agotó y el volumen lo justifica. Módulo 20."],
         ],
         [3.6, 5.6, 7.3]),

        "La recomendación que hay que dar: **para estilo, los ejemplos ganan a las "
        "descripciones casi siempre.** Es la aplicación directa de la regla del módulo 5 —los "
        "ejemplos comunican formato, las instrucciones comunican criterio— y el estilo es "
        "forma, no criterio.",

        ("sub", "Agentes conversacionales como pipelines"),

        "Esta es la parte más original del temario base y conviene conservarla íntegra "
        "porque describe bien un tipo de sistema que se construye mucho y se documenta poco.",

        "La observación de partida es acertada: **una conversación con un objetivo no es "
        "libre, tiene estructura.** Una entrevista de calificación, un proceso de alta, una "
        "atención de soporte: todas siguen una línea con un objetivo comunicativo. Modelarla "
        "como un chat abierto desperdicia esa estructura y produce sistemas impredecibles.",

        "Verla como un pipeline de nodos hace explícito lo que ya estaba implícito. En cada "
        "nodo ocurre una de estas cosas: se pregunta algo, se responde algo, se carga "
        "contexto, se ejecuta una acción o se delega en otro agente. Y cada nodo puede "
        "descomponerse en artefactos: lo que produce, lo que consume y lo que deja para el "
        "siguiente.",

        "Lo que hay que hacer explícito, y que el temario base ya intuía al mencionarlo junto "
        "a la observabilidad: **este modelo resuelve tres problemas a la vez.** Da "
        "predecibilidad, porque el conjunto de estados posibles es conocido. Da "
        "trazabilidad, porque cada nodo es un span natural del módulo 16. Y da control de "
        "costo, porque cada nodo carga solo su contexto, que es la carga bajo demanda del "
        "módulo 15.",

        "Conviene también decir la contrapartida: un pipeline rígido maneja mal lo "
        "inesperado. El diseño realista combina nodos deterministas para el camino principal "
        "con capacidad de salirse del guion cuando el usuario hace algo que no estaba "
        "previsto. Es la misma tensión entre flujo y agente del módulo 9, ahora aplicada a "
        "conversación.",

        ("sub", "Streaming y respuestas por fases"),

        "El streaming ya se vio en los módulos 7 y 10. Lo que aporta este módulo es el patrón "
        "de **respuesta por fases** para trabajos largos, y conviene usar el ejemplo interno "
        "que el temario base menciona: el análisis masivo de candidatos.",

        "Cuando hay que procesar cien elementos, hay tres estrategias con perfiles muy "
        "distintos, y conviene contrastarlas porque la elección suele hacerse por inercia:",

        ("bullets", [
            "**Una sola llamada con todo.** Simple, pero el contexto es enorme, la calidad "
            "se degrada, la latencia es alta y si falla se pierde todo.",
            "**Una llamada por elemento, en paralelo.** Mejor calidad porque cada análisis "
            "tiene contexto limpio, tolerante a fallos parciales, y se puede ir mostrando "
            "conforme llega. Es el patrón por defecto razonable.",
            "**Por lotes asíncronos.** Cuando nadie está esperando la respuesta. Del orden "
            "de la mitad de costo, según lo visto en el módulo 14.",
        ]),

        "El criterio: **si hay una persona esperando, paralelo y por fases; si no la hay, "
        "por lotes.** Y en el caso de un análisis masivo de candidatos, normalmente no la hay.",

        ("sub", "Latencia"),

        "El temario base la describe bien y solo hace falta ordenar los factores por si se "
        "pueden controlar o no, que es lo que convierte la explicación en algo accionable:",

        ("table",
         ["Factor", "¿Se controla?", "Qué se puede hacer"],
         [
             ["Número de peticiones encadenadas", "Sí",
              "Es el factor dominante y el más ignorado. Reducir viajes de ida y vuelta."],
             ["Tamaño del contexto", "Sí",
              "Todo el contexto se procesa antes de emitir el primer token."],
             ["Tokens de salida y de razonamiento", "Sí",
              "Se generan de uno en uno. Limitar la longitud y el esfuerzo de razonamiento."],
             ["Elección de modelo", "Sí", "Los modelos pequeños son notablemente más rápidos."],
             ["Carga del proveedor", "No", "Reintentos, alternativas y degradación elegante."],
             ["Ubicación geográfica", "Parcialmente",
              "Elegir la región del proveedor más cercana a los usuarios."],
         ],
         [4.4, 2.6, 9.5]),

        ("box", "correccion", "Matiz sobre la CDN", [
            "El temario base sugiere que la latencia por ubicación geográfica «se "
            "resuelve por CDN o infraestructura propia». Conviene precisarlo.",
            "Una CDN acelera contenido estático que se puede cachear y replicar. **La "
            "inferencia de un modelo no es contenido estático**: cada respuesta es distinta "
            "y se calcula en el momento, así que no se cachea en el borde de la red. Lo que "
            "sí reduce la latencia geográfica es **elegir la región del proveedor más "
            "cercana** a los usuarios, o desplegar el modelo en infraestructura propia en esa "
            "región, que es muy costoso.",
            "Donde una CDN o el cómputo en el borde sí ayudan es en todo lo que rodea a la "
            "llamada: la aplicación, los recursos estáticos y la lógica previa. Es una "
            "distinción útil porque evita esperar de la CDN algo que no puede dar.",
        ]),

        "El cierre honesto del módulo: en una arquitectura compleja la latencia es difícil de "
        "reducir porque es la suma de muchas partes, y la AI está empujando los límites de "
        "la capacidad de cómputo disponible. El factor que casi siempre domina, y sobre el "
        "que casi siempre se puede hacer algo, es **el número de peticiones encadenadas**.",
    ],
    "ejercicio": [
        "Elegir **una** de las tres líneas, según lo que el equipo necesite:",
        ("numbers", [
            "**Compresión.** Tomar un historial largo real, comprimirlo con un modelo barato "
            "y medir tokens ahorrados frente a pérdida de calidad en las respuestas "
            "posteriores.",
            "**Pipeline conversacional.** Modelar una conversación con objetivo real del "
            "producto como un grafo de nodos, especificando en cada uno qué se pregunta, qué "
            "contexto se carga y qué artefacto se produce. Implementar el camino principal.",
            "**Latencia.** Medir la latencia de un flujo existente descomponiéndola por "
            "etapa, identificar el factor dominante y aplicar dos optimizaciones. Reportar "
            "el antes y el después en percentiles 50 y 95.",
        ]),
    ],
    "evaluacion": [
        "Elige una técnica de control de contexto justificándola con el problema concreto que resuelve.",
        "Conoce las cuatro formas reales de controlar el estilo y sabe que los ejemplos suelen ganar.",
        "Modela una conversación con objetivo como un pipeline de nodos con artefactos.",
        "Elige entre llamada única, paralelo y lotes con el criterio de si alguien está esperando.",
        "Separa los factores de latencia controlables de los que no, y sabe qué puede y qué no puede hacer una CDN.",
    ],
}


M20 = {
    "num": 20,
    "title": "Fine tuning en detalle",
    "tagline": "El programa termina donde mucha gente quería empezar.",
    "objetivo": "Decidir con criterio si un proyecto de fine tuning está justificado, y "
                "dimensionar honestamente lo que cuesta mantenerlo.",
    "duracion": "2 horas",
    "dependencias": "Módulo 6, que abrió este arco, y los módulos 14 y 16.",
    "contenidos": [
        "Recapitulación de la escalera y de la pregunta «¿no sabe o no puede?».",
        "Qué sí arregla el fine tuning.",
        "Qué no arregla, y el efecto perverso de intentarlo.",
        "Fine tuning completo frente a LoRA y métodos de ajuste eficiente.",
        "Destilación: usar un modelo grande para entrenar uno pequeño.",
        "El dataset es el proyecto: cantidad, calidad, distribución y conjunto de prueba.",
        "Cómo saber si funcionó: la línea base obligatoria.",
        "El costo completo, incluido el que nadie presupuesta.",
        "Alternativas que suelen ganarle.",
        "Lista de verificación de cinco preguntas.",
    ],
    "enfoque": [
        ("sub", "Cerrar el arco abierto en el módulo 6"),

        "Conviene abrir recordando la escalera y la pregunta que la resuelve, porque han "
        "pasado catorce módulos: **¿el modelo no sabe, o no puede?** Y la prueba diagnóstica: "
        "pegar la información directamente en el prompt y ver si con eso acierta.",

        "Lo que este módulo añade es todo lo técnico y económico que el módulo 6 aplazó "
        "deliberadamente. Ahora la sala tiene el vocabulario para entenderlo: sabe qué es "
        "entrenamiento frente a inferencia del módulo 4, sabe leer un costo del módulo 14 y "
        "sabe qué significa medir del módulo 16.",

        ("sub", "Qué sí arregla"),

        ("bullets", [
            "**Formato y estructura muy específicos y consistentes**, cuando el esquema "
            "forzado no basta porque lo que se quiere es más sutil que la forma.",
            "**Tono y voz sostenidos** a lo largo de textos largos.",
            "**Una tarea estrecha y repetitiva**: clasificación, extracción, transformación. "
            "Un modelo pequeño ajustado puede igualar a uno grande **en su tarea**, mucho más "
            "barato y más rápido.",
            "**Reducir tokens de prompt.** Mover instrucciones largas y decenas de ejemplos a "
            "los pesos.",
            "**Enseñar un protocolo propio**: cómo usar las herramientas internas, cómo "
            "seguir un flujo particular de la empresa.",
            "**Dominios con vocabulario muy particular** donde el prompt ya no da más.",
        ]),

        ("box", "correccion", "El caso con el argumento económico más sólido", [
            "**Reducir tokens de prompt** es el caso que casi nadie plantea y el que mejor "
            "se sostiene con aritmética.",
            "Si el prompt de producción tiene cuatro mil tokens de instrucciones y veinte "
            "ejemplos, y se hacen un millón de llamadas al mes, mover eso a los pesos y "
            "quedarse con doscientos tokens es un ahorro enorme y además baja la latencia.",
            "Ese caso se paga solo con matemáticas simples, y es **muy distinto** de "
            "«quiero que sepa de mi empresa». Conviene contrastarlos explícitamente.",
            "Matiz honesto que hay que dar: el caché de prompts del módulo 14 se come buena "
            "parte de este argumento. Hay que hacer la cuenta con caché antes de decidir.",
        ]),

        ("sub", "Qué no arregla, y el efecto perverso"),

        "Aquí conviene ser insistente, sobre todo con el punto contraintuitivo:",

        ("bullets", [
            "**Agregar conocimiento fresco o cambiante.** Eso es RAG.",
            "**Corregir hechos puntuales.** No es un editor de hechos.",
            "**Reemplazar autorización, validación o seguridad.**",
            "**Arreglar un prompt mal escrito.**",
        ]),

        ("box", "alerta", "El efecto perverso, que conecta con el módulo 4", [
            "**Entrenar un modelo con hechos que no conocía bien puede aumentar sus "
            "alucinaciones.**",
            "La razón es la del mecanismo: no se le están enseñando los hechos, se le está "
            "enseñando el **patrón** de responder con seguridad a ese tipo de preguntas. "
            "Cuando le llegue una pregunta parecida sobre algo que no estaba en el conjunto "
            "de entrenamiento, va a responder con la misma seguridad y va a inventar.",
            "Es exactamente el resultado opuesto al que se buscaba. La regla que hay que "
            "dejar: **el conocimiento va en el contexto, el comportamiento va en los pesos.**",
        ]),

        ("sub", "LoRA frente a fine tuning completo"),

        "La explicación no necesita matemáticas. En lugar de mover los miles de millones de "
        "pesos del modelo, se congela todo y se entrena un conjunto pequeño de matrices "
        "adicionales que se suman al resultado.",

        ("table",
         ["", "Fine tuning completo", "LoRA y métodos eficientes"],
         [
             ["Qué se modifica", "Todos los pesos", "Un conjunto pequeño de matrices añadidas"],
             ["Tamaño del artefacto", "Un modelo entero, gigabytes", "Un adaptador, megabytes"],
             ["Cómputo necesario", "Alto", "Bajo. Cabe en hardware modesto con cuantización"],
             ["Riesgo de olvidar lo aprendido", "Real", "Mucho menor: el modelo base queda intacto"],
             ["Servir varias variantes", "Un despliegue por variante",
              "Varios adaptadores sobre el mismo modelo base, intercambiables"],
             ["Cuándo elegirlo", "Volumen grande de datos y cambio real de capacidad, o un "
                                 "dominio o idioma que el base cubre mal",
              "**Prácticamente siempre como primer intento**"],
         ],
         [3.6, 6.4, 6.5]),

        ("sub", "Destilación"),

        "El camino más práctico hoy: se usa un modelo grande y caro para generar y etiquetar "
        "los datos, se **filtra agresivamente por calidad** —este es el paso que decide el "
        "resultado, no la generación— y se entrena un modelo pequeño con eso. El resultado es "
        "un modelo barato y rápido que hace bien esa tarea concreta.",

        "Y la parte incómoda que hay que mencionar: **revisar los términos de servicio del "
        "proveedor.** Varios prohíben usar sus salidas para entrenar modelos competidores. Es "
        "un riesgo legal real, no un tecnicismo.",

        ("sub", "El dataset es el proyecto"),

        "El mensaje central de esta sección: **el entrenamiento es la parte fácil.**",

        ("bullets", [
            "**Cantidad.** Para LoRA en una tarea estrecha, del orden de cientos a unos pocos "
            "miles de ejemplos de calidad. Es un orden de magnitud a calibrar, no una cifra.",
            "**Calidad sobre cantidad.** Trescientos ejemplos curados superan a diez mil "
            "sucios, y no por poco.",
            "**Distribución.** Los ejemplos tienen que parecerse a lo que se va a ver en "
            "producción, incluidos los casos raros. Un conjunto solo de casos fáciles produce "
            "un modelo que falla justo donde importa.",
            "**Conjunto de prueba apartado desde el principio**, nunca visto durante el "
            "entrenamiento. Sin esto no hay proyecto.",
            "**De dónde salen los datos:** registros de producción, generación sintética con "
            "filtrado, y anotación humana.",
        ]),

        ("sub", "La línea base obligatoria"),

        ("box", "correccion", "El paso que más proyectos se saltan", [
            "Antes de comparar nada, hay que medir **el mismo modelo sin ajustar, pero bien "
            "prompteado**, sobre el conjunto de prueba apartado.",
            "Con una frecuencia incómoda, **la línea base gana**. Y descubrirlo antes de "
            "invertir tres semanas es exactamente el valor de este módulo.",
            "Además hacen falta pruebas de regresión: verificar que el ajuste no rompió lo "
            "que antes funcionaba.",
        ]),

        ("sub", "El costo completo"),

        ("table",
         ["Partida", "Peso real"],
         [
             ["Datos y curación", "El grueso del esfuerzo. Semanas de trabajo humano."],
             ["Medición", "Imprescindible. Sin esto no se sabe si mejoró."],
             ["Entrenamiento", "Relativamente barato. Es lo de menos."],
             ["Hospedaje",
              "Donde duele. Con infraestructura propia se paga la GPU por hora se use o no, "
              "y con tráfico irregular el costo por petición es terrible. En servicio "
              "administrado suele haber un precio por token más alto o una cuota fija."],
             ["Mantenimiento", "Versionado, reversión, monitoreo continuo."],
         ],
         [4.0, 12.5]),

        ("box", "alerta", "El costo que nadie presupuesta", [
            "**El modelo base va a cambiar.** En seis o doce meses saldrá uno mejor, más "
            "barato y más rápido, o el actual se deprecará.",
            "**El adaptador no se transfiere.** Hay que volver a entrenar, volver a evaluar y "
            "volver a desplegar.",
            "El fine tuning no es un proyecto con fecha de término: es un **compromiso de "
            "mantenimiento recurrente**, y así hay que presupuestarlo.",
            "Y una ironía que vale la pena señalar: hay bastantes equipos que ajustaron un "
            "modelo para igualar la calidad de uno grande, y seis meses después el modelo "
            "pequeño de nueva generación del mismo proveedor ya lo superaba de fábrica, con "
            "un prompt y sin mantener nada.",
        ]),

        ("sub", "Alternativas que suelen ganarle"),

        ("bullets", [
            "Un prompt bien diseñado con ejemplos, más caché de prompts.",
            "RAG con reordenamiento.",
            "Un modelo más nuevo y barato que el que se estaba usando.",
            "Enrutamiento: modelo pequeño para lo fácil, grande para lo difícil.",
        ]),

        ("sub", "Cerrar el programa"),

        "La lista de verificación con la que conviene terminar, para que la sala salga con un "
        "instrumento y no con una opinión:",

        ("numbers", [
            "¿Se probó un prompt bien diseñado con ejemplos, y se midió?",
            "¿El problema es de conocimiento? Si lo es, es RAG, no fine tuning.",
            "¿Hay al menos unos cientos de ejemplos de calidad y un conjunto de prueba "
            "apartado?",
            "¿Se puede medir objetivamente la mejora contra la línea base?",
            "¿El volumen justifica el hospedaje y el reentrenamiento cada vez que cambie el "
            "modelo base?",
        ]),

        "Si las cinco son afirmativas, adelante. Si alguna es negativa, el escalón anterior "
        "todavía tiene algo que dar.",

        ("box", "nota", "Frase de cierre del programa", [
            "«Terminamos donde mucha gente quería empezar. Y ahora la diferencia es que "
            "pueden justificar por qué empezar aquí habría sido un error, o por qué en su "
            "caso concreto sí tiene sentido. Ese criterio es todo el programa.»",
        ]),
    ],
    "ejercicio": [
        "Evaluación completa de un caso real, sin llegar necesariamente a entrenar nada:",
        ("numbers", [
            "Elegir una tarea del producto que sea candidata a fine tuning.",
            "Establecer la **línea base**: el mismo modelo bien prompteado, medido sobre "
            "treinta casos apartados.",
            "Estimar el costo completo del proyecto con la tabla de partidas, incluyendo el "
            "reentrenamiento anual.",
            "Estimar el ahorro esperado con los volúmenes reales, comparándolo también "
            "contra la opción de prompt más caché.",
            "Aplicar la lista de cinco preguntas y emitir una recomendación escrita.",
        ]),
        "**Se acepta y se valora una recomendación negativa.** Concluir con datos que el fine "
        "tuning no está justificado es el resultado más frecuente en la práctica y demuestra "
        "el mismo dominio que concluir lo contrario.",
    ],
    "evaluacion": [
        "Aplica la pregunta «¿no sabe o no puede?» y la prueba diagnóstica del prompt.",
        "Distingue lo que el fine tuning arregla de lo que no, y explica el efecto perverso "
        "de entrenar con conocimiento.",
        "Compara LoRA con fine tuning completo y justifica cuál probar primero.",
        "Establece una línea base antes de comparar, y sabe que a menudo gana.",
        "Presupuesta el costo completo incluyendo hospedaje y reentrenamiento futuro.",
        "Emite una recomendación justificada, incluso si es negativa.",
    ],
}


PARTS = [
    {
        "kicker": "PARTE V",
        "title": "Más allá",
        "intro": "Las dos últimas sesiones cubren lo que aparece cuando todo lo anterior ya "
                 "está en su sitio y aun así se queda corto. Cierran el arco que abrió el "
                 "módulo 6. Cuatro horas.",
        "modules": [M19, M20],
    },
]
