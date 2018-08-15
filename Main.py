# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#IMPORTING CLASSES FOR DIFFERENT WIDGETS WINDOW
from New_Team import Ui_New_Team
from Open_Team import Ui_Open_Team
from Evaluate_Score import Ui_Evaluate
from Dialog_Save import Ui_Dialog

#IMPORTING FUNCTIONS TO CALCULATE PLAYER'S POINTS
from calculate_points import batscore,bowlscore

#ESTABLISH CONNECTION WITH CREATED DATABASE
import sqlite3
cricket_db=sqlite3.connect('fantasy_cricket.db')
curs=cricket_db.cursor()


class Ui_MainWindow(object):
    def __init__(self):
        #OBJECT CREATION FOR NEW_TEAM WINDOW
        self.New_Team=QtWidgets.QWidget()
        self.new_ui=Ui_New_Team()
        self.new_ui.setupUi(self.New_Team)

        #OBJECT CREATION FOR OPEN_TEAM WINDOW
        self.Open_Team=QtWidgets.QWidget()
        self.open_ui=Ui_Open_Team()
        self.open_ui.setupUi(self.Open_Team)

        #OBJECT CREATION FOR EVALUATE WINDOW
        self.Evaluate_Team=QtWidgets.QWidget()
        self.evaluate_ui=Ui_Evaluate()
        self.evaluate_ui.setupUi(self.Evaluate_Team)

        ##OBJECT CREATION FOR SAVE CONFIRMATION DIALOG BOX
        self.Dialog_Save=QtWidgets.QDialog()
        self.save_ui=Ui_Dialog()
        self.save_ui.setupUi(self.Dialog_Save)

        #RETRIEVING PLAYERS INFORMATTION FROM DATABASE
        sql_bat="SELECT player,value from stats WHERE ctg='BAT';"
        sql_bow="SELECT player,value from stats WHERE ctg='BWL';"
        sql_ar="SELECT player,value from stats WHERE ctg='AR';"
        sql_wk="SELECT player,value from stats WHERE ctg='WK';"
        curs.execute(sql_bat)
        self.batsman_names=curs.fetchall()
        curs.execute(sql_bow)
        self.bowler_names=curs.fetchall()
        curs.execute(sql_ar)
        self.allrounder_names=curs.fetchall()
        curs.execute(sql_wk)
        self.wk_names=curs.fetchall()
            

    def setupUi(self, MainWindow):
        self.bat_count=0
        self.bow_count=0
        self.ar_count=0
        self.wk_count=0
        self.total_count=0
        self.points_available=800
        self.points_used=0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 750)
        MainWindow.setMinimumSize(QtCore.QSize(900, 750))
        MainWindow.setMaximumSize(QtCore.QSize(900, 750))
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_Your_Selections = QtWidgets.QFrame(self.centralwidget)
        self.frame_Your_Selections.setGeometry(QtCore.QRect(40, 39, 811, 111))
        self.frame_Your_Selections.setStyleSheet("background-color:rgb(230, 230, 230)")
        self.frame_Your_Selections.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Your_Selections.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Your_Selections.setObjectName("frame_Your_Selections")
        self.Your_Selections = QtWidgets.QLabel(self.frame_Your_Selections)
        self.Your_Selections.setGeometry(QtCore.QRect(20, 10, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Your_Selections.setFont(font)
        self.Your_Selections.setObjectName("Your_Selections")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_Your_Selections)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 791, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BAT_count = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.BAT_count.setFont(font)
        self.BAT_count.setStyleSheet("")
        self.BAT_count.setObjectName("BAT_count")
        self.horizontalLayout.addWidget(self.BAT_count)
        self.BOW_count = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.BOW_count.setFont(font)
        self.BOW_count.setObjectName("BOW_count")
        self.horizontalLayout.addWidget(self.BOW_count)
        self.AR_count = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.AR_count.setFont(font)
        self.AR_count.setObjectName("AR_count")
        self.horizontalLayout.addWidget(self.AR_count)
        self.WK_count = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.WK_count.setFont(font)
        self.WK_count.setObjectName("WK_count")
        self.horizontalLayout.addWidget(self.WK_count)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 170, 251, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Points_available = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Points_available.setFont(font)
        self.Points_available.setObjectName("Points_available")
        self.horizontalLayout_2.addWidget(self.Points_available)
        self.points_available_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.points_available_count.setFont(font)
        self.points_available_count.setStyleSheet("color:rgb(33, 218, 255)")
        self.points_available_count.setWordWrap(False)
        self.points_available_count.setObjectName("points_available_count")
        self.horizontalLayout_2.addWidget(self.points_available_count)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(500, 170, 211, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Points_used = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Points_used.setFont(font)
        self.Points_used.setObjectName("Points_used")
        self.horizontalLayout_3.addWidget(self.Points_used)
        self.points_used_count = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.points_used_count.setFont(font)
        self.points_used_count.setStyleSheet("color:rgb(33, 218, 255)")
        self.points_used_count.setObjectName("points_used_count")
        self.horizontalLayout_3.addWidget(self.points_used_count)
        self.frame_players_available = QtWidgets.QFrame(self.centralwidget)
        self.frame_players_available.setGeometry(QtCore.QRect(60, 240, 331, 441))
        self.frame_players_available.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_players_available.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_players_available.setObjectName("frame_players_available")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_players_available)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 311, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radio_BAT = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.radio_BAT.setFont(font)
        self.radio_BAT.setObjectName("radio_BAT")
        self.horizontalLayout_4.addWidget(self.radio_BAT)
        self.radio_BOW = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radio_BOW.setFont(font)
        self.radio_BOW.setObjectName("radio_BOW")
        self.horizontalLayout_4.addWidget(self.radio_BOW)
        self.radio_AR = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radio_AR.setFont(font)
        self.radio_AR.setObjectName("radio_AR")
        self.horizontalLayout_4.addWidget(self.radio_AR)
        self.radio_WK = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radio_WK.setFont(font)
        self.radio_WK.setObjectName("radio_WK")
        self.horizontalLayout_4.addWidget(self.radio_WK)
        self.list_players_available = QtWidgets.QListWidget(self.frame_players_available)
        self.list_players_available.setGeometry(QtCore.QRect(10, 60, 311, 371))
        self.list_players_available.setObjectName("list_players_available")
        self.frame_players_selected = QtWidgets.QFrame(self.centralwidget)
        self.frame_players_selected.setGeometry(QtCore.QRect(500, 240, 341, 441))
        self.frame_players_selected.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_players_selected.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_players_selected.setObjectName("frame_players_selected")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_players_selected)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 321, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Team_name = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Team_name.setFont(font)
        self.Team_name.setObjectName("Team_name")
        self.horizontalLayout_5.addWidget(self.Team_name, 0, QtCore.Qt.AlignHCenter)
        self.team_name_display = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.team_name_display.setFont(font)
        self.team_name_display.setStyleSheet("color:rgb(33, 218, 255)")
        self.team_name_display.setObjectName("team_name_display")
        self.horizontalLayout_5.addWidget(self.team_name_display)
        self.list_players_selected = QtWidgets.QListWidget(self.frame_players_selected)
        self.list_players_selected.setGeometry(QtCore.QRect(10, 60, 321, 371))
        self.list_players_selected.setObjectName("list_players_selected")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setStyleSheet("color:green;")
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_team = QtWidgets.QAction(MainWindow)
        self.actionNEW_team.setObjectName("actionNEW_team")
        self.actionNEW_team.setShortcut("Ctrl+N")
        self.actionOPEN_team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_team.setObjectName("actionOPEN_team")
        self.actionOPEN_team.setShortcut("Ctrl+O")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionSAVE_Team.setShortcut("Ctrl+S")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionEVALUATE_Team.setShortcut("Ctrl+E")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.menufile.addAction(self.actionNEW_team)
        self.menufile.addAction(self.actionOPEN_team)
        self.menufile.addAction(self.actionSAVE_Team)
        self.menufile.addAction(self.actionEVALUATE_Team)
        self.menufile.addAction(self.actionQuit)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #MENU TRIGGERED
        self.menufile.triggered[QtWidgets.QAction].connect(self.menufunction)

        #RADIO BUTTON CLICKED
        self.radio_BAT.clicked.connect(self.load_names)
        self.radio_BOW.clicked.connect(self.load_names)
        self.radio_AR.clicked.connect(self.load_names)
        self.radio_WK.clicked.connect(self.load_names)

        #DOUBLE CLICK LIST ITEMS
        self.list_players_available.itemDoubleClicked.connect(self.selectPlayer)
        self.list_players_selected.itemDoubleClicked.connect(self.de_selectPlayer)

        #PUSHBUTTON CLICKED
        self.new_ui.pushButton.clicked.connect(self.newTeam)
        self.open_ui.pushButton.clicked.connect(self.openTeam)
        self.save_ui.pushButton.clicked.connect(self.hideSaveDialog)
        self.evaluate_ui.pushButton.clicked.connect(self.calculatePoints)

        #TEXT CHANGED TEAM COMBOBOX FOR EVALUATE WINDOW 
        self.evaluate_ui.combo_team.currentTextChanged.connect(self.comboTeam)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Your_Selections.setText(_translate("MainWindow", "Your Selections"))
        self.BAT_count.setText(_translate("MainWindow", "Batsmen(BAT)  ##"))
        self.BOW_count.setText(_translate("MainWindow", "Bowlers(BOW)  ##"))
        self.AR_count.setText(_translate("MainWindow", "Allrounders(AR)  ##"))
        self.WK_count.setText(_translate("MainWindow", "Wicket-keeper(WK)  ##"))
        self.Points_available.setText(_translate("MainWindow", "Points Available"))
        self.points_available_count.setText(_translate("MainWindow", "####"))
        self.Points_used.setText(_translate("MainWindow", "Points Used"))
        self.points_used_count.setText(_translate("MainWindow", "####"))
        self.radio_BAT.setText(_translate("MainWindow", "BAT"))
        self.radio_BOW.setText(_translate("MainWindow", "BOW"))
        self.radio_AR.setText(_translate("MainWindow", "AR"))
        self.radio_WK.setText(_translate("MainWindow", "WK"))
        self.Team_name.setText(_translate("MainWindow", "Team Name"))
        self.team_name_display.setText(_translate("MainWindow", "Displayed Here"))
        self.menufile.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    #FUNCTION FOR QMenu
    def menufunction(self,action):
        txt=action.text()
        if txt =='NEW Team':
            self.New_Team.show()
        if txt =='OPEN Team':
            self.open_ui.fillCombo()
            self.Open_Team.show()
        if txt =='SAVE Team':
            self.saveTeam()
        if txt=='EVALUATE Team':
            self.evaluate_ui.fillEvaluateWindow()
            self.Evaluate_Team.show()
        if txt=='Quit':
            cricket_db.close()
            MainWindow.close()

    

    #ALLOWS USER TO CREATE NEW TEAM
    def newTeam(self):
        teams=None
        t_name=self.new_ui.lineEdit.text()
        sql="SELECT name FROM teams WHERE name='"+t_name+"';"
        curs.execute(sql)
        teams=curs.fetchone()
        if teams!=None:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Team name already exists! Please try another name.')
            error_dialog.exec_()
            return
        self.team_name= self.new_ui.lineEdit.text()
        if self.new_ui.lineEdit.text()!='':
            self.team_name_display.setText(self.team_name)
            self.new_ui.lineEdit.setText('')
            self.bat_count=0
            self.bow_count=0
            self.ar_count=0
            self.wk_count=0
            self.total_count=0
            self.points_available=800
            self.points_used=0
            self.list_players_selected.clear()
            self.BAT_count.setText('Batsmen(BAT)  '+str(self.bat_count))
            self.BOW_count.setText('Bowlers(BOW)  '+str(self.bow_count))
            self.AR_count.setText('Allrounders(AR)  '+str(self.ar_count))
            self.WK_count.setText('Wicket-keeper(WK)  '+str(self.wk_count))
            self.points_available_count.setText(str(self.points_available))
            self.points_used_count.setText(str(self.points_used))
            self.points_available_count.setText(str(self.points_available))
            self.points_used_count.setText(str(self.points_used))
            self.New_Team.close()
        else:
            print('Please enter name!')

    #DISPLAYS THE INFORMATION OF SAVED TEAM
    def openTeam(self):
        team=self.open_ui.comboBox.currentText()
        self.Open_Team.close()
        sql="SELECT * FROM teams WHERE name='"+team+"';"
        curs.execute(sql)
        team_details=curs.fetchone()
        self.bat_count=0
        self.bow_count=0
        self.ar_count=0
        self.wk_count=0
        self.total_count=11
        self.points_used=int(team_details[2])
        self.points_available=800-self.points_used
        self.list_players_selected.clear()

        for p_name in eval(team_details[1]):
            self.list_players_selected.addItem(p_name)
            for i in range(len(self.batsman_names)):
                if p_name==self.batsman_names[i][0]:
                    self.bat_count+=1
                    break
            for i in range(len(self.bowler_names)):
                if p_name==self.bowler_names[i][0]:
                    self.bow_count+=1
                    break
            for i in range(len(self.allrounder_names)):
                if p_name==self.allrounder_names[i][0]:
                    self.ar_count+=1
                    break
            for i in range(len(self.wk_names)):
                if p_name==self.wk_names[i][0]:
                    self.wk_count+=1
                    break

        self.points_used_count.setText(str(team_details[2]))
        self.points_available_count.setText(str(self.points_available))
        self.team_name_display.setText(team_details[0])
        self.BAT_count.setText('Batsmen(BAT)  '+str(self.bat_count))
        self.BOW_count.setText('Bowlers(BOW)  '+str(self.bow_count))
        self.AR_count.setText('Allrounders(AR)  '+str(self.ar_count))
        self.WK_count.setText('Wicket-keeper(WK)  '+str(self.wk_count))
        
    #SAVING NEW OR UPDATED TEAM
    def saveTeam(self):
        if self.total_count==11:
            if self.wk_count==0:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Select atleast 1 Wicket-keeper!')
                error_dialog.exec_()
            else:
                team_name=self.team_name_display.text()
                player_names=[]
                for index in range(self.total_count):
                    player_names.append(self.list_players_selected.item(index).text())
                teams=None
                curs.execute("SELECT name FROM teams WHERE name='"+team_name+"';")
                teams=curs.fetchone()
                if teams==None:
                    sql="INSERT INTO teams (name,players,value) VALUES(?,?,?);"
                    curs.execute(sql,(team_name,str(player_names),str(self.points_used)))
                    cricket_db.commit()
                else:
                    curs.execute("DELETE FROM teams WHERE name='"+team_name+"';")
                    cricket_db.commit()
                    sql="INSERT INTO teams (name,players,value) VALUES(?,?,?);"
                    curs.execute(sql,(team_name,str(player_names),str(self.points_used)))
                    cricket_db.commit()
                self.Dialog_Save.show()
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Select 11 Players!')
            error_dialog.exec_()


    #HIDING SAVE CONFIRMATION DIALOG BOX
    def hideSaveDialog(self):
        self.Dialog_Save.hide()

    #LOADING PLAYERS LIST IN LIST WIDGET(MAIN WINDOW)
    def load_names(self):
        if self.radio_BAT.isChecked()==True:
            self.list_players_available.clear()
            for i in range(len(self.batsman_names)):
                item=self.batsman_names[i][0]
                self.list_players_available.addItem(item)

        if self.radio_BOW.isChecked()==True:
            self.list_players_available.clear()
            for i in range(len(self.bowler_names)):
                item=self.bowler_names[i][0]
                self.list_players_available.addItem(item)

        if self.radio_AR.isChecked()==True:
            self.list_players_available.clear()
            for i in range(len(self.allrounder_names)):
                item=self.allrounder_names[i][0]
                self.list_players_available.addItem(item)

        if self.radio_WK.isChecked()==True:
            self.list_players_available.clear()
            for i in range(len(self.wk_names)):
                item=self.wk_names[i][0]
                self.list_players_available.addItem(item)

    #SELECTING PLAYERS FROM ONE LIST TO OTHER LIST WIDGET(MAIN WINDOW)
    def selectPlayer(self,item):
        if self.team_name_display.text()=='Displayed Here':
            self.New_Team.show()
            return
        if self.radio_BAT.isChecked()==True and self.error(item.text()):
            self.list_players_selected.addItem(item.text())
            item_txt=item.text()
            for i in range(len(self.batsman_names)):
                if item_txt==self.batsman_names[i][0]:
                    self.points_available-=int(self.batsman_names[i][1])
                    self.points_used+=int(self.batsman_names[i][1])
                    break
            self.bat_count+=1
            self.total_count+=1
            self.BAT_count.setText('Batsmen(BAT)   '+str(self.bat_count))
            self.points_available_count.setText(str(self.points_available))
            self.points_used_count.setText(str(self.points_used))
            

        if self.radio_BOW.isChecked()==True and self.error(item.text()):
            self.list_players_selected.addItem(item.text())
            item_txt=item.text()
            for i in range(len(self.bowler_names)):
                if item_txt==self.bowler_names[i][0]:
                    self.points_available-=int(self.bowler_names[i][1])
                    self.points_used+=int(self.bowler_names[i][1])
                    break
            self.bow_count+=1
            self.total_count+=1
            self.BOW_count.setText('Bowlers(BOW)   '+str(self.bow_count))
            self.points_available_count.setText(str(self.points_available))
            self.points_used_count.setText(str(self.points_used))

        if self.radio_AR.isChecked()==True and self.error(item.text()):
            self.list_players_selected.addItem(item.text())
            item_txt=item.text()
            for i in range(len(self.allrounder_names)):
                if item_txt==self.allrounder_names[i][0]:
                    self.points_available-=int(self.allrounder_names[i][1])
                    self.points_used+=int(self.allrounder_names[i][1])
                    break
            self.ar_count+=1
            self.total_count+=1
            self.AR_count.setText('Allrounders(AR)   '+str(self.ar_count))
            self.points_available_count.setText(str(self.points_available))
            self.points_used_count.setText(str(self.points_used))

        if self.radio_WK.isChecked()==True and self.error(item.text()):
            self.list_players_selected.addItem(item.text())
            item_txt=item.text()
            for i in range(len(self.wk_names)):
                if item_txt==self.wk_names[i][0]:
                    self.points_available-=int(self.wk_names[i][1])
                    self.points_used+=int(self.wk_names[i][1])
                    break
            self.wk_count+=1
            self.total_count+=1
            self.WK_count.setText('Wicket-Keeper(WK)   '+str(self.wk_count))
            self.points_available_count.setText(str(self.points_available))
            self.points_used_count.setText(str(self.points_used))

    #DE-SELECTING OF SELECTED PLAYERS(MAIN WINDOW) 
    def de_selectPlayer(self,item):
        self.list_players_selected.takeItem(self.list_players_selected.row(item))
        item_txt=item.text()
        for i in range(len(self.batsman_names)):
            if item_txt==self.batsman_names[i][0]:
                self.bat_count-=1
                self.points_available+=int(self.batsman_names[i][1])
                self.points_used-=int(self.batsman_names[i][1])
                self.BAT_count.setText('Batsmen(BAT)   '+str(self.bat_count))
                break
        for i in range(len(self.bowler_names)):
            if item_txt==self.bowler_names[i][0]:
                self.bow_count-=1
                self.points_available+=int(self.bowler_names[i][1])
                self.points_used-=int(self.bowler_names[i][1])
                self.BOW_count.setText('Bowlers(BOW)   '+str(self.bow_count))
                break
        for i in range(len(self.allrounder_names)):
            if item_txt==self.allrounder_names[i][0]:
                self.ar_count-=1
                self.points_available+=int(self.allrounder_names[i][1])
                self.points_used-=int(self.allrounder_names[i][1])
                self.AR_count.setText('Allrounders(AR)   '+str(self.ar_count))
                break
        for i in range(len(self.wk_names)):
            if item_txt==self.wk_names[i][0]:
                self.wk_count-=1
                self.points_available+=int(self.wk_names[i][1])
                self.points_used-=int(self.wk_names[i][1])
                self.WK_count.setText('Wicket-Keeper(WK)   '+str(self.wk_count))
                break
        self.total_count-=1
        self.points_available_count.setText(str(self.points_available))
        self.points_used_count.setText(str(self.points_used))

    #DISPLAY PLAYERS OF SELECTED TEAM(EVALUATE WINDOW)
    def comboTeam(self):
        self.evaluate_ui.list_players.clear()
        team=self.evaluate_ui.combo_team.currentText()
        if team!='':
            sql="SELECT * FROM teams WHERE name='"+team+"';"
            curs.execute(sql)
            team_details=curs.fetchone()
            for p_name in eval(team_details[1]):
                self.evaluate_ui.list_players.addItem(p_name)
        
    #CALCULATING POINTS FOR SELECTED TEAM AND MATCH(EVALUATE WINDOW)
    def calculatePoints(self):
        player_names=[]
        for index in range(self.evaluate_ui.list_players.count()):
            player_names.append(self.evaluate_ui.list_players.item(index).text())

        self.evaluate_ui.list_points.clear()
        total_points=0
        for player in player_names:
            sql="SELECT * FROM "+self.evaluate_ui.combo_match.currentText()+" WHERE Player='"+player+"';"
            curs.execute(sql)
            player_details=curs.fetchone()
            player_points=batscore(player_details)+bowlscore(player_details)
            total_points+=player_points
            self.evaluate_ui.list_points.addItem(str(player_points))
        self.evaluate_ui.total_points.setText(str(total_points))

    #ERROR HANDLING FOR SELECTION CRITERIA VIOLATION
    def error(self,item):
        error_dialog = QtWidgets.QErrorMessage()
        for index in range(self.total_count):
            if item==self.list_players_selected.item(index).text():
                error_dialog.showMessage('Player All-Ready Selected!')
                error_dialog.exec_()
                return 0

        if self.total_count>=0 and self.total_count<=10:
            pass
        else:
            error_dialog.showMessage('Only 11 Players are allowed!')
            error_dialog.exec_()
            return 0
        
        if self.bat_count>=0 and self.bat_count<=4:
            pass
        else:
            for i in range(len(self.batsman_names)):
                if item==self.batsman_names[i][0]:
                    error_dialog.showMessage('Only 5 Batsman are allowed!')
                    error_dialog.exec_()
                    return 0

        if self.bow_count>=0 and self.bow_count<=4:
            pass
        else:
            for i in range(len(self.bowler_names)):
                if item==self.bowler_names[i][0]:
                    error_dialog.showMessage('Only 5 Bowlers are allowed!')
                    error_dialog.exec_()
                    return 0

        if self.ar_count>=0 and self.ar_count<=1:
            pass
        else:
            for i in range(len(self.allrounder_names)):
                if item==self.allrounder_names[i][0]:
                    error_dialog.showMessage('Only 2 Allrounders are allowed!')
                    error_dialog.exec_()
                    return 0

        if self.wk_count==0:
            pass
        else:
            for i in range(len(self.wk_names)):
                if item==self.wk_names[i][0]:
                    error_dialog.showMessage('Only 1 Wicket-keeper are allowed!')
                    error_dialog.exec_()
                    return 0
        
        return 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

