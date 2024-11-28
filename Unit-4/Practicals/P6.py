import mysql.connector as ms
mydb=ms.connect(host='localhost',username='root',password='Dpking@2073')
mycursor=mydb.cursor()

if mydb.is_connected():
    print("Connection is established...")


try:
    # mycursor.execute("create database sample_db")
    mycursor.execute("show databases")
    my=mycursor.fetchall()
    print('Database is Created \n')
    for i in my:
        print(i)
   
except:
    print("error")