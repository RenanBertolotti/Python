"""
Funçoes def - *args **kwargs
"""

#def funcao(a1, a2, a3, a4, a5, nome=None , a6=None): #caso use um padrao por default, os proximos depois dele precisam ter um padrao!!
#    print(a1, a2, a3, a4, a5)


#funcao(1, 2, 3, 4, 5)       #Sem declarar o nome e o a6
#funcao(1, 2, 3, 4, 5, nome="Renan" , a=6)    #As proximas funçones precisam ser declaradas como argumento

##############################################################################################
def novafuncao(*args):       #funcao que vc nao sabe quantos argumentos vao entrar, precisa utilizar *args
                             #args é uma TUPLA e itens de uma TUPLA NAO PODEM SER MODIFICADOS, porem, pode ser convertidos
                             #para uma LISTA

    #args = list(args)        #converte para uma lista , caso nao queira, nao precisa usar

    print(args)              #mostra todas os agumentos
    print(args[0])           #monstra o 1 argumento
    print(args[-1])          #monstra o ultimo argumento
    print(len(args))         #monstra o tamanho da tupla

    #para mandar uma lista como argumento:
lista = [1,2,3,4,5]
novafuncao(*lista)
    #####################################

novafuncao(1,2,3,4,5)

####################################################################################################
def function(*args, **kwargs):    #serve para argumentos com palavras chaves, *args(numeros,listas e afins)
    print(args)                                                              #*kwargs(palavras)
    print(kwargs)
    #print(kwargs["nome"], kwargs["sobrenome"])
    #ou assim
    #nome = kwargs.get("nome")
    #print(nome)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
function(*lista, *lista2, nome="Renan", sobrenome="Bertolotti")