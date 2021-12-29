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
            
conn.close()

