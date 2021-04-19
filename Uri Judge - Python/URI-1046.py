"""Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar
em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo."""

digitado = input().split(" ")
num1, num2 = int(digitado[0]), int(digitado[1])

if num1 == 0 and num2 ==0:
    horatotal = 24

    print(f"O JOGO DUROU {horatotal} HORA(S)")
elif num1 > num2 or  num1 == num2:
    horatotal = (24 - num1) + num2
    print(f"O JOGO DUROU {horatotal} HORA(S)")
elif num2 > num1:
    horatotal = num2 - num1
    print(f"O JOGO DUROU {horatotal} HORA(S)")
