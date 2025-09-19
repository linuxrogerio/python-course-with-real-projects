# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os


def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('\nTAREFAS:')
    for tarefa in tarefas:
        print(f"* {tarefa}")
    print('')  # linha em branco


def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'Tarefa {tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print("")  # linha em branco
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print("Nenhuma tarefa para refazer")
        return

    tarefa = tarefas_refazer.pop()
    print(f'Tarefa {tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print("")  # linha em branco
    listar(tarefas)


def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return

    print(f"Tarefa {tarefa=} adicionada na lista de tarefas.")
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada com sucesso!')
    print("")  # linha em branco
    listar(tarefas)

# main call

tarefas = []
tarefas_refazer = []

while True:
    print('\nComandos: listar, desfazer, refazer, limpar ou sair')
    tarefa = input('\nDigite uma tarefa ou comando: ')

    comandos = {
        "listar": lambda: listar(tarefas),
        "desfazer": lambda: desfazer(tarefas, tarefas_refazer),
        "refazer": lambda: refazer(tarefas, tarefas_refazer),
        "limpar": lambda: os.system("clear"),
        "adicionar": lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos["adicionar"]
    comando()

    # if not tarefa:
    #     print("Tarefa ou comando inválid(a|o)")
    #     continue
    # elif tarefa == "listar":
    #     listar(tarefas)
    #     continue
    # elif tarefa == "desfazer":
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == "refazer":
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == "limpar":
    #     os.system("clear")
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue
