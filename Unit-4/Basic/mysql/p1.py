import mysql.connector as ms;
mydb=ms.connect(host='localhost',password='Dpking@2073',username='root',database="mydatabase")
if mydb.is_connected():
   print("Connection is estlablished....")
mycursor=mydb.cursor()


#creating a table:
# mycursor.execute("create table Newstudent(id int ,name varchar(255),branch varchar(255))")


#inserting values:
# sql ='insert into Newstudent(id,name,branch) values(%s,%s,%s)'
# values=(5,"dp","bca")
# mycursor.execute(sql,values)
# mydb.commit()

#delting values:
# sql ='delete from Newstudent where name="dp"'
# mycursor.execute(sql)
# mydb.commit()

#updating  data:
# sql=mycursor.execute("update Newstudent set id='2' where name='dp'")
# mycursor.execute(sql)
# mydb.commit()

#retrieving data:
mycursor.execute("select * from Newstudent")
myresult=mycursor.fetchall()
print(myresult)
