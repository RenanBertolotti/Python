import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url) #retorna todoo o codigo html da "url" para a string response
html = BeautifulSoup(response.text, 'html.parser') #retorna todoo o codigo html da "response" para a "html"

count = 0
#Apos fazer o codgio acima, é necessário achar a classe de algo que voce quer no html, para isso use o Inspecionar do google,
#apos achar a classe do html, faça um for para percorrer todoo o html que tenha a classe
for pergunta in html.select(".question-summary"):   #percorrer o html que tenha a classe "question-summary"
    titulo = pergunta.select_one('.question-hyperlink') #percorrer o html que tenha a classe ".question-hyperlink"
    data = pergunta.select_one(".relativetime")
    votos = pergunta.select_one(".vote-count-post")


    print(f"{data.text}, {titulo.text} ==== Votos:{votos.text}",sep='\t') #Mostra a data #Mostra todos os titulos
    count +=1

print(count)