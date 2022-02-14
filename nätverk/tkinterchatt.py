from tkinter import *
from socket import *
from _thread import *
from tkinter import messagebox

'''try:
        s = socket()
        IP = getStringFromEntry(entryIP)
        host = IP
        port = getStringFromEntry(entryPort)
        s.bind((host,port))
        s.listen()
        return s
    except:
        messagebox.showerror("Error", "Invalid IP or Port")'''

import time

def getStringFromEntry(entryName):
    string = entryName.get()
    return string

def waitForMessage(conn):
    while True:
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        print(msg)

def sendMessage(s):
    while True:
        msg = input("skicka ett meddelande: ")
        b = msg.encode("utf-16")
        s.send(b)

def waitForClient(s):
    while True:
        s.listen()
        conn, addr = s.accept()
        print("en ny klient anslöt")
        start_new_thread(waitForMessage, (conn,))
        start_new_thread(sendMessage, (conn,))
        #test
        msg = "Servern säger hej till klienten! Hur mår du idag?"
        b = msg.encode("utf-16")
        conn.send(b)

def hostServer():
    print("starting server...")
    s = socket()
    host = str(getStringFromEntry(entryIP))
    port = int(getStringFromEntry(entryPort))
    s.bind((host,port))
    start_new_thread(waitForClient, (s,))
    return s
    
def joinServer():
    print("joining server")
    s = socket()

    host = str(getStringFromEntry(entryIP))
    port = int(getStringFromEntry(entryPort))
    s.connect((host, port))
    start_new_thread(sendMessage, (s,))
    start_new_thread(waitForMessage, (s,))
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

buttonHost = Button(root, text="Host",command=hostServer).grid(row=2,column=0,sticky=N+S+E+W)
buttonClinet = Button(root, text="Join Server",command=joinServer).grid(row=2,column=1, sticky=N+S+E+W)

chatt = Toplevel(width=300, height = 100)
chattHistory = Listbox(chatt,height= 13, width = 60)
chattHistory.grid(row = 0, column = 0, sticky = N+S+W+E)
for line in range(100):
   chattHistory.insert(END, "This is line number " + str(line))

chattHistoryScrollbar = Scrollbar(chatt)
chattHistoryScrollbar.grid(row = 0, column = 1, sticky = 'NSW')
chattHistoryScrollbar.config(command = chattHistory.yview)
#chatt.withdraw()

'''
import time
TIME_INTERVAL = 0.2

starta tråd, med funktionnamn och attribut (print_letters, (attribut))
start_new_thread(print_letters, ())

start_new_thread(print_numbers, ())

tid för att förhindra mainthreaden att yeeta iväg
time.sleep(30*TIME_INTERVAL)
'''

root.mainloop()