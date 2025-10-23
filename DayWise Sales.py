import numpy, pandas, traceback, sys, mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QDate
from datetime import datetime
from tkinter import Tk
from PyQt5.QtWidgets import (QDialog, QApplication, QTabWidget, QLabel, QMainWindow, QComboBox, QTableWidget,
                             QTableWidgetItem, QMessageBox, QDateEdit, QFrame, QCalendarWidget)
import sql as s
from fpdf import FPDF


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




app = QApplication(sys.argv)
d = day_sales()
d.show()
app.exec_()