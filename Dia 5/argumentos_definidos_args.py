#*args = argumentos indefinidos, permite usar mas de dos argumentos o que el numero de parametros que acepte sea variable
#**kwargs =

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total
#return sum(args) Tambien solo puede funcioanr con esta linea y borrar el for y la variable total

print(suma(5,5,5,9,7,4,7,9,6))


#Ejemplos Practicos:
def suma_cuadrados(*args):
    return sum(arg**2 for arg in args)

resultado = suma_cuadrados(1,2,3)
print(resultado)



'''
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la
 suma de sus valores al cuadrado.
Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
'''
def suma_cuadrados(*args):
    suma = 0
    for x in args:
        suma += x**2
    return suma

print(suma_cuadrados(1,2,3))





'''
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma
 de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a 
 todos -negativos y positivos- como positivos).
 
 absoluto = apesar de que un numero sea negativo siempre lo hace positivo como el -8 sera = 8 usando la funcion abs()
 el cual quiere decir absoluto
 
 El valor absoluto de un número es su distancia desde el cero en la recta numérica, sin importar su signo.
  En otras palabras, el valor absoluto de un número siempre es positivo o cero.
'''
def suma_absolutos(*args):
    return sum(abs(x) for x in args) #comprehesion de listas

resultado = suma_absolutos(2,-3,5,-6,-9,9)
print(resultado)



'''Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, 
una cantidad indefinida de números. La función debe devolver el siguiente mensaje:
"{nombre}, la suma de tus números es {suma_numeros}"
'''
def numeros_persona(nombre,*args):
    return f"{nombre}, la suma de tus números es {sum(x for x in args)}"

resultado = numeros_persona('Giovanni',2,2,2,2,2)
print(resultado)




print('')
print('Funciones con el uso de **kwargs'.center(50,'-'))
#**kwars se usa para crear un diccionario con n cantidad de argumentos variables
def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total
print(suma(x=3, y=4, z=5))



'''Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan,
 y devuelva esa cantidad como resultado.'''
def cantidad_atributos(**kwargs):
    return len(kwargs)

print(cantidad_atributos(x=1,y=""))



'''
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en 
forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
'''
def lista_atributos(**kwargs):
    return list(kwargs.values())

resultado = lista_atributos(nombre="Juan", edad=25, ciudad="Madrid")
print(resultado)  # Salida: ['Juan', 25, 'Madrid']






'''
Este me marco error en el sistema solo era quitar la ultima linea que manda a llamar la funcion
'''
def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for c,v in kwargs.items():
        print(f"{c}: {v}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")




print('')
print('Ejercisio Practico'.center(50,'-'))
#la funcion max siempre espera un iterable y no solo un entero si coloco max(suma)marcara error ya que es un solo valor y no varios
#para ser un iterable
def devolver_distintos(a,b,c):
    sumar = a + b + c
    if sumar > 15:
        print(f'mayor a 15 y el numero mayor es: {max(a,b,c)}')
    elif sumar < 10:
        print(f'Menor a 10 y el valor más pequeño es: {min(a,b,c)}')
    else:
        numeros = [a, b, c]
        numeros.sort()
        mediano = numeros[1]
        print(f'La suma de los 3 números es un valor entre 10 y 15. El número mediano es: {mediano}')

devolver_distintos(1,5,3)

#oyto ejemplo:
def devolver_distintos(a, b, c):
    sumar = a + b + c

    if sumar > 15:
        return f'Mayor a 15 y el número mayor es: {max(a, b, c)}'
    elif sumar < 10:
        return f'Menor a 10 y el valor más pequeño es: {min(a, b, c)}'
    else:
        mediano = sorted([a, b, c])[1]  # Encuentra el mediano
        return f'La suma de los 3 números es un valor entre 10 y 15. El número mediano es: {mediano}'

# Ejemplo de uso:
#print(devolver_distintos(3, 5, 8))  # Mayor a 15
#print(devolver_distintos(1, 2, 3))  # Menor a 10
#print(devolver_distintos(4, 4, 5))  # Entre 10 y 15




print('Ejercisio Practico 2'.center(50,'-'))

def palabreria(word):
    letras_unicas = sorted(set(word)) #set elimina las letras repetidas, sorted las ordena y join las une
    #Las comillas antes de .join() se utilizan para especificar el separador que se colocará entre los elementos al unirlos en una cadena.
    return ','.join(letras_unicas)

resultado = palabreria('entretenido')
print(resultado)







print('Ejercisio Practico 3'.center(50,'-'))
def doblecero(*args):
    if args.count(0) == 2:
        print(True)
    else:
        print(False)

doblecero(0,1,2,2,3,4,5,6,0)



#Ejemplo del instructor:
def ceros_vecinos(*args):
    contador = 0

    for num in args:
        if contador + 1 == len(args): #Propósito: Evitar un error al intentar acceder a un índice fuera del rango. Esto ocurre al evaluar args[contador + 1] en la última posición.
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(1,0,4,5,6,7,53,6,8,9,0))


#otra manera de ia
def ceros_vecinos(*args):
    for i in range(len(args) - 1):  # Recorre índices hasta el penúltimo
        if args[i] == 0 and args[i + 1] == 0:  # Verifica ceros consecutivos
            return True
    return False








print('Ejercisio Practico 4'.center(50,'-'))

#un numero primo es aquel que solo es divicible eltre ellos mismos y el uno
def contar_primos(numero):
    if numero < 2:
        return 0  # No hay números primos menores que 2 ya que 0 y 1 no son numero primos

    primos = []
    for n in range(2, numero + 1):  # Empezamos en 2, porque 0 y 1 no son primos, usamos mas uno porque range no incluye el ultimo numero
        es_primo = True
        for i in range(2, int(n ** 0.5) + 1):  # Verificamos divisores hasta la raíz cuadrada de n
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)

    print(f"Números primos en el rango 0-{numero}: {primos}")
    return len(primos)


# Ejemplo de uso:
cantidad = contar_primos(23)
print(f"Cantidad de números primos encontrados: {cantidad}")



def contar_primos2(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos2(150))