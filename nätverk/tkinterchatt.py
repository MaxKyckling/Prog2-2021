from tkinter import *
from socket import *
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

def hostServer():
    
    s = socket()
    host = str(getStringFromEntry(entryIP))
    port = int(getStringFromEntry(entryPort))
    print(host, port)
    s.bind((host,port))
    s.listen()
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
buttonClinet = Button(root, text="Join Server").grid(row=2,column=1, sticky=N+S+E+W)



'''
import time
TIME_INTERVAL = 0.2
from _thread import *

starta tråd, med funktionnamn och attribut (print_letters, (attribut))
start_new_thread(print_letters, ())

start_new_thread(print_numbers, ())

tid för att förhindra mainthreaden att yeeta iväg
time.sleep(30*TIME_INTERVAL)
'''

root.mainloop()