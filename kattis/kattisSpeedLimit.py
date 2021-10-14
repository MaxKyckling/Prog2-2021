#https://open.kattis.com/problems/speedlimit

n = int(input())
timeTotal = 0
mileage = 0

input = input().split()
if len(input) != 2:
    print("felaktig input")
time = int(input[1]) 
print("time: ", time)
print("timetotal: ", timeTotal)
if timeTotal != 0:
    time -= timeTotal
    print("time ", time)
timeTotal = int(input[1])
print("timetotal: ", timeTotal)

speed = int(input[0])

mileage += speed*time
print("mileage: ", mileage )

