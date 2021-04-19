"""Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir,
 calcule e mostre o valor da conta a pagar.

    codigo  --- Especificação    --- preco
    1   ------  Cachorro QUente ---- R$ 4.00
    2   ------  X-Salada        ---- R$ 4.50
    3   ------  X-Bacon         ---- R$ 5.00
    4   ------  Torrada Simples ---- R$ 2.00
    5   ------  Refrigerante    ---- R$ 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela
acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
"""

codigo, qtd = input().split(" ")
codigo, qtd = int(codigo), int(qtd)

resultado = 0.0

if codigo == 1:
    resultado = 4 * qtd
elif codigo == 2:
    resultado = 4.50 * qtd
elif codigo == 3:
    resultado = 5.00 * qtd
elif codigo == 4:
    resultado = 2.00 * qtd
elif codigo == 5:
    resultado = 1.50 * qtd

print(f"Total: R$ {resultado:.2f}")
