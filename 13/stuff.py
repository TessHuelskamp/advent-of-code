
from sys import setrecursionlimit

with open("./input.txt", "r") as f:
    lines = f.readlines()

dots=set()
for line in lines:
    line = line.strip()
    if "," in line:
        left, right = line.split(",")
        left = int(left)
        right = int(right)
        dots.add((left,right))


    if "f" in line:
        _, _, ins= line.split(" ")
        print(ins)
        d, loc = ins.split("=")
        loc = int(loc)


        newDots=set()
        if d=="x":
            for x, y in dots:
                if x < loc:
                    newDots.add((x,y))
                else:
                    delta  = x - loc
                    newX = loc-delta
                    newDots.add((newX,y))
        else:
            for x, y in dots:
                if y < loc:
                    newDots.add((x,y))
                else:
                    delta  = y - loc
                    newY = loc-delta
                    newDots.add((x, newY))

        from copy import copy
        dots =copy(newDots)
        # 1 is x
        


print(dots)

for j in range(50):
    for i in range(50):
        if (i,j,) in dots:
            print("#", end="")
        else:
            print(".", end="")
    print()
