class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def porAnoNascimento(cls, nome, anoNascimento):
        idade = cls.ano_atual - anoNascimento
        return cls(nome, idade)