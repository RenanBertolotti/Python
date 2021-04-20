from datetime import datetime
from calendar import mdays #import que retorna os dias do mes, quantos dias tem um mes
from locale import setlocale, LC_ALL #import para colocar ptbr em data

setlocale(LC_ALL, "") #funcao que set o idioma do programa a partir do idioma da IDE que esta utilizando
#OU setlocale(LC_ALL, "pt_BR.utf-8")

data = datetime.now()
formatacao1 = data.strftime("%A, %d de %B de %Y")
formatacao2 = data.strftime("%d/%m/%Y - %H:%M:%S")
print(formatacao1)
print(formatacao2)


mes_atual = int(data.strftime("%m"))
print(mes_atual, mdays[mes_atual])