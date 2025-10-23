from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox,QMainWindow ,QTableWidget , QDateEdit,QCalendarWidget,QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from tkinter import  Tk
import sys
import sql as s
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore

class TOTALSALES(QDialog):

    def __init__(self):
        super(TOTALSALES,self).__init__()

        self.screen()
        win = Tk()
        screen_width = int(win.winfo_screenwidth())
        print(screen_width)
        screen_height = int(win.winfo_screenheight())
        print(screen_height)
        self.setFixedSize(screen_width,screen_height)

        label_font = QtGui.QFont()
        label_font.setPointSize(20)
        label_font.setFamily("Arial Black")

        label = QtWidgets.QLabel
        label.setStyleSheet(self, "background-image: url(wp4795094-general-store-wallpapers.jpg)")

        main_font = QtGui.QFont()
        main_font.setPointSize(30)
        main_font.setFamily("Cooper Black")

        BTN_font = QtGui.QFont()
        BTN_font.setPointSize(15)
        BTN_font.setFamily("Stencil")

        date_font = QtGui.QFont()
        date_font.setPointSize(18)
        date_font.setFamily("Erais")

        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setText(" Total Sales ")
        self.text_label.setGeometry(screen_width//2-200, 30, 290, 30)
        self.text_label.setFont(main_font)

        self.Back_BTN = QtWidgets.QPushButton(self)
        y1_ = screen_height - 20
        y1 = screen_height - y1_
        self.Back_BTN.setGeometry(30, y1, 200, 30)
        self.Back_BTN.setText("Back")
        self.Back_BTN.setFont(BTN_font)


        self.from_dateEdit = QDateEdit(self, calendarPopup = True , date = QtCore.QDate.currentDate(), displayFormat="yyyy/MM/dd" )
        self.from_dateEdit.setGeometry(50,100,100,30)

        self.to_dateEdit = QDateEdit(self, calendarPopup=True, date=QtCore.QDate.currentDate(),displayFormat="yyyy/MM/dd" )
        self.to_dateEdit.setGeometry(200, 100, 100, 30)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setGeometry(40, screen_height//2-200, screen_width//2-50, screen_height-400)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Barcode','DATE', 'Item no', 'Particulars', 'PRICE', 'QUANTITY', 'Grand Total'])
        self.font = QFont('Arial', 12, QFont.Bold)  # Create a QFont object with desired attributes
        self.tableWidget.horizontalHeader().setFont(self.font)
        self.tableWidget.setColumnWidth(0, int(150/ 1920 * screen_width))
        self.tableWidget.setColumnWidth(1, int(100/ 1920 * screen_width))
        self.tableWidget.setColumnWidth(2, int(100/ 1920 * screen_width))
        self.tableWidget.setColumnWidth(3, int(200/ 1920 * screen_width))
        self.tableWidget.setColumnWidth(4, int(150/ 1920 * screen_width))
        self.tableWidget.setColumnWidth(5, int(150/ 1920 * screen_width))
        self.tableWidget.setColumnWidth(6, int(150/ 1920 * screen_width))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.Done_Btn = QtWidgets.QPushButton(self)
        self.Done_Btn.setGeometry(400,100,100,30)
        self.Done_Btn.setText("DONE")
        self.Done_Btn.setStyleSheet("background : Red")
        self.Done_Btn.clicked.connect(self.done_clicked)


        self.days = QtWidgets.QComboBox(self)
        self.days.setGeometry(600,100, 150,40)
        self.days.setFont(BTN_font)
        self.days.addItem("All Days")
        self.days.addItem("Sunday")
        self.days.addItem("Monday")
        self.days.addItem("Tuesday")
        self.days.addItem("Wednesday")
        self.days.addItem("Thursday")
        self.days.addItem("Friday")
        self.days.addItem("Saturday")

        self.graph_txt = QtWidgets.QLabel(self)
        w1 = screen_width//4
        self.graph_txt.setGeometry(screen_width//2, screen_height//2-200,screen_width//2-50, screen_height-400)

        sales_of_month = []
        mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct","Nov", "Dec"]
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
        print(sales_of_month )

        pixmap = QPixmap("graph.jpg")
        self.graph_txt.setPixmap(pixmap.scaled(self.graph_txt.width(),self.graph_txt.height()))


        if self.Back_BTN.clicked:
            self.Back_BTN.clicked.connect(self.welcomepage)

    def welcomepage(self):
        self.destroy()
        self.p = WelcomePage()
        self.p.show()

    def done_clicked(self):
        try:
            from_date =self.from_dateEdit.date()
            to_date = self.to_dateEdit.date()
            if (from_date > to_date):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Error")
                msg.setText("YOUR FROM DATE IS GREATER THAN TO DATE \n \t PLEASE CHANGE IT.")
                msg.exec()
            elif (self.days.currentText() == "All Days"):
                s.cursor1.execute(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' order by monthname(sold_date);")
                print(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' order by monthname(sold_date);")
                rows = s.cursor1.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j,QTableWidgetItem(str(col)))
            elif self.days.currentText() == "Sunday":
                day = "Sunday"
                s.cursor1.execute(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                rows = s.cursor1.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
            elif self.days.currentText() == "Monday":
                day = "Monday"
                s.cursor1.execute(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                rows = s.cursor1.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
            elif self.days.currentText() == "Tuesday":
                day = "Tuesday"
                s.cursor1.execute(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                rows = s.cursor1.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
            elif self.days.currentText() == "Wednesday":
                day = "Wednesday"
                s.cursor1.execute(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                rows = s.cursor1.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
            elif self.days.currentText() == "Thursday":
                day = "Thursday"
                s.cursor1.execute(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                rows = s.cursor1.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
            elif self.days.currentText() == "Friday":
                day = "Friday"
                s.cursor1.execute(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                rows = s.cursor1.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
            elif self.days.currentText() == "Saturday":
                day = "Saturday"
                s.cursor1.execute(f"select * from sales where sold_date between '{from_date.toPyDate()}' and '{to_date.toPyDate()}' and dayname(sold_date) = '{day}';")
                rows = s.cursor1.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, col in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))

            a = []

            for i in range(self.tableWidget.rowCount()):
                a.append(int(self.tableWidget.item(i,6).text()))

            plt.plot(a)
            plt.savefig('graph.jpg')
            pixmap = QPixmap("graph.jpg")
            self.graph_txt.setPixmap(pixmap.scaled(self.graph_txt.width(), self.graph_txt.height()))

            print(sum(a))


        except Exception as e:
            print(e)

app = QApplication(sys.argv)
l = TOTALSALES()
l.show()
app.exec_()



