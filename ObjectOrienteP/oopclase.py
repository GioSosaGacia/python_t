#El nombre de la clase va n mayuscula, declaramos una clase usando la palabra class
#Para crear un objeto creamos una variable = el nombre de la clase(argumentos)

'''
1-Hay atibutos de clase los cuales serán utilizados para todos los objetos de la misma
2-Atributos de la instancia que pertencen a cada objeto y cada objeto puede tener un valor distinto
2.1-Atributos de clase todos los objetos tienen el mismo valor
3-Cada que creamos un objeto las clase llama a su contructor para ver que requisitos o argumentos tiene o se necesita para ser creado un objeto
4-Parametro es lo mismo que una variable y un argumento es lo que almacena el parametro


decoradores
1-Metodos de instancia, son los comunes, acceden y modifican atributos del objeto, acceden a otros metodos y modifican el estado de la clase
2-metodos de clase, @classmethod en vez de self usa cls y esta asociado a la clase, no accedes a atributos de la instancia solo a los de clase
3-metodos staticos @staticmethod no acepta como parametro a self o cls, se usan para indicar que no se podra modificar el estado de la clase o de la instacia

'''

class Pajaro:
    #atributos de una clase son iguales para todos los objetos, __init__ es el metodo contructor, self es la intancia del objeto que se va a crear
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    #Metodos de instancia, cuando metodo invoca a un atributo necesitas relacionar a la instancia o objeto con self
    def piar(self):
        print('piopio, mi color es {}'.format(self.color))

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es de color: {self.color}')


    #metodos de clase relacionado a la clase, y no necesitan una instancia para poder ejecutarse, no puede acceder a los atributos de instancia
    #pero si a los de clase e incluso modificarlos
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)


    #Metodos estaticos no se refieren ni a la clase ni a la instancia, no usa self ni cls, sirve para evitar modificar a la instancio o la clase
    @staticmethod
    def mirar():
        print("El pajaro mira")


piolin = Pajaro('Amarillo','Canario')
piolin.pintar_negro()
print('Usando un metodo de instacia en otro'.center(50,'-'))
piolin.volar(50)
piolin.alas = False
print(f'Tengo alas? {piolin.alas}')
print('')


#crear una instancia de la clase pajaro
mi_pajaro = Pajaro('Negro','Tucan')
print(F'Tengo un oajaro de tipo {mi_pajaro.especie} y es de color {mi_pajaro.color}')#objeto
print(type(mi_pajaro))#tipo de mi objeto

otro_pajaro = Pajaro('Amarillo','Aguila')
print(otro_pajaro.color)


#Para acceder a un atributo de clase primero debemos de acceder a la misma
print('Accediendo a un atributo de clase'.center(50,'-'))
print(Pajaro.alas)
print('')


print('Probando metodos'.center(50,'-'))
print(mi_pajaro.alas)
piolin.piar()
piolin.volar(10)


print('Metodos de clase'.center(50,'-'))
Pajaro.poner_huevos(10)


print('Metodos de instancia'.center(50,'-'))
Pajaro.mirar()













print('Clase Alarma'.center(50,'-'))
class Alarma:
    def postergar(self,cantidad_minutos):
        print("La alarma ha sido pospuesta {} minutos".format(cantidad_minutos))

alarma1 = Alarma()
alarma1.postergar(10)


class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        # Cambia el valor del atributo de clase 'vivo' a True
        cls.vivo = True
        print(f"El jugador ha revivido: {cls.vivo}")


jugador1 = Jugador()
print("Estado inicial del jugador:", jugador1.vivo)  # Debería ser False
jugador1.revivir()
print("Estado después de revivir:", jugador1.vivo)  # Debería ser True


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        return self.cantidad_flechas - 1

personaje1 = Personaje(5)
print(personaje1.lanzar_flecha())
