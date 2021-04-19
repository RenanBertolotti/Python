"""Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina
3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código
(até que seja válido). O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível,
conforme exemplo."""

al = 0
ga = 0
di = 0
x = 0

while x != 4:
	x = int(input())
	if x == 1:
		al = al + 1
	if x == 2:
		ga = ga + 1
	if x == 3:
		di = di + 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(al))
print('Gasolina: {}'.format(ga))
print('Diesel: {}'.format(di))
