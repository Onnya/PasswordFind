from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sqlite3
from passwordtools import check_pswrd, gen_pswrd, take_pr_key, take_pub_key, encrypt_pswrd, decrypt_pswrd


class AddEditWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('addeditwindow.ui', self)
        self.setFixedSize(319, 304)
        self.con = sqlite3.connect("passwords.sqlite")
        self.generateBtn.clicked.connect(self.generated_password)


    def check_close(self, sender):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM main WHERE name=?",
                             (self.nameLn.text(),)).fetchall()
        if sender == "Add":
            if result:
                self.statusBar().showMessage('Error. This name is already on the list.')
            else:
                if (check_pswrd(self.passwordLn.text()) == True) and (self.nameLn.text() != ""):
                    cur.execute("INSERT INTO main(name,password) VALUES(?,?)",
                                (str(self.nameLn.text()), encrypt_pswrd(self.passwordLn.text(), take_pub_key())))
                    self.con.commit()
                    self.close()
                elif self.nameLn.text() == "":
                    self.statusBar().showMessage("Empty title.")
                else:
                    self.statusBar().showMessage(check_pswrd(self.passwordLn.text()))
        else:
            if check_pswrd(self.passwordLn.text()) == True:
                cur.execute('''UPDATE main
                SET password = ?
                WHERE name = ?
                ''', (encrypt_pswrd(self.passwordLn.text(), take_pub_key()), self.nameLn.text()))
                self.con.commit()
                self.close()
            else:
                self.statusBar().showMessage(check_pswrd(self.passwordLn.text()))

    def generated_password(self):
        self.passwordLn.setText(gen_pswrd())