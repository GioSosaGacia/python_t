for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

#como iterar un diccionario:
#.items() imprime la clave y el valor de un diccionario

dic = {'clave1':'a','clave2':'b','clave3':'c'}

for diccionario in dic.items():
    print(diccionario)

for a,b in dic.items():
    print(a,b)




lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for suma in lista_numeros:
    suma_numeros = suma_numeros + suma
    print(suma_numeros)

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num

print(suma_pares)
print(suma_impares)





print('while'.center(50,'-'))
#While se repite un fragmento de codigo miestras se cumpla una condición una vez cumplida se finaliza.
#Estas palabras reservadas se utilizan dentro de los loops
#break = interumpe la interaccion actual para salir corta el loop
#continue = continuar no corta el loop si no que vuelve al inicio y continua con la siguiente iteración
#pass == pasar no hacer nada.

moneda = 5

while moneda  > 0:
    print(f'Tengo {moneda} monedas')
    moneda -= 1
else:
    print('Ya no tengo monedas...')


#break  termina en fede and continue imprime federico sin la r
'''nombre = input('Tu nombre: ')

for letra in nombre:
    if letra == "r":
        continue
    print(letra)
'''

#loop while 2
numero = 50

while numero >= 0:
    if numero %5 == 0:
        print(numero)
    numero -= 1


#interuccion de flujo al encontrar un valor negativo
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for lista in lista_numeros:
    if lista == -1:
        break
    print(lista)






print(' ')
print('rango'.center(50,'-'))
#Un rango es una función que permite crear establecer un rango de nuemeros sin necesidad de crear una lista o una variable
#Rango recibe 3 parameteos: 1.Desde que numero inicia, 2,donde terminará si agregar el ultimo valor y 3.el incremento si es de dos en dos etc

#crear una lista con un rango:  lista = list(range(1,101))

#Usando range
for numero in range(1,20):
    print(numero)


#suma de cuadrados
suma_cuadrados = 0

for numero in range(1,16):
    cuadrado = numero**2
    suma_cuadrados += cuadrado
    print(suma_cuadrados)







print('')
print("Enumerate".center(50,'-'))
#Enumerate su funcion nos permite acceder al indice de una colección de datos: lista, tupla, etc.

lista = ['a','b','b']
indice = 0

#sin enumerate
for item in lista:
    print(indice, item)
    indice += 1


#con enumerate crea una serie de tuplas con el indice y el elemento
#for indice, elememt in enumerate(lista):
#   print(indice,elememt) de esta manera podemos ver el indice y elemento fuera de una tupla al utilizar enumerate
for elememt in enumerate(lista):
    print(elememt)

mi_tuples = list(enumerate(lista))
print(mi_tuples)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


'''
Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() 
los índices de cada caracter del string "Python".
Llama a la lista obtenida con el nombre de variable lista_indices .'''

lista_indices = list(enumerate("Python"))
for elemento in lista_indices:
    print(elemento)



'''
Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

Loops
Condicionales if
El método enumerate()
Métodos de strings o indexado
'''
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)






print('')
print('Zip'.center(50,'-'))
#En Python, la función incorporada zip() permite combinar elementos de múltiples iterables (como listas, tuplas, etc.)

nombres = ['Giovanni','Aneliz','Luis','Maria']
edades = [32,39,23,27]

#Para usar zip debemos de castear a una lista o tupla. etc y si una lista tiene mas datos que la otra zip se queda con la lista
#mas corta
comninaciones = list(zip(nombres,edades))

for nombre,edad in comninaciones:
    print(f'{nombre} tiene {edad} años')


espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espanol, portugues, ingles))

print(numeros)


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = 0

ultimo_nombre = ''

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima)
print(ultimo_nombre)
