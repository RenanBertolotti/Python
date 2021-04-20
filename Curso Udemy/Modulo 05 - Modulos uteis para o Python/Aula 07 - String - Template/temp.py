from string import Template
from datetime import datetime

                                #Utiliza o encoding para acentos e para o "ç"
with open("template.html", 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.substitute(nome="Renan", data=data_atual) #Gera erro caso nao use o placeholder $variavel
    # corpo_msg = template.safe_substitute(nome="Renan", data=data_atual) #Nao gera erro caso nao use o placeholder $variavel


print(corpo_msg)