import tkinter as tk

from functools import reduce
from operator import iconcat
from Funciones import matchPreference, read_csv


class MovieRecommendationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Recomendación de Películas")

        self.attributes_frame = tk.Frame(self.master)
        self.attributes_frame.pack()

        self.create_checkboxes()

        self.continue_button = tk.Button(
            self.master, text="Continuar", command=self.continue_clicked
        )
        self.continue_button.pack()

    def create_checkboxes(self):
        # Género
        self.genre_label = tk.Label(self.attributes_frame, text="Género:")
        self.genre_label.grid(row=0, column=0, sticky="w")
        self.genre_vars = []
        genres = [
            "Terror",
            "Acción",
            "Comedia",
            "Drama",
            "Ciencia Ficción",
            "Familiar",
            "Romance",
            "Fantasía",
            "Musical",
            "Animado",
            "Documental",
        ]
        for i, genre in enumerate(genres):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.attributes_frame, text=genre, variable=var)
            checkbox.grid(row=i // 3, column=i % 3 + 1, sticky="w")
            self.genre_vars.append(var)

        # Clasificación
        self.rating_label = tk.Label(self.attributes_frame, text="Clasificación:")
        self.rating_label.grid(row=4, column=0, sticky="w")
        self.rating_vars = []
        ratings = ["G", "PG", "PG-13", "R", "NC-17"]
        for i, rating in enumerate(ratings):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.attributes_frame, text=rating, variable=var)
            checkbox.grid(row=4, column=i + 1, sticky="w")
            self.rating_vars.append(var)

        # Premio
        self.awards_label = tk.Label(self.attributes_frame, text="Premio:")
        self.awards_label.grid(row=5, column=0, sticky="w")
        self.awards_vars = []
        awards = ["Globo", "Oscar", "Razzie"]
        for i, award in enumerate(awards):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.attributes_frame, text=award, variable=var)
            checkbox.grid(row=5, column=i + 1, sticky="w")
            self.awards_vars.append(var)

        # Productora
        self.producer_label = tk.Label(self.attributes_frame, text="Productora:")
        self.producer_label.grid(row=6, column=0, sticky="w")
        self.producer_vars = []
        producers = [
            "A24",
            "Paramount",
            "Columbia",
            "Universal",
            "Fox",
            "Sony",
            "Warner",
            "Walt Disney",
            "Dreamworks",
            "Marvel",
            "Pixar",
            "Lucasfilm",
            "Lionsgate",
        ]
        for i, producer in enumerate(producers):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(
                self.attributes_frame, text=producer, variable=var
            )
            checkbox.grid(row=6, column=i + 1, sticky="w")
            self.producer_vars.append(var)

        # Servicio de Streaming
        self.streaming_label = tk.Label(
            self.attributes_frame, text="Servicio de Streaming:"
        )
        self.streaming_label.grid(row=7, column=0, sticky="w")
        self.streaming_vars = []
        streamings = [
            "Netflix",
            "Disney",
            "HBO",
            "Paramount+",
            "Amazon",
            "Apple+",
            "Star",
            "Claro Video",
            "VIX",
        ]
        for i, streaming in enumerate(streamings):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(
                self.attributes_frame, text=streaming, variable=var
            )
            checkbox.grid(row=7, column=i + 1, sticky="w")
            self.streaming_vars.append(var)

        # Idioma Original
        self.language_label = tk.Label(self.attributes_frame, text="Idioma Original:")
        self.language_label.grid(row=8, column=0, sticky="w")
        self.language_vars = []
        languages = [
            "Español",
            "Inglés",
            "Francés",
            "Italiano",
            "Japonés",
            "Chino",
            "Coreano",
            "Indú",
            "Portugués",
            "Ruso",
        ]
        for i, language in enumerate(languages):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(
                self.attributes_frame, text=language, variable=var
            )
            checkbox.grid(row=8, column=i + 1, sticky="w")
            self.language_vars.append(var)

    def continue_clicked(self):
        selected_genres = [1 if var.get() == 1 else 0 for var in self.genre_vars]
        selected_ratings = [1 if var.get() == 1 else 0 for var in self.rating_vars]
        selected_awards = [1 if var.get() == 1 else 0 for var in self.awards_vars]
        selected_producers = [1 if var.get() == 1 else 0 for var in self.producer_vars]
        selected_streamings = [
            1 if var.get() == 1 else 0 for var in self.streaming_vars
        ]
        selected_languages = [1 if var.get() == 1 else 0 for var in self.language_vars]

        movie_info = {
            "Géneros": selected_genres,
            "Clasificaciones": selected_ratings,
            "Premios": selected_awards,
            "Productoras": selected_producers,
            "Servicios de Streaming": selected_streamings,
            "Idiomas": selected_languages,
        }

        self.show_movie_popup(movie_info)

    def show_movie_popup(self, movie_info):
        popup = tk.Toplevel(self.master)
        popup.title("Información de Película")

        usuario = reduce(iconcat, movie_info.values(), [])
        print(f"{usuario = }")
        base = read_csv("base-de-conocimiento.csv", "Pelicula")
        text = matchPreference(usuario, base)

        label = tk.Label(popup, text=text)
        label.pack()


def main():
    root = tk.Tk()
    app = MovieRecommendationApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
