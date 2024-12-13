debugFile = ''
debug = bool(debugFile)


board = []

with open("./input."+debugFile+".txt" if debugFile else "./input.txt", "r") as f:
  for line in f.readlines():
    board.append(list(line.strip()))


def onBoard(i, j):
  return 0 <= i and i<len(board) and 0<=j and j<len(board[0])


def possibleNeighbors(i, j):
  return [
    [i-1, j, 'N'], [i+1, j, 'S'],
    [i, j-1, 'W'], [i, j+1, 'E']
  ]

# can't use - as a delimeter bc of negatives
DELIM = "_"

def key(i, j):
  return str(i)+DELIM+str(j)

def rKey(keyStr):
  i, j = keyStr.split(DELIM)
  return int(i), int(j)

def sideKey(i, j, dir):return str(i)+DELIM+str(j)+DELIM+dir
def rSideKey(keyStr):
  i, j, dir = keyStr.split(DELIM)
  return int(i), int(j), dir


# There can be multiple section of each plant
globalVisited=set()

def totalSides(mySet):
  total = 0
  while mySet:
    total += 1
    currentSide = mySet.pop()

    i, j, dir = rSideKey(currentSide)

    # Traverse the fence to see if there are nearby fences.
    # Kick them out the set if needed
    # These should really be fns but this works so...
    if dir == "E" or dir == "W":
      step = 1
      while sideKey(i-step, j, dir) in mySet:
        mySet.remove(sideKey(i-step, j, dir))
        step+=1

      step = 1
      while sideKey(i+step, j, dir) in mySet:
        mySet.remove(sideKey(i+step, j, dir))
        step+=1
    elif dir == "N" or dir == "S":
      step = 1
      while sideKey(i, j-step, dir) in mySet:
        mySet.remove(sideKey(i, j-step, dir))
        step+=1
        
      step = 1
      while sideKey(i, j+step, dir) in mySet:
        mySet.remove(sideKey(i, j+step, dir))
        step+=1
    else:
      print('unknown dir')

  return total


def fillPlot(i, j):
  area, perimeter = 0, 0
  toVisit = {key(i,j)}
  visited = set()

  sides = set()

  plantType = board[i][j]

  while toVisit:
    myKey = toVisit.pop()
    visited.add(myKey)
    globalVisited.add(myKey)
    i, j = rKey(myKey)

    area += 1

    for neighbor in possibleNeighbors(i, j):
      ii, jj, _ = neighbor
      newKey = key(ii, jj)
      if not onBoard(ii, jj) or board[ii][jj] != plantType:
        perimeter += 1
        sides.add(sideKey(*neighbor))

      else:
        if newKey not in visited:
          toVisit.add(newKey)

  
  return area, perimeter, totalSides(sides)

partOne = 0
partTwo = 0

for i, line in enumerate(board):
  for j, val in enumerate(line):
    myKey = key(i, j)
    if myKey not in globalVisited:

      area, perimeter, sides = fillPlot(i, j)

      # if debug: print("p: ",val, area, perimeter)
      if debug: print("s: ", val, area, sides)

      partOne += area * perimeter
      partTwo += area * sides


print(partOne)
print(partTwo)


