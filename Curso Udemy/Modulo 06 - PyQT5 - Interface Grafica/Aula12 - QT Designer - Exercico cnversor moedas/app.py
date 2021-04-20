from PyQt5.QtWidgets import QMainWindow
from conversor import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnConverter.clicked.connect(self.converter)

    def converter(self):
        try:
            valor = float(self.valorParaConverter.text())
        except Exception as e:
            pass

        print(self.cbConverterDe.currentText())

        if self.cbConverterDe.currentText() == 'Real(BRL)':
            if self.cbConverterPara.currentText() == "Dolar dos Estados Unidos(USD)":
                dolar = 5.46
                convertido = (valor / dolar)

                self.valorConvertido.setText(f"{convertido:.2f}")
                print(convertido)
            elif self.cbConverterPara.currentText() == "Iene(JPY)":
                iene = 0.052
                convertido = valor/iene

                self.valorConvertido.setText(f'{convertido:.2f}')
                print(convertido)
            else:
                print("o valor do real é R$1.00")
                self.valorConvertido.setText("R$1.00")
        elif self.cbConverterDe.currentText() == "Dolar dos Estados Unidos(USD)":
            if self.cbConverterPara.currentText() == "Real(BRL)":
                real = 5.46
                convertido = valor * real

                self.valorConvertido.setText(f"{convertido:.2f}")
