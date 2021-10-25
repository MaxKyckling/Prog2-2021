#program som bestämmer hur många siffror 0-9 som går åt

sidor = int(input())
antalSiffror = [0,0,0,0,0,0,0,0,0,0]
for i in range(1, sidor+1):
    if i % 2 == 0:
        pass
    else:
        if(i < 10):
            int(i)
            antalSiffror[i] += 1
        else:
            iList = list(map(int, str(i)))
            for i in range(0, len(iList)):
                antalSiffror[iList[i]] += 1
print(antalSiffror)