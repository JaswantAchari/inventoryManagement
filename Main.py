import traceback, sys, mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QDate
from tkinter import Tk
from datetime import datetime
import os
from PyQt5.QtWidgets import (QDialog, QApplication, QTabWidget, QLabel, QMainWindow, QComboBox, QTableWidget,
                             QTableWidgetItem, QMessageBox, QDateEdit, QFrame, QCalendarWidget)
import sql as s
from fpdf import FPDF


# Message function for my Whole Project
def msg(text):
      Msg = QMessageBox()
      Msg.setWindowTitle("EXCEPTION")
      Msg.setText(text)
      Msg.setFixedSize(200, 120)
      Msg.exec()

def resource_path(relative_path):
    try:
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        resource_full_path = os.path.join(base_path, relative_path)

        return resource_full_path
    except Exception as e:
        print(f"Error in resource_path: {e}")
        return relative_path1


# Todo : Login Page
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
                  label_font.setPointSize(15)
                  label_font.setFamily("Arial Black")

                  # Text font
                  txt_font = QtGui.QFont()
                  txt_font.setPointSize(10)
                  txt_font.setFamily("Arial Black")

                  # Line edit font
                  line_Edit = QtGui.QFont()
                  line_Edit.setPointSize(20)

                  # Username Label
                  self.username_label = QtWidgets.QLabel(self)
                  self.username_label.setText("USERNAME")
                  self.username_label.setGeometry(120, 20, 200, 50)
                  self.username_label.setFont(label_font)
                  self.username_label.setStyleSheet("background:white")

                  # Username Line Edit
                  self.username_lE = QtWidgets.QLineEdit(self)
                  self.username_lE.setGeometry(380, 20, 250, 50)
                  self.username_lE.setFont(line_Edit)
                  self.username_lE.returnPressed.connect(self.next_lE)
                  self.username_lE.setPlaceholderText("USER ID")
                  self.username_lE.setStyleSheet("background:white")

                  # Password Label
                  self.Password_label = QtWidgets.QLabel(self)
                  self.Password_label.setText("PASSWORD")
                  self.Password_label.setGeometry(120, 90, 200, 50)
                  self.Password_label.setFont(label_font)
                  self.Password_label.setStyleSheet("background:white")

                  # Password Line Edit
                  self.Password_LE = QtWidgets.QLineEdit(self)
                  self.Password_LE.setGeometry(380, 90, 250, 50)
                  self.Password_LE.setEchoMode(QtWidgets.QLineEdit.Password)
                  self.Password_LE.returnPressed.connect(self.verify)
                  self.Password_LE.setFont(line_Edit)
                  self.Password_LE.setPlaceholderText("PASSWORD")
                  self.Password_LE.setStyleSheet("background:white")

                  # CheckBox
                  self.checkbox = QtWidgets.QCheckBox("SHOW",self)
                  self.checkbox.setGeometry(520,150,80,20)
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

      def showpass(self,checked):
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

# Todo : Welcome Page
class WelcomePage(QMainWindow):

      def __init__(self):
            super(WelcomePage, self).__init__()
            self.setWindowTitle("SUPER MARKET")
            '''self.setStyleSheet("""
                            QLabel {
                                font-size: 20px;
                                color: #000;
                            }
                            QPushButton {
                                background-color: #FFFFFF;
                                color: black;
                                border-radius: 5px;
                                padding: 10px;
                                font-size: 14px;
                            }
                            QPushButton:hover {
                                background-color: #FF00FF;
                            }
                        """)'''

            self.setFixedHeight(500)
            self.setFixedWidth(800)

            label_font = QtGui.QFont()
            label_font.setPointSize(17)
            label_font.setFamily("Arial Black")

            background_image = resource_path('images/download_(9)-sBf4iQeLr-transformed (1).jpg')

            background_image_url = background_image.replace("\\", "/")
            print(f"Formatted background image path: {background_image_url}")

            self.setStyleSheet(f'background-image: url({background_image_url});')

            # Button font
            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(15)
            BTN_font.setFamily("Stencil")

            OPER_FONT = QtGui.QFont()
            OPER_FONT.setPointSize(15)
            OPER_FONT.setFamily("28 Days Later")

            # Operator label
            self.operator_Label = QtWidgets.QLabel(self)
            self.operator_Label.setText(" Operator : ")
            self.operator_Label.setGeometry(10, 30, 170, 30)
            self.operator_Label.setFont(BTN_font)
            self.operator_Label.setStyleSheet("background: White")

            # Operator LineEdit
            self.operator_LE = QtWidgets.QLineEdit(self)
            s.cursor1.execute(f"select name from admins_data where user_id ={user}")
            rows1 = s.cursor1.fetchone()
            name = rows1[0]
            self.operator_LE.setText(f" {name} ")
            self.operator_LE.setGeometry(190, 30, 120, 30)
            self.operator_LE.setEnabled(False)
            self.operator_LE.setFont(OPER_FONT)
            self.operator_LE.setStyleSheet("background: White")

            # logout Button
            self.LOGOUT_BTN = QtWidgets.QPushButton(self)
            self.LOGOUT_BTN.setText("LOGOUT")
            self.LOGOUT_BTN.setGeometry(600, 30, 160, 30)
            self.LOGOUT_BTN.setFont(label_font)
            self.LOGOUT_BTN.setStyleSheet("background: White")
            self.LOGOUT_BTN.clicked.connect(self.back)

            # Purchases Button
            self.Purchase_BTN = QtWidgets.QPushButton(self)
            self.Purchase_BTN.setGeometry(90, 200, 200, 30)
            self.Purchase_BTN.setText("Purchases")
            self.Purchase_BTN.setFont(BTN_font)
            self.Purchase_BTN.setStyleSheet("background: White")

            # sale Button
            self.Sale_BTN = QtWidgets.QPushButton(self)
            self.Sale_BTN.setGeometry(90, 300, 200, 30)
            self.Sale_BTN.setText("Sell Now")
            self.Sale_BTN.setFont(BTN_font)
            self.Sale_BTN.setStyleSheet("background: White")

            # Total sales Button
            self.TotalSales_BTN = QtWidgets.QPushButton(self)
            self.TotalSales_BTN.setGeometry(460, 200, 200, 30)
            self.TotalSales_BTN.setText("Total Sales ")
            self.TotalSales_BTN.setFont(BTN_font)
            self.TotalSales_BTN.setStyleSheet("background: White")

            # Item stock Button
            self.itemStock_BTN = QtWidgets.QPushButton(self)
            self.itemStock_BTN.setGeometry(460, 300, 200, 30)
            self.itemStock_BTN.setText("Inventory")
            self.itemStock_BTN.setFont(BTN_font)
            self.itemStock_BTN.setStyleSheet("background: White")

            # Admin Button
            self.Admin_BTN = QtWidgets.QPushButton(self)
            self.Admin_BTN.setGeometry(460, 400, 200, 30)
            self.Admin_BTN.setText("Add Admin")
            self.Admin_BTN.setFont(BTN_font)
            self.Admin_BTN.setStyleSheet("background: White")

            # Gst Button
            self.GST_BTN = QtWidgets.QPushButton(self)
            self.GST_BTN.setGeometry(90, 400, 200, 30)
            self.GST_BTN.setText("Gst Calc")
            self.GST_BTN.setFont(BTN_font)
            self.GST_BTN.setStyleSheet("background: White")

            self.Admin_BTN.clicked.connect(self.Adminpage)
            self.Purchase_BTN.clicked.connect(self.Purchasepage)
            self.Sale_BTN.clicked.connect(self.SalesPage)
            self.GST_BTN.clicked.connect(self.gst)
            self.TotalSales_BTN.clicked.connect(self.Totalsales)
            self.itemStock_BTN.clicked.connect(self.inventory)

      def Adminpage(self):
            self.sec = security()
            self.sec.show()

      def Purchasepage(self):
            self.destroy()
            self.p = Purchases()
            self.p.show()

      def SalesPage(self):
            self.destroy()
            self.s = SellNow()
            self.s.show()

      def gst(self):
            self.destroy()
            self.g = GstCalc()
            self.g.show()

      def Totalsales(self):
            self.destroy()
            self.TS = TOTALSALES()
            self.TS.show()

      def inventory(self):
            self.destroy()
            self.i = inventory()
            self.i.show()

      def back(self):
            self.destroy()
            self.a = login()
            self.a.show()

