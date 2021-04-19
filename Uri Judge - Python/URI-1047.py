"""Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” ."""

list = input().split(" ")
hora_inicial, minuto_inicial, hora_final, minuto_final = int(list[0]), int(list[1]), int(list[2]), int(list[3])

hora = 0
minuto = 0

if hora_inicial == hora_final == minuto_inicial == minuto_final:
    hora = 24
    minuto = 0

elif hora_inicial == hora_final:
    if minuto_inicial == minuto_final:
        hora = 24
        minuto = 0
    elif minuto_inicial > minuto_final:
        hora = 23
        minuto = (60 - minuto_inicial) + minuto_final
    else:
        hora = 0
        minuto = minuto_final - minuto_inicial

elif hora_inicial < hora_final:
    if hora_final - hora_inicial == 1:
        if minuto_inicial == minuto_final:
            hora = 1
            minuto = 0
        elif minuto_inicial < minuto_final:
            hora = 1
            minuto = minuto_inicial - minuto_final
        else:
            hora = 0
            minuto = (60 - minuto_inicial) + minuto_final
    elif minuto_inicial == minuto_final:
        hora = hora_final - hora_inicial
        minuto = 0
    elif minuto_inicial > minuto_final:
        hora = hora_final - hora_inicial - 1
        minuto = (60 - minuto_inicial) + minuto_final
    else:
        hora = hora_final - hora_inicial
        minuto = minuto_final - minuto_inicial
elif hora_inicial > hora_final:
    if (hora_final - hora_inicial) == 1 :
        if minuto_inicial == minuto_final:
            hora = 1
            minuto = 0
        elif minuto_inicial < minuto_final:
            hora = 1
            minuto = minuto_final - minuto_inicial
        else:
            hora = 1
            minuto = (60 - minuto_inicial) + minuto_final
    elif minuto_inicial == minuto_final:
        hora = (24 - hora_inicial) + hora_final
        minuto = 0
    elif minuto_inicial > minuto_final:
        hora = (23 - hora_inicial) + hora_final
        minuto = (60 - minuto_inicial) + minuto_final
    else:
        hora = (24 - hora_inicial) + hora_final
        minuto = minuto_final - minuto_inicial

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")