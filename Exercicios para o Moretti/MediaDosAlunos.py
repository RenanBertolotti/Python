import math

nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))

mediaAritimetica = (nota1 + nota2) / 2
mediaGeometrica = math.pow((nota1 * nota2), 1/2)
mediaHarmonica = 2/ ((1/nota1) + (1/nota2))


print("\nMédias: ")
print(f"Media Aritimetica: {mediaAritimetica:.2f}")
print(f"Media Geometrica: {mediaGeometrica:.2f}")
print(f"Media Harmonica: {mediaHarmonica:.4f}")
