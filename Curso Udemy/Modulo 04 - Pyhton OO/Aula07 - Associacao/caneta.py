class Caneta:

    def __init__(self, marca):
        self.__marca = marca

    # Getter
    @property
    def marca(self):
        return self.__marca

    # Setter
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def escrever(self):
        print("Caneta esta escrevendo...")