from random import randint

class Pessoa:
    anoAtual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self):
        print(self.anoAtual - self.idade)

    @classmethod
    def porAnoNascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        return randint(00000, 10000)