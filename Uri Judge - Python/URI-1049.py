"""Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo,
da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras
fornecidas.
                   |- carnivoro = aguia
            |--ave-|
            |      |- onivoro = pomba
vertebrado -|
            |           |-onivoro = homem
            |--mamifero-|
                        |-herbivoro = vaca

                       |- hematofago = pulga
             |--inseto-|
             |         |- herbivoro = lagarta
invertebrado-|
             |           |-hematofago = sanguessuga
             |--anelideo-|
                         |-onivoro = minhoca

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima,
com todas as letras minúsculas."""

linha1 = input()
linha2 = input()
linha3 = input()

if linha1 == "vertebrado":
    if linha2 == "ave":
        if linha3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if linha3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if linha2 == "inseto":
        if linha3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if linha3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")