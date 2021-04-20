"""O governo estadual estará fazendo um programa de bolsa de estudos para o ensino superior e para que
o aluno possa se inscrever é necessário possuir todos os requisitos abaixo:
- Ter ultrapassado 500 pontos na redação do ENEM.
- Ter um salário mensal abaixo de R$ 1800,00.
- Ter nota acima de 6 no SARESP ou ter nota acima de 600 na
nota geral do ENEM.
Com base nas informações acima, faça o algoritmo que colete
a nota da redação do ENEM,
nota geral do ENEM,
salário mensal e
nota do SARESP,
em seguida, informe se o aluno está “apto” a se inscrever ou “não apto”.
Utilize obrigatoriamente operadores lógicos.

"""

nota_redacao_enem = int(input("Digite a sua nota da redação do Enem: "))
nota_geral_enem = int(input("Digite a sua nota geral do Enem: "))
salario_mensal = float(input("Digite o seu salário mensal: "))
nota_saresp = float(input("Digite a sua nota do SARESP: "))

if (nota_redacao_enem > 500) and (salario_mensal < 1800.00) and (nota_saresp > 6 or nota_geral_enem > 600):
    print("Apto")
else:
    print("Não apto")
