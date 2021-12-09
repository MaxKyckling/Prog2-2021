vokaler = ['a','e','i','o','u','y']

antal_ord = int(input("Antal ord ? "))
mening = input("Mening ? ").split()
svar = ''

for i in range(0, len(mening)):
    mening[i] = list(mening[i])

for i in mening: #loopar genom varje ord
    for j in range(0, len(i)): #loopar genom varje bokstav
        try:
            if i[j] in vokaler and i[j+1] not in vokaler and i[j+2] not in vokaler:
                del i[j]
        except:
            pass

for i in mening[::-1]:
    for n in i[::-1]:
        svar += n
    svar += ' '

print(svar)
        




