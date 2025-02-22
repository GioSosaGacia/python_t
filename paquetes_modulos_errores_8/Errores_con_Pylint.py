#Herramientas de prueba pylint: es un verificadpr de codigo, errores y calidad para Python, siguiendo el stilo recomendado por
#    PEP8 la guia de estilo de python
#    se debde de instalar pylint con pip install pylint y al ejecutarlo devolvera un reporte con las caracteristicas que fueron evaluadas.

#    PEP-8:
#Unittes: Permite probar los programas

#Vamos al CDM PARA EJECUTAR EL ARCHIVO
#C:\Users\giova\Python_Total\paquetes_modulos_errores_8>pylint Errores_con_Pylint.py -r y (la r es de reporte y la y de yes)
# al ejecutarlo nos arrojara un reporte
    #lOS QUE COMIENzan con C son cuestiones de estilo
    #Los que inician con E son errores
    #Errores_con_Pylint.py:2:0: E0011: Unrecognized file option 'por' (unrecognized-inline-option)
    #Errores_con_Pylint.py:4:0: C0301: Line too long (138/100) (line-too-long)
    #Errores_con_Pylint.py:13:0: C0304: Final newline missing (missing-final-newline)
    #Errores_con_Pylint.py:1:0: C0114: Missing module docstring (missing-module-docstring)
    #Errores_con_Pylint.py:1:0: C0103: Module name "Errores_con_Pylint" doesn't conform to snake_case naming style (invalid-name)
    #Errores_con_Pylint.py:12:0: C0103: Constant name "numero1" doesn't conform to UPPER_CASE naming style (invalid-name)
    #Errores_con_Pylint.py:13:6: E0602: Undefined variable 'Numero1' (undefined-variable)

    #Lo podemos ejecutar desde el cmd o directamente del editor de codigo

'''
Este es un modulo que imprime algo
'''


def unafuncion():
    numero1 = 500
    print(numero1)


unafuncion()