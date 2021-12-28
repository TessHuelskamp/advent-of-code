import operator

with open("./input.txt", "r") as f:
    lines = f.readlines()


lines = [map(int, list(line.strip())) for line in lines]

height=len(lines)
width=len(lines[0])
numflashes=0

def getNeighbors(h, w):
    ns = list()
    for i in range(h-1, h+1+1):
        for j in range(w-1, w+1+1):
            if i==h and j==w:
                continue
            if not (0 <= i < height):
                continue
            if not (0 <= j < width):
                continue
            ns.append((i,j))
    return ns

def getAll():
    size=len(lines)
    for i in range(size):
        for j in range(size):
            yield i, j

def pprint(lines):
    #assert len(lines) == 10
    for line in lines:
        #assert len(line) == 10
        pass

    for line in lines:
        print(",".join(map(str, line)))
    print()

pprint(lines)
for r in range(1000):

    for i, j in getAll():
        lines[i][j]+=1

    flashed=set()

    toFlash=True
    while toFlash:
        toFlash=False
        for i, j in getAll():
            if (i,j) in flashed:
                continue

            if lines[i][j] > 9:
                toFlash=True
                flashed.add((i,j))
                for ni, nj in getNeighbors(i,j):
                    lines[ni][nj]+=1

    for i, j in getAll():
        if lines[i][j] >9:
            lines[i][j] = 0

    numflashes+=len(flashed)

    if r < 10:
        pprint(lines)
        print(flashed)

    # zero based ranges :)
    if r == 100-1:
        print(numflashes)

    if len(flashed) == 100:
        # zero based ranges :)
        print(r+1)
        break
