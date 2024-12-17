import copy
debug = ''

board = []
board2= []
moves = []

rI, iJ = 0, 0

def printBoard(rI, rJ):
  for i, row in enumerate(board):
    if i == rI:
      row = copy.copy(row)
      row[rJ] = "@"
     
    print("".join(row))

with open("./input."+debug+".txt" if debug else "./input.txt", "r") as f:
  i = 0
  for line in f.readlines():
    line = line.strip()
    if line == "": continue

    if "@" in line:
      rI = i
      rJ = line.find("@")
    i+=1

    if "#" in line:
      board.append(list(line))
      if "@" in line:
        board[rI][rJ] = "."
    else:
      moves.extend(list(line))


    


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


def runMove(move, rI, rJ):
  firstI, firstJ = None, None
  for i, j in generateMoves(rI, rJ, move):
    if firstI == None: firstI, firstJ = i, j
    val = board[i][j]

    if val == "O":
      continue

    if val == "#":
      return rI, rJ
    
    if val == ".":
      # move the robot
      rI, rJ = firstI, firstJ


      # move the blocks if there were any
      if i != firstI or j !=firstJ:
        # if the robot pushes a stack of blocks,
        # We only need to put the first block in the last spot
        board[i][j] = "O"
        board[firstI][firstJ] = "."

      return rI, rJ



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


partOne = 0

for i, line in enumerate(board):
  for j, val in enumerate(line):
    if val == "O":
      partOne += 100*i + j


print('partOne: ', partOne)
      

