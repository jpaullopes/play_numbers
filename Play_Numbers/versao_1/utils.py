#função que vai pedir um numero inteiro positivo ao usuário
def get_positive_number(text):
    number = int(input(text))

    while number < 0:
        number = int(input(text))
    
    return number


#função que vai pedir um numero inteiro negativo ao usuário
def get_negative_number(text):
    number = int(input(text))

    while number >= 0:
        print('Informe um valor válido')
        number = int(input(text))
    
    return number

#função que vai pedir um número entre um faixa delimitada
def get_between_numbers(text, min, max):
    number = int(input(text))

    while number < min or number > max:
        print('Informe um valor válido')
        number = int(input(text))

    return number


#função que vai pedir um número maior que determiada faixa
def get_number_great(text,min):
    number = int(input(text))

    while number < min:
        print('Informe um valor válido')
        number = int(input(text))

    return number


#função que vai pedir um número maior que determiada faixa
def get_number_smaller(text,max):
    number = int(input(text))

    while number > max:
        print('Informe um valor válido')
        number = int(input(text))

    return number


def get_number_different(text,exception):
    number = int(input(text))

    while number == exception:
        print('Informe um valor válido')
        number = int(input(text))
    return number