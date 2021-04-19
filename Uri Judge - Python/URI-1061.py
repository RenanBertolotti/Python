"""Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e
terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que
ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração
deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai
começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss.
Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas,
indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto."""

dia_inicio = int(input("Dia "))
hora_inicio = input().split()
hora_inicio = [int(x) for x in hora_inicio]

dia_termino = int(input("Dia "))
dia_termino = int(dia_termino)
hora_termino = input().split()
hora_termino = [int(x) for x in hora_termino]

minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24

inicio = hora_inicio[0] + hora_inicio[1] * minuto_seg + hora_inicio[0] * hora_seg + dia_inicio * dia_seg
final = hora_termino[2] + hora_termino[1] * minuto_seg + hora_termino[0] * hora_seg + dia_termino * dia_seg

if inicio < final:
    tempo = final - inicio
    dias = int(tempo/dia_seg)
    tempo = tempo % dia_seg
    horas = int(tempo/hora_seg)
    tempo = tempo % hora_seg
    minutos = int(tempo/minuto_seg)
    tempo = tempo % minuto_seg
    segundos = tempo

    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))