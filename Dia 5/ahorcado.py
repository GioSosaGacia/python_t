from random import choice

'''fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print(random_fruit)
'''

#funciones para:pedir letra, validar letra, checar letra, ver si gano o no


'''def juego_palabras():
    palabras = ["python", "programar", "juego", "computadora", "teclado"]
    palabra = random.choice(palabras)  # Selecciona una palabra aleatoria
    palabra_oculta = ["_"] * len(palabra)  # Representa la palabra con guiones
    intentos_restantes = 6  # Intentos permitidos

    print("¡Adivina la palabra!")
    print(" ".join(palabra_oculta))


    while intentos_restantes > 0 and "_" in palabra_oculta:
        letra = input(f"\nIntroduce una letra (intentos restantes: {intentos_restantes}): ").lower()

juego_palabras()'''




#Ejemplo del video:
palabras = ["python", "programar", "juego", "computadora", "teclado","tiburon","helipuesto","manzana", "enfermera","ingeniero","doctor"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


#elige una oalabra de una lista retornando la palabra + el conjunto de caracteres sin repeticiones mediente el uso de un set
def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas



#que le pida l usaurio que elija una letra y si esta dentro de abecedario el caracter seleccionado para a letra elegida
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No has elegido una letra correcta')
    return letra_elegida



#Motrar un guion por cada letra, imprime el stado en cada juego
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))



#Checar si la letra del usuario se encuentra o no
def checar_letra(letra_elejida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elejida in palabra_oculta and letra_elejida not in letras_correctas:
        letras_correctas.append(letra_elejida)
        coincidencias += 1
    elif letra_elejida in palabra_oculta and letra_elejida in letras_correctas:
        print("Ya has encontrado esa letra, intenta con otra diferente: ")
    else:
        letras_incorrectas.append(letra_elejida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias



#
def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)

    return True



def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones has encontrado la palabra!!!")
    return True



palabra, letras_unicas = elegir_palabra(palabras)


while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()
    intentos, terminado, aciertos = checar_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminado