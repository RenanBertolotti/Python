from datetime import datetime


class Pessoa:

    def __init__(self, nome, idade, comendo=False, falando=False, ano_nascimento=None):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.ano_nascimento = ano_nascimento

    def falar(self, assunto):
        if self.comendo:
            print("Não pode falar de boca cheia")
            return

        print(f"{assunto}")

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        return

    def parar_comer(self):
        if self.comendo is not True:
            print(f"{self.nome} não está comendo")
        else:
            self.comendo = False

    def get_ano_nascimento(self):
        ano_atual = int(datetime.strftime(datetime.now(), "%Y"))
        return ano_atual - self.ano_nascimento
