from endereco import Endereco

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insereEndereco(self, rua, numero, bairro, cidade):
        self.endereco.append(Endereco(rua, numero, bairro, cidade))

    def listaEndereco(self):
        for i in self.endereco:
            print(i.rua, i.numero, i.bairro, i.cidade)

    def __del__(self):
        print(f"{self.nome} FOI APAGADO")