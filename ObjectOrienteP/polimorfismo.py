'''
Polimorfismo muchos y forma
Objetos de diferentes clases pueden compartir el mismo nombre del metodo y puedes mandar a llamar el metodo desde el mismo lugar

Tipos de Polimorfismo
Hay principalmente dos tipos de polimorfismo:

Polimorfismo de tiempo de compilación (también llamado overloading o sobrecarga).
Polimorfismo de tiempo de ejecución (también llamado overriding o sobreescritura).

permite que métodos con el mismo nombre se comporten de manera diferente en clases diferentes.
El polimorfismo de tiempo de ejecución (overriding) es el más utilizado en Python, y permite que las
clases derivadas proporcionen su propia implementación de los métodos de la clase base.
'''

class Vaca:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice Muuu')


class Obeja:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice Beeee')

vaca1 = Vaca('juana')
obeja1 = Obeja('kATALINA')

#vaca1.hablar()
#obeja1.hablar()


animales = [vaca1,obeja1]

#El polomorfismo en una iteracion permite implementar el metodo de formas distintas a corde a su clase aunque sea el mismo metodo
for animal in animales:
    animal.hablar()





print('Practicas'.center(50,'-'))
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)



palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)


objetos = [palabra,lista,tupla]

for objeto in objetos:
    print(f'La longitud de {objeto} es: {len(objeto)}')



'''
Práctica Polimorfismo 2
Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() 
de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable 
(una lista llamada personajes) que pueda recorrese en dicho orden.
'''


class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


arquero = Arquero()
mago = Mago()
samurai = Samurai()
personajes = [arquero, mago, samurai]

for personaje in personajes:
    personaje.atacar()




'''
Práctica Polimorfismo 3
Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.

Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes),
 y ejecutar su método defender() independientemente de qué tipo de personaje se trate.
 '''


class Mago():
    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")


arquero = Arquero()
mago = Mago()
samurai = Samurai()


def personaje_defender(personaje):
    personaje.defender()


personaje_defender(mago)