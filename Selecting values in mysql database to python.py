import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Ajay@1234",database= "komeer")

mycursor = mydb.cursor()

#mycursor.excute("CREATE TABLE person (name varchar(50), age INTEGER(10), personID INTEGER AUTO_INCREMENT PRIMARY KEY)")
mycursor.excute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Tim", 19))
db.commit()

mycursor.excute("SELECT * FROM Person")

for x in mycursor: 
     print(x)







     








	


