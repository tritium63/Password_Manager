import mysql.connector
Connector=mysql.connector.connect(host="localhost", user="root", password="Aditya2004@google", database="Testing-db")
#print("Connection Sucessful")
c=Connector.cursor()

#Requesting user id and password from user#

UserId=input("enter user id : ")
MasterPass=input("Enter Master Password : ")


# Function is defined with attributes UserId, MasterPass these values 
# are collected from the user the function is called at the end with the same values
# the function also has a return value which is the user id this will be further used to select the users
# specific table 

def UserVerification(UserId, MasterPass):
    templis=[]
    #An empty list is created to store the user id and password#
    c.execute("select * from headlogin")#selecting all user id and passwords together
    for i in c:     #itterating through user id and password as pair# 
        for j in i: #pair is seperated and user id is checked with the one in database
            if j==UserId:   #if user id is matched 
                templis.append(i)#then the id password pair represented by i is appenden in to the empty list 
        #print(templis) #for debuging
    if templis == [(UserId, MasterPass)] : #now id pass pair is checked again to what the user has entred 
        #print("Id pass Match") For debugibg :D
        return UserId #this is what the function returns 
    else:
        #print("No user found") # if pair is not matched 
        return 2 #If password id pair does not match  
Var=UserVerification(UserId, MasterPass)# the value that is returned ie the userid is stored in object Var 
if Var != 2:
    c.execute("select * from "+Var )#the mathcing Table is then selected
    for i in c:     #all the table entries are printed
        pass         
        # print(i)
else:
    print("User id password do not match")

# UID=input("Enter User Name : ")
Service=input("Enter Service Name : ")

def Searching(Service, Var):
    c.execute("select service from "+Var)
    VarList=c.fetchall()
    # print(XX)
    for i in VarList:
        if i == (Service,):
            pass  # Temp Statement
            # print(i)
            # return i
            # print("select * from " +Var+ " where SERVICE =" + "\""+Service +"\""+";")
            c.execute("select * from " +Var+ " where SERVICE =" + "\""+Service +"\""+";")
            # for d in c:
            #     print(d)
            x=c.fetchall()
            print(x)
if Var != 2:#Exception handled "str + int" 
    Searching(Service, Var)
    # print("ALL OK")


# select * from Var wherer  SERVICE = "TableIndex" 





# Table structure Head Login 
# +----------+-------------+------+-----+---------+-------+
# | Field    | Type        | Null | Key | Default | Extra |
# +----------+-------------+------+-----+---------+-------+
# | USERID   | varchar(32) | YES  |     | NULL    |       |
# | PASSWORD | varchar(32) | YES  |     | NULL    |       |
# +----------+-------------+------+-----+---------+-------+
# Table structure User
# +----------+-------------+------+-----+---------+-------+
# | Field    | Type        | Null | Key | Default | Extra |
# +----------+-------------+------+-----+---------+-------+
# | USERID   | varchar(32) | YES  |     | NULL    |       |
# | PASSWORD | varchar(32) | YES  |     | NULL    |       |
# | SERVICE  | varchar(32) | YES  |     | NULL    |       |
# +----------+-------------+------+-----+---------+-------+