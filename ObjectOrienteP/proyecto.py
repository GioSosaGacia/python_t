class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self,nombre,apellido,no_cuenta,balance=0):
        super().__init__(nombre,apellido)
        self.no_cuenta = no_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\nTu saldo es de: ${self.balance} pesos.'


    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print('¡Deposito exitoso!')

    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print('Retiro realizado.')
        else:
            print('Fondos Insuficientes')


def crear_cliente():
    nombre_cl = input('Ingrese su nombre: ')
    apellido_cl = input('Ingrese su apellido: ')
    no_cuenta = int(input('Ingrese su numero de cuenta: '))
    cliente1 = Cliente(nombre_cl,apellido_cl,no_cuenta)
    return cliente1

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije : Depositar (D), Retirar (R), o Salir (S) ')
        opcion = input()

        if opcion == 'D':
            monto_deposito  = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_deposito)
        elif opcion == 'R':
            monto_retiro = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_retiro)
        print(mi_cliente)
    print('Gracias por operar banco Python')

inicio()
