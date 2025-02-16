#Las listas van entre[] , se pueden anidar, van separados por coma, son mutables y podemos reorganizar su contenido
#contiene metodos con sort(), reverse(), append(), pop() son inplace que se modifican en la lista original

'''
La función sort() en Python ordena los elementos de una lista en el lugar, lo que significa que modifica la lista original.
No devuelve una nueva lista, sino que modifica la lista existente y retorna None.
'''
redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"]

# Usando el método sort()
resultado = redes.sort()

# Mostrar la lista después de ordenar

print(redes)
print(resultado)  # Esto imprimirá None

'''
Explicación:
La función sort() ordena los elementos de la lista redes en orden alfabético por defecto (en orden ascendente).
La lista original se modifica en el lugar y no se crea una nueva lista. Como sort() no devuelve nada, su valor de retorno es None.
'''


print("Diccionarios".center(50,'-'))
#Un diccionario es una colección de pares clave:valor, se asigna entre llaves{}, no tienen un indice ya que no son ordenados, se puede buscar valor en base a su clave,
#las claves no se pueden repetir pero los valores si,
diccionario = {"c1":"Valor1",'c2':'Valor2'}
print(type(diccionario))
print(diccionario)

#como consultar un dato: un diccionario puede alojar distimtos tipos de datos e incluso un lista, tupla u otro diccionario
resultado = diccionario['c1']
print(resultado)

cliente = {'Nombre':'Juan', 'Apellido':'Sosa', 'Peso':70, 'Edas':32, 'Talla':184.0}
consulta = cliente['Apellido']
print(consulta)

dic = {'c1':['a','e','d'],'c2':['q','z','x']}
print(dic['c2'][1].upper())

#agregar elementos a un diccionario:
dic1 = {1:'a',2:'b'}
print(dic1)

dic1[3] = 'c'
print(dic1)

#modivicar un valor de una clave
dic1[2] = 'B'
print(dic1)
print(dic1.keys())
print(dic1.values())
print(dic1.items())

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["pais"] = "Colombia"
mi_dic["edad"] = 36
print(mi_dic)





print('')
print("Tuplas".center(50,'-'))
#Tuplas son colecciones de elementos similar a las listas, solo que no son mutables y van entre () o sin parentesis,
#las tuplas ocupan menos espacio en memoria y se usa para datos fijos, pueden contener cualquier tipo de objetos,
#tambien se manejan mediante indices.
#Para poder modificar una tupla 1. la debemos de convertir en una lista se modifica y despues a la tupla
#sus metodos son index and count()

mi_tuple = (1,2,3,4,5,(10,2,3))
print(type(mi_tuple))
print(mi_tuple[5][1])

#asignarvalores de una tupla a variables: debe de ser estactos los valores y las variables si ahi mas o menos marcara error
t = (1,2,3)
x,y,z = t
print(x,y,z)
print(len(t))
print(t.count(1))
print(t.index(1))


print(" ")
print("set".center(50,"-"))

#Un set se declara usando la palabra clave set + los elementos entre parentesis y dentro de los parentesis agregar {} o [] para que los lea
# como un solo elemenrto ya que si solo lo escribes separado por , marcará error o declararlos entre {}
# en un set los elementos deben de ser unicos, no se repiten, si ahi mas de uno igual solo homite los que estan repetidos,
#no cuentan con un indice y no son inmutables ademas no permite agregar listas o diccionarios, solo tuplas, admite tuplas porque son inmutables

set1 = set([1,2,3,4,5,6])
print(set1)
print(type(set))

conjunto = {1,2,3,4,5,67,(4,5,6,7,3,4,6,8),6,6}
print(conjunto)
print(len(conjunto))
print( 2 in conjunto)
print(type(conjunto))

#Union de sets
s1 = {1,2,3}
s1.add(6)
s2 = {3,4,5}
s3 = s1.union(s2)
s3.remove(6) #si no existe marca error
s3.discard(6)#si no existe no marcará error ya que lo descarta
s3.pop()#si dejamos vacion la funcion elimina un dato de manera aleatoria
print(s3)




print(" ")
print("booleanos".center(50,"-"))

#Un bool solo contiene True or False
#se pueden declarar de manera indirecta mediante el uso de operadores logicos < > == != <= >=
#Los bool son una base para la IA

var1 = True
var2 = False
print(type(var1))

lista = [1,2,3,4,5]
control = 5 in lista
print(type(control))
print(control)