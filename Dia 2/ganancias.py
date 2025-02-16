
#Vendedor recibe la comisión del 13% sobre el valor acumulado

nombre = input('Dime tu nombre: ')
ventas_totales = float(input('Dame el total de tus ventas: '))
#Cuando un resultado es entero arroja solo un decimal y si no es entero solo arrojara 2 decimales ya que es lo qhe se ha programado.
resultado = round(ventas_totales * 13 / 100, 2)

print(f'Buena tarde mi nombre es: {nombre} y mis vetas totales son: {ventas_totales}, tu ganancia es de: {resultado}')