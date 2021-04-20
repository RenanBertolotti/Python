"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo) #le o arquivo em forma de lista
    dados_Dicionario = csv.DictReader(arquivo) #le o arquivo em forma de dicionario

    #next(dados) - pula uma linha, nao mostra mais o nome das colunas, apenas os dados

    #for dado in dados:
    #    print(dado)

    for dado in dados_Dicionario:
        print(dado)


#########################################################################################################
#Nesse caso do CSV voce nao consegue acessar os dados apos fechar o arquivo,caso queira usar os dados apos fechar o arquivo
#é necessário fazer uma LISTA COMPREHENSIONS, segue o exemplo abaixo:
with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.reader(arquivo)] #le o arquivo em forma de lista
    #next(dados) - pula uma linha, nao mostra mais o nome das colunas, apenas os dados

    #for dado in dados:
    #    print(dado)

for dado in dados:
    print(dado)


############################################################################
#Exemplo de como criar um novo arquivo CSV:
with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)] #le o arquivo em forma de lista


with open('clientes2.csv', 'w+') as arquivo: #Cria o arquivo2
    escreve = csv.writer(arquivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    chave = dados[0].keys() #Pega as chaves do dicionario
    chave = list(chave) #converte o diconario em uma lista
    escreve.writerow(chave) #escreve a lista no novo arquivo csv

    for dado in dados:
        escreve.writerow([dado["Nome"], dado["Sobrenome"], dado["E-mail"], dado["Telefone"]])
