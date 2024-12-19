import sys
sys.setrecursionlimit(10000)


debugFile = ''


size = 7 if debugFile else 70+1
firstBits = 12 if debugFile else 1024

board = [[ "." for _ in range(size)] for _ in range(size)]

fallingStuff = list()

with open("./input."+debugFile+".txt" if debugFile else "./input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    x, y = [int(x) for x in line.split(",")]

    fallingStuff.append((x, y))

class Board:
  def __init__(self, size, fallingStuff, firstBits):
    self.board = [[ "." for _ in range(size)] for _ in range(size)]
    self.fallingStuff = fallingStuff
    self.size = size
    self.firstBits = firstBits
  
  def __len__(self):
    return self.size
  
  def thingFalls(self, x, y):
    try:
      self.board[y][x] = "#"
    except IndexError as e:
      print(x, y)
      raise e

  def blocked(self, x, y):
    return self.board[y][x] == "#"
  
  def partOne(self):
    for i, val in enumerate(self.fallingStuff):
      if i >= self.firstBits: continue
      self.thingFalls(*val)
    
    return self.runShortestPath()
    
  def key(self, x, y):
    return str(x)+"-"+str(y)
  
  def rKey(self, aKey):
    x, y = [int(x) for x in aKey.split("-")]
    return x, y
  
  def neighbors(self, x, y):
    # return right and down first
    possible = [
      [x+1, y],
      [x, y+1],
      [x, y-1],
      [x-1, y],
    ]

    return [p for p in possible if self.onBoard(*p) ]

  def onBoard(self, x, y):
    return 0 <= x and x<self.size and 0<=y and y<self.size

    
  def visit(self, x, y, steps):
    if self.blocked(x, y): return

    myKey = self.key(x, y)
    mySteps = self.shortestSteps.get(myKey)
    
    if mySteps and mySteps < steps:
      return
    
    # This is the shortest way to get to this point
    # mark it and visit the neighbors
    self.shortestSteps[myKey] = steps

    for neighbor in self.neighbors(x, y):
      nKey = self.key(*neighbor)
      nSteps = self.shortestSteps.get(nKey)

      if nSteps is None or nSteps > steps+1:
        self.visit(*neighbor, steps+1) 


  def partTwo(self):
    for i, val in enumerate(self.fallingStuff):
      self.thingFalls(*val)
      # maybe there's a way to binary search this :shrug:
      if i < self.firstBits: continue

      if i %100 == 0:
        print("thinking... ", i)

      if self.runShortestPath() is None:
        return self.key(*val).replace('-', ',')
  
    return None


  def runShortestPath(self):
    # clear out shortest-steps
    shortestSteps = dict()

    # steps, x y
    toVisit = [[0, 0, 0]]

    while toVisit:
      steps, x, y = toVisit[0]
      toVisit = toVisit[1:]

      if self.blocked(x, y): continue

      key = self.key(x, y)
      currentVal = shortestSteps.get(key)
      
      if currentVal is None or steps < currentVal:
        shortestSteps[key]=steps
        
        for neighbor in self.neighbors(x, y):
          xx, yy = neighbor
          toVisit.append([steps+1, xx, yy])
      
      # print(toVisit)
      # short toVisit based off of first val
      toVisit.sort(key=lambda x: x[0])

    # print(shortestSteps)

    lowerRight = self.key(self.size-1, self.size-1)


    if lowerRight in shortestSteps:
      return shortestSteps[lowerRight]
    else:
      return None
  
  def printBoard(self):
    for line in self.board:
      print("".join(line))


board = Board(size, fallingStuff, firstBits)


print(board.partOne())

# board.printBoard()
print(board.partTwo())
