import mysql.connector as ms
mydb=ms.connect(host='localhost',password='Dpking@2073',username='root',database="mydatabase")
mycursor=mydb.cursor()

#deleting row's data:
sql='delete from customer where name="jp"'
mycursor.execute(sql)
mydb.commit()

#retrieving row's data:
mycursor.execute("select * from customer")
myresult=mycursor.fetchall()
print(myresult)
