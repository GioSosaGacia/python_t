'''
1.El método iterdir() en la clase Path de pathlib en Python es utilizado para iterar sobre los contenidos de un directorio.
envolver el codigo en un bucle while
usar system para limpiar la consola
buscar mas metodos en la documentacion
crea las funciones que necesites
crear un diagrama de flujo
'''
'''
#Administrador de recetas:
from pathlib import Path


print("¡Hola, Bienvenido al administradir de recetas!".center(78,'-'))

categorias = []

base = Path('C:/Users/giova/Recetas')
print(f'Las recetas estan en: {base}')

# Iterar sobre cada archivo o subdirectorio dentro de 'Recetas'
for fichero in base.iterdir():
    if fichero.is_dir():  # Verificar si es un subdirectorio
        print(f'\nEntrando en la carpeta: {fichero.name}')
        categorias.append(fichero.name)

        # Iterar sobre los archivos dentro del subdirectorio
        for archivo in fichero.iterdir():
            if archivo.is_file():  # Si es un archivo
                print(f'Archivo en {fichero.name}: {archivo.name}')
    else:
        # Si no es una carpeta, es un archivo directamente en el directorio base
        print(f'Archivo en {base.name}: {fichero.name}')
opciones = input("Elige una opción: ")

print(categorias)'''

from pathlib import Path
import os
from os import system

mi_ruta = Path(Path.home(),"Recetas")

#cuantas recetas hay:
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):  #** para que busque en todas las carpetas dentro de recetas con la terminación txt
        contador += 1
    return contador


def inicio():
    system('cls')#para que limpie la consola, configurar el debug
    print('*' * 80)
    print(" Bienvenido al administrador de recetas ".center(80,'*'))
    print('*' * 80)
    print('\n')
    print(f'Las recetas se encuentran en la ruta: {mi_ruta}')
    print(f'Total de recetas: {contar_recetas(mi_ruta)}')

#Creamos una opcion incorrecta

    eleccion_menu = 'x'
    #Si no es numerico y o no esta dentro del rango 1 -6 se sguira ejecutando
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion: ")
        print('''
        [1] - Leer receta
        [2] - Crear rceta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()
    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print('Categorias: ')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir(): #iterdir permite iterar dentro de un direcctorio
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias


def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input('\nElige una receta: ')

    return lista[int(eleccion_receta) - 1]


def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")
    # se le resta 1 porque las listas inician desde 0 y nuestro indice comienza en el 1
    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}]- {receta_str}')
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def leer_receta(receta):
    print(Path.read_text(receta))#read_text es el metodo del path para poder leer un archivo


def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print('Escribe tu nueva receta')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print('Lo siento esa receta ya existe')


def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu nueva categoria {nombre_categoria} ha sido creada')
            existe = True
        else:
            print('Lo siento esa receta ya existe')


def eliminar_receta(receta):
    Path(receta).unlink()#elimina un archivo
    print(f'La receta {receta.name} ha sifo eliminada')


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ha sido eliminada')


def volver_al_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")


finalizar_programa = False
while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_al_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_al_inicio()
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_al_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        volver_al_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_al_inicio()
    elif menu == 6:
        finalizar_programa = True




















'''if base.exists() and base.is_dir():
    # Iterar sobre el contenido del directorio y mostrarlo
    for item in base.iterdir():
        print(item)
else:
    print(f"La carpeta {base} no existe.")

print(f"Directorio home: {Path.home()}")'''
