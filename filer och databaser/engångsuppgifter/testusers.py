import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testapp"
)
mycursor = mydb.cursor()
print("Uppkopplad till databasen!")

sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
val = ("kennybenny", "bab12345")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
# Läsa från databasen
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
