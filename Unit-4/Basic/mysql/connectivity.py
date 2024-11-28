import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dpking@2073'
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")


if mydb.is_connected():
    print("Connection is established...")

