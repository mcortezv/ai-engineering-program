# -*- coding: utf-8 -*-
"""Parte II: cómo se le habla a un modelo (módulos 5 a 7)."""

M5 = {
    "num": 5,
    "title": "Prompt engineering: cómo habla un modelo",
    "tagline": "No es «cómo escribir prompts bonitos». Es la única interfaz que existe con el modelo, y todo lo que viene después es un prompt.",
    "objetivo": "Construir prompts cuya estructura se justifique en el mecanismo del módulo "
                "4, y diagnosticar por qué un prompt falla en lugar de reescribirlo a ciegas.",
    "duracion": "3 horas",
    "dependencias": "Módulo 4. Este módulo es incomprensible sin él.",
    "contenidos": [
        "El prompt como única interfaz. Los roles system, user y assistant.",
        "Instrucciones: especificidad, y por qué decir qué hacer funciona mejor que decir qué no hacer.",
        "Contexto: cuánto poner, dónde ponerlo y por qué la posición importa.",
        "Ejemplos y few-shot: cuándo un ejemplo vale más que tres párrafos de instrucciones.",
        "Delimitadores: XML, Markdown y bloques. Por qué funcionan.",
        ("Cadenas de pensamiento", [
            "Qué son y por qué mejoran los problemas de varios pasos.",
            "Cuándo NO pedirlas: modelos de razonamiento, tareas triviales, costo y latencia.",
        ]),
        "Salidas estructuradas: JSON, esquemas y el uso de herramientas como mecanismo de formato.",
        "Anti-patrones: el prompt kilométrico, las instrucciones contradictorias, los adjetivos vacíos.",
        "Cómo se depura un prompt de forma sistemática.",
    ],
    "enfoque": [
        ("box", "nota", "Por qué este módulo se adelantó", [
            "En el temario base no existía un módulo de prompt engineering: el tema aparecía "
            "disperso, sobre todo dentro de agentes al hablar del system prompt.",
            "Se adelanta hasta aquí porque **el prompt es la única interfaz con el modelo**, "
            "y todo lo que viene después lo es también: un system prompt es un prompt, la "
            "descripción de una herramienta es un prompt, la plantilla que arma la respuesta "
            "de un RAG es un prompt. Enseñarlo tarde obliga a explicarlo mal tres veces "
            "antes de explicarlo bien una.",
        ]),

        ("sub", "El encuadre: no es redacción, es diseño de entrada"),

        "Conviene abrir descartando la lectura popular del tema. Esto no va sobre encontrar "
        "las palabras mágicas ni sobre colecciones de trucos. Va sobre una pregunta técnica: "
        "**dado que el modelo predice el siguiente token ponderando el contexto por "
        "atención, ¿cómo se construye ese contexto para que la continuación más probable sea "
        "la que se necesita?**",

        "Planteado así, cada técnica del módulo se deduce del módulo 4 en lugar de "
        "memorizarse. Vale la pena hacer esa deducción explícita cada vez, porque es lo que "
        "distingue este módulo de cualquier lista de consejos que se encuentre en internet.",

        ("sub", "Los tres roles"),

        "Antes de las técnicas hay que fijar la estructura. Una petición no es una cadena de "
        "texto suelta: es una lista de mensajes con rol.",

        ("table",
         ["Rol", "Qué contiene", "Observación importante"],
         [
             ["system", "Quién es el modelo, qué reglas sigue, qué formato produce, qué "
                        "límites tiene. Es estable entre peticiones.",
              "Al ser estable y estar al principio, es lo que mejor aprovecha el caché de "
              "prompts del módulo 14. No es una zona privilegiada a prueba de manipulación: "
              "el módulo 18 muestra por qué."],
             ["user", "La petición concreta, y el contexto recuperado que la acompaña.",
              "Es la parte variable. Conviene que vaya después de todo lo estable."],
             ["assistant", "Lo que el modelo respondió antes, y lo que se le puede poner en "
                           "la boca para guiar el formato.",
              "Escribir el inicio de la respuesta esperada es una técnica válida y muy "
              "efectiva para forzar un formato."],
         ],
         [2.2, 6.5, 7.8]),

        ("sub", "Instrucciones: específicas y en positivo"),

        "Dos reglas que conviene demostrar en vivo, porque leídas suenan obvias y aplicadas "
        "casi nadie las cumple.",

        "La primera es la **especificidad medible**. «Resume esto brevemente» "
        "no es una instrucción, es un deseo: brevemente no significa nada concreto. "
        "«Resume esto en máximo tres frases, sin adjetivos valorativos, mencionando "
        "las cifras exactas que aparezcan» sí lo es. La prueba que conviene aplicar en "
        "clase: si dos personas del equipo pueden cumplir la instrucción de formas muy "
        "distintas y ambas serían válidas, la instrucción está incompleta.",

        "La segunda es **decir qué hacer, no qué evitar**. «No uses lenguaje "
        "técnico» deja al modelo sin destino: ha excluido una región del espacio de "
        "continuaciones pero no ha señalado ninguna. «Explícalo como se lo explicarías "
        "a alguien de ventas» sí lo señala. Esto no es psicología del modelo: la "
        "instrucción positiva aporta tokens que empujan hacia la zona deseada, la negativa "
        "solo describe una zona a evitar y además la mantiene presente en el contexto.",

        ("sub", "Contexto: la posición no es neutra"),

        "Aquí se cobra directamente lo aprendido sobre atención. Tres recomendaciones que se "
        "deducen de ella:",

        ("bullets", [
            "**Las instrucciones críticas van al principio o al final**, nunca enterradas "
            "entre documentos. Un patrón muy efectivo con contextos largos es repetir la "
            "instrucción clave al final, después del material.",
            "**El material de referencia va claramente separado** de las instrucciones, con "
            "delimitadores, para que no se confunda una cosa con la otra.",
            "**Menos contexto relevante gana a más contexto por si acaso.** Es la aplicación "
            "directa del tercer modo de fallo del módulo 3: el que no da error y sí baja la "
            "calidad.",
        ]),

        ("sub", "Few-shot: cuándo un ejemplo sustituye a un párrafo"),

        "La regla práctica es que **los ejemplos comunican formato mucho mejor que las "
        "instrucciones, y las instrucciones comunican criterio mejor que los ejemplos.** Si "
        "cuesta describir con palabras cómo debe verse la salida, hay que enseñarla. Si "
        "cuesta describir cuándo aplicar una regla y cuándo no, hay que explicarla.",

        "Cuatro advertencias sobre few-shot que valen la sesión:",

        ("numbers", [
            "**El sesgo de los ejemplos se copia.** Si los tres ejemplos tienen respuestas "
            "largas, las respuestas serán largas. Si por casualidad todos son del mismo "
            "tipo, el modelo generalizará ese tipo.",
            "**Hay que incluir el caso difícil.** Los ejemplos fáciles no enseñan nada que "
            "el modelo no hiciera ya. El ejemplo valioso es el ambiguo, el que muestra qué "
            "hacer cuando la información falta.",
            "**Cuestan tokens en cada petición.** Veinte ejemplos en el prompt se pagan un "
            "millón de veces si hay un millón de llamadas. Ese cálculo es exactamente el "
            "argumento económico legítimo del fine tuning que aparece en el módulo 20.",
            "**Con modelos actuales, menos ejemplos rinden más de lo que se cree.** Dos o "
            "tres bien elegidos suelen bastar. La costumbre de poner diez viene de una "
            "generación anterior de modelos.",
        ]),

        ("sub", "Delimitadores: por qué funcionan de verdad"),

        "Este es el punto donde el módulo 4 se cobra otra vez. Los delimitadores no funcionan "
        "porque el modelo «entienda XML». Funcionan porque marcan fronteras claras "
        "en la secuencia de tokens, y eso le da al mecanismo de atención señales inequívocas "
        "de dónde empieza y termina cada bloque.",

        ("code",
         "<instrucciones>\n"
         "  Extrae el nombre del cliente y el monto total.\n"
         "  Si alguno no aparece, devuelve null en ese campo.\n"
         "</instrucciones>\n"
         "\n"
         "<documento>\n"
         "  ...texto de la factura...\n"
         "</documento>\n"
         "\n"
         "<formato_salida>\n"
         '  {\"cliente\": string|null, \"monto\": number|null}\n'
         "</formato_salida>"),

        "Sirve cualquier convención consistente: etiquetas tipo XML, encabezados Markdown, "
        "líneas de guiones. Lo que importa es que sea **inequívoca y estable**. Las "
        "etiquetas tipo XML tienen una ventaja práctica: son fáciles de generar por código, "
        "fáciles de anidar y difíciles de confundir con el contenido.",

        "Y una advertencia de seguridad que conviene sembrar aquí aunque se desarrolle en el "
        "módulo 18: si el contenido que se inserta entre delimitadores viene de un usuario, "
        "ese usuario puede escribir el delimitador de cierre. Hay que escaparlo o elegir "
        "marcas que no puedan aparecer en el contenido.",

        ("sub", "Cadenas de pensamiento, y cuándo no pedirlas"),

        "Por qué funcionan es una deducción directa del módulo 4: cada token generado entra "
        "como entrada para el siguiente. Si el modelo escribe primero los pasos "
        "intermedios, esos pasos están en el contexto cuando calcula la respuesta final. No "
        "está «pensando más», está **construyendo contexto útil para sí mismo**.",

        ("box", "alerta", "Cuándo NO pedir cadena de pensamiento", [
            "**Con modelos de razonamiento.** Ya generan tokens de razonamiento por su "
            "cuenta. Pedirles explícitamente que piensen paso a paso puede interferir y "
            "empeorar el resultado, además de duplicar el gasto. La recomendación general de "
            "los proveedores en estos modelos es dar la tarea de forma directa.",
            "**En tareas de un solo paso.** Clasificar, extraer un campo, traducir. No hay "
            "razonamiento intermedio que aportar, y se paga latencia y tokens a cambio de nada.",
            "**Cuando la latencia es crítica.** Cada token de razonamiento se genera antes de "
            "que aparezca la primera palabra de la respuesta.",
            "**Cuando se necesita salida estructurada limpia.** Mezclar razonamiento y JSON "
            "en la misma respuesta complica el parseo. Si hace falta, se separan en dos "
            "campos del esquema o en dos llamadas.",
        ]),

        ("sub", "Salidas estructuradas"),

        "Hay tres niveles de rigor y conviene que se conozcan los tres, porque la diferencia "
        "entre ellos es la diferencia entre un prototipo y un sistema:",

        ("table",
         ["Nivel", "Qué es", "Qué garantiza"],
         [
             ["Pedirlo en el prompt",
              "«Responde solo con JSON».",
              "Nada. Funciona casi siempre y falla justo cuando hay volumen. Añade texto "
              "alrededor, cercas de código o disculpas."],
             ["Modo JSON",
              "Un parámetro que obliga a que la salida sea JSON sintácticamente válido.",
              "Que parsea. No que tenga los campos que se esperaban ni los tipos correctos."],
             ["Esquema forzado",
              "Se declara un esquema y el proveedor restringe el muestreo para que la salida "
              "lo cumpla. Incluye el uso de herramientas como mecanismo de formato.",
              "Estructura y tipos. Sigue sin garantizar que el contenido sea verdadero."],
         ],
         [3.2, 6.4, 6.9]),

        "Cuatro recomendaciones de diseño de esquemas, que en la práctica importan más que "
        "el mecanismo:",

        ("bullets", [
            "**Nombres descriptivos.** El nombre del campo es una instrucción. "
            "`monto_total_con_impuestos` guía mejor que `total`.",
            "**Descripciones en el esquema.** La mayoría de los formatos permiten describir "
            "cada campo, y esa descripción llega al modelo. Es prompt engineering dentro del "
            "esquema.",
            "**Planos antes que profundos.** La calidad se degrada con el anidamiento. Tres "
            "niveles ya es mucho.",
            "**Siempre una salida para abstenerse.** Un campo `encontrado` booleano o un "
            "nivel de confianza. Un esquema que obliga a llenar un campo obliga al modelo a "
            "inventarlo, y eso conecta directo con las alucinaciones del módulo 4.",
        ]),

        ("box", "alerta", "La regla que cierra la sección", [
            "**El esquema garantiza la forma, nunca la verdad.** Una salida perfectamente "
            "válida puede contener un dato inventado. Hay que validar en el código de todos "
            "modos, y cualquier decisión de autorización se toma del lado del servidor, "
            "nunca a partir de un campo que devolvió el modelo. Se retoma en el módulo 18.",
        ]),

        ("sub", "Anti-patrones y depuración"),

        "Conviene cerrar con los tres fallos que más se repiten: el prompt kilométrico que "
        "creció por acumulación y ya nadie sabe qué línea hace qué; las instrucciones que se "
        "contradicen entre sí porque se añadieron en momentos distintos; y los adjetivos "
        "vacíos —profesional, conciso, de alta calidad— que no restringen nada.",

        "Y una metodología de depuración, que es lo que realmente separa a quien improvisa "
        "de quien controla:",

        ("numbers", [
            "**Juntar quince o veinte casos reales antes de tocar nada.** Sin un conjunto "
            "fijo de casos no se puede saber si un cambio mejoró o solo movió el problema.",
            "**Cambiar una cosa a la vez** y volver a pasar los casos.",
            "**Registrar el prompt exacto que se envió**, no la plantilla. Es la misma idea "
            "que sostiene el módulo 16.",
            "**Saber cuándo parar.** Si van cinco iteraciones y sigue fallando, el problema "
            "probablemente no es el prompt: le falta contexto, le falta una herramienta o el "
            "modelo es el equivocado. Eso es exactamente la pregunta del módulo 6.",
        ]),
    ],
    "ejercicio": [
        "Cada participante trae un prompt real que use en su trabajo y lo somete a un "
        "rediseño completo:",
        ("numbers", [
            "Reunir diez casos de entrada reales y registrar la salida actual de cada uno.",
            "Reescribir el prompt aplicando el módulo: separar roles, delimitar bloques, "
            "convertir las instrucciones negativas en positivas, sustituir los adjetivos "
            "vacíos por criterios medibles y añadir un esquema de salida con un campo para "
            "abstenerse.",
            "Volver a pasar los diez casos y comparar en una tabla de tres columnas: caso, "
            "antes, después.",
            "Medir los tokens de ambas versiones y anotar la diferencia.",
        ]),
        "La entrega es la tabla comparativa más un párrafo explicando **qué cambio produjo "
        "la mejora y por qué**, apoyándose en el mecanismo del módulo 4.",
    ],
    "evaluacion": [
        "Justifica cada decisión del prompt con el mecanismo, no con la costumbre.",
        "Convierte una instrucción vaga en una instrucción verificable.",
        "Explica por qué los delimitadores funcionan y cómo se abusa de ellos desde fuera.",
        "Identifica al menos dos situaciones en las que NO se debe pedir cadena de pensamiento.",
        "Diseña un esquema de salida que incluye una vía para abstenerse, y sabe que el "
        "esquema no garantiza veracidad.",
        "Depura con un conjunto de casos fijo en lugar de por impresión.",
    ],
}


