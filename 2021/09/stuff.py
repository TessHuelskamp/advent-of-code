import operator

with open("./input.txt", "r") as f:
    lines = f.readlines()


lines = [map(int, list(line.strip())) for line in lines]

height= len(lines)
width=len(lines[0])

def getNeighbors(h, w):
    ns = [ (h+1, w), (h-1, w), (h, w-1), (h, w+1)]
    return list(filter(lambda x: 0 <= x[0] < height and 0 <= x[1] < width, ns))

def getNeighborVal(h, w):
    for nh, nw in getNeighbors(h, w):
        yield lines[nh][nw]

def getBasinSize(h, w):
    toVisit={(h,w)}
    basinSeen=set()

    while toVisit:
        # basin is every neighbor that's 1 above it that is NOT nine
        ch, cw = toVisit.pop()
        cVal = lines[ch][cw]

        basinSeen.add((ch, cw))

        for nh, nw in getNeighbors(ch, cw):
            nVal = lines[nh][nw]
            if nVal != 9 and (nh, nw) not in basinSeen:
                toVisit.add((nh, nw))

    return len(basinSeen)


totalDangerous=0
totalLowPoints=0
basinSizes=list()
for h in range(height):
    for w in range(width):
        # look things up to make sure I did this right
            val = lines[h][w]
            minNeighbor = min(getNeighborVal(h, w))

            isLowPoint = val < minNeighbor
            if isLowPoint:
                totalDangerous += val+1
                totalLowPoints += 1

            if isLowPoint:
                basinSizes.append(getBasinSize(h, w))




assert totalDangerous==530
print(totalDangerous)


assert totalLowPoints == len(basinSizes)
basinSizes = sorted(basinSizes)
product = reduce(operator.mul, basinSizes[-3:], 1)

print(product)


