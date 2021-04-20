from PyQt5.QtWidgets import QMainWindow
from formulario import Ui_MainWindow
from pessoa import Pessoa


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.listaPessoas = []

        self.pushButton.clicked.connect(self.cadastrar)
        self.pushButton_2.clicked.connect(self.listaCadastro)

    def cadastrar(self):
        print("Cadastrado com Sucesso")
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())

        self.listaPessoas.append(Pessoa(self.lineEdit.text(), self.lineEdit_2.text()))

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def listaCadastro(self):
        try:
            for pessoa in self.listaPessoas:
                print("Pessoa -----")
                print(pessoa)
                print("-------------")
        except Exception as e:
            print(e)