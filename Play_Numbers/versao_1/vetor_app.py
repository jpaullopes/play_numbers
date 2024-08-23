import utils as ut
import vetor_utils as vu
import vetor_funcionalidades as vf


#função com as opções de escolha do menu
def menu_options():
     
    return'''  ----- [ PLAY NUMBERS ] -----
[ 1 ] - INICIALIZAR VETOR NUMÉRICO
[ 2 ] - MOSTRAR TODOS OS VALORES
[ 3 ] - RESETAR VETOR (PEDIR VALOR NÚMERO PADRÃO)
[ 4 ] - VER QUANTIDADE DE ITENS NO VETOR
[ 5 ] - VER MENOR E MAIOR VALORES E SUAS POSIÇÕES
[ 6 ] - SOMATÓRIO DOS VALORES
[ 7 ] - MÉDIA DOS VALORES
[ 8 ] - MOSTRAR VALORES POSITIVOS E QUANTIDADE
[ 9 ] - MOSTRAR VALORES NEGATIVOS E SUAS QUANTIDADES
[ 10 ] - ATUALIZAR TODOS OS VALORES POR UMA DAS REGRAS
[ 11 ] - ADICIONAR NOVOS VALORES
[ 12 ] - REMOVER ITENS POR VALOR EXATO
[ 13 ] - REMOVER POR POSIÇÃO
[ 14 ] - EDITAR VALOR ESPECÍFICO POR POSIÇÃO
[ 15 ] - SALVAR VALORES EM ARQUIVO
[ 16 ] - SAIR'''

def mini_menu_one():
        return''' --- [ OPÇÕES ] ---
[ 1 ] - GERAR LISTA COM VALORES ALEÁTORIOS
[ 2 ] - INFORMAR VALORES
[ 3 ] - CARREGAR VALORES DE UM ARQUIVO'''


def mini_menu_ten():
        return''' --- [ OPÇÕES ] ---
[ 1 ] - MULTIPLICAR POR UM VALOR
[ 2 ] - ELEVAR A UM VALOR
[ 3 ] - REDUZIR A UMA FRAÇÃO
[ 4 ] - SUBSTITUIR VALORES NEGATIVOS POR UM NÚMERO ALEATÓRIO
[ 5 ] - ORDENAR VALORES
[ 6 ] - EMBARALHAR VALORES'''


def main():

    menu = menu_options()
    print(menu)
    
    option = ut.get_between_numbers('Escolha uma opção: ',1,16)

    while option != 16:

        if option == 1:

            mini_menu = mini_menu_one()
            print(mini_menu)

            option_one = ut.get_between_numbers('Escolha uma opção: ',1,3)

            if option_one == 1:
                list_range = ut.get_positive_number('Informe o tamanho da lista: ')
                min_value = int(input('Informe o valor minimo do número aleátorio: '))
                max_value = ut.get_number_great('Informe o valor máximo do número aleatório: ',min_value)

                array = vu.random_list(list_range,min_value,max_value)

            elif option_one == 2:
                array = []
                list_range = ut.get_positive_number('Informe o tamanho da lista: ')

                for e in range(list_range):
                    array.append(int(input(f'{e + 1}° valor: ')))

            elif option_one == 3:
                array = []
                file_name = input('Informe o nome do arquivo: ')
                temp = vu.read_file(file_name)

                for e in temp:
                    array.append(int(e))

        elif option == 2:
            for ind,e in enumerate(array):
                print(f'{ind} - [{e}]')

        elif option == 3:
            corrent_value = int(input('Informe o valor de padronização: '))
            array = vf.padronization_value(array,corrent_value)
        
        elif option == 4:
            values_number = len(array)
            print(f'Esta lista possui [{values_number}] elementos')

        elif option == 5:
            value_min = vf.my_min(array)
            value_max = vf.my_max(array)
            index_value_min = vf.my_min(array, index= True)
            index_value_max = vf.my_max(array, index= True)
            
            print(' --[ MENOR ]--')
            print(f'{index_value_min} - [{value_min}]')
            print(' --[ MAIOR ]--')
            print(f'{index_value_max} - [{value_max}]')

        elif option == 6:
            sum = vf.my_sum(array)
            print(f'A soma dos elementos é de [{sum}]')

        elif option == 7:
            sum = vf.my_sum(array)
            average = sum / len(array)

            print(f'A média dos valores dessa lista é de [{average:.2f}]')

        elif option == 8:
            new_array = vu.my_filter(vf.positive_number,array)
            count = len(new_array)

            print('--[ NÚMERO(S) POSITIVO(S) ]--')
            for e in new_array:
                print(f'[{e}]')
            print(f'A lista possui [{count}] números positivos')

        elif option == 9:
            new_array = vu.my_filter(vf.negative_number,array)
            count = len(new_array)

            print('--[ NÚMERO(S) NEGATIVO(S) ]--')
            for e in new_array:
                print(f'[{e}]')
            print(f'A lista possui [{count}] número(s) negativo(s)')

        elif option == 10:
            mini_menu = mini_menu_ten()
            print(mini_menu)

            option_ten = ut.get_between_numbers('Escolha uma opção: ',1,6)

            if option_ten == 1:
                factor = int(input('Informe o valor multiplicador: '))
                array = vf.multiplicator(array,factor)

            elif option_ten == 2:
                exponent = int(input('Informe o valor do expoente da potenciação: '))
                array = vf.potentiaton(array,exponent)

            elif option_ten == 3:
                divider = float(input('Informe o valor do divisor: '))
                array = vf.division(array,divider)

            elif option_ten == 4:
                min_value = int(input('Informe o valor minimo da substituição:')) 
                max_value = int(input('Informe o valor maximo da substituição:')) 

                array = vf.replace_negative_numbers(array,min_value,max_value)

            elif option_ten == 5:
                array = vu.bobble_sorted(array)

            else:
                array = vf.shuffle(array)
        
        elif option == 11:
            count = int(input('Informe a quantidade de valores que serão adicionados: '))

            for e in range(count):
                new_value = int(input('Informe o novo valor a ser adicionado: '))
                array.append(new_value)
        
        elif option == 12:
            for ind,element in enumerate(array):
                print(f'{ind} - [{element}]')

            remove_value = float(input('Informe o valor que você quer remover da lista: '))
            array = vu.my_remove_value(array,remove_value)

        elif option == 13:
            for ind,element in enumerate(array):
                print(f'{ind} - [{element}]')

            remove_index = ut.get_between_numbers('Informe o index do valor que será removido: ',0,len(array))
            array = vu.my_remove_ind(array,remove_index)

        elif option == 14:
            for ind,element in enumerate(array):
                print(f'{ind} - [{element}]')

            index = int(input('Informe o index do valor: '))
            new_value = float(input('Informe o novo valor: ')) 

            array[index] = new_value

        elif option == 15:
            with open('play_numbers.txt','w') as file:
                for ind,element in enumerate(array):
                    file.write(f'{ind} - [{element}]\n')        

        print('-'*60)
        option = ut.get_between_numbers('Escolha uma opção: ',1,16)
    
    with open('play_numbers.txt','w') as file:
        for ind,element in enumerate(array):
            file.write(f'{ind} - [{element}]\n')  

    print(' ---[FIM DO PROGRAMA]---')
                

main()