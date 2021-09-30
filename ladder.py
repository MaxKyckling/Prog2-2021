#test

import time


switches = int(input("Hur många gånger kommer den byta håll? "))

loops = int(input("Hur lång ska den bli? "))

def drawRight(loops, iSpace):
    ladder = "\\"
    space = " "
    for n in range(1, loops):
        print(iSpace + ladder)
        iSpace = iSpace + space
        time.sleep(0.05)
    return iSpace

def drawLeft(loops, iSpace):
    space = " "
    ladder = "/"

    for n in range(1, loops):
        iSpace = iSpace[1::1]
        print(iSpace + ladder)
        time.sleep(0.05)
    return iSpace

for i in(1, switches):
    print(i)
    #iSpace = drawRight(loops, "")

    #iSpace = drawLeft(loops, iSpace)

