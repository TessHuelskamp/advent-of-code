import copy
debug = ''

board = []
moves = []

rI, iJ = 0, 0

def printBoard(rI, rJ):
  for i, row in enumerate(board):
    if i == rI:
      row = copy.copy(row)
      row[rJ] = "@"
     
    print("".join(row))

def double(x):
  if x == ".":
    return ".."
  elif x == "@":
    return "@."
  elif x == "#":
    return "##"
  elif x == "O":
    return "[]"
  else:
    print("???")

with open("./input."+debug+".txt" if debug else "./input.txt", "r") as f:
  i = 0
  for line in f.readlines():
    line = line.strip()
    if line == "": continue
    
    if "#" not in line:
      moves.extend(list(line))
      continue

    doubleLine = "".join([double(x) for x in list(line)])
  
    board.append(list(doubleLine))

    if "@" in doubleLine:
      rJ = doubleLine.find("@")
      rI = i
      board[rI][rJ] = "."
      
    i+=1

def generateMoves(rI, rJ, val):
  i = 1
  while True:
    if val == "^":
      yield rI -i, rJ
    elif val == "v":
      yield rI+i, rJ
    elif val == ">":
      yield rI, rJ+i
    elif val == "<":
      yield rI, rJ-i
    else:
      print("???", val)
      break
    i+=1

def getFirstMove(rI, rJ, val):
  return next(generateMoves(rI, rJ, val))

def moveHorz(move, rI, rJ):
  # we dont have to do anything special here.
  # the boxes can "bunch up" since they're only 1 tall
  firstI, firstJ = None, None

  for i, j in generateMoves(rI, rJ, move):
    if firstI == None: firstI, firstJ = i, j

    val = board[i][j]
    
    if val == "#":
      return rI, rJ
    
    if val in "[]":
      continue

    if val == ".":
      # move the robot first.
      rI, rJ = firstI, firstJ

      # move the blocks if there were any
      # instead of moving the blocks one by one
      # we can delete the fist "." we find
      # and then add it before the start of the boxes

      # we need to handle left and right too
      # I think this should work for both but should 2x check
      if i!= firstI or j != firstJ:
        
        # print(i, j)
        # print(firstI, firstJ)
        # print(board[firstI][firstJ:j+1])
        
        del board[i][j]
        board[i].insert(firstJ, ".")
        
        # print(board[firstI][firstJ:j+1])

      return rI, rJ
  
def getPair(j, bracket):
  if bracket == "[":
    return j, j+1
  else:
    return j-1, j

    
def moveVert(move, rI, rJ):
  firstI, firstJ = getFirstMove(rI, rJ, move)
  val = board[firstI][firstJ]

  # if we get lucky, we hit a wall or empty space on the first move
  # moved into an empty space on the first trye
  if val == ".": return firstI, firstJ
  elif val == "#" : return rI, rJ

  # If we don't, we setup our "toMove" dict and start scanning each row
  toMove = dict()
  left, right = getPair(firstJ, val)
  toMove[firstI] = set()
  toMove[firstI].add(left)
  toMove[firstI].add(right)

  # print(toMove)

  direction = -1 if move == "^" else 1

  previousI = firstI
  nextI = previousI + direction
  while True:
    foundBox = False
    toMove[nextI] = set()

    for j in toMove[previousI]:
      val = board[nextI][j]
      # if we hit a wall we can exit early & return the robot val
      if val == "#":
        return rI, rJ
      elif val in "[]":
        foundBox = True
        left, right = getPair(j, val)
        toMove[nextI].add(left)
        toMove[nextI].add(right)
    
    if not foundBox:
      if len(toMove[nextI]) != 0:
        print("wtf")
        exit()
      
      # we can remove the "next" row toMove cuz its all dots
      del toMove[nextI]
      break
    else:
      # We found another box so we need to setup the next iteration
      previousI = nextI
      nextI += direction
    
  # When we break out of our loop we know we're clear to move everything "up" a spot
  keys = sorted(toMove.keys())

  # start from smallest I and work from there. In order works
  if move == "^": pass
  # start moving boxes based off of the larger numbers  
  else: keys = keys[::-1]

  if debug:
    print(keys)
    print(rI, rJ, move)
    print(toMove)

  for i in keys:
    # print(i, j)

    # row by row, starting from the "top" of the pile to move,
    # move everything "up" a row
    for j in toMove[i]:
      val = board[i][j]
      board[i+direction][j] = val
      board[i][j] = "."
      

  # return the first value the robot tried to go to
  return firstI, firstJ

  


def runMove(move, rI, rJ):
  if move in "<>":
    return moveHorz(move, rI, rJ)
  else:
    return moveVert(move, rI, rJ)



def runStuff(rI, rJ):
  if debug:
    print("Inital State:")
    printBoard(rI, rJ)

  for move in moves:
    rI, rJ = runMove(move, rI, rJ)

    if not rI:
      print('uhoh')
      break

    if debug:
      print("Move ", move)
      printBoard(rI, rJ)

runStuff(rI, rJ)


partTwo = 0

for i, line in enumerate(board):
  for j, val in enumerate(line):
    if val != "[":
      continue


    partTwo += 100*i + j


print("part 2: ", partTwo)
      

