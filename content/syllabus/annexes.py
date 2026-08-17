# -*- coding: utf-8 -*-
"""Anexos del documento: A (dependencias) y B (glosario).

El antiguo Anexo B —registro de correcciones respecto al borrador base— se
retiro del documento; su contenido vive en syllabus_anexo_correcciones.py y
no se importa desde ningun lado.
"""

ANEXO_A = {
    "title": "Anexo A · Mapa de dependencias",
    "blocks": [
        ("lead", "Qué necesita saber la persona participante antes de cada módulo. Útil si "
                 "se quiere impartir el programa en otro orden, partirlo en bloques o "
                 "diseñar una ruta corta."),

        ("h2", "Dependencias por módulo"),

        ("table",
         ["Módulo", "Requiere", "Es requisito de"],
         [
             ["1. Introducción", "—", "2, 3"],
             ["2. Qué es un LLM", "1", "3, 4"],
             ["3. Tokens y ventana de contexto", "1, 2", "4, 7, 14"],
             ["4. Cómo razona un LLM", "3", "**Todos los siguientes**"],
             ["5. Prompt engineering", "4", "6, 9, 13, 18"],
             ["6. La escalera de adaptación", "5", "20"],
             ["7. API frente a chat", "4, 5", "8, 9, 10"],
             ["8. Contexto y memoria", "7", "9, 11, 15"],
             ["9. Agentes", "5, 7, 8", "10, 15, 18"],
             ["10. Protocolos", "7, 9", "18"],
             ["11. Bases de datos", "8", "12, 13"],
             ["12. Embeddings", "4, 11", "13"],
             ["13. RAG", "11, 12", "14, 16, 18"],
             ["14. Costos", "7, 9, 13", "15, 16, 20"],
             ["15. Orquestación", "9, 14", "16, 17"],
             ["16. Observabilidad", "13, 14, 15", "17, 18, 20"],
             ["17. Buenas prácticas", "8, 14, 15, 16", "—"],
             ["18. Seguridad", "9, 10, 13, 16", "—"],
             ["19. Conceptos avanzados", "Parte IV completa", "—"],
             ["20. Fine tuning en detalle", "6, 14, 16", "—"],
         ],
         [5.4, 4.6, 5.5]),

        ("h2", "Los tres módulos bisagra"),

        "Si hay que recortar, estos tres no se pueden tocar sin que el resto pierda sentido:",

        ("bullets", [
            "**Módulo 4 — Cómo razona un LLM.** Todo lo que viene después consiste en "
            "manipular la predicción del siguiente token. Sin este módulo, el resto del "
            "programa se convierte en una colección de recetas.",
            "**Módulo 7 — API frente a chat.** La ausencia de estado es lo que crea la "
            "necesidad de la Parte III completa. Sin esta revelación, la memoria, el RAG y la "
            "orquestación parecen complicaciones gratuitas.",
            "**Módulo 12 — Embeddings.** Una base vectorial sin entender embeddings se "
            "percibe como magia, y el módulo 13 se vuelve imposible de depurar.",
        ]),

        ("h2", "Rutas alternativas"),

        ("table",
         ["Ruta", "Módulos", "Horas", "Para quién"],
         [
             ["Programa completo", "1 a 20", "44",
              "Equipos que van a construir y operar sistemas de AI."],
             ["Fundamentos", "1 a 8", "20",
              "Perfiles no técnicos, o una primera fase antes de decidir si continuar."],
             ["Ruta RAG", "1 a 4, 7, 11, 12, 13, 14, 16", "22",
              "Equipos cuyo objetivo inmediato es recuperación sobre documentación propia."],
             ["Ruta agentes", "1 a 10, 14, 15, 16, 18", "30",
              "Equipos que van a construir automatizaciones con herramientas."],
             ["Puesta al día para personas con experiencia", "4, 6, 13, 14, 16, 18", "15",
              "Quienes ya construyen con AI pero aprendieron por recetas."],
         ],
         [4.6, 3.8, 1.6, 5.5]),

        ("box", "nota", "Sobre la ruta de puesta al día", [
            "Es la más solicitada por equipos que ya trabajan con AI, y la selección no es "
            "arbitraria: son los seis módulos que corrigen los malentendidos más caros. El "
            "mecanismo del modelo, la escalera de adaptación, la corrección de la similitud "
            "coseno, el desglose real de costos, la instrumentación y las vulnerabilidades "
            "propias de la AI.",
        ]),
    ],
}


