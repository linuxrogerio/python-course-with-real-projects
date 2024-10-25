import os

palavra_secreta = 'especial'
letras_acertadas = ''
letras_erradas = '-'
tentativas = 0

print('\nTente adivinha a palavra letra por letra: \n')

while True:
    letra_digitada = input('\nDigite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    else:
        letras_erradas += f" {letra_digitada} -"

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '_'
    
    
    print(f'\nPalavra secreta: {palavra_formada}' )
    print(f'\nLetras já usadas: {letras_erradas}' )


    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ ACERTOU!!!')
        print(f'A palavra era: {palavra_formada}')
        print(f'Você realizou {tentativas} tentativas.')
        letras_acertadas = ''
        tentativas = 0