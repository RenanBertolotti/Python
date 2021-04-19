"""Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste
nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com
 objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido."""

dias_ano = int(input())
ano = mes = dia = 0

if dias_ano >= 365:
    ano = int(dias_ano / 365)
    dias_ano = int(dias_ano % 365)
if dias_ano >= 30:
    mes = int(dias_ano/30)
    dias_ano = int(dias_ano % 30)
if dias_ano >1:
    dia = int(dias_ano/1)
    dias_ano = int(dias_ano/1)

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")