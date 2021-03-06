import tkinter as tk
import socket
import threading 
import pickle
from tkinter import messagebox

class Client:
    def __init__(self):
        self.GUIHandler = GUI()
        self.serverHandler = ServerInteraction()

class ServerInteraction:
    def __init__(self):
        pass

    #loop för att lyssna efter meddelanden från servern
    def waitForMessage(self, conn):
        while True:
            try:
                b = conn.recv(4096)
                messageArray = pickle.loads(b)
            except ConnectionError:
                print("Tappat kontakten med servern")
                messagebox.showerror("Error", "Tappade kontakt med servern!")
                client.GUIHandler.chattHistory.insert('end', "Tappade kontakten till servern!")
                return
            if(messageArray[0] == "Recieved_message"):
                client.GUIHandler.chattHistory.insert('end', messageArray[1]+"\n")
                client.GUIHandler.chattHistory.see('end')
            elif(messageArray[0] == "Errormessage"): #värdet på arrayns första index bestämmer vad man gör med meddelandet
                messagebox.showerror(messageArray[1],messageArray[2]) #ex. messageArray[0] == "Errormessage" då skapar man ett errormessage med värdena messageArray[1] och messageArray[2] som är förbestämda
            elif(messageArray[0] == "Login"):
                client.id = messageArray[1]
                client.username = messageArray[2]
                client.password = messageArray[3]
                client.GUIHandler.chat()
            elif(messageArray[0] == "registrerad"):
                messagebox.showinfo("Grattis!", "Profil skapad!")
            elif(messageArray[0] == "History"):
                for i in range(0, len(messageArray[1])): #loopar genom listan med historiken i st gånger
                    client.GUIHandler.chattHistory.insert('end', messageArray[1][i]+"\n")
                client.GUIHandler.chattHistory.see('end')

    def sendMessage(self, messageArray): #skickar iväg en Array som man bestämmer när man kallar på funktioner
        data = pickle.dumps(messageArray)
        self.s.send(data)

    #använder inmatat input och kopplar till servern
    def joinServer(self):
        self.s = socket.socket()
        self.host = client.GUIHandler.getStringFromEntry(client.GUIHandler.entryIP)
        self.port = int(client.GUIHandler.getStringFromEntry(client.GUIHandler.entryPort))    
        self.s.connect((self.host, self.port))

        waitForMessageThread = threading.Thread(target=self.waitForMessage,args= (self.s,)) #lyssna efter meddelanden
        waitForMessageThread.start()

        client.GUIHandler.loginBuildGUI() #funktionen som skapar själva inloggningsUI:n 
        client.GUIHandler.serverLogin.withdraw()
    
    def registerUser(self):
        #skapar en array där index 0 ger en string som representerar typen av meddelande, och resterande index för de värden man kommer använda (vilket man vet är användarnamn och lösenord eftersom att man kan bestämma vilken funktion man använder, exempelvis "register")
        messageArray = ["register", client.GUIHandler.getStringFromEntry(client.GUIHandler.entryRegisterName), client.GUIHandler.getStringFromEntry(client.GUIHandler.entryRegisterPassword)]
        if(messageArray[1] == '' or messageArray[2] == ''):
            messagebox.showerror("Error", "Alla fält måste vara ifyllda!")          #Om en eller flera entries är tomma, error
        else:
            self.sendMessage(messageArray)

    def loginUser(self):
        messageArray = ["login", client.GUIHandler.getStringFromEntry(client.GUIHandler.entryName), client.GUIHandler.getStringFromEntry(client.GUIHandler.entryPassword)]
        if(messageArray[1] == '' or messageArray[2] == ''):
            messagebox.showerror("Error", "Alla fält måste vara ifyllda!")
        else:
            self.sendMessage(messageArray)
    
    def sendWrittenMessage(self,s): #skapar en array med en sträng som används för att bestämma vad man gör med arrayn, och en sträng med själva texten
        messageArray = ["WrittenMessage", client.username + ": " + client.GUIHandler.getStringFromEntry(client.GUIHandler.chattEntry)]
        self.sendMessage(messageArray)
        client.GUIHandler.chattEntry.delete(0,'end') #tömmer entry-widgeten på text #56


