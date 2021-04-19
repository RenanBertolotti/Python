from random import randint

numero_aleatorio = randint(1,100)
tentativas = 7

print("Bem vindo:")
while tentativas != 0 :
    numero_digitado = int(input("Digite um numero dentre 1 e 100: "))

    print(f"\nNumero digitado: {numero_digitado}")
    if numero_digitado > numero_aleatorio:
        print("O numero digitado é maior que o numero sorteado: ")
    elif numero_digitado < numero_aleatorio:
        print("O numero digitado é menor que o numero sorteado: ")
    else:
        print("Parabens você ganhou!!!")
        print(f"O numero sorteado foi: {numero_aleatorio}")
        break

    tentativas -= 1
    print(f"Tentativas restantes: {tentativas}\n")
    
    if tentativas == 0:
        print("Você perdeu!!!")
        print(f"Numero sorteado era: {numero_aleatorio}")
        break
