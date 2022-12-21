"""
En python disponemos de una serie de functiones generadores que van generando resultados a medida que los necesitamos
Por ejemplo si necesitamos ir obteniendo un listado de números de un rango elevado al cuadrado.
Si esa lista es muy larga y la generamos de golpe consumirá mucha memoria. Sin embargo, podemos ir generando los números
a nedida que los necesitamos
"""

## Ejemplo de una funcion normal en la que generamos un listado completo de un rango de numeros y lo devolvemos
def normal_function():
    list = []
    for n in range(1, 5):
        list.append(n*10)
    return list


## Ejemplo de function generadora con la palabra clave yield que irá generando guardando los números en memoria
## en el momento en el que lo necesitemos
def generator_function():
    for n in range(1, 5):
        yield n*10


generated_number = generator_function()
# print(normal_function())
# print(next(generated_number))
# print(next(generated_number))


## Creacion de funcion que va devolviendo un valor hasta el infinito
def generator():
    x = 0
    while True:
        x += 1
        yield x


generador = generator()

print(next(generador))
print(next(generador))


def decrease_life():
    for n in reversed(range(3)):
        yield f"Te quedan {n + 1} vidas"


perder_vida = decrease_life()

print(next(perder_vida))
print(next(perder_vida))

print(next(perder_vida))

