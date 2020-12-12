import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setStyleSheet("""QScrollBar:vertical {
            border: 2px solid grey;
            background: #32CC99;
            height: 15px;
            margin: 0px 20px 0 20px;
        }
        QScrollBar::handle:vertical {
            background: white;
            min-width: 20px;
        }
        QScrollBar::add-line:vertical {
            border: 2px solid grey;
            background: #32CC99;
            width: 20px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical {
            border: 2px solid grey;
            background: #32CC99;
            width: 20px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }
                                      }""")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())