from tkinter import * 
from socket import *
from _thread import * 

class Client:
    def __init__(self):
        self.lmbdown = False
        self.drawRadius = 30
        
    
    def getStringFromEntry(self, entryName):
        string = entryName.get()
        return string

    def start(self):
        self.root = Tk()
        self.root.withdraw()

        self.login = Toplevel(width=150, height =50)
        self.labelIP = Label(self.login, text= "IP: ").grid(row=0, column=0)
        self.labelPort = Label(self.login, text= "Port: ").grid(row=1,column=0)

        self.entryIP = Entry(self.login)
        self.entryPort = Entry(self.login)

        self.entryIP.grid(row=0, column=1)
        self.entryPort.grid(row=1,column=1)

        self.joinButton = Button(self.login, text="Join", command = self.joinServer)
        self.joinButton.grid(row = 2, column = 1, sticky = N+S+W+E)

    def startCanvas(self):
        self.root.deiconify()
        self.canvas = Canvas(self.root, height = 500, width = 1000, bg="blue")
        self.canvas.pack()

        print("canvas startat")
    
    def joinServer(self):
        self.s = socket()
        self.host = self.getStringFromEntry(self.entryIP)
        self.port = int(self.getStringFromEntry(self.entryPort))    
        self.s.connect((self.host, self.port))
        self.login.withdraw()
        self.startCanvas()
        start_new_thread(self.waitForMessage, (self.s,))
    
    def waitForMessage(self, conn):
        while True:
            b = conn.recv(1024)
            msg = b.decode("utf-16")
            msgArray = [int(msgArray) for msgArray in msg.split()]
            x, y = msgArray[0], msgArray[1]
            self.canvasDraw(x,y)
    
    def canvasDraw(self, x, y):
        offset = self.drawRadius/2
        self.canvas.create_oval(x-offset, y-offset, x+offset, y+offset, fill = "black")

    def motion(self,event):
        self.x, self.y = event.x, event.y

    def mouseDown(self,event):
        print("mouseDown")
        self.lmbdown = True
    
    def mouseUp(self,event):
        print("mouseup")
        if(event.state == 256):
            self.lmbdown = False
    
    def mouseStateCheck(self):
            if (self.lmbdown == True):
                self.sendDrawInformation()
    
    def sendDrawInformation(self):
        msg = str(self.x) + " " + str(self.y)
        b = msg.encode("utf-16")
        self.s.send(b)

client = Client()
client.start()
client.root.focus_set()
client.root.bind('<Button-1>', client.mouseDown)
client.root.bind("<ButtonRelease>", client.mouseUp)
client.root.bind('<Motion>', client.motion)

def gameHandler(): #använder detta ist för en thread för att en thread är onödigt snabb och kallar på koden snabbare än vad som hinner uppfattas
    client.mouseStateCheck()
    client.root.after(3,gameHandler)

gameHandler()

client.root.mainloop()