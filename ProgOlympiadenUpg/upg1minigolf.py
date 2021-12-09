#https://progolymp.se/2017/skolkval/kval17.pdf

nBanor = int(input("Antal banor ? "))
difference = 0
for i in range(1, nBanor+1):
    slag = int(input())
    if(slag > 7):
        slag = 7    

    if i % 2 == 0: #even
        difference += (slag - 3)
    else: #odd
        difference += (slag -2)
print("Differensen är: ", difference)