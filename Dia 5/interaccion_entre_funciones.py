
#interaccion entre funciones  una funcion a retorna un valor ver
from random import shuffle

#lista inicial
palitos = ['-','--','---','----']

#mezclar palitos usando el metodo shuffle importado de randon
#shuffle(palitos) #shuffle no retorna nada asi que no lo podemos asignar a una variable
def mezclar(lista):
    shuffle(lista)
    return lista

#linea solo para comprobar que funcione --> print(mezclar(palitos))

#pedirle iuntento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 - 4: ")
    return  int(intento)

#probar la funcion
#intento1 = probar_suerte()
#print(intento1)

#comprobar intento
def checar_intento(lista,intento):
    if lista[intento -1] == '-':
        print("A LAVAR LOS PLATOS!!")
    else:
        print("Te has salvado!!")
    print(f"Te ha tocado {lista[intento-1]}")

#ejecucion de las fucniones
#palitos_mezclados = mezclar(palitos)
#seleccion = probar_suerte()
#checar_intento(palitos_mezclados,seleccion)








#Practica 1:
'''
Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
(es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- 
un mensaje según la suma de estos valores:
'''
from random import randint
#randint recibe 2 parametros, donde inicia y en donde termina
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1, dado2

resultado = lanzar_dados()
print(resultado)

def evaluar_jugada(dado1,dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return  f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

#resultado_dados = lanzar_dados()
#mensaje = evaluar_jugada(*resultado_dados)
#print(mensaje)







#Practica 2
lista_numeros = [1,2,15,7,2]
def reducir_lista(lista):
    lista = list(set(lista))
    return lista

#validamos que funcione la lista
#lista_numeros = reducir_lista(lista_numeros)
#print(lista_numeros)

def promedio(lista):
    if len(lista) > 0:
        return sum(lista) / len(lista)
    else:
        return 0

lista_numeros = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_numeros)

print(f"Lista sin duplicados: {lista_numeros}")
print(f"Promedio de la lista sin duplicados: {resultado_promedio}")




#RESULTADO CORRECTO REMUVIENDO EL CAMPO MAS ALTO
'''Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), 
y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el
 valor más alto. El orden de los elementos puede modificarse.
Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que 
calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
'''


def reducir_lista(lista):
    # Eliminar duplicados usando set y luego convertirlo nuevamente a lista
    lista_sin_duplicados = list(set(lista))

    # Eliminar el valor más alto
    lista_sin_duplicados.remove(max(lista_sin_duplicados))
    return lista_sin_duplicados


def promedio(lista):
    # Calcular el promedio de la lista
    if len(lista) > 0:  # Verificar si la lista no está vacía
        return sum(lista) / len(lista)
    else:
        return 0  # Si la lista está vacía, el promedio es 0


# Ejemplo de uso
lista_numeros = [1, 2, 15, 7, 2]

# Reducir la lista
lista_reducida = reducir_lista(lista_numeros)

# Calcular el promedio de la lista reducida
resultado_promedio = promedio(lista_reducida)

# Imprimir resultados
print(f"Lista reducida: {lista_reducida}")
print(f"Promedio de la lista reducida: {round(resultado_promedio,2)}")






#Practica 3
'''
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe 
poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del 
lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores 
y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla 
(devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
'''

import random

def lanzar_moneda():
    # Elegir al azar entre "Cara" o "Cruz" random.choice(): Esta función selecciona al azar un valor de la lista
    # proporcionada. En este caso, la lista ["Cara", "Cruz"] contiene los dos posibles resultados.
    return random.choice(["Cara", "Cruz"])

# Ejemplo de uso
#resultado = lanzar_moneda()
#print(resultado)

def probar_suerte(moneda,lista):
    if moneda == "Cara":
        print(f"La lista se autodestruirá te toco: '{moneda}'")
        lista.clear()
        return lista
    else:
        print(f"La lista fue salvada te toco: '{moneda}'")
        return lista

lista_numeros = [1, 2, 15, 7, 2]

resultado = lanzar_moneda()
intento = probar_suerte(resultado,lista_numeros)
print(intento)
