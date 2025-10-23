from PyQt5 import QtWidgets ,QtGui ,QtCore
from PyQt5.QtGui import QFont
import tkinter
from tkinter import *
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QApplication, QTabWidget, QLabel, QMainWindow,QComboBox,QTableWidget,QTableWidgetItem
import sys
import sql as s


class Purchases(QMainWindow):

    def __init__(self):
        try:
            super(Purchases, self).__init__()
            self.screen()
            win = Tk()
            screen_width = int(win.winfo_screenwidth())
            screen_height = int(win.winfo_screenheight())
            self.setWindowTitle("Purchases Page")

            self.setFixedHeight(screen_height)
            self.setFixedWidth(screen_width)

            # OPER_FONT
            OPER_FONT = QtGui.QFont()
            OPER_FONT.setPointSize(20)
            OPER_FONT.setFamily("28 Days Later")

            # label_font
            label_font = QtGui.QFont()
            label_font.setPointSize(20)
            label_font.setFamily("Arial Black")
            label = QtWidgets.QLabel

            # main_font
            main_font = QtGui.QFont()
            main_font.setPointSize(30)
            main_font.setFamily("Cooper Black")

            # Button font
            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(15)
            BTN_font.setFamily("Stencil")

            # Com_font
            Com_font = QtGui.QFont()
            Com_font.setPointSize(15)
            Com_font.setFamily("Times New Roman")

            line_Edit = QtGui.QFont()
            line_Edit.setPointSize(20)

            self.text_label = QtWidgets.QLabel(self)
            self.text_label.setText("PURCHASES")

            ratio = int(screen_width) // 2
            x_ = ratio + 135
            x = screen_width - x_
            y_ = screen_height - 30
            y = screen_height - y_
            self.text_label.setGeometry(x, y, 270, 30)
            self.text_label.setFont(main_font)

            #  Operator label
            self.operator_Label = QtWidgets.QLabel(self)
            self.operator_Label.setText("Operator")
            self.operator_Label.setGeometry(300, 30, 120, 30)
            self.operator_Label.setFont(BTN_font)

            # operator lineEdit
            self.operator_LE = QtWidgets.QLineEdit(self)
            s.cursor1.execute(f"select name from admins_data where user_id ={user}")
            rows1 = s.cursor1.fetchone()
            name = rows1[0]
            self.operator_LE.setText(name)
            self.operator_LE.setGeometry(430, 30, 120, 30)
            self.operator_LE.setFont(OPER_FONT)
            self.operator_LE.setEnabled(False)

            # Back Button
            self.Back_BTN = QtWidgets.QPushButton(self)
            self.Back_BTN.setGeometry(30, 30, 200, 30)
            self.Back_BTN.setText("Back")
            self.Back_BTN.setFont(BTN_font)
            self.Back_BTN.setStyleSheet("background: White")

            # Add purchases Button
            self.Add_pur_BTN = QtWidgets.QPushButton(self)
            ratio1 = int(screen_width) // 3
            x_1 = ratio1 - 250
            x1 = screen_width - x_1
            y1_ = screen_height - 30
            y1 = screen_height - y1_

            self.Add_pur_BTN.setGeometry(x1, y1, 210, 30)
            self.Add_pur_BTN.setText("Add New Purchase")
            self.Add_pur_BTN.setFont(BTN_font)
            self.Add_pur_BTN.setStyleSheet("background: White")

            # update Button
            self.update_inv_BTN = QtWidgets.QPushButton(self)
            self.update_inv_BTN.setGeometry(x1 - 80, 100, 210, 30)
            self.update_inv_BTN.setText("Update Stock ")
            self.update_inv_BTN.setFont(BTN_font)
            self.update_inv_BTN.setStyleSheet("background: White")
            self.update_inv_BTN.clicked.connect(self.update)

            self.Back_BTN.clicked.connect(self.welcompage)
            self.Add_pur_BTN.clicked.connect(self.AddPur)

            # Add suppliers Button
            self.Add_sup_BTN = QtWidgets.QPushButton(self)
            ratio2 = int(screen_width) // 3
            x2_ = ratio2 - 40
            x2 = screen_width - x2_
            y2_ = screen_height - 30
            y2 = screen_height - y2_
            self.Add_sup_BTN.setGeometry(x2, y2, 200, 30)
            self.Add_sup_BTN.setText("Add supplier")
            self.Add_sup_BTN.setFont(BTN_font)
            self.Add_sup_BTN.setStyleSheet("background: White")
            self.Add_sup_BTN.clicked.connect(self.Addsup)

            # done Button
            self.done_btn = QtWidgets.QPushButton(self)
            self.done_btn.setText("DONE")
            self.done_btn.setFont(BTN_font)
            self.done_btn.setGeometry(360, 100, 80, 30)
            self.done_btn.setStyleSheet("background: White")
            self.done_btn.clicked.connect(self.done)

            #  combo box of supplier names
            self.combo3 = QComboBox(self)
            self.combo3.setGeometry(120, 100, 200, 30)
            self.combo3.setFont(Com_font)

            s.cursor1.execute("select sup_name from store.suppliers")
            sup_names = s.cursor1.fetchall()
            for name in sup_names:
                self.combo3.addItem(name[0])

            # Table Widget
            self.tableWidget = QTableWidget(self)
            self.tableWidget.setColumnCount(7)
            y3_ = screen_height - 250
            y3 = screen_height - y3_
            self.tableWidget.setGeometry(40, y3, screen_width - 80, screen_height - y3 - 100)
            self.tableWidget.setStyleSheet("Background : white")
            self.tableWidget.setHorizontalHeaderLabels(
                ['Barcode', 'Supplier ID', 'Item no', 'Particulars', 'PRICE', 'QUANTITY', 'Grand Total'])
            self.font = QFont('Arial', 12, QFont.Bold)  # Create a QFont object with desired attributes
            self.tableWidget.horizontalHeader().setFont(self.font)
            self.tableWidget.setColumnWidth(0, int(280 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(1, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(2, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(3, int(750 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(4, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(5, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(6, int(150 / 1920 * screen_width))
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

            background_image = resource_path('images/Purchases.png')

            background_image_url = background_image.replace("\\", "/")
            print(f"Formatted background image path: {background_image_url}")

            self.setStyleSheet(f'background-image: url({background_image_url});')
        except Exception as ex:
            traceback.print_exc()
            msg(str(ex))

    def Addsup(self):
        self.sup = addsupplier()
        self.sup.show()

    def update(self):
        self.u = update()
        self.u.show()

    def done(self):
        name = self.combo3.currentText()
        try:
            self.tableWidget.clear()
            s.cursor1.execute(f'Select sup_id from suppliers where sup_name = "{name}"')
            rows = s.cursor1.fetchone()
            if len(rows) == 0:
                pass
            elif (len(rows) <= 1):
                for i in range(len(rows)):
                    self.id = rows[i]
                    print(self.id)
                s.cursor1.execute(
                    f"select Barcode,supplier_id,itemno,particular,unit_price,Quantity,Totalprice from purchases where supplier_id ={self.id}")
                row = s.cursor1.fetchall()
                no = len(row)
                self.tableWidget.setRowCount(no)
                if row == []:
                    msg("NOTHING YOU BOUGHT FROM HIM .")
                print("BOUGHT", row)
                for i, k in enumerate(row):
                    for j, col in enumerate(k):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                self.tableWidget.setRowCount(len(row))
                for i, k in enumerate(row):
                    for j, col in enumerate(k):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                self.tableWidget.setHorizontalHeaderLabels(
                    ['Barcode', 'Supplier ID', 'Item no', 'Particulars', 'PRICE', 'QUANTITY', 'Grand Total'])

        except Exception as e:
            self.tableWidget.setHorizontalHeaderLabels(
                ['Barcode', 'Supplier ID', 'Item no', 'Particulars', 'PRICE', 'QUANTITY', 'Grand Total'])
            traceback.print_exc()
            msg(str(e))

    def clicked(self, index):
        a = self.combo3.currentText()
        print(a)

    def welcompage(self):
        self.destroy()
        self.p = WelcomePage()
        self.p.show()

    def AddPur(self):
        self.Ap = addPurchases()
        self.Ap.show()

app = QApplication(sys.argv)
P = Purchases()
P.show()
app.exec_()