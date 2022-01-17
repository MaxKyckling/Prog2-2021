from re import L
from tkinter import *
from time import *
import random
import math

root = Tk()
root.title("0 | 0")
canvasWidth = 750
canvasHeight = 500
playerSpeed = 3
ballSpeed = 5
canvas = Canvas(root,height=canvasHeight,width=canvasWidth,bg="black")
canvas.pack()
image1 = PhotoImage(file='tkinter/number1.png')
image2 = PhotoImage(file='tkinter/number2.png')
image3 = PhotoImage(file='tkinter/number3.png')

class Image:
    def __init__(self,root, canvas, x, y, image):
        self.root = root
        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = image
            
    def draw(self):
        self.image = canvas.create_image(self.x,self.y, image=self.image)


class Ball:
    def __init__(self,root,canvas, x, y, diameter, color, xVelocity, yVelocity, obstacles):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.obstacles = obstacles
        self.scoreRed = 0
        self.scoreBlue = 0
        self.image = canvas.create_oval(x,y,x+diameter,y+diameter,fill=color)
        self.root = root
        self.scoreRed = -1
        self.scoreBlue = 0
        self.isMoving = True
        self.tick = 0
    
    def move(self):
        if(self.tick > 0): #ville inte göra på det här sättet men fick RecursionError: maximum recursion depth exceeded in comparison ifall jag använde en funktion för det
            self.tick += 1
            if(self.tick > 60):
                self.isMoving = True
                self.tick = 0

        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width())):
            self.xVelocity = -self.xVelocity #blå dör, röd vinner
            self.scoreRed +=1
            title = str(self.scoreRed)+" | "+str(self.scoreBlue)
            self.root.title(title)
            self.moveToCenter(coordinates)
            self.isMoving = False
            self.tick = 1
        if(coordinates[0]<0): #röd dör, blå vinner
            self.xVelocity = -self.xVelocity
            self.scoreBlue +=1
            title = str(self.scoreRed)+" | "+str(self.scoreBlue)
            self.root.title(title)
            self.moveToCenter(coordinates)
            self.isMoving = False
            self.tick = 1
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity
    
        #kollision rektanglar
        if(coordinates[1]<self.obstacles[1].coordinates[3] and coordinates[3]>=self.obstacles[1].coordinates[1]):
            if(coordinates[2]>self.obstacles[1].coordinates[0]):
                self.xVelocity = -abs(self.xVelocity)
        if(coordinates[1]<self.obstacles[0].coordinates[3] and coordinates[3]>self.obstacles[0].coordinates[1]):
            if(coordinates[0]<self.obstacles[0].coordinates[2]):
                self.xVelocity = abs(self.xVelocity)             
        if(self.isMoving == True):
            self.canvas.move(self.image,self.xVelocity,self.yVelocity)

    def moveToCenter(self, coordinates):
        deltaX = canvasWidth/2 - coordinates[0]
        deltaY = canvasHeight/2 - coordinates[1]
        print(self.x, deltaX)
        print(self.y, deltaY)
        self.canvas.move(self.image,deltaX,deltaY)
        root.update()


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

        self.coordinates = self.canvas.coords(self.image)
        if(self.coordinates[2]>=(self.canvas.winfo_width()) or self.coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(self.coordinates[3]>=(self.canvas.winfo_height()) or self.coordinates[1]<0):
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)

def key_handler(event):
    if(event.keycode == 87): #w
        rect1.yVelocity = -playerSpeed
        rect2.xVelocity = 0.000000001 #får inte vara 0
    elif(event.keycode == 83): #s
        rect1.yVelocity = playerSpeed
        rect1.xVelocity = 0.000000001
    elif(event.keycode == 40): #ner
        rect2.yVelocity = playerSpeed
        rect2.xVelocity = 0.000000001
    elif(event.keycode == 38): #upp
        rect2.yVelocity = -playerSpeed
  
        
root.bind("<Key>", key_handler)

rect1 = Rectangle(canvas, 0, canvasHeight/2, 15, 80, "red",0.00000001,1)
rect2 = Rectangle(canvas, canvasWidth-15, canvasHeight/2, 15,80, "blue",0.00000001,1)
players = [rect1, rect2]
ball1 = Ball(root, canvas, canvasWidth/2,canvasHeight/2, 15, "white", ballSpeed, ballSpeed,players)


while True:
    if(ball1.tick ==1):
        image = Image(root, canvas, canvasWidth/2, 100, image3)
        image.draw()
    if(ball1.tick == 20):
        canvas.delete(image.image)
        image = Image(root, canvas, canvasWidth/2, 100, image2)
        image.draw()
    if(ball1.tick == 40):
        canvas.delete(image.image)
        image = Image(root, canvas, canvasWidth/2, 100, image1)
        image.draw()
    if(ball1.tick == 60):
        canvas.delete(image.image)
    rect1.move()
    rect2.move()
    ball1.move()
    root.after(10)
    root.update()

root.mainloop()