import mysql.connector as ms
mydb=ms.connect(host='localhost',password='Dpking@2073',username='root',database="mydatabase")
mycursor=mydb.cursor()

#updating row's data:
sql='update customer set address="bareja" where id="4"'
mycursor.execute(sql)
mydb.commit()

#retrieving row's data:
mycursor.execute("select * from customer")
myresult=mycursor.fetchall()
print(myresult)
