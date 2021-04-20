"""
Try / Except em python


#Try/Except basico
try:
    a = 1/0
except NameError as erro:
    print("erro", erro)
except (IndexError, KeyError) as erro:
    print("erro de indice", erro)
except Exception as erro:
    print("ocorreu um erro inesperado")
else:
    print("Seu codigo foi afetuado com sucesso")
finally:
    print("Eu aconteço independende se der erro ou nao")

print("bora continuar")


###################################################################################
#Levantando exceçoes em Pyhton
def divide(n1,n2):
    if n2 == 0 :
        raise ValueError("n2 noa pode ser 0.")

    return n1 / n2


try:
    print(divide(2,0))
except ZeroDivisionError as erro:
    print("erro", erro)

"""
#######################################################################################
#Try/except como condicional

def convertenumero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while(True):
    numero = convertenumero(input("Digite um numero: "))

    if numero is not None:
        print(numero * 2)
    else:
        print("isso nao e numero.")
