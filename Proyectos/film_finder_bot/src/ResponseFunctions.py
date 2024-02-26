import os, time, string, random, re
from random import randrange
import json
from PyMovieDb import IMDB

class BaseDeDatos:
    def __init__(self) -> None:
        self.imdb = IMDB()
        #self.peliculas_list = re.findall('"id": "(tt\d{8})"', self.imdb.popular_movies())
        #self.serie_list = re.findall('"id": "(tt\d{8})"', self.imdb.popular_tv())

        self.peliculas_list = json.loads(self.imdb.popular_movies())
        self.peliculas_list = [id for (id, name, _, _, poster) in 
                               [dicc.values() for dicc in self.peliculas_list['results']]
                               if name != 'Lo que ignoramos' and poster != 'image_not_found']
        self.series_list = json.loads(self.imdb.popular_tv())
        self.series_list = [id for (id, name, _, _, poster) in 
                               [dicc.values() for dicc in self.series_list['results']]
                               if name != 'Fantasmas' and poster != 'image_not_found']

    def get_pelicula(self, otra=False):
        random_id = random.choice(self.peliculas_list)
        dicc = json.loads(self.imdb.get_by_id(random_id))

        if 'status' in dicc or not dicc['director']:
            self.peliculas_list.remove(random_id)
            return self.get_pelicula(otra)

        respuesta = {
            "False": [
                f"Por supuesto! Sabías que la pelicula '{dicc['name']}' salió en el año {dicc['datePublished']} y fue dirigida por {dicc['director'][0]['name']}",
                f"Claro, la pelicula es {dicc['name']}\n{dicc['poster']}"
            ],
            "True": [
                f"Otra pelicula que me gusta es '{dicc['name']}'",
            ]
        }

        return random.choice(respuesta[str(otra)])

    def get_serie(self, otra=False):
        random_id = random.choice(self.series_list)
        dicc = json.loads(self.imdb.get_by_id(random_id))

        if 'status' in dicc or not dicc['creator']:
            self.series_list.remove(random_id)
            return self.get_serie(otra)

        respuesta = {
            "False": [
                f"la fecha es {dicc['date']}" + f"lo creó {dicc['creator']}"
                f"Por supuesto! Sabías que la serie {dicc['name']} salió en el año {dicc['datePublished']} y fue creada por {dicc['creator'][0]['name']}",
                f"Claro, la serie es {dicc['name']}\n{dicc['poster']}"
            ],
            "True": [
                f"Otra serie que me gusta es '{dicc['name']}'",
            ]
        }

        return random.choice(respuesta[str(otra)])

def contar_chiste():
    '''
    Cuenta un chiste de forma aleatoria

    :return El chiste que se va a contar
    :rtype str
    '''
    chistes = [
        'Hay dos personas en un restaurante:\nX-Camarero, traigame una fanta de naranja\nM.-Lo siento señor, no nos queda Fanta, ¿Le va bien un Kas?\nX-Está bien.\nDespués de un rato, el camarero vulve con una fanta. ¿Cómo se llamó el videojuego? \nAl Final Fanta sí.\n', 
        '¿Cuál es el mejor juego de terror de la Wii?\n La Wiija. XD XD XD',
        'Se abre el telón y sale Leonardo Dantés muy constipado. ¿Como se llama el videojuego? Dantés Enfermo.',
        'Esto es una consola de Nintendo sin juegos de Mario. ¿Cómo se llama la película?: "Misión imposible"',
        'Esto es una encuesta de a ver que boss de FF es mas difícil y gana artemisa.'
    ]
    chiste = random.choice(chistes)
    return chiste

def despedida(user_input):
    '''
    Devuelve la despedida de glados

    :param str user_input: El texto escrito por el usuario
    :return La despedida de glados
    :rtype str
    '''
    des = user_input.split()
    despedida_usuario = ['salir', 'adios', 'bye', 'hasta luego', 'adiós']
    despedida_glados = ['Adiós', 'Bye!', '¡Hasta la vista, baby!']
    despedida_definitiva = ''
    for i in des:
        if i in des:
            despedida_definitiva = random.choice(despedida_glados)
    return despedida_definitiva
