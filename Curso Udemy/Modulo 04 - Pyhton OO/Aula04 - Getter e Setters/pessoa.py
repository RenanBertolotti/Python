class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            nome = nome.title()

        self._nome = nome

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, preco):
        if isinstance(preco, str):
            preco = float(preco.replace("R$", ''))

        self._preco = preco
