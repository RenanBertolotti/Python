import numpy

matriz10x10 = numpy.empty([10,10], dtype=int)

for i in range(10):
    for j in range(10):
        matriz10x10[i][j] = int(input(f"Digite o valor da posicao {i + 1}-{j + 1}: "))

print("Imprimindo a Matriz10-10:")
print(matriz10x10)
print("\n")
print("\n")
print("Imprimindo a Matriz10-10 com os elementos girados em 90ª:")
print(matriz10x10.transpose())
