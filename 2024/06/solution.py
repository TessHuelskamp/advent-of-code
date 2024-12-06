debug = False


board = []

startingI, startingJ = 0, 0

with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  for line in f.readlines():
    board.append(list(line.strip()))

    if "^" in line:
      startingI = len(board)-1
      startingJ = line.find("^")




def rotateRight(dir):
  if dir == "N": return "E"
  elif dir == "E": return "S"
  elif dir == "S": return "W"
  else: return "N"


def nextSpot(i, j, dir):
  # North and south go opposite your intuition bc of how the board is read in
  if dir == "N": return i-1, j
  elif dir == "E": return i, j+1
  elif dir == "S": return i+1, j
  else: return i, j-1


def onBoard(i, j):
  return 0 <= i and i <len(board) and 0 <=j and j <len(board[0])


def key(i, j):
  return str(i)+"-"+str(j)

def keyDirection(i, j, direction):
  return key(i,j)+"-"+direction


def runRoute(startingI, startingJ, direction):
  i, j = startingI, startingJ

  visited=set()
  visitedLoop=set()

  while onBoard(i, j):

    # Exit early if we detect we've been at this spot facing the same direction
    loopKey = keyDirection(i, j, direction)
    if loopKey in visitedLoop:
      return len(visited), True
    
    visitedLoop.add(loopKey)
    visited.add(key(i, j))

    nextI, nextJ = nextSpot(i, j, direction)


    try: 
      if board[nextI][nextJ] == "#":
        direction = rotateRight(direction)
      else:
        i, j = nextI, nextJ
    except IndexError:
      i, j = nextI, nextJ

  return len(visited), False


initialDirection = "N"

partOne, _ = runRoute(startingI, startingJ, initialDirection)

print(partOne)

partTwo = 0

# This takes about 45 seconds :)
for i in range(len(board)):
  
  for j in range(len(board)):
    if board[i][j] == "#": continue

    board[i][j] = "#"

    _, loop = runRoute(startingI, startingJ, initialDirection)

    if loop: partTwo +=1


    board[i][j] = "."



print(partTwo)

    
  
                                                       