# Todo : Purchase Page
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

# Todo : addPurchases page
class addPurchases(QMainWindow):

      def __init__(self):
            super(addPurchases, self).__init__()
            self.setWindowTitle("Add Purchase Page")

            self.setFixedHeight(600)
            self.setFixedWidth(500)

            # Label Font
            label_font = QtGui.QFont()
            label_font.setPointSize(15)
            label_font.setFamily("Arial Black")
            label = QtWidgets.QLabel
            label.setStyleSheet(self, "background-image: url()")

            # Main Font
            main_font = QtGui.QFont()
            main_font.setPointSize(12)
            main_font.setFamily("Cooper Black")

            # Button font
            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(15)
            BTN_font.setFamily("Stencil")

            line_Edit = QtGui.QFont()
            line_Edit.setPointSize(20)

            #  barcode label
            self.barcode_lbl = QtWidgets.QLabel(self)
            self.barcode_lbl.setText("Barcode:")
            self.barcode_lbl.setGeometry(60, 60, 100, 30)
            self.barcode_lbl.setFont(label_font)

            # barcode line Edit
            self.barcode_LE = QtWidgets.QLineEdit(self)
            self.barcode_LE.setGeometry(300, 60, 130, 30)
            self.barcode_LE.setFont(line_Edit)
            self.barcode_LE.returnPressed.connect(self.next_lE)

            # supplier name
            self.sup_name_label = QtWidgets.QLabel(self)
            self.sup_name_label.setText("Supplier_Name:")
            self.sup_name_label.setGeometry(60, 100, 180, 30)
            self.sup_name_label.setFont(label_font)

            try:
                  # combo box of suppliers name
                  self.combo3 = QComboBox(self)
                  self.combo3.setGeometry(300, 100, 130, 30)
                  s.cursor1.execute("select sup_id,sup_name from store.suppliers")
                  sup_names = s.cursor1.fetchall()
                  for name in sup_names:
                        self.combo3.addItem(f"{name[1]}")
            except Exception as e:
                  traceback.print_exc()
                  msg(str(e))

            # Item no label
            self.item_no_label = QtWidgets.QLabel(self)
            self.item_no_label.setText("Item_no:")
            self.item_no_label.setGeometry(60, 150, 200, 30)
            self.item_no_label.setFont(label_font)

            try:
                  s.cursor1.execute("select max(item_no) from store.inventory")
                  item_no = s.cursor1.fetchone()
                  self.max_item_no = item_no[0]

                  self.item_no_LE = QtWidgets.QLineEdit(self)
                  self.item_no_LE.setGeometry(300, 156, 130, 30)
                  self.item_no_LE.setFont(line_Edit)
                  self.item_no_LE.setText(str(self.max_item_no + 1))
                  self.item_no_LE.setReadOnly(True)

            except Exception as e:
                  traceback.print_exc()
                  msg(str(e))

            # Invoice no label
            self.invoice_no_label = QtWidgets.QLabel(self)
            self.invoice_no_label.setText("Invoice_No:")
            self.invoice_no_label.setGeometry(60, 200, 200, 30)
            self.invoice_no_label.setFont(label_font)

            # invoice no Line Edit
            self.invoice_no_LE = QtWidgets.QLineEdit(self)
            self.invoice_no_LE.setGeometry(300, 200, 130, 30)
            self.invoice_no_LE.setFont(line_Edit)
            self.invoice_no_LE.returnPressed.connect(self.next_lE)

            # Item name label
            self.Item_name_label = QtWidgets.QLabel(self)
            self.Item_name_label.setText("Particular:")
            self.Item_name_label.setGeometry(60, 250, 150, 30)
            self.Item_name_label.setFont(label_font)

            # Item name Line Edit
            self.Item_name_LE = QtWidgets.QLineEdit(self)
            self.Item_name_LE.setGeometry(300, 250, 130, 30)
            self.Item_name_LE.setFont(line_Edit)
            self.Item_name_LE.returnPressed.connect(self.next_lE)

            # Unit price label
            self.PriceOfEach_label = QtWidgets.QLabel(self)
            self.PriceOfEach_label.setText("Unit_price:")
            self.PriceOfEach_label.setGeometry(60, 300, 150, 30)
            self.PriceOfEach_label.setFont(label_font)

            # unit price Line Edit
            self.PriceOfEach_LE = QtWidgets.QLineEdit(self)
            self.PriceOfEach_LE.setGeometry(300, 300, 130, 30)
            self.PriceOfEach_LE.setFont(line_Edit)
            self.PriceOfEach_LE.returnPressed.connect(self.next_lE)

            # Qty label
            self.Quantity_label = QtWidgets.QLabel(self)
            self.Quantity_label.setText("Quantity:")
            self.Quantity_label.setGeometry(60, 350, 150, 30)
            self.Quantity_label.setFont(label_font)

            # Qty Line Edit
            self.Quantity_LE = QtWidgets.QLineEdit(self)
            self.Quantity_LE.setGeometry(300, 350, 130, 30)
            self.Quantity_LE.setFont(line_Edit)
            self.Quantity_LE.returnPressed.connect(self.next_lE)

            # Total amt label
            self.Total_amt_label = QtWidgets.QLabel(self)
            self.Total_amt_label.setText("Total_Amount:")
            self.Total_amt_label.setGeometry(60, 400, 180, 30)
            self.Total_amt_label.setFont(label_font)

            # Total line Edit
            self.Total_amtLE = QtWidgets.QLineEdit(self)
            self.Total_amtLE.setGeometry(300, 400, 130, 30)
            self.Total_amtLE.setFont(line_Edit)

            # Add Button
            self.add_BTN = QtWidgets.QPushButton(self)
            self.add_BTN.setGeometry(190, 450, 180, 30)
            self.add_BTN.setText("ADD PURCHASE")
            self.add_BTN.setFont(BTN_font)
            self.add_BTN.clicked.connect(self.add)

            # Back Button
            self.Back_BTN = QtWidgets.QPushButton(self)
            self.Back_BTN.setGeometry(30, 10, 60, 30)
            self.Back_BTN.setText("Back")
            self.Back_BTN.setFont(BTN_font)
            self.Back_BTN.setStyleSheet("background: White")
            self.Back_BTN.clicked.connect(self.purchase)

      def add(self):
            global Sup_id
            try:
                  a = int(self.Quantity_LE.text())
                  b = int(self.PriceOfEach_LE.text())
                  c = str(a * b)
                  self.Total_amtLE.setText(c)
                  Barcode = self.barcode_LE.text()
                  Supplier_ID = self.combo3.currentText()
                  Item_no = self.item_no_LE.text()
                  Invoice_No = self.invoice_no_LE.text()
                  Particular = self.Item_name_LE.text()
                  Unit_price = self.PriceOfEach_LE.text()
                  Quantity = self.Quantity_LE.text()
                  Total_Amount = self.Total_amtLE.text()
                  print("use store")
                  s.cursor1.execute("use store")
                  s.cursor1.execute(f'Select sup_id from suppliers where sup_name = "{Supplier_ID}"')
                  rows = s.cursor1.fetchone()
                  for i in range(len(rows)):
                        Sup_id = rows[i]
                  bill_no = 0
                  self.Total_amtLE.setText(c)
                  insert_query = f"insert into purchases values( {Barcode},{Sup_id},{Item_no},{Invoice_No},'{Particular}',{Unit_price},'{Quantity}',{Total_Amount})"
                  insert_query1 = f"insert into inventory values({Barcode},{Item_no},'{Particular}',{Unit_price},'{Quantity}')"
                  s.cursor1.execute(insert_query1)
                  s.cursor1.execute("commit")
                  print(insert_query)
                  print("inserting values")
                  s.cursor1.execute(insert_query)
                  s.cursor1.execute("commit")
            except Exception as e:
                  traceback.print_exc()
                  msg(str(e))
            self.barcode_LE.clear()
            self.item_no_LE.clear()
            self.invoice_no_LE.clear()
            self.Item_name_LE.clear()
            self.PriceOfEach_LE.clear()
            self.Quantity_LE.clear()
            self.Total_amtLE.clear()
      def next_lE(self):
            self.focusNextChild()

      def purchase(self):
            self.destroy()

