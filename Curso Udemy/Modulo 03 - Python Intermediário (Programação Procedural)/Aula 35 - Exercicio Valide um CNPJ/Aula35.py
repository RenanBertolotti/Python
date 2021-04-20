"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05
54 329 876 5432

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
--------------------------------------------------
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
------------------------------------------------------
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
#inicio
import cnpj

lista1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

while(True):
    cnpj_original = cnpj.removeCaracteres(input("Digite o seu cpf: "))

    if cnpj.sequencia(cnpj_original) == True:
        print("CNPJ sequencial, digite outro CNPJ")
    else:
        cnpj_copia = list(cnpj_original[0:-2])
        cnpj_copia = cnpj.converteInteiro(cnpj_copia)

        soma1 = cnpj.primeiraSoma(cnpj_copia,lista1)
        primeiro_digito = cnpj.primeiroDigito(soma1)

        cnpj_copia.append(primeiro_digito)
        soma2 = cnpj.segundaSoma(cnpj_copia, lista2)
        segundo_digito = cnpj.segundoDigito(soma2)

        cnpj_copia.append(segundo_digito)
        cnpj_copia = cnpj.reconverteStr(cnpj_copia)

        if cnpj.comparaCnpj(cnpj_original,cnpj_copia) == True:
            print("CNPJ VALIDO")
        else:
             print("CNPJ INVALIDO")