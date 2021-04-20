
string = "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"

lista = [string[0:10] for numero in string if numero == '9']
lista_nova = '.'.join(lista)

print(lista)
print(lista_nova)