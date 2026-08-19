# -*- coding: utf-8 -*-
"""Deck: Módulo 16 — Observabilidad."""

from engine.diagrams import mod16 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 16 · Observabilidad",
    "footer": "Programa de AI · Módulo 16",
    "outfile": "Modulo 16 - Observabilidad.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 16  ·  2 HORAS",
        "title": "Observabilidad",
        "tagline": "Poder responder por qué el sistema respondió lo que respondió.",
        "meta": [
            "<b>Antes de esta sesión:</b> recuperación, costos y orquestación",
            "<b>Al terminar:</b> instrumentas lo suficiente para depurar de verdad",
        ],
    },

    {
        "kind": "statement",
        "text": "En un sistema de AI el fallo típico es un <em>200 OK con una "
                "respuesta mala</em>.",
        "after": "No hay excepción, no hay error, y desde fuera todo se ve sano.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Por qué lo de siempre no alcanza</b> — el fallo silencioso y el no
            determinismo.</li>
          <li><b>La traza como árbol</b> — modelar una petición completa.</li>
          <li><b>Qué registrar</b> — por tipo de operación, y el campo que casi todos
            olvidan.</li>
          <li><b>Métricas</b> — por qué el promedio miente.</li>
          <li><b>El prompt es código</b> — versionarlo y poder revertirlo.</li>
          <li><b>Privacidad y muestreo</b> — lo que cuesta observar.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Por qué lo de siempre no alcanza",
        "note": "La diferencia que justifica dedicarle una sesión entera.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Dos modos de fallo distintos",
        "title": "El error que se anuncia y el que no",
        "html": dg.fallo_silencioso(),
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Y encima no se reproduce",
        "title": "Tres cosas que hacen difícil depurar esto",
        "html": """
        <ul class="pts">
          <li><b>El mismo caso puede fallar una de cada diez veces.</b>
            <span class="n">Se sortea un token de una distribución, así que dos
            ejecuciones idénticas pueden divergir. No puedes reproducir el fallo a
            voluntad.</span></li>
          <li><b>Sin el prompt exacto no hay forma de reconstruirlo.</b>
            <span class="n">La plantilla no basta: lo que hay que guardar es el texto
            renderizado que se envió, con el contexto que se recuperó ese día y el
            historial que había.</span></li>
          <li><b>Y el sistema cambia debajo de ti.</b>
            <span class="n">El proveedor actualiza el modelo, alguien edita un prompt,
            el corpus se reindexa. Sin registrar la versión de cada cosa no puedes
            responder qué cambió.</span></li>
        </ul>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "La traza como árbol",
        "note": "El concepto central: una petición es un árbol de operaciones.",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Una petición completa",
        "title": "Qué pasó, en qué orden y cuánto costó cada paso",
        "html": dg.traza_arbol(),
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Qué guardar en cada tipo de operación",
        "title": "Los campos que hacen falta",
        "html": dg.que_registrar(),
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "El campo que más veces salva una depuración",
        "title": "Sin los puntajes no sabes qué falló",
        "html": dg.fallo_recuperacion_o_generacion(),
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Y en los registros",
        "title": "Lo renderizado, no la plantilla",
        "html": """
        <ul class="pts">
          <li><b>El prompt final tal como salió.</b>
            <span class="n">Con las variables ya sustituidas y el contexto ya
            pegado. La plantilla no reproduce el fallo.</span></li>
          <li><b>Los documentos recuperados en su forma exacta.</b>
            <span class="n">Si el corpus se reindexa mañana, el trozo que causó la
            mala respuesta puede haber dejado de existir.</span></li>
          <li><b>Los errores del proveedor, con código y cuerpo.</b>
            <span class="n">Un «falló la llamada» sin más no permite distinguir un
            límite de tasa de un contexto excedido.</span></li>
          <li><b>Los reintentos: cuántos y por qué.</b>
            <span class="n">Una latencia alta que en realidad son tres intentos se
            diagnostica en segundos si está registrado, y en horas si no.</span></li>
        </ul>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Métricas",
        "note": "Qué medir, y por qué el promedio no sirve.",
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "Colas largas",
        "title": "El promedio miente",
        "html": dg.promedio_miente(),
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "El cuadro mínimo",
        "title": "Qué tener desde el primer día",
        "html": """
        <table>
          <thead><tr><th style="width:26%">Métrica</th><th style="width:36%">Cómo cortarla</th>
          <th>Para qué sirve</th></tr></thead>
          <tbody>
            <tr><td><b>Costo</b></td>
              <td>por petición, sesión, usuario, funcionalidad y modelo</td>
              <td>Sin atribución, cuando la factura suba no sabrás qué recortar.</td></tr>
            <tr><td><b>Latencia</b></td>
              <td>p50, p95, p99 — y el tiempo al primer token aparte</td>
              <td>El usuario percibe el primer token, no el total.</td></tr>
            <tr><td><b>Errores y reintentos</b></td>
              <td>por tipo y por proveedor</td>
              <td>Distingue tu bug de la saturación del servicio.</td></tr>
            <tr><td><b>Ocupación del contexto</b></td>
              <td>tokens por petición contra el límite</td>
              <td>Avisa antes de que empiecen los truncados silenciosos.</td></tr>
            <tr><td><b>Fallo por herramienta</b></td>
              <td>cuáles fallan y con qué frecuencia</td>
              <td>Casi siempre hay una que se lleva la mayoría.</td></tr>
            <tr><td><b>Iteraciones por bucle</b></td>
              <td>la distribución, no el promedio</td>
              <td>Un promedio de tres esconde el 2% que da veinte vueltas.</td></tr>
            <tr><td><b>Recuperación vacía</b></td>
              <td>consultas que no pasaron el umbral</td>
              <td>Si sube, el corpus o el troceado tienen un problema.</td></tr>
          </tbody>
        </table>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "El prompt es código",
        "note": "Y por tanto se versiona, se revisa y se revierte.",
    },

    {
        "kind": "content", "covers": [6, 7],
        "eyebrow": "Versionado y correlación",
        "title": "Poder responder «ayer funcionaba, ¿qué cambió?»",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Versionar el prompt</h3>
            <p>Vive en el repositorio, se revisa antes de entrar y tiene versión.</p>
            <p><b>Cada traza registra qué versión se usó</b>, así que puedes comparar
            el antes y el después con datos.</p>
            <p>Y se revierte igual que se revierte un despliegue.</p>
          </div>
          <div class="col">
            <h3>Correlacionar</h3>
            <p>Un identificador de traza que no se propaga no sirve: tiene que viajar
            a los servicios externos.</p>
            <p>Donde el proveedor acepte metadatos, mándalo: es lo que permite cruzar
            tus trazas con su facturación.</p>
            <p>Y con el de sesión y usuario, un reporte vago se vuelve diez trazas
            concretas.</p>
          </div>
        </div>
        <div class="box danger" style="margin-top:7mm">
          <p class="lab">El anti-patrón</p>
          <p>Editar el prompt en la interfaz web de una herramienta, sin control de
          versiones, en producción. <b>Es exactamente equivalente a editar código en
          el servidor por FTP.</b></p>
        </div>""",
    },

    # ── 05 ────────────────────────────────────────────────────────────────
    {
        "kind": "content", "covers": [8, 9],
        "eyebrow": "Lo que cuesta observar",
        "title": "Privacidad y muestreo",
        "html": """
        <div class="box danger">
          <p class="lab">Todo lo que va en el prompt termina en tus trazas</p>
          <p>Si inyectas datos de clientes, tu sistema de observabilidad acaba de
          convertirse en un repositorio de datos personales, con su propio control de
          acceso, su política de retención y su superficie de auditoría.</p>
        </div>
        <ul class="pts" style="margin-top:7mm">
          <li><b>La redacción ocurre antes de emitir la traza</b>, no como limpieza
            posterior.</li>
          <li><b>Muestrea con sesgo:</b> el 100% de los errores, el 100% de lo lento,
            y un porcentaje del resto. Guardar todo es caro sin aportar más.</li>
          <li><b>Emitir trazas nunca va en el camino crítico</b> de la respuesta al
            usuario.</li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [10],
        "eyebrow": "El panorama, por estilo y no por marca",
        "title": "Cómo se integra, que es lo que de verdad decides",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>En tu código</h3>
            <p>Con un SDK o decoradores dentro de tu propia lógica.</p>
            <p>Control fino y contexto semántico: sabe qué es una recuperación y qué
            es un paso de tu flujo.</p>
            <p>Cuesta tocar código.</p>
          </div>
          <div class="col">
            <h3>Interceptando</h3>
            <p>Un proxy o pasarela delante del proveedor.</p>
            <p>Se instala en minutos y no requiere cambios.</p>
            <p>Ve menos: registra llamadas, no tu lógica.</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p><b>La única recomendación de arquitectura que conviene dar:</b> emite en un
          formato estándar y mantén el backend intercambiable. Este espacio se mueve
          rápido y casarse con un proveedor envejece mal.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [11],
        "eyebrow": "Cierre",
        "title": "Si solo tienes un día para instrumentar",
        "html": """
        <div class="box big">
          <p>Por cada petición, registra: <b>el prompt final renderizado</b>, la
          respuesta completa, el modelo y su versión, los tokens de entrada y salida,
          la latencia, y —si hay recuperación— los documentos con sus puntajes.</p>
        </div>
        <ul class="pts" style="margin-top:7mm">
          <li>Todo amarrado con un identificador de traza y uno de sesión.</li>
          <li>Son un puñado de campos en una tabla, y ya resuelven la mayoría de las
            depuraciones.</li>
          <li>Lo demás se construye encima, cuando haga falta.</li>
        </ul>
        <div class="box danger" style="margin-top:6mm">
          <p>Este programa no cubre cómo <b>medir la calidad</b> de un sistema de AI.
          Una traza dice qué pasó, no si estuvo bien. Quien vaya a operar en
          producción va a necesitar eso además de esto.</p>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 16 · Observabilidad.",
        "rows": [
            ("2", "La frase del 200 OK es el eje. Dila antes de cualquier "
                  "definición."),
            ("6", "Contrasta los dos paneles despacio. Quien viene de software "
                  "tradicional necesita ver que sus herramientas de siempre no "
                  "sirven aquí."),
            ("10", "<b>Proyecta una traza real y desármala en pantalla.</b> Ver el "
                   "árbol convierte «¿por qué respondió esto?» en algo mecánico."),
            ("12", "El campo de los puntajes es el que más implementaciones caseras "
                   "olvidan. Insiste: sin él no puedes distinguir dos problemas con "
                   "soluciones opuestas."),
            ("16", "El promedio que miente convence mejor con la gráfica delante. "
                   "Pregunta cuál de las tres marcas les preocuparía más."),
            ("19", "El anti-patrón del prompt editado en producción sin versión suele "
                   "provocar risas incómodas. Es señal de que ha calado."),
            ("22", "Cierra con la ausencia declarada: medir la calidad es otro tema y "
                   "este programa no lo cubre. Mejor decirlo que dejar el hueco."),
        ],
    },
]
