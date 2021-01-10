import sys

import subprocess

import os.path

from datetime import datetime

import sqlite3

import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog

from addeditwindow import AddWindow, EditWindow

from passwordtools import make_key, take_pr_key, take_pub_key, encrypt_pswrd, decrypt_pswrd


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 547)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #CED4DA;")
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 110, 401, 291))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border:none;")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName("listWidget")
        self.copyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.copyBtn.setGeometry(QtCore.QRect(20, 440, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        self.copyBtn.setFont(font)
        self.copyBtn.setStyleSheet("QPushButton:pressed { background-color: #495057 }\n"
                                   "QPushButton {\n"
                                   "background-color:#6C757D;\n"
                                   "border-radius:12px;\n"
                                   "border-style: solid;\n"
                                   "border-color:#343A40;\n"
                                   "border-width:2px;}")
        self.copyBtn.setFlat(False)
        self.copyBtn.setObjectName("copyBtn")
        self.changeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.changeBtn.setGeometry(QtCore.QRect(300, 430, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        self.changeBtn.setFont(font)
        self.changeBtn.setStyleSheet("QPushButton:pressed { background-color: #495057 }\n"
                                     "QPushButton {\n"
                                     "background-color:#6C757D;\n"
                                     "border-radius:12px;\n"
                                     "border-style: solid;\n"
                                     "border-color:#343A40;\n"
                                     "border-width:2px;}")
        self.changeBtn.setFlat(False)
        self.changeBtn.setObjectName("changeBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(300, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setStyleSheet("QPushButton:pressed { background-color: #495057 }\n"
                                     "QPushButton {\n"
                                     "background-color:#6C757D;\n"
                                     "border-radius:12px;\n"
                                     "border-style: solid;\n"
                                     "border-color:#343A40;\n"
                                     "border-width:2px;}")
        self.deleteBtn.setFlat(False)
        self.deleteBtn.setObjectName("deleteBtn")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(20, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("QPushButton:pressed { background-color: #212529 }\n"
                                  "QPushButton {\n"
                                  "background-color:#343A40;\n"
                                  "border-radius:9px;\n"
                                  "border-style: solid;\n"
                                  "border-color:#212529;\n"
                                  "border-width:2px;\n"
                                  "color:#E9ECEF}")
        self.addBtn.setObjectName("addBtn")
        self.exportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportBtn.setGeometry(QtCore.QRect(160, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        self.exportBtn.setFont(font)
        self.exportBtn.setStyleSheet("QPushButton:pressed { background-color: #212529 }\n"
                                     "QPushButton {\n"
                                     "background-color:#343A40;\n"
                                     "border-radius:9px;\n"
                                     "border-style: solid;\n"
                                     "border-color:#212529;\n"
                                     "border-width:2px;\n"
                                     "color:#E9ECEF}")
        self.exportBtn.setObjectName("exportBtn")
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(300, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        self.importBtn.setFont(font)
        self.importBtn.setStyleSheet("QPushButton:pressed { background-color: #212529 }\n"
                                     "QPushButton {\n"
                                     "background-color:#343A40;\n"
                                     "border-radius:9px;\n"
                                     "border-style: solid;\n"
                                     "border-color:#212529;\n"
                                     "border-width:2px;\n"
                                     "color:#E9ECEF}")
        self.importBtn.setObjectName("importBtn")
        self.showBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QtCore.QRect(160, 440, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        self.showBtn.setFont(font)
        self.showBtn.setStyleSheet("QPushButton:pressed { background-color: #495057 }\n"
                                   "QPushButton {\n"
                                   "background-color:#6C757D;\n"
                                   "border-radius:12px;\n"
                                   "border-style: solid;\n"
                                   "border-color:#343A40;\n"
                                   "border-width:2px;}")
        self.showBtn.setFlat(False)
        self.showBtn.setObjectName("showBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color:#ADB5BD")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PasswordFind"))
        self.copyBtn.setText(_translate("MainWindow", "To clipboard"))
        self.changeBtn.setText(_translate("MainWindow", "Change"))
        self.deleteBtn.setText(_translate("MainWindow", "Delete"))
        self.addBtn.setText(_translate("MainWindow", "Add password"))
        self.exportBtn.setText(_translate("MainWindow", "Export csv"))
        self.importBtn.setText(_translate("MainWindow", "Import csv"))
        self.showBtn.setText(_translate("MainWindow", "Show"))


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)

        self.setFixedSize(442, 538)
        self.setWindowIcon(QtGui.QIcon('source\\img.png'))

        self.addBtn.clicked.connect(self.show_add_win)
        self.changeBtn.clicked.connect(self.show_edit_win)
        self.showBtn.clicked.connect(self.show_hide)
        self.deleteBtn.clicked.connect(self.delete)
        self.copyBtn.clicked.connect(self.to_clip)
        self.exportBtn.clicked.connect(self.export_csv)
        self.importBtn.clicked.connect(self.import_csv)

        self.con = sqlite3.connect("source\\passwords.sqlite")
        if not os.path.isfile('source\\public.pem'):
            make_key()

        self.AddWin = AddWindow(self)
        self.EditWin = EditWindow(self)

        self.AddWin.okBtn.clicked.connect(self.update_list)
        self.EditWin.okBtn.clicked.connect(self.update_list)

        self.update_list()

    def show_edit_win(self):
        if self.listWidget.selectedItems():
            self.statusBar().clearMessage()
            self.EditWin.refresh(self.x(), self.y(), self.listWidget.currentItem().text())
            self.EditWin.show()
        else:
            self.statusBar().showMessage("Name not selected", 2000)

    def show_add_win(self):
        self.AddWin.refresh(self.x(), self.y())
        self.AddWin.show()

    def update_list(self):
        self.listWidget.clear()

        cur = self.con.cursor()
        result = cur.execute("SELECT name FROM main").fetchall()
        result.sort(key=lambda x: str(x).lower())

        for i in result:
            self.listWidget.addItem(str(i[0]))

    def to_clip(self):
        if self.listWidget.selectedItems():
            name = self.listWidget.currentItem().text()

            cur = self.con.cursor()
            result = cur.execute("SELECT password FROM main WHERE name=?",
                                 (name,)).fetchall()

            subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(
                bytes(decrypt_pswrd(result[0][0], take_pr_key()), encoding='utf8'))
        else:
            self.statusBar().showMessage("Name not selected", 2000)

    def show_hide(self):
        if self.listWidget.selectedItems():
            name = self.listWidget.currentItem().text()

            cur = self.con.cursor()
            result = cur.execute("SELECT password FROM main WHERE name=?",
                                 (name,)).fetchall()

            self.statusBar().showMessage(decrypt_pswrd(result[0][0], take_pr_key()), 3000)
        else:
            self.statusBar().showMessage("Name not selected", 2000)

    def delete(self):
        if self.listWidget.selectedItems():
            self.statusBar().clearMessage()

            name = self.listWidget.currentItem().text()
            cur = self.con.cursor()
            cur.execute("DELETE FROM main WHERE name=?", (name,))
            self.con.commit()

            self.update_list()
        else:
            self.statusBar().showMessage("Name not selected", 2000)

    def export_csv(self):
        name = datetime.now().strftime("%d-%m-%y_%H-%M-%S") + ".csv"
        self.statusBar().showMessage(f"Saved as {name}", 2500)

        cur = self.con.cursor()
        result = cur.execute("SELECT name, password FROM main").fetchall()

        with open('files\\' + name, 'w', newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(
                csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["name", "password"])
            for i in range(len(result)):
                writer.writerow([result[i][0], decrypt_pswrd(result[i][1], take_pr_key())])

    def import_csv(self):
        filename = QFileDialog.getOpenFileName(
            self, 'Choose file', '',
            'csv file (*.csv)')[0]

        if filename:
            delimit, ok_pressed = QInputDialog.getText(self, "Choose delimiter",
                                                       "Enter delimiter:")

            if delimit:
                res = []
                change = False

                with open(filename, encoding="utf8") as csv_file:
                    reader = csv.reader(csv_file, delimiter=delimit, quotechar='"')
                    for index, row in enumerate(reader):
                        res.append(row)

                cur = self.con.cursor()
                names = [str(i[0]) for i in cur.execute("SELECT name FROM main").fetchall()]

                res = res[1:] if res[0] == ['name', 'password'] else res

                for i in res:
                    if i[0] in names:
                        change, ok_pressed = QInputDialog.getItem(
                            self, "Duplicate names", "Replace old passwords with imported ones?",
                            ("Yes", "No"), 1, False)

                        change = True if change == "Yes" else False
                        break

                for i in res:
                    if i:
                        if i[0] in names:
                            if change:
                                cur.execute('''UPDATE main
                                            SET password = ?
                                            WHERE name = ?
                                            ''', (encrypt_pswrd(i[1], take_pub_key()), i[0]))
                                self.con.commit()
                        else:
                            cur.execute("INSERT INTO main(name,password) VALUES(?,?)",
                                        (i[0], encrypt_pswrd(i[1], take_pub_key())))
                            self.con.commit()

        self.update_list()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
