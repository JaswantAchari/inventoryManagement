from PyQt5 import QtWidgets , QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox , QMainWindow
import sys
import mysql.connector as m
import sql as s
connection = m.connect(host = "127.0.0.1" , user = "root" , password = "sairam")
cursor1 = connection.cursor()


class admin(QMainWindow):

    def __init__(self):
        try:
            super(admin, self).__init__()
            self.setWindowTitle("Add Admin")

            self.setFixedHeight(400)
            self.setFixedWidth(600)

            line_Edit = QtGui.QFont()
            line_Edit.setPointSize(15)

            # Label font
            label_font = QtGui.QFont()
            label_font.setPointSize(15)
            label_font.setFamily("Arial Black")

            # Button font
            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(10)
            BTN_font.setFamily("Stencil")

            # username_label
            self.username_label = QtWidgets.QLabel(self)
            self.username_label.setText(" USERNAME : ")
            self.username_label.setGeometry(60, 100, 150, 30)
            self.username_label.setFont(label_font)
            self.username_label.setStyleSheet("background: White")

            # username_lE
            self.username_lE = QtWidgets.QLineEdit(self)
            self.username_lE.setGeometry(350, 100, 200, 30)
            self.username_lE.setFont(line_Edit)
            self.username_lE.setStyleSheet("background: White")
            self.username_lE.returnPressed.connect(self.next_le)

            # Password_label
            self.Password_label = QtWidgets.QLabel(self)
            self.Password_label.setText(" PASSWORD : ")
            self.Password_label.setGeometry(60, 150, 150, 30)
            self.Password_label.setFont(label_font)
            self.Password_label.setStyleSheet("background: White")

            # Password_LE
            self.Password_LE = QtWidgets.QLineEdit(self)
            self.Password_LE.setGeometry(350, 156, 200, 30)
            self.Password_LE.setEchoMode(QtWidgets.QLineEdit.Password)
            self.Password_LE.setStyleSheet("background: White")
            self.Password_LE.returnPressed.connect(self.next_le)

            # ConfirmPassword_label
            self.ConfirmPassword_label = QtWidgets.QLabel(self)
            self.ConfirmPassword_label.setText(" CONFIRM PASSWORD : ")
            self.ConfirmPassword_label.setGeometry(60, 200, 280, 30)
            self.ConfirmPassword_label.setFont(label_font)
            self.ConfirmPassword_label.setStyleSheet("background: White")

            # ConfirmPassword_LE
            self.ConfirmPassword_LE = QtWidgets.QLineEdit(self)
            self.ConfirmPassword_LE.setGeometry(350, 200, 200, 30)
            self.ConfirmPassword_LE.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ConfirmPassword_LE.setStyleSheet("background: White")
            self.ConfirmPassword_LE.returnPressed.connect(self.next_le)

            # NAME_label
            self.NAME_label = QtWidgets.QLabel(self)
            self.NAME_label.setText(" NAME : ")
            self.NAME_label.setGeometry(60, 250, 100, 30)
            self.NAME_label.setFont(label_font)
            self.NAME_label.setStyleSheet("background: White")

            # NAME_line Edit
            self.NAME_lE = QtWidgets.QLineEdit(self)
            self.NAME_lE.setGeometry(350, 250, 200, 30)
            self.NAME_lE.setFont(line_Edit)
            self.NAME_lE.setStyleSheet("background: White")
            self.NAME_lE.returnPressed.connect(self.checkpswd)

            # Signup_Button
            self.Signup_BTN = QtWidgets.QPushButton(self)
            self.Signup_BTN.setGeometry(140, 300, 90, 30)
            self.Signup_BTN.setText(" SIGN UP ")
            self.Signup_BTN.clicked.connect(self.checkpswd)
            self.Signup_BTN.setStyleSheet("background: White")

            # Back_Button
            self.Back_BTN = QtWidgets.QPushButton(self)
            self.Back_BTN.setGeometry(30, 30, 70, 40)
            self.Back_BTN.setText(" Back ")
            self.Back_BTN.setFont(BTN_font)
            self.Back_BTN.setStyleSheet("background: White")

            self.upda_sec_BTN = QtWidgets.QPushButton(self)
            self.upda_sec_BTN.setGeometry(240, 300, 90, 40)
            self.upda_sec_BTN.setText("Update\n Security key ")
            self.upda_sec_BTN.setStyleSheet("background: White")
            self.upda_sec_BTN.clicked.connect(self.updateKey)

            if self.Back_BTN.clicked:
                self.Back_BTN.clicked.connect(self.welcompage)
        except Exception as e:
            traceback.print_exc()
            msg(str(e))

    def welcompage(self):
        self.destroy()
        # self.p = WelcomePage()
        # self.p.show()

    def updateKey(self):
        self.o = Update_key()
        self.o.show()

    def next_le(self):
        self.focusNextChild()

    def checkpswd(self):
        if self.Password_LE.text() == self.ConfirmPassword_LE.text():
            self.Correct()
        elif self.Password_LE.text() != self.ConfirmPassword_LE.text():
            print("Password did not Match .")
            self.error()

    def Correct(self):
        try:
            # msg.setWindowTitle("Success")
            msg("PASSWORD IS SET ! ")
            a = self.username_lE.text()
            b = self.Password_LE.text()
            c = self.NAME_lE.text()
            print(f"insert into Admins_data values({a},{b},{c})")
            s.cursor1.execute(f"insert into admins_data values({a},{b},'{c}')")
            s.cursor1.execute("commit")

            self.username_lE.clear()
            self.NAME_lE.clear()
            self.ConfirmPassword_LE.clear()
            self.Password_LE.clear()
        except Exception as e:
            traceback.print_exc()
            msg(str(e))

    def error(self):
        msg("Your Passwords didn't Match")

app = QApplication(sys.argv)
A = admin()
A.show()
app.exec_()