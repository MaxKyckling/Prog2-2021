#Implementera en funktion som beräknar och returnerar eller skriver ut summan av ett godtyckligt antal inmatade tal

#försökte fixa input men när jag väl hade en lista av ints så var själva asterisken onödig och jag visste inte hur jag skulle omvandla min lista till en mängd olika tal så jag sket i det för fuck det här

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
    

print(add(3,5,7))

def food(s, vegan=False):
    if vegan == True:
        s = "soja"+s
    print(s)

food("mjölk")
food("mjölk", True)