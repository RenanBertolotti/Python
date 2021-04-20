num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

# isnumeric isdigit isdecimal
# numero e positivos...
print(num1.isnumeric(), num2.isnumeric())  # Retorna true

##################### Usando IF ######################
if num1.isnumeric() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Nao pode converter char para int")

####################  Usando try Except  ##############
try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except:
    print("Error")
