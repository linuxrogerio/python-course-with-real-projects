# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(l1, l2):
#   intervalo = min(len(l1), len(l2))
#   return [
#     (l1[i], l2[i]) for i in range(intervalo)
#   ]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))


# nova_lista = []
# def zipper(l1, l2):
#   for estado in zip(l1, l2):
#     print(estado)
#     nova_lista.append(estado)
#   return nova_lista

# nova_lista = zipper(l1, l2)
# print(nova_lista)
