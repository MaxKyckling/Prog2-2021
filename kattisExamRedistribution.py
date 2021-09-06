#https://open.kattis.com/problems/redistribution

try:
      rumLen = int(input("Hur många rum finns det? Det får vara mellan 2 och 30 rum."))
      if (rumLen<2):
            raise Exception("Det får inte finnas mindre än 2 rum!")
      if (rumLen>30):
            raise Exception("Det får inte finnas mer än 30 rum!")
      print(rumLen)
      rum = [int(rum) for rum in input("Ange antal elever i vardera rum, t.ex (3 4 5 ger 3 elever i första rummet och 4 elever i andra rummet etc. )").split()]
      print(rum)
      if(len(rum) != rumLen):
            raise Exception("Du måste ange antal elever för alla rum.")
except:
      print("Något gick fel")
      