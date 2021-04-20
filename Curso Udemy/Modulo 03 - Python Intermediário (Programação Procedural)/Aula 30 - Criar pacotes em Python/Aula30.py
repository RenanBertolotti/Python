#import vendas.calcpreco    #Assim,ou
#from vendas import calcpreco  #OU
from vendas.calcpreco import aumento, reducao


preco = 49.50
precoAumento = aumento(preco, 10, True)

print(precoAumento)


preconovo = 49.50
precoReducao = reducao(preconovo, 15)

print(precoReducao)