from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QApplication
from PyQt5 import QtWidgets, QtGui
import mysql.connector
from fpdf import FPDF
import sql as s
import sys


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


app = QApplication(sys.argv)
l = see_supplier()
l.show()
app.exec_()