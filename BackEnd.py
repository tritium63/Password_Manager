import mysql.connector
# logging into my local mysql server for trial
conn = mysql.connector.connect(host = 'bk3mjn0digzdwyfts1ir-mysql.services.clever-cloud.com', user ='umterzn51pcaf9nw', password='sNwAPpmFIKjYG17iwZKJ', database ="bk3mjn0digzdwyfts1ir")

c= conn.cursor()

#selected the database
# c.execute('use my_db')
ReturnID="TestID2"
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




# Function is defined with attributes MasterID, MasterPass these values 
# are collected from the user the function is called at the end with the same values
# the function also has a return value which is the user id this will be further used to select the users
# specific table 

def UserVerification(MasterID, MasterPass):
    templis=[]
    #An empty list is created to store the user id and password#
    c.execute("select * from headlogin")#selecting all user id and passwords together
    for i in c:     #itterating through user id and password as pair# 
            #pair is seperated and user id is checked with the one in database
        if i[0]==MasterID:   #if user id is matched 
            templis.append(i)#then the id password pair represented by i is appenden in to the empty list 
        #print(templis) #for debuging
    if templis == [(MasterID, MasterPass)] : #now id pass pair is checked again to what the user has entred 
        #print("Id pass Match") For debugibg :D
        return MasterID #this is what the function returns 
    else:
        #print("No user found") # if pair is not matched 
        return 2 #If password id pair does not match  
# ReturnID=UserVerification(MasterID, MasterPass)# the value that is returned ie the userid is stored in object ReturnID 

# if ReturnID != 2:
#     print("Connection sucesfull")
# else:
#     print("User id password do not match")

# Service input acquired 
# Searching Fn defined with calling attributes "Service" and "ReturnID". User ID Stored in ReturnID 
# 1st execute statement selects all entreies in users table 
# stored in AquredServices
# The service is matched with the users input 
# if they match corresponding service with it's id and password is selected and printed
def Searching(Service):
    UID=ReturnID
    c.execute("select service from "+ReturnID)
    AquredServices=c.fetchall()
    # print(XX)
    for i in AquredServices:
        if i == (Service,):
            c.execute(f"select * from {ReturnID} where service=\"{Service}\" ;")
            x=c.fetchall()
            print(x)
        else:
            print("No service Found")


while True:
    Flow=int(input("enter no"))
    if Flow==0:
        break
    if Flow==1:
        addUser(input("Uid"), input("Pas"))
    if Flow==2:
        addData(input("USERID"),input("SERVICE"),input("USERNAME"),input("PASSWORD"))
    if Flow==3:
        ReturnID=UserVerification(input("Uid"), input("Pas"))
        if ReturnID != 2:
            print("Connection sucesfull")
        else:
            print("User id password do not match")
    if Flow==4:
        Searching(input("Service Name"))
conn.close()