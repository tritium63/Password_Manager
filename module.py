import mysql.connector
import random, string
conn = mysql.connector.connect(host = 'bk3mjn0digzdwyfts1ir-mysql.services.clever-cloud.com', user ='umterzn51pcaf9nw', password='NQKckcvxBcKYTmGKBigD', database ="bk3mjn0digzdwyfts1ir")

def Update(MasterID,UserID, Service, PassWord,con): 
    c=con.cursor()
    c.execute(f"select * from {MasterID} where SERVICE=\"{Service}\" AND USERID=\"{UserID}\"")
    templis=c.fetchall()
    if templis!=[]:
        try:
            c.execute(f"update {MasterID} SET PASSWORD=\"{PassWord}\" WHERE USERID=\"{UserID}\" AND SERVICE=\"{Service}\";")
            con.commit()
            return True
        except Exception as e:
            print(e)
    else:
        return False


def addUser(USERID,PASSWORD,con):

    #adds user to users table
    c = con.cursor()
    c.execute("select USERID from headlogin")
    userList = c.fetchall()
    for i in userList:
        if USERID==i[0]:
            return 1
    query1 = f'INSERT INTO headlogin (USERID,PASSWORD) VALUES (\"{USERID}\",\"{PASSWORD}\")'
    c.execute(query1)
    con.commit()
    #create table USERID(USERID VARCHAR(32),PASSWORD VARCHAR(32),SERVICE VARCHAR(32));
    query2 = f"create table {USERID}(USERID VARCHAR(32),PASSWORD VARCHAR(32),SERVICE VARCHAR(32));"
    c.execute(query2)
    con.commit()
    return 0

def addData(USERID,service,username,password,con):
    c = con.cursor()
    #INSERT INTO USERID (USERID,PASSWORD,SERVICE) VALUES (username,password,service) \
    query =f"INSERT INTO {USERID} (USERID,PASSWORD,SERVICE) VALUES (\"{username}\",\"{password}\",\"{service}\");"
    c.execute(query)
    con.commit()
    print("commited successfully")          

def UserVerification(MasterID, MasterPass,con):
    c = con.cursor()
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
        return True #this is what the function returns 
    else:
        #print("No user found") # if pair is not matched 
        return False #If password id pair does not match  



def Searching(Service,MasterID,con):
    UID=MasterID
    c=con.cursor()
    c.execute("select service from "+MasterID)
    AquredServices=c.fetchall()
    if Service=="":
        c.execute(f"select * from {MasterID};")
        AllServ=c.fetchall()
        return AllServ

    # print(XX)
    for i in AquredServices:
        if i == (Service,):
            c.execute(f"select * from {MasterID} where service=\"{Service}\" ;")
            x=c.fetchall()
            return x
    return False

def PassGen(Lenght=16):
    P="".join(random.choices(string.ascii_letters + string.digits , k=Lenght))
    return P

def delrecord(MasterID,userID,service,con):
    try:
        query = f"delete from {MasterID} where USERID = \"{userID}\" and SERVICE = \"{service}\""
        c = con.cursor()
        c.execute(query)
        con.commit()
        return 1
    except Exception:
        print(Exception)
        return 0
