#Creating a table:
import mysql.connector as ms
try:
    mydb=ms.connect(host='localhost',username='root',password='Dpking@2073',database='sample_db')
    mycursor=mydb.cursor()

    if mydb is None:
        print("Connection is not established...")
    else:
        print("Connection is established...")
    print('111')
    mycursor.execute('show tables')
    tables=mycursor.fetchall()
    print(tables)
    # mycursor.execute('drop table Newemp')
    # mycursor.execute('create table Newemp(eno int,ename char(30),gender char(1),salary float)')
    print("New Employee table created")

except:
    print("error")

