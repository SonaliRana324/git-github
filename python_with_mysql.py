import mysql.connector as connector
class DBHelper:
    # Creating connection
    def __init__(self):
        self.con = connector.connect(host = 'localhost' , port = '3306' , user = 'root' ,
                                     password = '1234' , database = 'python_with_mysql')
        query = 'create table if not exists user(userid int auto_increment  primary key, username varchar(20), phone varchar(20))'
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        #print("Created")
    # Insert
    def insert_into(self, userid, username, phone):
        query = 'insert into user(userid , username , phone) values({}, "{}" , "{}" )'.format(userid , username , phone)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to database")

    # Fetch All
    def fetch_all(self):
        query = " select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Userid :" , row[0])
            print("Username :", row[1])
            print("Phone :" , row[2])
            print()
            print()

    # Delete Record
    def delete_record(self , userid):
        query= f"delete from user where userid = {userid} "
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

    #Update
    def update_table(self,userid, newname, newphone):
        query = f'update user set username = "{newname}" , phone = "{newphone}" where userid = {userid}'
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Table Updated")







 # connection of python program to database:
#helper = DBHelper()

#Inserting data using python to Database
#helper.insert_into(679 , "Shin" , "85747")
#helper.insert_into(680 , "Scan" , "85749")
#helper.insert_into(681 , "Sxnbx" , "85749")
#helper.insert_into(682 , "Seiuei" , "74749")

#fetching data using python
#helper.fetch_all()

#Delete record using python
#helper.delete_record
#helper.fetch_all()

# Update the table
#helper.update_table(678 , "shakira" , "99999999")
#helper.fetch_all()



