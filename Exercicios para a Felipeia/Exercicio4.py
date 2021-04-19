
def QntVezesDivisivel(x, y):
    resultado = y
    cont = 0

    if(x > y):
        return -1

    while(resultado >= x):
        cont += 1
        resultado = resultado / x;
        if(resultado > mat):
            break

    return int(resultado)


if __name__ == "__main__":
    numero1 = int(input())
    numero2 = int(input())

    resultado = QntVezesDivisivel(numero1, numero2)

    print(f"O numero {numero2} eh divisivel por {numero1} em: {resultado} vezes")
