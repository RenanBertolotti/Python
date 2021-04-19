
def divisivel(x, y):
    if y % x ==0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    numero1 = int(input())
    numero2 = int(input())

    print(f"Numero {numero1} e divisivel por {numero2}?: ")
    resposta = divisivel(numero1, numero2)
    if resposta == 1:
        print("É divisivel")
    else:
        print("Não é divisível")
