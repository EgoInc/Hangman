import random, sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
import design
import startwindow
# ________________________________________________________________


showWord=['q']
WORD = ''
MISTAKES=1
alphabet=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
used = []

# ________________________________________________________________





class TwoPlayerApp(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):

        # Это здесь нужно для доступа к переменным, методами т.д. в файле design.py
        super().__init__()

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        QMessageBox.critical(self, "Указание", "Введите слово под рисунком и нажмите начать игру", QMessageBox.Ok)
        self.startbutton.clicked.connect(self.start)


    def setword2(self):
        global showWord, WORD
        WORD = self.show_word.toPlainText()
        if len(showWord) == 1:
            showWord = ['-'] * len(WORD)
        self.showword()



    def restart(self):
        global showWord, WORD, MISTAKES, used
        showWord = ['q']
        WORD = ''
        MISTAKES = 1
        used = []

    def showword(self):
        self.show_word.setText(''.join(showWord))





    def changeImage(self):
        image = QPixmap("D:/Hack/Виселица/image/{}.png".format(MISTAKES))
        self.imagelabel.setPixmap(image)


    def move(self, letter):
        global showWord, WORD,MISTAKES
        if letter in WORD:
            i = 0
            for each in WORD:
                if each==letter:
                    showWord[i]=letter
                i+=1
        else:
            MISTAKES += 1
            self.showmistakes.display(7-MISTAKES)
            self.changeImage()
        if MISTAKES==7:
            self.show_word.setText(WORD)
            QMessageBox.critical(self, "Ошибка ", "Вы проиграли!", QMessageBox.Ok)



        elif '-' not in showWord:
            self.show_word.setText(WORD)
            QMessageBox.critical(self, "Поздравляем ", "Вы выиграли!", QMessageBox.Ok)


        self.showword()


    def reading(self):
        global used

        letter = self.writting_letter.toPlainText()
        self.writting_letter.clear()
        if len(letter)==1 and letter in alphabet and letter not in used:
            self.move(letter.lower())
            used.append(letter)
        elif letter in used:

            QMessageBox.critical(self, "Ошибка ", "Вы уже вводили эту букву", QMessageBox.Ok)
        elif len(letter)!=1:
            QMessageBox.critical(self, "Ошибка ", "Введите одну букву", QMessageBox.Ok)
        elif not letter.isalpha():
            QMessageBox.critical(self, "Ошибка ", "Введите букву", QMessageBox.Ok)
        elif letter not in alphabet:
            QMessageBox.critical(self, "Ошибка ", "Буква должна быть из русского алфавита", QMessageBox.Ok)


    def start(self):


        self.restart()
        self.setword2()
        self.show_word.setReadOnly(True)
        self.readbutton.setEnabled(True)
        self.startbutton.setEnabled(False)



        self.changeImage()
        self.showmistakes.display(7 - MISTAKES)
        self.readbutton.clicked.connect(self.reading)


    def main():
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        window = TwoPlayerApp()  # Создаём объект класса TwoPlayerApp
        window.show()  # Показываем окно
        app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    TwoPlayerApp.main()