import mysql.connector
Connector=mysql.connector.connect(host="localhost", user="root", password="Aditya2004@google", database="Testing-db")
#print("Connection Sucessful")
c=Connector.cursor()
UserId=input("enter user id : ")
MasterPass=input("Enter Master Password : ")
def UserVerification(UserId, MasterPass):
    templis=[]
    c.execute("select * from headlogin") 
    for i in c:
        for j in i:
            if j==UserId:
                templis.append(i)
    #print(templis)   
    if templis == [(UserId, MasterPass)] :
        print("YOUR A FUCKING GENIUS")
        return UserId
    else:
        print("No user found")
        return 2 
Var=UserVerification(UserId, MasterPass)
c.execute("select * from "+Var )
for i in c:
    print(i)