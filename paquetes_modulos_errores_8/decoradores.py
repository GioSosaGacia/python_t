"""
Son patrones de diseño utilizados para dar nueva funcionalidad a objetos(funciones)
modificando su comportamiento sin alterar su estructura son funciones que modifican funciones y pueden ser asignadas a varibles y funciones

Inician con un @
"""

def cambiar_letras(tipo):

    def cambiar_mayuscula(texto):
         print(texto.upper())

    def cambiar_minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return cambiar_mayuscula
    elif tipo == "min":
        return cambiar_minuscula

operacion = cambiar_letras("may")
operacion('giovanni sosa garcia')


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return  otra_funcion


def cambiar_mayuscula(texto):
    print(texto.upper())


def cambiar_minuscula(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(cambiar_mayuscula)

cambiar_mayuscula('Giovanni')
mayuscula_decorada('Giovanni')
