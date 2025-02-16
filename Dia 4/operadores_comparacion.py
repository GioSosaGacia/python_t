# == es igual?
# != diferente , > < mayor o menor >= =< mayor o menor igual,

#verificar si es el mismo resultado de la raiz
num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2
print(mi_bool)

num1 = 64 * 3
num2 = 24 * 8

mi_bool = num1 != num2
print(mi_bool)

#Operadores logicos and, or para que de true uno o el otro debe de ser True and not
#Usando and ambas comparaciones deben d ser verdaderas
mi_bool = 4 > 5 and 5 == 2+3
print(mi_bool)

texto = " Esta frase es breve"
mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool)

#not sirve para negar la comparacion original
mi_bool  = not  ('a' == 'a')
print(mi_bool)

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num2 < num3
print(mi_bool)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not ('exito' in frase) and not ('tecnología' in frase)
print(mi_bool)




#Control de flujo es segun sea el caso pytho ejecute un fragmento de codigo u otro segun sea el caso
#if else, elif, while, do while, for
print('if else'.center(50,'-'))
if 10 > 9:
    print('Es correcto')
else:
    print('Es falso')

edad = 19
calificacion = 6

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Felicidades, aprobaste!')
    else:
        print('Reprobado!!')
else:
    print('Eres adulto')


num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"

if num1 > num2:
    print(f'{num1} es mayor que {num2}')
elif num2 > num1:
    print(f'{num2} es mayor que {num1}')
else:
    print(f'{num1} y {num2} son iguales')

#El código que has escrito tiene un error en la última condición (else num1 == num2:)
# porque no se permite usar una expresión después de else. La corrección es simplemente
# usar else sin condiciones adicionales. Aquí está el código corregido:

edad = 19
tiene_licencia = True

if edad > 18 and tiene_licencia ==True:
    print("Puedes conducir")
    if tiene_licencia == False:
        print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

#Sin error:

'''Tu código tiene un problema lógico porque estás anidando una condición que verifica tiene_licencia == False dentro de
 un bloque que solo se ejecuta si tiene_licencia == True. Esto provoca que la condición interna nunca se cumpla.
Aquí está el código corregido y mejorado: python
'''
edad = 19
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad >= 18 and not tiene_licencia:
    print("No puedes conducir aún. Necesitas contar con una licencia.")
else:
    print("No puedes conducir. Debes tener al menos 18 años.")



habla_ingles = True
sabe_python = True

if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles == False and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")




print('')
#loop = bucle  un bloque de codigo se ejecuta mas de una vez asta cumplir una condición
#iterable recorrer una lista asta que se termine
#dos tipos de loops nveces y de manera infinita
print('Introduccion a loops'.center(50,'-'))

#for
lista = ['a','b','c','d']

for letras in lista:
    numero_letra = lista.index(letras) + 1
    print(f'letra {numero_letra} = {letras}')

lista = ['pablo','laura','fede','luis','julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre no comienza con la letra L')

#Nota si el print esta dentro del for se ejecuta ncantidad de veces asta terminar de recorres la lista etc
#si lo dejamos afuera del print solo imprimirá la ultima iteración

numero = [1,2,3,4,5,6,7]
mi_valor = 0

for numeros in numero:
    mi_valor = mi_valor + numeros

print(mi_valor)

