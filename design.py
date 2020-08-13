# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 838)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.955, y1:0.0511364, x2:0.091, y2:0.92, stop:0 rgba(157, 157, 157, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.readbutton = QtWidgets.QPushButton(self.centralwidget)
        self.readbutton.setEnabled(False)
        self.readbutton.setGeometry(QtCore.QRect(340, 660, 261, 71))
        self.readbutton.setMinimumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.readbutton.setFont(font)
        self.readbutton.setObjectName("readbutton")
        self.startbutton = QtWidgets.QPushButton(self.centralwidget)
        self.startbutton.setGeometry(QtCore.QRect(30, 750, 591, 61))
        self.startbutton.setMinimumSize(QtCore.QSize(301, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startbutton.setFont(font)
        self.startbutton.setObjectName("startbutton")
        self.imagelabel = QtWidgets.QLabel(self.centralwidget)
        self.imagelabel.setGeometry(QtCore.QRect(30, 20, 581, 361))
        self.imagelabel.setMinimumSize(QtCore.QSize(351, 281))
        self.imagelabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.imagelabel.setText("")
        self.imagelabel.setObjectName("imagelabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 390, 441, 51))
        self.label.setMinimumSize(QtCore.QSize(161, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.showmistakes = QtWidgets.QLCDNumber(self.centralwidget)
        self.showmistakes.setGeometry(QtCore.QRect(470, 390, 131, 51))
        self.showmistakes.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.showmistakes.setObjectName("showmistakes")
        self.writting_letter = QtWidgets.QTextEdit(self.centralwidget)
        self.writting_letter.setGeometry(QtCore.QRect(30, 660, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(9)
        self.writting_letter.setFont(font)
        self.writting_letter.setObjectName("writting_letter")
        self.show_word = QtWidgets.QTextEdit(self.centralwidget)
        self.show_word.setGeometry(QtCore.QRect(30, 450, 581, 81))
        self.show_word.setMinimumSize(QtCore.QSize(361, 51))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(14)
        self.show_word.setFont(font)
        self.show_word.setObjectName("show_word")
        MainWindow.setCentralWidget(self.centralwidget)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.readbutton.setText(_translate("MainWindow", "Ввод буквы"))
        self.startbutton.setText(_translate("MainWindow", "Начать игру"))
        self.label.setText(_translate("MainWindow", "Осталось попыток:"))
        self.action.setText(_translate("MainWindow", "Один игрок"))
        self.action_2.setText(_translate("MainWindow", "Два игрока"))
