"""Este script lee y procesa archivos PDF usando PyPDF2.
"""
import os
from PyPDF2 import PdfReader

# Construir la ruta de forma segura
carpeta = 'Automatizar-docs/archivos'
archivo_pdf = 'cv.pdf'
ruta_completa = os.path.join(carpeta, archivo_pdf)

# Abrir el archivo PDF
with open(ruta_completa, 'rb') as archivo:
    lector = PdfReader(archivo)
    # Obtener el número de páginas
    num_paginas = len(lector.pages)
    print(f'Número de páginas: {num_paginas}')

    # Extraer texto de la primera página
    pagina = lector.pages[0]
    print(pagina)