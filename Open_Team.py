# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Open_Team.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
cricket_db=sqlite3.connect('fantasy_cricket.db')
curs=cricket_db.cursor()

class Ui_Open_Team(object):   
    def setupUi(self, Open_Team):
        Open_Team.setObjectName("Open_Team")
        Open_Team.resize(400, 270)
        Open_Team.setMinimumSize(QtCore.QSize(400, 270))
        Open_Team.setMaximumSize(QtCore.QSize(400, 270))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Open_Team)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 60, 381, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(Open_Team)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Open_Team)
        QtCore.QMetaObject.connectSlotsByName(Open_Team)

    def retranslateUi(self, Open_Team):
        _translate = QtCore.QCoreApplication.translate
        Open_Team.setWindowTitle(_translate("Open_Team", "Open Team"))
        self.label.setText(_translate("Open_Team", "        Team Name  :"))
        self.pushButton.setText(_translate("Open_Team", "OK"))

    #ADDS ALL THE SAVED TEAMS TO COMBO BOX(OPEN WINDOW)
    def fillCombo(self):
        sql="SELECT name FROM teams;"
        curs.execute(sql)
        teams=curs.fetchall()
        self.comboBox.clear()
        for name in teams:
            self.comboBox.addItem(name[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Open_Team = QtWidgets.QWidget()
    ui = Ui_Open_Team()
    ui.setupUi(Open_Team)
    Open_Team.show()
    sys.exit(app.exec_())

