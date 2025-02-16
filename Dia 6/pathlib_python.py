from pathlib import Path
#Usando pathlib nos permite usar rutas de sistemas orientada a objetos
'''
Permite crear o mover arxhivos, enumerar archivos, crear rutas basadas en strings como ejemplo recibiendo una
tupla de str con los elementos de la tupla creará la ruta 

Ruta relativa que puede existir en varias direcciones o ubicaciones de nuestra sistema de archivos
Ruta absoluta se refiere a una ubicacion en especifico y solo una 
'''
base = Path.home()#imprime la ruta absoluta de mi direcctorio principal
guia = Path(base,"Barcelona",'Giovanni.txt')#al usar home podemos agregar una ruta en especifico  a nuestro directorio principal
guia_2 = guia.with_name("Polanco.txt")#with_name retorna una nueva ruta cambiando el archivo de destino
print(guia)
print(guia.parent)#retorna el antecesor de la ruta,como referencia la ultima carpeta antes del ultimo archivo
print(base)
print(guia_2)



'''Tambien podemos recorrer una serie de carpetas que elojen archivos txt como ejemplo e iterarlos '''
guia = Path(Path.home(),"Europa") #europa es uan carpeta que alojas otras carpetas con archivos txt como ejemplo
#con Path.home imprime la o las rutas desde home
#iteracion
for txt in Path(guia).glob("*.txt"):
    print(txt)

'''Si tenemos mas carpetas demtro de Europa y dentro de esas carpetas se alojan mas archivos .txt las podemos iterar
de la siguiente manera agregando otro * dentro de global hace que incluya todas las carpetas y subcarpetas para encontrar 
todas la carpetas '''
for txt in Path(guia).glob("**/*.txt"):
    print(txt)



'''Calcular rutas relacionadas entre si usando un metodo relative_to() y se usa para recuperar una porsion de 
una ruta larga, podemos construir rutas que nos permitan ver el contenido de rutas en especifico  '''

guia3 = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_ueropa = guia3.relative_to("Europa")
en_espania = guia3.relative_to(Path("Europa","España"))
print(en_ueropa)
print(en_espania)



'''Práctica Path 1
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
Recuerda importar Path del módulo pathlib, y utilizar el método home()'''
from pathlib import Path

ruta_base = Path.home()#el metodo home(), imprime la ruta del directorio principal
print(ruta_base)





'''base: Es una variable que contiene una ruta base (puede ser un directorio inicial como "/home/usuario", 
"C:/MisArchivos", etc.).
Path(base, "Barcelona", "Giovanni.txt"): El constructor de la clase Path toma varios argumentos y los combina de manera 
que representa una ruta completa. En este caso, a partir de base, se agrega la carpeta "Barcelona" y el archivo 
"Giovanni.txt", generando una ruta como, por ejemplo, "/home/usuario/Barcelona/Giovanni.txt" o "C:/MisArchivos/Barcelona/Giovanni.txt",
 dependiendo del valor de base.'''

'''Práctica Path 2
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
Almacena el directorio obtenido en la variable ruta. No olvides importar Path.'''

ruta3 = Path("Curso Python","Día 6","practicas_path.py")
print(ruta3)






'''
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py"
 a partir de la siguiente estructura de carpetas:
Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto 
Path que refiere a la carpeta base del usuario.'''
base = Path.home()
ruta = Path(base,"Curso Python","Día 6","practicas_path.py")
print(ruta)