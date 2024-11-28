#Creating a table:
import mysql.connector as ms
try:
    mydb=ms.connect(host='localhost',username='root',password='Dpking@2073',database='sample_db')
    mycursor=mydb.cursor()

    if mydb is None:
        print("Connection is not established...")
    else:
        print("Connection is established...")



#deleting data of table dynamacally:
    id=input('Enter Employee id:')
    sql=f'delete from emp where id="{id}"'
    # sql='delete from emp  where id=%s'
    # val=(id)
    # mycursor.execute('delete from emp where name="dd"')
    mycursor.execute(sql)
    print("Record Deleted")
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

