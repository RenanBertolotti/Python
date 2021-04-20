################################FUNCAO NORMAL########################
def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)
print(var)


################################FUNCAO LAMBDA########################
a = lambda x, y: x * y
print(a(2,2))


#-----------------SEM LAMBDA---------------------------
lista = [ ["P1", 13], ["P2", 6], ["P3", 7], ["P4", 50], ["P5", 8] ]

def func(lista):            #lista pelo numero!!
    return lista[1]


lista.sort(key = func)     #lista.sort(key = func, reverse = True) - ordena do maior ao menor
print(lista)


#-----------------COM LAMBDA---------------------------------
lista = [ ["P1", 13], ["P2", 6], ["P3", 7], ["P4", 50], ["P5", 8] ]

lista.sort(key=lambda lista: lista[0])                   #ordena a lista original
print(sorted(lista,key = lambda lista: lista[0], reverse=True))        #ordena uma copia da lista original
print(lista)
