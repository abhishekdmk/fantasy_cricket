# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate_Score.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
cricket_db=sqlite3.connect('fantasy_cricket.db')
cur=cricket_db.cursor()

class Ui_Evaluate(object):
    def setupUi(self, Evaluate):
        Evaluate.setObjectName("Evaluate")
        Evaluate.resize(800, 688)
        Evaluate.setMinimumSize(QtCore.QSize(800, 688))
        Evaluate.setMaximumSize(QtCore.QSize(800, 688))
        Evaluate.setStyleSheet("background-color:#b3b3b3")
        self.title = QtWidgets.QLabel(Evaluate)
        self.title.setGeometry(QtCore.QRect(80, 40, 650, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAutoFillBackground(False)
        self.title.setObjectName("title")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Evaluate)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 110, 581, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(140)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combo_team = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo_team.setObjectName("combo_team")
        self.horizontalLayout.addWidget(self.combo_team)
        self.combo_match = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo_match.setObjectName("combo_match")
        self.horizontalLayout.addWidget(self.combo_match)
        self.line = QtWidgets.QFrame(Evaluate)
        self.line.setGeometry(QtCore.QRect(70, 200, 650, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.players = QtWidgets.QLabel(Evaluate)
        self.players.setGeometry(QtCore.QRect(110, 230, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.players.setFont(font)
        self.players.setObjectName("players")
        self.list_players = QtWidgets.QListWidget(Evaluate)
        self.list_players.setGeometry(QtCore.QRect(110, 270, 250, 320))
        self.list_players.setStyleSheet("background-color:white;")
        self.list_players.setObjectName("list_players")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Evaluate)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(450, 220, 231, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.points = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.points.setFont(font)
        self.points.setObjectName("points")
        self.horizontalLayout_2.addWidget(self.points)
        self.total_points = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.total_points.setFont(font)
        self.total_points.setStyleSheet("color:red;")
        self.total_points.setObjectName("total_points")
        self.horizontalLayout_2.addWidget(self.total_points)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 10)
        self.list_points = QtWidgets.QListWidget(Evaluate)
        self.list_points.setGeometry(QtCore.QRect(450, 270, 250, 320))
        self.list_points.setStyleSheet("background-color:white;")
        self.list_points.setObjectName("list_points")
        self.pushButton = QtWidgets.QPushButton(Evaluate)
        self.pushButton.setGeometry(QtCore.QRect(340, 640, 130, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Evaluate)
        QtCore.QMetaObject.connectSlotsByName(Evaluate)

    def retranslateUi(self, Evaluate):
        _translate = QtCore.QCoreApplication.translate
        Evaluate.setWindowTitle(_translate("Evaluate", "Evaluate Score"))
        self.title.setText(_translate("Evaluate", "                           Evaluate the Performance of your Fantacy Team"))
        self.players.setText(_translate("Evaluate", "Players"))
        self.points.setText(_translate("Evaluate", "Points  :"))
        self.total_points.setText(_translate("Evaluate", "0"))
        self.pushButton.setText(_translate("Evaluate", "Calculate Score"))

    #FILL ALL THE FIELDS IN EVALAUTE WINDOW
    def fillEvaluateWindow(self):
        self.list_points.clear()
        self.total_points.setText('0')
        sql1="SELECT name FROM teams;"
        sql2="SELECT match_id FROM match_played;"
        cur.execute(sql1)
        teams=cur.fetchall()
        self.combo_team.clear()
        for name in teams:
            self.combo_team.addItem(name[0])
        cur.execute(sql2)
        matches=cur.fetchall()
        self.combo_match.clear()
        for name in matches:
            self.combo_match.addItem(name[0])        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evaluate = QtWidgets.QWidget()
    ui = Ui_Evaluate()
    ui.setupUi(Evaluate)
    Evaluate.show()
    sys.exit(app.exec_())

