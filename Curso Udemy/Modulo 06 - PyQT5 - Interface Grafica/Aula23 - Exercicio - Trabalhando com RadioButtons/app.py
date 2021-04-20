from PyQt5.QtWidgets import QMainWindow
from radiobutton import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.tamanho = None
        self.pagamento = None

        self.radioButton.toggled.connect(self.getTamanho)
        self.radioButton_2.toggled.connect(self.getTamanho)
        self.radioButton_3.toggled.connect(self.getTamanho)

        self.radioButton_4.toggled.connect(self.getPagamento)
        self.radioButton_5.toggled.connect(self.getPagamento)
        self.radioButton_6.toggled.connect(self.getPagamento)

    def getTamanho(self):
        self.tamanho = self.sender().text()
        self.imprimeCompra()

    def getPagamento(self):
        self.pagamento = self.sender().text()
        self.imprimeCompra()

    def imprimeCompra(self):
        if self.tamanho is not None and self.pagamento is not None:
            self.label_3.setText(f"Voce selecionou o tamanho: {self.tamanho}, e a forma de pagamamento:{self.pagamento}")
