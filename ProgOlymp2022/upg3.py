class N:
    def __init__(self, ockuperad, klattrat):
        self.ockuperad = False
        self.klattrat = False

class M:
    def __init__(self, klattrat):
        self.klattrat = False

antal_N = int(input("Antal med grönt kort, N  ? "))
antal_M = int(input("Antal utan grönt kort, M ? "))

Nlist = []
Mlist = []

for i in range(0, antal_N):
    klattrare = N(False, False)
    Nlist.append(klattrare)

for i in range(0, antal_M):
    klattrare = M(False)
    Mlist.append(klattrare)
     
tid = 0

if len(Nlist) > len(Mlist):
    for i in Mlist:
        i.klattrat = True
    for i in range(0,len(Mlist)):
        Nlist[i].ockuperad = True
    for i in Nlist:
        if i.ockuperad == True:
            pass
        else:
            
