'''
Making the Grade - alcanzando la calificacion

Python has two looping constructs. while loops for indefinite (uncounted) iteration and for loops for definite, (counted) iteration.
 The keywords break, continue, and else help customize loop behavior. range() and enumerate() help with loop counting and indexing.

 loops will continue to execute as long as the loop expression or "test" evaluates to True in a boolean context,
 terminating when it evaluates to False:

'''

'''Va eliminando cada elemento de la lista y lo imprime hasta que la lista queda vacia'''
placeholders = ["spam", "ham", "eggs", "green_spam", "green_ham", "green_eggs"]

while placeholders:
    print(placeholders.pop(0))

print('')
word_list = ["bird", "chicken", "barrel", "bongo"]

for word in word_list:
    if word.startswith("b"):
        print(f"{word.title()} starts with a B.")
    else:
        print(f"{word.title()} doesn't start with a B.")

'''
 range(3, 15, 2):
La función range() genera una secuencia de números desde un número inicial hasta uno final, con un paso determinado.
3: Es el valor inicial (el primer número que aparecerá en la secuencia).
15: Es el valor final excluyente (el número 15 no se incluirá en la secuencia).
2: Es el paso. Esto significa que la secuencia aumentará de 2 en 2 (es decir, comenzará en 3, luego sumará 2, 
luego sumará 2 nuevamente, y así sucesivamente).
'''



print('')
'''
If both values and their indexes are needed, the built-in enumerate(<iterable>) will return (index, value) pairs:'''

word_list = ["bird", "chicken", "barrel", "apple"]

# *index* and *word* are the loop variables.
# Loop variables can be any valid python name.

for index, word in enumerate(word_list):
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a B.")
    else:
        print(f"{word.title()} (at index {index}) doesn't start with a B.")




print('')
# The same method can be used as a "lookup" for pairing items between two lists.
# Of course, if the lengths or indexes don't line up, this doesn't work.
#Para que una lista se una ambas listas deben de tener la misma longitud

word_list = ["cat", "chicken", "barrel", "apple", "spinach"]
category_list = ["mammal", "bird", "thing", "fruit", "vegetable"]

for index, word in enumerate(word_list):
    print(f"{word.title()} is in category: {category_list[index]}.")


#Altering Loop Behavior
#The continue keyword can be used to skip forward to the next iteration cycle:




print('')
#The continue keyword can be used to skip forward to the next iteration cycle:

word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple", "bear"]

# This will skip *bird*, at index 0
for index, word in enumerate(word_list):
    if index == 0:
        continue
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a b.")




print('')
#The break (like in many C-related languages) keyword can be used to stop the iteration and "break out" of the innermost enclosing loop
word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple"]

for index, word in enumerate(word_list):
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a B.")
    elif word == "sliver":
       break
    else:
       print(f"{word.title()} doesn't start with a B.")
       print("loop broken.")




print('')
print(' '.center(60,'-'))
'''Practicas:
round() no se puede usar directamente en una lista pero si al usar list comprehentions 
return [round(score) for score in student_scores] ya que itera la lista mediante un bucle'''
def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    return [round(score) for score in student_scores]
    #for numero in student_scores:
     #   rouned_numbers.append(round(numero))
    #return f'Lista de numeros redondeados: {rouned_numbers}'

student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
print(student_scores)
#rouned_numbers = []

print(round_scores(student_scores))