"""
Precisa instalar o Selenium no terminal:
"pipenv install selenium"

Depois entrar no site https://pypi.org/ e digitar selenium, apos, abrir o projeto e baixar o driver do navegador que desejar.
link do driver do Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads e baixar junto a versao do seu navegador
Depois de baixar o driver, mover ele pra pasta do seu projeto.
"""

from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = "chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(self.driver_path, options= self.options)

    def acessa(self, site):
        self.chrome.get(site)

    def clica_sing_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in') #procura pelo codigo o nome Sign in
            btn_sign_in.click()
        except Exception as e:
            print("Erro ao clicar em SingIN: ",e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id("login_field") #procura pelo id do input de login
            input_password = self.chrome.find_element_by_id("password") #procura pelo id do input de senha
            input_login.send_keys('renan.bertolotti@gmail.com') #envia os dados para colocar o email
            input_password.send_keys('#Renan#123')  #envia os dados para colocar o email

            btn_login = self.chrome.find_element_by_name("commit") #clica no botao com o nome no codigo "commit"
            btn_login.click() #clica
        except Exception as e:
            print("Erro ao fazer login: ",e)


    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex')
            perfil.click()
        except Exception as e:
            print("Erro ao clicar no perfil: ",e)


    def verifica_usuario(self, usuario):
        profiel_link = self.chrome.find_element_by_class_name("user-profile-link")
        profile_link_html = profiel_link.get_attribute('innerHTML')

        assert usuario in profile_link_html #checa se o usuario é igual o atributo do profile_link_html


    def clica_sair(self):
        try:
            btn_sair = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            btn_sair.click()
        except Exception as e:
            print("Erro ao sair: ",e)


    def sair(self):
        self.chrome.quit()


chrome = ChromeAuto()
chrome.acessa("https://github.com/")
chrome.clica_sing_in()
chrome.faz_login()
chrome.clica_perfil()
chrome.verifica_usuario("RenanBertolotti")

sleep(3)


