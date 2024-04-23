import csv
import numpy as np


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


def obtenerDF(conocimiento):
    return 0


def obtenerIDF(df, conocimiento):
    return 0


def normalizar(conocimiento, total):
    return conocimiento


def matchUserInput(preferencia, c):
    pref = []
    for text in c:
        found = False
        for r in preferencia:
            if r.strip().lower() == text.strip().lower():
                # print("MATCH:", r)
                pref.append(1)
                found = True
                break
        if not found:
            pref.append(0)
    return pref


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


base = read_csv("base-de-conocimiento.csv", "Pelicula")
usuarios = read_csv("usuarios.csv", "Usuario")
