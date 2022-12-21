## Creación de clases

class Bird:

    ## Es como el constructor de js y self es el this
    def __init__(self, color):
        self.color = color

    ## En todas las funciones tenemos que pasarle el self
    def fly(self, meters):
        print(f'Ha volado {meters} metros')


## Al igual que en js tenemos herencia de otras clases

class Animal:
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad


class Perro(Animal):
    pass


my_dog = Perro('Brown', 2);

## Las clases tienen tambien una serie de metodos especiales:

class Cd:
    def __init__(self, title, author, songs):
            self.title = title
            self.author = author
            self.songs = songs

    ## Este metodo nos sirve para especificar la longitud de algun dato de la clase
    def __len__(self):
        print(f"There are {self.songs} songs")


    ## Este metodo especial nos sirve por ejemplo para definir la clase
    def __str__(self):
        print(f"This is the album: {self.title}")


    ## Este metodo se ejecutara cuando eliminemos la instancia de esta clase
    def __del__(self):
        print(f"The album {self.title} was deleted")


my_cd = Cd('Breaking free', 'Queen', 13)
## Con este metodo eliminamos la instancia
del my_cd
