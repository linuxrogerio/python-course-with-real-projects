# Exercício - sistema de perguntas e respostas
import sys
perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]


# for pergunta in perguntas:
#     print(list(pergunta.items()))

#     lista = list(pergunta.items())
#     print(f"{lista[0][0]}: {lista[0][1]}")
#     print()
#     print(f"{lista[1][0]}:")

#     for indice, opcao in enumerate(lista[1][1]):
#         print(f"{indice}) {opcao}")
#         #print(indice)

#     indice = int(input("Escolha uma opção: "))
#     print(lista[2][1])
#     print("Acertou") if lista[1][indice] == lista[2][1] else print("Errou")

#     print()

qtd_acertos = 0
for pergunta in perguntas:
  print(f"Pergunta: {pergunta["Pergunta"]}")
  print()

  opcoes = pergunta["Opções"]

  for i, opcao in enumerate(opcoes):
    print(f"{i}) {opcao}")

  print()

  escolha = input("Escolha uma opção: ")

  acertou = False
  escolha_int = None
  qtd_opcoes = len(opcoes)


  if escolha.isdigit():
    escolha_int = int(escolha)

  if escolha_int is not None:
    if escolha_int >= 0 and escolha_int < qtd_opcoes:
      if opcoes[escolha_int] == pergunta["Resposta"]:
        acertou = True


  print()
  if acertou:
    qtd_acertos += 1
    print("Acertou!!")
  else:
    print("Errou!!")


  print()

print("Você acertou: ", qtd_acertos)
print("de ", len(perguntas), "Perguntas.")