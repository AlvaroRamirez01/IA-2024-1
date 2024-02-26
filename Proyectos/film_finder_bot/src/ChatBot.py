#------------------------------------------------#
#  ChatBot.py                                     #
#------------------------------------------------#

import string, re, random, sys
from Conocimiento import conocimientoT
from ResponseFunctions import *

class ChatBot:
    """
    Clase ChatBot para simular una conversación 
    sobre videojuegos
    """ 
    contexto = "DEFAULT"
    entrada = ""

    def __init__(self):
        """
        ChatBot consta de una base de conocimiento
        representada como una lista de casos o intents.
        """ 
        self.conocimiento = [] 
        for caso in conocimiento:
            caso['regex'] = list(map(lambda x:re.compile(x, re.IGNORECASE), caso['regex']))
            self.conocimiento.append(caso)
        self.base = BaseDeDatos()

    def responder(self, user_input):
        '''
        Flujo básico para identificar coincidencias de intents para responder al usuario.
        Con el texto del usuario como parámetro, los paso a realizarse son:
        1. Encontrar el caso de la base de conocimiento usando expresiones regulares
        2. Si es necesario, realizar acciones asociadas al intent (por ejemplo: consultar información adicional)
        3. Seleccionar una respuesta de la lista de respuestas según el caso del intent
        4. Si es necesario, identificar los parámetros o entidades del texto para dar formato a la respuesta seleccionada
        5. Devolver la respuesta

        :param str user_input: El texto escrito por el usuario
        :return Un texto de respuesta al usuario
        :rtype: str
        '''
        caso = self.encontrar_intent(user_input)
        self.identifica_contexto(caso) 
        informacion_adicional = self.acciones(caso, user_input)
        respuesta = self.convertir_respuesta(random.choice(caso['respuesta']), caso, user_input)
        respuesta_final = (respuesta + '\n' + informacion_adicional).strip() 
        return respuesta_final

    def encontrar_intent(self, user_input):
        '''
        Encuentra el caso o intent asociado en la base de conocimiento

        :param str user_input: El texto escrito por el usuario
        :return El diccionario que representa el caso o intent deseado
        :rtype: str
        '''
        for caso in self.conocimiento:
            for regularexp in caso['regex']:
                match = regularexp.match(user_input)
                if match:
                    self.regexp_selected = regularexp 
                    return caso
        return {}

    def identifica_contexto(self, caso):
        '''
        Asegura que el contexto sea el adecuado para que
        ChatBot responde de manera coherente

        :param dict caso: El intent del cual se solicita información 
        '''
        intent = caso['intent']
        if intent == 'bienvenida':
            self.contexto = "BIENVENIDA"
        elif intent == 'pelicula':
            self.contexto = 'PELICULA'
        elif intent == 'repetirpelicula':
            self.contexto = 'PELICULA'
        elif intent == 'serie':
            self.contexto = 'SERIE'
        elif intent == 'repetirserie':
            self.contexto = 'SERIE'
        elif intent == 'chiste':
            self.contexto = "CHISTE"
        elif intent == 'desconocido':
            self.contexto = "DEFAULT"  

    def convertir_respuesta(self, respuesta, caso, user_input):
        '''
        Cambia los textos del tipo %1, %2, %3, etc., por su correspondiente propiedad
        identificada en los grupos parentizados de la expresión regular asociada.

        :param str respuesta: Una respuesta que desea convertirse
        :param dict caso: El caso o intent asociado a la respuesta
        :param str user_input: El texto escrito por el usuario
        :return La respuesta con el cambio de parámetros
        :rtype: str
        '''
        respuesta_cambiada = respuesta
        intent = caso['intent']
        match = self.regexp_selected.match(user_input)
        if intent == 'estado':
            respuesta_cambiada = respuesta_cambiada.replace('%1', match.group(1))
        return respuesta_cambiada

    def acciones(self, caso, user_input):
        '''
        Obtiene información adicional necesaria para dar una respuesta coherente al usuario.
        El tipo de acciones puede ser una consulta de información, revisar base de datos, generar
        un código, etc. y el resultado final es expresado como una cadena de texto

        :param dict caso: El caso o intent asociado a la respuesta
        :return Texto que representa información adicional para complementar la respuesta al usuario
        :rtype: str
        '''
        intent = caso['intent']
        if intent == 'chiste':
            return contar_chiste()
        elif intent == 'pelicula':
            return self.base.get_pelicula()
        elif intent == 'repetirpelicula':
            return self.da_respuesta_apropiada(user_input)
        elif intent == 'serie':
            return self.base.get_serie()
        elif intent == 'repetirserie':
            return self.da_respuesta_apropiada(user_input)
        elif intent == 'terminar':
            print(despedida(user_input))
            sys.exit(0)
        return ''


    def da_respuesta_apropiada(self, user_input):
        '''
        Devuelve la respuesta según el contexto en el que se encuentre

        :param str user_input: El texto escrito por el usuario
        :return Texto que representa la respuesta
        :rtype str
        '''
        if self.contexto == 'CHISTE':
            return 'Aquí va otro: ' + contar_chiste()
        elif self.contexto == 'PELICULA':
            return self.base.get_pelicula(otra=True)
        elif self.contexto == 'SERIE':
            return self.base.get_serie(otra=True)
        elif self.contexto == 'DEFAULT':
            return '¿Podrías tratar de expresarte mejor?'
        else:
            return '¿Podrías tratar de expresarte mejor?'

#---------------------------------------#
#  Base de conocimiento                 #
#---------------------------------------#
conocimiento = conocimientoT()


#---------------------------------------#
#  Interfaz de texto                    #
#---------------------------------------#
def chatBot():
    input_usuario = ''
    asistente = ChatBot()    
    while input_usuario != ' ':
        try:
            input_usuario = input('>> ')            
        except EOFError:
            print('Saliendo...')
            sys.exit(0)
        except KeyboardInterrupt: 
            print('Saliendo...')
            sys.exit(0)
        else:
            print(asistente.responder(input_usuario))

if __name__ == "__main__":
    chatBot()
