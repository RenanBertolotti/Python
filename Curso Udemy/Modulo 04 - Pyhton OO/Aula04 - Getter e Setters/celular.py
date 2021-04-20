class Celular:

    def __init__(self, marca, modelo, ram, memoria):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.memoria = memoria


    # Getter
    @property
    def marca(self):
        return self._marca

    # Getter
    @property
    def modelo(self):
        return self._modelo

    # Getter
    @property
    def ram(self):
        return self._ram

    # Getter
    @property
    def memoria(self):
        return self._memoria


    # Setter
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @ram.setter
    def ram(self, ram):
        self._ram = ram

    @memoria.setter
    def memoria(self, memoria):
        self._memoria = memoria