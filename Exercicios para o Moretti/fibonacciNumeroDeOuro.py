print("Gere N número de Fibonacci:")

n = int(input("Digite o valor de N: "))

lista = []
anterior = 1
proximo = 1
soma = 1

for n in range(0,n):
    print(anterior)

    soma = proximo + anterior
    anterior = proximo
    proximo = soma

    lista.append(proximo/anterior)


print(lista)