M6 = {
    "num": 6,
    "title": "La escalera de adaptación de un modelo",
    "tagline": "El mapa del resto del programa, y el módulo que evita un proyecto de fine tuning innecesario.",
    "objetivo": "Ubicar cualquier problema de comportamiento de un modelo en la escalera "
                "prompt → contexto → RAG → herramientas → fine tuning, y justificar por qué "
                "no hace falta subir al siguiente escalón.",
    "duracion": "1 hora",
    "dependencias": "Módulo 5.",
    "contenidos": [
        "El mito: «quiero que responda como mi empresa, entonces necesito fine tuning».",
        ("Los cinco escalones", [
            "Prompt: cambiar las instrucciones.",
            "Contexto: meter la información en la petición.",
            "RAG: recuperar la información correcta automáticamente.",
            "Herramientas: dejar que consulte y actúe sobre sistemas reales.",
            "Fine tuning: modificar los pesos.",
        ]),
        "El criterio que decide: ¿no sabe, o no puede?",
        "Costo, tiempo de iteración y reversibilidad de cada escalón.",
        "Mapa del programa: en qué módulo se cubre cada escalón.",
    ],
    "enfoque": [
        ("box", "nota", "Módulo nuevo, deliberadamente corto", [
            "Este módulo no existía en el temario base, donde el fine tuning aparecía al "
            "final, dentro de conceptos avanzados.",
            "Se adelanta porque el mito que hay que romper aparece el primer día, no el "
            "último. Y se mantiene **corto y sin detalle técnico**: aquí solo se instala el "
            "criterio de decisión y el mapa. Todo lo técnico —LoRA, datasets, hospedaje, "
            "costo real— vive en el módulo 20, que cierra el arco que este abre.",
        ]),

        ("sub", "Abrir por el mito"),

        "La secuencia mental que hay que interrumpir es esta, y conviene escribirla tal cual "
        "en el pizarrón porque casi todo el mundo la reconoce:",

        ("code",
         "«quiero que responda como mi empresa»\n"
         "          ↓\n"
         "     fine tuning"),

        "Y al lado, el orden real:",

        ("code",
         "Prompt  →  Contexto  →  RAG  →  Herramientas  →  Fine tuning"),

        "En la enorme mayoría de los casos, «que responda como mi empresa» se "
        "resuelve en el primer escalón: un system prompt bien escrito y tres o cuatro "
        "ejemplos. Decirlo así, sin matices, es el punto del módulo.",

        ("sub", "Por qué el orden es ese"),

        "El orden no es estético ni ideológico. Es económico y de velocidad de iteración.",

        ("table",
         ["Escalón", "Qué problema resuelve", "Tiempo de iteración", "Reversibilidad"],
         [
             ["Prompt", "Le falta instrucción: no sabe qué se espera de él.",
              "Segundos", "Total. Se deshace cambiando texto."],
             ["Contexto", "Le falta información, y esa información cabe en la petición.",
              "Minutos", "Total."],
             ["RAG", "Le falta información, es demasiada y cambia con el tiempo.",
              "Días", "Alta, aunque hay infraestructura que mantener."],
             ["Herramientas", "No le falta información: le falta poder consultar o actuar "
                              "sobre sistemas vivos.",
              "Días", "Alta."],
             ["Fine tuning", "Tiene toda la información y aun así no produce de forma "
                             "consistente el formato, el tono o el criterio que se necesita.",
              "Semanas", "Baja. Queda un artefacto que hay que mantener y reentrenar."],
         ],
         [2.6, 6.4, 2.9, 4.6]),

        "La regla que hay que dejar dicha: **se sube de escalón cuando el anterior se agotó, "
        "no cuando se puso difícil.**",

        ("sub", "La pregunta que resuelve la decisión"),

        "Todo el módulo se puede comprimir en una sola pregunta, y conviene que la sala salga "
        "con ella memorizada:",

        ("box", "correccion", "¿El modelo no sabe, o no puede?", [
            "**No sabe** — le falta la información: los precios de la empresa, el contenido "
            "de un documento, lo que pasó ayer. Entonces la solución es contexto, RAG o "
            "herramientas. **El fine tuning no aplica**, y el módulo 20 explica por qué "
            "intentarlo puede empeorar las cosas.",
            "**No puede** — tiene toda la información delante y aun así no produce el "
            "formato correcto, no sostiene el tono, o falla de forma consistente en un "
            "criterio propio del dominio. Ahí el fine tuning entra en la conversación, "
            "después de haber agotado el prompt.",
            "**La prueba diagnóstica**, que es trivial y hay que enseñarla: pegar la "
            "información directamente en el prompt. Si con eso acierta, el problema era de "
            "contexto y acaba de ahorrarse un proyecto de tres semanas.",
        ]),

        ("sub", "Cerrar con el mapa"),

        "Los últimos diez minutos se dedican a mostrar dónde vive cada escalón en el resto "
        "del programa. Esto convierte los catorce módulos siguientes en respuestas a una "
        "pregunta ya planteada:",

        ("table",
         ["Escalón", "Dónde se cubre"],
         [
             ["Prompt", "Módulo 5, ya visto."],
             ["Contexto", "Módulos 7 y 8: la API sin estado y la arquitectura de memoria."],
             ["RAG", "Módulos 11, 12 y 13: bases de datos, embeddings y recuperación."],
             ["Herramientas", "Módulos 9 y 10: agentes y protocolos de comunicación."],
             ["Fine tuning", "Módulo 20, al final del programa."],
         ],
         [3.4, 13.1]),

        ("box", "alerta", "Una aclaración necesaria sobre el orden", [
            "El programa **no recorre la escalera en el orden de la escalera**: ve "
            "herramientas y agentes en los módulos 9 y 10, antes que RAG en el 13.",
            "Conviene decirlo en voz alta para que nadie se confunda. La escalera ordena por "
            "**costo y complejidad de adaptación**; el temario ordena por **dependencia "
            "conceptual**. Son dos criterios distintos y ambos son correctos. Al abrir el "
            "módulo 13 conviene recordar en qué escalón se está.",
        ]),
    ],
    "ejercicio": [
        "Se reparten seis situaciones reales y cada grupo debe ubicarlas en un escalón y "
        "justificar por qué no hace falta subir más. Ejemplos que funcionan bien:",
        ("bullets", [
            "«El asistente responde con un tono demasiado informal para nuestros clientes.»",
            "«No conoce nuestra política de devoluciones, que cambió el mes pasado.»",
            "«Necesitamos que devuelva siempre el mismo formato de JSON y a veces se lo salta.»",
            "«No sabe cuántas unidades hay en inventario ahora mismo.»",
            "«Tenemos doce mil documentos internos y necesita poder consultarlos.»",
            "«Tenemos un prompt de cuatro mil tokens con veinte ejemplos y hacemos dos "
            "millones de llamadas al mes.»",
        ]),
        "El último caso es el interesante: es el único donde el fine tuning tiene un "
        "argumento económico legítimo, y conviene que la sala llegue sola a esa conclusión.",
    ],
    "evaluacion": [
        "Ubica un problema en el escalón correcto y justifica por qué no hace falta subir.",
        "Aplica la pregunta «¿no sabe o no puede?» y la prueba diagnóstica de pegar "
        "la información en el prompt.",
        "Explica el orden de la escalera en términos de costo, iteración y reversibilidad.",
        "Reconoce que el temario no sigue el orden de la escalera, y por qué.",
    ],
}


