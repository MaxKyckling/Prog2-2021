list = []

try:
    n = int(input("Välj antal integers i listan (1-5): "))
    if(n>5 or n<1):
        print("n får inte vara större än 5 eller mindre än 1, starta om programmet")
    for i in range(0, n):
        list.append(int(input("Välj ett tal ")))
    for i in range(0, n):
        print(list[-1-i])
except:
    print("Något gick fel, starta om programmet")