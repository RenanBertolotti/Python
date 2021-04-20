"""
Sets em python
- add (adiciona)
- update (atualiza)
- clear
- discard
- union | (une)
- intersection & (todos os elementos presentes nos dois sets)
- diference - (elementos apenas no set da esquerda)
- symmetric_diference ^ (elementos que estao nos dois sets, mas nao em ambos)
"""
#se cria assim:
s1 = {1, 2, 3, 4, 5, 6}

#criar set vazio
s2 = set()
#Nao se pode criar um Set em branco, Ex: s1 = {} , se fizer isso,estara criando um dicionario

for v in s1:
    print(v)

#-----------------------------------------
#add
s1.add(7)
s1.add(8)
s1.add(9)
print(s1)

#update
s1.update("renan")  #Nao adiciona o nome completo e sim seus indices, {'a', 'r', 'n', 'e'} e nao tem ordem!

#remove
s1.discard(2)
print(s1)

#Union - une dois Sets adcionando os numeros nao repetidos
sets = {1, 2, 3, 4, 5}
setss = {1, 2, 3, 4, 5, 6}

#assim:
setsss = sets | setss
#Ou
setsss.union(s1,s2)
print(setsss)
#----------------------------

#Intersection - une dois Sets removendo os numeros repetidos
sets = {1, 2, 3, 4, 5}
setss = {1, 2, 3, 4, 5, 6}

#assim:
setsss = sets & setss
#Ou
setsss.intersection(s1,s2)
print(setsss)
#----------------------------

#Difference - Remove todos os itens, menos o item que esta no Set da esquerda
sets = {1, 2, 3, 4, 5, 7}
setss = {1, 2, 3, 4, 5, 6}

#assim:
setsss = sets - setss
#Ou
setsss.difference(s1,s2)
print(setsss)
#----------------------------

#Symmetric_diference ^ Remove todos os itens, menos os itens que nao se repete
sets = {1, 2, 3, 4, 5, 7}
setss = {1, 2, 3, 4, 5, 6}

#assim:
setsss = sets ^ setss
print(setsss)
#----------------------------

############################################################################################
l1 = ["Renan", "Ana", "Maria"]
l2 = ["Renan", "Ana", "Maria", "Maria", "Maria", "Maria", "Maria", "Maria", "Maria", "Ana", "Ana", "Ana", "Ana", "Ana"]

l1 = set(l1)
l2 = set(l2)
print(l1 == l2)

#Fazendo a mesma coisa,porem sem converter para set
if set(l1) == set(l2):
    print("l1 é igual a l2")
else:
    print("l1 noa e igual a l2")

####################Convertendo uma lista em Set e depois voltando pra Lista################
l1 = [1,1,1,2,2,3,4,5,6,5,4,3,5,46,7,8,97,4,8,7,9,9,8,10,10]
l1 = set(l1)
l1 = list(l1)           #O codigo retora os numeros repetidos, porem tira da ordem
l1.sort()               #usanod o sort, ele volta na ordem!
print(l1)