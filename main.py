from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from app import Flatmate, Room, PdfReport

class Ui_MainWindow(object):
    
    def __init__(self):
        self.room = None
        self.fl = list()
        self.p = PdfReport(path=None)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 663)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-170, -190, 1281, 991))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(80, 230, 1111, 81))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(110, 0, 291, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(850, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLabel\" name=\"label\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>110</x>\n"
"     <y>50</y>\n"
"     <width>291</width>\n"
"     <height>81</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>MS Sans Serif</family>\n"
"     <pointsize>15</pointsize>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(85, 170, 255);</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>Flatmates Bill Calculator</string>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(1000, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\\")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(750, 40, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLabel\" name=\"label\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>110</x>\n"
"     <y>50</y>\n"
"     <width>291</width>\n"
"     <height>81</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>MS Sans Serif</family>\n"
"     <pointsize>15</pointsize>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(85, 170, 255);</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>Flatmates Bill Calculator</string>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(100, 310, 1031, 51))
        self.frame_3.setStyleSheet("background-color: rgb(71, 142, 213);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pdf = QtWidgets.QPushButton(self.frame_3)
        self.pdf.setGeometry(QtCore.QRect(80, 10, 131, 31))
        self.pdf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.pdf.setObjectName("pdf")
        self.csv = QtWidgets.QPushButton(self.frame_3)
        self.csv.setGeometry(QtCore.QRect(220, 10, 131, 31))
        self.csv.setStyleSheet("background-color: rgb(173, 173, 173);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.csv.setObjectName("csv")
        self.sett = QtWidgets.QPushButton(self.frame_3)
        self.sett.setGeometry(QtCore.QRect(360, 10, 131, 31))
        self.sett.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.sett.setObjectName("sett")
        self.rl = QtWidgets.QPushButton(self.frame_3)
        self.rl.setGeometry(QtCore.QRect(640, 10, 131, 31))
        self.rl.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.rl.setObjectName("rl")
        self.rs = QtWidgets.QPushButton(self.frame_3)
        self.rs.setGeometry(QtCore.QRect(500, 10, 131, 31))
        self.rs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.rs.setObjectName("rs")
        self.rall = QtWidgets.QPushButton(self.frame_3)
        self.rall.setGeometry(QtCore.QRect(780, 10, 181, 31))
        self.rall.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.rall.setObjectName("rall")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(110, 150, 1031, 81))
        self.frame_4.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.close = QtWidgets.QPushButton(self.frame_4)
        self.close.setGeometry(QtCore.QRect(930, 50, 20, 20))
        self.close.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.close.setObjectName("close")
        self.minimize = QtWidgets.QPushButton(self.frame_4)
        self.minimize.setGeometry(QtCore.QRect(900, 50, 20, 21))
        self.minimize.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.minimize.setObjectName("minimize")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(70, 40, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.list = QtWidgets.QListWidget(self.frame)
        self.list.setGeometry(QtCore.QRect(170, 360, 901, 411))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.list.setFont(font)
        self.list.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 5px;")
        self.list.setAlternatingRowColors(False)
        self.list.setMovement(QtWidgets.QListView.Static)
        self.list.setProperty("isWrapping", False)
        self.list.setObjectName("list")
        item = QtWidgets.QListWidgetItem()
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list.addItem(item)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(100, 770, 1031, 51))
        self.frame_5.setStyleSheet("background-color: rgb(71, 142, 213);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.new_2 = QtWidgets.QPushButton(self.frame_5)
        self.new_2.setGeometry(QtCore.QRect(650, 10, 131, 31))
        self.new_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.new_2.setObjectName("new_2")
        self.name = QtWidgets.QLineEdit(self.frame_5)
        self.name.setGeometry(QtCore.QRect(80, 10, 311, 31))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"color: rgb(111, 111, 111);")
        self.name.setClearButtonEnabled(True)
        self.name.setObjectName("name")
        self.day = QtWidgets.QLineEdit(self.frame_5)
        self.day.setGeometry(QtCore.QRect(400, 10, 241, 31))
        self.day.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"color: rgb(111, 111, 111);")
        self.day.setFrame(True)
        self.day.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.day.setClearButtonEnabled(True)
        self.day.setObjectName("day")
        self.delete_2 = QtWidgets.QPushButton(self.frame_5)
        self.delete_2.setGeometry(QtCore.QRect(790, 10, 171, 31))
        self.delete_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.delete_2.setObjectName("delete_2")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(140, 820, 1031, 51))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.stat = QtWidgets.QLabel(self.frame_6)
        self.stat.setGeometry(QtCore.QRect(40, 5, 891, 21))
        self.stat.setStyleSheet("color: rgb(147, 147, 147);")
        self.stat.setObjectName("stat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.list.clear()

        def update_list():
            l = self.list
            l.clear()
            add = []
            count = 1
            for flatmate in self.fl:
                add.append(f'{count}- {flatmate.name} - {flatmate.days}')
                count += 1
            l.addItems(add)

        def room_settings():
            text, okPressed = QtWidgets.QInputDialog.getText(None, 
                                                        "Room Settings",
                                                        "Enter Total Amount Of Bill: ", 
                                                        QtWidgets.QLineEdit.Normal, 
                                                        "")   
            if okPressed and text != '':
                try:
                    text = int(text)
                    self.room = Room(text)
                except:
                    self.stat.setText('Enter Number !')

        def add_flatmate():
            name = self.name.text()
            days = self.day.text()

            if name != '' or days != '':
                
                if self.room != None:
                    try:
                        test = int(days)
                        self.fl.append(Flatmate(name,days))
                        self.name.setText('')
                        self.day.setText('')
                        update_list()
                        self.stat.setText('OK')
                    except:
                        self.stat.setText('Enter Number !')        
                else:
                    self.stat.setText('Set Room Settings !')    
            else:
                self.stat.setText('Fill Out The Name And Day Entries !')

        def delete_item():
                listItems=self.list.selectedItems()
                if not listItems: return        
                for item in listItems:
                        self.fl.pop(int(item.text()[0])-1)
                        self.list.takeItem(self.list.row(item))

        def rall():
            self.list.clear()
            self.room = None
            self.fl = []

        def rl():
            self.list.clear()
            self.fl = []

        def rs():
            self.room = None

        def pdf():
                if len(self.fl) != 0:
                
                        if self.room != None:
                                options = QFileDialog.Options()
                                options |= QFileDialog.DontUseNativeDialog
                                file_name, _ = QFileDialog.getSaveFileName(MainWindow,"Save File","","PDF Files(*.pdf)",options = options)
                                if file_name:
                                        self.p.set_path(file_name)
                                        self.room.calculate_bills(self.fl)
                                        self.p.export(self.room,self.fl)
                        else:
                                self.stat.setText('Set Room Settings !')    
                else:
                        self.stat.setText('Add One Flatmate At Least !')

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close) # type: ignore
        self.minimize.clicked.connect(MainWindow.showMinimized) # type: ignore
        self.new_2.clicked.connect(add_flatmate)
        self.sett.clicked.connect(room_settings)
        self.delete_2.clicked.connect(delete_item)
        self.rall.clicked.connect(rall)
        self.rs.clicked.connect(rs)
        self.rl.clicked.connect(rl)
        self.pdf.clicked.connect(pdf)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flatmates Bill Calculator"))
        self.label.setText(_translate("MainWindow", "Flatmates Bill Calculator"))
        self.label_2.setText(_translate("MainWindow", "Created By Kian-RZ"))
        self.label_3.setText(_translate("MainWindow", "Created By Kian-RZ"))
        self.label_4.setText(_translate("MainWindow", "Advanced Python Programing Class"))
        self.pdf.setText(_translate("MainWindow", "Export PDF Report"))
        self.csv.setText(_translate("MainWindow", "Import CSV"))
        self.sett.setText(_translate("MainWindow", "Room Settings"))
        self.rl.setText(_translate("MainWindow", "Reset List"))
        self.rs.setText(_translate("MainWindow", "Reset Settings"))
        self.rall.setText(_translate("MainWindow", "Reset All"))
        self.close.setText(_translate("MainWindow", "X"))
        self.minimize.setText(_translate("MainWindow", "-"))
        self.label_6.setText(_translate("MainWindow", "Flatmates Bill Calculator"))
        __sortingEnabled = self.list.isSortingEnabled()
        self.list.setSortingEnabled(False)
        self.list.setSortingEnabled(__sortingEnabled)
        self.new_2.setText(_translate("MainWindow", "New Flatmate"))
        self.name.setPlaceholderText(_translate("MainWindow", "Flatmate Full Name"))
        self.day.setPlaceholderText(_translate("MainWindow", "Number Of Days He/She Stays"))
        self.delete_2.setText(_translate("MainWindow", "Delete Selected"))
        self.stat.setText(_translate("MainWindow", "OK"))

    def getTextInputDialog(self):
        text, okPressed = QtWidgets.QInputDialog.getText(None, 
                                                        "Room Settings",
                                                        "Enter Total Amount Of Bill: ", 
                                                        QtWidgets.QLineEdit.Normal, 
                                                        "")   
        if okPressed and text != '':
            print(text)
            ui.lineedit.setText(text)        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
