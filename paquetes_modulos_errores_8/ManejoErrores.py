'''
Manejo de Errores: Para implementar el manejo de errores debemos de implementar:
try: intenta ejecutar tal codigo
except: si presenta un error, haz esto..
finally: no importa ejecuta esto...

Existen varios tipo de errores
'''

def suma():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    print('Gracias por sumar' + n1)


try:
    #coigo a probar
    suma()
except TypeError:
    #codigo a ejecutar si ahi un error
    print('Estas intentando concatenar tipos distintos de datos')
except ValueError:
    print('Ese no es un numero')
else:
    #Codigo a ejecutar si no ahy un error
    print('Funcion ejecutada correctamente')
finally:
    #cofigo que se ejecutara de todos modos
    print('Eso fue todo')


def pedir_numero():

    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste un numero {numero}')
            break
    print('Gracias!!')

pedir_numero()


def suma(num1, num2):
    try:
        resultado = num1 + num2
        print(resultado)
    except:
        print(f'El numero ingresado no es un numero')
    else:
        print(f'El resultado fue lo esperado {resultado}')


suma(3,3)



def cociente(num1, num2):
    try:
        # Intentamos realizar la división
        resultado = num1 / num2
        print(resultado)
    except TypeError:
        # Si hay un error de tipo, se maneja de esta manera
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        # Si hay un error de división por cero, se maneja de esta manera
        print("El segundo argumento no debe ser cero")

# Ejemplo de uso
cociente(10, 2)  # Esto imprimirá 5.0
cociente(10, 'a')  # Esto imprimirá "Los argumentos a ingresar deben ser números"
cociente(10, 0)  # Esto imprimirá "El segundo argumento no debe ser cero"




def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo,'r')
        contenido = archivo.read()
        print("Abriendo exitosamente")
        return contenido
    except FileNotFoundError:
        print( "El archivo no fue encontrado")
    except:
        print("Error desconocido")
    finally:
        print("Finalizando ejecución")
        try:
            archivo.close()  # Aseguramos que el archivo se cierre correctamente
        except:
            pass


contenido = print(abrir_archivo('mi_texto.txt'))