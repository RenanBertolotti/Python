"""
CPF = 168.995.350-09
--------------------------------------------------
1 * 10                   # 1 * 11 = 11 <-
6 * 9                    # 6 * 10 = 60
8 * 8                    # 8 * 9 = 72
9 * 7                    # 9 * 8 = 72
9 * 6                    # 9 * 7 = 63
5 * 5                    # 5 * 6 = 30
3 * 4                    # 3 * 5 = 15
5 * 3                    # 5 * 4 = 20
0 * 2                    # 0 * 3 = 0
                         # 0 * 2 = 0
    297                  #          343
11 - (297 % 11 =11       #      11 - (343 % 11) = 9
11 > 9 = 0               #
(Se for menor, recebe o) #
(valor da conta        ) #
Digito 1 =0              #    Digito 2 = 9
"""

cpf = input("Digite o seu CPF: ")

if not cpf:
    print("Digite um cpf valido")
else:
    cpfCopia = cpf.split("-",1)                                  # 443.063.478 , 50
    numeroDigitos = cpfCopia[1]                                  # 50
    numeroAntes = cpfCopia[0].split('.')                         # 443, 063, 478
    numeroAntes = numeroAntes[0]+numeroAntes[1]+numeroAntes[2]   # 443063478


# ----------------------------Tratando a 1ª parte --------------------------------------
    soma = 0

    for i,y in enumerate(range(10,1,-1)):
         soma += int(numeroAntes[i]) * y

    soma = 11 - (soma % 11)

    if soma > 9:
        soma = 0

    digitoFinal1 = soma

# ----------------------------Tratando a 2ª parte --------------------------------------
    numeroAntes = numeroAntes + str(soma)   # 168995350 + o resultado da 1 parte

    soma = 0

    for i,y in enumerate(range(11,1,-1)):
        soma += int(numeroAntes[i]) * y

    soma = 11 - (soma % 11)

    if soma > 9:
        soma = 0

    digitoFinal2 = soma

# -----------------------------Validando o CPF ----------------------------------------------
    cpfDigitado = cpfCopia[0].split('.')
    cpfDigitado = cpfDigitado[0] + cpfDigitado[1] + cpfDigitado[2] + cpfCopia[1]
    novo_cpf = numeroAntes[:-1] + str(digitoFinal1) + str(digitoFinal2)

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia =  str(novo_cpf[0]) * len(cpf)
    sequencia = sequencia[:-3]

    if cpfDigitado == novo_cpf and not cpfDigitado == sequencia:
        print("CPF valido")
    else:
        print("CPF invalido")