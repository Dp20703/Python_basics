import mysql.connector as ms
mydb=ms.connect(host='localhost',password='Dpking@2073',username='root',database="mydatabase")
mycursor=mydb.cursor()

#creating table:
# mycursor.execute('create table student(name varchar(33),address varchar(255),age int)')

# #inserting row's data:
# sql='insert into student(name,age) values(%s,%s)'
# values=('red',22)
# mycursor.execute(sql,values)
# mydb.commit()

#retrieving row's data:
mycursor.execute("select * from student")
myresult=mycursor.fetchall()
print(myresult)
