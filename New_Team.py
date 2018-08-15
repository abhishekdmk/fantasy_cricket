# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Team.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_New_Team(object):
    def __init__self(self):
        self.team_name1='hellocheck'
    def setupUi(self, New_Team):
        New_Team.setObjectName("New_Team")
        New_Team.resize(400, 300)
        New_Team.setMinimumSize(QtCore.QSize(400, 300))
        New_Team.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtWidgets.QLabel(New_Team)
        self.label.setGeometry(QtCore.QRect(120, 100, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(New_Team)
        self.lineEdit.setGeometry(QtCore.QRect(80, 150, 250, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(New_Team)
        self.pushButton.setGeometry(QtCore.QRect(160, 210, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(New_Team)
        QtCore.QMetaObject.connectSlotsByName(New_Team)

    def retranslateUi(self, New_Team):
        _translate = QtCore.QCoreApplication.translate
        New_Team.setWindowTitle(_translate("New_Team", "New Team"))
        self.label.setText(_translate("New_Team", "Enter Team Name"))
        self.pushButton.setText(_translate("New_Team", "OK"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_Team = QtWidgets.QWidget()
    ui = Ui_New_Team()
    ui.setupUi(New_Team)
    New_Team.show()
    sys.exit(app.exec_())

