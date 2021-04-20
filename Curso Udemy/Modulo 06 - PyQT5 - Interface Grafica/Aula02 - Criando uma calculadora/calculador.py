from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora do Reinan")
        self.setFixedSize(400, 400)

        self.centralWidget = QWidget()
        self.grid = QGridLayout(self.centralWidget)

        self.display = QLineEdit()
        self.display.setStyleSheet(
            "* {background: #FFF; color: #000; font-size:30px;}"
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.display.setDisabled(True)

        self.addBtn(QPushButton('7'), 1, 0, 1, 1)
        self.addBtn(QPushButton('8'), 1, 1, 1, 1)
        self.addBtn(QPushButton('9'), 1, 2, 1, 1)
        self.addBtn(QPushButton('+'), 1, 3, 1, 1)
        self.addBtn(QPushButton('C'), 1, 4, 1, 1, self.limpaTela, "background: red; color: #fff; font-weight:700;")

        self.addBtn(QPushButton('4'), 2, 0, 1, 1)
        self.addBtn(QPushButton('5'), 2, 1, 1, 1)
        self.addBtn(QPushButton('6'), 2, 2, 1, 1)
        self.addBtn(QPushButton('-'), 2, 3, 1, 1)
        self.addBtn(QPushButton('<-'), 2, 4, 1, 1, self.apagaUm, "background: #13823a; color: #fff; font-weight:700;")

        self.addBtn(QPushButton('1'), 3, 0, 1, 1)
        self.addBtn(QPushButton('2'), 3, 1, 1, 1)
        self.addBtn(QPushButton('3'), 3, 2, 1, 1)
        self.addBtn(QPushButton('/'), 3, 3, 1, 1)
        self.addBtn(QPushButton('('), 3, 4, 1, 1)

        self.addBtn(QPushButton('.'), 4, 0, 1, 1)
        self.addBtn(QPushButton('0'), 4, 1, 1, 1)
        self.addBtn(QPushButton(')'), 4, 2, 1, 1)
        self.addBtn(QPushButton('*'), 4, 3, 1, 1)
        self.addBtn(QPushButton('='), 4, 4, 1, 1, self.igual, "background: blue; color: #fff; font-weight:700;")

        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.setCentralWidget(self.centralWidget)

    def limpaTela(self):
        self.display.setText("")

    def apagaUm(self):
        self.display.setText(self.display.text()[:-1])

    def igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText("Conta invalida")

    def addBtn(self, botao, linha, coluna, tam1, tam2, funcao=None, style=None):
        self.grid.addWidget(botao, linha, coluna, tam1, tam2)

        if not funcao:
            botao.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + botao.text()
                )
            )
        else:
            botao.clicked.connect(funcao)

        if style:
            botao.setStyleSheet(style)

        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
