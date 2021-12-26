import copy
import itertools

with open("./input.txt", "r") as f:
    sea = [ list(line.strip()) for line in f.readlines()]

h=len(sea)
w=len(sea[0])

def getSouth(hh, ww): return (hh+1)%h , ww
def getEast(hh, ww): return hh, (ww+1)%w

assert getSouth(0, 0) == (1, 0)
assert getSouth(1, 3) == (2, 3)
assert getSouth(h-1, 0) == (0, 0)

assert getEast(0, 0) == (0, 1)
assert getEast(0, 4) == (0, 5)
assert getEast(0, w-1) == (0, 0)

def getNewSea():
    return [ [ "." for _ in range(w) ] for _ in range(h) ]

newSea = getNewSea()
assert len(newSea) == len(sea)
assert len(newSea[0]) == len(sea[0])

def isRight(c): return c==">"
def isDown(c): return c=="v"
def isOpen(c): return c=="."

def move(sea, isEast=True, isSouth=False):
    assert isEast ^ isSouth

    newSea = getNewSea()
    if isEast:
        neighFun = getEast
        isSpecial= isRight
    elif isSouth:
        neighFun = getSouth
        isSpecial= isDown
    else:
        assert False

    for hh, ww in itertools.product(range(h), range(w)):

        spot = sea[hh][ww]
        if isOpen(spot):
            continue

        newSea[hh][ww] = spot


        if isSpecial(spot):
            hn, hw = neighFun(hh, ww)
            if isOpen(sea[hn][hw]):
                newSea[hn][hw] = spot
                newSea[hh][ww] = "."
    return newSea


i=1
while True:

    if False:
        print("="*10)
        for j, line in enumerate(sea):
            if j > 10: continue
            print("".join(line[:10]))

    oldSea = copy.copy(sea)

    temp = move(sea, isEast=True)
    sea  = move(temp, isEast=False, isSouth=True)

    if oldSea == sea:
        break

    i+=1

assert i == 560
print(i)



