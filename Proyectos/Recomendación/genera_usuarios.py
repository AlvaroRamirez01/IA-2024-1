import csv
import random
import sys


def preferencia(num_peliculas):
    """Genera una lista con las preferencias del usuari

    Parametros:
    num_peliculas: el número de peliculas para usar
    """

    # A cada valor se le asigna una probabilidad de que aparezca
    valores = {-1: 0.1, 0: 0.5, 1: 0.3}

    return [
        random.choices(list(valores.keys()), weights=list(valores.values()))[0]
        for _ in range(num_peliculas)
    ]


def main():
    if len(sys.argv) != 2:
        print(f"uso: python {sys.argv[0]} <numero de usuarios>")

    with open("base-de-conocimiento.csv", "r") as file:
        # Obtiene las peliculas de nuestra base de conocimientos
        peliculas = [linea.split(",")[0] for linea in file.readlines()[1:]]

        # numero de usuarios que usaremos
        num_usuarios = int(sys.argv[1])

        # Por cada usuario, crea una lista con las preferencias al azar de cada uno
        tabla = [preferencia(len(peliculas)) for _ in range(num_usuarios)]

        # Crea el archivo csv con las preferencias de los usuarios
        with open("usuarios.csv", "w") as file:
            csv_writer = csv.writer(file)

            peliculas.insert(0, "Usuario")
            csv_writer.writerow(peliculas)

            tabla = [[f"Usuario {i + 1}"] + fila for i, fila in enumerate(tabla)]
            csv_writer.writerows(tabla)


main()
