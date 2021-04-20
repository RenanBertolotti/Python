class Endereco:
    def __init__(self, rua, numero, bairro, cidade):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade

    def __del__(self):
        print(f'{self.rua} FOI APAGADO')
