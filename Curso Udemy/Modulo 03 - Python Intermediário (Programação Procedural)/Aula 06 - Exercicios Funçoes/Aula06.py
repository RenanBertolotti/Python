# 1 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada
def function1(function2):
    return print(function2)


def function2():
    return 1 + 1


function1(function2())

# 2 -Crie uma funcao que recebe uma funcao2 como parametro e retorne o valor da funca2 executada. Faca a funcao1 executar
#duas funcoes que recebam um numero diferente de argumentos
def funcao1(funcao2):
    return funcao2


def funcao2(*args, **kwargs):
    for valor in kwargs:
        return print(valor)

    for i,j in args,args:
        return print(i, j)



lista = [1,2,3,4,5]
lista2 = lista + [6, 7, 8, 9, 10]
funcao1(funcao2(lista, lista2))