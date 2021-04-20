"""
Count - Itertools
"""
from itertools  import count

contador = count()             #recebe um valor infinito, vai sempre adicionando
contador = count(start=5)      #Seta um inicio pra começar a contar
contador = count(start=5)      #Seta um inicio pra começar a contar
contador = count(step=2+2)     #Seta para contar em 2 em 2
contador = count(step=0.5)     #Seta para contar em 0.5 em 0.5
#contador = count(step=-1)      #Decremeta para contar em -1 em -1


for valor in contador:
    print(valor)

    if valor == 10:
        break


#######################################################################
contador = count()
lista = ["Renan", "Ana", "Maria"]
lista = zip(contador,lista)

print(list(lista))