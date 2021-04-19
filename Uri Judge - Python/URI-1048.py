"""A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 400.00          --- 15%
400.01 - 800.00     --- 12%
800.01 - 1200.00    --- 10%
1200.01 - 2000.00   --- 7%
Acima de 2000.00    --- 4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice
reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho"""

salario = float(input())

if salario <= 400.00:
    porcentagem = 15
    reajuste = (salario / 100) * porcentagem
    salario = salario + reajuste
elif salario <= 800.00:
    porcentagem = 12
    reajuste = (salario / 100) * porcentagem
    salario = salario + reajuste
elif salario <= 1200.00:
    porcentagem = 10
    reajuste = (salario / 100) * porcentagem
    salario = salario + reajuste
elif salario <= 2000.00:
    porcentagem = 7
    reajuste = (salario / 100) * porcentagem
    salario = salario + reajuste
else:
    porcentagem = 4
    reajuste = (salario / 100) * porcentagem
    salario = salario + reajuste

print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {porcentagem} %")
