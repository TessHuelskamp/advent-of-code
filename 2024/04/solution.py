puzzle = []

from copy import deepcopy

debug = False

with open("./input.small.txt" if debug else "./input.txt", "r") as f:
  for line in f.readlines():
  
    puzzle.append(list(line.strip()))

    
# tg the puzzle is a square
puzzleLen = len(puzzle)

def getPossibleRows(i, j):
  possible = [
    # Up and down
    [[i,j], [i+1, j], [i+2, j], [i+3, j]],
    [[i,j], [i-1, j], [i-2, j], [i-3, j]],
    # left and right
    [[i,j], [i, j+1], [i, j+2], [i, j+3]],
    [[i,j], [i, j-1], [i, j-2], [i, j-3]],
    # Front diagonals
    [[i,j], [i+1, j+1], [i+2, j+2], [i+3, j+3]],
    [[i,j], [i-1, j-1], [i-2, j-2], [i-3, j-3]],
    # back diagonals
    [[i,j], [i-1, j+1], [i-2, j+2], [i-3, j+3]],
    [[i,j], [i+1, j-1], [i+2, j-2], [i+3, j-3]],
  ]

  results = []

  for row in possible:
    if not any(pair[0] < 0 or pair[1] <0 or pair[0] >= puzzleLen or pair[1] >= puzzleLen for pair in row):
      results.append(row)

  return results


def getPossibleXs(i,j):
  if i-1 < 0 or j-1 <0 or i+1 >= puzzleLen or j+1 >= puzzleLen: return []

  return [
    [[i-1, j-1], [i,j], [i+1, j+1]],
    [[i+1, j-1], [i,j], [i-1, j+1]],
  ]


puzzleOneDupe = deepcopy(puzzle)
puzzleTwoDupe = deepcopy(puzzle)

partOne=0
partTwo = 0

for i in range(len(puzzle)):
  for j in range(len(puzzle)):
    # part 1
    rows = getPossibleRows(i, j)

    if i==9 and j==3 and debug:
      print(rows)

    for row in rows:

      word = "".join([puzzle[p[0]][p[1]] for p in row])

      if i==9 and j==3 and debug:
        print(word)

      if word == "XMAS":
        partOne +=1

        for pair in row:
          puzzleOneDupe[pair[0]][pair[1]]="."
    
    # Part 2
    possibleX = getPossibleXs(i, j)
    if possibleX:
      left, right = possibleX
   
      leftWord = "".join([puzzle[p[0]][p[1]] for p in left])
      rightWord = "".join([puzzle[p[0]][p[1]] for p in right])


      if (leftWord == "MAS" or leftWord == "SAM") and (rightWord == "MAS" or rightWord == "SAM"):
        partTwo+=1
        for pair in [*left, *right]:
          puzzleTwoDupe[pair[0]][pair[1]]="."


for i in range(len(puzzle)):
  for j in range(len(puzzle)):
    if puzzleTwoDupe[i][j] != ".":
      puzzle[i][j] = "."
    
  if debug:
    print("".join(puzzle[i]))


print(partOne)
print(partTwo)