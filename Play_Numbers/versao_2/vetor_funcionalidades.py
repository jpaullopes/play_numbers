from random import randint
from vetor_utils import my_inssert

#função que padroniza todos os valores em um,pelo menos foi isso que eu entendi
def padronization_value(array,value):
    new_array = []
    for e in range(len(array)):
        new_array.append(value)
    return new_array


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


#soma os elementos de uma lista e retorna a soma
def my_sum(array):
    sum = 0
    for e in array:
        sum += e

    return sum

def positive_number(number):
    return number >= 0

def negative_number(number):
    return number < 0

#função que multiplica os valores de uma list apor um fator
def multiplicator(array,factor):
    new_array = []

    for e in array:
        new_array.append(e * factor)

    return new_array


#função que eleva os valores de uma lista por um determinado expoente
def potentiaton(array,exponent):
    new_array = []

    for e in array:
        new_array.append(e ** exponent)

    return new_array


def division(array,divider):
    new_array = []

    for e in array:
        new_array.append(e / divider)

    return new_array


#substitui os valores negativos da array por um aleatorio em uma determinada faia
def replace_negative_numbers(array,min,max):
    new_array = []

    for e in array:
        if e < 0:
            e = randint(min,max)
        new_array.append(e)

    return new_array


#embaralha uma lista
def shuffle(array):
    new_array = []

    for e in range(len(array)):
        random_position = randint(0,len(array))
        new_array = my_inssert(new_array,array[e],random_position)

    return new_array
