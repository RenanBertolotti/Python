"""
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa,
seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

Entrada
O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

Saída
Imprima a saída conforme o exemplo fornecido.
"""
casos_teste = int(input())

contador = 1
valor1 = 1

for i in range(1, casos_teste+1):
    valor1 = i*i
    valor2 = i*i*i

    print(i, valor1, valor2)

    valor3 = valor1+1
    valor4 = valor2+1

    print(i, valor3, valor4)


