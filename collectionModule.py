"""
El modulo de collection ayuda a manipular de forma más sencilla ciertos tipos de datos
"""

## Con namedTuple podemos crear un tuple dandole nombre a sus elementos (podemos acceder a sus elementos
## tanto como si de un array se tratase por su indice como por el nombre que le asignamos al elemento
## como si de un objeto se tratase
from collections import namedtuple

Person = namedtuple('Person', ['name', 'height', 'weight'])
john = Person('John', 80, 180)

print(john.weight)



## Cuando tenemos un dictionary y tratamos de acceder a una propiedad que no existe, nos salta error.
## Con defaultDict podemos evitar este error y definir que nos devuelva lo que digamos
from collections import defaultdict

my_dic = defaultdict(lambda: None)
my_dic['first'] = 'first'

print(my_dic['first'])
print(my_dic['no_exist'])



## Con Counter podemos pasarle una list o string y nos devuelve un objeto con los elementos y numero de
## repeticiones
from collections import Counter

example_list = [1,1,1,1,2,2,2,3,3]
my_counter = Counter(example_list)
print(my_counter)