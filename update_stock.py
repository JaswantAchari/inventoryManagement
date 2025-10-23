from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox,QMainWindow , QTableWidget,QComboBox
import sys
import sql as s

class update(QMainWindow):

      def __init__(self):
            super(update,self).__init__()

            self.setFixedHeight(450)
            self.setFixedWidth(500)

            label_font = QtGui.QFont()
            label_font.setPointSize(15)
            label_font.setFamily("Arial Black")
            label = QtWidgets.QLabel
            label.setStyleSheet(self, "background-image: url()")

            main_font = QtGui.QFont()
            main_font.setPointSize(12)
            main_font.setFamily("Cooper Black")

            BTN_font = QtGui.QFont()
            BTN_font.setPointSize(15)
            BTN_font.setFamily("Stencil")

            line_Edit = QtGui.QFont()
            line_Edit.setPointSize(20)

            self.Item_name_label = QtWidgets.QLabel(self)
            self.Item_name_label.setText("Particular:")
            self.Item_name_label.setGeometry(60, 100, 150, 30)
            self.Item_name_label.setFont(label_font)

            try:
               self.combo1 = QComboBox(self)
               self.combo1.setGeometry(300, 100, 130, 30)
               s.cursor1.execute("select ITEM_NAME from store.inventory;")
               item_names = s.cursor1.fetchall()
               for item in item_names:
                     self.combo1.addItem(f"{item[0]}")
            except Exception as e:
                  print(e)

            self.SUP_lbl = QtWidgets.QLabel(self)
            self.SUP_lbl.setText("Supplier: ")
            self.SUP_lbl.setGeometry(60, 150, 150, 30)
            self.SUP_lbl.setFont(label_font)

            try:
                  self.combo2 = QComboBox(self)
                  self.combo2.setGeometry(300, 150, 130, 30)
                  s.cursor1.execute("select sup_id,sup_name from store.suppliers")
                  sup_names = s.cursor1.fetchall()
                  for name in sup_names:
                        self.combo2.addItem(f"{name[1]}")
            except Exception as e:
                  print(e)

            self.Quantity_label = QtWidgets.QLabel(self)
            self.Quantity_label.setText("Quantity:")
            self.Quantity_label.setGeometry(60, 200, 150, 30)
            self.Quantity_label.setFont(label_font)

            self.Quantity_LE = QtWidgets.QLineEdit(self)
            self.Quantity_LE.setGeometry(300, 200, 130, 30)
            self.Quantity_LE.setFont(line_Edit)
            self.Quantity_LE.returnPressed.connect(self.next_Le)

            self.invoice_no_label = QtWidgets.QLabel(self)
            self.invoice_no_label.setText("Invoice_No:")
            self.invoice_no_label.setGeometry(60, 250, 200, 30)
            self.invoice_no_label.setFont(label_font)

            self.invoice_no_LE = QtWidgets.QLineEdit(self)
            self.invoice_no_LE.setGeometry(300, 250, 130, 30)
            self.invoice_no_LE.setFont(line_Edit)
            self.invoice_no_LE.returnPressed.connect(self.next_Le)

            self.unit_price_label = QtWidgets.QLabel(self)
            self.unit_price_label.setText("Unit_price:")
            self.unit_price_label.setGeometry(60, 300, 150, 30)
            self.unit_price_label.setFont(label_font)

            self.unit_price_LE = QtWidgets.QLineEdit(self)
            self.unit_price_LE.setGeometry(300, 300, 130, 30)
            self.unit_price_LE.setFont(line_Edit)
            self.unit_price_LE.returnPressed.connect(self.update_clicked)

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
                Total_Amount = int(Qty)*int(Unit_price)
                print(Total_Amount)
                print("This is Qty ", Qty)
                s.cursor1.execute(f"update store.inventory set Qty_avail = {Qty} where item_name = '{name}'")
                self.Quantity_LE.clear()
                s.cursor1.execute("commit")

                insert_query = (f"insert into purchases values( (select barcode from inventory where item_name ='{name}'),"
                                f"(select sup_id from suppliers where sup_name = '{sup_name}'),"
                                f"(select item_no from inventory where item_name = '{name}'),"
                                f"{Invoice_No},'{name}',{Unit_price},'{Qty}',{Total_Amount})")
                s.cursor1.execute(insert_query)
                s.connection.commit()


                name = self.combo1.currentText()
                s.cursor1.execute(f"select Qty_avail from store.inventory where item_name = '{name}'")
                Qty = s.cursor1.fetchall()
                Qty_avail = str(Qty[0][0])
                New_Qty = self.Quantity_LE.text()
                updated_Qty = Qty_avail + New_Qty
                print(updated_Qty)


            except Exception as e :
                  print(e)

      def next_Le(self):
            self.focusNextChild()

app = QApplication(sys.argv)
l = update()
l.show()
app.exec_()
