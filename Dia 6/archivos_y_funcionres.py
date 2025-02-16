'''
Práctica Archivos y Funciones 1
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro,
y devuelva su contenido (read).
'''

def abrir_leer(nombre_archivo):
    with open(nombre_archivo,'r') as archivo:
        contenido = archivo.read()
    return contenido

contenido = abrir_leer("Giovanni.txt")
#print(contenido)



'''Práctica Archivos y Funciones 2
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"'''
def sobrescribir(file_name):
    with open(file_name,'w') as archivo:
        contenido = archivo.write("contenido eliminado y sobrescrito por la funcion")
    return contenido

contenido = sobrescribir('mi_archivo.txt')
#print(contenido)



'''Práctica Archivos y Funciones 3
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
Finalmente, debe cerrar el archivo abierto.'''


def registro_error(documento):
    with open(documento, 'a') as archivo:
        contenido = archivo.write("\nse ha registrado un error de ejecución")
    return contenido

resultado = registro_error("mi_archivo.txt")
print(resultado)

#Respuesta:
def registro_error(archivo):
    mi_archivo = open(archivo, "a")
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()