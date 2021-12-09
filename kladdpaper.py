import tkinter

root = tkinter.Tk()

def key_handler(event):
    print(event.char, event.keysym, event.keycode)

root.bind("<Key>", key_handler)

root.mainloop()
