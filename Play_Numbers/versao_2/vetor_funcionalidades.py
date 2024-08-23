from random import randint
from vetor_utils import my_inssert


#retorna o maior elemento da lista e caso o parametro index sej atrue ela retorna o index do maior
def my_max(array,index = False):
    biggest_value = array[0]
    biggest_index = 0

    for ind,e in enumerate(array):
       if e > biggest_value:
            biggest_index = ind
            biggest_value = e

    if index:
        return biggest_index
    return biggest_value


#retorna o menor elemento em uma lista, caso o parametro index seja True ela retorna o index do menos
def my_min(array, index = False):
    minor_value = array[0]
    minor_index = 0

    for ind,e in enumerate(array):
        if e < minor_value:
            minor_index = ind
            minor_value = e
    
    if index:
        return minor_index
    return minor_value


#embaralha uma lista
def shuffle(array):
    new_array = []

    for e in range(len(array)):
        random_position = randint(0,len(array))
        new_array = my_inssert(new_array,array[e],random_position)

    return new_array
