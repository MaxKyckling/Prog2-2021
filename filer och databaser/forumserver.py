from tkinter import *
from socket import *
from _thread import *
from tkinter import messagebox

clients, names = [], []

def getStringFromEntry(entryName):
    string = entryName.get()
    return string

def waitForMessage(conn):
    while True:
        index = clients.index(conn)
        name = names[index]
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        print(msg)
        message = (name + ": " + msg)
        broadcastMessage(message)
        

def sendMessage(s):
    while True:
        msg = input("skicka ett meddelande: ")
        b = msg.encode("utf-16")
        s.send(b)

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
        name = conn.recv(1024)
        name = name.decode("utf-16")
        names.append(name)
        clients.append(conn)
        broadcastMessage(name + " anslöt till chatten!")
        start_new_thread(waitForMessage, (conn,))

def hostServer():
    print("starting server...")
    s = socket()
    host = str(getStringFromEntry(entryIP))
    port = int(getStringFromEntry(entryPort))
    s.bind((host,port))
    start_new_thread(waitForClient, (s,))
    return s

root = Tk()

#IP widgets
labelIP = Label(root, text="IP: ").grid(row=0, column=0)
entryIP = Entry(root)
entryIP.grid(row=0, column=1)


#port widgets
labelPort = Label(root, text="Port: ").grid(row=1, column=0)
entryPort = Entry(root)
entryPort.grid(row=1, column=1)

buttonHost = Button(root, text="Host",command=hostServer).grid(row=2,column=1,sticky=N+S+E+W)

root.mainloop()