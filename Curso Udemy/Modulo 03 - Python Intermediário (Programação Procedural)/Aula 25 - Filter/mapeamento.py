from Aula25 import produtos, pessoas, lista


novalista = filter(lambda i: i['idade']>18, pessoas)

for i in novalista:
    print(i)