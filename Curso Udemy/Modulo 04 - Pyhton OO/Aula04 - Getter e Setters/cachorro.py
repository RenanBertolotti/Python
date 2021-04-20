class Cachorro:

    def __init__(self, nome, raca, cor, idade):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade

    # Getter
    @property
    def nome(self):
        return self._nome

    @property
    def raca(self):
        return self._raca

    @property
    def cor(self):
        return self._cor

    @property
    def idade(self):
        return self._idade

    # Setter
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @raca.setter
    def raca(self, raca):
        self._raca = raca

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @idade.setter
    def idade(self, idade):
        self._idade = idade