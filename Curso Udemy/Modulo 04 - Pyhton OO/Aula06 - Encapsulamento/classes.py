class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar(self):
        if not self.__dados:
            print("o dicionario esta vazio")
        else:
            for i, y in self.__dados['clientes'].items():
                print(i, y)

    def apaga_cliente(self, id):
        if id in self.__dados['clientes']:
            del self.__dados['clientes'][id]
        else:
            print("Usuario não existe na base de dados")