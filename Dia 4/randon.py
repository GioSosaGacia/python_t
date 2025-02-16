
#randin sirve para que python retorne un entero de manera aleatoria
#rando debe de ser importado
print('Random'.center(50,'-'))

from random import * # si usamos un * nos importará todo
#randint recibe dos parametros inicio y final
aleatorio = randint(1,50)
print(aleatorio)

#Arroja un valor decimal dentro del rango seleccionado, para que no arrojes muchos decimalos usamos round para redondear y declaramos los decimales
aleatorio = round(uniform(1,5),2)
print(aleatorio)

#random no recibe parametros solo te dará una fraccion de un entero
aleatorio = random()
print(aleatorio)


#permite trabajar con una seleccion aleatorio dentro de los elementos de una lista
#choice

primos = ['Giovanni','Miclo', 'Luis','Julian','Higor','Chore Crema','Chore Torno','Po']
aleatorio = choice(primos)
print(aleatorio)


#shuffle = mezclar no se puede utilizar con string
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)





print('')
print('Comprensión de listas'.center(50,'-'))

#la comprension de listas es una forma dinamica de crear una lista
palabra ='Python'
#lista = []

#1.forma de crear una listas
#for letra in palabra:
#   lista.append(letra)

#2. con list comprehention
lista = [letra for letra in palabra]
print(lista)


#lista = [n for n in range(0,21,2)  if n * 2 > 10] si no tiene else esta correcto de esta manera pero si tiene va como el ajemplo que sigue
lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]
print(lista)

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]

print(metros)


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n **2 for n in valores]
print(valores_cuadrado)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [p for p in valores if p %2==0]
print(valores_pares)

#de f° a °c
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(c - 32) * (5/9) for c in temperatura_fahrenheit]

print(grados_celsius)




print('')
print('Match es como el switch case pero con match'.center(70,'-'))
serie = 'N-02'

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Lg')
    case 'N-04':
        print('Motorola')
    case _:
        print('Este producto no existe')




cliente = {'nombre':'Federico',
           'edad': 45,
           'ocupacion':'Instructor'}

pelicula = {'titulo':'matrix',
            'ficha_tecnica':{'protagonista':'Giovanni Sosa',
                             'director':'Lana'}}

elementos = [cliente,pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad': edad,
              'ocupacion':ocupacion}:
            print('Es un cliente')
            print(f'Mi nombre es: {nombre}, tengo {edad} años, soy: {ocupacion}')
        case {'titulo':titulo,
              'ficha_tecnica':{'protagonista':protagonista,
                               'director':director}}:
            print('Es una pelicula')
            print(f'Pelicula: {titulo} - Protagonistas: {protagonista} - Director: {director}')
        case _:
            print('No se que es esto')







from random import randint

intentos = 5
aleatorio = randint(1, 50)
jugador = input('Dime tu nombre: ')

print(f'Bienvenido {jugador}, adivina el número entre 1 y 50.')

while intentos > 0:
    intento = int(input(f'Intentos restantes: {intentos}. Adivina el número: '))

    # Validación si el número está dentro del rango permitido
    if intento < 1 or intento > 50:
        print(f'Número no permitido, debes adivinar un número entre 1 y 50.')
    elif intento < aleatorio:
        print('El número es mayor que el que ingresaste.')
        intentos -= 1  # Se restan intentos solo cuando el jugador se equivoca
    elif intento > aleatorio:
        print('El número es menor que el que ingresaste.')
        intentos -= 1  # Se restan intentos solo cuando el jugador se equivoca
    else:
        print(f'¡Felicidades {jugador}, adivinaste el número {aleatorio} en {6 - intentos} intentos!')
        break  # Si adivinó el número, termina el juego

    if intentos == 0:
        print(f'¡Lo siento, {jugador}! Has agotado tus intentos. El número era {aleatorio}.')
