import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import oneplayer, gamefortwo
import start


class StartWindow(QtWidgets.QMainWindow, start.Ui_MainWindow):
    def __init__(self):
                # Это здесь нужно для доступа к переменным, методами т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна





class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')

    def choice_mod(self):
        self.w1 = StartWindow()
        self.w1.pushButton_2.clicked.connect(self.game_for_one)
        self.w1.pushButton_2.clicked.connect(self.w1.close)
        self.w1.pushButton_3.clicked.connect(self.game_for_two)
        self.w1.show()

    def game_for_one(self):

        self.w2 = oneplayer.OnePlayerApp()
        self.w2.show()

    def game_for_two(self):

        self.w2 = gamefortwo.TwoPlayerApp()
        self.w2.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MainWindow()
    w.choice_mod()
    sys.exit(app.exec_())