#como limpiar la consola sin que nos muestre los input mas que solo el resultado
'''
1.en el menu primcipal seleccionamos run
2.seleccionamos edit configurations
3.emulate terminal in output console

Resultado:
C:\Python\POO\Django\venv\Scripts\python.exe "C:\Python_Total\Dia 6\limpiar_consola.py"
Tu nombre es: Giovanni y tienes 32 años
Ya no muestra los inputs, esto lo podemos usar en el ahorcado
'''
from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('cls') #cls es = clear solo que es windows se usa cls
print(f'Tu nombre es: {nombre} y tienes {edad} años')