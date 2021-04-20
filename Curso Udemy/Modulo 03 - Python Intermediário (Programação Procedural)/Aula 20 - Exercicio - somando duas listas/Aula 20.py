"""
Considerando duas listas de inteiros ou floats ( Lista A e Lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho menor.

exemplo:
listaA =    [1, 2, 3, 4, 5, 6, 7]
listaB =    [1, 2, 3, 4]
-----------RESULTADO--------------
listaSoma = [2, 4, 6, 8]
"""

listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]

#solucao #1
listaSoma = [a+b for a,b in zip(listaA,listaB)]
print(listaSoma)

#Solucao #2
listaSoma = []
for i in range(len(listaB)):
    listaSoma.append(listaA[i] + listaB[i])
print(listaSoma)


#Soluçao #3


