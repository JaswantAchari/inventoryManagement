from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox,QMainWindow,QComboBox,QBoxLayout
import sys


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


app = QApplication(sys.argv)
A = GstCalc()
A.show()
app.exec_()