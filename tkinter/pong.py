from tkinter import *
from time import *
import random
import math
root = Tk()
canvasWidth = 1000
canvasHeight = 800
canvas = Canvas(root,height=canvasHeight,width=canvasWidth,bg="#fff")
canvas.pack()
antSpeed = 1.5

class Ball:
    def __init__(self,canvas, x, y, diameter, color, xVelocity, yVelocity):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
    
    def move(self):

        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)
        self.setDirection()
    
    def setDirection(self):
        angle = math.atan(self.yVelocity/self.xVelocity)

def key_handler(event):
    #print(event.char, event.keysym, event.keycode)

    if(event.keycode == 87): #w
        print("framåt")
        ball1.yVelocity = -1
        ball1.xVelocity = 0.000000001 #får inte vara 0
    elif(event.keycode == 65): #a
        print("vänster")
        ball1.xVelocity = -1
        ball1.yVelocity = 0.000000001
    elif(event.keycode == 83): #s
        print("bakåt")
        ball1.yVelocity = 1
        ball1.xVelocity = 0.000000001
    elif(event.keycode == 68): #d
        print("höger")
        ball1.xVelocity = 1
        ball1.yVelocity = 0.000000001

root.bind("<Key>", key_handler)   

ball1 = Ball(canvas, 10, 10, 50, "red",1,1)

while True:
    ball1.move()
    root.after(10)
    root.update()



root.mainloop()


