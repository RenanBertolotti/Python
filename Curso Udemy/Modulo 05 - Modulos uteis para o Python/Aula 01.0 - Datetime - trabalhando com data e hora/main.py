# https://docs.python.org/2/library/datetime.html -> documentaçao para a biblioteca datetime

from datetime import datetime, timedelta

data = datetime(2019,4,20, 10,53,20)  #instancia a data, sendo (ano,mes,dia, hora,minuto,segundo)
print(data) # mostra a data no padrao americano
print(data.strftime('%d/%m/%Y - %H:%M:%S')) #converte a data do padrao americano para a "Diretiva", essa "Diretiva" esta na documentação!


#strptime(str, fmt)
data2 = datetime.strptime('20/04/2019', '%d/%m/%Y') #instancia a data usando String com a "Diretiva" que voce quiser.
print(data2)
print(data2.timestamp())  #mostra o tempo em segundos

# .fromtimestamp cria uma data a partir dos segundos
data3 = datetime.fromtimestamp(1555729200.0) #instancia o tempo em segundos
print(data3)


data4 = datetime.strptime("20/04/1987 20:00:00","%d/%m/%Y %H:%M:%S")
print(data4)
data4 = data4 + timedelta(days=5, seconds=59)  #soma na data criada, precisa utilizar o timedelta()
data4 = data4 + timedelta(seconds=2*60*60)  #pode-se fazer caculo tambem, nesse caso foi adicionado 2 horas
print(data4.strftime("%d/%m/%Y %H:%M:%S"))


#Comparando datas!
d1 = datetime.strptime("20/04/1987 20:00:00","%d/%m/%Y %H:%M:%S")
d2 = datetime.strptime("25/04/1987 22:33:00","%d/%m/%Y %H:%M:%S")
print(d1.time())

dif = d2 - d1   #cria uma variavel que mostra a diferencia de dias e horas e minutos
print(dif)
print(dif.seconds) #mostra a diferencia convertido em segundos
print(dif.total_seconds()) #mostra a diferencia convertido em segundos
print(dif.days)  #mostra a diferencia convertido em dias
print(d2 > d1) #retona verdadeiro se a data for maior que a outra data

