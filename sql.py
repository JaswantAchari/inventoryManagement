import mysql.connector as m
connection = m.connect(host = "JASWANTH" , user = "root" , password = "sairam" , database = "Store")
cursor1 = connection.cursor()
cursor1.execute("use store")

