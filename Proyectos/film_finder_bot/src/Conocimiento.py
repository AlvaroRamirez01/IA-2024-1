#----------------------------------------------------------------------
# Base de conocimiento
# La base de conocimiento representa una lista de todos los casos o intents.
#
# Cada caso o intent es un diccionario que incluye los siguientes keys (propiedades):
# - intent: Nombre para identificar el intent
# - regex: Lista de posibles expresiones regulares asociadas al intent, donde los parámetros se obtienen del texto parentizado en la expresión regular
# - respuesta: Lista de posibles respuestas al usuario, indicando los parámetros obtenidos con la notación %1, %2, %3, etc para cada parámetro
#----------------------------------------------------------------------
def conocimientoT():
    '''
    Define la base de conocimiento de glados

    :return El conicimiento a mostrar
    :rtype str 
    '''
    conocimiento = [
        #cada uno de estos es un cado de conocimieto 
        #////////////////////////////////////////////////Bienvenida.
        {
        
            #nombre de la intecion que se quiera
            'intent': 'bienvenida',
            # con mas de 1 expercion regugar par un caso particular 
            # la exprecion reguar va entre comillas simples 
            'regex': [
                r'.*hola.*',
                r'.*buen(a|o)s (dias|tardes|noches).*',
            ],
            #contine las posibles respuestas
            'respuesta': [
                '¡Hola Cinéfilo!, ¿de que quieres hablar hoy?',
                '¡Hola! ¿quieres conversar acerca de una película?',
            ]
        },
        #////////////////////////////////////////////////Chiste.
        {
            'intent': 'chiste',
            'regex': [
                r'.*chiste.*',
                r'.*broma.*'
            ],
            'respuesta': [
                'Bien',
                'Ahí te va'
            ]
        },
        #////////////////////////////////////////////////Chiste.
        {
            'intent': 'estado',
            'regex': [
                r'^.*me siento (.*)$',
            ],
            'respuesta': [
                'Por que te sientes %1'
            ]
        }, 
        #////////////////////////////////////////////////Fin.
        {
            'intent': 'terminar',
            'regex': [
                r'.*salir.*',
                r'.*adios.*',
                r'.*bye.*',
                r'.*hasta luego.*'
            ],
            'respuesta': [
                ''
            ]
        },
        
        #////////////////////////////////////////////////
        {
            'intent': 'genero',
            'regex': [
                r'.*(di|da)me un genero.*',
                r'.*(recomienda|sugiere)(|me) un genero.*',
                r'.*que genero prefieres.*',
            ],
            'respuesta': [
                'Aquí está un genero que te puede gustar: ',
                'El genéro que más me gusta es: ',
                'Este es el genero que te recomiendo: '
            ]
        },
        
        #////////////////////////////////////////////////
        {
        'intent': 'pelicula',
        'regex': [
        r'.*(di|da)me una pelicula.*',
        r'.*(que|cual) pelicula (me recomiendas|prefieres|te gusta).*',
        ],
        'respuesta': [
            'La pelicula que yo prefiero es: ',
            'Te recomiendo la pelicula: ',
            'Una elección de pelicula sería: '
        ]
        },
        #////////////////////////////////////////////////Cualquier caso no contemplado.
        {
            'intent': 'desconocido',
            'regex': [
                r'.*'
            ],
            'respuesta': [
                'Disculpa, yo solo hablo de peliculas y series.',
                'No conozco ninguna pelicula o serie con ese nombre.',
                'Creo que no tengo información al respecto; lo siento',
                'Disculpa, no comprendí lo que dices'
            ]
        }
        #////////////////////////////////////////////////
    ]
    return conocimiento