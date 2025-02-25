'''
Metodos de listas:
    1.copy()
    2.Insert(0,2)  recibe un index en la posicicion que se agregara el 2
    3.Copy
    4.extends numbers.extend(other_numbers) combine an existing list with other iterable
    5.remove <list>.remove(<item>) will throw a ValueError if the item is not present in the list.
    6.pop remove an item using an index if an index is not specify pop will remove de last item or the final item numbers.pop(0)
    7.clear remove all items from a list, it doesn´t take any parameters numbers.clear() []
    8.reverse this method will reverse the order of elements in place
    9.sort names.sort() can be re-order the elements in place if you want to be in descending order you must use names.sort(reverse=True)
    10.sorted() return a sorted copy  where mutating the original list is undesirable, and count, count the items
    11.items.index(4) return the indx of the specify item items.index(4) -}> >>> items.index(4) = 1, names.index("Tina", 2, 5)

'''


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        print(f'se añadia a {person_name}, al lista: {express_queue}')
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue

express_queue = ["Carlos", "Lucía"]
normal_queue = ["Pedro", "María"]


print(add_me_to_the_queue(express_queue, normal_queue, 1, "Giovanni"))
print(add_me_to_the_queue(express_queue, normal_queue, 1, "Elena"))
print(add_me_to_the_queue(express_queue, normal_queue, 0, "Giovanni"))


#express_queue = ["John", "Anna"]
#normal_queue = ["Steve", "Sarah"]
#ticket_type = 0  # Express ticket
#person_name = "Alejandra"

#updated_queue = add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name)
#print(updated_queue)  # It will print the updated express queue with "Tom" added.






def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)

friens = ["Pedro", "María","Carlos", "Lucía"]

print(find_my_friend(friens,'Pedro'))



def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index,person_name)
    return queue
queue = ["Pedro", "María","Carlos", "Lucía"]
print(add_me_with_my_friends(queue,2,'Raquel'))




def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue
queue = ["Pedro", "María","Carlos", "Lucía"]
print(remove_the_mean_person(queue,'Carlos'))




def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """

    _1 = queue.count(person_name)
    return _1
queue = ["Pedro", "María", "Carlos", "Lucía", "Pedro"]

print(how_many_namefellows(queue,'Pedro'))



def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """

    return queue.pop()
queue = ["Pedro", "María", "Carlos", "Lucía", "Pedro"]
print(remove_the_last_person(queue))




def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    return sorted(queue)
queue = ["Pedro", "María", "Carlos", "Lucía", "Pedro"]
print(sorted_names(queue))