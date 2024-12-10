debug = False

board = []

with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  for line in f.readlines():
    board.append([int(x) for x in list(line.strip())])

def onBoard(i, j):
  return 0 <= i and i<len(board) and 0<=j and j<len(board[0])

def neighbors(i, j):
  possible = [
    [i-1, j], [i+1, j],
    [i, j-1], [i, j+1]
  ]

  return [x for x in possible if onBoard(*x)]

def key(i, j):
  return str(i)+"-"+str(j)


def traverse2(i, j):
  val = board[i][j]

  if val == 9:
    return 1

  nextStep = val+1
  total = 0

  for neighbor in neighbors(i, j):
    ii, jj = neighbor
    if board[ii][jj] == nextStep:
      total += traverse2(ii, jj)

  return total

def traverse(i, j):
  val = board[i][j]

  if val == 9:
    return { key(i, j) }

  nextStep = val+1
  total = set()

  for neighbor in neighbors(i, j):
    ii, jj = neighbor
    if board[ii][jj] == nextStep:
      total |= traverse(ii, jj)

  return total
    



partOne = 0
partTwo = 0

for i, line in enumerate(board):
  for j, val in enumerate(line):
    if val != 0: continue


    score = traverse(i,j)
    partOne += len(score)

    partTwo += traverse2(i, j)


print(partOne)
print(partTwo)