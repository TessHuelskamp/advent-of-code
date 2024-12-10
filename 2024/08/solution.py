import itertools

debug = False

board = []

with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  for line in f.readlines():
    board.append(list(line.strip()))


# should really be using default dict but....
def push(i, j, val):
  if val not in allNodes: allNodes[val] = []
  
  allNodes[val].append((i, j))


def inBounds(i, j):
  return 0 <= i and i<len(board) and 0<=j and j<len(board[0])

def key(i, j):
  return str(i)+"-"+str(j)

def addAntinode(i, j):
  if not inBounds(i, j): return

  antiNodes.add(key(i, j))
  antiNodesTwo.add(key(i, j))

def addAntinodeTwo(i, j):
  if not inBounds(i, j): return

  antiNodesTwo.add(key(i, j))


def printBoard():
  for i, line in enumerate(board):
    for j, val in enumerate(line):
      if key(i, j) in antiNodes:
        print("#", end="", sep="")
      else:
        print(val, end="")
    print()

  
def printBoardWithPoints(point0, point1):
  for i, line in enumerate(board):
    for j, val in enumerate(line):
      if key(i, j) in antiNodesTwo:
        print("#", end="", sep="")
      elif point0[0] ==i and point0[1] == j:
        print("A", end="")
      elif point1[0] ==i and point1[1] == j:
        print("B", end="")
      else:
        print(".", end="")

    print()

  



antiNodesTwo = set()
antiNodes = set()

allNodes = dict()

# separate out nodes
for i, line in enumerate(board):
  for j, val in enumerate(line):
    if val == ".": continue

    push(i, j, val)


def getBounds(x, y):
  diff = abs(x - y)

  if x < y:
    return x-diff, y+diff
  else:
    return x+diff, y-diff


# process each pair of matching nodes
for val, nodes in allNodes.items():
  for pair in itertools.combinations(nodes, 2):
    l, r = pair
 
    iDiff = l[0]-r[0]
    jDiff = l[1]-r[1]

    a0i = l[0]+iDiff
    a0j = l[1]+jDiff
    a0 = [a0i, a0j]

    a1i = r[0]-iDiff
    a1j = r[1]-jDiff
    a1 = [a1i, a1j]

    addAntinode(*a0)
    addAntinode(*a1)


    # add/sub the differences until we run off the board
    while inBounds(a0i, a0j):
      a0i += iDiff
      a0j += jDiff
      addAntinodeTwo(a0i, a0j)

    while inBounds(a1i, a1j):
      a1i -= iDiff
      a1j -= jDiff
      addAntinodeTwo(a1i, a1j)

    # add in the og points too
    addAntinodeTwo(*l)
    addAntinodeTwo(*r)

    # debugging :)
    # print(l, r)
    # printBoardWithPoints(l, r)
    # print()
    # antiNodesTwo = set()
    # antiNodes = set()



printBoardWithPoints([0,0], [0,1])
print(len(antiNodes))
print(len(antiNodesTwo))

# DO I need this? or does thi just work

# I = len(board)
# J = len(board[0])




    

