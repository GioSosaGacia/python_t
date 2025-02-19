'''la oop esta basada en
Herencia, polimorfismo, cohesion, abstraccion, acoplamiento y encapsulamiento

Herencia: es la creacion de una clase hija que herda los atributos de la clase padre compartiendo sus metodos y atributos
class Pajaro(Animal):aplicando el DRY evitas declarar cada metodo en cada clase asi solo se crean en la clase padre y se hereda a los hijos

Una clase hija no necesariamnete hereda todo de la clase padre, ya que puede tener metodos heredados, metodos modificados y metodos nuevos

Herencia mUltiple: Herencia de dos clases o mas, cuando se hereda de mas de una clase los metodos pueden cambiar dependiendo de la clasde y debemos
analizar cual es el metodo que tomara de x clase si de la padre o de otra hija
'''

#Herencia en primera persona
class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal a nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        '''
        esta es una manera de trasncribir los atributos de la clase animal y otra usando super.__init__(edad,color)
        self.edad = edad
        self.color = color'''
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    #Ejecuto el metodo de su misma clase
    def hablar(self):
        print("Pio")

    #Metodos nuevos en los hijos que no existen en los padres
    def volar(self,metros):
        print(f'El pajaro vuela {metros} metros')



print("Herencia".center(50,'-'))
piolin = Pajaro(2,"amarillo",60)
print(piolin.color)
piolin.nacer()
piolin.hablar()
piolin.volar(50)


mi_animal = Animal(5,'negro')
mi_animal.hablar()




print("")
print("Gerarquia de herencia".center(50,'-'))
# Este atributo es útil cuando deseas inspeccionar la jerarquía de herencia de una clase y ver de qué otras clases hereda. __subclasses__()
print(Pajaro.__bases__)