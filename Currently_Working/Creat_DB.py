import mysql.connector
Connector=mysql.connector.connect(host="localhost", user="root", password="Aditya2004@google")
Cursor=Connector.cursor()
Output=Cursor.execute("show DATABASES")
x=Cursor.fetchall()
print(x)