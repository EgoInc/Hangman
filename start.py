# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 420)
        MainWindow.setMinimumSize(QtCore.QSize(589, 420))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.955, y1:0.0511364, x2:0.091, y2:0.92, stop:0 rgba(157, 157, 157, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 561, 91))
        self.label.setMinimumSize(QtCore.QSize(521, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 330, 271, 51))
        self.pushButton_2.setMinimumSize(QtCore.QSize(271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 224, 201);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 330, 271, 51))
        self.pushButton_3.setMinimumSize(QtCore.QSize(271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 224, 201);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Выберете режим игры"))
        self.pushButton_2.setText(_translate("MainWindow", "Один игрок"))
        self.pushButton_3.setText(_translate("MainWindow", "Два игрока"))