# Todo : Add Suppliers
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

# Todo : update
class update(QMainWindow):

      def __init__(self):
            super(update, self).__init__()
            self.setWindowTitle("Update Inventory Page")

            self.setFixedHeight(450)
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

            # Button font
            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(15)
            BTN_font.setFamily("Stencil")

            line_Edit = QtGui.QFont()
            line_Edit.setPointSize(20)

            # Item Name Label
            self.Item_name_label = QtWidgets.QLabel(self)
            self.Item_name_label.setText("Particular:")
            self.Item_name_label.setGeometry(60, 100, 150, 30)
            self.Item_name_label.setFont(label_font)

            try:
                  #    combo box of item names
                  self.combo1 = QComboBox(self)
                  self.combo1.setGeometry(300, 100, 130, 30)
                  s.cursor1.execute("select ITEM_NAME from store.inventory;")
                  item_names = s.cursor1.fetchall()
                  for item in item_names:
                        self.combo1.addItem(f"{item[0]}")
            except Exception as e:
                  traceback.print_exc()
                  msg(str(e))

            # Supplier label
            self.SUP_lbl = QtWidgets.QLabel(self)
            self.SUP_lbl.setText("Supplier: ")
            self.SUP_lbl.setGeometry(60, 150, 150, 30)
            self.SUP_lbl.setFont(label_font)

            try:
                  # combo box of suppliers names
                  self.combo2 = QComboBox(self)
                  self.combo2.setGeometry(300, 150, 130, 30)
                  s.cursor1.execute("select sup_id,sup_name from store.suppliers")
                  sup_names = s.cursor1.fetchall()
                  for name in sup_names:
                        self.combo2.addItem(f"{name[1]}")
            except Exception as e:
                 traceback.print_exc()
                 msg(str(e))

            # Qty label
            self.Quantity_label = QtWidgets.QLabel(self)
            self.Quantity_label.setText("Quantity:")
            self.Quantity_label.setGeometry(60, 200, 150, 30)
            self.Quantity_label.setFont(label_font)

            # Qty Line Edit
            self.Quantity_LE = QtWidgets.QLineEdit(self)
            self.Quantity_LE.setGeometry(300, 200, 130, 30)
            self.Quantity_LE.setFont(line_Edit)
            self.Quantity_LE.returnPressed.connect(self.next_Le)

            # Invoice no label
            self.invoice_no_label = QtWidgets.QLabel(self)
            self.invoice_no_label.setText("Invoice_No:")
            self.invoice_no_label.setGeometry(60, 250, 200, 30)
            self.invoice_no_label.setFont(label_font)

            # Invoice No Line Edit
            self.invoice_no_LE = QtWidgets.QLineEdit(self)
            self.invoice_no_LE.setGeometry(300, 250, 130, 30)
            self.invoice_no_LE.setFont(line_Edit)
            self.invoice_no_LE.returnPressed.connect(self.next_Le)

            # Unit Price label
            self.unit_price_label = QtWidgets.QLabel(self)
            self.unit_price_label.setText("Unit_price:")
            self.unit_price_label.setGeometry(60, 300, 150, 30)
            self.unit_price_label.setFont(label_font)

            # Unit price Line Edit
            self.unit_price_LE = QtWidgets.QLineEdit(self)
            self.unit_price_LE.setGeometry(300, 300, 130, 30)
            self.unit_price_LE.setFont(line_Edit)
            self.unit_price_LE.returnPressed.connect(self.update_clicked)

            # Update Button
            self.update_BTN = QtWidgets.QPushButton(self)
            self.update_BTN.setGeometry(150, 360, 180, 30)
            self.update_BTN.setText("UPDATE")
            self.update_BTN.setFont(BTN_font)
            self.update_BTN.clicked.connect(self.update_clicked)

      def update_clicked(self):
            try:
                  name = self.combo1.currentText()
                  Qty = self.Quantity_LE.text()
                  sup_name = self.combo2.currentText()
                  Invoice_No = self.invoice_no_LE.text()
                  Unit_price = self.unit_price_LE.text()
                  Total_Amount = int(Qty) * int(Unit_price)
                  print("This is Qty ", Qty, "This is total amount", Total_Amount)
                  insert_query = (
                        f"insert into purchases values( (select barcode from inventory where item_name ='{name}'),"
                        f"(select sup_id from suppliers where sup_name = '{sup_name}'),"
                        f"(select item_no from inventory where item_name = '{name}'),"
                        f"{Invoice_No},'{name}',{Unit_price},'{Qty}',{Total_Amount})")
                  print(insert_query)
                  s.cursor1.execute(insert_query)
                  s.connection.commit()

                  name = self.combo1.currentText()
                  s.cursor1.execute(f"select Qty_avail from store.inventory where item_name = '{name}'")
                  Qty = s.cursor1.fetchall()
                  Qty_avail = str(Qty[0][0])
                  New_Qty = self.Quantity_LE.text()
                  updated_Qty = int(Qty_avail) + int(New_Qty)
                  print("This is old Qty", Qty)
                  print("This is update Qty ", updated_Qty)

                  s.cursor1.execute(
                        f"update store.inventory set Qty_avail = {updated_Qty} where item_name = '{name}'")
                  s.cursor1.execute("commit")
                  self.Quantity_LE.clear()
                  self.unit_price_LE.clear()
                  self.invoice_no_LE.clear()

            except Exception as e:
                  traceback.print_exc()
                  msg(str(e))

      def next_Le(self):
            self.focusNextChild()

