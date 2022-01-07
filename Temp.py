import mysql.connector
conn = mysql.connector.connect(host = 'bk3mjn0digzdwyfts1ir-mysql.services.clever-cloud.com', user ='umterzn51pcaf9nw', password='sNwAPpmFIKjYG17iwZKJ', database ="bk3mjn0digzdwyfts1ir")

def Update(UserID, Service, PassWord,con): 
    c=con.cursor()
    try:
        c.execute(f"update TestID SET PASSWORD=\"{PassWord}\" WHERE USERID=\"{UserID}\" AND SERVICE=\"{Service}\";")
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
while int(input()):
    print(Update(input(),input(),input(),conn))