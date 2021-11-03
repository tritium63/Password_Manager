import mysql.connector
# logging into my local mysql server for trial
conn = mysql.connector.connect(host = 'localhost', user ='root', password='Aditya2004@google')

c= conn.cursor()

#selected the database
c.execute('use my_db')

#fucntion to create user as explained by in the image sent on whatsapp
def addUser(name):

    #adds user to users table
    #i don't need to specify user id as i have used auto_increment attribute while creating the users table
    #therefore only specifing name
    query1 = f'INSERT INTO `users` (name) VALUES ("{name}");'
    c.execute(query1)

    #since i have used auto increant therefore the latest user will have largest value of uesr_id;
    #hence selecting the max id to create a table on its name as user<id>
    q = "select max(user_id) from users;"
    c.execute(q)#<-max id stored in c
    x = c.fetchall()#<-fetching max id from c into x
    n=x[0][0] #<-the id was stored as list in list-> [[id]] therefore i added [0][0] meaning 0th index of 0th list in the list x
    # after finally getting the id given to the current user we can create table on his name
    query2=f"CREATE TABLE user{n}(website varchar(100), username varchar(50), pass varchar(20));"
    c.execute(query2)


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

c.close()
addUser("Aditya")