class GUI:
    def __init__(self):
        pass

    def getStringFromEntry(self, entryName):
        string = entryName.get()
        return string

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
        self.joinButton = tk.Button(self.serverLogin, text="Join", command = client.serverHandler.joinServer)
        self.joinButton.grid(row=4, column = 1, sticky = tk.N+tk.S+tk.W+tk.E)

    def loginBuildGUI(self): #UI för inloggningen
        self.root.withdraw()
        #login
        self.login = tk.Toplevel(width=150, height =300)
        self.login.title('Login')
        #frames
        self.loginFrameLogin = tk.Frame(self.login)
        self.loginFrameRegister = tk.Frame(self.login)

        #^^ ingen .grid funktion ännu, därför att de "kopplas" på och av (.grid, .grid_forget)

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
        self.loginButton = tk.Button(self.loginFrameLogin, text="Login", command = client.serverHandler.loginUser)
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
        self.registerButton = tk.Button(self.loginFrameRegister, text="Register", command = client.serverHandler.registerUser)
        self.goBackButton = tk.Button(self.loginFrameRegister, text="Go Back", command = self.loginGUI)
        self.registerButton.grid(row=4, column = 1, sticky = tk.N+tk.S+tk.W+tk.E)
        self.goBackButton.grid(row=5, column = 1, sticky = tk.N+tk.S+tk.W+tk.E)

        self.loginGUI()

    #GUI för själva inmatningen av inloggningsuppgifter där man använder .grid och .grid_forget för att byta
    def loginGUI(self):
        try:
            print("loginGUI")
            self.loginFrameRegister.grid_forget()
            self.loginFrameLogin.grid()
        except:
            print("något gick fel i loginGUI")
    
    def registerGUI(self): #GUI för själva inmatningen av inloggningsuppgifter där man använder .grid och .grid_forget för att byta
        try:
            print("registerGUI")
            self.loginFrameLogin.grid_forget()
            self.loginFrameRegister.grid()
        except:
            print("fel i registerGUI")

    def chat(self):
        #ladda ner tidigare historik
        messageArray = ["Get history"]
        client.serverHandler.sendMessage(messageArray)

        #bygg själva chatten med tkinter
        self.root.title('Chatt')

        self.upperFrame = tk.Frame(self.root) #delar upp i två olika frames, en för chatten och scrollen (övre) och en för input och knapp
        self.lowerFrame = tk.Frame(self.root)
        self.chattHistory = tk.Text(self.upperFrame,height= 13, width = 60)

        self.upperFrame.grid(row=0, column = 0, sticky = tk.N+tk.S+tk.W+tk.E)
        self.lowerFrame.grid(row=1, column= 0, sticky = tk.N+tk.S+tk.W+tk.E)
        self.chattHistory.grid(row = 0, column = 0, sticky = tk.N+tk.S+tk.W+tk.E)

        self.chattHistoryScrollbar = tk.Scrollbar(self.upperFrame) #tkinter scrollbar för chatten
        self.chattHistoryScrollbar.grid(row = 0, column = 1, sticky = 'NSE')
        self.chattHistoryScrollbar.config(command = self.chattHistory.yview)

        self.chattEntry = tk.Entry(self.lowerFrame, width= 56)
        
        self.chattButton = tk.Button(self.lowerFrame, text= "Skicka", command=lambda : client.serverHandler.sendWrittenMessage(client.serverHandler.s))
        self.chattEntry.grid(row=0, column=0, sticky = tk.N+tk.S+tk.W+tk.E)
        self.chattButton.grid(row=0, column=1, sticky = tk.N+tk.S+tk.W+tk.E)
        
        self.root.deiconify()
        self.login.withdraw()
        client.serverHandler.sendMessage(["WrittenMessage", client.username + " har anslutit!"]) #skickar samma slags meddelande som sparas och skickas till alla användare att användare N är nu med

client = Client()
client.GUIHandler.joinServerGUI()

client.GUIHandler.root.mainloop()