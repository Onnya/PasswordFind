import sqlite3

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from passwordtools import check_pswrd, gen_pswrd, take_pub_key, encrypt_pswrd


class AddEditWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('addeditwindow.ui', self)

        self.setWindowIcon(QtGui.QIcon('img.png'))
        self.setWindowTitle("PasswordFind")
        self.setAttribute(Qt.WA_QuitOnClose, False)
        self.setFixedSize(319, 304)

        self.generateBtn.clicked.connect(self.generated_password)
        self.okBtn.clicked.connect(self.check_close)

        self.con = sqlite3.connect("passwords.sqlite")

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
            if (check_pswrd(self.passwordLn.text())) and (self.nameLn.text() != ""):
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
        if check_pswrd(self.passwordLn.text()):
            self.cur.execute('''UPDATE main
            SET password = ?
            WHERE name = ?
            ''', (encrypt_pswrd(self.passwordLn.text(), take_pub_key()), self.nameLn.text()))
            self.con.commit()
            self.hide()
        else:
            self.statusBar().showMessage(check_pswrd(self.passwordLn.text()))
