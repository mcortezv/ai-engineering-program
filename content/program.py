# -*- coding: utf-8 -*-
"""Metadatos del programa y preámbulo del documento.

Aquí se edita la portada, la duración total y todo lo que va antes
del primer módulo. Los módulos viven en content/syllabus/partN.py.
"""

META = {
    "mark": "HyperLabs",
    "title": "Programa de AI",
    "subtitle": "Cómo funciona, de verdad, un sistema de inteligencia artificial",
    "who": "HyperLabs",
    "who_sub": "Área de desarrollo de Hyperdigital · Programa de formación interna",
    "footer": "Programa de AI · HyperLabs",
    "cover_meta": [
        "**Dirigido a:** desarrolladores de software, con un diseño que permite "
        "seguirlo sin experiencia previa en AI",
        "**Duración:** 44 horas lectivas · 20 módulos · 5 partes",
        "**Modalidad:** sesiones teórico-prácticas con ejercicio evaluable por módulo",
        "**Versión:** 2.0 · revisión del temario base con correcciones técnicas",
        "**Documento base:** Programa de AI.docx · correcciones señaladas en cada módulo",
    ],
}


FRONTMATTER = [
    ("h1", "Sobre este programa"),

    ("box", "nota", "Qué se lleva quien termina este programa", [
        "La capacidad de leer, diseñar y discutir la arquitectura de un sistema de AI "
        "completo: entender por qué cada pieza está donde está, cuánto cuesta, cómo "
        "falla y cómo se mide.",
        "Y, sobre todo, criterio propio para construirlo apoyándose en agentes de código "
        "como Claude Code, sabiendo exactamente qué le está pidiendo al agente y por qué.",
    ]),

    ("lead", "La mayoría de los cursos de AI enseñan a usar herramientas. Este enseña a "
             "entender el sistema que hay debajo, para que las herramientas se puedan "
             "cambiar sin volver a empezar."),

    ("h2", "Propósito"),

    "Existe una brecha incómoda en los equipos de desarrollo: casi todo el mundo ha usado "
    "un chat de AI, muy poca gente ha construido un sistema de AI, y prácticamente nadie "
    "sabe explicar qué ocurre entre ambas cosas. Esa brecha produce dos errores caros y "
    "simétricos. El primero es tratar al modelo como una caja mágica que "
    "«entiende», y construir encima de una intuición equivocada. El segundo es "
    "copiar arquitecturas de referencia sin saber qué problema resolvía cada pieza, y "
    "terminar con un sistema que funciona en la demo y es imposible de pagar, de depurar "
    "o de mantener en producción.",

    "Este programa ataca esa brecha desde el mecanismo. Su hipótesis es que si alguien "
    "entiende de verdad que un modelo de lenguaje predice el siguiente token, y nada más "
    "que eso, entonces el prompt engineering, la ventana de contexto, el RAG, los agentes, "
    "el costo y las alucinaciones dejan de ser temas sueltos que hay que memorizar y se "
    "convierten en consecuencias de un mismo hecho. Ese es el hilo que atraviesa los "
    "veinte módulos.",

    ("h2", "A quién está dirigido"),

    "El destinatario principal es una persona que ya programa: entiende qué es una API, "
    "qué es una base de datos y qué es una petición HTTP. Para esa persona, el programa "
    "asume ese vocabulario y no lo vuelve a explicar.",

    "Al mismo tiempo, está deliberadamente diseñado para que alguien de producto, diseño u "
    "operaciones pueda seguirlo completo. Eso impone una restricción de escritura que se "
    "respeta en todo el documento: no hay una sola fórmula que sea imprescindible para "
    "entender la idea. Donde aparece una expresión matemática, siempre está acompañada de "
    "la versión en palabras, y la versión en palabras basta.",

    ("box", "nota", "Prerrequisitos reales", [
        "**Indispensable:** saber leer código en cualquier lenguaje y haber consumido "
        "alguna API HTTP alguna vez, aunque sea desde Postman.",
        "**Recomendable:** nociones básicas de bases de datos relacionales y haber usado "
        "un chat de AI de forma habitual.",
        "**No se requiere:** matemáticas más allá de la preparatoria, estadística, "
        "álgebra lineal ni experiencia previa en machine learning.",
    ]),

    ("h2", "Resultados de aprendizaje"),

    "Al terminar el programa, la persona participante será capaz de:",

    ("numbers", [
        "**Explicar el mecanismo.** Describir qué hace un modelo de lenguaje cuando recibe "
        "un prompt, y derivar de ahí por qué alucina, por qué el orden del contexto "
        "importa y por qué no aprende de la conversación.",
        "**Diseñar el contexto.** Decidir qué información entra en cada petición, de dónde "
        "sale y cuándo se descarta, entendiendo que la API no tiene memoria y que esa "
        "arquitectura es responsabilidad de quien construye.",
        "**Elegir la técnica correcta.** Ubicar cualquier problema en la escalera prompt → "
        "contexto → RAG → herramientas → fine tuning, y justificar por qué no hace falta "
        "subir al siguiente escalón.",
        "**Construir un RAG que funcione.** Explicar con precisión cómo se recupera "
        "información por significado, qué mide realmente la similitud coseno y qué métrica "
        "conviene en cada caso.",
        "**Diseñar agentes que sobrevivan a las modas.** Separar lo que un agente necesita "
        "conceptualmente de la herramienta concreta que hoy lo implementa.",
        "**Estimar el costo antes de construir.** Calcular lo que va a costar una "
        "funcionalidad al mes y saber qué palanca mover para bajarlo.",
        "**Operar el sistema.** Instrumentar trazas suficientes para responder por qué el "
        "sistema respondió lo que respondió, y detectar los modos de fallo propios de la AI.",
    ]),

    ("h2", "Cómo está organizado"),

    "El programa avanza en cinco partes, y el orden no es arbitrario: cada parte cierra "
    "una pregunta que la siguiente necesita tener resuelta.",

    ("table",
     ["Parte", "Pregunta que responde", "Módulos", "Horas"],
     [
         ["I. Fundamentos", "¿Qué es y qué no es un modelo de lenguaje?", "1 – 4", "8"],
         ["II. Cómo se le habla a un modelo", "¿Cómo consigo que haga lo que necesito?", "5 – 7", "6"],
         ["III. Construir un sistema", "¿Cómo le doy memoria, información y capacidad de actuar?", "8 – 13", "16"],
         ["IV. Operar un sistema", "¿Cómo lo hago pagable, observable y seguro?", "14 – 18", "10"],
         ["V. Más allá", "¿Qué hago cuando todo lo anterior se queda corto?", "19 – 20", "4"],
     ],
     [4.0, 6.6, 2.2, 1.6],
     "Total: 44 horas lectivas. Las duraciones son una propuesta de calibración; conviene "
     "ajustarlas tras la primera impartición."),

    ("h2", "Estructura de cada módulo"),

    "Todos los módulos siguen la misma plantilla, para que el documento sirva como guía de "
    "clase y no solo como índice de temas:",

    ("bullets", [
        "**Objetivo de aprendizaje** — qué podrá hacer la persona al terminar, en una frase.",
        "**Contenidos** — los subtemas en el orden en que se imparten.",
        "**Enfoque didáctico** — cómo abordar cada tema: qué analogía usar, qué error "
        "anticipar, dónde detenerse y qué decir en voz alta. Es la sección más extensa y es "
        "donde vive el criterio pedagógico del programa.",
        "**Ejercicio práctico** — una actividad concreta y verificable.",
        "**Criterios de evaluación** — cómo se comprueba que el objetivo se cumplió.",
    ]),

    ("h2", "Sobre esta versión"),

    "Este documento es una revisión del temario base de Hyperlabs. Conserva íntegramente su "
    "enfoque y su secuencia narrativa, y añade cuatro módulos nuevos, reubica tres y corrige "
    "una serie de imprecisiones técnicas del borrador original.",

    ("box", "correccion", "Dónde están señalados los cambios", [
        "Cada corrección técnica respecto al borrador base aparece señalada **en el módulo "
        "donde vive**, en un recuadro de este color, con la afirmación original citada, por "
        "qué era incorrecta y cómo quedó redactada.",
        "El **Anexo A** muestra el mapa de dependencias entre módulos, útil si se quiere "
        "impartir el programa en un orden distinto o partirlo en varios bloques.",
    ]),

    ("box", "volatil", "Contenido con fecha de caducidad", [
        "Algunas secciones describen productos y protocolos concretos que van a cambiar. "
        "Están marcadas con este color a lo largo del documento y conviene revisarlas antes "
        "de cada impartición. El contenido conceptual que las rodea no caduca: esa "
        "separación es intencional y es la razón de que el módulo de agentes esté dividido "
        "en dos mitades.",
    ]),
]


