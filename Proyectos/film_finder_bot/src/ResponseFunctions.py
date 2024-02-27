import random, re
import json
from PyMovieDb import IMDB


class BaseDeDatos:
    """
    Clase BaseDeDatos para manejar la manipulación de la API y sus funciones.
    Hay dos medios principales: peliculas y series.
    """

    def __init__(self) -> None:
        self.imdb = IMDB()
        self.tema = ""
        self.medio = {}

        self.peliculas_list = json.loads(self.imdb.popular_movies())
        self.peliculas_list = [
            id
            for (id, name, _, _, poster) in [
                dicc.values() for dicc in self.peliculas_list["results"]
            ]
            if name != "Lo que ignoramos" and poster != "image_not_found"
        ]
        self.series_list = json.loads(self.imdb.popular_tv())
        self.series_list = [
            id
            for (id, name, _, _, poster) in [
                dicc.values() for dicc in self.series_list["results"]
            ]
            if name != "Fantasmas" and poster != "image_not_found"
        ]

    def get_pelicula(self) -> str:
        """
        Devuelve la información de la película de acuerdo a la información
        de la API.

        :return Una respuesta con información acerca de la película
        """
        random_id = random.choice(self.peliculas_list)
        self.medio = json.loads(self.imdb.get_by_id(random_id))

        if "status" in self.medio or not self.medio["director"]:
            self.peliculas_list.remove(random_id)
            return self.get_pelicula()

        respuesta = [
            f"Por supuesto! ¿Sabías que la película {self.medio['name']} salió en "
            + f"la fecha {self.medio['datePublished']} y fue creada por {self.medio['director'][0]['name']}?",
            f"Claro, la película es '{self.medio['name']}' y tiene una calificación de {self.medio['rating']['ratingValue']}!\n{self.medio['poster']}",
        ]

        return random.choice(respuesta)

    def get_serie(self):
        """
        Devuelve la información de la serie de acuerdo a la información
        de la API.

        :return Una respuesta con información acerca de la serie
        """
        random_id = random.choice(self.series_list)
        self.medio = json.loads(self.imdb.get_by_id(random_id))

        if "status" in self.medio or not self.medio["creator"]:
            self.series_list.remove(random_id)
            return self.get_serie()

        respuesta = [
            f"Por supuesto! ¿Sabías que la serie {self.medio['name']} salió en "
            + f"la fecha {self.medio['datePublished']} y fue creada por {self.medio['creator'][0]['name']}?",
            f"Claro, la serie es '{self.medio['name']}' y tiene una calificación de {self.medio['rating']['ratingValue']}!\n{self.medio['poster']}",
        ]

        return random.choice(respuesta)

    def repite_info(self):
        """
        Devuelve la información del medio respectivo de acuerdo al contexto
        en el que se encontraba.

        :return Una respuesta con nueva informacion acerca del mismo contexto
        """
        medio_list = self.series_list if self.tema == "serie" else self.peliculas_list
        random_id = random.choice(medio_list)
        self.medio = json.loads(self.imdb.get_by_id(random_id))

        if (
            "status" in self.medio
            or not self.medio["creator"]
            or not self.medio["director"]
        ):
            medio_list.remove(random_id)
            return self.get_serie()

        respuesta = [
            f"Otra {self.tema} que me gusta es '{self.medio['name']}'",
        ]

        return random.choice(respuesta)

    def get_info(self, user_input):
        """
        Devuelve información específica que esté al alcance de la API.
        Las oraciones se pueden encadenar para obtener más información
        a la vez

        :return Una respuesta con informacion del medio.
        """
        regexes = [
            ".*(sali(o|ó)|estren(o|ó)|public(o|ó))",
            ".*(director|productor|creador).*",
            ".*genero.*",
            ".*califica.*",
        ]
        funciones = [
            self._get_fecha,
            self._get_director,
            self._get_generos,
            self._get_rating,
        ]
        prefijos = ["¡Por supuesto!", "¡Claro!", "¡De acuerdo!", "¡Seguro!", ""]

        respuestas = [
            funcion(user_input)
            for regex, funcion in zip(regexes, funciones)
            if re.match(regex, user_input)
        ]
        respuestas = [random.choice(respuesta) for respuesta in respuestas]

        respuesta = respuesta[0] if len(respuestas) == 0 else " y ".join(respuestas)
        return f"{random.choice(prefijos)}.{respuesta.capitalize()}"

    def _get_fecha(self, user_input):
        """
        Devuelve la fecha del medio, ya sea completa o los componentes de la misma.

        :return Una respuesta con información de la fecha del medio
        """
        self.medio["datePublished"]
        año, mes, dia = re.match("(\d*)-(\d*)-(\d*)", fecha).groups()

        if re.match("d(i|í)a|mes|año", user_input):
            meses = {
                "01": "Enero",
                "02": "Febrearo",
                "03": "Marzo",
                "04": "Abril",
                "05": "Mayo",
                "06": "Junio",
                "07": "Julio",
                "08": "Agosto",
                "09": "Septiembre",
                "10": "Octubre",
                "11": "Noviembre",
                "12": "Diciembre",
            }
            match re.match("d(i|í)a|mes|año", user_input).groups():
                case ("dia", _):
                    # en que día se estreno
                    return [
                        f"El {dia} de {meses[mes]}",
                        f"Se estrenó el {dia} de {meses[mes]}"
                        f"Un {dia} de {meses[mes]}"
                        f"Se estrenó un {dia} de {meses[mes]}",
                    ]
                case ("mes", _):
                    return [
                        f"En {meses[mes]} de {año}",
                        f"Se estrenó en {meses[mes]} de {año}"
                        f"Un mes de {meses[mes]} de {año}"
                        f"Se estrenó un mes de {meses[mes]} de {año}",
                    ]
                case ("año", _):
                    return [
                        f"En {año}",
                        f"En el año de {año}",
                        f"Se estrenó en el año de {año}",
                    ]
        else:
            fecha = f"el {dia} de {meses[mes]} del {año}"
            return [
                f"La {self.tema} se estrenó en {fecha}",
            ]

    def _get_director(self, user_input):
        """
        Devuelve a los directores o creadores del medio.

        :return Una respuesta con información acerca del director o creador del medio
        """
        director_list = (
            self.medio["director"] if self.tema == "pelicula" else self.medio["creator"]
        )

        directores = [name for (name, _) in [dicc.values() for dicc in director_list]]
        directores_str = (
            directores[0]
            if len(directores) == 1
            else " y ".join([", ".join(directores[:-1]), directores[-1]])
        )

        if len(directores) == 1:
            return [
                f"El director es {directores_str}",
                f"El creador es {directores_str}",
                f"El director de la {self.tema} es {directores_str}",
                f"El creador de la {self.tema} es {directores_str}",
            ]
        else:
            return [
                f"Los directores son {directores_str}",
                f"Los creadores son {directores_str}",
                f"Los directores de la {self.tema} son {directores_str}",
                f"Los creadores de la {self.tema} son {directores_str}",
            ]

    def _get_generos(self, user_input):
        """
        Devuelve los generos del medio.

        :return Una respuesta con información acerca de los generos del medio
        """
        generos = self.medio["genre"]
        generos_str = " y ".join([", ".join(generos[:-1]), generos[-1]])

        if len(generos) == 1:
            return [
                f"El genero es {generos_str}",
                f"El genero de la {self.tema} es {generos_str}",
            ]
        else:
            return [
                f"Los generos son {generos_str}",
                f"Los generos de la {self.tema} son {generos_str}",
            ]

    def _get_rating(self, user_input):
        """
        Devuelve las calificaciones del medio y la cantidad de calificaciones
        que tiene.

        :return Una respuesta con información acerca de las calificaciones del medio
        """
        rating = self.medio["rating"]
        if re.match(".*personas.*", user_input):
            rating = rating["ratingCount"]
            return [
                f"Al rededor de {rating} calificaron la {self.tema}",
                f"Hubo {rating} personas que calificaron la {self.tema}",
            ]
        elif re.match(".*tiene.*", user_input):
            rating = rating["ratingValue"]
            return [
                f"La {self.tema} tiene una calificación de {rating}",
                f"¡Tiene una calificación de {rating}!",
            ]


def despedida():
    """
    Devuelve la despedida de glados

    :param str user_input: El texto escrito por el usuario
    :return La despedida de glados
    :rtype str
    """
    despedidas = [
        "Hasta pronto!",
        "Hasta pronto! cinéfilo",
        "Nos vemos pronto!",
        "Nos vemos pronto! cinéfilo",
        "Adiós, fue un gusto!",
        "Vuelve cuando quieras!",
    ]
    return random.choice(despedidas)
