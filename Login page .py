from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox , QMainWindow
import sys
from customtkinter import *

Username = "1"
password = "1"


class login(QMainWindow):

    def __init__(self):
        try:
            super(login, self).__init__()
            self.setWindowTitle("Login Page")

            self.tabWidget = None
            self.setFixedHeight(500)
            self.setFixedWidth(750)

            # Label font
            label_font = QtGui.QFont()
            label_font.setPointSize(20)
            label_font.setFamily("Arial Black")

            # Text font
            txt_font = QtGui.QFont()
            txt_font.setPointSize(25)
            txt_font.setFamily("Arial Black")

            # Line edit font
            line_Edit = QtGui.QFont()
            line_Edit.setPointSize(20)

            # Username Label
            self.username_label = QtWidgets.QLabel(self)
            self.username_label.setText(" USERNAME : ")
            self.username_label.setGeometry(150, 20, 200, 50)
            self.username_label.setFont(label_font)
            self.username_label.setStyleSheet("background:white")

            # Username Line Edit
            self.username_lE = QtWidgets.QLineEdit(self)
            self.username_lE.setGeometry(380, 20, 200, 50)
            self.username_lE.setFont(line_Edit)
            self.username_lE.returnPressed.connect(self.next_lE)
            self.username_lE.setPlaceholderText("USER ID")
            self.username_lE.setStyleSheet("background:white")

            # Password Label
            self.Password_label = QtWidgets.QLabel(self)
            self.Password_label.setText(" PASSWORD : ")
            self.Password_label.setGeometry(150, 90, 200, 50)
            self.Password_label.setFont(label_font)
            self.Password_label.setStyleSheet("background:white")

            # Password Line Edit
            self.Password_LE = QtWidgets.QLineEdit(self)
            self.Password_LE.setGeometry(380, 90, 200, 50)
            self.Password_LE.setEchoMode(QtWidgets.QLineEdit.Password)
            self.Password_LE.returnPressed.connect(self.verify)
            self.Password_LE.setFont(line_Edit)
            self.Password_LE.setPlaceholderText("PASSWORD")
            self.Password_LE.setStyleSheet("background:white")

            # CheckBox
            self.checkbox = QtWidgets.QCheckBox("SHOW", self)
            self.checkbox.setGeometry(510, 150, 50, 20)
            self.checkbox.setStyleSheet("background:white")
            self.checkbox.toggled.connect(self.showpass)

            # login Button
            self.login_BTN = QtWidgets.QPushButton(self)
            self.login_BTN.setGeometry(270, 380, 150, 50)
            self.login_BTN.setText(" Login ")
            self.login_BTN.clicked.connect(self.verify)
            self.login_BTN.setFont(txt_font)
            self.login_BTN.setStyleSheet("background:white")

            background_image = resource_path('images/logo.png')

            background_image_url = background_image.replace("\\", "/")
            print(f"Formatted background image path: {background_image_url}")
            try:
                self.setStyleSheet(f'background-image: url({background_image_url});')
            except Exception as p:
                print(p)
        except Exception as e:
            traceback.print_exc()
            msg(str(e))

    def showpass(self, checked):
        if checked:
            self.Password_LE.setEchoMode(False)
        else:
            self.Password_LE.setEchoMode(QtWidgets.QLineEdit.Password)

    def next_lE(self):
        self.focusNextChild()

    def verify(self):
        try:
            global user
            pasword = self.Password_LE.text()
            user = self.username_lE.text()
            if (user == "" or pasword == ""):
                msg("YOU HAVE NOT ENTERED THE USERNAME OR PASSWORD:) ")
            else:
                s.cursor1.execute(f"select user_id from admins_data where user_id = {user};")
                rows = s.cursor1.fetchone()
                a = rows
                s.cursor1.execute(f"select password from admins_data where user_id = {user};")
                row = s.cursor1.fetchone()
                p_ = row
                if p_ is None:
                    msg("Your Password or username is not correct!")
                elif pasword == str(p_[0]) and str(a[0]) == user:
                    self.destroy()
                    self.w = WelcomePage()
                    self.w.show()
                else:
                    msg("Your Password or username is not correct!")
        except Exception as e:
            traceback.print_exc()
            msg(str(e))

app = QApplication(sys.argv)
l = login()
l.show()
app.exec_()