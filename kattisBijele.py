#https://open.kattis.com/problems/bijele

#input är 6 ints på en line, 0-10

def fel():
    print("You did something wrong, please try again!")

fullSet = [1, 1, 2, 2, 2, 8]

try:
    mirkoSet = [int(mirkoSet) for mirkoSet in input("How many kings, queens, rooks, bishops, knights and pawns? Separate with space: ").split()]
    if(len(mirkoSet) != 6):
        fel()
        pass
    else:
        for i in range(0, len(mirkoSet)):
            if ((mirkoSet[i] > 10) or (mirkoSet[i] < 0)):
                fel()
                break
    for i in range(0, len(mirkoSet)):
        print(fullSet[i] - mirkoSet[i], end=" ")
except:
    fel()
    

    