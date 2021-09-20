#test

import time

ladder = "\\"
space = " "

for n in range(1, 10):
    print(ladder)
    ladder = space + ladder
    time.sleep(0.1)

ladder = "/"

for n in range(1, 10):
    print(ladder)
    ladder = space + ladder
    time.sleep(0.1)