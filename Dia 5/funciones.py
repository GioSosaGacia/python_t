#funciones
#debemos de apoyarnos en la ayuda contextual de python
#metodos son funciones pertenecientes a los objetos

dic = {'clave1':100, 'clave2':500}

a = dic.popitem() #elimina el ultimo dato del dic usa last in, first out
print(dic)
print(a) #este fue el valor eliminado del dic

'''
En Python, el método lstrip() elimina los caracteres iniciales de una cadena.
 Es útil para limpiar cadenas que comienzan con espacios o caracteres no deseados
 '''


#Remueve los caracteres a la izquierda de nuestro texto principal:
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

a = texto.lstrip(',:_#,,,,,,:::____##')
print(a)
print(texto)


#Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando
#el método insert(): agrega un item enn una pisicion determinada
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)




#isdisjoint()  method returns True if none of the items are present in both sets, otherwise it returns False.
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)






#Permiten crear bloques de codigo que solo se ejecuta cuando son llamadas, reciben información en forma de parametros y retornan datos
print('Funciones'.center(50,'-'))
print('')

def saludar_persona(nombre):
    print('Hola ' + nombre)
saludar_persona('Giovanni')

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
nombre_persona = 'Carlos'
bienvenida(nombre_persona)





def cuadrado(un_numero):
    print(un_numero ** 2)
un_numero = 5




def multiplicar(num1, num2):
    return  num1*num2 #return almacena el resultado en una variable y printn solo la muestra en pantalla

resultado = multiplicar(2,5)
print(resultado)




def potencia(num1, num2):
    return num1 ** num2
resultado = potencia(2, 2)
print(resultado)




#conversion de dolares a euros
def usd_a_eur(num):
    return num * 0.96
dolares = usd_a_eur(5)
print(dolares)




#transformar una palabra a mayusculas y leerla usando reverse() y usando el slicing [::-1]y luego convier.upper().
def invertir_palabra(palabra):
    return palabra[::-1].upper()

palabra = "Python"

resultado = invertir_palabra(palabra)
print(resultado)