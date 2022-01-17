from tkinter import *
from tkinter import messagebox
#https://open.kattis.com/problems/timeloop

root = Tk()
root.title("Gör ett eller flera program med fönster som innehåller ett flertal widgets och som tar input från användaren i fönstret, behandlar denna på något sätt och visar output i fönstret. Du ska hantera layout med metoden pack.")
canvasWidth = 750
canvasHeight = 500
window = Tk()
text1 = Text(window, )
text1.pack()
window.title("Resultat")
window.withdraw()


def button():
    try:
        n = int(entry1.get())
        if(n < 1):
            messagebox.showerror("errorWindow","tal 1-100")
        elif(n > 100):
            messagebox.showerror("errorWindow","tal 1-100")
        else:
            window.deiconify()
            for i in range(1,n+1):
                var = str(i) + " Abrakadabara"
                text1.insert(END, var + '\n')
    except:
        messagebox.showerror("errorWindow","tal 1-100")
    
label1 = Label(root, text= "Skriv ett nummer mellan 1 och 100").pack()
entry1 = Entry(root,width = 30)
entry1.pack()
button1 = Button(root, width = 30, text = "button", command = button).pack(fill=X)

root.mainloop()