from tkinter import *
from time import *
import random
import math
root = Tk()
canvasWidth = 1000
canvasHeight = 800
canvas = Canvas(root,height=canvasHeight,width=canvasWidth,bg="#000000")
canvas.pack()

class Ball:
    def __init__(self,canvas, x, y, diameter, color, xVelocity, yVelocity, obstacles):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.obstacles = obstacles
        self.image = canvas.create_oval(x,y,x+diameter,y+diameter,fill=color)
    
    def move(self):
        
        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)
        #print(coordinates[0],coordinates[1],coordinates[2],coordinates[3])
        for i in range(0,len(self.obstacles)): #för varje objekt bollen kan kollidera med
            print(self.obstacles[i].x)
            for j in range(self.obstacles[i].width): #för varje x-värde i objektets area
                print(j)
                #for n in range(self.obstacles[i].height): #för varje y-värde 

            #if not (((x1-self.x)**2) + (( y1-self.y)**2) <= (self.diameter/2)**2):
             #   pass
            #else:
             #   self.xVelocity = -self.xVelocity
              #  self.yVelocity = -self.yVelocity

        self.setDirection()
    
    def setDirection(self):
        angle = math.atan(self.yVelocity/self.xVelocity)

class Rectangle:
    def __init__(self,canvas, x, y, width, height, color, xVelocity, yVelocity):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.image = canvas.create_rectangle(x,y,x+width,y+height,fill=color)
    
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
        rect1.yVelocity = -1
        rect2.xVelocity = 0.000000001 #får inte vara 0
    elif(event.keycode == 83): #s
        print("bakåt")
        rect1.yVelocity = 1
        rect1.xVelocity = 0.000000001
    elif(event.keycode == 40): #ner
        rect2.yVelocity = 1
        rect2.xVelocity = 0.000000001
    elif(event.keycode == 38): #upp
        rect2.yVelocity = -1
        

 

root.bind("<Key>", key_handler)   

rect1 = Rectangle(canvas, 10, 10, 30, 50, "red",1,1)
rect2 = Rectangle(canvas, 100, 10, 30,50, "blue",1,1)
players = [rect1, rect2]
ball1 = Ball(canvas, 300,300, 30, "white", 1,1,players)

while True:
    rect1.move()
    rect2.move()
    ball1.move()
    root.after(10)
    root.update()

#https://stackoverflow.com/questions/12262017/python-checking-if-coordinates-are-within-circle

root.mainloop()


