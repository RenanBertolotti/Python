"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

nome = "renan"

for letra in nome:  # letra recebe o indice da string, porem em char
    print(letra)

for i, letra in enumerate(nome):  # cria um map da String, {i == indice} {letra == char da string}
    print(i, letra)

for i in range(10): # vai automatico do 0 ate o 10
    print(i)

for i in range(0,10): #vai do 0 ate o 10
    print(i)

for i in range(0,10,1): #vai do 0 ate o 10 e pula de 1 em 1
    print(i)

for i in range(20,10,-1): #vai do 20 ate o 10 e decremente de 1 em 1
    print(i)

for i in range(100): # vai do 0 ate o 100 e mostra apenas os numeros pares
    if i % 2 == 0:
        print("par")