# Todo : See Supplier Page
class see_supplier(QMainWindow):

      def __init__(self):

            super(see_supplier, self).__init__()
            self.setWindowTitle("See Supplier Page")

            self.setFixedHeight(500)
            self.setFixedWidth(800)

            # Table widget
            self.tableWidget = QTableWidget(self)
            self.tableWidget.setRowCount(20)  # Set no of rows
            self.tableWidget.setColumnCount(5)  # Set no of columns
            self.tableWidget.setGeometry(140, 100, 520, 350)  # Set geometry of table
            self.tableWidget.setHorizontalHeaderLabels(
                  ["Supplier Id ", 'Supplier Name', 'Phone number ', ' Address', 'Alternate Number'])
            self.tableWidget.setColumnWidth(0, 80)
            self.tableWidget.setColumnWidth(1, 100)
            self.tableWidget.setColumnWidth(2, 100)
            self.tableWidget.setColumnWidth(3, 100)
            self.tableWidget.setColumnWidth(4, 120)
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

            try:
                  s.cursor1.execute("SELECT * FROM store.suppliers order by sup_id;")
                  rows = s.cursor1.fetchall()
                  self.tableWidget.setRowCount(len(rows))
                  self.tableWidget.setColumnCount(len(rows[0]))
                  for i, row in enumerate(rows):
                        for j, col in enumerate(row):
                              self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))

                  self.tableWidget.setRowCount(len(rows))
                  self.tableWidget.setColumnCount(len(rows[0]))

                  for i, row in enumerate(rows):
                        for j, col in enumerate(row):
                              self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))

            except mysql.connector.Error as error:
                  print("Failed to fetch data from MySQL table:", error)
                  msg(str(error))
            # Back Button
            self.Back_BTN = QtWidgets.QPushButton(self)
            self.Back_BTN.setGeometry(30, 30, 60, 30)
            self.Back_BTN.setText("Back")
            self.Back_BTN.setStyleSheet("background: White")
            self.Back_BTN.clicked.connect(self.purchase)

      def purchase(self):
            self.destroy()

