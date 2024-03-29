# ----------------------------------------------------------------------
# Base de conocimiento
# La base de conocimiento representa una lista de todos los casos o intents.
#
# Cada caso o intent es un diccionario que incluye los siguientes keys (propiedades):
# - intent: Nombre para identificar el intent
# - regex: Lista de posibles expresiones regulares asociadas al intent, donde los parámetros se obtienen del texto parentizado en la expresión regular
# - respuesta: Lista de posibles respuestas al usuario, indicando los parámetros obtenidos con la notación %1, %2, %3, etc para cada parámetro
# ----------------------------------------------------------------------
def conocimientoT():
    """
    Define la base de conocimiento de glados

    :return El conicimiento a mostrar
    :rtype str
    """
    conocimiento = [
        # ////////////////////////////////////////////////Bienvenida.
        {
            "intent": "bienvenida",
            "regex": [
                r".*hola.*",
                r".*buen(a|o)s (d(i|í)as|tardes|noches).*",
            ],
            "respuesta": [
                "¡Hola Cinéfilo!, ¿de que quieres hablar hoy?",
                "¡Hola! ¿quieres conversar acerca de una película o serie?",
            ],
        },
        # ////////////////////////////////////////////////Fin.
        {
            "intent": "terminar",
            "regex": [r".*salir.*", r".*adios.*", r".*bye.*", r".*hasta luego.*"],
            "respuesta": [""],
        },
        # //////////////////////////////////////////////// pelicula
        {
            "intent": "pelicula",
            "regex": [
                r".*(di|da)me una pel(i|í)cula.*",
                r".*(que|cual) pel(i|í)cula (me recomiendas|prefieres|te gusta).*",
                r".*habla(me)? de una pel(i|í)cula.*",
                r".*(recomienda|muestra)(me)? una pel(i|í)cula.*",
            ],
            "respuesta": [
                "",
            ],
        },
        # //////////////////////////////////////////////// serie
        {
            "intent": "serie",
            "regex": [
                r".*(di|da)me una serie.*",
                r".*(que|cual) serie (me recomiendas|prefieres|te gusta).*",
                r".*habla(me)? de una serie.*",
                r".*(recomienda|muestra)(me)? una serie.*",
            ],
            "respuesta": [
                "",
            ],
        },
        # //////////////////////////////////////////////// repeticion
        {
            "intent": "repetir",
            "regex": [
                r".*qu(e|é) tal otra( \w*)?.*",
                r".*(di|da)me otra( \w*)?.*",
                r".*(que|cual) otra( \w*)? (me recomiendas|prefieres|te gusta).*",
                r".*habla(me)? de otra( \w*)?.*",
                r".*(recomienda|muestra)(me)? otra( \w*)?.*",
                r".*me (recomienda|muestra)(s)? otra( \w*)?.*",
            ],
            "respuesta": [
                "",
            ],
        },
        # //////////////////////////////////////////////// pregunta
        {
            "intent": "pregunta",
            "regex": [
                r".*cu(a|á)ndo (sali(o|ó)| se (estren(o|ó)|public(o|ó))).*",
                r".*en (qu(e|é)|cu(a|á)l) (d(i|í)a|mes|año)( sali(o|ó)| se (estren(o|ó)|public(o|ó)))?.*",
                r".*(cu(a|á)l|qui(e|é)n) (fue|es) el (director|creador).*",
                r".*cu(a|á)les son los generos.*",
                r".*de que generos? (son|es).*",
                r".*(cu(a|á)ntas|qu(e|é) cantidad de) personas lo calificaron.*",
                r".*(cu(a|á)nta|qu(e|é)) calificaci(o|ó)n (tiene|tuvo).*",
            ],
            "respuesta": [
                "",
            ],
        },
        # ////////////////////////////////////////////////Cualquier caso no contemplado.
        {
            "intent": "desconocido",
            "regex": [r".*"],
            "respuesta": [
                "Disculpa, yo solo hablo de peliculas y series.",
                "No conozco ninguna pelicula o serie con ese nombre.",
                "Creo que no tengo información al respecto; lo siento",
                "Disculpa, no comprendí lo que dices",
            ],
        },
    ]
    return conocimiento