ANEXO_B = {
    "title": "Anexo B · Glosario",
    "blocks": [
        ("lead", "Términos que aparecen en el programa, con la definición que se usa aquí y "
                 "el módulo donde se desarrollan."),

        ("table",
         ["Término", "Definición", "Módulo"],
         [
             ["Agente", "Sistema con objetivo, memoria, herramientas, planificación, "
                        "observación, acción y reflexión, que itera hasta cumplir su objetivo "
                        "o agotar su presupuesto.", "9"],
             ["Alucinación", "Continuación estadísticamente plausible producida sin "
                             "información que la respalde. Es el mecanismo funcionando, no un "
                             "fallo.", "4"],
             ["Atención", "Mecanismo por el que el modelo pondera de forma distinta cada "
                          "token anterior al predecir el siguiente.", "4"],
             ["Búsqueda híbrida", "Combinación de recuperación léxica y semántica, fusionando "
                                  "ambos conjuntos de resultados.", "13"],
             ["Caché de prompts", "Reutilización del prefijo ya procesado de un prompt, a un "
                                  "precio muy reducido. Funciona por coincidencia exacta del "
                                  "prefijo.", "14"],
             ["Chunk / trozo", "Fragmento en que se divide un documento para indexarlo. Cada "
                               "uno produce un embedding.", "13"],
             ["Destilación", "Entrenar un modelo pequeño con datos generados y filtrados por "
                             "uno grande.", "20"],
             ["Embedding (interno)", "Representación vectorial de un token dentro del modelo "
                                     "generativo. No se expone ni sirve para buscar.", "4"],
             ["Embedding (de recuperación)", "Vector que representa el significado de un "
                                             "fragmento de texto, producido por un modelo "
                                             "específico para poder compararlo con otros.", "12"],
             ["Fine tuning", "Modificar los pesos de un modelo con ejemplos propios. Último "
                             "escalón de la escalera de adaptación.", "6, 20"],
             ["Guardrail", "Control que impide que el sistema se salga del comportamiento "
                           "previsto. Su fiabilidad depende de la capa donde se implemente.", "18"],
             ["Inyección de prompts", "Manipulación del comportamiento del sistema mediante "
                                      "texto. Directa si viene del usuario, indirecta si viene "
                                      "de contenido que el sistema lee.", "18"],
             ["LoRA", "Método de ajuste eficiente que congela el modelo base y entrena un "
                      "conjunto pequeño de matrices añadidas.", "20"],
             ["MCP", "Protocolo abierto que estandariza cómo un host de AI accede a "
                     "herramientas, recursos y plantillas externas. Su consumidor es el "
                     "modelo, no el código.", "10"],
             ["Producto punto", "Métrica de similitud sensible tanto a la orientación como a "
                                "la magnitud. Equivale a la similitud coseno si los vectores "
                                "están normalizados.", "13"],
             ["RAG", "Recuperar información relevante y añadirla al prompt antes de generar. "
                     "Su ganancia está en la búsqueda, no en la generación.", "13"],
             ["Reordenamiento", "Segundo paso que evalúa con más precisión los candidatos "
                                "recuperados para quedarse con los mejores. Baja el costo y "
                                "sube la calidad a la vez.", "13"],
             ["Similitud coseno", "Coseno del ángulo entre dos vectores. Mide orientación e "
                                  "ignora la magnitud. **No es una distancia.**", "13"],
             ["Skill", "Instrucciones sobre cómo hacer bien algo, que se cargan cuando son "
                       "relevantes. Es conocimiento procedimental, no capacidad.", "9"],
             ["Span", "Cada operación registrada dentro de una traza: una llamada al modelo, "
                      "una recuperación, una herramienta.", "16"],
             ["Temperatura", "Parámetro que aplana o agudiza la distribución de probabilidad "
                             "antes de muestrear. Controla aleatoriedad, no calidad.", "4"],
             ["Token", "Unidad en que se fragmenta el texto para el modelo. Es también la "
                       "unidad de cobro.", "3"],
             ["Tokens de razonamiento", "Texto intermedio que generan los modelos de "
                                        "razonamiento. Se factura como salida aunque no se "
                                        "muestre.", "4, 14"],
             ["Tool / herramienta", "Función que el agente puede solicitar ejecutar. El modelo "
                                    "no la ejecuta: la pide, y el código la ejecuta.", "9"],
             ["Traza", "Árbol de operaciones de una petición completa, desde la entrada del "
                       "usuario hasta la respuesta.", "16"],
             ["Ventana de contexto", "Número máximo de tokens que caben en una petición, "
                                     "incluyendo prompt, herramientas, historial, contexto "
                                     "recuperado y respuesta.", "3"],
             ["Webhook", "Inversión del modelo pull: el servidor remoto avisa cuando ocurre un "
                         "evento. Exige verificar firma y ser idempotente.", "10"],
         ],
         [3.6, 10.4, 2.5]),
    ],
}


ANEXOS = [ANEXO_A, ANEXO_B]
