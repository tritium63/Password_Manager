import mysql.connector
Connector=mysql.connector.connect(host="localhost", user="root", password="Aditya2004@google", database="Testing-db")
#print("Connection Sucessful")
c=Connector.cursor()
UID=input("Enter User Name : ")
Service=input("Enter Service Name : ")

def Searching(Service, UID):
    c.execute("select service from "+UID)
    for i in c:
        print(i)
Searching(Service, UID)