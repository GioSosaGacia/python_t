mi_text = 'This is a test'
#result = mi_text[0]
#rindex is the same but the opposite
#result = mi_text.index('h',5,10)#2th and 3th parameter indicate where to start and where to endup
#alerta de acción completada
#Un valor negativo en el tercer parámetro (step), permite invertir el sentido en el que recorremos un string
#Fragment str [donde inicia:donde termina:de cuantos carcateres avanzar]
result = mi_text[:6:2]
print(result)

text = "This is Giovanni's text"
#resultado = text.lower()/upper()
resultado = text.split()#lo separa por palabras/spacios vacios o por una letra en specifico entre ""
print(resultado)


#Para usar un join lo debemos de usar con un lista
'''
La función join() en Python se utiliza para unir los elementos de un iterable (como una lista, tupla o conjunto) en una sola cadena de texto, con un delimitador especificado entre los elementos.
'''
a ="Aprender"
b = "Python"
c = "es"
d = "genial!!"
e = " ".join([a,b,c,d])
print(e)

#find encuentra la posición del caracter deseado si no lo encuantra arroja -1
resultado1 = e.find("p")
print(resultado1)

#replace toma un fragmento del texto y lo cambia por otro
resultado2 = e.replace("Aprender", "Adquirir")
print(resultado2)

lista_palabras = ["La","legibilidad","cuenta."]
frase = " ".join(lista_palabras)
print(frase)


#Remplazar mas de una palabra dentro de str
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
nfrase = frase.replace("difícil","fácil")
nfrase = nfrase.replace("mala","buena")
print(nfrase)