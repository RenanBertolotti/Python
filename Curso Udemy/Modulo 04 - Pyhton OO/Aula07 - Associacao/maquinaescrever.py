class MaquinaEscrever:

    def __init__(self, marca):
        self.__marca = marca

    # Getter
    @property
    def marca(self):
        return self.__marca

    # Getter
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def escrever(self):
        print("Maquina esta escrevendo...")