"""
Más formas de tratar archivos y carpetas en python
"""

import os
import shutil

##Con shutil podemos hacer cosas como mover archivos de un directorio a otro
##Para eliminar archivos y directorios tenemos algunas opciones en el modulo os
## Tambien tenemos un modulo externo, send2trash que dispone de funciones para eliminar

import send2trash

send2trash.send2trash('nombre de archivo a eliminar')

## Un metodo interesante para recorrer todas las carpetas y archivos dentro de una ruta es el metodo walk de os

for route, dirs, files in os.walk("C:\\Users\\atzar\\OneDrive\\Escritorio\\practice"):
    print(f"En la ruta {route}")
    print('Las carpetas son: ')
    for dir in dirs:
        print(f"{dir}\n")
    print('Los archivos: ')
    for file in files:
        print(f"\t{file}")