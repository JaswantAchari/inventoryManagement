from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox,QMainWindow , QTableWidget
import sys
import sql as s


class addsupplier(QMainWindow):

    def __init__(self):
        super(addsupplier, self).__init__()
        self.setWindowTitle("Add Supplier Page")

        self.setFixedHeight(400)
        self.setFixedWidth(500)

        # Label font
        label_font = QtGui.QFont()
        label_font.setPointSize(15)
        label_font.setFamily("Arial Black")
        label = QtWidgets.QLabel
        label.setStyleSheet(self, "background-image: url()")

        # Main font
        main_font = QtGui.QFont()
        main_font.setPointSize(12)
        main_font.setFamily("Cooper Black")

        # Button Font
        BTN_font = QtGui.QFont()
        BTN_font.setPointSize(15)
        BTN_font.setFamily("Stencil")

        line_Edit = QtGui.QFont()
        line_Edit.setPointSize(20)

        # Name label
        self.NAME_label = QtWidgets.QLabel(self)
        self.NAME_label.setText("NAME : ")
        self.NAME_label.setGeometry(20, 100, 150, 30)
        self.NAME_label.setFont(label_font)

        # Name Line Edit
        self.NAME_lE = QtWidgets.QLineEdit(self)
        self.NAME_lE.setGeometry(300, 100, 130, 30)
        self.NAME_lE.setFont(line_Edit)
        self.NAME_lE.returnPressed.connect(self.next_lE)

        # Address Label
        self.Address_label = QtWidgets.QLabel(self)
        self.Address_label.setText("Address :")
        self.Address_label.setGeometry(20, 150, 150, 30)
        self.Address_label.setFont(label_font)

        # Address Line Edit
        self.Address_LE = QtWidgets.QLineEdit(self)
        self.Address_LE.setGeometry(300, 150, 130, 30)
        self.Address_LE.setFont(line_Edit)
        self.Address_LE.returnPressed.connect(self.next_lE)

        # Phone No Label
        self.Phone_No_label = QtWidgets.QLabel(self)
        self.Phone_No_label.setText("Phone No :")
        self.Phone_No_label.setGeometry(20, 200, 200, 30)
        self.Phone_No_label.setFont(label_font)

        # Phone no Line Edit
        self.Phone_No_LE = QtWidgets.QLineEdit(self)
        self.Phone_No_LE.setGeometry(300, 200, 130, 30)
        self.Phone_No_LE.setFont(line_Edit)
        self.Phone_No_LE.returnPressed.connect(self.next_lE)

        # phone no 2 label
        self.phone_no_2_label = QtWidgets.QLabel(self)
        self.phone_no_2_label.setText("Alternate Phone no :")
        self.phone_no_2_label.setGeometry(20, 250, 220, 30)
        self.phone_no_2_label.setFont(label_font)

        # Phone no 2 Line Edit
        self.phone_no_2_LE = QtWidgets.QLineEdit(self)
        self.phone_no_2_LE.setGeometry(300, 250, 130, 30)
        self.phone_no_2_LE.setFont(line_Edit)
        self.phone_no_2_LE.returnPressed.connect(self.add)

        # Add Suppliers Button
        self.add_BTN = QtWidgets.QPushButton(self)
        self.add_BTN.setGeometry(170, 300, 180, 30)
        self.add_BTN.setText("ADD SUPPLIER")
        self.add_BTN.setFont(BTN_font)
        self.add_BTN.clicked.connect(self.add)

        # See suppliers Button
        self.see_BTN = QtWidgets.QPushButton(self)
        self.see_BTN.setGeometry(170, 350, 180, 30)
        self.see_BTN.setText("SEE SUPPLIERS")
        self.see_BTN.setFont(BTN_font)
        self.see_BTN.clicked.connect(self.sup)

        # Back Button
        self.Back_BTN = QtWidgets.QPushButton(self)
        self.Back_BTN.setGeometry(30, 30, 60, 30)
        self.Back_BTN.setText("Back")
        self.Back_BTN.setFont(BTN_font)
        self.Back_BTN.setStyleSheet("background: White")
        self.Back_BTN.clicked.connect(self.purchase)

    def add(self):
        Name1 = self.NAME_lE.text()
        address1 = self.Address_LE.text()
        phone_number = self.Phone_No_LE.text()
        alt_phone_no = self.phone_no_2_LE.text()
        print("use store")
        s.cursor1.execute("use store")
        insert_query = f"insert into suppliers (SUP_NAME,SUP_PHONE_NO,SUP_ADDRESS,SUP_ALT_NO) values('{Name1}',{phone_number},'{address1}',{alt_phone_no})"
        print(insert_query)
        print("inserting values")
        try:
            s.cursor1.execute(insert_query)
            s.cursor1.execute("commit")
        except Exception as e:
            traceback.print_exc()
            msg(str(e))
        msg("SUCCESSFULLY ADDED!")
        self.NAME_lE.clear()
        self.Address_LE.clear()
        self.Phone_No_LE.clear()
        self.phone_no_2_LE.clear()

    def next_lE(self):
        self.focusNextChild()

    def sup(self):
        self.a = see_supplier()
        self.a.show()

    def purchase(self):
        self.destroy()

app = QApplication(sys.argv)
l = addsupplier()
l.show()
app.exec_()