M7 = {
    "num": 7,
    "title": "El LLM como servicio: API frente a chat",
    "tagline": "La revelación que reorganiza todo: la API no tiene memoria, y la arquitectura de contexto es responsabilidad de quien construye.",
    "objetivo": "Explicar la diferencia entre consumir un chat y consumir una API de "
                "modelo, y asumir la consecuencia: el estado de la conversación lo diseña y "
                "lo mantiene quien construye el sistema.",
    "duracion": "2 horas",
    "dependencias": "Módulos 4 y 5.",
    "contenidos": [
        "Qué hace realmente un chat de AI que la API no hace.",
        "La petición mínima: modelo, mensajes y parámetros.",
        "La ausencia de estado: cada petición empieza de cero.",
        "Cómo se simula una conversación reenviando el historial.",
        "Parámetros habituales: temperatura, top-p, máximo de tokens, secuencias de parada, semilla.",
        "El campo de uso de la respuesta: la fuente de verdad del consumo.",
        "Streaming: por qué la respuesta aparece token a token.",
        "Errores, límites de tasa y reintentos.",
        "Handoff: la API del modelo es un protocolo entre varios.",
    ],
    "enfoque": [
        ("sub", "El mensaje central del módulo"),

        "Este módulo tiene una sola idea que importa, y todo lo demás es andamiaje para "
        "llegar a ella: **la API no tiene memoria.** Cada petición es independiente. El "
        "modelo no sabe que existió una petición anterior, no sabe quién es el usuario, no "
        "sabe qué se dijo hace dos mensajes. Cada llamada es, literalmente, el primer mensaje.",

        "El temario base ya identificaba esto como el punto más importante del módulo, y "
        "acertaba. Merece ser el eje.",

        ("sub", "Empezar por la comparación, porque todos tienen la referencia"),

        "Casi todo el mundo en la sala ha usado un chat de AI. Casi nadie ha pensado en qué "
        "hace el chat que la API no hace. Conviene construir esa lista en el pizarrón antes "
        "de mostrar una sola línea de código:",

        ("table",
         ["Lo que hace el chat", "Quién lo hace en la API"],
         [
             ["Recuerda la conversación", "Tu código. Reenviando el historial en cada petición."],
             ["Sabe quién eres y tus preferencias", "Tu código. Guardando y recuperando de una base de datos."],
             ["Busca en internet cuando hace falta", "Tu código. Llamando a un buscador y pegando los resultados."],
             ["Ejecuta código y analiza archivos", "Tu código. Con herramientas, módulo 9."],
             ["Corta el historial cuando ya no cabe", "Tu código. Con la política que tú decidas, módulo 8."],
             ["Reintenta si el servicio falla", "Tu código."],
             ["Muestra la respuesta poco a poco", "Tu código, consumiendo el flujo de streaming."],
         ],
         [7.0, 9.5],
         "La columna derecha es, esencialmente, el índice de la Parte III de este programa."),

        "La conclusión que hay que enunciar: **un chat de AI es un producto construido "
        "encima de una API, y ese producto es en su mayor parte todo lo que no es el "
        "modelo.** Quien construye con la API está construyendo ese producto.",

        ("sub", "Demostrar la ausencia de estado, no contarla"),

        "La demostración cabe en dos peticiones y es más persuasiva que cualquier "
        "explicación. Primero:",

        ("code",
         'messages = [\n'
         '    {"role": "user", "content": "Me llamo Cristian."}\n'
         ']'),

        "El modelo saluda. Y después, en una petición nueva:",

        ("code",
         'messages = [\n'
         '    {"role": "user", "content": "¿Cómo me llamo?"}\n'
         ']'),

        "No lo sabe. Y no lo sabe porque nunca lo supo: no hay sesión, no hay identificador "
        "de usuario implícito, no hay nada guardado del lado del proveedor. La forma de que "
        "lo sepa es mandarlo todo otra vez:",

        ("code",
         'messages = [\n'
         '    {"role": "user",      "content": "Me llamo Cristian."},\n'
         '    {"role": "assistant", "content": "Mucho gusto, Cristian."},\n'
         '    {"role": "user",      "content": "¿Cómo me llamo?"}\n'
         ']'),

        "Aquí hay que detenerse y hacer explícita la consecuencia económica, porque es el "
        "gancho perfecto para el módulo 14: en el turno veinte se está reenviando toda la "
        "conversación anterior. **El costo de una conversación no crece de forma lineal con "
        "su longitud, crece mucho más rápido.** No hace falta desarrollarlo aquí; basta con "
        "dejar la incomodidad instalada.",

        ("sub", "Los parámetros, sin repetir el módulo 4"),

        "La temperatura, el top-p y el top-k ya se explicaron con la distribución delante, "
        "así que aquí solo se ubican como campos de la petición. Lo que sí es nuevo y merece "
        "atención:",

        ("bullets", [
            "**Máximo de tokens de salida.** Es un límite duro, no una sugerencia de "
            "longitud: si se alcanza, la respuesta se corta a media frase. Hay que revisar "
            "siempre el motivo de finalización que devuelve la API para distinguir «terminó» "
            "de «se quedó sin espacio».",
            "**Secuencias de parada.** Detienen la generación al encontrar cierto texto. "
            "Útiles con formatos propios.",
            "**Semilla.** Algunos proveedores la ofrecen para acercarse a la "
            "reproducibilidad, pero conviene ser honesto: no garantiza determinismo perfecto "
            "en un servicio distribuido.",
            "**El campo de uso de la respuesta.** Es el dato más importante de la respuesta "
            "después del texto: tokens de entrada, de salida, de razonamiento y de caché. Es "
            "la fuente de verdad para todo el módulo 14 y para las métricas del módulo 16. "
            "Conviene registrarlo desde la primera línea de código que se escriba.",
        ]),

        ("box", "nota", "Sembrar el caché de prompts", [
            "Vale la pena mencionar aquí, en una frase, que la mayoría de los proveedores "
            "permiten cachear el prefijo estable del prompt y cobrarlo mucho más barato al "
            "reutilizarlo. No hay que desarrollarlo: el módulo 14 lo cuantifica.",
            "Pero sí hay que decir la consecuencia de diseño, porque condiciona cómo se "
            "escribe el código desde hoy: **lo estable va al principio del prompt y lo "
            "variable al final.**",
        ]),

        ("sub", "Streaming, errores y límites"),

        "El streaming se explica en cinco minutos y conviene hacerlo porque desmitifica algo "
        "que todo el mundo ha visto: los tokens aparecen uno a uno porque se generan uno a "
        "uno, y la API puede ir enviándolos conforme salen. No es un efecto visual. Baja "
        "mucho el tiempo hasta el primer token percibido sin cambiar la latencia total.",

        "De los errores, lo que hay que dejar es una lista corta de lo que sí va a ocurrir en "
        "producción: límites de tasa, saturación temporal del proveedor, exceso de contexto, "
        "y respuestas que no cumplen el formato esperado. La política mínima razonable es "
        "reintento con espera creciente y un tope, y **presupuesto de reintentos**, porque "
        "un bucle de reintentos sin límite es un incidente de facturación. Es el mismo "
        "riesgo que el módulo 18 señala para la reindexación.",

        ("sub", "Cerrar con el handoff explícito"),

        ("box", "nota", "Frase de cierre recomendada", [
            "«Acaban de usar un protocolo de comunicación: una API REST sobre HTTP. Es "
            "uno de varios, y no es el único que va a aparecer en un sistema de AI. En el "
            "módulo 10 se ven todos juntos —REST, webhooks, streaming y MCP— y se explica "
            "qué problema resuelve cada uno. Antes hace falta ver por qué un agente los "
            "necesita.»",
            "Este handoff importa: sin él, el módulo 10 se lee como una repetición de este. "
            "Con él, se lee como la continuación que es.",
        ]),
    ],
    "ejercicio": [
        "Construir, desde cero y sin ninguna biblioteca de orquestación, un chat de consola "
        "de menos de cincuenta líneas que:",
        ("bullets", [
            "Mantenga el historial en una lista y lo reenvíe completo en cada turno.",
            "Imprima, después de cada respuesta, los tokens de entrada, los de salida y el "
            "costo acumulado de la sesión con los precios reales del proveedor.",
            "Corte el historial cuando supere un límite de tokens configurable, avisando en "
            "pantalla cuando lo haga.",
            "Consuma la respuesta por streaming.",
        ]),
        "La entrega incluye una captura de la sesión con el costo acumulado tras veinte "
        "turnos, y una respuesta escrita a la pregunta: **¿por qué el turno veinte cuesta "
        "tanto más que el primero?**",
    ],
    "evaluacion": [
        "Explica sin ayuda que la API no tiene estado y qué implica eso para la arquitectura.",
        "Distingue lo que hace el modelo de lo que hace el producto construido a su alrededor.",
        "Construye una conversación de varios turnos manejando el historial a mano.",
        "Lee el campo de uso de la respuesta y calcula el costo real de una sesión.",
        "Reconoce que el turno N reenvía todo lo anterior, y anticipa el efecto en la factura.",
    ],
}


PARTS = [
    {
        "kicker": "PARTE II",
        "title": "Cómo se le habla a un modelo",
        "intro": "Con el mecanismo ya entendido, esta parte cubre la única interfaz que "
                 "existe con un modelo —el prompt—, instala el criterio para decidir qué "
                 "técnica aplicar a cada problema, y termina con la revelación que "
                 "reorganiza todo lo que viene después: la API no tiene memoria. Seis horas.",
        "modules": [M5, M6, M7],
    },
]
