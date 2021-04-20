"""
Faça uma lista de tarefas com as seguintes opcoes:
    adicionar tarefa
    listar tarefa
    opcao de desfazer (A cada vez que chamarmos, desfaz a ultima ação)
    opcao de refazer (A cada vez que chamarmos, refaz a ultima ação)

    ["Tarefa1","Tarefa2"]
    Desfazer -> ["Tarefa1"]
    Refazer -> ["Tarefa1","Tarefa2"]

    input -> Nova Tarefa
"""
def listar(listaTarefas):
    if not listaTarefas:
        print("lista vazia")
    else:
        for i,y in enumerate(listaTarefas):
            print(f"Tarefa {i}: {y}")


def desfazer(listaTarefas, ultimo):
    if not listaTarefas:
        print("lista Vazia")
    else:
        ultimo.append(listaTarefas[-1])
        listaTarefas.pop()


def refazer(listaTarefas, ultimo):
    if not ultimo:
        ("Vazio")
    else:
        listaTarefas.extend(ultimo)

#inicio
listaTarefas = []
ultimo = []

while(True):
    tarefa = input("Digite sua tarefa: ")

    if tarefa == "listar":
        listar(listaTarefas)
    elif tarefa == "desfazer":
        desfazer(listaTarefas, ultimo)
    elif tarefa == "refazer":
        refazer(listaTarefas, ultimo)
    elif tarefa == "sair":
        break
    else:
        listaTarefas.append(tarefa)
