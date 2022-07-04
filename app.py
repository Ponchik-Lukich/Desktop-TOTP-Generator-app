import credentials
import keyring
import base64
import hmac
import struct
import time
import string
import random
import math
import cryptocode
from PyQt5.QtWidgets import (QMessageBox, QWidget)
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QTimer, QRect, QSize, Qt)
from PyQt5.QtGui import (QMovie, QFont, QIcon, QPixmap)
from PyQt5.QtWidgets import *

def English(string):
    try:
        string.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def show_popup():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("Wrong secret key!\n Try again.")
    msg.setIcon(QMessageBox.Critical)
    msg.exec_()


def show_popup_1():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("You have no active secret key!\nAdd the key using the button below")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()

def show_popup_2(password):
    msg = QMessageBox()
    msg.setWindowTitle("Important")
    msg.setText("Your password is: " + str(password) + "\nSave it!")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()

def show_popup_3():
    msg = QMessageBox()
    msg.setWindowTitle("Wrong password!")
    msg.setText("Wrong password!")
    msg.setIcon(QMessageBox.Critical)
    msg.exec_()

Style = "border-radius: 10px;\ncolor: #FFFFFF;\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));"

def pass_check():
    return keyring.get_password(credentials.service_id, credentials.pos2) is None


def change_secret(password):
    if keyring.get_password(credentials.service_id, credentials.pos1) is not None:
        secret = cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos1),
                             cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos2),
                                         credentials.secret_key))
        keyring.set_password(credentials.service_id, credentials.pos1, cryptocode.encrypt(secret, password))

def generate_password():
    rand_str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
    show_popup_2(rand_str)
    change_secret(rand_str)
    keyring.set_password(credentials.service_id, credentials.pos2, cryptocode.encrypt(rand_str, credentials.secret_key))


def word(path):
    with open(path, "r") as f:
        for line in f:
            for word in line.split():
                return word


