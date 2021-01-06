import sys
import subprocess
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from addeditwindow import AddEditWindow
import sqlite3
import os.path
from passwordtools import make_key, take_pr_key, take_pub_key, encrypt_pswrd, decrypt_pswrd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(442, 538)
        self.con = sqlite3.connect("passwords.sqlite")
        self.addBtn.clicked.connect(self.show_add_win)
        self.changeBtn.clicked.connect(self.show_edit_win)
        self.showBtn.clicked.connect(self.show_hide)
        self.deleteBtn.clicked.connect(self.delete)
        self.send = ""
        self.update_list()
        self.copyBtn.clicked.connect(self.to_clip)
        if not os.path.isfile('public.pem'):
            make_key()

    def show_edit_win(self):
        if self.listWidget.selectedItems() != []:
            self.editWin = AddEditWindow(self)
            self.statusBar().clearMessage()
            self.editWin.nameLn.setText(self.listWidget.currentItem().text())
            self.editWin.move(self.x() + 50, self.y() + 100)
            self.send = "Change"
            self.editWin.okBtn.clicked.connect(self.ok_pressed)
            self.editWin.nameLn.setReadOnly(True)
            self.editWin.show()
        else:
            self.statusBar().showMessage("Name not selected", 2000)

    def show_add_win(self):
        self.editWin = AddEditWindow(self)
        self.editWin.move(self.x() + 50, self.y() + 100)
        self.send = "Add"
        self.editWin.okBtn.clicked.connect(self.ok_pressed)
        self.editWin.show()

    def ok_pressed(self):
        self.editWin.check_close(self.send)
        self.update_list()

    def update_list(self):
        self.listWidget.clear()
        cur = self.con.cursor()
        result = cur.execute("SELECT name FROM main").fetchall()
        result.sort(key=lambda x: str(x))
        for i in result:
            self.listWidget.addItem(str(i[0]))

    def to_clip(self):
        if self.listWidget.selectedItems() != []:
            name = self.listWidget.currentItem().text()
            cur = self.con.cursor()
            result = cur.execute("SELECT password FROM main WHERE name=?",
                                 (name,)).fetchall()
            subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(
                bytes(decrypt_pswrd(result[0][0], take_pr_key()), encoding='utf8'))
        else:
            self.statusBar().showMessage("Name not selected", 2000)

    def show_hide(self):
        if self.listWidget.selectedItems() != []:
            name = self.listWidget.currentItem().text()
            cur = self.con.cursor()
            result = cur.execute("SELECT password FROM main WHERE name=?",
                                 (name,)).fetchall()
            self.statusBar().showMessage(decrypt_pswrd(result[0][0], take_pr_key()), 3000)
        else:
            self.statusBar().showMessage("Name not selected", 2000)

    def delete(self):
        if self.listWidget.selectedItems() != []:
            self.statusBar().clearMessage()
            name = self.listWidget.currentItem().text()
            cur = self.con.cursor()
            cur.execute("DELETE FROM main WHERE name=?", (name,))
            self.con.commit()
            self.update_list()
        else:
            self.statusBar().showMessage("Name not selected", 2000)

    def export(self):
        name = datetime.now().strftime("%d/%m/%y-%H:%M:%S")
        self.statusBar().showMessage(f"Saved as {name}.csv", 2500)

        cur = self.con.cursor()
        result = cur.execute("SELECT name, password FROM main").fetchall()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

# TODO: шифровка change
# TODO: импорт экспорт
# TODO: загрузка с паролем (?)