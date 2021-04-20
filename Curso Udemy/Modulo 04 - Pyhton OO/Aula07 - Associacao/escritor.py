class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    # Getter
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    # Setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
