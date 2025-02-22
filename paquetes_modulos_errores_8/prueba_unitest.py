"""
unittest se usa para probar el codigo programado, viene incorporada con python
Creamos dos modulos:1-con el nombre del codigo a probar, 2-para hacer la prueba
"""

import unittest
import cambia_texto


class ProbarCambiarTexto(unittest.TestCase):

    #debe de empezar con la palabras test para que el sistema lo identifique
    def test_mayusculas(self):
        palabar = 'buen dia'
        resultado = cambia_texto.todo_mayusculas(palabar)
        #Verifica que resultado sea == a 'BUEN DIA'
        self.assertEqual(resultado,'Buen Dia')

if __name__ == '__main__':
    unittest.main()