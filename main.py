import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QTimer, Qt)
from PyQt5.QtGui import (QColor, QIcon)
from PyQt5.QtWidgets import *

from app import Ui_LinuxAuth

from splash_screen import Ui_SplashScreen

counter = 0

# Splash-screen is useless. You can delete it

class Mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LinuxAuth()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/linux_icon.png'))


class SplashScreen(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.ui.label_description.setText("<strong>WELCOME</strong> TO OUR APPLICATION")
        QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>ITS</strong> our project"))
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> Something"))
        self.show()

    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.main = Mainwindow()
            self.main.show()
            self.close()
        counter += 1



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LinuxAuth = SplashScreen()
    sys.exit(app.exec_())