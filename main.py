import mysql.connector
# logging into my local mysql server for trial
conn = mysql.connector.connect(host = 'bk3mjn0digzdwyfts1ir-mysql.services.clever-cloud.com', user ='umterzn51pcaf9nw', password='sNwAPpmFIKjYG17iwZKJ', database ="bk3mjn0digzdwyfts1ir")

c= conn.cursor()

#selected the database
# c.execute('use my_db')

#fucntion to create user as explained by in the image sent on whatsapp
def addUser(USERID,PASSWORD):

    #adds user to users table
    c.execute("select USERID from headlogin")
    userList = c.fetchall()
    for i in userList:
        if USERID==i[0]:
            print("sorry the username alredy exists")
            return 1
    query1 = f'INSERT INTO headlogin (USERID,PASSWORD) VALUES (\"{USERID}\",\"{PASSWORD}\")'
    c.execute(query1)
    conn.commit()
    #create table USERID(USERID VARCHAR(32),PASSWORD VARCHAR(32),SERVICE VARCHAR(32));
    query2 = f"create table {USERID}(USERID VARCHAR(32),PASSWORD VARCHAR(32),SERVICE VARCHAR(32));"
    c.execute(query2)
    conn.commit()
    return 0

def addData(USERID,service,username,password):
    #INSERT INTO USERID (USERID,PASSWORD,SERVICE) VALUES (username,password,service) \
    query =f"INSERT INTO {USERID} (USERID,PASSWORD,SERVICE) VALUES (\"{username}\",\"{password}\",\"{service}\");"
    c.execute(query)
    conn.commit()
    print("commited successfully")          



def InputAndCalling():
    global UserId, MasterPass, Var
    UserId=input("enter user id : ")
    MasterPass=input("Enter Master Password : ")
    Var=UserVerification(UserId, MasterPass)# the value that is returned ie the userid is stored in object Var 

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
InputAndCalling()
if Var != 2:
    print("Connection sucesfull")
    # c.execute("select * from "+Var )#the mathcing Table is then selected
    # for i in c:     #all the table entries are printed
    #     
    #     pass         
    #     # print(i)
else:
    print("User id password do not match")

# UID=input("Enter User Name : ")
# Service=input("Enter Service Name : ") 
# Service input acquired 
# Searching Fn defined with calling attributes "Service" and "Var". User ID Stored in Var 
# 1st execute statement selects all entreies in users table 
# stored in VarList
# The service is matched with the users input 
# if they match corresponding service with it's id and password is selected and printed
# def Searching(Service, Var):
#     c.execute("select service from "+Var)
#     VarList=c.fetchall()
#     # print(XX)
#     for i in VarList:
#         if i == (Service,):
#             # pass  # Temp Statement
#             # print(i)
#             # return i
#             # print("select * from " +Var+ " where SERVICE =" + "\""+Service +"\""+";")
#             c.execute("select * from " +Var+ " where SERVICE =" + "\""+Service +"\""+";")
#             # for d in c:
#             #     print(d)
#             x=c.fetchall()
#             print(x)
#         else:
#             print("No service Found")
# if Var != 2:#Exception handled "str + int" 
#     Searching(Service, Var)
conn.close()