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

#No python é uma ma pratica de progamaçao usar variavel global dentro de uma funcao!

def adicionaTarefa():
    global listatarefas
    lista = list(input("Digite o nome da Tarefa: ").split("\n"))
    listatarefas.extend(lista)


def listaTarefa():
    global listatarefas

    if not listatarefas :
        print("Lista Vazia")
    else:
        for i,x in enumerate(listatarefas):
            print(f"tarefa {i}: {x}")


def desfazerLista():
    global listatarefas
    global ultimo

    if not listatarefas:
        print("lista Vazia")
    else:
        ultimo = str(listatarefas[-1]).split("\n")
        print(ultimo)
        listatarefas.remove(listatarefas[-1])

def refazerLista():
    global ultimo
    if not ultimo:
        print("Precisa Desfazer primeiro")
    else:
        global listatarefas
        listatarefas.extend(list(ultimo))


def sair():
    global testa
    testa = False



def opcEscolhida(opc):
    if opc == 1:
        adicionaTarefa()
    elif opc == 2:
        listaTarefa()
    elif opc == 3:
        desfazerLista()
    elif opc == 4:
        refazerLista()
    elif opc == 5:
        sair()
    else:
        print("Digite uma opc válida")


def menu():
    print("[1] = Adicionar Tarefa: ")
    print("[2] = Listar Tarefas: ")
    print("[3] = Desfazer Tarefas: ")
    print("[4] = Refazer Tarefaz: ")
    print("[5] - Sair")


#inicio
testa = True
listatarefas = []
ultimo = []

print("BEM VINDO AO APP DE TAREFAS")

while(testa == True):
    menu()
    opc = int(input("Selecione a opc desejada: "))
    opcEscolhida(opc)
    print("\n")








