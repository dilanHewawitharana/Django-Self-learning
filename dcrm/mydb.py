import mysql.connector;

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'abcd1234',
    auth_plugin='mysql_native_password'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE crm_database")

print("All Done!")
