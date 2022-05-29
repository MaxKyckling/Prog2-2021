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
        try:
            b = conn.recv(4096)
        except ConnectionError:
            print(f"Connection from {conn} has been lost")
            try:
                index = clients.index(conn) #hittar vilket index connectionen hade
                print(index)
                print(names[index])
                messageArray = ['', f"{names[index]} har lämnat forumet!"] 
                if(conn in clients):
                    clients.remove(conn)
                    names.remove(names[index])
                addToChatHistory(messageArray)
                broadcastMessage(messageArray)
            except:
                clients.remove(conn)
                 #namnet läggs endast till efter att man loggat in, vilket betyder att om man inte loggar in behöver servern inte berätta för andra att kontakten brutits
            return
        messageArray = pickle.loads(b) #tar emot en array och bestämmer vad den ska göra baserat på vad arrayns första index har för värde
        if(messageArray[0] == "WrittenMessage"):
            addToChatHistory(messageArray)
            broadcastMessage(messageArray)
        elif(messageArray[0] == "register"): 
            registerUser(conn,messageArray)
        elif(messageArray[0] == "login"):
            loginUser(conn,messageArray)
        elif(messageArray[0] == "Get history"):
            getHistory(conn)

def addToChatHistory(messageArray):
    sql = "INSERT INTO chat (Text) VALUES (%s)"
    val = (messageArray[1])
    mycursor.execute(sql, (val,))
    mydb.commit()

def sendMessage(s, messageArray):
    data = pickle.dumps(messageArray)
    s.send(data)

def broadcastMessage(messageArray):
    messageArray[0] = "Recieved_message"
    for client in clients:
        sendMessage(client, messageArray)

def waitForClient(s):
    while True:
        s.listen()
        conn, addr = s.accept()
        print("en ny klient anslöt")
        clients.append(conn) #sparar vilken klient som har vilken connection
        waitForMessageThread = threading.Thread(target=waitForMessage,args= (conn,))
        waitForMessageThread.start()

def registerUser(conn, messageArray): #skapar en sql-sträng för att inserta värdena för username och password
    username = messageArray[1]
    password = messageArray[2]
    sql = ("SELECT ID FROM users WHERE username = %s") #kollar efter ett id med angivna användarnamn 
    mycursor.execute(sql, (username,))
    idresult = mycursor.fetchone()
    if(idresult == None): #Om det inte finns ett ID med användarnamnet så är det tillgängligt!
        messageArray = ["registrerad"]
        sendMessage(conn, messageArray)
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
    else: #Om det finns ett ID med användarnamnet så är det otillgängligt
        messageArray = ["Errormessage", "Error", "Användarnamnet är upptaget!"]
        sendMessage(conn, messageArray)

def loginUser(conn, messageArray): #andra och trejde indexen i messageArray innehåller användarnamn och lösen respektivt
    username = messageArray[1]
    password = messageArray[2]
    sql = ("SELECT ID FROM users WHERE username = %s and password =%s") #letar efter det ID med angivna användarnamn och lösen
    mycursor.execute(sql, (username, password,))
    idresult = mycursor.fetchone()
    if(idresult == None): #Om det inte finns ett ID med lösen och användarnamn så har man skrivit in fel, för då finns användaren inte
        messageArray = ["Errormessage", "Error", "Felaktigt lösenord eller användarnamn!"]
        sendMessage(conn, messageArray)
    else:
        names.append(username)
        messageArray = ["Login", idresult, username, password]
        sendMessage(conn, messageArray)

def getHistory(conn):
    sql = "SELECT Text FROM chat"
    
    mycursor.execute(sql)
    fetched_data = mycursor.fetchall() #hämtar en lista av tuples, men jag vill ha strängar inte tuples så...
    history = [''.join(i) for i in fetched_data] #För varje tuple i listan konverterar den till en sträng
    messageArray = ["History", history]
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