from pessoa import Pessoa

p1 = Pessoa("Renan", 22, False, False, 1998)
p2 = Pessoa("Ivan", 23)

print(p1)
print(p2)

p2.comer("chocolate")
p2.comer("maca")
p2.parar_comer()
p2.falar("Ola mundo")

print(p1.ano_nascimento)
print(p1.get_ano_nascimento())