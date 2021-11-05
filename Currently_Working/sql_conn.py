def Sql_Connection():
    import mysql.connector
    Conector=mysql.connector.connect(host="bk3mjn0digzdwyfts1ir-mysql.services.clever-cloud.com", user="umterzn51pcaf9nw", password="sNwAPpmFIKjYG17iwZKJ")
    #for debuging
    print("Connected")