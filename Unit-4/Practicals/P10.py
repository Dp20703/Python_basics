#Creating a table:
import mysql.connector as ms
try:
    mydb=ms.connect(host='localhost',username='root',password='Dpking@2073',database='sample_db')
    mycursor=mydb.cursor()

    if mydb is None:
        print("Connection is not established...")
    else:
        print("Connection is established...")



#updating salary of employee dynamacally:
    id=input('Enter Employee id:')
    inc=int(input("Enter increment amount:"))
    sql='update emp set sal=sal+%s  where id=%s'
    val=(inc,id)
    # mycursor.execute('delete from emp where name="dd"')
    mycursor.execute(sql,val)
    print("Record Updated")
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

