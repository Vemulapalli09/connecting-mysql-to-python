import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Ajay@1234",database= "komeer")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

for i in mycursor:
	print(i)
	
