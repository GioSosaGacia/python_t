
#1.pEDIR AL USUARIO QUE ingrese cualquier texto

texto = input("Escribe tu texto: ")
texto_minusculas = texto.lower()
texto_inverso = texto_minusculas[::-1]

#2.pEDIR AL usuario que ingrese 3 letras
letras_a_contar = list(input('Ingresa 3 letras: '))

#3.cONTRAR cuantas veces aparacen tales letras dentro del texto, ademas convertir el texto en minusculas
conteo_letras = {letra: texto_minusculas.count(letra) for letra in letras_a_contar}

#4.Cuantas palabras ahi a lo largo del texto
cantidad_palabras = len(texto_minusculas.split())

#5.Checar cual es la primera y ultima letra

#6.Palabras en inverso usando reverse
print(texto_inverso)

#7.Validar si existe la palabra python dentro del texto usando un bool y un diccionario
print("python" in texto_minusculas)

print(texto_minusculas)
print(conteo_letras)
print(cantidad_palabras)







print(" ")
print("Analizador de texto curso".center(50,"-"))

texto1 = input("Ingresa un texto de tu elección: ")
letras1 = []

texto1 = texto1.lower()

letras1.append(input("Ingresa la primera letra: ").lower())
letras1.append(input("Ingresa la segunda letra: ").lower())
letras1.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("Cantidad de letras")
cantidad_letras1 = texto1.count(letras1[0])
cantidad_letras2 = texto1.count(letras1[1])
cantidad_letras3 = texto1.count(letras1[2])

print(f'Hemos encontrado la letra: {letras1[0]} repetida {cantidad_letras1} veces')
print(f'Hemos encontrado la letra: {letras1[1]} repetida {cantidad_letras2} veces')
print(f'Hemos encontrado la letra: {letras1[2]} repetida {cantidad_letras3} veces')

print("\n")
print("Cantidad de palabras")#split separa en texto en porsiones mediante u nspacio vacio
palabras = texto1.split()
print(f'Hemos encontrado el largo {len(palabras)} palabras en el texto')

print("\n")
print("Letras de inicio y fin")
letras1_inicio = texto1[0]
letras1_final = texto1[-1]
print(f'La letra inicial es {letras1_inicio} y la final es {letras1_final}')

print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f'Si ordenamo tu texto alreves dirá: {texto_invertido}')


print("\n")
print("Buscando la palabra python")
buscar_python = 'python' in texto1
dic = {True:'si',False:'no'}
print(f'La palabra "Python" {dic[buscar_python]} se encuantra en el texto')