vetor = [20]
impar = []
par = []

for i in range(20):
    vetor.insert(i, int(input()))
    if vetor[i] %2 == 0:
        par.append(vetor[i])
    else:
        impar.append(vetor[i])

print("Numeros Digitados: ", end="")
for i in range(20):
    print(f"{vetor[i]}", end=" ")

print(f"\n{len(par)} números pares: ", end="")
for i in range(len(par)):
    print(f"{par[i]}", end=" ")

print(f"\n{len(impar)} números impares: ", end="")
for i in range(len(impar)):
    print(f"{impar[i]}", end=" ")