class Ui_LinuxAuth(object):
    def setupUi(self, LinuxAuth):
        LinuxAuth.setObjectName("LinuxAuth")
        LinuxAuth.setFixedSize(649, 411)

        LinuxAuth.setStyleSheet("")

        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)

        font2 = QFont()
        font2.setFamily("Segoe UI")
        font2.setPointSize(46)

        font3 = QFont()
        font3.setFamily("Segoe UI")
        font3.setPointSize(40)
        font3.setBold(False)
        font3.setWeight(75)

        font4 = QFont()
        font4.setFamily("Segoe UI")
        font4.setPointSize(10)

        font5 = QFont()
        font5.setFamily("Segoe UI")
        font5.setPointSize(25)
        font5.setBold(True)
        font5.setWeight(75)

        self.centralwidget = QWidget(LinuxAuth)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(0, -21, 651, 491))
        self.widget.setStyleSheet("background-color: rgb(56, 58, 89);")
        self.widget.setObjectName("widget")

        self.line = QLabel(self.widget)
        self.line.setGeometry(QRect(0, 30, 651, 21))
        self.line.setStyleSheet("border-bottom: 4px solid  rgb(254, 121, 199)")
        self.line.setText("")
        self.line.setObjectName("line")

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QRect(-1, 59, 651, 361))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QWidget()
        self.page_0.setObjectName("page_0")

        self.enter_button = QPushButton(self.page_0)
        self.enter_button.setEnabled(True)
        self.enter_button.setGeometry(QRect(210, 260, 221, 81))
        self.enter_button.setFont(font1)
        self.enter_button.setStyleSheet(Style)
        self.enter_button.setObjectName("enter_button")

        self.password_line = QLineEdit(self.page_0)
        self.password_line.setGeometry(QRect(100, 130, 441, 91))
        self.password_line.setFont(font3)
        self.password_line.setEchoMode(QLineEdit.Password)
        self.password_line.setAlignment(Qt.AlignCenter)
        self.password_line.setStyleSheet("color: #FFFFFF")
        self.password_line.setObjectName("password_line")

        self.label_title = QLabel(self.page_0)
        self.label_title.setGeometry(QRect(-10, 30, 661, 91))
        self.label_title.setFont(font2)
        self.label_title.setStyleSheet("color: #FFFFFF;")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")

        self.loading = QLabel(self.page_1)
        self.loading.setGeometry(QRect(480, 80, 151, 151))
        self.loading.setText("")
        self.loading.setScaledContents(True)
        self.loading.setObjectName("loading")

        self.TOTP = QLabel(self.page_1)
        self.TOTP.setGeometry(QRect(200, 100, 261, 91))
        self.TOTP.setFont(font3)
        self.TOTP.setStyleSheet("color: #FFFFFF")
        self.TOTP.setObjectName("TOTP")

        self.add_button = QPushButton(self.page_1)
        self.add_button.setGeometry(QRect(40, 280, 131, 61))
        self.add_button.setFont(font1)
        self.add_button.setStyleSheet(Style)
        self.add_button.setObjectName("add_button")

        self.label = QLabel(self.page_1)
        self.label.setGeometry(QRect(40, 90, 141, 141))
        self.label.setText("")
        self.label.setPixmap(QPixmap("icons/pink_icon.png").scaled(140, 140))
        self.label.setObjectName("label")

        self.settings_button = QPushButton(self.page_1)
        self.settings_button.setGeometry(QRect(500, 280, 111, 61))
        self.settings_button.setStyleSheet(Style)
        self.settings_button.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/settings.png"), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QSize(40, 40))
        self.settings_button.setObjectName("settings_button")

        self.reload_button = QPushButton(self.page_1)
        self.reload_button.setGeometry(QRect(470, 80, 161, 151))
        self.reload_button.setStyleSheet("margin: 4px 2px;\nborder-radius: 30%;")
        self.reload_button.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("icons/round.png"), QIcon.Normal, QIcon.Off)
        self.reload_button.setIcon(icon1)
        self.reload_button.setIconSize(QSize(150, 150))
        self.reload_button.setObjectName("reload_button")

        self.label_2 = QLabel(self.page_1)
        self.label_2.setGeometry(QRect(40, 30, 151, 51))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet("color: #FFFFFF;")
        self.label_2.setObjectName("label_2")

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")

        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setGeometry(QRect(60, 60, 381, 131))
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet("color: #FFFFFF")
        self.textEdit.setObjectName("textEdit")

        self.back_button = QPushButton(self.page_2)
        self.back_button.setGeometry(QRect(480, 280, 131, 61))
        self.back_button.setFont(font4)
        self.back_button.setStyleSheet(Style)
        self.back_button.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("icons/4765130.png"), QIcon.Normal, QIcon.Off)
        self.back_button.setIcon(icon2)
        self.back_button.setIconSize(QSize(70, 70))
        self.back_button.setObjectName("back_button")

        self.check_button = QPushButton(self.page_2)
        self.check_button.setGeometry(QRect(440, 50, 171, 151))
        self.check_button.setStyleSheet("margin: 4px 2px;\nborder-radius: 30%;")
        self.check_button.setText("")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("icons/check.png"), QIcon.Normal, QIcon.Off)
        self.check_button.setIcon(icon3)
        self.check_button.setIconSize(QSize(130, 130))
        self.check_button.setObjectName("check_button")

        self.label_text = QLabel(self.page_2)
        self.label_text.setGeometry(QRect(130, 200, 421, 71))
        self.label_text.setFont(font5)
        self.label_text.setStyleSheet("color: #FFFFFF")
        self.label_text.setObjectName("label_text")

        self.plus_button = QPushButton(self.page_2)
        self.plus_button.setGeometry(QRect(440, 50, 171, 161))
        self.plus_button.setStyleSheet("margin: 4px 2px;\nborder-radius: 30%;")
        self.plus_button.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("icons/plus.png"), QIcon.Normal, QIcon.Off)
        self.plus_button.setIcon(icon4)
        self.plus_button.setIconSize(QSize(130, 130))
        self.plus_button.setObjectName("plus_button")

        self.file_button = QPushButton(self.page_2)
        self.file_button.setGeometry(QRect(40, 190, 91, 91))
        self.file_button.setStyleSheet("margin: 4px 2px;\nborder-radius: 30%;")
        self.file_button.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("icons/file.png"), QIcon.Normal, QIcon.Off)
        self.file_button.setIcon(icon4)
        self.file_button.setIconSize(QSize(75, 75))
        self.file_button.setObjectName("file_button")

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")

        self.enter_button_2 = QPushButton(self.page_3)
        self.enter_button_2.setEnabled(True)
        self.enter_button_2.setGeometry(QRect(260, 140, 131, 71))
        self.enter_button_2.setFont(font5)
        self.enter_button_2.setStyleSheet(Style)
        self.enter_button_2.setObjectName("enter_button_2")

        self.manual_button = QPushButton(self.page_3)
        self.manual_button.setEnabled(True)
        self.manual_button.setGeometry(QRect(350, 140, 201, 71))
        self.manual_button.setFont(font5)
        self.manual_button.setStyleSheet(Style)
        self.manual_button.setObjectName("enter_button_3")
        self.manual_button.hide()

        self.random_button = QPushButton(self.page_3)
        self.random_button.setEnabled(True)
        self.random_button.setGeometry(QRect(100, 140, 201, 71))
        self.random_button.setFont(font5)
        self.random_button.setStyleSheet(Style)
        self.random_button.hide()

        self.confirm_button = QPushButton(self.page_3)
        self.confirm_button.setEnabled(True)
        self.confirm_button.setGeometry(QRect(240, 280, 181, 61))
        self.confirm_button.setFont(font5)
        self.confirm_button.setStyleSheet(Style)
        self.confirm_button.setObjectName("enter_button_2")
        self.confirm_button.hide()

        self.label_generate = QLabel(self.page_3)
        self.label_generate.setGeometry(QRect(130, 40, 401, 41))
        self.label_generate.setFont(font5)
        self.label_generate.setStyleSheet("color: #FFFFFF")
        self.label_generate.setObjectName("label_generate")

        self.label_old = QLabel(self.page_3)
        self.label_old.setGeometry(QRect(20, 20, 221, 41))
        self.label_old.setFont(font5)
        self.label_old.setStyleSheet("color: #FFFFFF")
        self.label_old.setObjectName("old")
        self.label_old.hide()

        self.label_new = QLabel(self.page_3)
        self.label_new.setGeometry(QRect(20, 110, 241, 41))
        self.label_new.setFont(font5)
        self.label_new.setStyleSheet("color: #FFFFFF")
        self.label_new.setObjectName("new")
        self.label_new.hide()

        self.label_repeat = QLabel(self.page_3)
        self.label_repeat.setGeometry(QRect(20, 200, 241, 41))
        self.label_repeat.setFont(font5)
        self.label_repeat.setStyleSheet("color: #FFFFFF")
        self.label_repeat.setObjectName("repeat")
        self.label_repeat.hide()

        self.old_line = QLineEdit(self.page_3)
        self.old_line.setGeometry(QRect(260, 0, 351, 81))
        self.old_line.setFont(font3)
        self.old_line.setEchoMode(QLineEdit.Password)
        self.old_line.setStyleSheet("color: #FFFFFF")
        self.old_line.setObjectName("old_line")
        self.old_line.hide()

        self.new_line = QLineEdit(self.page_3)
        self.new_line.setGeometry(QRect(260, 90, 351, 81))
        self.new_line.setFont(font3)
        self.new_line.setEchoMode(QLineEdit.Password)
        self.new_line.setStyleSheet("color: #FFFFFF")
        self.new_line.setObjectName("new_line")
        self.new_line.hide()

        self.repeat_line = QLineEdit(self.page_3)
        self.repeat_line.setGeometry(QRect(260, 180, 351, 81))
        self.repeat_line.setFont(font3)
        self.repeat_line.setEchoMode(QLineEdit.Password)
        self.repeat_line.setStyleSheet("color: #FFFFFF")
        self.repeat_line.setObjectName("repeat_line")
        self.repeat_line.hide()

        self.exit_button = QPushButton(self.page_3)
        self.exit_button.setGeometry(QRect(40, 280, 131, 61))
        self.exit_button.setFont(font5)
        self.exit_button.setStyleSheet(Style)
        self.exit_button.setObjectName("exit_button")
        self.back_button_2 = QPushButton(self.page_3)
        self.back_button_2.setGeometry(QRect(480, 280, 131, 61))
        self.back_button_2.setFont(font4)
        self.back_button_2.setStyleSheet(Style)
        self.back_button_2.setText("")
        self.back_button_2.setIcon(icon2)
        self.back_button_2.setIconSize(QSize(70, 70))
        self.back_button_2.setObjectName("back_button_2")
        self.stackedWidget.addWidget(self.page_3)
        LinuxAuth.setCentralWidget(self.centralwidget)
        self.retranslateUi(LinuxAuth)
        self.retranslateUi(LinuxAuth)
        if pass_check() is False:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(LinuxAuth)
        self.movie = QMovie("icons/render.gif")
        self.add_functions()
        QMetaObject.connectSlotsByName(LinuxAuth)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("LinuxAuth", "LinuxAuth"))
        self.enter_button.setText(_translate("LinuxAuth", "Enter"))
        self.label_title.setText(_translate("LinuxAuth",
                                            "<html><head/><body><p><span style=\" font-weight:600;\">Enter password</span></p></body></html>"))
        self.TOTP.setText(_translate("LinuxAuth", "– – – – – –"))
        self.add_button.setText(_translate("LinuxAuth", "Add"))
        self.label_2.setText(_translate("LinuxAuth", "Linux"))
        self.textEdit.setPlaceholderText(_translate("LinuxAuth", "Secret key"))
        self.password_line.setPlaceholderText(_translate("LinuxAuth", "Password"))
        self.label_text.setText(_translate("LinuxAuth", "Txt file input"))
        self.enter_button_2.setText(_translate("LinuxAuth", "Yes"))
        self.manual_button.setText(_translate("LinuxAuth", "Manual"))
        self.random_button.setText(_translate("LinuxAuth", "Random"))
        self.confirm_button.setText(_translate("LinuxAuth", "Confirm"))
        self.label_generate.setText(_translate("LinuxAuth", "Generate new password?"))
        self.label_old.setText(_translate("LinuxAuth", "Old password:"))
        self.label_new.setText(_translate("LinuxAuth", "New password:"))
        self.label_repeat.setText(_translate("LinuxAuth", "New password:"))
        self.exit_button.setText(_translate("LinuxAuth", "Exit"))

    def add_functions(self):
        self.add_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.back_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.back_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.settings_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.enter_button.clicked.connect(lambda: self.enter())
        self.reload_button.clicked.connect(lambda: self.writeOtp())
        self.plus_button.clicked.connect(lambda: self.writeSecret())
        self.file_button.clicked.connect(lambda: self.file_reader())
        self.enter_button_2.clicked.connect(lambda: self.hider())
        self.manual_button.clicked.connect(lambda : self.unhider())
        self.confirm_button.clicked.connect(lambda: self.change_password())
        self.random_button.clicked.connect(lambda: generate_password())
        self.exit_button.clicked.connect(lambda: self.exit())

    def writeOtp(self):
        if keyring.get_password(credentials.service_id, credentials.pos1) is None:
            show_popup_1()
        else:
            self.reload_button.hide()
            self.loading.show()
            self.loading.setMovie(self.movie)
            self.movie.start()
            QTimer.singleShot(30000, lambda: self.reload_button.show())
            QTimer.singleShot(30000, lambda: self.TOTP.setText("– – – – – –"))
            QTimer.singleShot(30000, lambda: self.loading.hide())
            QTimer.singleShot(30000, lambda: self.movie.stop())
            key = base64.b32decode(cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos1),
                                               cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos2), credentials.secret_key)), True)
            totp = self.totp(key)
            self.TOTP.setText(str(totp).replace("", " ")[1: -1])

    def enter(self):
        if cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos2), credentials.secret_key) == self.password_line.text():
            self.stackedWidget.setCurrentWidget(self.page_1)
        else:
            self.password_line.setText("")
            show_popup_3()

    def totp(self, key):
        msg = int(math.floor(time.time() / 30))
        hashcode = hmac.new(key, struct.pack('i', msg), 'sha1').hexdigest()
        offset = int(hashcode[-1], 32)
        trunc = int(hashcode[offset * 2:(offset * 2) + 8], 32) & 0x7fffffff
        totp = trunc % 1000000
        return totp

    def hider(self):
        self.enter_button_2.hide()
        self.manual_button.show()
        self.random_button.show()

    def unhider(self):
        self.label_generate.hide()
        self.manual_button.hide()
        self.random_button.hide()
        self.confirm_button.show()
        if (pass_check() is False):
            self.label_new.setGeometry(QRect(20, 110, 241, 41))
            self.new_line.setGeometry(QRect(260, 90, 351, 81))
            self.label_repeat.setGeometry(20, 200, 241, 41)
            self.repeat_line.setGeometry(260, 180, 351, 81)
            self.old_line.show()
            self.label_old.show()
        else:
            self.label_new.setGeometry(QRect(20, 60, 241, 41))
            self.new_line.setGeometry(QRect(260, 40, 351, 81))
            self.label_repeat.setGeometry(20, 180, 241, 41)
            self.repeat_line.setGeometry(260, 160, 351, 81)
        self.label_new.show()
        self.label_repeat.show()
        self.new_line.show()
        self.repeat_line.show()

    def get_line_test(self):
        return str(self.textEdit.toPlainText())

    def change_password(self):
        new = self.new_line.text()
        if (pass_check() is False):
            old = self.old_line.text()
            if (old == cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos2), credentials.secret_key) and new != "" and self.new_line.text() == self.repeat_line.text()):
                change_secret(new)
                show_popup_2(new)
                new = cryptocode.encrypt(self.new_line.text(), credentials.secret_key)
                keyring.set_password(credentials.service_id, credentials.pos2, new)
                self.old_line.setText("")
            else:
                show_popup_3()
                self.old_line.setText("")
        else:
            if new != "" and self.new_line.text() == self.repeat_line.text():
                change_secret(new)
                show_popup_2(new)
                new = cryptocode.encrypt(self.new_line.text(), credentials.secret_key)
                keyring.set_password(credentials.service_id, credentials.pos2, new)
            else:
                show_popup_3()
        self.old_line.setText("")
        self.new_line.setText("")
        self.repeat_line.setText("")
        self.old_line.hide()
        self.new_line.hide()
        self.label_new.hide()
        self.label_old.hide()
        self.repeat_line.hide()
        self.label_repeat.hide()
        self.confirm_button.hide()
        self.label_generate.show()
        self.enter_button_2.show()

    def writeSecret(self):
        if len(self.get_line_test()) != 32 or English(self.get_line_test()) == False:
            show_popup()
        else:
            self.plus_button.hide()
            self.check_button.show()
            QTimer.singleShot(1000, lambda: self.check_button.hide())
            QTimer.singleShot(1000, lambda: self.plus_button.show())
            keyring.set_password(credentials.service_id, credentials.pos1, cryptocode.encrypt(self.get_line_test(),
                                                                                       cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos2), credentials.secret_key)))
            self.textEdit.setText("")
        if pass_check() is True:
            generate_password()

    def file_reader(self):
        filename = QFileDialog.getOpenFileName()
        secret = word(filename[0])
        self.textEdit.setText(secret)

    def exit(self):
        exit()