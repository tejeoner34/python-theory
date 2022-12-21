# COMO CREAR Y AÑADIR INFO EN UN ARCHIVO
# my_file = open('text_file.txt', 'w')
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# for element in registro_ultima_sesion:
#     my_file.write(element + '\n')
# my_file.close()


# COMO USAMOS LAS RUTAS
# Tenemos que importar el módulo de os
import os

# path = 'C:\\Users\\atzar\\projects\\learning\\python-proyects\\example_directory'
# ruta = os.getcwd()  # Obtenemos el current path
# os.chdir(path)  # Nos permite cambiar de directorio para modificar archivos en otros directorios
# os.makedirs(path + '\\my_directory')  # Crear directorios
# archivo = os.path.basename(path + '\\prueba.txt')  # Te da el nombre del archivo
# os.rmdir(path + '\\my_directory')  # Elimina directios

# Importante, para leer paths en cualquier sistema operativo tenemos que usar el modulo pathlib

from pathlib import Path

def fileContent(path):
    file = Path(path)
    if file.exists():
        return file.open().read()
    else:
        return 'Does not exist'


def over_write(path, value):
    file = Path(path)
    if file.exists():
        file.open('w').write(value)
        return file.open().read()
    else:
        return 'No content'


def add_content(path, value):
    file = Path(path)
    if file.exists():
        file.open('a').write(value)
        return file.read_text()
    else:
        return 'No content'


url = Path('C:/Users/atzar/projects/learning/python-proyects/example_directory/example.txt')

my_file = over_write(url, 'Overwritten')
print(my_file)
my_file = add_content(url, 'Added content')
print(my_file)
