"""A Universidade do Futuro aceita alunos por meio da nota do ENEM. Para ingressar com bolsa o aluno
deverá atingir uma determinada nota de corte, caso contrário, fará o pagamento integral do curso. No
curso de Engenharia Civil a nota de corte segue a tabela abaixo:
Nota de corte do ENEM Bolsa de estudos

Abaixo de 500 Não terá bolsa
De 500 até 600 pontos Terá bolsa FIES
De 600 até 700 pontos Terá bolsa FIES ou PROUNI
Acima de 700 pontos Terá bolsa FIES, PROUNI ou SISU"""

print("Bem vindo")
nota = input("Digite a sua nota do Enem: ")
nota = int(nota)

if nota < 500:
    print("Não terá bolsa")
elif nota >= 500 and nota < 600:
    print("Terá bolsa FIES")
elif nota >= 600 and nota < 700:
    print("Terá bolsa FIES ou PROUNI")
else:
    print("Terá bolsa FIES, PROUNI ou SISU")

