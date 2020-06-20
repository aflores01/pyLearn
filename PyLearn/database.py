#Crud
import mysql.connector

class databaseClass:
    def __init__(self):
        self.conn = mysql.connector.connect(host="192.168.88.251",database="people",user="root",password="my-secret-pw")
        self.cursor = self.conn.cursor()

    def getData(self):
        self.cursor.execute('select * from people')
        for row in self.cursor:
            print(row)

    def insertData(self,name,country):
        query = ("INSERT INTO people(name,country) VALUES('"+ name +"','"+ country+"')")
        self.cursor.execute(query)
        self.conn.commit()

    def deleteData(self,id):
        query = ("DELETE FROM people WHERE id = '"+ id +"'")
        self.cursor.execute(query)
        self.conn.commit()
    
    def updateData(self,id,name,country):
        query = ("UPDATE people SET name = '"+ name +"', country = '"+ country +"' WHERE id = '"+ id +"'")
        self.cursor.execute(query)
        self.conn.commit()
