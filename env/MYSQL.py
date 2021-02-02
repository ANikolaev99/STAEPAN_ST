import sys
import mysql.connector
from mysql.connector import errorcode

try:
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="qwerty-123",
      port="3306",
      database="stepan"
    )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    sys.exit()
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
    sys.exit()
  else:
    print(err)
    sys.exit()

cursor = db.cursor()
#cursor.execute("CREATE DATABASE stepan")

#cursor.execute("CREATE TABLE users (name VARCHAR(255))")
#cursor.execute("SHOW TABLES")

cursor.execute("ALTER TABLE users ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT UNIQUE)")


