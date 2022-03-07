import os



def InputOutput():
    f = open("chattHistorik.txt", "a")
    inputText = input("Skriv något som ska sparas: ")
    text = inputText + "\n"
    f.write(text)
    f = open("chattHistorik.txt", "r")
    print(f.read())
    f.close()
    os.remove("chattHistorik.txt") # markera som kommentar för att dubbelkolla dess innehåll

InputOutput()