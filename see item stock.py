from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QApplication
from PyQt5 import QtWidgets, QtGui
import mysql.connector
import tkinter
from tkinter import Tk
from fpdf import FPDF
import sql as s


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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = inventory()
    window.show()
    sys.exit(app.exec_())
