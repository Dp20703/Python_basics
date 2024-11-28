#Creating a table:
import mysql.connector as ms
try:
    mydb=ms.connect(host='localhost',username='root',password='Dpking@2073',database='sample_db')
    mycursor=mydb.cursor()

    if mydb is None:
        print("Connection is not established...")
    else:
        print("Connection is established...")



#inserting data into table dynamacally:
    while('True'):
        choice=input("Would you like to enter record:")
        if (choice=='yes' or choice=='Yes'):
            id=input("Enter employee id:")
            name=input("Enter employee name:")
            sal=int(input("Enter employee salary:"))
            sql='insert into emp(id,name,sal) values(%s,%s,%s)'
            values=(id,name,sal)
            mycursor.execute(sql,values)
            mydb.commit()
        elif(choice=='No'or choice=='no'):
            break
        else:
            print("wrong Input!")


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

