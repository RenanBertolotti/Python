class Teclado:

    def __init__(self, marca, modelo, n_teclas, mecanico):
        self.marca = marca
        self.modelo = modelo
        self.n_teclas = n_teclas
        self.mecanico = mecanico

    # Getter
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def n_teclas(self):
        return self._n_teclas

    @property
    def mecanico(self):
        return self._mecanico

    # Setter
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @n_teclas.setter
    def n_teclas(self, n_teclas):
        self._n_teclas = n_teclas

    @mecanico.setter
    def mecanico(self, mecanico):
        self._mecanico = mecanico
