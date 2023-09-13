# importing module
import mysql.connector

# initiate connection to mysql server
mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password=''
)

print(mydb)