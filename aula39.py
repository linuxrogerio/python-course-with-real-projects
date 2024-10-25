nome = 'Rogerio Reis'
indice = 0
nome_novo = ''

while indice < len(nome):
    letra = nome[indice]
    nome_novo += f'#{letra}'
    indice += 1
nome_novo += '#'
print(nome_novo)