# Todo : Sellnow page
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

# Todo : Gst calc page
class GstCalc(QMainWindow):

      def __init__(self):
            super(GstCalc, self).__init__()
            self.setWindowTitle("Gst Calculator ")

            # Label font
            label_font = QtGui.QFont()
            label_font.setPointSize(15)
            label_font.setFamily("Arial Black")

            # Gst Calculator label
            self.text_label = QtWidgets.QLabel(self)
            self.text_label.setText(" GST CALCULATOR ")
            self.text_label.setGeometry(150, 50, 370, 30)
            self.text_label.setFont(label_font)

            # Button font
            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(10)
            BTN_font.setFamily("Stencil")

            self.setFixedHeight(350)
            self.setFixedWidth(450)

            line_Edit = QtGui.QFont()
            line_Edit.setPointSize(20)

            # Catalogue label
            self.Catalogue_label = QtWidgets.QLabel(self)
            self.Catalogue_label.setText(" Catalogue Price :")
            self.Catalogue_label.setGeometry(60, 100, 150, 30)
            self.Catalogue_label.setFont(BTN_font)

            # Catalogue Line Edit
            self.Catalogue_lE = QtWidgets.QLineEdit(self)
            self.Catalogue_lE.setGeometry(250, 100, 130, 30)
            self.Catalogue_lE.setFont(line_Edit)

            # Trade discount  label
            self.Trade_disc_label = QtWidgets.QLabel(self)
            self.Trade_disc_label.setText("Trade Discount :")
            self.Trade_disc_label.setGeometry(60, 150, 150, 30)
            self.Trade_disc_label.setFont(BTN_font)

            # Trade discount Line Edit
            self.Trade_disc_LE = QtWidgets.QLineEdit(self)
            self.Trade_disc_LE.setGeometry(250, 156, 130, 30)
            self.Trade_disc_LE.setFont(line_Edit)

            # Gst Percentage label
            self.Gst_perc_label = QtWidgets.QLabel(self)
            self.Gst_perc_label.setText(" GST Percentage :")
            self.Gst_perc_label.setGeometry(60, 200, 150, 30)
            self.Gst_perc_label.setFont(BTN_font)

            # Gst Percentage Line Edit
            self.Gst_Perc_LE = QtWidgets.QLineEdit(self)
            self.Gst_Perc_LE.setGeometry(250, 200, 130, 30)
            self.Gst_Perc_LE.setFont(line_Edit)

            # Total Amt Label
            self.Total_amt_label = QtWidgets.QLabel(self)
            self.Total_amt_label.setText("TOTAL AMOUNT")
            self.Total_amt_label.setGeometry(100, 250, 150, 30)
            self.Total_amt_label.setFont(BTN_font)

            # Total amt line Edit
            self.Total_amtLE = QtWidgets.QLineEdit(self)
            self.Total_amtLE.setGeometry(200, 250, 130, 30)
            self.Total_amtLE.setFont(line_Edit)
            self.Total_amtLE.setEnabled(False)

            # Result Button
            self.Result_BTN = QtWidgets.QPushButton(self)
            self.Result_BTN.setGeometry(150, 300, 90, 30)
            self.Result_BTN.setText("Result")
            self.Result_BTN.clicked.connect(self.check)

            # Clear Button
            self.clear_BTN = QtWidgets.QPushButton(self)
            self.clear_BTN.setGeometry(250, 300, 90, 30)
            self.clear_BTN.setText("Clear")
            self.clear_BTN.clicked.connect(self.clear)

            # Back Button
            self.Back_BTN = QtWidgets.QPushButton(self)
            self.Back_BTN.setGeometry(30, 30, 80, 30)
            self.Back_BTN.setText("Back")
            self.Back_BTN.setFont(BTN_font)
            self.Back_BTN.clicked.connect(self.welcompage)

      def clear(self):
            self.Catalogue_lE.clear()
            self.Trade_disc_LE.clear()
            self.Gst_Perc_LE.clear()
            self.Total_amtLE.clear()

      def check(self):
            try:
                  self.tdfinder = ""
                  self.gstfinder = ""
                  self.tdfinder += self.Catalogue_lE.text()
                  self.tdfinder += "*("
                  self.tdfinder += self.Trade_disc_LE.text()
                  self.tdfinder += "/100)"
                  self.gstfinder += self.Catalogue_lE.text()
                  self.gstfinder += "-"
                  self.gstfinder += str(eval(self.tdfinder))
                  self.gstfinder += "*"
                  self.gstfinder += self.Gst_Perc_LE.text()
                  self.gstfinder += "/100"
                  print(eval(self.gstfinder))
                  self.Total_amtLE.setText(str(eval(self.gstfinder)))
            except Exception as e:
                  traceback.print_exc()
                  msg(str(e))

      def welcompage(self):
            self.destroy()
            self.p = WelcomePage()
            self.p.show()

