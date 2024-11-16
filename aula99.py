from sys import path

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import * # Não recomendado

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')

print(soma_do_modulo(1, 3))
print(aula99_package.modulo.soma_do_modulo(1, 3))
print(modulo.soma_do_modulo(1, 3))
print(soma_do_modulo(1, 3))
print(variavel)
print(nova_variavel)
