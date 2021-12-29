import mysql.connector
# logging into my local mysql server for trial
conn = mysql.connector.connect(host = 'bk3mjn0digzdwyfts1ir-mysql.services.clever-cloud.com', user ='umterzn51pcaf9nw', password='sNwAPpmFIKjYG17iwZKJ', database ="bk3mjn0digzdwyfts1ir")
c=conn.cursor()
while True:
    x=input("Enter comand")
    if x=="exit":
        conn.close()
        break
    else:
        c.execute(x)
        # c.commit()
        print(c.fetchall())
    