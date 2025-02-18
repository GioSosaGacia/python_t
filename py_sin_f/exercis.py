def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
        # Verificar si la carta es un 'A' (As)
    elif card == 'A':
        return 1
        # Si la carta es un número (de '2' a '10'), isdigit() si es un digito se convierte en un valor entero y lo retorna
    else:
        return int(card)  # For cards '2' to '10', return their numerical value

print(value_of_card('J'))

def higher_card(card_one, card_two):
    # Utilizamos la función value_of_card para obtener los valores de ambas cartas
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    # Comparar los valores
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return (card_one, card_two)  # Retorna ambas cartas si son iguales

print(higher_card('A', 'A'))

def value_of_ace(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    total_value = value_one + value_two

    # If there's already an Ace in the hand, treat the next Ace as 1
    if 'A' in [card_one, card_two]:
        return 1

    # If adding 10 (i.e., treating the Ace as 11) doesn't bust the hand, return 11
    if total_value + 10 <= 21:
        return 11
    else:
        return 1