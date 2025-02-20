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


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # Define the set of ten-cards
    ten_cards = {'10', 'K', 'Q', 'J'}

    # Check if one card is an Ace and the other is a ten-card
    if ('A' in [card_one, card_two]) and (card_one in ten_cards or card_two in ten_cards):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    # Define the set of ten-cards
    ten_cards = {'10', 'K', 'Q', 'J'}
    if card_one == card_two or (card_one == 'Q' and card_two == 'K') or (card_one == 'K' and card_two == 'Q'):
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    # Asignar valor a cada carta
    if card_one in ['J', 'Q', 'K', '10']:
        value_one = 10
    elif card_one == 'A':
        value_one = 1  # Tratamos el As como 1 inicialmente
    else:
        value_one = int(card_one)  # Para las cartas numéricas de '2' a '9'

    if card_two in ['J', 'Q', 'K', '10']:
        value_two = 10
    elif card_two == 'A':
        value_two = 1  # Tratamos el As como 1 inicialmente
    else:
        value_two = int(card_two)  # Para las cartas numéricas de '2' a '9'

    # Calcular el total de las cartas
    total_value = value_one + value_two

    # Si alguna carta es un As, tratamos de sumarlo como 11 si es posible
    if card_one == 'A' or card_two == 'A':
        # Si sumamos 10 al total (tratando el As como 11) y es 9, 10 o 11, podemos duplicar
        if total_value + 10 in [9, 10, 11]:
            total_value += 10

    # Verificar si la suma total es 9, 10 o 11
    if total_value in [9, 10, 11]:
        return True
    return False





def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words_with_prefix = [prefix] + [prefix + i for i in vocab_words[1:]]
    return ' :: '.join(words_with_prefix)


vocab_words = ['en', 'close', 'joy', 'lighten']
result = make_word_groups(vocab_words)
print(result)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    # Verificamos si el sufijo es 'ness' y lo eliminamos
    if word.endswith('ness'):
        word = word[:-4]  # Elimina 'ness'

        # Realizamos ajustes ortográficos si es necesario
        if word.endswith('i'):
            word = word[:-1] + 'y'  # Cambiar 'i' por 'y' en palabras como 'happiness' -> 'happy'

    return word

print(remove_suffix_ness('happiness'))

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    frase = sentence.split(' ')[2] + index
    return frase

print(adjective_to_verb("It got, dark as the sun set.", 'en'))

import string


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    words = sentence.split()  # Dividir la oración en palabras
    adjective = words[index]  # Obtener la palabra en la posición indicada (adjetivo)

    # Eliminar cualquier puntuación que esté al final del adjetivo
    adjective = adjective.strip(string.punctuation)

    # Convertir el adjetivo en un verbo añadiendo el sufijo 'en'
    verb = adjective + "en"

    return verb


# Ejemplo de uso
sentence = "His expression went dark."
index = -1
result = adjective_to_verb(sentence, index)
print(result)  # Resultado esperado: 'darken'




def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    palabra = title.title()
    return palabra

print(capitalize_title("hello, and welcome to my world."))


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    return sentence.replace(old_word, new_word)


print(replace_word_choice("I bake good cakes.", "good", "amazing"))