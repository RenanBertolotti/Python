from cliente import Cliente


class ClienteJuridico(Cliente):
    def __init__(self, nome, idade, telefone, email, cpf, cnpj, nome_empresa):
        super().__init__(nome, idade, telefone, email, cpf)
        self.__cnpj = cnpj
        self.__nome_empresa = nome_empresa

    # Getter
    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def nome_empresa(self):
        return self.__nome_empresa

    # Getter
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        self.__nome_empresa = nome_empresa

    def __str__(self):
        return f"{self.nome} , {self.idade}, {self.telefone}, {self.email},{self.cpf}, {self.cnpj},{self.nome_empresa}"
