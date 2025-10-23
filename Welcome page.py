from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox,QTabWidget,QMainWindow
import sys


class WelcomePage(QMainWindow):

    def __init__(self):
        super(WelcomePage, self).__init__()
        self.setWindowTitle("SUPER MARKET")
        self.setStyleSheet("""
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
                      """)

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
        OPER_FONT.setPointSize(20)
        OPER_FONT.setFamily("28 Days Later")

        # Operator label
        self.operator_Label = QtWidgets.QLabel(self)
        self.operator_Label.setText(" Operator : ")
        self.operator_Label.setGeometry(10, 30, 130, 30)
        self.operator_Label.setFont(BTN_font)
        self.operator_Label.setStyleSheet("background: White")

        # Operator LineEdit
        self.operator_LE = QtWidgets.QLineEdit(self)
        s.cursor1.execute(f"select name from admins_data where user_id ={user}")
        rows1 = s.cursor1.fetchone()
        name = rows1[0]
        self.operator_LE.setText(f" {name} ")
        self.operator_LE.setGeometry(160, 30, 120, 30)
        self.operator_LE.setEnabled(False)
        self.operator_LE.setFont(OPER_FONT)
        self.operator_LE.setStyleSheet("background: White")

        # logout Button
        self.LOGOUT_BTN = QtWidgets.QPushButton(self)
        self.LOGOUT_BTN.setText("LOGOUT")
        self.LOGOUT_BTN.setGeometry(650, 50, 120, 30)
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
        self.Sale_BTN.setText("Sell Now ")
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
        self.itemStock_BTN.setText("See Item Stock ")
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
        self.GST_BTN.setText("Gst Calculator")
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

app = QApplication(sys.argv)
W = WelcomePage()
W.show()
app.exec_()