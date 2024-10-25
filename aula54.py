"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
incluir, apagar e listar valores da sua lista
Não permida que o programa quebre com erros
de índices inixistentes na lista.
"""
import os


option = ''
lista = []
while True:
    print('\nSelecione uma opção...\n')
    option = input(str('[i]nserir [a]pagar [l]istar [s]air: ').lower())
    
     

    if option[0] == 's':
        break
    
    elif option[0] == 'i':
        item = input('Valor a inserir: ' )
        lista.append(item)
        os.system('clear')
    
    elif option[0] == 'l':
        print('-=-' * 20)
        for indice, valor in enumerate(lista):
            print(f'{indice} -> {valor}')
        print('-=-' * 20)
    
    elif option[0] ==  'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    else:
        print('Por favor escolha i, a, l, ou s.\n')
