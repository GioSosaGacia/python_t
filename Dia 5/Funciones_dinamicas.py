#Funciones dinamicas con loops, if, elif, else

def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(11)
print(resultado)

def checar_3(lista):

    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass  #Nota en el else no se usa return se uso pass para que siguera recorriendo la lista puede ir pero fuera del else en el for
    return lista_3_cifras

resultado1 = checar_3([555,2,34,343])
print(resultado1)





'''La función incorporada de Python all() sirve para verificar si todos los elementos de un iterable 
(como una lista, tupla o conjunto) cumplen con una condición específica o son "verdaderos" en un contexto booleano.
'''
def todos_positivos(lista):
    return all(num > 0 for num in lista)

lista_numeros = [5, -3, 7, 12, -1]






'''Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros)
 siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.'''
def suma_menores(lista):
    return sum(num for num in lista if 0 < num < 1000)
listar_numeros = suma_menores([1, 2,-2, 3, 4, 5, 454, 345])
print(listar_numeros)


#de esta manera paso el test pero ambos funcionan igual y dan el mismo resultado:
def suma_menores(lista):
    return sum(num for num in lista if 0 < num < 1000)
lista_numeros = [-1, 1, 2, 3, 4, 5, 454, 345]
resultado = suma_menores(lista_numeros)
print(resultado)









'''Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros),
 y devuelva el resultado de dicha cuenta.'''
def cantidad_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:
            contador += 1
    return contador

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = cantidad_pares(lista_numeros)
print(resultado)


def cantidad_pares(lista_numeros):
    """
    Cuenta la cantidad de números pares en una lista.
    :param lista_numeros: Lista de números
    :return: Cantidad de números pares en la lista
    """
    return sum(1 for num in lista_numeros if num % 2 == 0) #suma 1 cada que se cumple la condicion
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llamada a la función
resultado = cantidad_pares(lista_numeros)
print(resultado)  # Salida: 5








print('Ejemplos de función'.center(50,'-'))
print('')

#Desempacar tuplas
precio_cafe = [('Capuchino',1.5),('Expreso',2.2),('Moka',1.9)]

#for elemento in precio_cafe:  desempaquetando tuplas
    #print(elemento)

#Saber el precio mas alto
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precio_cafe)

print(f'El cafe más caro es: {cafe} cuyo precio es {precio}')