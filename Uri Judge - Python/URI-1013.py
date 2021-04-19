"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
Utilize a fórmula:

MaiorAB = (a+b+abs(a-b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
 Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
"""
linha1 = input().split(" ")

a, b, c = linha1

a = int(a)
b = int(b)
c = int(c)

MaiorAB = (a+b+abs(a-b)) / 2
MaiorFinal = (MaiorAB+c+abs(MaiorAB-c)) / 2

print(f"{MaiorFinal:.0f} eh o maior")
