"""Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa
o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos,
sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada."""

num1, num2, num3 = input().split(" ")
num1, num2, num3 = float(num1), float(num2), float(num3)

lista = [num1, num2, num3]
lista.sort(reverse=True)

num1, num2, num3 = lista[0], lista[1], lista[2]

if num1 >= (num2+num3):
    print("NAO FORMA TRIANGULO")
elif num1**2 == ((num2**2) + (num3**2)):
    print("TRIANGULO RETANGULO")
elif num1**2 > ( (num2**2) + (num3**2)):
    print("TRIANGULO OBTUSANGULO")
elif num1**2 < ( (num2**2) + (num3**2)):
    print("TRIANGULO ACUTANGULO")

if num1 == num2 and num2 == num3:
    print("TRIANGULO EQUILATERO")
elif (num1 == num2 and num1 != num3) or (num2 == num3 and num2 != num1) or (num1 == num3 and num1 != num3):
    print("TRIANGULO ISOSCELES")