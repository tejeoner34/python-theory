from random import randint

# alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
#
# for alumno in alumnos_clase:
#     print(f"Hola {alumno}")


# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# suma_pares = 0
# suma_impares = 0
#
# for number in lista_numeros:
#     if number%2 == 0:
#         suma_pares += number
#     else:
#         suma_impares += number
#
# print(suma_impares, suma_pares)

# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#
# for index, nombre in enumerate(lista_nombres):
#     print(f'{nombre} se encuentra en el índice {index}')

# var = "Python"
#
# for tuple in enumerate(var):
#     print(tuple)

# METODO zip
# capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
# paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
#
# combination = list(zip(capitales, paises))
#
# for capital, pais in combination:
#     print(f"La capital de {capital} es {pais}")

# Práctica 4

max_oppor = 4
num_oppor = 0
answer = randint(0, 100)
print(answer)
while num_oppor <= max_oppor:
    user_answer = int(input('Introduce un número: '))

    if user_answer > 100 or user_answer < 0:
        print('el número no puede estar fuera del rango')
    else:
        if user_answer == answer:
            print('correcto!')
            break
        elif user_answer > answer:
            print('es mayor')
            num_oppor += 1
        else:
            print('es menor')
            num_oppor += 1

        if num_oppor > max_oppor:
            print('Has perdido')

