from tkinter import *
from socket import *
from _thread import *
from tkinter import messagebox

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
        msg = getStringFromEntry(chattEntry)
        b = msg.encode("utf-16")
        s.send(b)

def joinServer():
    s = socket()
    host = getStringFromEntry(entryIP)
    port = int(getStringFromEntry(entryPort))
    name = getStringFromEntry(entryName)
    s.connect((host, port))
    start_new_thread(sendMessage, (s,))
    start_new_thread(waitForMessage, (s,))
    return s


root = Tk()
root.title('Chatt')

upperFrame = Frame(root)
upperFrame.grid(row=0, column = 0, sticky = N+S+E+W)
lowerFrame = Frame(root)
lowerFrame.grid(row=1, column= 0, sticky = N+S+E+W)
chattHistory = Listbox(upperFrame,height= 13, width = 60)
chattHistory.grid(row = 0, column = 0, sticky = N+S+W+E)
for line in range(100):
   chattHistory.insert(END, "This is line number " + str(line))

chattHistoryScrollbar = Scrollbar(upperFrame)
chattHistoryScrollbar.grid(row = 0, column = 1, sticky = 'NSE')
chattHistoryScrollbar.config(command = chattHistory.yview)

chattEntry = Entry(lowerFrame, width= 56)
chattEntry.grid(row=0, column=0, sticky = N+S+W+E)
chattButton = Button(lowerFrame, text= "Skicka", command=sendMessage)
chattButton.grid(row=0, column=1, sticky = N+S+W+E)
root.withdraw()

#login
login = Toplevel(width=150, height =50)
login.title('Login')
#labels
labelLogin = Label(login, text = "Login")
labelName = Label(login, text= "Namn: ")
labelIP = Label(login, text = "IP: ")
labelPort = Label(login, text = "Port: ")
labelLogin.grid(row=0, column=1)
labelName.grid(row=1, column = 0)
labelIP.grid(row=2, column = 0)
labelPort.grid(row=3, column= 0)
#entries
entryName = Entry(login)
entryIP = Entry(login)
entryPort = Entry(login)
entryName.grid(row=1, column=1, sticky=N+S+W+E)
entryIP.grid(row=2, column=1, sticky = N+S+W+E)
entryPort.grid(row=3, column=1, sticky = N+S+W+E)
#button
joinButton = Button(login, text="Join", command = joinServer)
joinButton.grid(row=4, column = 1, sticky = N+S+W+E)

root.mainloop()