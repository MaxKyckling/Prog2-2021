#https://open.kattis.com/problems/triangleornaments

nTriangles = int(input())

for i in range(1, nTriangles+1):
    ornament = [int(n) for n in input().split()] #a b c [a,b,c]
    print(ornament)


    #använd cosinussatsen