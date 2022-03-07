import random
import os

class Guesser:
    def __init__(self):
        self.randomNumber = random.randint(1,101)


    def createFiles(self):
        try:
            os.mkdir("undermapp")
        except:
            pass
        for i in range(1, 100):
            self.f = open("undermapp/exempel" + str(i) + ".txt", "a")
            if(i == self.randomNumber):
                text = "Bingo!"
                self.f.write(text)






guesser = Guesser()
guesser.createFiles()