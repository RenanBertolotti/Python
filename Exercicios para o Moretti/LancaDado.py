from random import randint

dado = []
numero1 = numero2 = numero3 = numero4 = numero5 = numero6 = 0

for i in range(50):
    dado.append(randint(1,6))
    if dado[i] == 1:
        numero1 +=1
    elif dado[i] == 2:
        numero2 +=1
    elif dado[i] == 3:
        numero3 +=1
    elif dado[i] == 4:
        numero4 +=1
    elif dado[i] == 5:
        numero5 +=1
    elif dado[i] == 6:
        numero6 +=1


porcentagem_face6 = (numero6 * 100) /50

print("*******************************************")
print("Valores de 50 vezes do dado lançado: ")
print(dado)

print("\nNumero total de vezes que caiu em cada lado:")
print(f"Lado1: {numero1}")
print(f"Lado2: {numero2}")
print(f"Lado3: {numero3}")
print(f"Lado4: {numero4}")
print(f"Lado5: {numero5}")
print(f"Lado6: {numero6}")


print(f"\nPercentual de Ocorrencias de face 6: {porcentagem_face6}%")
