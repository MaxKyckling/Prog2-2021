import tkinter as tk
import socket
import threading 


class Client:
    def __init__(self):
        pass

    def getStringFromEntry(self, entryName):
        string = entryName.get()
        return string

    def waitForMessage(self, conn):
        while True:
            b = conn.recv(1024)
            msg = b.decode("utf-16")
            self.chattHistory.insert(threading.END, msg)

    def sendWrittenMessage(self, s):
        msg = self.getStringFromEntry(self.chattEntry)
        b = msg.encode("utf-16")
        s.send(b)

    def sendMessage(self, s): #just nu samma funktion som sendWrittenMessage
        while True:
            msg = self.getStringFromEntry(self.chattEntry)
            b = msg.encode("utf-16")
            s.send(b)

    #använder inmatat input och kopplar till servern
    def joinServer(self):
        self.s = socket.socket()
        self.host = self.getStringFromEntry(self.entryIP)
        self.port = int(self.getStringFromEntry(self.entryPort))    
        self.s.connect((self.host, self.port))

        self.loginBuildGUI()
        self.serverLogin.withdraw()

    #GUI för port och IP
    def joinServerGUI(self):
        self.root = tk.Tk()
        self.root.withdraw()
        #login
        self.serverLogin = tk.Toplevel(width=150, height =50)
        self.serverLogin.title('Join Server')
        #labels
        self.labelJoin = tk.Label(self.serverLogin, text = "Join server")
        self.labelIP = tk.Label(self.serverLogin, text = "IP: ")
        self.labelPort = tk.Label(self.serverLogin, text = "Port: ")
        #labels.grid
        self.labelJoin.grid(row=0, column=1)
        self.labelIP.grid(row=2, column = 0)
        self.labelPort.grid(row=3, column= 0)
        #entries
        self.entryIP = tk.Entry(self.serverLogin)
        self.entryPort = tk.Entry(self.serverLogin)
        self.entryIP.grid(row=2, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        self.entryPort.grid(row=3, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        #button
        self.joinButton = tk.Button(self.serverLogin, text="Join", command = self.joinServer)
        self.joinButton.grid(row=4, column = 1, sticky = tk.N+tk.S+tk.W+tk.E)

    def loginBuildGUI(self):
        self.root.withdraw()
        #login
        self.login = tk.Toplevel(width=150, height =300)
        self.login.title('Login')
        #frames
        self.loginFrameLogin = tk.Frame(self.login)
        self.loginFrameRegister = tk.Frame(self.login)

        #^^ ingen .grid funktion ännu

        #labels
        self.labelLogin = tk.Label(self.loginFrameLogin, text = "Login")
        self.labelName = tk.Label(self.loginFrameLogin, text= "Namn: ")
        self.labelPassword = tk.Label(self.loginFrameLogin, text= "Password: ")
        self.labelNoUser = tk.Label(self.loginFrameLogin, text= "No User? ")
        #labels grid
        self.labelLogin.grid(row=0, column=1)
        self.labelName.grid(row=1, column = 0)
        self.labelPassword.grid(row=2, column = 0)
        self.labelNoUser.grid(row=5, column= 0)
        #entries
        self.entryName = tk.Entry(self.loginFrameLogin)
        self.entryPassword = tk.Entry(self.loginFrameLogin)
        #entries grid
        self.entryName.grid(row=1, column=1, sticky= tk.N+tk.S+tk.W+tk.E)
        self.entryPassword.grid(row=2, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        #button
        self.loginButton = tk.Button(self.loginFrameLogin, text="Join", command = self.joinServer)
        self.signInButton = tk.Button(self.loginFrameLogin, text="Sign In", command = self.registerGUI)
        self.loginButton.grid(row=4, column = 1, sticky = tk.N+tk.S+tk.W+tk.E)
        self.signInButton.grid(row=5, column =1, sticky = tk.N+tk.S+tk.W+tk.E)

        #REGISTER GUI WIDGETS
        #labels
        self.labelRegister = tk.Label(self.loginFrameRegister, text = "Register")
        self.labelRegisterName = tk.Label(self.loginFrameRegister, text= "Namn: ")
        self.labelRegisterPassword = tk.Label(self.loginFrameRegister, text= "Password: ")
        #labels grid
        self.labelRegister.grid(row=0, column=1)
        self.labelRegisterName.grid(row=1, column = 0)
        self.labelRegisterPassword.grid(row=2, column = 0)
        #entries
        self.entryRegisterName = tk.Entry(self.loginFrameRegister)
        self.entryRegisterPassword = tk.Entry(self.loginFrameRegister)
        #entries grid
        self.entryRegisterName.grid(row=1, column=1, sticky= tk.N+tk.S+tk.W+tk.E)
        self.entryRegisterPassword.grid(row=2, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        #button
        self.registerButton = tk.Button(self.loginFrameRegister, text="Register", command = self.registerUser)
        self.goBackButton = tk.Button(self.loginFrameRegister, text="Go Back", command = self.loginGUI)
        self.registerButton.grid(row=4, column = 1, sticky = tk.N+tk.S+tk.W+tk.E)
        self.goBackButton.grid(row=5, column = 1, sticky = tk.N+tk.S+tk.W+tk.E)

        self.loginGUI()

    #GUI för själva inmatningen av inloggningsuppgifter
    def loginGUI(self):
        try:
            print("loginGUI")
            self.loginFrameRegister.grid_forget()
            self.loginFrameLogin.grid()
        except:
            print("något gick fel i loginGUI")
    
    def registerGUI(self):
        try:
            print("registerGUI")
            self.loginFrameLogin.grid_forget()
            self.loginFrameRegister.grid()
        except:
            print("fel i registerGUI")
    
    def registerUser(self):
        print("registerUser funktionen har aktiverats")

    def chat(self):
        self.root.title('Chatt')

        self.upperFrame = tk.Frame(self.root)
        self.lowerFrame = tk.Frame(self.root)
        self.chattHistory = tk.Listbox(self.upperFrame,height= 13, width = 60)

        self.upperFrame.grid(row=0, column = 0, sticky = tk.N+tk.S+tk.W+tk.E)
        self.lowerFrame.grid(row=1, column= 0, sticky = tk.N+tk.S+tk.W+tk.E)
        self.chattHistory.grid(row = 0, column = 0, sticky = tk.N+tk.S+tk.W+tk.E)

        self.chattHistoryScrollbar = tk.Scrollbar(self.upperFrame)
        self.chattHistoryScrollbar.grid(row = 0, column = 1, sticky = 'NSE')
        self.chattHistoryScrollbar.config(command = self.chattHistory.yview)

        self.chattEntry = tk.Entry(self.lowerFrame, width= 56)
        
        self.chattButton = tk.Button(self.lowerFrame, text= "Skicka", command=lambda : self.sendWrittenMessage(self.s))
        self.chattEntry.grid(row=0, column=0, sticky = tk.N+tk.S+tk.W+tk.E)
        self.chattButton.grid(row=0, column=1, sticky = tk.N+tk.S+tk.W+tk.E)

client = Client()
client.joinServerGUI()
client.root.mainloop()