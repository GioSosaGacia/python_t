'''
Los generadores son funciones que retornan un valor conforme se va necesitando, ocupando menos espacio en la memoria, creando iteradores
con grandes volumenes, son eficientes en memoria ya que no puestran todos los datos de una solo vez si no que va produciendo los valores de uno
en uno.
Aumenta el rendimiento, simplicidad al escribir codigo mas limpio y conciso, iteracion peresoza o lazy iteration ya que va calculando los
datos de uno en uno a oferta demanda
En vez de usar return usamos yield para generar cado valor de manera individual
'''

def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_genredarador():
    for x in range(1,5):
        yield x * 10


print(mi_funcion())

#no muestra resultado asta que es requerido mediante el uso de next
print(mi_genredarador())
g = mi_genredarador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))



#Un generador no interumpe el codigo como el return , usando yield se puede seguir ejecutando el codigo asta que se le terminen los datos
def mi_generador1():
    x = 1
    yield x

    x += 1
    yield  x

    x += 1
    yield x

a = mi_generador1()
print(next(a))
print(next(a))
print('Hola yield')
print(next(a))


print('')
print('Ejercisios con yield'.center(50,'-'))

'''
Práctica Generadores 1
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, 
iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

Pista: Utiliza un loop while para realizar este ejercicio.'''

def generador():
    numero = 1
    while True:
        yield numero
        numero += 1

# Crear el generador
generador = generador()

print(next(generador))  # Devuelve 1
print(next(generador))

print('Practica 2'.center(50,'-'))
"""
Práctica Generadores 2
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, 
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).
"""


def generador1():
    for x in range(1, 10):
        yield x * 7


generador1 = generador1()
print(next(generador1))
print(next(generador1))
print(next(generador1))
print(next(generador1))


print('Practica 3'.center(50,'-'))
def perder_vida():
    vidas = 3
    while vidas > 0:
        if vidas > 1:
            yield f"Te quedan {vidas} vidas"
        else:
            yield "Te queda 1 vida"
        vidas -= 1
    yield "Game Over"

# Crear el generador
perder_vida = perder_vida()

# Ejemplo de uso:
print(next(perder_vida))  # Te quedan 3 vidas
print(next(perder_vida))  # Te quedan 2 vidas
print(next(perder_vida))  # Te queda 1 vida
print(next(perder_vida))  # Game Over
