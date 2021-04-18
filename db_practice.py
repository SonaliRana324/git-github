import mysql.connector as connector
class DBHelper:
    # Creating connection
    def __init__(self):
        self.con = connector.connect(host = 'localhost' , port = '3306' , user = 'root' ,
                                     password = '1234' , database = 'registration')
        query = "create table if not exists user( name varchar(20), gender varchar(10), phone int, address varchar(20))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")
    # Insert
    def insert_into(self,name,gender,phone,address):

        query = 'insert into user( name,gender , phone, address) values( "{}" , "{}",{},"{}" )'.format( name , gender , phone , address)
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
            print("name :", row[0])
            print("gender :" , row[1])
            print("phone :", row[2])
            print("address :" , row[3])

    # Delete Record
   # def delete_record(self , userid):
    #    query= f"delete from user where userid = {userid} "
     #   print(query)
      #  cur = self.con.cursor()
       # cur.execute(query)
        #self.con.commit()
        #print("Deleted")

    #Update
    #def update_table(self,userid, newname, newphone , newaddress, newgender):
     #   query = f'update user set username = "{newname}" , phone = "{newphone}" , address = "{newaddress}" where userid = {userid}'
      #  cur = self.con.cursor()
       # cur.execute(query)
      #  self.con.commit()
       # print("Table Updated")



