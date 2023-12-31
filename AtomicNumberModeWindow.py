# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AtomicNumberModeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import random

with open('Periodic Table of Elements.csv', mode='r+') as f:
    reader = csv.reader(f)
    name = []
    score = int()
    hp = 3
    for data in reader:
        name.append([data[0],data[1]])
    name.remove(['AtomicNumber', 'Element'])

    class Ui_AtomicNumberModeWindow(object):
        def setupUi(self, AtomicNumberModeWindow):
            AtomicNumberModeWindow.setObjectName("AtomicNumberModeWindow")
            AtomicNumberModeWindow.resize(1000, 800)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            AtomicNumberModeWindow.setWindowIcon(icon)
            AtomicNumberModeWindow.setStyleSheet("background-image: url(:/images/AtomicNumberModeWindow.png);")
            self.centralwidget = QtWidgets.QWidget(AtomicNumberModeWindow)
            self.centralwidget.setObjectName("centralwidget")
            AtomicNumberModeWindow.setCentralWidget(self.centralwidget)
            self.centralwidget.setObjectName("centralwidget")
            self.lcd_score = QtWidgets.QLCDNumber(self.centralwidget)
            self.lcd_score.setGeometry(QtCore.QRect(850, 50, 101, 41))
            self.lcd_score.setStyleSheet("background-image: url(:/images/white screen.jpg);")
            self.lcd_score.setObjectName("lcd_score")
            self.lcd_hp = QtWidgets.QLCDNumber(self.centralwidget)
            self.lcd_hp.setGeometry(QtCore.QRect(850, 110, 101, 41))
            self.lcd_hp.setStyleSheet("background-image: url(:/images/white screen.jpg);")
            self.lcd_hp.setDigitCount(5)
            self.lcd_hp.setProperty("intValue", 3)
            self.lcd_hp.setObjectName("lcd_hp")
            self.Element_name = QtWidgets.QLabel(self.centralwidget)
            self.Element_name.setGeometry(QtCore.QRect(400, 200, 161, 81))
            self.Element_name.setStyleSheet("background-image: url(:/images/white screen.jpg);")
            self.Element_name.setObjectName("Element_name")
            self.input_element_name = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_element_name.setGeometry(QtCore.QRect(350, 350, 261, 31))
            self.input_element_name.setStyleSheet("background-image: url(:/images/white screen.jpg);")
            self.input_element_name.setObjectName("input_element_name")
            self.input_element_name.setPlainText("Example : 1 (Hydrogen) ")
            self.summit_button = QtWidgets.QPushButton(self.centralwidget)
            self.summit_button.setGeometry(QtCore.QRect(440, 400, 91, 31))
            self.summit_button.setObjectName("summit_button")
            self.summit_button.setStyleSheet("color: rgb(255, 255, 255);")

            self.start_button = QtWidgets.QPushButton(self.centralwidget)
            self.start_button.setGeometry(QtCore.QRect(200, 200, 91, 31))
            self.start_button.setStyleSheet("color: rgb(255, 255, 255);")
            self.start_button.setObjectName("start_button")
            # Send signal t StartGame function.
            self.start_button.clicked.connect(self.StartGame)
            self.summit_button.clicked.connect(self.CheckAnswer)
            self.retranslateUi(AtomicNumberModeWindow)
            QtCore.QMetaObject.connectSlotsByName(AtomicNumberModeWindow)

        def retranslateUi(self, AtomicNumberModeWindow):
                _translate = QtCore.QCoreApplication.translate
                AtomicNumberModeWindow.setWindowTitle(_translate("AtomicNumberModeWindow", "Elementium"))
                self.start_button = QtWidgets.QPushButton(self.centralwidget)
                self.start_button.setGeometry(QtCore.QRect(200, 200, 91, 31))
                self.start_button.setStyleSheet("color: rgb(255, 255, 255);")
                self.start_button.setObjectName("start_button")
                # Send signal t StartGame function.
                self.start_button.clicked.connect(self.StartGame)
                self.summit_button.clicked.connect(self.CheckAnswer)

                AtomicNumberModeWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(AtomicNumberModeWindow)
                QtCore.QMetaObject.connectSlotsByName(AtomicNumberModeWindow)

        def retranslateUi(self, SymbolsModeWindow):
            _translate = QtCore.QCoreApplication.translate
            SymbolsModeWindow.setWindowTitle(_translate("SymbolsModeWindow", "Elementium"))
            self.summit_button.setText(_translate("SymbolsModeWindow", "SUMMIT"))
            self.start_button.setText("START")

        def StartGame(self):
            global hp, score, random_element
            _translate = QtCore.QCoreApplication.translate
            if hp > 0 :
                random_element = random.choice(name)  # Choose a random element name from your list
                self.Element_name.setText(_translate("SymbolsModeWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{random_element[1]}</span></p></body></html>"))
            else:
                self.Element_name.setText(_translate("SymbolsModeWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Game Over</span></p></body></html>"))
            print(random_element)

        def CheckAnswer(self):
            global hp, score, random_element 
            answer = self.input_element_name.toPlainText()
            if answer.lower() == random_element[0].lower():
                score += 1
                self.lcd_score.display(score)
            else:
                hp -= 1
                self.lcd_hp.display(hp)

                
            self.input_element_name.setPlainText('')
            self.StartGame()

import AtomicNumberModeWindow_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AtomicNumberModeWindow = QtWidgets.QMainWindow()
    ui = Ui_AtomicNumberModeWindow()
    ui.setupUi(AtomicNumberModeWindow)
    AtomicNumberModeWindow.show()
    sys.exit(app.exec_())
