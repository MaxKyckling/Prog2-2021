#https://open.kattis.com/problems/buka
#om log(A) ger ett positivt tal, 1, 2, 3 etc. så är det till the power of 10
from math import log10

def A():
    a = int(input("Välj ett tal A, som är to the power of 10 "))
    check = (log10(a))
    if check != int(check):
        print("Talet måste vara till the power of 10")
        return None
    else:
        check = str(a)
        if len(check) > 100:
            print("A får inte ha fler än 100 siffror")
            return None
        else:
            return a
    

def B():
    b = int(input("Välj ett tal B, som är to the power of 10 "))
    check = (log10(b))
    if check != int(check):
        print("Talet måste va till the power of 10")
        return None
    else:
        check = str(b)
        if len(check) > 100:
            print("B får inte ha fler än 100 siffror")
            return None
        else:
            return b


def main():
    a = None
    b = None
    while a == None:
        a = A()
    operator = input("Välj om du ska använda addition '+' eller multiplikation '*'")
    while b == None:
        b = B()
    if operator == '*':
        sum = a * b
        print(sum)
    if operator == '+':
        sum = a + b
        print(sum)

        
    

    
    
    
#try:
main()
#except:
 #   print("Något gick fel, vänligen försök igen!")
  #  main()