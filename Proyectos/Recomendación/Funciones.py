import csv
import numpy as np
import random

from itertools import islice


def read_csv(archivo: str, columna: str):
    """
    Funcion que leer una base de conocimiento y la transforma en un diccionario.
    El diccionario tiene una lista con los campos, el nombre de las peliculas y
    una matriz con los datos
    """

    with open(archivo, "r") as file:
        reader = csv.DictReader(file)
        datos = [fila for fila in reader]

        return {
            "campos": reader.fieldnames,
            "nombres": [fila[columna] for fila in datos],
            "datos": np.array(
                [list(list(fila.values())[1:]) for fila in datos], dtype=int
            ),
        }


def normalizar(conocimiento):
    return [[campo / np.sqrt(sum(fila)) for campo in fila] for fila in conocimiento]


def recomendacion_contenido(conocimiento, usuario, n=10):
    datos, nombres = conocimiento["datos"], conocimiento["nombres"]
    normalizada = np.array(normalizar(datos))
    interes = [normalizada[:, i] @ usuario for i in range(normalizada.shape[1])]
    df = [sum(datos[:, i]) for i in range(datos.shape[1])]
    idf = [np.log10(datos.shape[0] / n) if n != 0 else 0 for n in df]
    predicciones = ((fila * idf) @ interes for fila in normalizada)
    predicciones = (
        (i, pred, u) for (i, pred), u in zip(enumerate(predicciones), usuario) if u == 0
    )
    predicciones = sorted(predicciones, key=lambda t: t[1], reverse=True)
    predicciones = (nombres[prediccion] for prediccion, _, _ in predicciones)

    return list(islice(predicciones, n))


# Calcular el angulo minimo entre el input, y la base de conocimiento
def matchPreference(preferencia, conocimiento):
    def angulo(v1, v2):
        def unit_vec(v):
            return v / np.linalg.norm(v)

        v1 = unit_vec(v1)
        v2 = unit_vec(v2)
        return np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0))

    recomendado = [angulo(preferencia, fila) for fila in conocimiento["datos"]]
    return conocimiento["nombres"][np.argmin(recomendado)]


def main():
    base_completa = read_csv("base-de-conocimiento.csv", "Pelicula")
    base_reducida = read_csv("base-de-conocimiento-reducida.csv", "Pelicula")
    usuarios = read_csv("usuarios.csv", "Usuario")
    usuario = random.choice(usuarios["datos"])
    # Usuario usado en el documento
    # usuario = np.array(
    #     [ 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, -1, 0, 1, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 1, -1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, -1, 0, -1, 1, 0, -1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, -1, 1, -1, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 1, -1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 1, -1, 1, 0, 1, 0, 0, -1, 1, 0, 1, 0, -1, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 1, 1, ]
    # )
    print(f"base completa: {recomendacion_contenido(base_completa, usuario)}")
    print(f"base reducida: {recomendacion_contenido(base_reducida, usuario)}")


main()
