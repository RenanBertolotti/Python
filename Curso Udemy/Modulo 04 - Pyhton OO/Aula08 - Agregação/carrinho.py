class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserirProduto(self, Produto):
        self.produtos.append(Produto)

    def listaProdutos(self):
        for i in self.produtos:
            print(i.nome, i.valor)

    def somaTotal(self):
        soma = 0
        for i in self.produtos:
            soma += i.valor

        return soma