# Todo : Total sales page
class TOTALSALES(QDialog):

      def __init__(self):
            super(TOTALSALES, self).__init__()
            self.setWindowTitle("Total Sales Page")

            self.screen()
            win = Tk()
            screen_width = int(win.winfo_screenwidth())
            screen_height = int(win.winfo_screenheight())
            self.setFixedSize(screen_width, screen_height)

            # Label font
            label_font = QtGui.QFont()
            label_font.setPointSize(20)
            label_font.setFamily("Arial Black")

            label = QtWidgets.QLabel
            label.setStyleSheet(self, "background-image: url(wp4795094-general-store-wallpapers.jpg)")

            # Main font
            main_font = QtGui.QFont()
            main_font.setPointSize(30)
            main_font.setFamily("Cooper Black")

            # Button font
            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(15)
            BTN_font.setFamily("Stencil")

            # Date font
            date_font = QtGui.QFont()
            date_font.setPointSize(18)
            date_font.setFamily("Erais")

            # Total sales Label
            self.text_label = QtWidgets.QLabel(self)
            self.text_label.setText(" Total Sales ")
            self.text_label.setGeometry(screen_width // 2 - 200, 30, 290, 30)
            self.text_label.setFont(main_font)

            # Back Button
            self.Back_BTN = QtWidgets.QPushButton(self)
            y1_ = screen_height - 20
            y1 = screen_height - y1_
            self.Back_BTN.setGeometry(30, y1, 200, 30)
            self.Back_BTN.setText("Back")
            self.Back_BTN.setFont(BTN_font)

            self.from_dateEdit = QDateEdit(self, calendarPopup=True, date=QtCore.QDate.currentDate(),
                                           displayFormat="yyyy/MM/dd")
            self.from_dateEdit.setGeometry(50, 100, 100, 30)

            self.to_dateEdit = QDateEdit(self, calendarPopup=True, date=QtCore.QDate.currentDate(),
                                         displayFormat="yyyy/MM/dd")
            self.to_dateEdit.setGeometry(200, 100, 100, 30)

            # Table Widget
            self.tableWidget = QtWidgets.QTableWidget(self)
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setGeometry(40, screen_height // 2 - 200, screen_width // 2 - 50, screen_height - 400)
            self.tableWidget.setHorizontalHeaderLabels(
                  ['Barcode', 'DATE', 'Item no', 'Particulars', 'PRICE', 'QUANTITY', 'Grand Total'])
            self.font = QFont('Arial', 12, QFont.Bold)  # Create a QFont object with desired attributes
            self.tableWidget.horizontalHeader().setFont(self.font)
            self.tableWidget.setColumnWidth(0, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(1, int(100 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(2, int(100 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(3, int(200 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(4, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(5, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(6, int(150 / 1920 * screen_width))
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

            # Day Button
            self.day_btn = QtWidgets.QPushButton(self)
            self.day_btn.setText("DAY WISE SALES")
            self.day_btn.setGeometry(800, 100, 100, 40)
            self.day_btn.setStyleSheet("background:red")
            self.day_btn.clicked.connect(self.daySales)

            # Done Button
            self.Done_Btn = QtWidgets.QPushButton(self)
            self.Done_Btn.setGeometry(400, 100, 100, 40)
            self.Done_Btn.setText("DONE")
            self.Done_Btn.setStyleSheet("background : Red")
            self.Done_Btn.clicked.connect(self.done_clicked)

            # Combo box of all days
            self.days = QtWidgets.QComboBox(self)
            self.days.setGeometry(600, 100, 150, 40)
            self.days.setFont(BTN_font)
            self.days.addItems(
                  ["All Days", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

            # Text area where the graph is placed
            self.graph_txt = QtWidgets.QLabel(self)
            w1 = screen_width // 4
            self.graph_txt.setGeometry(screen_width // 2, screen_height // 2 - 200, screen_width // 2 - 50,
                                       screen_height - 400)

            sales_of_month = []
            mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
            for i in range(len(months)):
                  s.cursor1.execute(f"select count(*) from sales where monthname(sold_date) = '{months[i]}';")
                  sales = s.cursor1.fetchone()
                  sales_of_month.append(sales[0])

            plt.plot(mon, sales_of_month)
            plt.xlabel("MONTHS")
            plt.ylabel("SALES")
            plt.savefig('graph.jpg')

            pixmap = QPixmap("graph.jpg")
            self.graph_txt.setPixmap(pixmap.scaled(self.graph_txt.width(), self.graph_txt.height()))

            if self.Back_BTN.clicked:
                  self.Back_BTN.clicked.connect(self.welcomepage)

      def welcomepage(self):
            self.destroy()
            self.p = WelcomePage()
            self.p.show()

      def done_clicked(self):
            try:
                  from_date = self.from_dateEdit.date()
                  to_date = self.to_dateEdit.date()
                  if (from_date > to_date):
                        msg("YOUR FROM DATE IS GREATER THAN TO DATE \n \t PLEASE CHANGE IT.")
                  elif (self.days.currentText() == "All Days"):
                        s.cursor1.execute(
                              f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' order by monthname(sold_date);")

                        rows = s.cursor1.fetchall()

                        self.tableWidget.setRowCount(len(rows))
                        for i, row in enumerate(rows):
                              for j, col in enumerate(row):
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                  elif self.days.currentText() == "Sunday":
                        day = "Sunday"
                        s.cursor1.execute(
                              f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                        rows = s.cursor1.fetchall()
                        self.tableWidget.setRowCount(len(rows))
                        for i, row in enumerate(rows):
                              for j, col in enumerate(row):
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                  elif self.days.currentText() == "Monday":
                        day = "Monday"
                        s.cursor1.execute(
                              f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                        rows = s.cursor1.fetchall()
                        self.tableWidget.setRowCount(len(rows))
                        for i, row in enumerate(rows):
                              for j, col in enumerate(row):
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                  elif self.days.currentText() == "Tuesday":
                        day = "Tuesday"
                        s.cursor1.execute(
                              f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                        rows = s.cursor1.fetchall()
                        self.tableWidget.setRowCount(len(rows))
                        for i, row in enumerate(rows):
                              for j, col in enumerate(row):
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                  elif self.days.currentText() == "Wednesday":
                        day = "Wednesday"
                        s.cursor1.execute(
                              f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                        rows = s.cursor1.fetchall()
                        self.tableWidget.setRowCount(len(rows))
                        for i, row in enumerate(rows):
                              for j, col in enumerate(row):
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                  elif self.days.currentText() == "Thursday":
                        day = "Thursday"
                        s.cursor1.execute(
                              f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                        rows = s.cursor1.fetchall()
                        self.tableWidget.setRowCount(len(rows))
                        for i, row in enumerate(rows):
                              for j, col in enumerate(row):
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                  elif self.days.currentText() == "Friday":
                        day = "Friday"
                        s.cursor1.execute(
                              f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                        rows = s.cursor1.fetchall()
                        self.tableWidget.setRowCount(len(rows))
                        for i, row in enumerate(rows):
                              for j, col in enumerate(row):
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
                  elif self.days.currentText() == "Saturday":
                        day = "Saturday"
                        s.cursor1.execute(
                              f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                        rows = s.cursor1.fetchall()
                        self.tableWidget.setRowCount(len(rows))
                        for i, row in enumerate(rows):
                              for j, col in enumerate(row):
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
            except Exception as e:
                  traceback.print_exc()
                  msg(str(e))

      def daySales(self):
            self.d = day_sales()
            self.d.show()

# Todo : Day sale page
class day_sales(QMainWindow):

      def __init__(self):
            super(day_sales, self).__init__()
            self.setWindowTitle("DAY SALES")

            self.setFixedWidth(1000)
            self.setFixedHeight(600)

            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(15)
            BTN_font.setFamily("Stencil")

            main_font = QtGui.QFont()
            main_font.setPointSize(18)
            main_font.setFamily("Cooper Black")

            self.lbl = QtWidgets.QLabel(self)
            self.lbl.setText("DAY SALES GRAPH GENERATOR")
            self.lbl.setFont(main_font)
            self.lbl.setGeometry(300, 10, 500, 30)

            self.year = QtWidgets.QComboBox(self)
            self.year.setGeometry(220, 100, 150, 40)
            self.year.setFont(BTN_font)
            min_yr = 2024
            max_yr = 2050
            for year in range(min_yr, max_yr + 1):
                  self.year.addItem(str(year))

            self.months = QtWidgets.QComboBox(self)
            self.months.setGeometry(50, 100, 150, 40)
            self.months.setFont(BTN_font)
            self.months.addItems(
                  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"])

            self.Done_Btn = QtWidgets.QPushButton(self)
            self.Done_Btn.setGeometry(400, 100, 100, 30)
            self.Done_Btn.setText("DONE")
            self.Done_Btn.setStyleSheet("background : Red")
            self.Done_Btn.clicked.connect(self.done)

            self.graph_le = QtWidgets.QLabel(self)
            self.graph_le.setGeometry(50, 160, 900, 410)
            self.graph_le.setStyleSheet("background:blue")

      def done(self):
            try:
                  sales_of_day = []
                  plt.clf()
                  month = self.months.currentText()
                  year = self.year.currentText()
                  days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                  for i in range(len(days)):
                        s.cursor1.execute(
                              f"select count(*) from sales where  monthname(sold_date) = '{month}'and year(sold_date) = '{year}' and dayname(sold_date) = '{days[i]}';")
                        sales = s.cursor1.fetchall()
                        sales_of_day.append(sales[0][0])

                  print("this is day sales ", sales_of_day)
                  cur_year = datetime.now().year
                  print(cur_year)

                  if sum(sales_of_day) == 0 and int(year) > int(cur_year):
                        msg(" No Sales Happened Check Your Year ")
                  else:
                        plt.plot(days, sales_of_day)
                        plt.xlabel("DAYS")
                        plt.ylabel("SALES")
                        for i in range(1):
                              plt.savefig(f'graph of {month}.jpg')

                        self.pixmap = QPixmap(f"graph of {month}.jpg")
                        self.graph_le.setPixmap(self.pixmap.scaled(self.graph_le.width(), self.graph_le.height()))

            except Exception as e:
                  traceback.print_exc()
                  msg(str(e))

# Todo : Admin Page
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
                  self.upda_sec_BTN.setGeometry(240,300,90,40)
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

# Todo : See Item stock
class inventory(QMainWindow):
      def __init__(self):
            super(inventory, self).__init__()
            self.setWindowTitle("ITEM STOCK")

            background_image = resource_path('images/Purchases.png')

            background_image_url = background_image.replace("\\", "/")
            print(f"Formatted background image path: {background_image_url}")

            self.setStyleSheet(f'background-image: url({background_image_url});')

            win = Tk()
            screen_width = int(win.winfo_screenwidth())
            screen_height = int(win.winfo_screenheight())

            self.setFixedHeight(screen_height)
            self.setFixedWidth(screen_width)

            # Main font
            main_font = QtGui.QFont()
            main_font.setPointSize(30)
            main_font.setFamily("Cooper Black")

            # Button font
            btn_font = QtGui.QFont()
            btn_font.setPointSize(15)
            btn_font.setFamily("Stencil")

            self.text_label = QtWidgets.QLabel(self)
            self.text_label.setText(" ITEMS AVAILABLE IN THE STORE")
            ratio = int(screen_width) // 2
            print("This is ratio ", ratio)
            x_ = ratio + 375
            x = screen_width - x_
            self.text_label.setGeometry(x, 30, 750, 50)
            self.text_label.setFont(main_font)
            self.text_label.setStyleSheet("background: White")

            # Back Button
            self.back_btn = QtWidgets.QPushButton(self)
            self.back_btn.setText("BACK")
            self.back_btn.setGeometry(10, 10, 70, 30)
            self.back_btn.setStyleSheet("background: White")
            self.back_btn.clicked.connect(self.show_welcome_page)

            # Proceed Button
            self.proceed_btn = QtWidgets.QPushButton(self)
            self.proceed_btn.setText("MAKE PDF")
            print("----------------------------------------------------")
            ratio1 = int(screen_width) // 4
            ht_ratio = int(screen_height) // 4
            x_1 = ratio1 - 200
            y1_ = ht_ratio - 10
            y1 = screen_height - y1_

            self.proceed_btn.setGeometry(screen_width - x_1, y1, 150, 40)
            self.proceed_btn.setStyleSheet("background: White")
            self.proceed_btn.clicked.connect(self.make_pdf)
            self.proceed_btn.setFont(btn_font)

            # table Widget
            self.tableWidget = QTableWidget(self)
            self.tableWidget.setRowCount(20)  # Set no of rows
            self.tableWidget.setColumnCount(5)  # Set no of columns
            y3_ = screen_height - 250
            y3 = screen_height - y3_

            self.tableWidget.setGeometry(50, y3, screen_width - 500, screen_height - y3 - 135)
            # self.tableWidget.setGeometry(200, 200, 1055, 650)  # Set geometry of table
            self.tableWidget.setHorizontalHeaderLabels(
                  ["BARCODE", 'SNO', 'PARTICULARS', 'UNIT PRICE', 'QTY AVAILABLE'])

            self.tableWidget.setColumnWidth(0, int(100 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(1, int(100 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(2, int(530 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(3, int(150 / 1920 * screen_width))
            self.tableWidget.setColumnWidth(4, int(150 / 1920 * screen_width))
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.tableWidget.setStyleSheet("background:white")

            try:
                  self.populate_table()

            except mysql.connector.Error as error:
                  print("Failed to fetch data from MySQL table:", error)
                  msg(str(error))

      def populate_table(self):
            s.cursor1.execute("SELECT * FROM store.inventory order by ITEM_NO;")
            rows = s.cursor1.fetchall()
            self.tableWidget.setRowCount(len(rows))
            self.tableWidget.setColumnCount(len(rows[0]))
            for i, row in enumerate(rows):
                  for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))

            self.tableWidget.setRowCount(len(rows))
            self.tableWidget.setColumnCount(len(rows[0]))

            for i, row in enumerate(rows):
                  for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))

      def show_welcome_page(self):
            self.close()
            self.p = WelcomePage()
            self.p.show()

      def make_pdf(self):
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=0)
            pdf.add_page()
            pdf.header()
            col_widths = [50, 20, 50, 25, 40]

            pdf.set_font("Arial", size=12, style='B')
            headers = ["BARCODE", 'SNO', 'PARTICULARS', 'UNIT PRICE', 'QTY AVAILABLE']
            for header, width in zip(headers, col_widths):
                  pdf.cell(width, 10, header, border=1)

            pdf.ln()

            for row in range(self.tableWidget.rowCount()):
                  for col in range(self.tableWidget.columnCount()):
                        pdf.cell(col_widths[col], 10, str(self.tableWidget.item(row, col).text()), border=1)
                  pdf.ln()

            pdf_output = "STOCK.pdf"
            pdf.output(pdf_output)
            path = ""

            print(f"PDF generated successfully: {pdf_output} \n path is {path}")

class security(QDialog):
      def __init__(self):
            super().__init__()
            try:
                  self.setWindowTitle("Security Key")
                  self.setFixedSize(300,100)
                  self.label = QLabel("Enter The Security Key:", self)
                  self.label.setGeometry(100,10,150,30)

                  self.input_field = QtWidgets.QLineEdit(self)
                  self.input_field.setGeometry(20, 35, 250, 30)
                  self.input_field.setEchoMode(QtWidgets.QLineEdit.Password)


                  self.submit_button = QtWidgets.QPushButton("Submit", self)
                  self.submit_button.setGeometry(80,70,150,30)
                  self.submit_button.clicked.connect(self.Submit)
            except Exception as e:
                 traceback.print_exc()
      def Submit(self):
          try:
            text = self.input_field.text()
            s.cursor1.execute("select * from security;")
            se = s.cursor1.fetchall()
            if str(text) in se[0]:
                self.destroy()
                self.a = admin()
                self.a.show()

            else:
                msg("Wrong Key")
          except Exceptionas as e:
              print(e)

      def closeEvent(self, event):
            event.accept()

class Update_key(QDialog):
      def __init__(self):
            super().__init__()
            try:
                  self.setWindowTitle("Security Key")
                  self.setFixedSize(300, 100)
                  self.label = QLabel("Update The Security Key:", self)
                  self.label.setGeometry(100, 10, 150, 30)

                  self.input_field = QtWidgets.QLineEdit(self)
                  self.input_field.setGeometry(20, 35, 200, 30)
                  self.input_field.setEchoMode(QtWidgets.QLineEdit.Password)

                  self.submit_button = QtWidgets.QPushButton("Submit", self)
                  self.submit_button.setGeometry(80, 70, 150, 30)
                  self.submit_button.clicked.connect(self.on_submit)

                  self.checkbox = QtWidgets.QCheckBox('Show', self)
                  self.checkbox.setGeometry(240, 35, 150, 30)
                  self.checkbox.toggled.connect(self.showpass)
            except Exception as e:
                  traceback.print_exc()

      def showpass(self,checked):
            if checked:
                  self.input_field.setEchoMode(False)
            else:
                  self.input_field.setEchoMode(QtWidgets.QLineEdit.Password)

      def on_submit(self):
            try:
                  text = self.input_field.text()
                  s.cursor1.execute("select * from security;")
                  se = s.cursor1.fetchall()
                  no = se[0][0]

                  if str(text) not in se[0]:
                        print("Yeah")
                        s.cursor1.execute(f"update security set Security_password={text} where Security_password={no}")
                        msg("Successfully Added")
                  elif(text==no):
                        msg("Same Key \nYou have Entered")
            except Exceptionas as e:
                  print(e)

      def closeEvent(self, event):
            event.accept()


app = QApplication(sys.argv)
l = login()
l.show()
app.exec_()