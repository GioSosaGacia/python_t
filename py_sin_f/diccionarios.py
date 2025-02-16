#diccionario anidado


carros = {'coche':{
    'chevrolet':'Cruze',
    'color':'negro',
    'motor':2.0
    },
    'minicar':
        {'fiat':'mobi like',
         'color':'plata',
         'motor':1.0
         },
    'camioneta':{
        'marca':'kia',
        'color':'vainilla',
        'motor':1.6
    }
}
print(carros)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    adjusted_exchange_rate = exchange_rate * (1 + spread / 100)
    exchanged_amount = budget / adjusted_exchange_rate
    max_value = int(exchanged_amount // denomination) * denomination

    return max_value


print(exchangeable_value(127.25, 1.20, 10, 20))
exchangeable_value(127.25, 1.20, 10, 5)