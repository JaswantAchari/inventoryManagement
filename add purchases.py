from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox,QMainWindow
import sys
import sql as s


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

app = QApplication(sys.argv)
l = addPurchases()
l.show()
app.exec_()
