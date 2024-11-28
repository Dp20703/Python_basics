import mysql.connector as ms
mydb=ms.connect(host='localhost',password='Dpking@2073',username='root',database="mydatabase")
mycursor=mydb.cursor()

#inserting row's data:
sql='insert into customer(id,name,age) values(%s,%s,%s)'
values=(2,'op',22)
mycursor.execute(sql,values)
mydb.commit()

#retrieving row's data:
mycursor.execute("select * from customer")
myresult=mycursor.fetchall()
print(myresult)
