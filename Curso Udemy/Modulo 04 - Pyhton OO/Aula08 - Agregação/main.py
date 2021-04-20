from carrinho import CarrinhoDeCompras
from produto import Produto

carrinho = CarrinhoDeCompras()
produto1 = Produto("Chocolate", 10.00)
produto2 = Produto("Macarrão", 15.00)
produto3 = Produto("Açai", 18.70)

carrinho.inserirProduto(produto1)
carrinho.inserirProduto(produto2)
carrinho.inserirProduto(produto3)

carrinho.listaProdutos()
print(carrinho.somaTotal())