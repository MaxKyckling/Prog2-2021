import tkinter as tk
import socket
import threading
import pickle
import mysql.connector

#koppla till sql-servern
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="forum"
)
mycursor = mydb.cursor()
print("Uppkopplad till databasen!")

clients, names = [], []

def getStringFromEntry(entryName):
    string = entryName.get()
    return string

def waitForMessage(conn):
    while True:
        b = conn.recv(4096)
        messageArray = pickle.loads(b) #tar emot en array och bestämmer vad den ska göra baserat på vad arrayns första index har för värde
        if(messageArray[0] == "register"): 
            registerUser(messageArray)
        elif(messageArray[0] == "login"):
            loginUser(conn,messageArray)

def sendMessage(s, messageArray):
    data = pickle.dumps(messageArray)
    s.send(data)

def broadcastMessage(message):
    print(message)
    msg = message.encode("utf-16")
    for client in clients:
        client.send(msg)

def waitForClient(s):
    while True:
        s.listen()
        conn, addr = s.accept()
        print("en ny klient anslöt")
        clients.append(conn) #sparar vilken klient som har vilken connection
        waitForMessageThread = threading.Thread(target=waitForMessage,args= (conn,))
        waitForMessageThread.start()

def registerUser(messageArray):
    print("test")
    #skapar en sql-sträng för att inserta värdena för username och password
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (messageArray[1], messageArray[2])
    mycursor.execute(sql, val)
    mydb.commit()

def loginUser(conn, messageArray): #andra och trejde indexen i messageArray innehåller användarnamn och lösen respektivt
    username = messageArray[1]
    password = messageArray[2]
    print(username)
    print(password)
    sql = ("SELECT ID FROM users WHERE username = %s and password =%s") #letar efter det ID med angivna användarnamn och lösen
    mycursor.execute(sql, (username, password,))
    idresult = mycursor.fetchone()
    print(idresult)
    if(idresult == None): #Om det inte finns ett ID med lösen och användarnamn så har man skrivit in fel, för då finns användaren inte
        messageArray = ["Errormessage", "Error", "Felaktigt lösenord eller användarnamn!"]
        sendMessage(conn, messageArray)
    else:
        messageArray = ["Login", idresult, username, password]
        sendMessage(conn, messageArray)

    

def hostServer():
    print("starting server...")
    s = socket.socket()
    host = str(getStringFromEntry(entryIP))
    port = int(getStringFromEntry(entryPort))
    s.bind((host,port))
    waitForClientThread = threading.Thread(target= waitForClient, args=(s,))
    waitForClientThread.start()
    return s

root = tk.Tk()

#IP widgets
labelIP = tk.Label(root, text="IP: ").grid(row=0, column=0)
entryIP = tk.Entry(root)
entryIP.grid(row=0, column=1)


#port widgets
labelPort = tk.Label(root, text="Port: ").grid(row=1, column=0)
entryPort = tk.Entry(root)
entryPort.grid(row=1, column=1)

buttonHost = tk.Button(root, text="Host",command=hostServer).grid(row=2,column=1,sticky=tk.N+tk.S+tk.E+tk.W)

root.mainloop()