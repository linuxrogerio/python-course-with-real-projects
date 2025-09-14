# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
  if lista is None:
    lista = []
  lista.append(nome)
  return lista

clientes1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', clientes1)
adiciona_clientes('Fernando', clientes1)
clientes1.append('Edu')

clientes2 = adiciona_clientes("Helena")
adiciona_clientes("Maria", clientes2)

clientes3 = adiciona_clientes("Moreira")
adiciona_clientes("Vivi", clientes3)

print(clientes1)
print(clientes2)
print(clientes3)
