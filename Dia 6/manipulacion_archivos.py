#entraDA: input y salida: output
#abrir, leer, escribir y cerrar usando open(), read(), wirte() and close()
#de preferencia el archivo debe de estar en la misma ruta del proyecto, tambien se puede abrir desde cualquier ruta
#readline solo lee la primera linea
#rstring elimina el salto de linea al usar readline()

mi_archivo = open('Giovanni.txt')
print(mi_archivo.read()) #de esta manera podemos leer el contenido del archivo en consola
mi_archivo.close()# siempre que abrimos un archivo debemos de ejecutar el close para que cuando finalize la ejecución lo cierre y no siga consuminedo espacio en memoria



'''
Crear y escribir archivos mediante el uso de open() el cual recibe dos parametros el archivo y el modo 
ahi tres modes r = read sololectura y ese viene por defeto
w = write si ya existe se resetea y si no existe se crea nota siempre sobreescribe el texto agregado lo ideal es usar 'a'
a = solo escritura posicionandoce al final del archivo para que puedas escribir a partir de la ultima linea
 y si no existe lo crea 
 "x" - Create (Creación) - Crea un archivo, y arroja un error si el
mismo ya existe en el directorio
 
 w: no escribe con salto de linea se debe de usar \n o triple comilla simple 
 writelines = pasa una lista de strings escribe un string detras de otro 
'''
#nota si solo usamos 'w' y ya existe el archivo lo sobreescribe y si usamos 'a' te opcion a segir escribiendo despues de la ultima linea sin borrar lo que ya tenia almacenado
#archivo = open('Giovanni1.txt', 'w')
#archivo.write('Texto una cita para una entrevista en megacable')
#archivo.writelines(['Hola','mundo','aqui', 'estoy'])# no genera espacios ni saltos de lineas a menos que lo codifiquemos



#Usando A
archivo = open('Giovanni1.txt', 'a')

'''lista = [' hola','mundo','aqui','estoy']
for p in lista:
    archivo.writelines(p + '\n')'''

archivo.write('bienvenido')
archivo.close()





'''ejercision practicos
Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
Imprime el contenido completo de "mi_archivo.txt" al finalizar.
Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.'''

archivo = open("mi_archivo.txt",'w')
archivo.write("Nuevo texto\n")

archivo = open("mi_archivo.txt", "r")
contenido = archivo.read()
#print(contenido)


'''Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
Imprime el contenido completo de "mi_archivo.txt" al finalizar.
Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.'''

archivo = open("mi_archivo.txt", 'a')
archivo.write("Nuevo inicio de sesión")

archivo = open("mi_archivo.txt", 'r')
contenido1 = archivo.read()
print(contenido1)


'''Práctica Crear y Escribir Archivos 3
Utiliza el método writelines para escribir los valores de la siguiente lista al 
final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en
 modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.'''

archivo = open("registro.txt",'a')

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for r in registro_ultima_sesion:
    archivo.write(r + '\t')

archivo = open("registro.txt", 'r')
contenido2 = archivo.read()
print(contenido2)


'''Nota tambien podemos abrir archivos utilizando la ruta donde se aloja el documento 
solo debemos de agregar la ruta usando \\ doble barra invertida ya que si utilizamos solo una python lo 
reconocera como un caracter especial

debemos de usar el modula Path y os = sistema operativo '''

import os
#getcwd get curring working direcctory
#os.chdir = change diectory
#ruta = os.getcwd()#mostrará la ruta en a cual estamos trabajando
#ruta = os.chdir('C:\\Users\\giova\\Escritorio\\ruta_alterna')#acceder a un archivo alojado en otra ruta
#ruta = os.makedirs('C:\\Users\\giova\\Escritorio\\ruta_alterna\\otra')#para crear un folder usasmo makedirs

ruta = 'C:\\Python_Total\\Dia 6\\prueba.txt'
#archivo = open('otro_ARCHIVO.txt')
#elemento = os.path.dirname(ruta) #dirname -> nos imprime la ruta base del direcctorio
#elemento = os.path.split(ruta) #mos mostrara una tupla con dos elemento 1 con la ruta y 2 el nombre del archivo
#print(elemento)

#os.rmdir('C:\\Users\\giova\\Escritorio\\ruta_alterna\\otra')#rmdir elimina un folder en este caso el de la ultima posicion

#print(archivo.read())
#print(ruta)

#otro archivo de uan ruta diferentee
otro_archivo = open('C:\\Users\\giova\\Escritorio\\ruta_alterna\\otro_ARCHIVO.txt')
print(otro_archivo.read())


'''Rutas que puedan ser interpretadas por cualquier sistema operativo mediante el uso del objeto Path 
cuando es un objeto la letra capital va en mayuscula'''

print('PathLib'.center(50,'-'))
from pathlib import Path, PureWindowsPath
#usa el / y no \ como lo usa windows
#carpeta = Path('C:/Users/giova/Escritorio/ruta_alterna')# de esta forma se usa en mac pero usando Path cualquier os lo podra abrir de esta manera
#archivo = carpeta / 'otro_ARCHIVO.txt' #con el / estamos concatenando un slash para crear la ruta y abrir el archivo

#Tambien se puede hacer de esta manera y ahorar codigo, en una sola liena
#carpeta = Path('C:/Users/giova/Escritorio/ruta_alterna') / 'otro_ARCHIVO.txt'

#mi_archivo = open(archivo)
#print(mi_archivo.read())

'''En Python, la función basename se utiliza para obtener el nombre del archivo a partir de una ruta completa.
 Es parte del módulo os.path'''

#pathlib permite gestionar rutas de sistemas de archivos en cualquier sistema operativo:
#de esta manera no debemos de usar el ipen y el close para poder gestionar un archivo

carpeta = Path('C:/Users/giova/Escritorio/ruta_alterna/otro_ARCHIVO.txt')
print(carpeta.read_text())
print(carpeta.name) #nos da el nombre del archivo
print(carpeta.suffix)#nos da el sufijo del tipo del archivo
print(carpeta.stem)#stem es un atributo que devuelve el nombre base de un archivo o directorio sin su extensión.

#PureWindowsPath transforma cualquier ruta a una ruta de windows
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Si existe')


