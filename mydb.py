import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Fad12345679*'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE filiz3")

print("All Done!")