import json

with open("abc.json","r") as file:
    d1json  = file.read()
    d1json = json.loads(d1json)  #Loads converte para dicionario
    print(d1json)