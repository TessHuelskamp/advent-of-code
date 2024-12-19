
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
    lowestVal = dict()

    # value, i, j, direction
    toVisit = [[0, *self.find("S"), "E"]]

    while toVisit:
      value, x, y, dir= toVisit[0]
      toVisit = toVisit[1:]

      if self.blocked(x, y): continue

      key = self.key(x, y, dir)
      currentVal = lowestVal.get(key)
      
      if currentVal is None or value < currentVal:
        lowestVal[key]=value

        xx, yy = self.getMove(x, y, dir)
        if xx:
          toVisit.append([value+1, xx, yy, dir])

        for newDIr in self.rotate(dir):
          toVisit.append([value+1000, x, y, newDIr])
        
      # print(toVisit)
      # short toVisit based off of first val
      toVisit.sort(key=lambda x: x[0])

    vals = list()
    ei, ej = self.find("E")

    for dir in ["N", "S", "E", "W"]:
      key = self.key(ei, ej, dir)
      stuff = lowestVal[key]
      if stuff : vals.append(stuff)


    return min(vals)
  
  def printBoard(self):
    for line in self.board:
      print("".join(line))


b = Board(board)


print(b.partOne())

# b.printBoard()
# print(b.partTwo())
