"""
Esta funcion retorna una suma de dos valores
"""


def sumar(numero1, numero2):
    """
       Suma dos números y devuelve el resultado.

       Parámetros:
       a (int, float): El primer número a sumar.
       b (int, float): El segundo número a sumar.
    """
    return numero1 + numero2


SUMA = sumar(5, 7)
print(f' El resultado de la suma es: {SUMA}')


'''
Se le llama constante porque nunca cambia su valor, ademas debe de ir en mayuscula, usamos pylint para probarlo 
estas ultimas lineas afectaran la puntuacion borraralas para ver el resultado en la terminal de pycharm o cmd'''

#C:aqui va un slash antes de users Users\giova\Python_Total\paquetes_modulos_errores_8>pylint Errores_con_Pylint.py -r y
# (la r es de reporte y la y de yes)'''