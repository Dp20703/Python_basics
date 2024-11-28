import mysql.connector as ms;
mydb=ms.connect(host='localhost',password='Dpking@2073',username='root',database="mydatabase")
if mydb.is_connected():
   print("Connection is estlablished....")
mycursor=mydb.cursor()
# mycursor.execute('drop database mongodb')

#show tables:
mycursor.execute('show tables')
for x in mycursor:
   print(x)

#show table's data:
# 1.using fetchall():
mycursor.execute('SELECT * FROM customer')
myresult=mycursor.fetchall()
# print(myresult)
for x in myresult:
   print(x)

# 2.using fetchone():
mycursor.execute('SELECT * FROM customer')
# mycursor.execute('SELECT id FROM customer')
# mycursor.execute('SELECT name FROM customer')
# mycursor.execute('SELECT age FROM customer')
myresult=mycursor.fetchone()
print(myresult)
