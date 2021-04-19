matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input())

numero = int(input())
verdadeiro = True

for l in range(0, 4):
    for c in range(0, 4):
        if numero == matriz[l][c]:
            print(f"posicao da matris: {l}, {c}")
            verdadeiro = False

if verdadeiro:
    print("Não possui esse número na matriz")

print(matriz)

