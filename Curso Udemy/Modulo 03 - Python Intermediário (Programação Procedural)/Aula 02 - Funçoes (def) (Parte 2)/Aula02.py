"""
Funçoes (def) - return
"""
def funcao(msg):
    #print(msg)
    #Em vez de print, usar:
    return msg


variavel = funcao("ola mundo")
print(variavel)                  #Retorna NULO , pois foi utilizado o print como retorno na funçao!,sendo o correto RETURN
#quando acontecer isso,usar:
if variavel is not None:    #checando se nao e Nulo
    print(variavel)
else:
    print("nenhum valor")

#########################################
def divisao(n1, n2):
    if n2 == 0:
        return f'nao existe divisao por 0'
    else:
        return n1 / n2

#Assim
conta = divisao(10, 0)
print(conta)
#OU
print(divisao(10, 5))

#############################################
def lista():                        # funcao que retorna lista
    return [1, 2, 3, 4, 5]


var = lista()
print(var, type(var))

#############################################
def none():
    return           #funcao que retona nulo

############################################
def boolean():
    return True    #Funcao que retonar booleano verdadeiro

#############################################

