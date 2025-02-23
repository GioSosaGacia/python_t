def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    rounds = [number, number + 1, number + 2]

    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


concatenate_rounds([1, 2, 3, 4], [5, 6, 7, 8])


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    for ronda in rounds:
        if ronda == number:
            return True
    return False


list_contains_round([1, 2, 3, 4, 5, 6, 7], 4)


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    total = sum(hand)
    average = total / len(hand) if len(hand) > 0 else 0
    return average


card_average([1, 2, 3, 4])


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    real_average = card_average(hand)
    fist_last_average = (hand[0] + hand[-1]) / 2
    hand_sorted = sorted(hand)
    media = hand_sorted[len(hand_sorted) // 2]
    return real_average == fist_last_average or real_average == media


print(approx_average_is_average([1, 2, 3, 4, 5, 6, 7, 8]))



hand_sorted = [1,2,3,4,5,6,7,8]
len(hand_sorted)
a = len(hand_sorted) // 2
print(a)
media = hand_sorted[4]
print(media)

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_average = card_average(hand[1::2])
    ood_average = card_average(hand[0::2])
    return even_average == ood_average

print(average_even_is_average_odd([1,2,3,4,5,6,7]))


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand


print(maybe_double_last([1, 4, 11]))


"""
El método .get() de un diccionario en Python se utiliza para obtener el valor asociado a una clave especificada, 
de manera más segura que acceder al diccionario directamente. La principal ventaja de usar .get() es que si la clave 
no existe, en lugar de generar un error, devuelve un valor predeterminado que tú elijas.

Sintaxis del .get():

dict.get(key, default_value)
key: Es la clave para la que deseas obtener el valor.
default_value (opcional): Es el valor que se devuelve si la clave no se encuentra en el diccionario. Si no se proporciona,
 el valor predeterminado es None.
"""

color_code_dict = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

# Función que devuelve el valor numérico asociado a un color
def color_code(color):
    color = color.lower()
    return color_code_dict.get(color, "Invalid color")

# Función que devuelve una lista de todos los colores disponibles
def colors():
    return list(color_code_dict.keys())  # Retorna los colores como una lista

# Bloque de pruebas para verificar el funcionamiento de las funciones
if __name__ == "__main__":
    # Prueba de la función color_code
    print("Test: color_code")
    print(color_code("red"))        # Debería retornar 2
    print(color_code("green"))      # Debería retornar 5
    print(color_code("blue"))       # Debería retornar 6
    print(color_code("black"))      # Debería retornar 0
    print(color_code("brown"))      # Debería retornar 1
    print(color_code("invalid_color"))

    # Prueba de la función colors
    print("\nTest: colors")
    print(colors())