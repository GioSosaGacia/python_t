
'''
Requisitos del proyecto Operadores comparacion, logicos, control de flujo, loops
1.Preguntar el nombre al usuario o jugador
2.Elige un numero dentro del rango 
3.Tienes 5 intentos
Condiciones
1.si es menor a 1 o superior a 100, numero no permitido o fuera de rango
2.Si es menor al que eligio el programa  notificará
3.si es mayor tambien
4.si es igual gano!! y cuantos intentos le ha tomado
'''

from random import randint

intentos = 5
aleatorio = randint(1,50)
jugador = input('Dime tu nombre: ')

print(f'Bienvenido {jugador}, adivina el número entre 1 y 50.')

while intentos > 0:
    intento = int(input(f'Intentos restantes: {intentos}. Adivina el número: '))
    #Tambien puede quedar de esta manera intentos -= 1 y omitir el de los if

    #otra manera if intento not in range(1,51)
    if intentos < 1 or intentos > 50:
        print(f'Numero no permitido, valor fuera de rango')
        intentos -= 1
    elif  intento < aleatorio:
        print(f'Numero por encima del valor')
        intentos -= 1
    elif intento > aleatorio:
        print(f'Numero abajo del valor')
        intentos -= 1
    else:
        print(f'¡Felicidades {jugador}, adivinaste el número {aleatorio} en {6 - intentos} intentos!')
        break
#salimos del bloque de codigo porque ya ha ganado o perdido
if intentos == 0:
    print(f'¡Lo siento, {jugador}! Has agotado tus intentos. El número era {aleatorio}.')





