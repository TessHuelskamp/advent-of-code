
debugFile = ''
board= list()

with open("./input."+debugFile+".txt" if debugFile else "./input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    board.append(list(line))



class Board:
  def __init__(self, board):
    self.board = board
    self.size = len(self.board)
  
  def __len__(self):
    return self.size
  
  def find(self, val):
    for i, line in enumerate(self.board):
      for j, vall in enumerate(line):
        if val == vall:
          return (i, j)

  def blocked(self, i, j):
    return self.board[i][j] == "#"
  
  def partOne(self):
    return self.runShortestPath()
  
  def partTwo(self):
    if not self.lowestVal or len(self.lowestVal) == 0:
      # populate dir
      self.runShortestPath()

    # too high: 544


    ei, ej = self.find("E")
    minDir = self.minDir(ei, ej)

    value = self.lowestVal[self.key(ei, ej, minDir)]

    seen = set()
    added = {self.key(ei, ej, minDir)}
    toVisit = [[value, ei, ej, minDir]]

    while toVisit:
      val, i, j, dir = toVisit[0]
      toVisit = toVisit[1:]
      seen.add(self.keyy(i, j))

      for dirr in ["N", "S", "E", "W"]:
        try:
          vall = self.lowestVal[self.key(i, j, dirr)]
        except KeyError:
          continue

        aKey = self.key(i, j, dirr)

        if val-1000 == vall or val-1 == vall and aKey not in added:
          added.add(aKey)
          toVisit.append([vall, i, j, dirr])

      
      for n in self.neighbors(i, j):
        ii, jj = n
        for dirr in ["N", "S", "E", "W"]:
          try:
            vall = self.lowestVal[self.key(ii, jj, dirr)]
          except KeyError:
            continue

          # An optimal path goes through this value if we can back-track
          # A solution that is 1 or 1000 less than this thing


          aKey = self.key(ii, jj, dirr)

          if val-1000 == vall or val-1 == vall and aKey not in added:
            added.add(aKey)
            toVisit.append([vall, ii, jj, dirr])

      # possibleVals = anything near that is 1 or 1000 less than the val

    for i, line in enumerate(self.board):
      for j, val in enumerate(line):
        if self.keyy(i, j) in seen:
          print("O", end="")
        else:
          print(self.board[i][j], end="")
        
      print("")

    

    return len(seen)
    

    
  def keyy(self, x, y):
    return str(x)+"-"+str(y)
  def key(self, x, y, dir):
    return str(x)+"-"+str(y)+"-"+dir
  
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

  def rotate(self, dir):
    if dir == "E" or dir == "W":
      return ("N", "S")
    else:
      return ("E", "W")

  def getMove(self, i, j, dir):
    ii, jj = i, j
    if dir == "E": jj+=1
    elif dir == "W": jj-=1
    elif dir == "N": ii-=1
    elif dir == "S": ii+=1

    if self.onBoard(ii, jj) and not self.blocked(ii, jj):
      return ii, jj
    else: return None, None

  

  def runShortestPath(self):
    # clear out shortest-steps
    self.lowestVal = dict()

    # value, i, j, direction
    toVisit = [[0, *self.find("S"), "E"]]

    while toVisit:
      value, x, y, dir=toVisit[0]
      toVisit = toVisit[1:]

      if self.blocked(x, y): continue

      key = self.key(x, y, dir)
      currentVal = self.lowestVal.get(key)
      
      if currentVal is None or value < currentVal:
        self.lowestVal[key]=value

        xx, yy = self.getMove(x, y, dir)
        if xx:
          toVisit.append([value+1, xx, yy, dir])

        for newDIr in self.rotate(dir):
          toVisit.append([value+1000, x, y, newDIr])
        
      # print(toVisit)
      # short toVisit based off of first val
      toVisit.sort(key=lambda x: x[0])

    ei, ej = self.find("E")

    minDir = self.minDir(ei, ej)

    return self.lowestVal[self.key(ei, ej, minDir)]
  
  
  def minDir(self, ei, ej):
    lowestval = 999_999_999_999
    lowestDir = None
    for dir in ["N", "S", "E", "W"]:
      key = self.key(ei, ej, dir)
      currentVal = self.lowestVal[key]
      if currentVal < lowestval:
        lowestval = currentVal
        lowestDir = dir

    return lowestDir



  
  def printBoard(self):
    for line in self.board:
      print("".join(line))


b = Board(board)


print(b.partOne())
p2 = b.partTwo()
# manual inspection of board to fix algo errors :)

print(p2 -(5+3+7))


