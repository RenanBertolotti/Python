"""
Pode acontecer de dar erro de envio pela conta Google por a mesma é bloqueada para envio por codigo, para resolver é ,
necessário entrar nesse link com a sua conta logada e ativar a opc "Permitir aplicativos menos seguros:"

https://myaccount.google.com/u/1/lesssecureapps
"""

from string import Template
from datetime import datetime
from dados_email import *

# Imports obrigatorios para enviar o email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib



                                #Utiliza o encoding para acentos e para o "ç"
with open("template.html", 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.substitute(nome="Gabriel", data=data_atual) #Gera erro caso nao use o placeholder $variavel
    # corpo_msg = template.safe_substitute(nome="Renan", data=data_atual) #Nao gera erro caso nao use o placeholder $variavel


msg = MIMEMultipart()
msg['From'] = "Renan Bertolotti" #Meu nome
msg['To'] = email_cliente1 #Email do cliente
msg["Subject"] = 'Atenção: este é um e-mail de testes.'


#para escrever uma mensagem é so usar a funcao abaixo e escrever a mensagem como argumento
#corpo = MIMEText("ola Mundo")
#Ou entao pode enviar o corpo html utilizando templates tambem, para isso fazer:
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)


#Enviando imagem em anexo
with open(r'C:\Users\Reinan\Pictures\.thumbnails\7140.jpg', 'rb') as imagem:
    imagem = MIMEImage(imagem.read())
    msg.attach(imagem)


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("pedrochiccozinho@gmail.com", "#Renan#123")
        smtp.send_message(msg)
        print("Email enviado com sucesso.")
    except Exception as e:
        print("Email nao enviado...")
        print("Erro:", e)

