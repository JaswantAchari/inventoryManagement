import traceback
from tkinter import Tk
import numpy as np
from PyQt5 import QtWidgets ,QtGui ,QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sql as s


class SellNow(QMainWindow):

    def __init__(self):
        super(SellNow, self).__init__()
        try:
            self.setWindowTitle("Sell Now Page")

            win = Tk()
            screen_width = int(win.winfo_screenwidth())
            screen_height = int(win.winfo_screenheight())

            self.setFixedHeight(screen_height)
            self.setFixedWidth(screen_width)

            background_image = resource_path('images/Purchases.png')

            background_image_url = background_image.replace("\\", "/")
            print(f"Formatted background image path: {background_image_url}")

            self.setStyleSheet(f'background-image: url({background_image_url});')

            #   horizontal line
            self.line = QtWidgets.QLabel(self)
            ht_ratio = int(screen_height) // 2
            y1_ = ht_ratio + 300
            y1 = screen_height - y1_
            self.line.setGeometry(0, y1, screen_width, 2)
            self.line.setStyleSheet("background: black")

            # Label font
            self.label_font = QtGui.QFont()
            self.label_font.setPointSize(20)
            self.label_font.setFamily("Arial Black")
            self.label = QtWidgets.QLabel

            # Operator Font
            OPER_FONT = QtGui.QFont()
            OPER_FONT.setPointSize(20)
            OPER_FONT.setFamily("28 Days Later")

            line_Edit = QtGui.QFont()
            line_Edit.setPointSize(20)

            # Main font
            main_font = QtGui.QFont()
            main_font.setPointSize(30)
            main_font.setFamily("Cooper Black")

            # Button font
            self.BTN_font = QtGui.QFont()
            self.BTN_font.setPointSize(15)
            self.BTN_font.setFamily("Stencil")

            # Sales Label
            self.text_label = QtWidgets.QLabel(self)
            self.text_label.setText(" Sales ")
            self.text_label.setGeometry(screen_width // 2 - 70, 30, 140, 30)
            self.text_label.setFont(main_font)

            # Operator Label
            self.operator_Label = QtWidgets.QLabel(self)
            self.operator_Label.setText("Operator")
            self.operator_Label.setGeometry(300, 30, 120, 30)
            self.operator_Label.setFont(self.BTN_font)

            # Operator Line Edit
            self.operator_LE = QtWidgets.QLineEdit(self)
            s.cursor1.execute(f"select name from admins_data where user_id ={user}")
            rows1 = s.cursor1.fetchone()
            name = rows1[0]
            self.operator_LE.setText(name)
            self.operator_LE.setGeometry(430, 30, 120, 30)
            self.operator_LE.setEnabled(False)
            self.operator_LE.setFont(OPER_FONT)

            # Back Button
            self.Back_BTN = QtWidgets.QPushButton(self)
            self.Back_BTN.setGeometry(30, 30, 200, 30)
            self.Back_BTN.setText("Back")
            self.Back_BTN.setFont(self.BTN_font)
            self.Back_BTN.setStyleSheet("background: White")

            # Grand Total Label
            self.Grand_total_label = QtWidgets.QLabel(self)
            self.Grand_total_label.setText(" Grand Total ")
            ht_ratio = int(screen_height) // 2
            y1_ = ht_ratio + 300
            y1 = screen_height - y1_
            self.Grand_total_label.setGeometry(screen_width // 2 - 250, screen_height // 2 + y1 + 175, 150, 30)
            self.Grand_total_label.setFont(self.BTN_font)

            # Grand total Line Edit
            self.Grand_total_LE = QtWidgets.QLineEdit(self)
            self.Grand_total_LE.setGeometry(screen_width // 2 - 100, screen_height // 2 + y1 + 175, 130, 30)
            self.Grand_total_LE.setFont(line_Edit)
            self.Grand_total_LE.setReadOnly(True)
            self.Grand_total_LE.setStyleSheet("background: White")

            # Amt paying by the customer label
            self.Amt_paying_label = QtWidgets.QLabel(self)
            self.Amt_paying_label.setText(" Paying ")
            self.Amt_paying_label.setGeometry(screen_width // 2 + 50, screen_height // 2 + y1 + 175, 100, 30)
            self.Amt_paying_label.setFont(self.BTN_font)

            # Amt paying by the customer Line Edit
            self.Amt_paying_LE = QtWidgets.QLineEdit(self)
            self.Amt_paying_LE.setGeometry(screen_width // 2 + 150, screen_height // 2 + y1 + 175, 130, 30)
            self.Amt_paying_LE.setFont(line_Edit)
            self.Amt_paying_LE.returnPressed.connect(self.Pay)
            self.Amt_paying_LE.setStyleSheet("background: White")

            # Pay Button
            self.Pay_BTN = QtWidgets.QPushButton(self)
            self.Pay_BTN.setGeometry(screen_width // 2 + 450, screen_height // 2 + y1 + 175, 130, 30)
            self.Pay_BTN.setText("Pay")
            self.Pay_BTN.setFont(self.BTN_font)
            self.Pay_BTN.clicked.connect(self.Pay)
            self.Pay_BTN.setStyleSheet("background:white")

            # Item code Label
            self.ItemCode_label = QtWidgets.QLabel(self)
            self.ItemCode_label.setText(" BARCODE  ")
            self.ItemCode_label.setGeometry(150, y1 + 10, 180, 30)
            self.ItemCode_label.setFont(self.label_font)

            # Item code Line Edit
            self.ItemCode_LE = QtWidgets.QLineEdit(self)
            self.ItemCode_LE.setGeometry(330, y1 + 10, 130, 30)
            self.ItemCode_LE.setFont(line_Edit)
            self.ItemCode_LE.setStyleSheet("background: White")
            self.ItemCode_LE.returnPressed.connect(self.search)
            self.ItemCode_LE.setFocus()

            # Search Button
            self.search_Btn = QtWidgets.QPushButton(self)
            self.search_Btn.setIcon(QtGui.QIcon("Search.png"))
            self.search_Btn.setStyleSheet("background-image : url(search.png);")
            self.search_Btn.setGeometry(480, y1 + 10, 30, 30)
            self.search_Btn.clicked.connect(self.search)

            # Items List
            self.items_LST = QtWidgets.QListWidget(self)
            A = 350
            self.items_LST.setGeometry(screen_width - 350, y1 + 10, 350, screen_height - y1 - 160)
            self.items_LST.setFont(self.label_font)
            self.items_LST.setStyleSheet("background:white")

            # table Widget
            self.tableWidget = QTableWidget(self)
            self.tableWidget.setGeometry(40, y1 + 50, screen_width // 2 + 240, 500)
            self.tableWidget.setColumnCount(6)
            self.tableWidget.acceptDrops()
            self.tableWidget.setHorizontalHeaderLabels(
                ['Barcode', 'Item no', 'Particulars', 'PRICE', 'QUANTITY', 'Total'])
            self.font = QFont('Arial', 12, QFont.Bold)
            self.tableWidget.horizontalHeader().setFont(self.font)
            self.tableWidget.setColumnWidth(0, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(1, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(2, int(300 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(3, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(4, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(5, int(150 / 1920 * screen_width))
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.tableWidget.setStyleSheet("background: white")

            s.cursor1.execute(
                "select concat(barcode,'-','-','-','-','-','-',item_name) from inventory where Qty_avail !=0  order by barcode;")
            list_items = s.cursor1.fetchall()
            for row in list_items:
                self.items_LST.addItem(row[0])
            if self.Back_BTN.clicked:
                self.Back_BTN.clicked.connect(self.welcompage)

        except Exception as E:
            traceback.print_exc()
            msg(str(E))

    def Set_data(self):
        try:
            s.cursor1.execute(
                f"SELECT BARCODE, ITEM_NO, ITEM_NAME, PRICE, Qty_avail, 0 FROM inventory WHERE barcode = {self.code};")
            row = s.cursor1.fetchmany()

            for cur_row_index, k in enumerate(row):
                for j, col in enumerate(k):
                    self.tableWidget.setItem(cur_row_index, j, QTableWidgetItem(str(col)))

                self.spin_box = QtWidgets.QSpinBox(self)
                self.spin_box.setObjectName(str(cur_row_index))
                self.spin_box.valueChanged.connect(self.get_spinbox_value_changed)
                self.tableWidget.setCellWidget(cur_row_index, 4, self.spin_box)

            s.cursor1.execute(f"SELECT Qty_avail FROM inventory WHERE barcode = {self.code}")
            rows = s.cursor1.fetchone()

            if int(rows[0]) > 1:
                self.spin_box.setMaximum(int(rows[0]))
                self.spin_box.setMinimum(0)
            else:
                print("Quantity not found")

        except Exception as e:
            traceback.print_exc()
            msg(str(e))

    def search(self):
        try:
            row_position = self.tableWidget.rowCount()
            self.code = self.ItemCode_LE.text()

            if self.code == '':
                msg("YOU HAVE NOT ENTERED ANYTHING AS THE BARCODE \n\t ENTER THE BARCODE :) ")
            else:
                self.spin_box = QtWidgets.QSpinBox(self)
                s.cursor1.execute(
                    f"SELECT BARCODE, ITEM_NO, ITEM_NAME, PRICE, Qty_avail, 0 FROM inventory WHERE barcode = {self.code};")
                self.row = s.cursor1.fetchall()

            isItemAvailable = bool(len(self.row))

            if not isItemAvailable:
                print("Here NO Output")
                msg(f"There is no item With this barcode {self.code}\n\t Please check the barcode :)")
                return

            Query = f"SELECT Qty_avail FROM inventory WHERE barcode = {self.code}"
            s.cursor1.execute(Query)
            no = s.cursor1.fetchall()

            for row1 in range(self.tableWidget.rowCount()):
                existing_barcode = self.tableWidget.item(row1, 0).text()
                if existing_barcode == self.code:
                    self.spin_box = self.tableWidget.cellWidget(row1, 4)
                    new_quantity = self.spin_box.value() + 1
                    self.spin_box.setValue(new_quantity)
                    self.update_row_total(row1, self.spin_box.value())
                    self.update_grand_total()
                    return

            else:
                self.tableWidget.insertRow(0)
                self.Set_data()
                self.update_grand_total()

        except Exception as e:
            traceback.print_exc()
            msg(str(e))

    def get_spinbox_value_changed(self):
        sender = self.sender()
        row = self.tableWidget.indexAt(sender.pos()).row()
        value = sender.value()
        self.update_row_total(row, value)

    def update_row_total(self, row1, quantity):
        try:
            price = float(self.tableWidget.item(row1, 3).text())
            self.total = price * quantity
            if row1 < self.tableWidget.rowCount():
                self.tableWidget.setItem(row1, 5, QTableWidgetItem(str(self.total)))
                self.update_grand_total()
            else:
                print(f"Invalid row index: {row1}")
        except Exception as e:
            traceback.print_exc()
            msg(str(e))

    def update_grand_total(self):
        total = []
        for i in range(self.tableWidget.rowCount()):
            a = self.tableWidget.item(i, 5).text()
            total.append(float(a))

        self.Grand_total_LE.setText(str(sum(total)))

    def Pay(self):
        try:
            gt = float(self.Grand_total_LE.text())
            amt = float(self.Amt_paying_LE.text())
            change = amt - gt
            msg(f"\t\tPaid\n\tchange to be given back is {change}\t")
            self.Grand_total_LE.clear()
            self.Amt_paying_LE.clear()
            print(F"Change is {change}")
            for i in range(self.tableWidget.rowCount()):
                barcode = self.tableWidget.item(i, 0).text()
                item_no = self.tableWidget.item(i, 1).text()
                item_name = self.tableWidget.item(i, 2).text()
                unit_price = self.tableWidget.item(i, 3).text()
                Qty_bought = self.tableWidget.cellWidget(i, 4).text()
                total = self.tableWidget.item(i, 5).text()
                Query = f"select Qty_avail from inventory where barcode = {barcode}"
                s.cursor1.execute(Query)
                no = s.cursor1.fetchall()
                # print(f"THIS IS QTY AVAIL of {item_name} ", no[0])
                Query1 = (f"update inventory set Qty_avail = Qty_avail-{Qty_bought} where barcode = {barcode};")
                Query2 = (
                    f"insert into sales values({barcode},current_date(),{item_no},'{item_name}',{unit_price},{Qty_bought},{total})")
                s.cursor1.execute(Query2)
                s.connection.commit()
                s.cursor1.execute(Query1)
                s.connection.commit()
                s.cursor1.execute(Query)
                present_no = s.cursor1.fetchall()
                # print(f"THIS IS UPDATED qty of {item_name} ", present_no[0])

            self.tableWidget.setRowCount(0)

            self.items_LST.clear()

            s.cursor1.execute(
                "select concat(barcode,'-','-',item_name,'-',Qty_avail) from inventory where Qty_avail != 0 order by barcode;")
            list_items = s.cursor1.fetchall()
            for row in list_items:
                self.items_LST.addItem(row[0])

        except Exception as e:
            traceback.print_exc()
            msg(str(e))

    def welcompage(self):
        self.destroy()
        self.p = WelcomePage()
        self.p.show()

app = QApplication(sys.argv)
P = SellNow()
P.show()
app.exec_()