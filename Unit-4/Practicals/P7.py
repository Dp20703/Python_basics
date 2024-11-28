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
    # mycursor.execute('drop table emp')
    # mycursor.execute('create table emp(id varchar(10) primary key,name varchar(10),sal numeric(15))')
    print("Employee table created")



#inserting data into table:
    # mycursor.execute("insert into emp values('EMP01','KETAN','15000')")
    # mycursor.execute("insert into emp values('EMP02','RAHUL','18000')")
    # mycursor.execute("insert into emp values('EMP03','MAHESH','21000')")
    # mycursor.execute("insert into emp values('EMP04','SURESH','54000')")
    # mycursor.execute("insert into emp values('EMP05','JAY','54000'),('EMP06','SHIVAM','54000')")
    print("New Table Created")
    mydb.commit()


#Retriving data:
    mycursor.execute('select * from emp')
    rows=mycursor.fetchall()
    # print(rows)
    #To display all records:
    for i in rows:
        print(i)
    mydb.commit()
except:
    print("error")

