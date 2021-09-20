#https://open.kattis.com/problems/redistribution

try:
      rumLen = int(input("Hur många rum finns det? Det får vara mellan 2 och 30 rum."))
      if (rumLen<2):
            raise Exception("Det får inte finnas mindre än 2 rum!")
      if (rumLen>30):
            raise Exception("Det får inte finnas mer än 30 rum!")
      print(rumLen)
      rum = [int(rum) for rum in input("Ange antal elever i vardera rum, t.ex (3 4 5 ger 3 elever i första rummet och 4 elever i andra rummet etc. )").split()]
      if(len(rum) != rumLen):
            raise Exception("Du måste ange antal elever för alla rum.")
except:
      print("Något gick fel")

bigRoom = max(rum)
papers = 0

while rum:
      print(rum)
      print(papers)
      papers += max(rum) #antal papper är samma som antal elever i största rummet
      print(papers)
      del rum[rum.index(max(rum))] #bort med stora rummet
      if(len(rum) != 0):
            papers -= max(rum) #delar ut pappren till det nya stora rummet
            print(papers)
      else:
            papers -= bigRoom
            if papers == 0:
                  print("det funkar")
            else:
                  print(papers)
                  print("Impossible")
#vi har rummen med 11, 9, 3 och 2 pers
#11 ger 9 till rummet med 9 och plockar upp 9, vilket ger 2 från rum 1 och 9 från rum 2
#dumpar 2 från rum 1 och 1 från rum 2 i rum 3, samt plockar upp 3 vilket ger att vi har 8 från rum 2 och 3 från rum 3
#dumpar 2 från rum 2 till rum 4 så vi har 6 från rum 2, 3 från rum 3 och 2 från rum 4 för totalt 11 papper
#vi dumpar resterande papper i rum 1 vilket fungerar