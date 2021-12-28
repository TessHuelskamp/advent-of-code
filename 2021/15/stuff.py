import heapq

with open("./input.txt", "r") as f:
    lines = f.readlines()

cave = [ map(int, line.strip()) for line in lines ]

# Annoyingly there's no heap class in python. Writing a wrapper around heapQ
class Heap:
    def __init__(self): self.heap = list()
    def push(self, point): heapq.heappush(self.heap, point)
    def pop(self): return heapq.heappop(self.heap)
    def isEmpty(self): return len(self.heap) == 0


startX, startY = 0, 0
endX, endY = len(cave[0])-1, len(cave)-1
caveSize = len(cave)


def getNeighbors(x, y, expansion=1):
    possible = [ (x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    possible = [ x for x in possible if 0<=x[0]<caveSize*expansion and 0<=x[1]<caveSize*expansion ]
    return possible

def getCost(x, y):
    return cave[y][x]

# Got the pseudo code over here: https://levelup.gitconnected.com/dijkstra-algorithm-in-python-8f0e75e3f16e
def djikstra(startNode=(0,0), endNode=(99,99), getCost=getCost, getNeighbors=getNeighbors):
    shortestDistance = {startNode: 0 }
    minDistanceHeap = Heap()

    # push the distance and the node as a pair so it sorts on distance in pos[0]
    minDistanceHeap.push((0, startNode))
    seen=set()

    while not minDistanceHeap.isEmpty():
        parentDistance, node = minDistanceHeap.pop()
        if node in seen:
            continue
        seen.add(node)
        x, y = node

        for neigh in getNeighbors(x,y):
            nx, ny = neigh
            distanceFromStart = parentDistance + getCost(nx, ny)

            shorterDistance = shortestDistance.get(neigh, distanceFromStart)
            shortestDistance[neigh] = shorterDistance

            if neigh not in seen:
                minDistanceHeap.push((shorterDistance, neigh))



    return shortestDistance[endNode]

res = djikstra()
assert res == 707
print(res)

#### PART 2 ####
grid=5
largeEndX = largeEndY = len(cave) * 5 - 1

"""
0 1 2 3 4
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
"""
def getDiffFromBase(x, y):
    dx = x // caveSize
    dy = y // caveSize
    return dx + dy

assert getDiffFromBase(100, 0) == 1
assert getDiffFromBase(0, 100) == 1
assert getDiffFromBase(0, 499) == 4
assert getDiffFromBase(200, 499) == 6
assert getDiffFromBase(499,499) == 8

def getCostLarge(x, y):
    ogCost = getCost(x%caveSize,y%caveSize)
    tempCost = ogCost + getDiffFromBase(x,y)

    if tempCost > 9:
        tempCost-=9
    return tempCost % 10

assert getCost(0,8) == 8
assert getCostLarge(0,108) == 9
assert getCostLarge(0,208) == 1
assert getCostLarge(100,108) == 1
assert getCostLarge(0,308) == 2

def getNeighborsLarge(x,y):
    return getNeighbors(x,y, grid)


res2 = djikstra((0,0), (499,499), getCostLarge, getNeighborsLarge)
assert res2 == 2942
print(res2)
