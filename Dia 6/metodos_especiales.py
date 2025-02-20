'''
Metodos especiales o dunder = double underscore

'''

class CD:

    def __init__(self,autor, titulo,cancioes):
        self.autor = autor
        self.titulo = titulo
        self.canciones = cancioes

    def __str__(self):
        return f'Albun: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def  __del__(self):
        print('Se ha eliminado el album')

mi_cd = CD('Sam smith', 'Dreams', 16)
print(mi_cd)
print(len(mi_cd))
del mi_cd
#print(mi_cd)


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'


libro = Libro('El yano en llamas', 'Juan Rulfo', 115)
print(libro)