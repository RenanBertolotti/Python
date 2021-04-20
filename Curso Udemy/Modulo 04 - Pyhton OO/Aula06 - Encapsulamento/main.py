"""
public    = variavel
private   = __variavel
protected = _variavel
"""
from classes import BaseDeDados

bd = BaseDeDados()

bd.inserir(1, "Renan")
bd.inserir(2, "Otavio")
bd.inserir(3, "Maria")
bd.inserir(4, "Pai")
bd.inserir(5, "Ivan")

bd.apaga_cliente(3)

bd.listar()
