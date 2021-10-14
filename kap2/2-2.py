class Djur:
    def __init__(self,namn):
        self.namn = namn
    
    def at(self):
        print(self.namn, " äter")
    
    def sov(self):
        print(self.namn, " sover!")

class Fagel(Djur):
    def __init__(self,namn, vingspann):
        super().__init__(namn)
        self.vingspann = vingspann

class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup
    
class Haj(Fisk):
    def __init__(self, namn, maxdjup, antalTander):
        super().__init__(namn, maxdjup)
        self.antalTander = antalTander
    
    def at(self, djur):
        print(self.namn, " äter djuret", djur.namn, "!!!")

class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet
    
    def simma(self):
        print(self.namn, "simmar!!!1!")
        

def catch(haj, torsk):
    if (isinstance(haj, Haj) == False) or (isinstance(torsk, Torsk) == False):
        print("De inmatade objekten måste vara av korrekt klass")
        return None
    else:
        if((torsk.hastighet < 30) and haj.maxdjup >= torsk.maxdjup):
            return True
        else:
            return False
    
torsk1 = Torsk("Nemo", 300, 29)
haj1 = Haj("Bruce", 310, 3004567)

print(catch(haj1, torsk1))

torsk1.simma()

haj1.at(torsk1)
