from tkinter import *
from socket import *
from _thread import *
from tkinter import messagebox

class user:
    def __init__(self):
        pass

    def getStringFromEntry(self, entryName):
        string = entryName.get()
        return string

    def waitForMessage(self, conn):
        while True:
            b = conn.recv(1024)
            msg = b.decode("utf-16")
            self.chattHistory.insert(END, msg)

    def sendWrittenMessage(self, s):
        msg = self.getStringFromEntry(self.chattEntry)
        b = msg.encode("utf-16")
        s.send(b)

    def joinServer(self):
        self.s = socket()
        self.host = self.getStringFromEntry(self.entryIP)
        self.port = int(self.getStringFromEntry(self.entryPort))    
        self.s.connect((self.host, self.port))

        #skicka namn
        self.name = self.getStringFromEntry(self.entryName)
        b = self.name.encode("utf-16")
        self.s.send(b)
        self.login.withdraw()
        self.root.deiconify()
        start_new_thread(self.waitForMessage, (self.s,))

    def login(self):
        self.root = Tk()
        self.root.withdraw()
        #login
        self.login = Toplevel(width=150, height =50)
        self.login.title('Login')
        #labels
        self.labelLogin = Label(self.login, text = "Login")
        self.labelName = Label(self.login, text= "Namn: ")
        self.labelIP = Label(self.login, text = "IP: ")
        self.labelPort = Label(self.login, text = "Port: ")
        #labels.grid
        self.labelLogin.grid(row=0, column=1)
        self.labelName.grid(row=1, column = 0)
        self.labelIP.grid(row=2, column = 0)
        self.labelPort.grid(row=3, column= 0)
        #entries
        self.entryName = Entry(self.login)
        self.entryIP = Entry(self.login)
        self.entryPort = Entry(self.login)
        self.entryName.grid(row=1, column=1, sticky=N+S+W+E)
        self.entryIP.grid(row=2, column=1, sticky = N+S+W+E)
        self.entryPort.grid(row=3, column=1, sticky = N+S+W+E)
        #button
        self.joinButton = Button(self.login, text="Join", command = self.joinServer)
        self.joinButton.grid(row=4, column = 1, sticky = N+S+W+E)

    def chat(self):
        self.root.title('Chatt')

        self.upperFrame = Frame(self.root)
        self.lowerFrame = Frame(self.root)
        self.chattHistory = Listbox(self.upperFrame,height= 13, width = 60)

        self.upperFrame.grid(row=0, column = 0, sticky = N+S+E+W)
        self.lowerFrame.grid(row=1, column= 0, sticky = N+S+E+W)
        self.chattHistory.grid(row = 0, column = 0, sticky = N+S+W+E)

        self.chattHistoryScrollbar = Scrollbar(self.upperFrame)
        self.chattHistoryScrollbar.grid(row = 0, column = 1, sticky = 'NSE')
        self.chattHistoryScrollbar.config(command = self.chattHistory.yview)

        self.chattEntry = Entry(self.lowerFrame, width= 56)
        
        self.chattButton = Button(self.lowerFrame, text= "Skicka", command=lambda : self.sendWrittenMessage(self.s))
        self.chattEntry.grid(row=0, column=0, sticky = N+S+W+E)
        self.chattButton.grid(row=0, column=1, sticky = N+S+W+E)

        self.root.mainloop()

client = user()
client.login()
client.chat()
client.joinServer()