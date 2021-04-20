#Lists, tuples, str -> Sequences -> Iteravel
nome = "Renan Bertolotti"

for letra in nome:
    print(letra)

#usando esta metodo de cima a "letra" seria o indice de cada caractere,para que isso nao aconteça tem que utilizar
#o iter
print("#" * 80,"\n")

nome = "Renan Bertolotti"
iterador = iter(nome)

for i in iterador:
    print(i)



print(iterador)
