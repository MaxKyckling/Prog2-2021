import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="prog2"
)
mycursor = mydb.cursor()
print("Uppkopplad till databasen!")

sql = "INSERT INTO klasskompisar (id, förnamn, efternamn, längd, hårfärg, idiot) VALUES (%s, %s, %s, %s, %s, %s)"
val = (0, "Test", "Kenny", 1000, "flintskallig", 1)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
# Läsa från databasen
mycursor.execute("SELECT * FROM klasskompisar")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
