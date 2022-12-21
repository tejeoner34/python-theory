## El manejo de errores se hace igual que en js, con un try catch


def suma():
    first = int(input('Enter number: '))
    second = int(input('Enter number: '))


try:
    suma()
except:
    print('You entered a wrong format')
finally:
    print('Se ejecuta siempre')
