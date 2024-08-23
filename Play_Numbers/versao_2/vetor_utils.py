from random import randint

#é o meu map da shoppe kkk
def my_map(func,array):
    new_array = []

    for element in array:
        new_array.append(func(element))
    
    return new_array


#meu filter paraguái
def my_filter(func,array):
    new_array = []

    for element in array:
        if func(element):
            new_array.append(element)
    
    return new_array


#função que inverte uma lista
def my_reverse(array):
    new_array = []
    for e in array:
        new_array = [e] + new_array
    
    return new_array


#uma função sorted com algoritimo bobble sort , é o único que eu sei até agora, apesar de não ser o mais eficiente
def bobble_sorted(array, reverse = False):
    new_array = array.copy()
    
    for n in range(len(new_array)):
        for x in range(len(new_array)-n- 1):
            if new_array[x] > new_array[x+1]:
                new_array[x], new_array[x + 1] = new_array[x + 1], new_array[x]
    
    if reverse:
        new_array = my_reverse(new_array)
    
    return new_array


#uma funçõa que cria uma array com elementos aletaorios em um intervalo
def random_list(number_elements,min,max):
    new_array = []

    for e in range(number_elements):
        new_array.append(randint(min,max))

    return new_array


#uma função minha que teenta replicar as funcionalidades básicas do inssert
def my_inssert(array,value,index = -1):
    if index < 0:
        index += len(array)
    
    if index > len(array):
        index = len(array)

    #isso aqui me ajudou até na função abaixo, peguei do chat gpt tá
    array = array[:index] + [value] + array[index:]

    return array


#remove um elemento a lista com base no index
def my_remove_ind(array,index = -1):

    if index < 0:
        index += len(array)
    
    if index > len(array):
        index = len(array) - 1

    array = array[:index] + array[index + 1:]
    
    return array


#remove um elemento de uma lista por meio  do valor dela(vai remover o primeiro valor que aparecer que for referente ao valor informado)
def my_remove_value(array,value):

    if value not in array:
        return array
    
    array = my_remove_ind(array, array.index(value))
    return array


#leitura do arquivo e retorna em uma lista
def read_file(file_name):
    array = []

    fin = open(file_name)
    for line in fin:
        number = line.split()
        array = array + number
    
    return array


def my_reduce(array,func,initial_value):
    accumulator = initial_value

    for e in range(len(array)):
        accumulator = func(accumulator,array[e])

    return accumulator