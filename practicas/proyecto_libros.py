"""Este es un proyecto para tener una idea sobre como leer los libros y su duracion"""


def analizar_libro(pag):
    paginas_año = pag / 365
    resultado = print(f"Débes leer {round(paginas_año,1)} páginas por día durante un año para completarlo")
    return resultado

numero_paginas = int(input("Cuantas páginas tiene el libro ? "))

analizar_libro(numero_paginas)