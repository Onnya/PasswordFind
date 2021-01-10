import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from passwordtools import check_pswrd, gen_pswrd, take_pub_key, encrypt_pswrd


class UiAddEdit(object):
    def setup_ui(self, AddEdit):
        AddEdit.setObjectName("AddEdit")
        AddEdit.resize(323, 313)
        AddEdit.setStyleSheet("background-color: #CED4DA;")
        self.centralwidget = QtWidgets.QWidget(AddEdit)
        self.centralwidget.setObjectName("centralwidget")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(210, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        self.okBtn.setFont(font)
        self.okBtn.setStyleSheet("QPushButton:pressed { background-color: #212529 }\n"
                                 "QPushButton {\n"
                                 "background-color:#343A40;\n"
                                 "border-radius:9px;\n"
                                 "border-style: solid;\n"
                                 "border-color:#212529;\n"
                                 "border-width:2px;\n"
                                 "color:#E9ECEF}")
        self.okBtn.setObjectName("okBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameLn = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLn.setGeometry(QtCore.QRect(20, 60, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        self.nameLn.setFont(font)
        self.nameLn.setStyleSheet("background-color:#ADB5BD;border:none;")
        self.nameLn.setText("")
        self.nameLn.setObjectName("nameLn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.passwordLn = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLn.setGeometry(QtCore.QRect(20, 160, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        self.passwordLn.setFont(font)
        self.passwordLn.setStyleSheet("background-color:#ADB5BD;border:none;")
        self.passwordLn.setText("")
        self.passwordLn.setObjectName("passwordLn")
        self.generateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.generateBtn.setGeometry(QtCore.QRect(210, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        self.generateBtn.setFont(font)
        self.generateBtn.setStyleSheet("QPushButton:pressed { background-color: #212529 }\n"
                                       "QPushButton {\n"
                                       "background-color:#343A40;\n"
                                       "border-radius:9px;\n"
                                       "border-style: solid;\n"
                                       "border-color:#212529;\n"
                                       "border-width:2px;\n"
                                       "color:#E9ECEF}")
        self.generateBtn.setObjectName("generateBtn")
        AddEdit.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddEdit)
        self.statusbar.setStyleSheet("background-color:#ADB5BD")
        self.statusbar.setObjectName("statusbar")
        AddEdit.setStatusBar(self.statusbar)

        self.retranslate_ui(AddEdit)
        QtCore.QMetaObject.connectSlotsByName(AddEdit)

    def retranslate_ui(self, AddEdit):
        _translate = QtCore.QCoreApplication.translate
        AddEdit.setWindowTitle(_translate("AddEdit", "MainWindow"))
        self.okBtn.setText(_translate("AddEdit", "Ok"))
        self.label.setText(_translate("AddEdit", "Name"))
        self.label_2.setText(_translate("AddEdit", "Password"))
        self.generateBtn.setText(_translate("AddEdit", "Generate"))


class AddEditWindow(QMainWindow, UiAddEdit):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui(self)

        self.setWindowIcon(QtGui.QIcon('source\\img.png'))
        self.setWindowTitle("PasswordFind")
        self.setAttribute(Qt.WA_QuitOnClose, False)
        self.setFixedSize(319, 304)

        self.generateBtn.clicked.connect(self.generated_password)
        self.okBtn.clicked.connect(self.check_close)

        self.con = sqlite3.connect("source\\passwords.sqlite")

    def check_close(self):
        self.cur = self.con.cursor()
        self.result = self.cur.execute("SELECT * FROM main WHERE name=?",
                                       (self.nameLn.text(),)).fetchall()

    def generated_password(self):
        self.passwordLn.setText(gen_pswrd())

    def refresh(self, x, y, text=""):
        self.move(x + 50, y + 100)
        self.passwordLn.setText("")
        self.nameLn.setText(text)
        self.statusBar().clearMessage()


class AddWindow(AddEditWindow):
    def __init__(self, parent=None):
        super().__init__()

    def check_close(self):
        super().check_close()
        if self.result:
            self.statusBar().showMessage('Error. This name is already on the list.')
        else:
            if (check_pswrd(self.passwordLn.text()) == True) and (self.nameLn.text() != ""):
                self.cur.execute("INSERT INTO main(name,password) VALUES(?,?)",
                                 (str(self.nameLn.text()), encrypt_pswrd(self.passwordLn.text(), take_pub_key())))
                self.con.commit()
                self.hide()
            elif self.nameLn.text() == "":
                self.statusBar().showMessage("Empty title.")
            else:
                self.statusBar().showMessage(check_pswrd(self.passwordLn.text()))


class EditWindow(AddEditWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.nameLn.setReadOnly(True)

    def check_close(self):
        super().check_close()
        if check_pswrd(self.passwordLn.text()) == True:
            self.cur.execute('''UPDATE main
            SET password = ?
            WHERE name = ?
            ''', (encrypt_pswrd(self.passwordLn.text(), take_pub_key()), self.nameLn.text()))
            self.con.commit()
            self.hide()
        else:
            self.statusBar().showMessage(check_pswrd(self.passwordLn.text()))
