"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, min, max, range
"""

# 0 ,  1 ,  2 ,  3 ,  4
lista = ["A", "Bacana", "C", "D", "E"]
# -5 , -4 , -3 , -2 , -1
print(lista)  # Mostra a linha inteira

lista[1] = "Renan"  # Modifica a lista de indice 1   , de "Bacana" vai para "Renan"
print(lista)

print(lista[0:3])  # imprime do 0 ate o 2
# ou
print(lista[:3])  # imprime do 0 ate o 2

print(lista[3:])  # imprime do 3 ate o final

print(lista[::2])  # imprime de 2 em 2

print(lista[::-1])  # imprime do final ate o começo de 1 em 1

############################
l1 = [1, 2, 3]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l3 = l1 + l2  È possivel!!!
l1.extend(l2)  # serve para adicionar na lista ,ou, l1.extend("Renan")
l2.append("b")  # serve para adicionar na lista apenas no final da lista
l2.insert(0, "banana")  # adciona na lista escolhendo o indice da lista
l2.pop()  # serve para excluir o ultimo elemento da lista
del (l2[0])  # exclui da lista do 0
del (l2[0:2])  # exclui da lista do 0 ate o 1

print(l1)
print(l2)
print(max(l2))  # pega o maior valor da lista
print(min(l2))  # pega o menor valor da lista

##################################
l3 = list(range(1, 10))  # adiciona na lista 1 ate o 9
# l3 = list(range(1,10:2)) # adiciona na lista 1 ate o 9 pulando de 2 em 2
print(l3)

for valor in l3:
    print(valor)

soma = 0
for i in l3:
    soma = soma + i

print(soma)

####################################
l4 = ["String", True, 10, -20, 5.5]

for elemento in l4:
    print(type(elemento))  # mostra o tipo do elemento

###########################  EXERCICIO  #############################
palavraSecreta = "perfume"
palavraDecifrada = ["*", "*", "*", "*", "*", "*", "*"]
letrasJaDigitadas = []
checa = "*"
chances = 3

while True:
    if chances == 0:
        print("GAME OVER")
        break

    if not checa in palavraDecifrada:
        print("PARABENS VOCE GANHOU!!!")
        break

    letraDigitada = input("Digite uma letra: ")

    if len(letraDigitada) > 1:
        if letraDigitada == "sair":
            break

        print("Digite apenas um caractere \n\n")
        continue
    else:
        if letraDigitada.isnumeric():
            print("Digite apenas letra \n\n")
            continue

        for i in range(len(palavraSecreta)):
            if letraDigitada == palavraSecreta[i]:
                print(f"Parabens: a {letraDigitada} esta na palavra secreta \n")

                palavraDecifrada[i] = letraDigitada

                print(palavraDecifrada)
                print(f"palavras ja digitadas: {letrasJaDigitadas}")

        if not letraDigitada in palavraSecreta:
            letrasJaDigitadas.append(letraDigitada)
            chances -= 1

            print(palavraDecifrada)
            print(f"palavras ja digitadas: {letrasJaDigitadas}")
