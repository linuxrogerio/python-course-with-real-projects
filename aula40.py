""" Calculadora com while """

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: (= - / *): ' )

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1) 
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados såo inválidos.')
        continue

    operadores_permitidos = '+-/*'


    if len(operador) > 1:
        print('Digite apenas 1 operador.')
        continue

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if operador == '+':
        resultado = (numero_1_float + numero_2_float)
        print(f'O resultado de {numero_1_float} {operador} {numero_2_float} é igual a {resultado}.')
    elif operador == '-':
        resultado = (numero_1_float - numero_2_float)
        print(f'O resultado de {numero_1_float} {operador} {numero_2_float} é igual a {resultado}.')
    elif operador == '/':
        resultado = (numero_1_float / numero_2_float)
        print(f'O resultado de {numero_1_float} {operador} {numero_2_float} é igual a {resultado}.')
    elif operador == '*':
        resultado = (numero_1_float * numero_2_float)
        print(f'O resultado de {numero_1_float} {operador} {numero_2_float} é igual a {resultado}.')
    else:
        print('Nunca deveria chegar aqui.')
    
         

    sair = input('Quer sair? [S/N]: ').lower().startswith('s')

    if sair is True:
        break