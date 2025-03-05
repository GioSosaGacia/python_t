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
return [round(score) for score in student_scores] ya que itera la lista mediante un bucle

How to create a list comprehension
[expresión for item in iterable]
'''
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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 != 0]
print(even_numbers)


print('')
def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    return len([score for score in student_scores if score <= 40])
print(count_failed_students(student_scores))



print('')
def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    return [score for score in student_scores if score >= threshold]

student_scores = [90,40,55,70,30,25,80,95,38,40]

print(f'Calificaciones que superar el limite: {above_threshold(student_scores,75)}')







import random
def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    # Definir un puntaje aleatorio para el estudiante
    score = random.randint(0, highest)  # Aquí generamos un puntaje aleatorio entre 0 y highest

    # Calcular el intervalo para cada calificación
    interval = (highest - 40) / 4  # Dividir el rango de 40 a highest en 4 partes iguales

    # Crear los umbrales (el primero será 41, luego sumamos el intervalo)
    thresholds = [int(40 + interval * i + 1) for i in range(1, 5)]

    # Asegurarse de que el último umbral no exceda la puntuación más alta
    thresholds[-1] = highest

    # Asegurarse de que el primer umbral sea exactamente 41
    thresholds[0] = 41

    # Asignar la calificación con letra según el puntaje
    if score <= 40:
        grade = "F"
    elif score < thresholds[1]:
        grade = "D"
    elif score < thresholds[2]:
        grade = "C"
    elif score < thresholds[3]:
        grade = "B"
    else:
        grade = "A"

    return f"Score: {score}, Grade: {grade}"  # Devuelve el puntaje generado y la calificación con letra



print(letter_grades(100))





print()
print('Union de listas usando zip y enumerate, usando list comprehention'.center(80,'-'))
def student_ranking(student_scores, student_names):
    """
    Empareja los nombres de los estudiantes con sus calificaciones y genera un ranking.

    :param student_scores: list de int - calificaciones de los estudiantes ordenadas de mayor a menor.
    :param student_names: list de str - nombres de los estudiantes ordenados por calificación de mayor a menor.
    :return: list de str - clasificación de los estudiantes con el formato requerido.
    """

    # Emparejamos nombres y calificaciones y generamos la lista con el formato adecuado
    ranking = [f"{i + 1}. {name}: {score}" for i, (name, score) in enumerate(zip(student_names, student_scores))]

    return ranking


student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names = ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred']
print(student_ranking(student_scores, student_names))

'''
Explicación:
zip(student_names, student_scores): Esto nos permite combinar las dos listas (nombres y calificaciones) en pares.
enumerate(): Esto nos da el índice i, que corresponde al lugar (ranking) del estudiante en la lista.
f"{i+1}. {name}: {score}": Utilizamos la sintaxis de f-strings para generar una cadena en el formato "rank. name: score",
 donde i+1 es el rango (porque i comienza en 0, pero queremos que los rangos comiencen desde 1).
'''






print("")
print("Usando next y list comprehention".center(70,'-'))

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    return next(([name, 100] for name, score in student_info if score == 100), [])

    #otra manera de hacerlo
    #for i in student_info:
     #   student, score = i
      #  if score == 100:
       #     return [student, 100]
    #return []

student_info = [['Sara', 99], ['Kora', 85],['Giovanni',100]]
print(perfect_score(student_info))


"""
next() obtiene el siguiente elemento de un iterador.
Si el iterador se agota, devuelve un valor predeterminado (si se pasa).
En este caso, estamos usando next() con un generador que produce solo el primer estudiante con una puntuación de 100.
es como un generador"""