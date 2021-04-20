"""
While / Else
contadores
acumuladores
"""

cont = 0
acumulador = 0

while cont < 100:
    print(cont)
    cont += 1

while acumulador < 100:
    print(acumulador , cont)

    # if cont > 5 :  # se tiver o BREAK, NAO IRA EXECUTAR O ELSE!!!
    #     break

    acumulador = acumulador + cont
    cont += 1
else:       # Consegue usar o no while, quando o while for FALSO
    print("abacou")  # executa uma unica vez e para tanto o While como o Else

