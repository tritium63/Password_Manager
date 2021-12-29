import mysql.connector
# logging into my local mysql server for trial
conn = mysql.connector.connect(host = 'localhost', user ='aditya', password='adimysql')

c= conn.cursor()

#selected the database
c.execute('use my_db')

#fucntion to create user as explained by in the image sent on whatsapp
def addUser(USERID,PASSWORD):

    #adds user to users table
    c.execute("select USERID from headlogin")
    userList = c.fetchall()
    for i in userList:
        if USERID==i[0]:
            print("sorry the username alredy exists")
            return 1
        else:
            query1 = f'INSERT INTO headlogin (USERID,PASSWORD) VALUES (\"{USERID}\",\"{PASSWORD}\")'
            c.execute(query1)
            c.commit()
            #create table USERID(USERID VARCHAR(32),PASSWORD VARCHAR(32),SERVICE VARCHAR(32));
            query2 = f"create table {USERID}(USERID VARCHAR(32),PASSWORD VARCHAR(32),SERVICE VARCHAR(32));"
            c.execute(query2)
            c.commit()
            return 0

            
conn.close()

# addUser("Aditya")
# addUser("Aditya Bakshi")
# addUser("Raghav Verma")
# after calling the functions as above 

#users table is ->
# +---------+---------------+
# | user_id | name          |
# +---------+---------------+
# |       1 | Aditya        |
# |       2 | Aditya Bakshi |
# |       3 | Raghav Verma  |
# +---------+---------------+

#all tables are
# +-----------------+
# | Tables_in_my_db |
# +-----------------+
# | user1           |
# | user2           |
# | user3           |
# | users           |
# +-----------------+

#user1 table has following feilds 
# +----------+--------------+------+-----+---------+-------+
# | Field    | Type         | Null | Key | Default | Extra |
# +----------+--------------+------+-----+---------+-------+
# | website  | varchar(100) | YES  |     | NULL    |       |
# | username | varchar(50)  | YES  |     | NULL    |       |
# | pass     | varchar(20)  | YES  |     | NULL    |       |
# +----------+--------------+------+-----+---------+-------+

#this was description of table user1, table1 is currently an empty set